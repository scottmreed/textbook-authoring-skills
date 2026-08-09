---
name: review-organic-chapter
description: Use when one produced organic chemistry chapter needs post-production QA, verified-error correction, publication-readiness feedback, or a post-revision regression check.
---

# Review Organic Chapter

**Type:** Orchestration skill (post-generation chapter QA) — **CANONICAL**.
**Last verified against main:** 2026-07-24.
**Implementation alignment (ChemIllusion repo):** Live-tested on Chapter 1 after
the Chapter 11 baseline. The workflow now preserves baseline evidence, corrects
verified errors by default, supports constrained reviewer concurrency, uses the
actual compiled-artifact paths/backend environment, checks generated links, and
updates the durable review tally.

Reviews a single, already-produced chapter, corrects verified errors by default,
and reports whether it is ready to publish. Generation and review are
**separate on purpose**: run this after
[produce-organic-chapter](../produce-organic-chapter/SKILL.md), and rerun it
independently after substantial revisions. Use **report only** only when the
requester explicitly opts out of corrections.

The orchestrator launches **one subagent per persona**, keeps their reviews
independent, then reconciles them. The orchestrator — not any persona — decides
how each recommendation should be addressed, always choosing the **least-complex
intervention that fully addresses the need**. Adding more media is not assumed to
be the right answer.

## Before you start — confirm three things

1. **One chapter, by id.** You are reviewing exactly one topic package
 (proprietary topic-package JSON, not in this repo). If asked for
 "the whole book," review chapters one at a time. If asked for **the next
 chapter**, do not ask the requester to name it: select it deterministically
 from the tally rule in step 7.
2. **It is compiled.** The reader/question artifacts must exist so personas see
 what a student sees: the proprietary compiled reader chapter and question-set
 artifacts (not in this repo). If the topic-id reader file is absent, try the
 legacy reader slug path (proprietary assets, not in this repo) for older
 packages. If both are missing, run the proprietary topic-package compiler
 (not in this repo) first. The backend environment is required because question
 validation loads the backend registry.
3. **Read the contracts.** Read [references/finding-schema.md](references/finding-schema.md)
 (the shared JSON envelope) and skim the four rubrics in `references/` before
 dispatching.

## The review loop

### 1. Assemble the chapter package
Resolve, from the topic package `publishing` + top-level keys:
`topic_id`, `reader_slug`, `content_chapter_id`, `title`, `publishing.available`.
The personas read the files themselves — you just pass the paths + ids.

Before dispatch, run the orchestrator integrity check on compiled external
links, topic/concept identifiers, generated artifact paths, and obvious
cross-surface mismatches. Keep any issue as an `orchestrator-*` finding for the
synthesis; do not silently fix it before the baseline report.

### 2. Dispatch four persona subagents — in parallel, isolated
Fill [references/reviewer-template.md](references/reviewer-template.md) once per
persona (substitute `{PERSONA}`, `{RUBRIC_PATH}`, `{TOPIC_PACKAGE_PATH}`,
`{READER_CHAPTER_PATH}`, `{TOPIC_ID}`, `{CHAPTER_TITLE}`, `{CHAPTER_VERSION}`).
Run all four concurrently when the environment has four reviewer slots
(pattern: [superpowers dispatching-parallel-agents](../superpowers/dispatching-parallel-agents/SKILL.md)).
When the orchestrator counts against a lower concurrency limit, launch as many
as fit and start the remaining isolated reviewer as soon as a slot opens.
Concurrency limits may change scheduling, never independence or the requirement
that exactly four personas run.
Use a read-only agent type (Explore or general-purpose). Give each subagent ONLY
its own rubric path — never another persona's rubric or findings — so reviews are
independent until synthesis (acceptance criterion). The four rubrics:

| Persona | Rubric |
|---|---|
| Organic Chemistry Instructor | [references/persona-instructor.md](references/persona-instructor.md) |
| Struggling Student | [references/persona-struggling-student.md](references/persona-struggling-student.md) |
| Accessibility Persona | [references/persona-accessibility.md](references/persona-accessibility.md) |
| Learner with Visual Preference | [references/persona-visual-preference.md](references/persona-visual-preference.md) |

### 3. Collect and validate the four returns
For each persona return, validate the JSON:
`python skills/review-organic-chapter/scripts/validate_findings.py -`
(pipe the blob). If a return is malformed, re-request that ONE persona once with
the validator's problem list; if it still fails, keep what parsed and log the
gap in the synthesized report's `open_questions`. Do not block the other three.

### 4. Synthesize — run this step exactly once
**One pass only.** Do not loop personas or re-review. Produce the synthesized
report (schema in [references/finding-schema.md](references/finding-schema.md),
layout in [references/report-templates.md](references/report-templates.md)):

- **Reconcile** duplicates (same `location` from multiple personas → one
 recommendation keeping the strongest severity and every learner impact) and
 **retain disagreements** verbatim with your resolution — never erase a
 minority finding.
- **Choose the intervention** per recommendation — the least-complex option that
 fully addresses the need: sufficient/again-improved alt text, a longer
 description, a structured chemical description, a static image sequence, an
 animation/interactive, a transcript, a keyboard alternative, a text
 equivalent, an alternate activity, a prose edit, a new figure, added practice,
 or an instructor note. Explicitly list where a description is **sufficient as
 is** so no one over-builds. Decide the target surface (prose / figure /
 interactive / practice / assessment / instructor-support).
- **Compute publication readiness** — `ready | ready with minor revisions |
 major revision | blocked`. This is **computed, not averaged**: any persona
 `publication_blocker` or any `blocker`-severity finding forces at least
 `major revision`; an unresolved required-access blocker forces `blocked`. A
 high average `overall_score` can never override a live blocker.

### 5. Write the report
Write `reports/topic-packages/<topic-id>/chapter-review.md` (compact editorial
view + full evidence view — do not flatten into one list) and
`reports/topic-packages/<topic-id>/chapter-review.json` (the machine schema, for
regression). Validate the synthesized machine report before corrections or tally
updates:

```bash
# proprietary function (not in this repo)
```

Fix any schema or cross-reference errors before continuing. Then report the
compact view to the requester.

### 6. Correct verified errors by default

Preserve the baseline findings and verdict, then apply corrections unless the
requester explicitly asked for **report only**.

Correct automatically:

- chemical/factual inaccuracies and misleading exceptionless rules;
- answer leaks and unambiguous accessibility-description defects;
- broken/fabricated links;
- invalid notation, schemas, identifiers, or cross-surface inconsistencies;
- local blocker/high findings whose correct fix is clear and bounded.

Do not silently expand scope for subjective enhancements such as a new video,
large question-bank expansion, major pedagogy redesign, or product-level
interaction changes. Keep those as described recommendations unless they are
required to clear a verified error or access blocker. If an access blocker does
require a broader change, choose and document the least-complex effective
alternative before editing.

For every edit, append a **Post-correction record** to the Markdown report and a
`corrections` object to the JSON report with:

- exact change and source `finding_id`s;
- resolved / partially addressed / still open;
- compile/test commands and results;
- a post-correction estimate clearly labeled as **not a new persona verdict**.

#### 6a. BEFORE compiling: diff the artifact against the package

**A recompile regenerates the reader from the package, so anything that exists
only in the compiled artifact is destroyed.** Two known historical commits (refs not in this repo) —
one fixing tier-1 chemistry errors, invalid energy-diagram barriers, and all dead links,
and one making 33 tier-2 chemistry corrections across 18 chapters — were
**data-only edits to the compiled reader artifact** (proprietary assets, not in this repo)
and touched no package. They span ~25 chapters, so most of the corpus is exposed.

Run this before every compile, including the routine one in step 6:

```bash
# proprietary assets (not in this repo)
```

Compare `external_link` urls, `reaction_coordinate` `spec.steps`, and text
blocks. **Every difference is either a correction the package lacks (back-port it
to the topic package FIRST) or a package change the artifact predates.** Never
compile until each one is classified.

Observed 2026-07-31: ch6 had flip-flopped twice (fixed → recompiled away →
refixed → recompiled away again) and was live with 6/6 fabricated 404 links and a
flat energy diagram. Ch7 read correctly but its package still said `exergonic`
for a carbocation-forming step and had no `wikipedia_title` at all — and it
*needed* a recompile for the callout emitter, so the fix it required was exactly
the action that would have broken it.

Two recurring mechanisms produce artifact-only drift, so check both by name:

- **`wikipedia_title` unauthored** → `_concept_wiki_title` falls back to the
 concept's prose title and mints article names that never existed. Author
 `wikipedia_title` on every concept and HTTP-verify each one.
- **Barrier vocabulary** → `BARRIER_HEIGHTS` is `{small, medium, large}` only and
 `reaction_coordinate_service.py` **silently coerces anything else to
 `medium`**, so an authored `high`/`low` draws a flat profile that still passes
 every chemistry check. Still present in `alkynes-organic-synthesis`,
 `epoxides`, and `carboxylic-acid-derivatives`.

Compile with the backend environment and run focused tests:

```bash
# proprietary function (not in this repo)
```

Compilation may rewrite aggregate catalogs or curated/science-reviewed assets
in addition to the chapter artifacts. Inspect the generated diff immediately:
keep chapter-derived corrections, but restore unrelated aggregate churn and
never replace reviewed asset types, review status, or richer curated specs with
generic package output.

### 7. Update the chapter tally

Update `reports/topic-packages/CHAPTER_REVIEW_STATUS.md` only after both reports
exist and all four persona envelopes validate. Preserve the baseline verdict and
record correction/regression state separately. For “next chapter,” use the
lowest-numbered eligible unreviewed topic package in
`ORGANIC_TEXTBOOK_CHAPTERS`; skip catalog entries without compiled package
artifacts. This eligibility rule applies to implicit **next** selection. If the
requester explicitly names a produced package whose artifact is missing, compile
it during preflight instead of skipping it.

### 8. Regression mode (rerun after revisions)
If a prior `chapter-review.json` already exists, diff the new findings against it by
stable `finding_id` and classify **resolved / unchanged / worsened / new**;
target changed sections/assets if asked. Keep a `finding_id` stable when the same
issue persists. A rising average must not hide an unchanged blocker.

## Definition of Done (mirrors a private tracker issue's acceptance criteria)

- [ ] Exactly four persona subagents ran: Instructor, Struggling Student,
 Accessibility, Learner with Visual Preference.
- [ ] Each persona returned a schema-valid, location-anchored envelope
 (validator clean, or the gap logged in `open_questions`).
- [ ] Persona reviews were independent before synthesis (each saw only its own
 rubric).
- [ ] The orchestrator produced BOTH the compact and full reports.
- [ ] Compiled links/ids/artifact paths received an orchestrator integrity check.
- [ ] The orchestrator explicitly decided, per recommendation, whether a
 description suffices vs a new visual/video/interactive/accessible
 alternative is needed.
- [ ] Accessibility findings judged effective access to chemistry content and to
 required activities — not metadata presence.
- [ ] Conflicting persona findings remain visible with a documented resolution.
- [ ] Regression mode compared findings across versions (when a prior run
 exists).
- [ ] Publication readiness reflects live blockers and cannot be hidden by an
 average score.
- [ ] Verified errors were corrected by default (or `report only` was explicitly
 requested), with every change and verification result recorded.
- [ ] `CHAPTER_REVIEW_STATUS.md` was updated after report validation.

If one persona remains malformed after the single retry, finish and disclose the
partial report but **do not increment the tally**; the tally requires four valid
envelopes even though the review report may record the gap.

## Tests to run

```bash
# proprietary function (not in this repo)
```

## Gotchas

- **Do not blur evidence and remediation.** Write the baseline report before
 editing, preserve its verdict, then add a separate correction record.
- **Fix the package, never the artifact.** Every correction goes into the topic
 package (proprietary topic-package JSON, not in this repo). A fix written into the
 compiled reader artifact looks correct, passes review, and is deleted by the
 next compile — it has already happened twice to ch6. If a defect appears
 unfixable in the package, that is a compiler finding, not a licence to patch
 the artifact. See step 6a.
- **A chapter that reads correctly can still be broken.** The reader is a build
 output. Judge the package too: ch7 shipped a correct reader on top of a package
 that said the carbocation-forming step was `exergonic`, and its deck homework
 tab was already serving that wrong figure to instructors (proprietary deck
 assets, not in this repo).
- **An answer tell can be the presence of a picture.** When only some options in
 a selected-response item carry `structure_smiles`, check whether the
 illustrated set correlates with the key — it did in ch6 and ch7.
- **A `rank_order` item can ship pre-solved.** `MechanismCardSortRenderer` does
 not shuffle: it seeds the answer with the authored card order on mount. If
 `student_config.cards` equals `answer_key.correct_order`, the item submits
 correct untouched. Both ch6 ranking items did.
- **The compile-time leak guard cannot see semantic leaks.**
 `find_accessibility_leaks` matches only answer ids, a fixed verdict vocabulary,
 and answer-key numbers. It returns clean while an `accessible_description`
 names the product ("methanol"), states which geometry is Z, or glosses a group
 label with the grading key. Read the descriptions; do not trust the guard.
- **A figure can be chemically correct and still unreadable.** The visual and
 struggling-student personas should call out labels that obscure the structure,
 not just wrong structures. The recurring instance: authored
 `rdkit_options.annotation_font_scale` above 1.0, which put R/S/E/Z glyphs at
 2.5× atom-label height across ch14/ch18 for months while every chemistry check
 passed. The band is now enforced at compile by the proprietary annotation-font
 clamp (not in this repo) and clamped at render
 (`deck_creator._apply_font_scale_options`) — but the *judgment* still belongs
 to the review: "is the label sitting on the molecule?" is a finding.
- **Do not claim formal accessibility compliance** — this is an AI review, not
 an audit of record. Report specific barriers.
- **The visual-preference persona is a usability lens, not a learning-style
 claim.** Do not assert fixed "visual learners."
- **Independence is load-bearing.** If you paste one persona's findings into
 another's prompt, the review is no longer four independent perspectives.
- **One synthesis pass per run.** Corrections and targeted validation are not a
 second persona verdict. A new verdict requires a separate four-persona
 regression run.
