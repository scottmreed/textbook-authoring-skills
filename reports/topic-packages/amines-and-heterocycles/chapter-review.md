# Chapter review — Amines and Heterocycles (`amines-and-heterocycles`)

**Run:** 2026-07-30 · **Chapter version:** 1 · **Mode:** baseline (no prior review)
**Baseline verdict: BLOCKED** — computed, not averaged.

| Persona | Score | Blockers raised |
|---|---:|---|
| Organic Chemistry Instructor | 7.6 | `instr-001` |
| Struggling Student | 6.4 | none |
| Accessibility Persona | 6.4 | `access-001`, `access-002` |
| Learner with Visual Preference | 6.0 | none |

---

# Compact editorial view

## What this chapter got right

Chemically this is the cleanest package the pipeline has produced. The instructor
persona verified all 26 asset SMILES and all 84 question structures with RDKit
against formula, canonical connectivity **and** InChIKey, independently re-derived
all 56 answer keys, and checked roughly twenty pKa values against literature.
Result: **zero wrong structures, zero wrong answer keys, zero wrong values** — including
the cases where a formula-identical isomer was available to go wrong (the azo dye's
E geometry, 2,4- versus 2,5-dinitroaniline, histamine's C4 attachment, quinoline
versus isoquinoline). That is the failure mode that caught ch18 and ch23, and it did
not recur.

The ch22 answer-leak class also did not recur. Both reaction-coordinate descriptions
report plotted geometry and relative heights and name neither the step count nor the
thermodynamic direction, and the automated guard is clean across all 56 items.

## Why it is still blocked

Three things, in descending order of how much they are the chapter's own fault.

**1. Two chapter-local blockers, both corrected the same day.** Both Hofmann drawing
items described a primary amine as *"a five-carbon secondary amine"* — and did so
**only in the accessibility channel**. Sighted learners never saw it; screen-reader
learners were taught, by the chapter itself, the precise misconception the chapter's
first concept exists to destroy. It also silently contradicted a sibling item whose
answer of 3 equivalents is correct only because the amine is primary. Separately,
`ch24-hofmann-equivalents-v2` told the non-visual learner the amine was *"cyclic
tertiary"* — which, given the chapter's own rule of four-minus-carbons-on-nitrogen,
is the answer. Its v1 twin was written correctly, which is what proved the standard
existed and this item had departed from it.

**2. The platform `structure_scaffold` ticket, unresolved.** The four drawing items
accept only pointer drawing on a Ketcher canvas whose toolbar profile also hides
paste, so there is no SMILES, name, or selection path in. A keyboard-only or
screen-reader learner cannot submit *any* answer. This is identical to ch1, ch11 and
ch15–19 and ch23, and it forces `blocked` on its own. It was deliberately **not**
worked around per chapter: a chapter-local hack would mask a recurring platform
ticket. Mitigating fact: no *concept* becomes unassessable, since both affected
concepts carry three or four other question types.

**3. The coherence pass introduced an error again.** Production's own reconciliation
pass added a benzylamine/diphenylamine paragraph closing with *"two rings, twice the
discount"* — refuted by the two numbers printed two sentences earlier (the first ring
costs 6.1 units, the second a further 3.8, not another 6.1). This is exactly the ch23
pattern, where the coherence pass introduced a wrong carbocation mechanism while
closing a different gap. **The lesson is now twice-confirmed: whatever the coherence
pass adds needs the same scrutiny as originally authored prose, not less.**

## The chapter's real weakness is form, not chemistry

All three non-instructor personas converged on this independently. Every one of the
26 figures is a static single molecule — not one shows a relationship, sequence,
ordering, orbital, or comparison. So the pKaH ladder (about eighteen values), the
diazonium replacement menu (seven reagents), the pyrrole-versus-pyridine orbital
geometry, and four multi-step mechanisms are all carried by prose alone. The chapter
twice tells the reader that content *"should be learned as a table because exams treat
it as one"* — and then does not supply one.

This is not a defect to correct; it is authoring that has not happened, and it needs
non-molecule asset kinds the pipeline does not yet have. It is ranked high and left open.

## Corrections applied (21 groups)

Every verified factual defect and every unambiguous accessibility defect was corrected,
then recompiled and re-tested. Highlights beyond the two blockers:

- **Halogens were graded twice, taught nowhere, and the stated rule predicted the wrong
 sign.** The chapter told students to reuse their EAS directing-effect vocabulary, which
 files chlorine with methoxy as an ortho/para director — so a student reasoning exactly
 as instructed ranked p-chloroaniline *above* aniline, and both graded items said
 otherwise. Added the induction-versus-resonance paragraph, which also supplies the
 two pKaH values that previously existed only in an undelivered `practice_check`.
- **Two unrelated reactions share the name Hofmann** (rearrangement in §5, elimination
 in §7) and nothing said so. Added an explicit contrast to both sections.
- **The Hofmann rule was stated without its domain of validity.** Bounded it with the
 E1cb/styrene exception.
- **Six discrete text defects**: a truncated enumeration (`"C3, C5..."`), a promised
 count of three delivered as two, an order-of-magnitude arithmetic slip
 (hundred-million- for billion-fold), an anion called *"Neutral NH2-"*, a false claim
 that diazonium hydrolysis was the chief industrial phenol synthesis, and PLP
 transamination conflated with genuine reductive amination.
- **Notation**: reader prose shipped ASCII while question prompts used Unicode, so a
 screen reader announced `C#N` as *"C hash N"* and `10^11` as *"ten caret eleven"*.
 Normalised 45 fields, keeping mechanism names (SN2, E2) plain per house rule.

## New platform finding from this review

`rank_order` **cannot display structures**. The backend's `visual_enrichment` does
enrich `cards` with `imageUrl`, but `MechanismCardSortRenderer` has no `imageUrl` path,
so any authored structure is silently dropped. Structures were therefore added only to
`categorize_groups` and `comparison_matrix`, where the renderers verifiably display
them — and the two ranking items were left as text with the gap recorded rather than
authored into a black hole.

## Where a description is sufficient as is — do not over-build

- Both reaction-coordinate accessible descriptions (they carry plotted heights and leak nothing).
- All 26 asset alt texts *as alt texts* — the gap is delivery of the authored
 `long_description`, not alt-text quality, so no asset needs re-authoring.
- `curved_arrow` site labels and `bond_change_ledger` `reaction_display` strings.
- The five video deferral records (now carrying the colour/motion constraint).
- `single_select` / `multi_select` option sets — name plus structure image is already
 an equivalent stimulus.

## Disagreements and how they were resolved

**Do students currently hit dead video players?** The Struggling Student persona said
yes ("I click the thing and nothing plays"); Accessibility and Visual said no. **Verified
directly: all six compiled video blocks carry `is_hidden: true` and an empty url.**
Accessibility and Visual are correct; that impact does not occur today. The underlying
point survives — nothing delivers the explanations those briefs were scoped to carry —
and is why the visual gaps rank high.

**Is the false industrial-phenol claim a blocker?** The instructor graded it medium and
explicitly invited override. Upheld at medium: the blocker bar is chemistry that changes
what a student *predicts*, and this changes only provenance. Corrected anyway, so the
call had no practical consequence.

**Is `practice_check` non-delivery a chapter or platform issue?** Three personas raised
it. Recorded as **platform** (verified identical in ch22 and ch23) and left visible in
the report because it materially degrades this chapter, but not re-authored — the content
is already correct and is dropped downstream.

## Post-correction estimate — **blocked** (not a new persona verdict)

All chapter-local blockers and every verified factual defect are resolved. The estimate
stays `blocked` **solely** because `access-001` is unresolved. **Setting that platform
item aside, the estimated state is `ready with minor revisions`.** Only a fresh
four-persona regression run can issue a new verdict.

---

# Full evidence view

## Ranked recommendations

| # | Recommendation | Severity | Intervention | Surface | Sources |
|---|---|---|---|---|---|
| rec-001 | Primary amines described as "secondary" in the accessibility channel | blocker | prose-edit | assessment | instr-001, access-005 |
| rec-002 | Numeric item hands the screen-reader learner its own answer | blocker | prose-edit | assessment | access-002 |
| rec-003 | `structure_scaffold` accepts only canvas drawing | blocker | keyboard-alternative | interactive | access-001 |
| rec-004 | "Two rings, twice the discount" refuted by its own numbers | high | prose-edit | prose | instr-003 |
| rec-005 | Halogens graded twice, never taught, stated rule predicts wrong sign | high | prose-edit | prose | instr-004, ss-009 |
| rec-006 | Classification item describes distractors more fully than its key | high | prose-edit | assessment | access-006 |
| rec-007 | Name-to-structure translation is an unstated gate | high | prose-edit | assessment | instr-002 |
| rec-008 | Two same-named Hofmann reactions never disambiguated | high | prose-edit | prose | ss-004, vis-014 |
| rec-009 | Authored accessibility payload never reaches the learner | high | instructor-note | instructor-support | access-003/004/009, instr-011, ss-001, vis-010 |
| rec-010 | List-shaped knowledge delivered as paragraphs | high | new-figure | figure | ss-002, ss-005, vis-002, vis-008 |
| rec-011 | The chapter's keystone idea has no visual representation | high | new-figure | figure | vis-001, instr-010 |
| rec-012 | Six discrete text defects | medium | prose-edit | prose | ss-003/006/016, instr-005/012/013/014/016 |
| rec-013 | Hofmann rule stated without its domain of validity | medium | prose-edit | prose | instr-006 |
| rec-014 | Feedback contradicts prose on what pyrrole's pKaH measures | medium | prose-edit | assessment | ss-010 |
| rec-015 | Descriptions promise drag-and-drop the UI does not ship | medium | prose-edit | assessment | access-008 |
| rec-016 | Explicit hydrogens applied inversely to teaching load | medium | new-figure | figure | vis-004, vis-005 |
| rec-017 | Ledger labels atoms absent from the drawn stimulus | medium | new-figure | assessment | vis-013 |
| rec-018 | Level-3 hints read out the answer key | medium | prose-edit | assessment | ss-011 |
| rec-019 | Prerequisite graph does not match prose dependencies | medium | prose-edit | prose | instr-007 |
| rec-020 | Reader prose and question prompts use different notation | medium | prose-edit | prose | instr-009, access-011 |
| rec-021 | Structure support uneven across structural tasks | medium | new-figure | assessment | vis-012 |
| rec-022 | Video briefs lacked a colour/motion-only constraint | medium | instructor-note | instructor-support | access-010 |
| rec-026 | Azide/Gabriel objective assessed only through failure cases | medium | added-practice | practice | instr-008 |
| rec-023 | Compound named by a word the chapter never uses | low | prose-edit | assessment | ss-018 |
| rec-024 | Background link did not cover its section's topic | low | prose-edit | prose | ss-019 |
| rec-025 | Term the question asks for absent from the default tier | low | prose-edit | prose | ss-015 |
| rec-027 | Figures stranded after long prose; no intra-section landmarks | low | instructor-note | instructor-support | vis-007, access-012 |
| rec-028 | Reader carries one OpenStax link, to chapter front matter | low | instructor-note | instructor-support | instr-015 |

Full per-persona findings (66 in total, with evidence and confidence) are embedded in
[`chapter-review.json`](chapter-review.json) under `personas[].findings`.

## Orchestrator integrity check (pre-dispatch)

Clean — no `orchestrator-*` findings. All 10 concept Wikipedia titles resolve HTTP 200
with no redirects and no raw-space slugs; all 11 compiled reader links resolve 200;
`topic_id` / `reader_slug` / `deck_chapter_id` agree across surfaces; compiled question
slugs match the package exactly.

## Verification record

| Command | Result |
|---|---|
| `compile_topic_package --write-runtime` | clean — 10 concepts / 26 assets / 47 slides / 56 questions / 28 surfaced / 28 staged / 15 types |
| `pytest tools/topic_packages/tests/ -q` | 62 passed |
| backend question-bank + leak-guard + numeric-grading suites | 177 passed |
| `find_accessibility_leaks`, compiler-identical 4-arg call, all 56 items | 0 hits |
| RDKit re-validation of every SMILES after edits | all parse; categorize structures' carbons-on-nitrogen match every key |
| Wikipedia `Acid_dissociation_constant` | HTTP 200, no redirect |

**Housekeeping:** `topic-package-textbook-profiles.json` was clobbered by each recompile
(14th and 15th recorded hits) and re-merged both times to 247 chapter entries across 13
textbooks.

**Publication state unchanged by this review:** the chapter remains `available: false`
and **unseeded**. Seeding and the `available` flip both need explicit permission.
