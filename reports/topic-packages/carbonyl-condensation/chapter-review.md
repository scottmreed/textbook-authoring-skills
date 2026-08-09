# Chapter review — Carbonyl Condensation Reactions (`carbonyl-condensation`)

- **Run:** 2026-07-30 · version 1 · four independent personas (instructor 6.8 · struggling student 5.2 · accessibility 5.2 · visual 6.2), all envelopes validator-clean
- **Baseline publication readiness: `blocked`** — computed, not averaged. Any persona blocker forces at least `major revision`; an unresolved required-access blocker forces `blocked`.
- **Corrections applied by default:** 11. The baseline verdict above is preserved.

## Compact editorial view

Baseline verdict is blocked, driven by two chapter-local chemistry blockers, two chapter-local delivery blockers, and the same three platform access blockers ch21 carries. The instructor persona verified every one of the 26 asset SMILES, every mass balance (aldol additions conserve formula, condensations lose exactly H2O, the Claisen loses exactly EtOH) and the Wieland-Miescher connectivity, and found the chapter's writing the strongest of the condensation series — but caught one error that formula checking structurally cannot catch: the chapter twice claimed octane-2,7-dione closes to a seven-membered ring, when the C3 enolate reaches C7 across only five atoms and the five-membered closure wins. Both candidate products are C8H12O isomers, so every automated check in the production pipeline passed. That claim also contradicted the chapter's own stated principle that reversible steps funnel into the strain-free closure, and the correct product was not among the matching options, so that item had no defensible answer. Separately the capstone Robinson worked example enumerated five ring atoms and called them six, and the acid-catalyzed dehydration had been written as a free secondary carbocation E1 — an error introduced during production's own coherence pass while fixing a different gap. All are corrected, along with a distractor bearing an impossible name and four definitions that existed only in a detail tier the reader does not show by default. Notably, the accessibility persona confirmed the ch22 answer-leak class was cleanly avoided: both profile descriptions were leak-free at baseline.

### Ranked recommendations

| Rec | Severity | What | Intervention | From |
|---|---|---|---|---|
| rec-001 | blocker | Correct the octane-2,7-dione ring-size claim | prose-edit | inst-001, inst-002 |
| rec-002 | blocker | Correct the Robinson ring-atom enumeration | prose-edit | inst-003, ss-003 |
| rec-003 | high | Replace the free-carbocation account of acid-catalyzed dehydration | prose-edit | inst-004 |
| rec-004 | blocker | Restore the definitions missing from the default detail tier | prose-edit | ss-001 |
| rec-005 | high | Fix the impossible distractor name and its explanation | prose-edit | inst-005 |
| rec-006 | high | Give the retrosynthesis item the target it references | new-figure | inst-006, visual-013 |
| rec-007 | high | Re-base the acidity ranking variant on values the chapter supplies | prose-edit | ss-011 |
| rec-008 | high | Show the structures in the donor/acceptor sorting items | new-figure | ss-010, visual-012 |
| rec-009 | high | Reconcile the mixed-aldol product count | prose-edit | ss-002 |
| rec-010 | high | Tighten the profile descriptions further | longer-description | inst-007 |
| rec-011 | blocker | Platform: deliver accessible_description; fix the renderer key; give drawing items a non-pointer path | text-equivalent | access-001, access-002, access-003 |
| rec-012 | high | Draw the intermediates the chapter's comparisons turn on | new-figure | ss-005, visual-004, visual-005 |

### Accessibility blockers

- access-001 (platform): authored accessible_description reaches no student-facing renderer.
- access-002 (platform): reaction-coordinate renderer reads accessibilityBundle?.description, not accessible_description.
- access-003 (platform): four blank-canvas drawing items have no non-pointer alternative; the type manifest itself declares keyboard_complete=False.

### Visual opportunities (recorded, not auto-applied)

- The coupled-equilibrium argument (shallow reversible well, deep irreversible well) is stated three times and drawn zero times, although the chapter's own question bank ships exactly that profile (visual-001).
- The prose numbers atoms in five sections and no figure carries a single number, label or highlight (visual-003).
- The pKa ladder is used as a decision rule in three sections and never shown as a scale (visual-008, ss-013).
- The Stork section instructs the reader to compare the enamine with 'an enol drawn beside it'; no enol is drawn anywhere in the chapter (visual-011).

### Sufficient as is — do not over-build

- All 26 alt texts convey chemistry rather than naming the image — no rewrite needed.
- curved_arrow site labels and bond_change_ledger atom labels are semantic rather than positional and are sufficient as non-visual equivalents.
- The per-species molecule substitution for a synthesis roadmap works as delivered for the intramolecular-aldol and Robinson sections, where the species chain is complete.
- Deferred videos compile hidden, exposing no dead controls.

### Consensus strengths

- All 26 asset SMILES valid and every mass balance exact; the Wieland-Miescher product is correctly connected with the alkene at the ring fusion and the enone conjugation in the right place.
- Both reaction_coordinate_reasoning descriptions were leak-free at baseline — the ch22 leak class was cleanly avoided.
- No lone-illustrated-option answer tell anywhere in the 52-item bank; every option set is uniformly illustrated or uniformly textual.
- Figure delivery is complete: all 26 nugget-referenced assets reach the compiled reader, one for one.
- show_hydrogens is applied with judgement — set on exactly the five small molecules where a student must count alpha hydrogens, omitted on larger skeletons.
- Nine of the fifteen question types are keyboard-complete in code; all 156 hints are text; every option carries a compound name alongside its structure.
- No annotation_font_scale defect anywhere — the ch14/ch18 oversized-stereo-glyph failure mode does not occur.

### Disagreements retained


**Whether the reaction-coordinate accessible descriptions leaked**

- *Accessibility Persona:* Leak-free and correct. The arithmetic was verified in both directions and none of the four asked-for answers is stated; this is the ch22 leak class cleanly avoided.
- *Organic Chemistry Instructor:* Still a leak: stating which climb is larger hands over the rate-determining step, which a sighted student must derive from the plotted heights.

 → **Resolution:** The accessibility persona is right that no answer was stated and right that the ch22 correction pattern was followed; the instructor is right that performing the comparison is a step the sighted student performs themselves. Resolved in the direction that satisfies both rather than adjudicating between them: the descriptions now report the plotted height of every stationary point and perform no comparison at all, which is strictly more faithful to what the figure shows.

**Whether the per-species figure substitution for synthesis roadmaps succeeds**

- *Learner with Visual Preference:* Works for the intramolecular aldol and Robinson, where the species chain is complete; fails for the Claisen, Stork and Dieckmann, where the intermediate or the second ring size is never drawn.
- *Struggling Student:* Fails generally — no intermediate is drawn anywhere in the chapter.

 → **Resolution:** The visual persona's split verdict is the more precise one and is adopted. The substitution is retained (roadmaps still render as empty images platform-wide), and the specific gaps it leaves are recorded as rec-012 rather than treated as a reason to reinstate a figure type that does not render.

## Full evidence view

The machine report `chapter-review.json` embeds all four validated persona envelopes verbatim — **70 findings total** (instructor 19, struggling student 23, accessibility 12, visual 16) — with locations, evidence and confidences, plus the ranked recommendations and the corrections record.

Per-persona summaries:


**Organic Chemistry Instructor** (score 6.8; blockers: inst-001, inst-002)

> NOT-GO as it stands, but the gap to publishable is narrow. This is the strongest-written condensation chapter I have reviewed here: the donor/acceptor framing is genuinely explanatory rather than list-based, every one of the 26 molecule assets parses in RDKit, and every mass balance I checked is exact — aldol additions conserve formula (2 x C2H4O = C4H8O2; 2 x C3H6O = C6H12O2), condensations lose exactly H2O (C4H8O2 -> C4H6O; C6H12O2 -> C6H10O; C11H16O3 -> C11H14O2), the Claisen loses exactly EtOH (2 x C4H8O2 - C2H6O = C6H10O3; C10H18O4 - C2H6O = C8H12O3), and the Robinson product SMILES is a correctly connected Wieland-Miescher skeleton with two fused six-membered rings, the alkene at the ring fusion and the enone conjugation in the right place. Ring sizes are correct everywhere I counted them except in one place, and that place blocks publication: the chapter twice claims that octane-2,7-dione closes to a seven-membered ring (3-methylcyclohept-2-enone) when the C3 enolate can reach C7 to give an essentially strain-free five-membered ring, delivering 1-acetyl-2-methylcyclopent-1-ene. That is not a debatable call — it contradicts the chapter's own stated principle that reversible steps funnel everything into the strain-free five- or six-membered closure, and the correct product is not even among the matching options, so the item has no defensible correct answer. Beyond that, one worked count in the Robinson section enumerates five ring atoms and calls them six, the acid-catalyzed dehydration is taught and assessed as a free beta-carbocation E1 rather than the enol route the mapped McMurry chapter gives, one distractor is labelled with a name no molecule can have, and the Robinson retrosynthesis item promises a target structure it never shows. Assessment breadth is excellent (52 items, 15 types, every concept covered by at least two types), but three learning objectives are never assessed and the entire mechanistic story is text-only because all five mechanism videos are deferred and hidden. Fix the octane-2,7-dione items and I would assign this chapter.

**Struggling Student** (score 5.2; blockers: ss-001, ss-003)

> The chemistry here is careful and the wrong-answer explanations are among the best I have read in this course — most distractors are diagnosed by name, and three of the four ring-counting worked examples walk atom by atom. But the chapter is delivered as ten walls of prose with every structure parked after the text, zero mechanism figures, zero delivered practice checks, and five mechanism animations that ship with empty URLs and is_hidden set. Every intermediate the chapter's central argument turns on — the tetrahedral intermediate, the alkoxide, the carbinolamine, the iminium — is described in words and never drawn. Worse, the reader defaults to the 'expanded' detail level, and several definitions I actually need (what 'condensation' means, what 'aldol' means, the addition-versus-condensation naming rule that four graded questions hinge on, what 'annulation' means, and the Dieckmann off-by-one warning) exist only in the 'standard' variant, which I would have to guess to go looking for. The capstone Robinson worked example lists five atoms and calls the count six. Two advanced free-energy-profile questions assume a skill the chapter never touches — the prose contains no energy diagram and never uses the words transition state, barrier, or rate-determining step — and one of them reports two steps for a reaction the prose says has three. As a shaky student I could follow individual sentences all day and still stall at exactly the places I would be graded.

**Accessibility Persona** (score 5.2; blockers: access-001, access-002, access-003)

> The authoring in this package is among the strongest accessibility work I have reviewed on this platform: every one of the 26 figures carries a chemistry-bearing alt text plus a genuinely structural long description, all 156 hints are text, every selectable option carries a compound name alongside its structure, the prose teaches by atom-numbering rather than by pointing at pictures, and — critically — both reaction_coordinate_reasoning items describe their profiles purely geometrically (relative heights, climb measured from the preceding valley) without ever stating step count, rate-determining step, overall classification or per-step classification. I verified the arithmetic behind both descriptions and they are correct and leak-free; the ch22 leak class has been cleanly avoided. The problem is delivery, not authoring. Three hard barriers stand between this package and a non-visual learner: (1) the authored `accessible_description` on all 52 questions is compiled and resolved into the activity envelope but no student-facing surface ever reads it; (2) the one renderer that tries — the reaction-coordinate renderer — reads the wrong key (`description` instead of `accessible_description`) and falls back to the aria-label "Schematic reaction coordinate diagram", leaving a blind student asked for four readings of a diagram they cannot perceive at all; (3) the four blank-canvas drawing items are delivered as an embedded Ketcher iframe whose own type manifest declares `keyboard_complete=False`, with the promised `structured_molecule_entry` fallback unimplemented. Separately, the reader compiler silently drops all 26 asset `long_description`s and all 10 nugget `practice_check` blocks, so the richest non-visual content in the package never reaches a reader at all. These are platform gaps, not authoring failures, but they are load-bearing here and the chapter should not publish over them.

**Learner with Visual Preference** (score 6.2; blockers: none)

> Every figure in this chapter is chemically correct, legibly drawn, and actually reaches the compiled reader — I verified all 26 assets render cleanly with RDKit at reader-scale sizes, found no annotation_font_scale defect, no crowded or label-on-structure figure, and a 100% nugget-asset delivery rate. The problem is not figure quality but figure *kind*. All 36 molecule blocks are isolated single-species skeletal structures and there is not one relational figure in the chapter: no energy profile, no labelled atom, no numbered chain, no side-by-side comparison, no marked bond. This is the only chapter of the twenty-four in the reader with zero non-molecule figure blocks, and it has the highest molecule count of any of them — nine sibling chapters carry native `reaction_coordinate` blocks. Meanwhile the prose does an unusual amount of explicitly spatial work: it numbers carbons one through six across four sections, tells the student to count ring atoms as a bond forms, instructs them to draw resonance forms, instructs them to set an enol beside an enamine, and builds its entire thermodynamic argument on a coupled-equilibrium picture (unfavourable aldol pulled by irreversible dehydration) that is stated three times and drawn zero times. The substitution of per-species molecule figures for a `synthesis_roadmap` works for the Robinson annulation and the intramolecular aldol, where the species chain is complete and the reader can follow reactant to product; it fails for the Claisen (two figures for a section whose whole point is what happens at a tetrahedral intermediate that is never drawn), the Stork (the iminium the section warns you not to forget is never shown, though a question offers it as an option), and the Dieckmann (the six-membered case is argued in prose and asked about in a question but never drawn, while the structurally identical intramolecular-aldol section draws both ring sizes). No lone illustrated option acts as an answer tell anywhere in the 52-item bank — option sets are uniformly illustrated or uniformly textual, which is a genuine strength.

## Post-correction record (2026-07-30, same run — not a new persona verdict)

Corrections were applied by default per skill policy; the baseline verdict above is preserved. **Post-correction readiness estimate: `major revision`** — Not a new persona verdict. Every chapter-local blocker is resolved and verified; the estimate is held at major revision solely because the three platform access blockers remain open. Those three are identical in every already-published chapter of this series, so on that axis this chapter is at parity with the live chapters. A new verdict requires a separate four-persona regression run.

### Applied

1. **inst-001** — Re-based ch23-match-diketone-to-ring on four substrates with unambiguous favoured closures (hexane-2,5-dione, heptane-2,6-dione, octane-3,6-dione, nonane-3,7-dione) forming a clean ring-size x substituent grid; removed octane-2,7-dione and the seven-membered product entirely.
2. **inst-002** — Re-based the intramolecular-aldol practice_check on nonane-3,7-dione and added the missing generalisation to the expanded prose: when more than one closure is reachable the five- or six-membered ring wins regardless of which enolate is drawn first, worked through octane-2,7-dione itself as the illustration. *(partially addresses inst-001)*
3. **inst-003, ss-003** — Corrected the Robinson ring enumeration to name all six atoms in order and identified the side-chain ketone carbon as the one that becomes the new ring's carbonyl.
4. **inst-004** — Replaced the free-beta-carbocation account of acid-catalyzed dehydration with the enol route, and rewrote ch23-addition-vs-dehydration-v2 accordingly: the carbocation feature is now an enolization feature with a corrected key, the redundant protonation row removed, and feedback and hints rewritten.
5. **inst-005** — Replaced the impossible '4-Methylpentane-2,4-dione' distractor with 4-hydroxy-4-methylpent-1-en-3-one, a true isomer of the starting material, and corrected its wrong-answer explanation's atom bookkeeping.
6. **inst-007** — Rewrote both profile accessible descriptions to report the plotted height of every stationary point and perform no comparison. *(partially addresses access-002)*
7. **ss-001** — Added the definitions of condensation, aldol, the aldol-addition versus aldol-condensation naming rule, and annulation to the expanded detail tier, which is the tier the reader shows by default.
8. **ss-002** — Reconciled the mixed-aldol product count at four-to-two across the overview and mixed-aldol sections, distinguishing possible products from isolated product.
9. **ss-011** — Re-based ch23-rank-michael-donors-v2 on the five acidity values the chapter actually supplies, removing malononitrile and diisopropylamine.
10. **ss-010** — Added structure_smiles to every item in both donor/acceptor categorize items and updated their accessible descriptions. *(partially addresses visual-012)*
11. **inst-006** — Added the bicyclic enone as molecule_smiles on ch23-robinson-retrosynthesis and rewrote its prompt and accessible description so the target it analyses is present. *(partially addresses visual-013)*

### Remaining high priority

- access-001, access-002, access-003 — platform access blockers, identical in every published chapter of this series.
- rec-012 — no reaction intermediates are drawn anywhere; recorded as the highest-value deferred figure work.
- visual-001/003/008/011 — energy profile, atom numbering, pKa scale, and the enol-beside-enamine comparison the prose instructs but the page cannot support.

### Verification

- compile_topic_package --write-runtime — clean, verification_required empty
- tools/topic_packages/tests — 62 passed
- backend question-pipeline suites (7 files) — 177 passed
- RDKit re-parse of every asset SMILES and every option/answer-key SMILES — all valid
- lone-illustrated-option guard across all questions — none
- textbook-profiles clobber re-merged — 18 topics present
