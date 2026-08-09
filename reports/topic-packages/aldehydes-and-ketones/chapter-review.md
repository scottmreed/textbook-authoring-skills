# Chapter review — Aldehydes and Ketones: Nucleophilic Addition Reactions (`aldehydes-and-ketones`)

**Run:** 2026-07-29 · chapter version 1 · four personas (Instructor 6.4, Struggling Student 5.2, Accessibility 7.2, Visual Preference 5.6), all envelopes schema-valid · full persona evidence in [persona-envelopes/](persona-envelopes/)

## Compact editorial view

**Baseline publication readiness: BLOCKED** (computed, not averaged)

Two blockers set the verdict:

1. **instr-001 (chemical-accuracy, the chapter's only chemistry error):** the conjugate-addition prose classed "the common hydride reagents" as 1,2-selective toward enones. False for NaBH₄ — the chapter's own default reductant — which gives substantial conjugate reduction (the reason Luche conditions exist). **Corrected same-day.**
2. **access-001 (interactive-fallback, platform-wide):** the four `structure_scaffold` drawing items have no non-pointer response path; the type's declared `nonvisual_response_mode` (`structured_molecule_entry`) is unimplemented in the student frontend. Identical to the standing ticket on chapters 1/11/15/16/17/18. **Unresolved — platform dependency, not chapter authoring.**

**Zero wrong answer keys** (all 18 surfaced keys verified correct by the instructor persona; two personas independently re-validated every SMILES with RDKit). **Zero accessibility answer leaks** (repository guard + manual review).

**Dominant non-blocking theme (3 of 4 personas):** every *process* — the master mechanism's electron flow, the condensation intermediates, the 1,2-vs-1,4 fork, spectra, the protect/react/deprotect cycle — is carried by prose plus endpoint molecule cards; all three mechanism videos are deferred (hidden, render-null, verified harmless today). This is the same **visual-scaffolding cluster** recorded open on chapters 14–18 (rec-008), scheduled work rather than a gate because the prose carries the chemistry completely.

**Corrections applied (12 groups, same-day):** hydride/enone selectivity rewritten with LiAlH₄-vs-NaBH₄/Luche specifics; gem-diol glossed at first use (sections 2 and 3) with forward pointers; alpha/beta carbons, the 1,4 counting origin, enol/enolate/tautomerization, "soft," and kinetic-vs-thermodynamic control all defined at first use; pH-4.5 rationale grounded in real speciation (pKaH ≈ 10–11, rate-product framing) and the pH-2 distractor explanation aligned; both IUPAC naming items made text-only (the correct answer and a distractor had carried byte-identical structure renders) and one naming style per item; racemic outcome stated where the stereocenter forms (prose + alt text + practice check); Bürgi–Dunitz trajectory named and corrected to ~107°; ketone-inertness absolute softened with the Baeyer–Villiger exception; level-3 hints on all four drawing items no longer hand over the answer SMILES; both error_repair accessible descriptions now describe their molecule stimulus; MVK alt text maps locants to alpha/beta; six wikipedia_title values underscored (house convention — compiled links previously contained raw spaces).

**Post-correction estimate (not a new persona verdict): BLOCKED on access-001 alone.** All chapter-authored blockers and verified errors are resolved; setting the platform ticket aside the chapter is estimated **ready with minor revisions**, headlined by rec-008 (visual scaffolding) and rec-015 (assessment coverage: IR/¹³C, ozonolysis, NaBH₄-vs-LiAlH₄ selection, reasoning-level oxidation item).

### Ranked recommendations (summary)

| Rec | Sev | Need | Intervention | Status |
|---|---|---|---|---|
| rec-001 | blocker | Hydride/enone selectivity wrong for NaBH₄ | prose-edit | **applied** |
| rec-002 | blocker | structure_scaffold non-drawing input path | keyboard-alternative (platform) | open (platform) |
| rec-003 | high | Naming items: duplicate/mismatched option structures | prose-edit | **applied** |
| rec-004 | high | Gem-diol used before defined | prose-edit | **applied** |
| rec-005 | high | Undefined load-bearing vocabulary | prose-edit | **applied** |
| rec-006 | high | pH-4.5 speciation misconception | prose-edit | **applied** |
| rec-007 | med | Deferred-video blocks: guard before unhiding | instructor-note | recorded |
| rec-008 | high | Visual-scaffolding cluster (10 process depictions) | static-image-sequence | scheduled |
| rec-009 | high | practice_check never reaches reader | alternate-activity (compiler) | open (platform) |
| rec-010 | high | accessible_description not rendered by delivery panels | text-equivalent (renderer) | open (platform; PROVED on ch16) |
| rec-011 | med | Racemic outcome unstated | prose-edit | **applied** |
| rec-012 | med | Drawing-item hints reveal answer | prose-edit | **applied** |
| rec-013 | med | error_repair stimuli undescribed | structured-chemical-description | **applied** (authoring half) |
| rec-014 | med | 105° unnamed/off-value | prose-edit | **applied** |
| rec-015 | med | Assessment coverage gaps | added-practice | scheduled |
| rec-016 | med | Oxime/hydrazone/Wolff-Kishner/Baeyer-Villiger scope | instructor-note | recorded (+absolute softened) |
| rec-017 | low | Naming-style mixing in items | prose-edit | **applied** |
| rec-018 | low | Reader heading hierarchy skips h3 | platform renderer | open (platform) |
| rec-019 | low | MVK alt text lacks alpha/beta | sufficient-alt-text | **applied** |
| rec-020 | low | Wikipedia URLs with raw spaces | prose-edit | **applied** |
| rec-021 | low | No teacher_optional/priority metadata | instructor-note | recorded |

### Sufficient as is (no new asset needed)

- Hidden deferred-video blocks **today** — `is_hidden:true` blocks render null (code-verified); nothing broken reaches a student.
- Preparation section's review framing — both tiers already state these are earlier-course reactions read in the synthetic direction.
- Molecule alt texts chapter-wide (13/13 substantive, answer-neutral).
- The single Wittig E/Z scope sentence.
- mol-cyclohexanone appearing once — adding identical re-renders would trade one persona's finding for another's (see disagreements).

### Disagreements (retained, with resolution)

1. **Do deferred video blocks harm students today?** Instructor: yes, empty players with storyboard captions. Accessibility + Visual: no — hidden blocks render null (code evidence). *Resolution:* render-null verified; treated as a future-guard note (rec-007), with the content gap carried by rec-008.
2. **Repeat figures: more or fewer?** Instructor wants cyclohexanone repeated in each section that reasons from it (instr-020); Visual persona flags verbatim repeats as attention-eroding filler (visual-014). *Resolution:* no change; the durable answer is re-annotated (not verbatim) reuse, folded into rec-008.
3. **Is the deferral note's "prose and figures carry the content" claim true?** Visual: figures don't (no transformation depicted). Accessibility: prose alone does, accessibly. Student: prose states every step but can't be self-checked. *Resolution:* chemistry content fully present; representational support is the open need (rec-008).

## Full evidence view

Complete location-anchored findings, verbatim per persona, are preserved in:

- [persona-envelopes/instructor.json](persona-envelopes/instructor.json) — 20 findings (1 blocker, 7 high, 8 medium, 4 low)
- [persona-envelopes/struggling-student.json](persona-envelopes/struggling-student.json) — 16 findings (0 blocker, 6 high, 8 medium, 2 low)
- [persona-envelopes/accessibility.json](persona-envelopes/accessibility.json) — 7 findings (1 blocker, 1 high, 3 medium, 2 low… access-005 low, access-006 low, access-007 low)
- [persona-envelopes/visual-preference.json](persona-envelopes/visual-preference.json) — 15 findings (0 blocker, 5 high, 8 medium, 2 low)

Orchestrator integrity check: **orchestrator-001** — compiled Wikipedia links carried raw spaces (`/wiki/Carbonyl group`) because `wikipedia_title` was authored with spaces against the underscore house convention; independently observed by the student persona (stud-016) and the instructor's open questions. Corrected.

## Post-correction record

Every applied change, its source findings, and its verification commands are recorded in the `corrections` object of [chapter-review.json](chapter-review.json). Verification summary:

- `[internal source reference — not in this repo] … --write-runtime` — clean, 36 questions, `verification_required: []`
- `pytest tools/topic_packages/tests/ -q` — **54 passed**
- RDKit re-validation of all 35 package SMILES post-correction — all valid
- Compiled reader spot-checks: no space-URLs remain; Bürgi–Dunitz/107°, racemic note, Baeyer–Villiger caveat, and pKaH speciation text all present; naming options structure-free
- `[internal source reference — not in this repo] --synthesized chapter-review.json` — valid

**The baseline verdict above is preserved; the post-correction estimate is not a persona verdict.** A new verdict requires a four-persona regression run.
