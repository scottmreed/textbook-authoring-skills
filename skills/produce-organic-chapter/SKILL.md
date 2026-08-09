---
name: produce-organic-chapter
description: End-to-end orchestrator for producing one complete organic chemistry chapter — reader prose, concepts, figures, videos, question sets, and LMS packaging. Use when asked to produce, build out, or complete a chapter, or to add a question set to an existing chapter. Runs the full pipeline and reports against a Definition of Done.
---

# Produce One Organic Chapter

**Type:** Orchestration skill (chapter production pipeline) — **CANONICAL**.
This is the single entry point for adding, producing, modernizing, or completing
a chapter. `add-organic-chapter` was a deprecated redirect stub to this skill;
`author-organic-topic-package` is step 2 of this pipeline, not an alternative.
**Last verified against main:** 2026-07-24
**Implementation alignment (ChemIllusion repo):** Infrastructure complete —
`question_sets[]` in the topic-package schema, chapter/concept linkage on
`question_bank_items`, `seed_question_sets.py`, Deep Linking `question_set`
entries, and the public sampler endpoint all exist. Content for each chapter is
produced by running this skill. The end-of-run handoff now explicitly offers the
separate `review-organic-chapter` QA/correction pass and points to the durable
chapter-review tally.

Canonical PRD: proprietary documentation (not in this repo).
Canonical SOP: proprietary documentation (not in this repo).

## When to use

- "Produce chapter 9" / "build out the alkynes chapter" / "do the next chapter"
- "Add a question set to the alkenes chapter"
- Any request to take a chapter from nothing (or from a legacy deck) to
 LMS-deliverable.

Do **not** use for: adding a new question *type* (proprietary scaffold, not in this repo),
adding a new textbook *lens* (product catalog work, out of scope for this repo), or
editing a single figure (use the figure authoring skills directly).

## Before you start — confirm three things

1. **Which chapter.** Get both identifiers; they differ and both are needed:
 - reader slug (e.g. `alkynes-organic-synthesis`) from the proprietary reader catalog (not in this repo)
 - deck `chapter_id` (e.g. `alkynes-structure-and-reactions`) from proprietary deck assets (not in this repo)
 The deck `chapter_id` is what goes in `question_bank_items.chapter_id`.
2. **Full package or shim.** A chapter with an existing legacy deck may take a
 shim package (concepts + question_sets only, deck referenced not recompiled).
 A chapter with no deck takes a full package. **Never recompile over a legacy
 deck without explicit permission** — a separate pptx tool owns those.
3. **Scope.** Default target is 1–2 questions per *suitable* type (PRD §5), not
 every type. Confirm before authoring dozens of questions.

## The loop

Work through these in order. Each step has a check you can actually run.

### 1. Audit what exists

```bash
# proprietary assets (not in this repo)
```

Then invoke `organic-chapter-asset-auditor` for figure gaps.

### 2. Author or extend the topic package

Invoke `author-organic-topic-package`. It owns the topic-package JSON
(proprietary assets, not in this repo).

Required sections: `concepts[]`, `nuggets[]` (all three text tiers plus
`practice_check`), `assets[]`, `video_briefs[]`, `textbook_matching`
(**mcmurry and loudon5e minimum**), and `question_sets[]`.

If source decks are being consulted, use `ingest-deck-json-to-nuggets` first —
source material is private evidence written to
`reports/topic-packages/<topic-id>/source-evidence/`. Published prose is authored
fresh. Source brand names in learner-facing text fail compilation by design.

### 3. Figures and accessibility

For each asset the auditor flagged, use the matching authoring skill:
`newman-projection-authoring`, `reaction-coordinate-diagram-authoring`,
`conformational-energy-profile-authoring`, `orbital-overlay-assets`.

Then `chem-representation-accessibility` for every figure. `alt_text` is
required — the compiler rejects assets without it.

Every figure that ships a hosted `image_url` also needs a `generation` block
naming the tool that drew it (method, tool, provider,
`ai_regeneration_allowed`); the compiler rejects it without one. An `ai_image`
figure must additionally store the verbatim `prompt` and set
`ai_regeneration_allowed: true` — which is only ever legitimate for pure
schematic illustration, never for structures, mechanisms, monomer sequences, or
quantitative plots. Full field reference in `author-organic-topic-package`
§"Figure provenance". Regenerate the inventory afterwards with the proprietary
asset-report script (not in this repo).

### 4. Videos

One video per `video_brief`, via `molecule-video-creator`. If deferring, record
the deferral in the package rather than dropping the brief silently.

### 5. Question set — SELECT TYPES, THEN AUTHOR REAL QUESTIONS

This step is load-bearing and the one most often left half-done: **naming question
types is not producing homework.** A chapter is not complete until it has one or
more concrete, validated questions per selected type, each tied to a concept the
chapter's text actually teaches. Do not stop at listing types.

**5a. Enumerate the released types.** They are the only legal `question_type`
values (validated against the backend registry at compile — an unknown slug or a
malformed `answer_key` fails the build):

```bash
# proprietary function (not in this repo)
```

**5b. Select types by concept kind** (PRD §5.2 — do not force all 25; pick the
ones the chemistry supports):

| Concept kind in the chapter | Well-suited question types |
| --- | --- |
| Recall / identify (functional group, hybridization, valence) | `single_select`, `short_answer`, `categorize_groups` |
| Compare / choose several | `multi_select`, `comparison_matrix` |
| Rank (stability, acidity, priority) | `rank_order` |
| Mechanism / electron flow | `curved_arrow`, `bond_change_ledger`, `error_repair` |
| Energy profile reasoning | `reaction_coordinate_reasoning` |
| Structure drawing / conversion | `structure_scaffold`, `newman`, `chair`, `fischer`, `haworth` |
| Spectroscopy | `peak_assignment`, `spectrum_peaks` |
| Numeric with a unit (J in Hz, shift in ppm, equivalents, kcal/mol) | `numeric_with_units` — set `student_config.units`/`unit_hint` and `answer_key.unit`+`tolerance` |
| Dimensionless count (isomer count, degrees of unsaturation) | `numeric_with_units` with **no** unit (a bare count is legitimately unitless) |
| Multi-step reasoning | `structured_reasoning`, `walkthrough`, `synthesis_route`, `composite_episode` |

Aim for **1–2 questions per suitable type** spread across the chapter's concepts —
not every type, and not all on one concept.

**5c. Author each question against the type's real schema.** Copy the exact
`student_config` / `answer_key` shape from that type's demo, then substitute
chapter chemistry:

```bash
# proprietary function (not in this repo)
```

Each `question_sets[]` entry:

```jsonc
{
 "slug": "ch1-sp-hybridized-carbon",
 "question_type": "single_select", // a released registry slug
 "concept_slug": "sp-hybridization", // a concept in THIS package
 "difficulty": "standard", // core | standard | advanced — nothing else
 "prompt_text": "Which molecule contains sp-hybridized carbon atoms?",
 "student_config": { "options": [ /* shape copied from the demo */ ] },
 "answer_key": { "correct_option_ids": ["c"] },
 "feedback_bundle": { /* wrong-answer explanations + hints (see below) */ },
 "accessibility_bundle": {"accessible_description": "..."},
 "demo_eligible": false // true only on the designated demo chapter
}
```

Enrich each question with the dedicated skills — these are part of authoring the
question, not optional polish:
- **`question-figure-authoring`** — add `structure_smiles` to options / a stimulus
 figure so the question is answerable from what is shown.
- **`question-explanation-authoring`** — `feedback_bundle.wrong_answer_explanations`
 + a specific `generic_incorrect_explanation` (never a bare "Not quite").
- **`question-hint-authoring`** — a progressive `feedback_bundle.hints` ladder.

**Question authoring guardrails** (enforced at compile / test time — author to
them the first time rather than fixing rejections):
- **`difficulty` is `core` | `standard` | `advanced`.** The `DIFFICULTIES` enum in the proprietary compile validator (not in this repo) is the authority; anything else
 (`intro`, `challenge`) fails the compile.
- **Wrong-answer `match` patterns are matched against the SUBMISSION, not the
 answer key.** `explanations._pattern_matches` subset-matches the student's
 submitted dict, so a pattern like `{"option_id": "d"}` can never fire — use
 the submission shape (`{"selected_option_ids": [...]}`, `{"assignments":
 {...}}`, `{"pairs": {...}}`, `{"ordered_ids": [...]}`, `{"cells": {...}}`).
 Several chapters up to ch25 carry the unreachable form.
- **Verify an answer key by grading the ideal SUBMISSION, not the key itself.**
 Graders read a different shape from the one keys are authored in
 (`correct_assignments` → `{"assignments": ...}`, `expected_rows` →
 `{"rows": ...}`, …), so feeding the key back reports a false failure — the
 registry's own demos "fail" that way too. Grader-to-key mappings live in the proprietary question-type registry (not in this repo).
- **`curved_arrow` cannot take a bond as an arrow endpoint.** The renderer
 emits a single site index while `mechanism_state._normalize_endpoint`
 requires two for `kind: "bond"`, so a bond endpoint is un-gradeable — author
 lone-pair-to-atom arrows.
- **Units on numeric questions.** A dimensioned `numeric_with_units` question
 must set `student_config.units` (a list when the student picks the unit) or
 `student_config.unit_hint` (a single fixed unit shown as an adornment) **and**
 `answer_key.unit` + `answer_key.tolerance`. Course units (`Hz`, `ppm`,
 `equiv`, plus SI) grade via the platform's numeric-grading service (not in this repo). Leave a genuine count
 unitless — don't invent a unit for degrees of unsaturation.
- **Answer-neutral accessibility.** `accessibility_bundle.accessible_description`
 describes the stimulus and the task, never the answer (verdict, values, or the
 grouping to produce). `validate_question_sets` runs `find_accessibility_leaks`
 and **fails the compile** on a leak. See
 [chem-representation-accessibility](../chem-representation-accessibility/SKILL.md#question-accessibility-text-never-reveals-the-answer).
- **Few-option feedback teaches the criterion.** For a ≤2-group `categorize_groups`
 or a two-option select, `wrong_answer_explanations` and the generic fallback
 must not name the correct group/option (it collapses the space) — teach the
 discriminating criterion. See
 [question-explanation-authoring](../question-explanation-authoring/SKILL.md).
- **Unicode chemistry labels.** `categorize_groups`/`matching_pairs` item and
 group text render as plain text (native `<option>` can't show markup), so
 store normalized Unicode (`R₃C⁺`, `OH⁻`, `H₂O`) — the
 `ensure_chemistry_display_text` form. Keep mechanism names plain (`SN2`, `E1`),
 which the normalizer would otherwise subscript.
- **Typed structure entry on drawing questions.** Every `structure_scaffold` /
 `draw_intermediate` question **must** set `student_config.typed_structure_entry`
 to `"allowed"` or `"blocked"`; the compile fails without it, because a
 pointer-only canvas is an access barrier and the decision has to be deliberate.
 Ask one question: **is drawing the skill being assessed, or just the input
 method?**
 - `"allowed"` when the *chemistry* is what's tested — "draw the major
 product", "draw the intermediate", "draw the alcohol released". A student who
 types the right structure has demonstrated exactly what the item asks. This
 is the large majority; 62 of the corpus's 66 drawing items are `allowed`.
 - `"blocked"` only when the *act of drawing* is the assessed skill — wedge and
 dash notation, chair or Newman geometry, translating a condensed formula
 into a drawn structure. Add a `typed_structure_entry_note` saying why, in
 words a student will read: that note is what a learner who cannot use a
 mouse sees instead of the field.

 A blocked item is accessibility debt, not a neutral choice. The concept it
 sits on must still carry **at least one keyboard-reachable question of any
 type** — a select, a ranking, a short answer, a Fischer or chair builder, or
 an `"allowed"` drawing item — or that concept becomes unassessable for
 keyboard-only students, which is the standing `access-001` finding across
 ch1/11/15–19/23/25–28. (Blocking every drawing item on a concept is fine when
 other question types cover it; ch5's `r-s-configuration` blocks its drawing
 item and is still reachable through `rank_order`, `short_answer` and
 `fischer`.) When `"allowed"`, the `answer_key` must carry a `smiles` or
 `molfile`; a typed answer cannot be graded against a KET-only key, and the
 validator rejects that combination.

**5d. Author TWO variants of every question; surface one.** Each surfaced
question gets one pre-authored alternate with **different chemistry** (a
different molecule, ranking set, or asked-for property — not a shuffle; the
runtime `question_variant_service` already does presentation shuffles). The
alternate carries `"variant_of": "<parent slug>"` and:

- must keep the parent's `question_type` and `concept_slug`, and cannot be
 `demo_eligible` (validated at compile);
- seeds as a **draft** bank item linked to its parent
 (`parent_item_id` / `variant_group_id`, provenance
 `source_kind: "pre_authored_variant"`) — never published, so it does not
 appear in the default HW set;
- feeds the **shipped** paid "create practice problems" runtime: when a
 student exhausts the fixed remediation pool, the LTI
 `request-variant?mode=ai` fallback serves staged variants instantly and —
 for paid/licensed contexts behind a feature flag (not in this repo) — falls
 back to live Claude Sonnet 5 generation
 (proprietary variant-generation service, not in this repo; drafts with
 `source_kind: "ai_variant"`). Teachers can also pre-generate with
 `strategy: "ai"` on the question-bank-item variants endpoint (not in this repo).

Slug convention: `<parent-slug>-v2`. The compile report shows
`surfaced` vs `staged_variants`; both should equal the intended question count.

**5e. Validate before moving on.** Compiling (step 8) runs
`validate_question_sets` against the live registry. Iterate until zero errors; a
question that references a `concept_slug` not in the package, a malformed
answer key, or an invalid `variant_of` fails the build here rather than
silently at seed time.

**5f. Reader homework preview exposure.** The end-of-chapter "Chapter homework
preview" panel on `/reader/organic/<slug>` (homework preview UI, not in this repo, teacher-preview/admin gated) shows **every published
item** of the chapter's system-managed bank, in `display_order` — there is no
per-chapter curation field and no inline-in-prose placement. Author the set so
this surface reads well:

- **6–10 surfaced questions spanning ≥5 question types**, with every major
 concept of the chapter covered by at least one question. A chapter whose
 panel shows 4 look-alike selects reads as unfinished (the ch1–6 expansion of
 2026-07-28 set this baseline).
- **Order the `question_sets[]` array to walk the chapter**: sort parents by
 the package's concept order (list order = `display_order` = panel order),
 each parent followed by its `-v2` variant.
- **Avoid stimulus-workspace + select-answer types here** (`molecular_geometry`,
 `molecular_vibration`): the question-set panel (not in this repo) renders the workspace OR the
 answer panel, never both, so those questions are unanswerable in this panel.
- **The panel reads the DB, not the package.** Nothing appears (or updates)
 until step 9's seed runs. Staged `-v2` variants stay drafts and never show.

### 6. Coherence pass — one loop back through every category

**Run this exactly once, after steps 2–5 are drafted and before compiling.**
Producing the categories in order means each one was authored without knowing
what the later ones would need. The homework you wrote in step 5 is the first
time you learned what the chapter actually demands of a student; the figures in
step 3 were chosen before that existed. This pass is where that knowledge flows
backwards. It is not a proofread — you are looking for *changes one category
forces on another*, and you may **add, edit, or delete** in any of them.

Do not skip a category because "nothing changed." Answer the question for each,
in writing, in the reconciliation note below.

Walk the categories in this order (later-authored → earlier-authored, so the
newest information propagates first):

| Now that this exists… | …re-examine | Ask |
| --- | --- | --- |
| **Question sets** (5) | nuggets, figures, videos, concepts | Does every question test something the prose actually teaches, at the depth it's asked? If a question needs a step the text hand-waves, **deepen the nugget or add a figure** — don't soften the question. Does any question need a figure that doesn't exist yet? |
| **Question sets** (5) | deck / reader slides | Is there a slide that prepares students for each question type used? A `curved_arrow` or `rank_order` question with no worked example anywhere upstream is the classic gap — **add the slide/nugget**, don't drop the question. |
| **Videos** (4) | nuggets, figures | Does a video now cover something the prose spends a paragraph on redundantly, or vice versa? Trim the duplicate; keep the better medium for that content. |
| **Figures** (3) | nuggets, question sets | Is any figure now unreferenced by any nugget or question? Either cite it or **delete it** — orphan assets inflate the package and the review queue. Conversely, is any nugget describing a spatial/energetic idea in words that a figure should carry? |
| **Concepts** (2) | everything | Is there a concept with no nugget, no figure, and no question? Either give it content or remove it — a concept node with no evidence path breaks mastery gating in the homework creator. Is there a question or figure whose real subject has **no** concept node? Add the node. |
| **Textbook crosswalks** (2) | final concept list | Did concepts get added or removed above? Re-check mcmurry + loudon5e mappings still cover the final list. |

Two hard rules:

- **One pass only.** Apply what this pass surfaces, then move to compile. If
 applying a change makes you want to re-audit everything again, note it under
 "deferred" in the reconciliation note and stop. Endless polish loops are the
 failure mode this step is bounded to prevent.
- **Deletions need a reason recorded.** Anything removed here gets a line in the
 note saying what replaced it or why it was redundant.

On a **shim package over a legacy deck**, this pass will often conclude "the deck
needs a slide." Legacy decks are frozen — do not edit one. Record the slide need
under "deferred" with the question that motivated it, and cover the gap in a
nugget instead. Escalate for permission only if the question is unanswerable
without the slide.

Write the outcome to
`reports/topic-packages/<topic-id>/coherence-pass.md`:

```markdown
# Coherence pass — <topic-id>
Date: YYYY-MM-DD

## Questions → text/figures
- <change made, or "no change: <why you're confident">>
## Questions → deck/reader
## Videos → text
## Figures → text/questions
## Concepts → whole package
## Crosswalks

## Deferred (not applied this pass)
## Deletions (what + why)
```

The note is a deliverable — the Definition of Done checks for it.

### 7. Additional Reading — link 1–6 specific OpenStax sections

The chapter text is deliberately short. The reader's **Additional Reading** panel
must therefore tell a student exactly where to go for the depth the chapter
skipped — which means links to *specific sections*, not to a chapter landing
page. `https://openstax.org/books/organic-chemistry/pages/20-why-this-chapter`
tells a reader nothing;
`https://openstax.org/books/organic-chemistry/pages/4-2-cis-trans-isomerism-in-cycloalkanes`
tells them precisely what they will get.

Author these entries in the proprietary McMurry section-links map (not in this
repo) — the `MCMURRY_SECTIONS` table keyed by **reader slug** (not topic id). They render in
the Additional Reading list with the same link treatment as the Wikipedia
targets, via `WikiSnapshotRenderer`.

```ts
"carboxylic-acids-and-nitriles": [
 os(
 "20-3-biological-acids-and-the-henderson-hasselbalch-equation",
 "§20.3 — Biological acids and the Henderson–Hasselbalch equation",
 "Calculates the ionized fraction at physiological pH — the quantitative step the chapter leaves out.",
 ),
],
```

**Choosing the links.** Pick **1–6**, and pick them *against the concept list you
just finished*: a section earns a place only if it develops something the
chapter's nuggets do not. Good candidates are the derivation behind a result the
chapter asserts, a reaction or reagent outside the chapter's set, a biological or
industrial application, and the spectroscopy section when the chapter treats
spectroscopy briefly. Do not link a section that merely restates a nugget.

**Writing the context sentence.** One sentence, naming what the section adds
*relative to this chapter* — "Adds the Baeyer–Villiger oxidation of ketones to
the chapter's aldehyde oxidation," not "Covers oxidation of aldehydes and
ketones." A sentence that would read the same for any textbook is not doing the
job.

**Verify every URL before committing.** A wrong slug returns HTTP 404, so this is
mechanical — never ship an unverified link:

```bash
python3 - <<'EOF'
import re, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
src = '…'.read()
block = src.split('const MCMURRY_SECTIONS', 1)[1].split('export const ORGANIC_TEXTBOOK_CHAPTERS', 1)[0]
slugs = re.findall(r'os\(\s*"([^"]+)"', block)
BASE = "https://openstax.org/books/organic-chemistry/pages/"
def check(s):
 try:
 req = urllib.request.Request(BASE + s, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
 with urllib.request.urlopen(req, timeout=25) as r: return (r.status, s)
 except urllib.error.HTTPError as e: return (e.code, s)
with ThreadPoolExecutor(max_workers=10) as ex: res = list(ex.map(check, slugs))
bad = [x for x in res if x[0] != 200]
print(f"{len(res) - len(bad)}/{len(res)} OK"); [print("FAIL", *x) for x in bad]
EOF
```

Section *numbering* is the usual failure: the OpenStax edition sometimes merges
or splits sections relative to the print McMurry, so a remembered number can be
off by one. Adjust the number and re-verify rather than dropping the link.

Then add the chapter's reader slug to `CHAPTERS_WITH_TOPIC_PACKAGES` in the proprietary reader catalog (not in this repo), which enforces the
1–6 count, the `§N.M — Title` label form, a non-stub context sentence, no
`why-this-chapter` links, and that each link's chapter number matches the
chapter it sits under.

### 8. Compile

```bash
# proprietary function (not in this repo)
```

Emits deck, reader chapter, LMS module, review manifest, textbook profiles, and —
when `question_sets[]` is present — the compiled question-set artifact (all
proprietary assets, not in this repo).

The compiled reader chapter is the **canonical textbook prose for two surfaces**:
`/reader/organic/<slug>` and the Deck Creator Teaching-Package Textbook tab
(rendered via `CanonicalTextbookView` → `TopicPackageChapterRenderer`, bridged
from the deck chapter id through the catalog + chapter crosswalk). There is no
separate textbook authoring for the deck — never write textbook prose into
the platform's teaching-package build fixtures (not in this repo).

**The compiled question-set artifact holds answer keys and must never be checked
into the public reader asset tree (proprietary assets, not in this repo).**

#### The compiled reader is a BUILD OUTPUT — never hand-edit it

The reader chapter JSON is regenerated from the package on every compile.
**A correction written there is deleted by the next compile.** This is not
hypothetical: two historical commits (refs not in this repo) fixed tier-1 chemistry,
invalid energy-diagram barriers, and 77 dead links across ~25 chapters *in the
artifacts only*. Ch6's fixes were then reverted by a recompile, reapplied, and
reverted again — it spent weeks live with six 404 links and a flat energy
diagram. Ch7 read correctly while its package still encoded the wrong energetics.

So: **fix the topic package, then compile.** If something appears fixable only
in the artifact, that is a compiler gap to report, not a file to edit.

Before recompiling any chapter that already has an artifact, diff the two:

```bash
# proprietary assets (not in this repo)
```

Classify every difference in `external_link` urls, `reaction_coordinate`
`spec.steps`, and text blocks before you compile.

Two authoring omissions cause this drift repeatedly:

- **Author `wikipedia_title` on every concept.** Unauthored, `_concept_wiki_title`
 falls back to the concept's prose title and mints Wikipedia article names that
 never existed — six 404s in ch6, and ch7 was one compile from the same. Always
 HTTP-verify each target.
- **Barrier values are `small | medium | large` only.**
 the reaction-coordinate render service (not in this repo) **silently coerces anything else to
 `medium`**, so an authored `high`/`low` renders a flat profile while passing
 every chemistry check. And a carbocation- or bromonium-forming first step is
 `endergonic`, not `exergonic` — the intermediate sits *above* the reactants.

### 9. Seed

```bash
# proprietary toolchain (not in this repo)
# proprietary function (not in this repo)
# proprietary function (not in this repo) --owner-user-id <id> --topic <topic-id> --dry-run
# proprietary function (not in this repo) --owner-user-id <id> --topic <topic-id>
```

Always dry-run first. Seeding is idempotent: rerunning an unchanged chapter
reports all `unchanged` and creates no version rows. If a rerun reports
`updated` you did not expect, something recompiled — find out what before
proceeding.

`--owner-user-id` must be an existing user. The script will not create one.

### 10. Verify the Definition of Done

- [ ] Reader chapter compiles and renders
- [ ] Deck Creator Textbook tab shows the same chapter: open the Deck Creator
 drawing route (proprietary app, not in this repo), select the chapter's deck, open the
 Teaching Package → Textbook tab, confirm the canonical sections render
 (identical prose to `/reader/organic/<slug>`, no book numbering)
- [ ] Concepts seeded with the correct `deck_chapter_id`
- [ ] Every nugget has three text tiers and a `practice_check`
- [ ] Every figure has an accessibility bundle
- [ ] Deck compiled and review manifest approved — or legacy deck left untouched
- [ ] One video per brief, or a recorded deferral
- [ ] 1–2 validated questions per suitable type, published and seeded with
 `chapter_id` + `concept_slugs`
- [ ] At least one structure or mechanism type where the chemistry supports it
- [ ] Coherence pass run once, with `reports/topic-packages/<topic-id>/coherence-pass.md`
 written — every category answered, deletions justified
- [ ] LMS module emitted; chapter appears in the Deep Linking picker
- [ ] mcmurry + openstax crosswalks present and pointing at the *right* chapter.
 Check the compiled mapping, don't assume: the matcher scores
 `textbook_matching.terms` against chapter titles, so a generic term
 ("introduction", "synthesis", "reduction") silently produces a confident
 wrong match. Prefer explicit `overrides` for every catalogued book. Where a
 book genuinely has no matching chapter, override to an empty chapter list
 with a note — never leave a wrong number in place.
- [ ] Reader homework preview verified in-browser (or via `list_public_demos`):
 ≥6 surfaced questions, ≥5 question types, every major concept covered,
 ordered to follow the chapter (5f)
- [ ] Additional Reading carries **1–6 specific OpenStax section links** with a
 context sentence each (step 7), every URL verified to return 200, the
 chapter's reader slug added to the section-links coverage test (not in this repo), and no
 `why-this-chapter` link among them
- [ ] Science review sign-off recorded
- [ ] `available: true` flipped **last** — this also clears the **Pending** badge on
 `/reader/organic` for approved teacher-preview users (chapters after dienes
 show Pending while the reader catalog entry still has `available !== true`
 (proprietary assets, not in this repo).

Then stop and report. Do not flip `available: true` or run a production
migration without explicit permission.

**Mandatory end-of-run offer.** After reporting the production result, ask the
requester exactly one direct follow-up question:

> Run `review-organic-chapter` on this chapter now?

Do not replace the offer with a passive mention or silently start the review.
If the requester already explicitly ordered the review in the current request,
that affirmative instruction satisfies the offer; proceed after production
without asking the same question again.
The separate QA pass uses four independent personas, corrects verified errors by
default, describes every applied change, and updates
`reports/topic-packages/CHAPTER_REVIEW_STATUS.md`. Rerun it after substantial
revisions.

## Tests to run

```bash
# proprietary function (not in this repo)
```

## Gotchas

- **Reader slug ≠ deck chapter_id.** Using the reader slug for `chapter_id`
 silently produces a chapter whose questions never join to its concepts.
- **`MCMURRY_SECTIONS` is keyed by reader slug**, like everything else in
 the textbook catalog config (not in this repo) — a topic id there silently yields an empty
 Additional Reading list, because the lookup falls through to `?? []` rather
 than failing. The frontend coverage test (not in this repo) is what
 catches it.
- **OpenStax section numbers drift from the print McMurry.** The online edition
 merges and splits sections, so chapters 8 and 16 in particular are offset by
 one from the numbering many sources quote. Always verify the URL rather than
 trusting a remembered section number.
- **The question-banks feature flag (not in this repo) must be on** for seeding and for question sets to
 appear in the Deep Linking picker. It is set on the deploy platform (not in this repo); local `.env` may not
 have it.
- **The public-question-demos feature flag (not in this repo) is off by default** and should stay off
 until a demo chapter is seeded and reviewed.
- **`demo_eligible` is not decoration.** It makes a question anonymously
 reachable. Set it only on the designated demo chapter.
- **The compiler writes files, never the DB.** Seeding is always a separate,
 explicit step.
- **Legacy decks are frozen** pending the new pptx tool. Prefer a shim package.
- **"Reader shows fewer questions than the package" = stale bank.** The
 homework preview panel reads the seeded database (not in this repo), not the compiled JSON — re-run
 `seed_question_sets.py` for that topic (idempotent; unchanged items report
 `unchanged`).
- **The question-set panel renders workspace OR answer panel, never both.**
 Question types with a stimulus workspace plus a `select` answer mode
 (`molecular_geometry`, `molecular_vibration`) are unanswerable there — keep
 them out of chapter banks until the panel is fixed.
- **Write an `overrides` entry for every catalogued book, not just the six
 usual ones.** Term scoring is confident and wrong on the rest: chapter 26's
 isoelectric-point vocabulary matched Bruice Essential chapter 2, "Acids and
 Bases", at `mapping_status: "exact"`. Where a book genuinely has no matching
 chapter (Bruice Essential stops at benzene and never reaches proteins),
 override to `chapters: []` with a note — a null number plus an explanation
 beats a confident wrong one. Read each number off the proprietary textbook
 catalog (not in this repo) by hand.
- **The compiler clobbers aggregate textbook catalogs** (proprietary assets, not in this repo;
 five hits as of 2026-07-28): it rewrites the file with only the compiled topic's
 entries. Back the file up before compiling and merge the fresh topic entries
 into the backup (per-textbook `chapters` map) afterwards.

## Science-review lessons (from a 2026-07-23 review pass — apply to every new chapter)

These patterns produced 92 needs-work marks across earlier chapters. Bake them
in at authoring time so review passes on the first try:

1. **Reaction coordinate diagrams only for clear, simple reactions.** One clean
 step (or a two-step profile whose shape IS the lesson, like SN1). Every
 diagram authored for a multistep ionic addition (HBr, hydration, Br₂,
 alkyne hydration, proton transfer) was rejected with "rewrite text to avoid
 needing diagram". Carry the energetics in prose; add molecule figures instead.
2. **Tiny molecules need explicit hydrogens.** Ethane, ethene/ethylene,
 acetylene, etc. render as a bare line/dot without them. The reader/deck now
 default to `hydrogens: "auto"` (show below 6 heavy atoms), a user-tunable
 preference — to force it regardless of the viewer's setting, set
 `rdkit_options: {"show_hydrogens": true}` on the molecule asset (an explicit
 authored boolean always overrides the user's tri-state preference).
3. **Stereo labels: leave the size alone.** R/S, E/Z and cis/trans annotations
 now render at ~1.0× the height of a default atom label with no options at
 all — `render_molecule_png` applies a house default of
 `annotation_font_scale: 0.75` (RDKit's raw 0.5 is the "too small" reviewers
 flagged). **Do not set `annotation_font_scale` to make a label bigger.**
 Values above 1.0 are clamped and logged; 1.8 — which the chapter pipeline
 shipped for months — rendered the glyph at 2.5× the atom labels and ~23% of
 the figure height, burying the structure it was labeling (the cis-2-butene
 figures in ch18/ch14). If a stereo label genuinely still reads small, the
 fix is a bigger *figure*, not a bigger font.
4. **Run all display text through the chemistry text normalizer**
 (`ensure_chemistry_display_text`): H₂, Br₂, X₂, σ/π. Plain "pKa" is the
 house convention (no subscript markup in display strings).
5. **Use canonical spec shapes or the asset silently renders blank** in the
 review queue and reader: `newman_projection` takes an `object`
 (NewmanProjectionObject), never an ad-hoc `spec`; `synthesis_roadmap` is
 linear `nodes` + `steps` (no `edges`, no branching — put the alternate
 branch in `scientific_caveats`); `stereochemistry_conversion` needs
 `spec.molecules: [{label, smiles}]`, not just text `labels`.
6. **Energy profiles use real numbers.** `relative_energy` accepts numeric
 kcal/mol — compute with an RDKit constrained MMFF94 scan or use canonical
 literature values (cyclohexane: chair 0, half-chair +10, twist-boat +5.5,
 boat +6.5). If two minima differ (E vs Z), draw the difference.
7. **Verify every asset renders in the Science Review Queue before submitting
 it for review.** An asset the reviewer can't see becomes a needs-work row
 and a wasted review round. Legacy ingested slide PNGs are served from proprietary
 documentation (not in this repo) via the deploy image — confirm the deploy carries them.
8. **Never double-list a figure for review.** A `deck-figure:<id>` review task
 whose `<id>` is already a chapter-manifest asset is a duplicate; the review
 queue hides them, so don't author them.
