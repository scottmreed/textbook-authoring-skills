# Chapter review — Carbonyl Alpha-Substitution Reactions (`carbonyl-alpha-substitution`)

- **Run:** 2026-07-29 · version 1 · four personas (Instructor 8.4 · Struggling Student 6.4 · Accessibility 7.2 · Visual Preference 6.3), all envelopes validator-clean
- **Baseline publication readiness: `major revision`** — forced by one accessibility blocker (access-001); scores cannot override it.

## Compact editorial view

**The chemistry is clean.** The instructor persona RDKit-verified every structure and all 50 answer keys: zero chemical errors, pKa framework quantitatively self-consistent, both prior-chapter compiler defects (error_repair keys, numeric tolerance shape) confirmed avoided. The accessibility authoring layer is the strongest in the series — every question bundled, every asset double-described, no lone-illustrated-option tells.

**One blocker.** Both `reaction_coordinate_reasoning` questions leak two of their four graded answers: the prompt says "slow enolization, then fast capture" (→ rate-determining step) and the accessible description says "a two-step free-energy profile" (→ step count), while omitting the energy information a non-visual learner needs for the two remaining items (access-001 + access-002).

**Chapter-local refinements (corrected in this run — see Post-correction record):**
| Rec | What | From |
|---|---|---|
| rec-001 | De-leak both profile questions; neutral geometric accessible description with relative heights | access-001, access-002 |
| rec-005 | Add the kinetic + thermodynamic enolate figures of 2-methylcyclohexanone to the teaching surface | visual-004, ss-008 |
| rec-006 | Add enol-content rank pair + kinetic-alkylation product pair; reframe biological objective | inst-005, inst-007, inst-006 |
| rec-007 | Align "three stages" prose with the two-step profile; state each transformation before analyzing it | ss-006, ss-002 |
| rec-008 | Swap enolate items out of the concept-1 tautomer-vs-resonance sorter for prior-chapter resonance pairs | ss-005 |
| rec-009 | Placement-neutral acetophenone caption | ss-007, visual-010 |
| rec-011 | Nine text fixes: homoallylic mislabel, carboxylate overstatement, enolate gloss, hint string-match, "in order", orientation-dependent alt text, H-bond caption, "soft", one-arrow note | inst-001/002/003, access-006, ss-010, visual-011/009, ss-011, inst-008 |
| rec-012 | Haloform prerequisites += alpha-halogenation-of-ketones | inst-004 |

**Platform-wide, not chapter-fixable (verified identical in ch21's compiled reader):**
- rec-002 — synthesis-roadmap assets compile to empty-URL image blocks (italic alt-text fallback); the chapter's two flagship figures render as nothing. [visual-001, access-005, ss-004]
- rec-003 — authored `practice_check`s (10) and `long_description`s (20) are dropped by the reader compiler; no inline checkpoints, no long descriptions for screen readers. [ss-001, access-004]
- rec-010 — blank-canvas `structure_scaffold` has no non-visual/non-pointer alternative (standing platform ticket); concept-level accessible equivalents exist for both affected concepts. [access-003]
- rec-015 — select-stem stimulus display and ledger hydrogen rendering are question-type capabilities. [visual-013, visual-014]

**Deferred visual opportunities** (prose confirmed to carry full content; gated on platform capability): mechanism step-through sequences (rec-004), pKa ladder figure (rec-013), chapter overview/recap nuggets (rec-014).

**Disagreement resolved:** the visual persona's "visually thin" verdict vs the accessibility persona's "fully reachable through text" strength — both true at different layers; the actionable subset that renders today (two enolate figures) was corrected, the rest recorded as opportunities. The struggling student's high on the expanded-tier default was downgraded to medium: the tier system (default `expanded`, user-switchable, `_detail_texts` preserved) is platform design; the chapter-local piece (transformation-statement openings) was fixed.

**Sufficient as is:** all remaining alt texts; curved-arrow site labels and ledger text rows as accessible mechanism assessment; deferred-video hiding with production notes; repeated enolate/enol cards (rec-016).

## Full evidence view

The machine report `chapter-review.json` embeds all four validated persona envelopes verbatim — 40 findings total (instructor 9, struggling student 11, accessibility 6, visual 14) with locations, evidence, and confidences — plus the ranked recommendations with chosen interventions and rationale. Open persona questions worth carrying forward:

- Does the profile widget expose its control points to assistive technology? (decides whether access-002's residue is closed by the new description alone)
- Has the runtime delivery gap for `accessibility_bundle` content found in the ch16 live review been closed?
- Are rank-order cards and curved-arrow interactions keyboard-operable?
- `demo_eligible=0` on all 50 questions — intended (no demo chapter designation for ch22).

## Post-correction record (2026-07-29, same run — not a new persona verdict)

Corrections were applied by default per skill policy; the baseline verdict above is preserved. Every change, its source findings, and verification results are recorded in the `corrections` object of `chapter-review.json`. Summary:

- **rec-001 applied** — both profile prompts no longer name the slow step; both accessible descriptions now narrate the curve neutrally (labelled stationary points, relative rises/falls) without stating step count, RDS, or energetic classifications, restoring all four graded items as genuine work in both modalities. Resolves access-001; addresses the content half of access-002.
- **rec-005 applied** — two new molecule assets (`mol-kinetic-enolate-2mcx`, `mol-thermo-enolate-2mcx`) attached to `nugget-enolate-formation-bases`.
- **rec-006 applied** — new question pairs `ch22-enol-content-rank`(+v2) and `ch22-kinetic-alkylation-product`(+v2); acetoacetic objective 3 reframed to the assessed malonic/acetoacetic contrast. Question bank now 54 questions / 27 surfaced.
- **rec-007, rec-008, rec-009, rec-011, rec-012 applied** as described in the compact table.
- **Not applied (platform):** rec-002, rec-003, rec-010, rec-013, rec-014, rec-015 — recorded above.
- **Verification:** recompile clean (54 questions validated, 0 errors); `tools/topic_packages/tests` 62 passed; backend question-pipeline suites 177 passed; `mcmurrySectionLinks` 6 passed; textbook-profiles clobber re-merged (all 17 topics present). Post-correction readiness estimate: **ready with minor revisions** (blocker resolved; remaining highs are platform-level delivery gaps outside chapter scope) — *estimate only; a new verdict requires a four-persona regression run.*
