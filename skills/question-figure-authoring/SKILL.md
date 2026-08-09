---
name: question-figure-authoring
description: Ensure every ChemIllusion question (demo fixtures, reasoning-template episodes, question-bank items) ships the figures a student needs to answer it. Use when authoring or reviewing question fixtures, when a demo page looks text-only but references structures/reactions/spectra, or when adding a new question type or reasoning template.
---

# Question Figure Authoring

**The rule: if the prompt asks the student to reason about something chemical,
the student must be able to see it.** "Audit the hydroxide-plus-acetone step"
with no depiction of the step is unanswerable; "compare acetate and ethoxide"
without either structure forces recall instead of reasoning.

Origin: on 2026-07-19 three reasoning-template demos shipped without figures
(`electron_accounting`, `confidence_reconsideration`, `candidate_elimination`),
and two type demos (`comparison_matrix`, `evidence_board`) *had* SMILES that the
enricher silently ignored because their list keys weren't registered. Both
failure modes are now guarded by the proprietary visual-enrichment registry
(not in this repo).

## How figures work (nobody hand-draws anything)

The proprietary visual-enrichment service (not in this repo) renders figures
server-side from SMILES at payload time. Authors only add data:

| You write | Where | Student receives |
|---|---|---|
| `"molecule_smiles": "CC(=O)C"` | top level of a `student_config` | `molecule` = interactive SVG with per-atom targets (hotspot/arrow workspaces; also shown as the reference figure by BondChangeLedgerRenderer) |
| `"structure_smiles": "CCO"` | entries of `options`, `items`, `left`, `right`, `cards`, `reagents`, `intermediates`, `cases`, `candidates`, `evidence` — and options nested in structured-reasoning `fields` | `imageUrl` SVG data URI on that entry |
| `structure_smiles` on `shared_stimulus.structures` entries | composite/reasoning episodes | rendered stimulus strip above the parts |
| `spectrum` peak data / `profile` control points | spectrum + energy-diagram types | the workspace draws the figure from data |
| `"smiles": "CCO"` inside `nmr_asset.molecule` | interactive-NMR builders (`nmr_equivalence_partition`, `nmr_spin_system_builder`) | enricher fills `nmr_asset.molecule.svgDataUri`; renderer shows the structure above the workspace |
| `"trace_url"` / `"grid_url"` at the **top level** of `student_config` | `nmr_integral_reconstruction` / `nmr_dynamic_explorer` | workspace fetches the approved proprietary NMR spectrum assets (not in this repo) and draws the spectrum |

### Interactive NMR figures — the two traps that broke three demos (2026-07-22)

1. **Spectrum asset URLs live at the top level, never inside `nmr_asset`.**
 `useNmrAsset` reads `trace_url`/`grid_url`/`asset_url` from the top of
 `student_config`. A URL nested inside `nmr_asset` (with no full inline
 payload) yields "The spectra could not be loaded" — the loader treats the
 stub as complete and never fetches. The hook now also tolerates the nested
 form, but **author the URL at the top level.** Only put a full
 `nmr_asset` inline when it carries the whole payload (multiplet/decoupling/
 spin-system builders, which draw from `available_partners`/`public_groups`/
 `molecule.atoms` — no external asset).
2. **A `molecule.atoms` list is data, not a picture.** The equivalence and
 spin-system builders render a *structure* only because the enricher turns
 `nmr_asset.molecule.smiles` into `svgDataUri`. Always give those types a
 `smiles`; the atom list alone shows a table with no structure.

**If you add a new list key holding structure-bearing entries, register it in
`visual_enrichment.py` — otherwise your SMILES silently render nothing.** That
was the comparison-matrix/evidence-board bug.

## Decision checklist per question

1. **Does the prompt name a specific species, reaction, spectrum, or diagram?**
 → it needs a figure. Named-with-formula text ("hydroxide (OH-)") is
 acceptable only for genuinely formula-level tasks.
2. **Is the workspace itself the figure?** Editor types (newman, chair,
 fischer, haworth, structure_scaffold) need no extra figure *unless* the task
 is a translation — then show the source representation in the stimulus
 (e.g. butane skeletal → "build the Newman").
3. **Composite episodes**: anything all parts share belongs in
 `shared_stimulus.structures` (+ `source_text` for the proposed step/arrow
 narrative being audited). Part-specific structures go on that part's
 entries.
4. **Symmetry**: if one option has `structure_smiles`, its siblings must too —
 a lone image can leak the answer. Verify every SMILES parses
 (`Chem.MolFromSmiles`); enrichment fails *silently* on bad SMILES, which
 recreates the asymmetry.
5. **Never answer-bearing**: figures come from student-safe config only. No
 `is_correct`, no answer keys, no hint imagery in the initial payload
 (hints have their own ladder — see [question-hint-authoring](../question-hint-authoring/SKILL.md)).

## The audit (run after adding/editing fixtures)

```bash
# proprietary toolchain (not in this repo)
python -m pytest tests/unit/test_services/test_demo_visual_coverage.py -q
```

The test walks every demo (`question_demo_service.list_demos()` = 25 type
demos + all reasoning-template episodes) and fails on any non-exempt demo with
no visual. Exemptions live in the test (`TEXT_ANSWERABLE`,
`WORKSPACE_IS_FIGURE`) — add to them only with a stated reason, never to make
a structure-referencing question pass. `WORKSPACE_IS_FIGURE` now also lists
`nmr_multiplet_builder` and `nmr_decoupling_experiment` (they draw from inline
data, no structure/asset). The equivalence, spin-system, integral, and dynamic
NMR types are intentionally left un-exempt so the audit keeps checking they ship
their `molecule` / `trace_url` / `grid_url` figure — which is exactly what
regressed on 2026-07-22.

## Frontend support (already built — don't duplicate)

`SelectedResponseRenderer`, `StructuredReasoningRenderer`,
`ComparisonMatrixRenderer`, `EvidenceCandidateBoardRenderer`,
`CompositeEpisodeRenderer` (stimulus strip), `BondChangeLedgerRenderer`
(reference figure), `HotspotActivityRenderer` all display enriched visuals. If
you add a renderer with structure-bearing entries, render `imageUrl`/`molecule`
from day one.

## Related

- [question-hint-authoring](../question-hint-authoring/SKILL.md) — hint ladders (server-gated, separate from figures)
- proprietary demo fixture catalogs (not in this repo) — the fixture catalogs
- proprietary demo visual-coverage test (not in this repo) — the executable audit
