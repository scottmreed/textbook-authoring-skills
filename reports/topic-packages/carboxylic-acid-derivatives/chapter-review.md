# Chapter review — Carboxylic Acid Derivatives (`carboxylic-acid-derivatives`)

- **Run:** 2026-07-30 · version 1 · four independent personas (instructor 7.2 · struggling student 5.6 · accessibility 4.2 · visual 6.0), all envelopes validator-clean
- **Baseline publication readiness: `blocked`** — computed, not averaged. Any persona blocker forces at least `major revision`; an unresolved required-access blocker forces `blocked`.
- **Corrections applied by default:** 4. The baseline verdict above is preserved.

## Compact editorial view

Baseline verdict is blocked, driven by two chapter-local blockers and three platform access blockers. The instructor persona independently re-parsed all 21 asset SMILES and all 48 answer keys in RDKit and found the chemistry otherwise sound — every formula matches its stated identity, both energy-profile keys read correctly off their own control points, and the curved-arrow site indices map exactly onto the SMILES atom order. The two chapter-local blockers were a genuinely wrong causal claim (a Grignard adds twice because the ketone is 'more reactive' than the acid chloride, which inverts the chapter's own reactivity ladder and is additionally circular, since the ketone IS the acid chloride's substitution product) and two recognition items whose four options each drew a different compound, so the key was the only option whose picture matched the stem. Both are corrected. A third defect was reported independently by all four personas: the chapter's only multi-step figure, the acid-to-amide synthesis roadmap, compiled to a visible image block with an empty URL — a caption and alt text promising a figure that renders as nothing. It has been replaced with a three-species molecule sequence and its reagent rationale moved into prose. The remaining blockers are platform-wide and identical in every already-published chapter of this series.

### Ranked recommendations

| Rec | Severity | What | Intervention | From |
|---|---|---|---|---|
| rec-001 | blocker | Correct the double-Grignard explanation | prose-edit | inst-001, ss-005 |
| rec-002 | blocker | Fix the two cyclic-derivative recognition items | prose-edit | inst-003, visual-015 |
| rec-003 | high | Deliver the acid-to-amide sequence as figures that render | new-figure | inst-002, ss-008, access-005, visual-001 |
| rec-004 | blocker | De-leak both energy-profile accessible descriptions | longer-description | access-001, access-002 |
| rec-005 | blocker | Platform: deliver accessible_description to the workspace | text-equivalent | access-006, access-002 |
| rec-006 | blocker | Platform: non-pointer path for blank-canvas drawing items | keyboard-alternative | access-003 |
| rec-007 | high | Reconcile the leaving-group rule with saponification | prose-edit | ss-002 |
| rec-008 | high | Reconcile the IR frequency-tracks-reactivity rule with its own counterexample | prose-edit | ss-010 |
| rec-009 | high | Nitrile family promised but never taught or assessed | prose-edit | ss-001, visual-009 |

### Accessibility blockers

- access-001 (chapter-local, CORRECTED): both profile descriptions stated the step count.
- access-002 (platform): reaction-coordinate renderer reads the wrong accessibility key, so the profile is announced only as 'Schematic reaction coordinate diagram'.
- access-003 (platform): four blank-canvas drawing items have no non-pointer alternative.

### Visual opportunities (recorded, not auto-applied)

- The reactivity ladder is the chapter's organising metaphor and is never drawn — four ungrouped structure cards do not read as a ranking (visual-004, ss-013).
- No figure anywhere shows a curved arrow, although the chapter teaches one mechanism throughout and describes each arrow's origin and destination in prose (visual-003, inst-014).
- The spectroscopy section carries five repeat structures and no spectral information; a wavenumber number line would replace its densest paragraph (visual-005, visual-006).

### Sufficient as is — do not over-build

- Molecule alt texts state connectivity rather than naming the image and are usable readouts on their own — no rewrite needed.
- Deferred videos compile hidden with empty URLs, so no dead controls are exposed; the deferral handling is correct as is.
- The tetrahedral-intermediate figure is placed correctly beside the prose that needs it and needs no change.

### Consensus strengths

- All 21 asset SMILES and all 48 answer keys verified correct in RDKit; every mass balance checked is exact.
- No option set uses positional 'Structure A/B/C/D' labels, and every illustrated option set is uniformly illustrated — no lone-illustrated-option answer tell anywhere in the bank.
- Every question type used is keyboard-complete through labelled Selects and IconButtons; no activity is drag-only, hover-only, or motion-dependent.
- bond_change_ledger items are fully answerable without seeing the structure — atom_labels are self-describing text rendered as a list.
- The paired energy-profile questions deliberately put the rate-determining step in step 1 in one and step 2 in the other, which a memoriser fails.
- All 48 questions carry a three-level hint ladder whose level-1 hints ask rather than tell.

### Disagreements retained


**Whether the empty-URL roadmap is a chapter defect or a platform gap**

- *Organic Chemistry Instructor:* Chapter-visible defect: the deferred videos were compiled is_hidden while the roadmap was not, so students are shown a broken figure.
- *Learner with Visual Preference:* Platform gap: the reader builder emits synthesis_roadmap as an image with url:'' and drops the spec, so no authoring choice could have rendered it.

 → **Resolution:** Both are right about different layers, and the chapter-local half is actionable now. Rather than wait on the renderer, the roadmap asset was removed and replaced with three molecule assets that do render, with its reagent rationale and caveats moved into prose. The platform behaviour is recorded for the renderer ticket.

## Full evidence view

The machine report `chapter-review.json` embeds all four validated persona envelopes verbatim — **72 findings total** (instructor 25, struggling student 19, accessibility 10, visual 18) — with locations, evidence and confidences, plus the ranked recommendations and the corrections record.

Per-persona summaries:


**Organic Chemistry Instructor** (score 7.2; blockers: inst-001, inst-003)

> NOT-GO as it stands, but the gap to publishable is small. I independently parsed and canonicalized all 21 asset SMILES, the 3 roadmap nodes, the 3 reaction-coordinate minima, and every structure_smiles/molecule_smiles/answer_key SMILES in all 48 question sets with RDKit: every one is valid, every molecular formula matches its stated identity, and every product/reactant claim I checked is mass- and charge-balanced (acetic anhydride C4H6O3 matches the C4H6O3 in the IR question; propanamide and DMF are correctly both C3H7NO so the N-H band count is genuinely load-bearing; sodium stearate is C18; the acid-chloride product ladder ethanol/acetone/tert-butanol/ethyl acetate is correct for LiAlH4 / Me2CuLi / excess MeMgBr / EtOH-pyridine). All 24 surfaced answer keys are chemically correct, the two reaction-coordinate profiles' rate-determining-step keys are correctly read off their own control points (step 1 for the 8-vs-6 profile, step 2 for the 22-vs-25 profile), the curved-arrow site indices map exactly onto the SMILES atom order, and the compiled question-set is byte-identical to the package. The reactivity ladder, saponification stoichiometry, DMF rotational barrier, thioester orbital argument, and the entire IR section are accurate. Two things block publication. First, one genuinely wrong chemistry claim: nugget-acid-halide-reactions tells students a Grignard reagent adds a second time because the ketone is 'more reactive' than the acid chloride, which inverts the chapter's own reactivity ladder. Second, both lactone/lactam recognition items render a different compound under each option, so the correct option is the only one whose picture matches the compound named in the prompt and can be chosen with no chemistry at all. Beyond those, the chapter over-generalizes two heuristics ('the weaker base is expelled', 'interconversions never run up the ladder') that its own later sections and its own distractor reagent list contradict, ships no worked example and no curved-arrow mechanism figure for its central mechanism, and delivers a broken empty image where the synthesis roadmap should be. Fix the two blockers and qualify the two heuristics and I would assign this chapter.

**Struggling Student** (score 5.6; blockers: none)

> The chapter is well organized around one mechanism and one reactivity ladder, and the question bank is genuinely broad (48 items, 15 types, every concept assessed), but for a student with weak prerequisites the reader itself gives almost nothing to hold on to. Eleven long prose sections arrive with no checkpoints, no worked examples, no summary and no ladder graphic; the eleven per-nugget practice checks that exist in the source package are never compiled into the reader, and the one synthesis roadmap compiles to an empty image block. Several places actively mislead me: the chapter states 'the weaker base is expelled' as the single principle governing every reaction, then has alkoxide (the stronger base) expelled in saponification with only a subordinate clause of justification; the IR section tells me frequency order equals reactivity order and then gives me an ester above a ketone; the acid-halide section says a ketone is 'more reactive' than the acid chloride it came from, one section after teaching me acid chlorides are the most reactive of all. The curved-arrow question lets me draw one arrow when the prose just told me the step takes two. Acid-catalysed substitution and amide-to-amine reduction are asserted in single sentences and then assessed by blank-canvas drawing questions. Nothing is strictly impossible to answer — the hint ladders are consistently three levels and usually rescue me — so I report no hard blocker, but I would stall, reread, and guess in at least six identifiable places.

**Accessibility Persona** (score 4.2; blockers: access-001, access-002, access-003)

> The authoring in this package is unusually accessibility-aware: every asset carries both an alt_text and a long_description, every question carries an accessible_description, no activity is drag-only or hover-only, no option set uses positional "Structure A/B/C/D" labels, and every question type in the bank (categorize, matching, rank, route builder, curved arrow, bond-change ledger, comparison matrix, structured reasoning) is keyboard-complete through labelled Selects and IconButtons. The problem is almost entirely one of delivery and of one question type. Three barriers block publication. First, both reaction_coordinate_reasoning questions open their accessible_description with "A two-maximum energy profile", which hands over step_count — the first thing the question asks — while omitting the relative heights that the other three asks (rate-determining step, step types, overall) depend on. Second, that description never reaches the learner anyway: ReactionCoordinateQuestionRenderer looks up envelope.question.accessibilityBundle?.description while the package (and the compiled bundle) key is accessible_description, so the SVG falls back to the generic label "Schematic reaction coordinate diagram", and the minima labels sit in <text> inside an svg with role="img", where assistive technology cannot reach them — the stimulus is simply absent non-visually. Third, four structure_scaffold questions require drawing on a blank Ketcher canvas embedded as an iframe with no typed, spoken, or keyboard-composed alternative offered by the renderer. Beyond the blockers, the compiler drops content the authors wrote specifically for non-visual access: all 23 assets' long_description fields are absent from the compiled reader (molecule and reaction_coordinate blocks carry alt_text only), the synthesis roadmap compiles to an image block with an empty url so no figure exists at all, all 11 nugget practice_checks vanish, and no question-workspace renderer consumes accessible_description — questionBankApi declares the field with zero consumers. The chapter is currently available:false, so none of this is live yet.

**Learner with Visual Preference** (score 6.0; blockers: none)

> The chapter is figure-dense by count (21 assets, 30 figure cards in the compiled reader) but almost monotonously so by kind: 20 of the 21 assets are single static molecules, and the two non-molecule figures are the chapter's only attempt to show a relationship. One of those two — the synthesis roadmap that carries the chapter's central 'you can only run down the ladder, so activate first' idea — compiles to an image block with an empty URL and no asset_id, so a student sees italic alt text where the three-structure sequence should be. The other, the addition–elimination energy profile, renders with both end labels chopped off by the canvas edge ('etyl chloride + methoxide' on the left, 'Methyl acetate + c…' on the right). Beyond those two delivery defects, the pattern is that every idea in this chapter that is inherently a relationship — electron flow through the tetrahedral intermediate, the sp²→sp³ geometry change, the four-family reactivity ordering, amide C–N delocalization and its 20 kcal/mol rotation barrier, the carbonyl-stretch number line, the polymer repeat unit — is asserted in prose and illustrated with unannotated single structures that show none of it, with the three animations that would have carried it deferred and hidden. Meanwhile acetyl chloride and methyl acetate are each rendered five separate times with identical captions and alt text, and the spectroscopy section is four repeat structures with no spectral information at all. Legibility of the individual molecule renders is good (I rendered all 21 through the platform's own renderer): no annotation_font_scale anywhere, no oversized stereo glyphs, no label collisions — the one weak render is sodium stearate, a hairline 18-carbon chain whose carboxylate labels shrink to a few pixels at the reader's 180px card height. On the assessment side the option art is disciplined: across all 48 questions, every option/card/item list is either uniformly illustrated or uniformly text, so there is no lone-illustrated-option tell — but two lactone/lactam items give the answer away a different visual way, and six recognition and ranking items ask students to classify structures presented only as condensed formulas.

## Post-correction record (2026-07-30, same run — not a new persona verdict)

Corrections were applied by default per skill policy; the baseline verdict above is preserved. **Post-correction readiness estimate: `major revision`** — Not a new persona verdict. Every chapter-local blocker is resolved and verified; the estimate is held at major revision solely because the three platform access blockers remain open. Those three are identical in every already-published chapter of this series, so on that axis this chapter is at parity with the live chapters. A new verdict requires a separate four-persona regression run.

### Applied

1. **inst-001** — Rewrote the double-Grignard explanation in both the standard and expanded tiers: removed the claim that the ketone is more reactive than the acid chloride and the circular 'more electrophilic than the acid chloride's substitution product would suggest', and replaced them with the correct reason plus an explicit note that the ladder ranks only the heteroatom-substituted derivatives. *(partially addresses ss-005)*
2. **inst-003** — Set all four options in ch21-recognize-lactone and ch21-recognize-lactone-v2 to show the subject compound (γ-butyrolactone and caprolactam respectively), so the options differ only in their claims. Updated both accessible descriptions to state that the structure is the same throughout. *(partially addresses visual-015)*
3. **inst-002** — Replaced the empty-rendering roadmap-acid-to-amide asset with two new molecule assets (mol-benzoic-acid, mol-n-methylbenzamide) which, with the existing mol-benzoyl-chloride, present the sequence in order; moved the roadmap's reagent rationale (why SOCl2 drives to completion, why a second equivalent of amine is needed) and its caveats into the section's expanded prose. *(partially addresses ss-008, access-005, visual-001)*
4. **access-001** — Rewrote both energy-profile accessible descriptions to give the plotted height of every stationary point without stating the step count, the rate-determining step, or any energetic classification. *(partially addresses access-002)*

### Remaining high priority

- access-002, access-003, access-006 — platform access blockers, identical in every published chapter of this series.
- rec-007, rec-008, rec-009 — high-severity pedagogical gaps recorded but deliberately not auto-applied (scope, not error).

### Verification

- compile_topic_package --write-runtime — clean, verification_required empty
- tools/topic_packages/tests — 62 passed
- backend question-pipeline suites (7 files) — 177 passed
- RDKit re-parse of every asset SMILES and every option/answer-key SMILES — all valid
- lone-illustrated-option guard across all questions — none
- textbook-profiles clobber re-merged — 18 topics present
