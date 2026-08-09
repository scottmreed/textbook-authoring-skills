---
name: question-hint-authoring
description: Author progressive hint ladders for ChemIllusion question types (demo fixtures, question-bank items, LMS tutorial questions). Use when adding, reviewing, or debugging hints, when a question type needs hint coverage, or when choosing which hint kind (text, structure, highlight, projection label, region focus, animation) fits a question type.
---

# Question Hint Authoring

> Figures are a separate contract: if the *question itself* references
> structures/reactions the student can't see, fix that first via
> [question-figure-authoring](../question-figure-authoring/SKILL.md) — hints
> must never be the only place a required figure appears. Post-answer
> wrong-answer explanations are a third, separate contract — see
> [question-explanation-authoring](../question-explanation-authoring/SKILL.md).

One hint system for every question type — a **progressive ladder** of typed
hints, server-gated, displayed by one shared panel in both the demo gallery
(`/question-types/{slug}`) and the LMS activity shell.

Canonical hint model, validation, profiles, serving, and UI panel: proprietary
hint subsystem (not in this repo).

## The ladder contract

- Hints form a ladder `level: 1..n` with **no gaps**. Follow the reasoning PRD
 §13.1 progression: orient → constraint → feature → reasoning prompt →
 (optionally) worked step. Early rungs narrow attention; only the final rung
 may approach a worked example.
- **Server-gated**: hints are never shipped in student payloads. Clients see a
 `hintCount` and request one rung at a time
 (demo and LTI hint endpoints, not in this repo), so "hints used" is meaningful
 and later rungs stay unseen.
- **Never name the answer**: no answer option ids, correct orderings, key
 values, or the word "correct" pointing at a choice. A hint narrows the
 search; the student still does the step.
- **Few-option rule (≤2 options/categories)**: for a binary categorize, a
 two-option select, or any question whose option space is 2, no hint rung may
 name a group/option — naming one collapses the entire remaining space. Point
 at the discriminating *criterion* instead ("compare the charge and lone
 pairs"), never the verdict. The demo guard for this lives on the explanation
 side (`test_question_wrong_answer_explanations.py::TestFewOptionFeedbackDoesNotNameTheAnswer`);
 hold hints to the same bar.
- **Name the unit on numeric hints**: a `numeric_with_units` hint that restates
 the formula or a worked step must state the expected unit (Hz, ppm, equiv,
 kcal/mol…). The field now shows a unit adornment; the hint should reinforce
 it, not drop it.
- **Never render an option's exact structure**: for choice-based types, a
 hint's `structure_smiles` must not canonically match any answer option's
 `structure_smiles` — even without naming the answer in text, showing the
 identical structure of one of the visible choices IS the answer. Use a
 different (but pedagogically similar) molecule instead, e.g. methanol to
 illustrate a hydroxyl when ethanol is one of the choices. Guarded by
 `hints.hint_reveals_option_structure` + `hints.collect_option_structure_smiles`,
 tested for every demo fixture with `hints` in
 `test_question_hints.py::TestHintsNeverRevealOptionStructures`.
- Every hint requires accessible `text`, whatever richer media it carries.

## Where hints live

| Surface | Location |
|---|---|
| Demo fixtures | top-level `"hints"` key in `question_types/demos.py` or `reasoning_templates/demos.py` (server-side only) |
| Question-bank items | `feedback_bundle.hints` (author-side column, never served) |
| LMS tutorial questions | `TutorialQuestion.feedback_bundle["hints"]` |

## Hint shape (see `Hint` in hints.py)

```json
{"level": 2, "kind": "structure_highlight",
 "text": "The C=O of acetone, highlighted.",
 "structure_smiles": "CC(=O)C",
 "highlight_atoms": [1, 2], "highlight_bonds": [[1, 2]],
 "caption": "optional", "target_ids": [], "asset_url": null,
 "projection": null, "part_id": null}
```

Kinds: `text`, `structure` (SMILES → server-rendered image),
`structure_highlight` (highlights baked into the SVG server-side),
`projection` (semantic state + display labels, e.g. a Haworth with the
anomeric carbon labeled), `region_focus` (semantic workspace ids to look at),
`animation` (existing asset URL), `worked_step` (final rungs only).
`part_id` scopes a hint to one part of a composite episode.

## Which hint kinds help which type

Mirror of `HINT_KIND_PROFILES` (keep the two in sync):

| Type | Best hint kinds | Example |
|---|---|---|
| single_select / multi_select | text → structure / structure_highlight | show a reference molecule with the deciding group highlighted |
| short_answer | text, structure | show the parent structure of the name being asked |
| numeric_with_units | text, worked_step | restate the formula, then one substituted step |
| rank_order | text, structure | compare just two adjacent items |
| matching_pairs / categorize_groups | text, structure_highlight | highlight the feature that decides one pairing |
| molecular_geometry | text | direct attention to domain counting or the labeled angle pattern — the diagram already shows the shape |
| hotspot | structure_highlight, region_focus | narrow to two candidate atoms before highlighting |
| curved_arrow | region_focus, structure_highlight, animation | point at the electron source; animate the push last |
| structure_scaffold | structure, text, worked_step | show a smaller analog (e.g. methanol for ethanol) |
| newman / chair / fischer | projection | labeled positions ("CH3 here, CH3 directly opposite") |
| haworth | projection, structure | **Haworth with a label** — flag the anomeric carbon (C1) |
| synthesis_route | text, structure, worked_step | reveal the intermediate's structure, not the reagent |
| comparison_matrix | text, structure_highlight | highlight the feature for ONE row |
| evidence_board / structured_reasoning / walkthrough | text | reframe the evidence or claim |
| bond_change_ledger | structure_highlight, text | highlight the bond that changes |
| reaction_coordinate_reasoning | region_focus, animation, text | name the two peaks to compare (`ts_1`, `ts_2`) |
| error_repair | region_focus, structure_highlight | point at the flawed element before classifying it |
| composite_episode | text/structure/region_focus with `part_id` | one hint per stuck-point, scoped to its step |
| spectrum_peaks | region_focus, text | narrow to a spectral region without naming the band |
| molecular_vibration | region_focus, text | point at the mode/region, not the frequency answer |
| nmr_equivalence_partition / nmr_spin_system_builder | structure_highlight, text | highlight one environment's atoms; never state the full grouping |
| nmr_multiplet_builder | text, worked_step | restate n+1 with the unit (Hz), one step at a time |
| nmr_decoupling_experiment / nmr_integral_reconstruction | region_focus, text | focus the affected signal / region without the answer |
| nmr_dynamic_explorer | region_focus, animation, text | point at coalescence behavior, not the labeled regimes |

## Workflow

1. Pick 2–3 rungs using the table; write ladder JSON (levels 1..n).
2. Demo fixture: add `"hints"` to the fixture. Bank/LMS question: put the list
 in `feedback_bundle.hints`.
3. Validate: `parse_hints` runs in tests — the proprietary hint validator
 (not in this repo) auto-covers every demo ladder (level gaps, required text,
 no answer-id leakage). Run it.
4. Preview: the demo page shows the Hint button when `hintCount > 0`; the LMS
 shell shows it via the tool rail (`requestHint`, visible in practice mode).

## Display guarantees (HintPanel)

Revealed rungs stack; structures arrive as server-rendered SVG data URIs
(highlights already baked in); projection hints render their label list;
region-focus hints render target chips; animations render as inline video.
Do not build per-type hint UI — extend `HintPanel` if a new display kind is
ever needed.
