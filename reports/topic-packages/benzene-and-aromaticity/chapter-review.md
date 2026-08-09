# Chapter review — Benzene and Aromaticity (`benzene-and-aromaticity`)

**Chapter version:** 1 · **Run:** 2026-07-28 · **Reviewers:** 4 independent personas
**Baseline publication readiness: `blocked`**

> This is an AI review, not an accessibility audit of record. It reports specific
> barriers; it does not certify WCAG conformance.

> **The chapter is already live.** `publishing.available` is `true` and the
> question bank is seeded, so every blocker below is in front of students now.

---

# Compact editorial view

## The verdict in one paragraph

The chemistry is strong. The instructor persona re-derived every quantitative
claim in the prose and every one of the 46 answer keys — bond lengths, heats of
hydrogenation, pKa values, chemical shifts, IR wavenumbers, both hotspot atom
indices, every charged-ion SMILES — and found them correct. The chapter is
blocked on **access**, not on chemistry: two required activities cannot be
completed without vision, and the authored descriptions meant to mitigate that
are read by no renderer the chapter uses. Three chapter-level defects sit
alongside: one sentence inverts the classic ortho-isomer-count evidence for
delocalization, the surfaced acidity ranking keys an order the chapter's own
prose argues against, and in ten statement-choice items exactly one option
carries a decorative structure — which is the correct answer in nine of them.
The orchestrator re-verified all three independently rather than trusting the
persona reports.

## Persona scores

| Persona | Score | Blockers raised |
|---|---:|---|
| Organic Chemistry Instructor | 7.2 | inst-001 |
| Struggling Student | 6.0 | ss-001 |
| Accessibility Persona | 5.4 | access-001, access-002, access-003 |
| Learner with Visual Preference | 5.7 | vis-001 |

Readiness is **computed, not averaged**. The instructor's 7.2 reflects genuine
chemical accuracy; two unresolved required-access blockers force `blocked`
regardless of the mean.

## Blockers

| # | What | Fix chosen | Where |
|---|---|---|---|
| rec-001 | Ortho-isomer-count evidence stated backwards and self-contradictorily | prose-edit | prose |
| rec-002 | Isomer items label options "Structure A–D"; all chemistry is in the images | text-equivalent | assessment |
| rec-003 | Hotspot atoms selectable only by bare index — a learner who knows the answer cannot enter it | structured-chemical-description | assessment |
| rec-004 | Four drawing items have no non-drawing response route | alternate-activity (**platform**) | assessment |
| rec-005 | 9 of 10 lone-illustrated options are the correct answer | prose-edit | assessment |
| rec-006 | Acidity ranking contradicts the chapter's cycloheptatriene claim | prose-edit | prose |

## High

- **rec-007** — the `accessible_description` authored on all 46 items is read by
 no renderer this chapter uses. Platform gap; it is the mechanism that turns
 rec-002 and rec-003 from awkward into unanswerable.
- **rec-008** — the π MO ladder, the inscribed-polygon construction, and the
 pyridine-versus-pyrrole lone-pair geometry have no orbital representation.
 `orbital_overlay` compiles to an empty image URL, so no chapter-level
 authoring closes this. Same open item as ch14.

## Medium and low

rec-009 through rec-034 cover the 13C symmetry condition, the toluene IR band
count and the missing meta ranges, the pyrrole pKa, the cyclobutadiene
square/rectangle contradiction, incomplete prerequisites, alt-text defects,
structures missing from classification cards, imidazole basicity, spectrum
descriptions, the video brief's accessibility requirements, and the reader's
missing practice and signposting. Full detail in the evidence view and in
`chapter-review.json`.

## Sufficient as is — do not over-build

- The **prose** treatment of the MO ladder, the inscribed-polygon construction,
 and the ring current is complete. A non-visual learner loses nothing relative
 to a sighted one here; the missing figures are a usability gap for everyone,
 not an access gap.
- `mol-cyclooctatetraene`'s alt text already separates drawing convention from
 molecular truth. No change.
- The keyboard-complete categorize / matching / rank-order / comparison-matrix
 renderers need **no** alternative activity — only structures on the cards.
- Hint ladders on the text-based question types are sufficient as written.
- The deferred video's hidden block causes no learner-visible problem today;
 only its brief needs the accessibility requirements bound.

---

# Full evidence view

## Disagreements retained

**1. Severity of the illustrated-option tell.**
*Visual Preference:* blocker — a learner who scans figures first gets nine free
answers, so those items measure nothing.
*Accessibility:* high — an inequity and a validity problem, not a hard block.
**Resolution:** blocker. The orchestrator re-derived the correlation
independently: 9 of 10 illustrated options are the key, and the tenth
(`ch15-benzene-bond-lengths-v2`) points at a distractor, so the cue the other
nine train actively misleads on that one. It defeats items across four of the
eight concepts, invalidates mastery gating built on them, and the mechanical
answer-leak guard reports zero leaks — nothing else catches it.

**2. Overall chapter quality.** Scores ranged 5.4–7.2 (see table).
**Resolution:** readiness is computed. Chemical accuracy is genuinely strong;
two unresolved required-access blockers force `blocked` regardless.

**3. Pyrrole conjugate-acid pKa.**
*Instructor:* the quoted 0.4 belongs to one textbook lineage; the widely cited
value is near −3.8 (confidence 0.62).
**Resolution:** toward −3.8. The chapter's derived "five orders of magnitude"
claim depends entirely on the 0.4 figure; against pyridinium's 5.25 the gap with
−3.8 is about nine orders. The qualitative conclusion is unaffected either way.

**4. Is the cycloheptatriene ranking an item defect or a prose defect?**
*Instructor:* the keyed order is experimentally defensible; the prose fails to
support it. *Struggling Student:* the item is unanswerable from the chapter.
**Resolution:** both, about different halves. The keyed order is correct
chemistry. The prose overstates by calling the antiaromatic anion "not formed
under comparable conditions" and omits the pKa that decides the pair. Fixing the
prose resolves the contradiction and keeps an item that tests the right idea.

## Consensus strengths

- Every quantitative claim and all 46 answer keys verify correct, including both
 hotspot atom indices and every charged aromatic SMILES.
- Misconceptions are named and pre-empted in the prose rather than left as
 traps: Kekulé forms as contributing structures rather than an equilibrium,
 non-integer *n*, cyclooctatetraene as nonaromatic rather than antiaromatic.
- Every question ships a three-level hint ladder that escalates without leaking,
 plus wrong-answer explanations that diagnose the specific reasoning error.
- The counterexample set is complete: cyclobutadiene (antiaromatic),
 cyclooctatetraene (nonaromatic by distortion), cyclopentadiene (nonaromatic by
 sp³ carbon), cyclopropenyl cation (*n* = 0).
- Drag-shaped question types are keyboard-complete; no color-only, motion-only,
 or hover-dependent content anywhere.
- Figures are grouped into deliberate comparison sets, and each asset's
 `learning_goal` compiles into the reader as a per-figure purpose statement.
- The unproduced MO animation was deferred with a written reason and compiled
 hidden rather than shipped as a broken player.

## Orchestrator integrity check

Run before dispatch, on the compiled artifacts:

- All 9 generated external links return HTTP 200 and land on the intended
 articles (verified effective URL and page title, not just status).
- **One defect found:** the `spectroscopy-of-aromatic-compounds` concept sets
 `wikipedia_title: "Ring_current"`, and that article is about the
 *magnetospheric* ring current in geophysics — "an electric current carried by
 charged particles trapped in a planet's magnetosphere" — not the NMR aromatic
 ring current. Recorded as `orchestrator-001`; corrected below.
- Concept slugs, nugget ids, reader section ids, and question `concept_slug`
 references all resolve. No orphan assets. `deck_chapter_id`,
 `content_chapter_id`, and the McMurry chapter number (15) are consistent
 across reader, question set, and registry.
- One empty-URL media block (the deferred video), correctly `is_hidden: true`.

## Persona envelopes

Preserved verbatim under `persona-returns/`, all four validator-clean:

- `persona-returns/instructor.json` — 14 findings
- `persona-returns/struggling-student.json` — 17 findings
- `persona-returns/accessibility.json` — 12 findings
- `persona-returns/visual-preference.json` — 17 findings

Machine-readable synthesis with every finding and recommendation:
`chapter-review.json` (validator-clean against the synthesized schema).

## Open questions carried forward

- Are the 23 `-v2` variants ever surfaced directly to students? If so, the
 item count affected by rec-002, rec-003, and rec-005 doubles.
- Does the embedded Ketcher workspace expose a keyboard-reachable SMILES import?
 If it does, rec-004 is a documentation gap rather than a missing capability.
- Is `accessibility_bundle.accessible_description` intended to be rendered, and
 is the `description` vs `accessible_description` key name a mismatch?
- Will `orbital_overlay` ever render, or is the reader permanently limited to
 `molecule` assets? This decides whether rec-008 is a content or platform gap.
- Are `practice_check` blocks meant to reach the reader at all?

---

# Post-correction record

**Status:** applied and verified, without a second persona run.
**Post-correction readiness estimate: `blocked` — this is not a new persona verdict.**

The baseline verdict and every baseline finding above are preserved unchanged.
Only a separate four-persona regression run can issue a new verdict.

## Why the estimate is still `blocked`

Every chemistry defect, every assessment-validity defect, and every
chapter-authored accessibility defect is resolved. The estimate does not move
because **one required activity is still impossible for some learners**: the
four `structure_scaffold` items accept only canvas drawing (access-003), and the
`accessible_description` authored on all 46 items is read by no renderer this
chapter uses (access-004). Neither can be closed by editing the chapter.

## Applied — 21 changes

**Blockers resolved**

1. **Ortho-isomer-count evidence** (inst-001) — rewritten: one ortho isomer is
 isolable where fixed alternating bonds predict two, with both alternatives
 spelled out.
2. **"Structure A–D" option labels** (access-001) — replaced in both isomer
 items with chemically identifying descriptions of each substitution
 relationship; both descriptions rewritten to match.
3. **Illustrated-option answer tell** (vis-001, access-005) — all 10 decorative
 single-option structures removed; the 9 descriptions that announced the cue
 rewritten. Audit now reports **0** items with partial option illustration.
4. **Acidity-ranking contradiction** (inst-003, ss-001) — the cycloheptatriene
 prose no longer claims its anion is "not formed"; it now gives pKa ≈ 36
 against propene's 43 and cyclopentadiene's 16, making the keyed order
 derivable from the chapter.

**Partially addressed**

5. **Hotspot atom identity** (access-002) — both prompts and descriptions now
 state the ring numbering and which carbons carry the double bonds, so a
 non-visual learner can map "C atom N" onto a ring position and deduce the
 saturated carbon. The renderer's bare label remains a platform need.
6. **Video accessibility** (access-010) — captions + transcript, described
 visual state changes, pausable/steppable playback, and no color-only
 encoding are now bound to the deferred brief.

**Chemistry and content**

7. Wikipedia target repointed from `Ring_current` — a **geophysics** article
 about planetary magnetospheres — to `Aromatic_ring_current` (orchestrator
 integrity finding; no persona caught it).
8. ¹³C signal-count rule given its symmetry condition (inst-005).
9. Toluene IR gained its second monosubstituted out-of-plane band at 694 cm⁻¹
 with its own wrong-answer explanation; meta ranges and a band-count
 discriminator added to the prose (inst-011, ss-012, vis-010).
10. Pyrrole conjugate-acid pKa 0.4 → −3.8, C2 protonation noted, derived gap
 recomputed five → nine orders in both tiers and the practice check (inst-012).
11. Cyclobutadiene square/rectangle account reconciled into one causal story
 (inst-006).
12. Imidazolium pKa ≈ 7.0 added, making the staged basicity ranking decidable
 (ss-015).
13. Prerequisites completed on three concepts (inst-007).
14. Alt text rewritten on 8 assets (inst-008, access-007/008/009, vis-013).
15. `show_hydrogens` made consistent within both comparison groups (vis-014).
16. Structures added to every categorize and rank-order card (ss-013, vis-017).
17. Both IR descriptions now carry every peak position and intensity (access-006).
18. Arene-naming description no longer adds a cue absent from the prompt (access-012).
19. Frost circle named at first use (ss-017).
20. Anthracene central-ring reasoning supplied (inst-013).
21. Resonance stabilization and aromatic stabilization energy identified as one
 quantity (inst-014).

## Verification

| Check | Result |
|---|---|
| `compile_topic_package` (isolated) | valid — 8 concepts, 8 nuggets, 21 assets, 46 questions, 13 mappings, `verification_required` empty |
| `find_accessibility_leaks` over all 46 items | **0 leaks** |
| Partial-option-illustration audit | **0 items** (was 10; 9 of 10 keyed correct) |
| `Structure A/B/C/D` labels remaining | **0** (was 8) |
| All 9 compiled external links | HTTP 200, effective URL + page title checked |
| `pytest tools/topic_packages/tests/ -q` | **54 passed** |
| Backend question-bank / accessibility / numeric suites | **171 passed** |
| `test_deep_linking_question_sets` | 5 failed — **pre-existing** (`sqlite: no such table: assignment_plans`), same list recorded during the ch14 build; no Python touched here |
| `topic-package-textbook-profiles.json` after `--write-runtime` | re-merged and diffed against pre-compile state — 91 chapter entries, **0 lost** |

## Still open

- **access-003 / rec-004** — drawing items have no non-drawing response route.
 Unresolved required-access blocker. Platform.
- **access-004 / rec-007** — `accessible_description` reaches no renderer this
 chapter uses. Platform. Note the key-name mismatch (`description` vs
 `accessible_description`) flagged in the persona's open questions.
- **access-002 / rec-003** — mitigated in-chapter; renderer label still bare.
- **rec-008, rec-021** — the orbital and energy-diagram visual cluster;
 `orbital_overlay` compiles to an empty image URL. Same open item as ch14.
- **rec-019, rec-020** — the reader compiles no practice and no objectives or
 prerequisites. Compiler-level.
- **rec-023, rec-024** — three declared objectives unassessed; the
 four-requirement test never demonstrated before it is assessed. New content,
 deliberately outside correction scope.
- **The seeded production bank is now stale** — 20 of the 46 items changed.
 Reseeding needs explicit permission.
