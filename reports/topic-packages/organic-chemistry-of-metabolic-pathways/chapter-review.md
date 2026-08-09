# Chapter review — The Organic Chemistry of Metabolic Pathways (`organic-chemistry-of-metabolic-pathways`)

_Reviewed 2026-07-30 · chapter version 1 · personas: Instructor, Struggling Student, Accessibility, Visual Preference_

**Publication readiness: blocked**

Chapter 29 is a strong, unusually well-documented chapter carrying a small number of load-bearing chemistry errors and one systemic delivery failure, and it cannot publish as it stands. All four personas independently praised the same things: the authored long descriptions are mechanism-level, the trouble spots name the right misconceptions, the wrong-answer explanations teach the discriminating criterion, and the figures are unusually honest about what they do not show. Against that, the instructor found five blocking chemistry errors - a fabricated rationale for why FAD rather than NAD+ is used, an invalid derivation of alkene geometry from facial relationship, a thiamine diphosphate drawn as a monophosphate with a sulfur-free formula, water invented as a product of the GAPDH step, and the wrong enantiomer of glyceraldehyde 3-phosphate in two question items - and the struggling-student persona found a sixth in the terse tier of the citric acid cycle section, which contradicts the alpha-versus-beta discrimination the previous section is built on. Independently, the accessibility persona found that the reader renders only alt text: the mechanism-level descriptions authored for all 44 figures are compiled into the blocks and then discarded at render for 41 of them, so the chemistry a non-visual learner needs exists in the data and is unreachable in the product. Two required activity types - structure drawing and hotspot selection - have no non-visual path, and the structure-drawing gap is a platform capability this chapter cannot supply, which is what forces the verdict to blocked rather than major revision. The visual persona's finding is different in kind and worth separating: the chapter's figures are individually good but never comparative, so three arguments the chapter makes by comparison, and assesses by comparison, are never shown as one.

### Top blockers

- **[BLOCKER] Every reaction (24) and molecule (8) block in the compiled reader carries a full content.** (Accessibility, `nugget-biochemical-energy-and-coupled-reactions`, `rxn-atp-phosphoryl-transfer`, `access-001`)
- **[BLOCKER] Because alt_text is the only description the reader surfaces, it has to carry the chemistry alone - and for roughly 14 of the 24 reaction figures it names only the species on each side of the arrow and never states which bond forms or breaks.** (Accessibility, `nugget-beta-oxidation-of-fatty-acids`, `rxn-thiolase-retro-claisen`, `access-002`)
- **[BLOCKER] The 5 synthesis_roadmap figures render as a single generated SVG in which every node label, per-arrow reagent, per-arrow teaching note and the caveat footer are SVG text elements baked into an image.** (Accessibility, `nugget-glycolysis-mechanisms`, `roadmap-glycolysis`, `access-003`)
- **[BLOCKER] Both structure_scaffold questions use scaffold 'blank_canvas' and are delivered through the ketcher workspace.** (Accessibility, `glycolysis-mechanisms`, `ch29-retro-aldol-product`, `access-005`)
- **[BLOCKER] The chapter's stated reason for using FAD rather than NAD+ in the two alpha,beta-dehydrogenations is that no hydride can leave and that flavin accepts electrons one at a time.** (Instructor, `coenzymes-as-organic-reagents`, `nugget-coenzymes-as-organic-reagents`, `rxn-acyl-coa-dehydrogenase`, `inst-001`)
- **[BLOCKER] Two separate errors.** (Instructor, `beta-oxidation-of-fatty-acids`, `nugget-beta-oxidation-of-fatty-acids`, `rxn-enoyl-coa-hydratase`, `inst-002`)
- **[BLOCKER] The asset titled 'Thiamine diphosphate' carries a SMILES that RDKit resolves to C12H17N4O4PS - a single phosphorus.** (Instructor, `oxidative-decarboxylation-of-pyruvate`, `mol-thiamine-diphosphate`, `inst-003`)
- **[BLOCKER] The alt_text and long_description both state that water is a product of the glyceraldehyde 3-phosphate dehydrogenase step.** (Instructor, `metabolic-step-to-mechanism-inventory`, `rxn-triose-phosphate-oxidation`, `inst-004`)
- **[BLOCKER] Two question items display a stereochemically specified structure labelled 'glyceraldehyde 3-phosphate' that is the wrong enantiomer.** (Instructor, `glycolysis-mechanisms`, `ch29-schiff-base-arrow-v2`, `inst-005`)
- **[BLOCKER] The terse variant of the citric acid cycle section states that both carbon dioxides leave by beta-keto acid decarboxylation.** (Struggling Student, `nugget-citric-acid-cycle-mechanisms`, `citric-acid-cycle-mechanisms`, `stu-001`)

### Top 5 recommended changes

1. **Replace the fabricated 'no hydride available' rationale for FAD** — The chapter's reason for using FAD rather than NAD+ in the two alpha,beta-dehydrogenations is mechanistically wrong: acyl-CoA dehydrogenase and succinate dehydrogenase both transfer the beta hydrogen as a hydride to flavin N5 while a general base takes the alpha proton. The real reason is the redox potential of the couple. → **prose-edit** (prose, blocker)
2. **Stop deriving alkene geometry and enantiomeric outcome from facial relationship alone** — The chapter states that anti removal 'is why' the E alkene is the sole product and that anti addition 'produces the S enantiomer only'. In a freely rotating acyclic chain neither inference is valid; the outcome comes from the conformation and face the enzyme enforces. The syn/anti assignments for acyl-CoA dehydrogenase and enoyl-CoA hydratase are also disputed by the reviewer. → **prose-edit** (prose, blocker)
3. **Draw the real thiamine diphosphate and fix its formula** — The asset titled 'Thiamine diphosphate' carries a SMILES that resolves to a monophosphate (C12H17N4O4PS) while its title, alt_text and long_description all promise a diphosphate, and the formula asserted in the description omits sulfur entirely. → **prose-edit** (figure, blocker)
4. **Remove the invented water from the GAPDH figure description** — The alt_text and long_description of rxn-triose-phosphate-oxidation state that water is a product. No water is formed; the drawn structures balance to a two-hydrogen difference that NAD+ carries away, which the same paragraph then double-counts. → **prose-edit** (figure, blocker)
5. **Correct the glyceraldehyde 3-phosphate enantiomer in two question items** — ch29-schiff-base-arrow-v2 and a distractor in ch29-retro-aldol-product display (S)-glyceraldehyde 3-phosphate - the L-isomer - while naming it as the substrate of GAPDH and as the aldolase cleavage fragment. The chapter's own figures correctly use the (R) D-isomer. → **prose-edit** (assessment, blocker)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 6.0/10 | 5 | Structures and residues are right; five load-bearing mechanism errors are not. |
| Struggling Student | 5.4/10 | 1 | Good teaching that never reaches me: no practice, no objectives, no trouble spots in the reader. |
| Accessibility Persona | 5.2/10 | 4 | Excellent authored descriptions, discarded at render for 41 of 44 figures. |
| Learner with Visual Preference | 6.3/10 | 0 | Captions promise what the pictures cannot deliver; nothing comparative is ever shown side by side. |

### Affected sections & assets

`ch29-aldol-ledger`, `ch29-atp-bond-cleaved`, `ch29-citrate-alcohol-class-v2`, `ch29-conjugate-addition-site`, `ch29-plp-electron-sink`, `ch29-reaction-family-inventory`, `ch29-retro-aldol-product`, `ch29-schiff-base-arrow`, `ch29-schiff-base-arrow-v2`, `ch29-synthesis-vs-degradation`, `ch29-thiamine-role`, `mol-thiamine-diphosphate`, `nugget-amino-acid-catabolism-and-transamination`, `nugget-beta-oxidation-of-fatty-acids`, `nugget-biochemical-energy-and-coupled-reactions`, `nugget-citric-acid-cycle-mechanisms`, `nugget-coenzymes-as-organic-reagents`, `nugget-fatty-acid-biosynthesis`, `nugget-glycolysis-mechanisms`, `nugget-metabolic-step-to-mechanism-inventory`, `nugget-oxidative-decarboxylation-of-pyruvate`, `nugget-thioester-activation`, `pdb-citrate-synthase`, `pdb-fatty-acid-synthase`, `roadmap-beta-oxidation`, `roadmap-fatty-acid-elongation`, `roadmap-glycolysis`, `rxn-acyl-coa-dehydrogenase`, `rxn-aldolase-retro-aldol`, `rxn-atp-phosphoryl-transfer`, `rxn-citrate-synthase-aldol`, `rxn-enoyl-coa-hydratase`, `rxn-fad-dehydrogenation`, `rxn-glycerol-to-dhap`, `rxn-isocitrate-oxidative-decarboxylation`, `rxn-malonyl-decarboxylative-claisen`, `rxn-pyruvate-to-acetyl-coa`, `rxn-thiamine-ylide-addition`, `rxn-thiolase-retro-claisen`, `rxn-triose-phosphate-oxidation`, `site-aldolase`, `site-aspartate-aminotransferase`, `site-citrate-synthase`, `video-aldolase-cleavage`, `video-beta-oxidation-spiral`, `video-citric-acid-cycle-carbons`

---

## Full evidence

### Independent persona reports

The four reviews below were produced in isolation — each subagent saw only its own rubric and the chapter package, never another persona's prompt or findings. They are presented separately and are not merged.

#### Organic Chemistry Instructor — 6.0/10

Not-go as it stands; a strong chapter with a small number of load-bearing chemistry errors that must be corrected first. All 32 SMILES-bearing assets parse; every molecule formula and every stereocentre checked is right except thiamine; every named catalytic residue is real and correctly assigned; the deliberate two-hydrogen imbalances are honestly captioned in five of six cases. Against that: the central 'why FAD and not NAD+' explanation is mechanistically wrong, two enzymatic stereochemistry claims rest on a causal non-sequitur, the molecule labelled thiamine diphosphate is drawn as a monophosphate with a formula that omits sulfur, one figure invents water as a product, and two questions display L-glyceraldehyde 3-phosphate while calling it the substrate of GAPDH.

**Publication blockers:** `inst-001`, `inst-002`, `inst-003`, `inst-004`, `inst-005`

**Strengths**

- Structural fidelity is high: all eight molecule assets except thiamine give correct molecular formulae, and the isoalloxazine ring is correctly drawn in its oxidised form.
- Stereochemistry is right wherever checkable against a reference, including alpha-D-glucopyranose 6-phosphate, beta-D-fructofuranose 1,6-bisphosphate, D-glyceraldehyde 3-phosphate, (Z)-cis-aconitate, (2R,3S)-isocitrate, (S)-3-hydroxybutyryl thioester and the L-Asp external aldimine. The R-versus-S contrast between beta-oxidation and biosynthesis is stated correctly in prose, roadmap and key alike.
- Every named catalytic residue is real and correctly assigned, and the anchor_atom indices in the active-site specs resolve to the right atoms in every case checked.
- The deliberate two-hydrogen imbalances are handled with unusual honesty: five of six affected figures name the coenzyme in the caption and explain the missing hydrogens in the long_description.
- The chapter is unusually good at flagging what a figure is not showing, including the cyclic-versus-open-chain caveat on the isomerase and the disordered domains in 2VZ8.
- The reaction-family assignments and numeric answer keys (2 CO2 and 3 NADH per turn, 7 passes for palmitate) are all defensible, as is the acyl-donor ranking with its pKa rationale.
- The carbon-bookkeeping caveat stating that whole-route accounting only holds from the second turn onwards is expert-level honesty most textbooks omit.

**Findings**

##### `inst-001` · blocker · chemical-accuracy

*Location:* `coenzymes-as-organic-reagents`, `nugget-coenzymes-as-organic-reagents`, `rxn-acyl-coa-dehydrogenase` · anchor: "The flavin ring, which accepts electrons singly, can do it."

*Observation.* The chapter's stated reason for using FAD rather than NAD+ in the two alpha,beta-dehydrogenations is that no hydride can leave and that flavin accepts electrons one at a time. This is not the accepted mechanism of either enzyme. Acyl-CoA dehydrogenase removes the alpha hydrogen as a proton (an active-site glutamate, Glu376 in MCAD) with concerted transfer of the beta hydrogen as a HYDRIDE to N5 of the flavin; succinate dehydrogenase is likewise hydride transfer to flavin N5. A hydride is therefore exactly what does leave. The genuine reason flavin is used is thermodynamic: the fumarate/succinate and enoyl/acyl couples sit near 0 V, far above the NAD+/NADH couple at about -0.32 V, so NAD+ could not accept the electrons.

*Learner impact.* Every student carries away a fabricated rationale that will be marked wrong in any biochemistry course and that blocks the correct thermodynamic reasoning. The claim is repeated in terse, standard and expanded prose, the practice_check answer, two asset learning_goals, two long_descriptions and the beta-oxidation roadmap note, so it is un-learnable from context and reinforced five times.

*Evidence.* nugget-coenzymes-as-organic-reagents standard: 'neither can accommodate the charge a hydride transfer would leave'. rxn-acyl-coa-dehydrogenase learning_goal: 'there is no hydride to remove from an unactivated CH2'. roadmap-beta-oxidation step 1 note: 'FAD is used rather than NAD+ because no hydride can be removed from an unactivated carbon.'

*Recommended outcome.* The chapter needs a coenzyme-choice explanation a biochemist would accept: the beta hydrogen does leave as a hydride to flavin N5 with a general base taking the alpha proton, and NAD+ cannot be used because of the redox potential of the couple. Every restatement across prose, practice, asset goals, descriptions and roadmap notes needs to move together. (confidence 0.82)

##### `inst-002` · blocker · chemical-accuracy

*Location:* `beta-oxidation-of-fatty-acids`, `nugget-beta-oxidation-of-fatty-acids`, `rxn-enoyl-coa-hydratase` · anchor: "opposite faces, which is why the E alkene is the sole product"

*Observation.* Two separate errors. (a) Acyl-CoA dehydrogenase and enoyl-CoA hydratase are reported in the enzymology literature as syn, not anti; the chapter asserts anti for both, including the roadmap note 'Anti dehydrogenation'. It gets succinate dehydrogenase and fumarase right, both genuinely anti. (b) Even where an anti claim is factually right, the causal chain drawn from it is a non-sequitur: in a freely rotating acyclic chain, anti-periplanar removal can give either E or Z depending on which conformer is held, and syn or anti addition does not by itself fix which enantiomer forms. What produces the exclusive E alkene and the single (S) alcohol is the conformation and face the enzyme enforces.

*Learner impact.* Students are taught two facts they may be examined on, and are taught to derive alkene geometry and enantiomeric outcome from facial relationship alone. That inference is invalid and will mislead them in every acyclic elimination and addition problem outside this chapter.

*Evidence.* rxn-acyl-coa-dehydrogenase long_description: 'they are removed from opposite faces, which is why the E alkene is the sole product'. rxn-enoyl-coa-hydratase long_description: 'The enzyme delivers the hydroxyl and the proton to opposite faces and produces the S enantiomer only'. nugget-coenzymes-as-organic-reagents repeats it.

*Recommended outcome.* The stereochemical outcome needs attributing to enzyme-enforced conformation and face selection rather than to syn/anti alone, with the contrast against succinate dehydrogenase and fumarase, which really are anti, made explicit. (confidence 0.78)

##### `inst-003` · blocker · chemical-accuracy

*Location:* `oxidative-decarboxylation-of-pyruvate`, `mol-thiamine-diphosphate` · anchor: "Thiamine diphosphate, molecular formula C12H18N4O7P2"

*Observation.* The asset titled 'Thiamine diphosphate' carries a SMILES that RDKit resolves to C12H17N4O4PS - a single phosphorus. That is thiamine MONOphosphate; the rendered figure shows one phosphate where the title, alt_text and long_description all promise two. Separately the formula asserted in the long_description, C12H18N4O7P2, contains no sulfur at all, which is impossible for a molecule the same sentence describes as containing a thiazolium ring. Correct ThDP is C12H18N4O7P2S as the drawn zwitterion.

*Learner impact.* The one structural figure a student has for the coenzyme of this section is the wrong compound and carries a formula that contradicts the structure beside it. A student who counts atoms - which the long_description invites - finds text and picture disagreeing, and learns a formula with no sulfur in a sulfur-containing coenzyme.

*Evidence.* SMILES parses to C12H17N4O4PS (one P, four O). Stated formula C12H18N4O7P2 has no S and two P.

*Recommended outcome.* The depicted structure and the stated formula must both become the real coenzyme - the diphosphate, with sulfur present in the formula. (confidence 0.97)

##### `inst-004` · blocker · chemical-accuracy

*Location:* `metabolic-step-to-mechanism-inventory`, `rxn-triose-phosphate-oxidation` · anchor: "to give 1,3-bisphosphoglycerate and water"

*Observation.* The alt_text and long_description both state that water is a product of the glyceraldehyde 3-phosphate dehydrogenase step. No water is formed and none appears in the figure; the drawn SMILES balances with a difference of exactly the two hydrogens taken by NAD+. The description both invents water and double-counts the missing hydrogens. Correct stoichiometry is G3P + Pi + NAD+ -> 1,3-BPG + NADH + H+.

*Learner impact.* This is a balancing figure whose stated purpose is to teach students to account for atoms across an arrow, and it models the exact error it is meant to prevent. A student who trusts the description will write a condensation with loss of water and cannot reconcile it with the structures drawn.

*Evidence.* alt_text: 'D-Glyceraldehyde 3-phosphate reacting with inorganic phosphate to give 1,3-bisphosphoglycerate and water.' RDKit mass balance shows an H2 difference only, no H2O.

*Recommended outcome.* The accessibility text must state the true stoichiometry - phosphate adds, nothing is lost, and the only unaccounted atoms are the two hydrogens NAD+ carries away. (confidence 0.97)

##### `inst-005` · blocker · chemical-accuracy

*Location:* `glycolysis-mechanisms`, `ch29-schiff-base-arrow-v2` · anchor: "Aldehyde carbon of glyceraldehyde 3-phosphate"

*Observation.* Two question items display a stereochemically specified structure labelled 'glyceraldehyde 3-phosphate' that is the wrong enantiomer. ch29-schiff-base-arrow-v2 uses 'O=C[C@@H](O)COP(=O)(O)O', which RDKit assigns (S) - L-glyceraldehyde 3-phosphate. The chapter's own asset rxn-aldolase-retro-aldol correctly draws the (R) D-isomer. ch29-retro-aldol-product carries the same wrong enantiomer as a wrong-answer distractor described as 'the other fragment' - it is that fragment's mirror image.

*Learner impact.* Students draw arrows onto, and receive feedback about, a molecule drawn with explicit stereochemistry that is the wrong compound. Because the chapter elsewhere insists on D/L and R/S correctness, the inconsistency reads as a legitimate alternative rather than an error. The distractor may also fail to match under a stereo-aware grader, so the intended feedback never fires.

*Evidence.* rdCIPLabeler returns S for the question SMILES and R for the asset SMILES; both are named glyceraldehyde 3-phosphate.

*Recommended outcome.* Every stereo-specified glyceraldehyde 3-phosphate in the question bank needs to be the D-(R) isomer the figures use, or the stereocentre left unspecified where the item says stereochemistry is ignored. (confidence 0.95)

##### `inst-006` · high · figure-accuracy

*Location:* `glycolysis-mechanisms`, `rxn-aldolase-retro-aldol` · anchor: "the substrate is a beta-hydroxy carbonyl compound"

*Observation.* The retro-aldol figure draws the reactant as cyclic beta-D-fructofuranose 1,6-bisphosphate and then describes it as 'a beta-hydroxy carbonyl compound' whose 'bond beta to the carbonyl' is cleaved. The structure drawn has no carbonyl - C2 is a hemiketal - so the pattern the caption asks the student to find is not present. The ring-opening step is never shown or named. rxn-phosphoglucose-isomerase handles the identical situation honestly ('the isomerisation happens on the open-chain forms').

*Learner impact.* The most-taught mechanism of the glycolysis section asks students to locate a carbonyl and a beta hydroxyl in a structure that shows neither, and the practice_check reinforces it. A careful student cannot follow the argument from the figure; a less careful one learns that hemiketals undergo retro-aldol directly.

*Evidence.* Reactant SMILES is the furanose; long_description: 'the substrate is a beta-hydroxy carbonyl compound, and cleaving the bond beta to the carbonyl'.

*Recommended outcome.* The open-chain keto form of fructose 1,6-bisphosphate needs to be visible at the point of the retro-aldol argument, with ring-opening named as a prior step. (confidence 0.9)

##### `inst-007` · high · figure-accuracy

*Location:* `glycolysis-mechanisms`, `site-aldolase`, `ch29-schiff-base-arrow` · anchor: "condensing the neutral amine of an active-site lysine, drawn here as butylamine, with the ketone of dihydroxyacetone phosphate"

*Observation.* The prose states that in the cleavage direction a class I aldolase condenses an active-site lysine with the C2 ketone of fructose 1,6-bisphosphate. Both supporting artefacts show the lysine condensing with dihydroxyacetone phosphate instead. DHAP is the product of the cleavage, not the species that forms the Schiff base before it, so figure and question depict the condensation direction while the prose describes the cleavage direction, without saying so.

*Learner impact.* A student who reads the section then works the figure and arrow question forms the belief that the covalent intermediate is made from DHAP, reversing the causal order of the mechanism just taught and making the practice_check answer unreconstructable.

*Evidence.* site-aldolase substrate label 'dihydroxyacetone phosphate' with arrow lys229 -> substrate_atom 2; ch29-schiff-base-arrow molecule_smiles 'OCC(=O)COP(=O)(O)O.CCCCN'.

*Recommended outcome.* The Schiff-base figure and arrow question need to act on the species the prose names, or state plainly that they show the reverse direction and why the same lysine adduct appears there. (confidence 0.88)

##### `inst-008` · high · chemical-accuracy

*Location:* `citric-acid-cycle-mechanisms`, `rxn-isocitrate-oxidative-decarboxylation` · anchor: "a cyclic six-membered transition state in which the carboxyl proton is delivered to the ketone oxygen"

*Observation.* The chapter asserts the isocitrate dehydrogenase decarboxylation goes through a cyclic six-membered transition state in which the carboxyl proton is delivered to the ketone oxygen. That transition state requires the free protonated acid. At pH 7 and in the IDH active site the substrate is oxalosuccinate - a carboxylate with no proton to deliver - and the decarboxylation is assisted by a divalent metal that stabilises the enolate; a residue then protonates C3. The uncatalysed acetoacetic acid illustration is correct; transferring it wholesale onto the enzymatic step is what a specialist would dispute.

*Learner impact.* Students get a transition state that cannot exist for the species involved, in the one step where the chapter promises the mechanism is the familiar one. It also teaches them not to check the ionisation state of a substrate before choosing a mechanism.

*Evidence.* rxn-isocitrate-oxidative-decarboxylation long_description and learning_goal both assert the six-membered TS with proton delivery; the nugget repeats it.

*Recommended outcome.* The enzymatic decarboxylation needs describing as a metal-stabilised enolate from a carboxylate substrate, kept explicitly distinct from the neutral beta-keto acid transition state taught for acetoacetic acid. (confidence 0.85)

##### `inst-009` · high · notation-consistency

*Location:* `citric-acid-cycle-mechanisms`, `rxn-citrate-synthase-aldol` · anchor: "citric acid - a central carbon carrying a hydroxyl, a carboxyl group and two CH2CO2H arms"

*Observation.* Every polycarboxylic acid in the reaction assets is drawn and named as the neutral free acid, while the prose, roadmaps and question bank consistently use the anion names, and roadmap-glycolysis specifies 'HOPO3(2-)' for the same phosphate that rxn-triose-phosphate-oxidation draws as H3PO4. NAD+ is drawn with one phosphate as O- and one as OH, so even the coenzymes are not internally consistent.

*Learner impact.* A student cannot tell whether ionisation state matters, yet it is exactly what decides whether the beta-keto acid cyclic transition state is available, whether an active-site carboxylate can act as a base, and why phosphorylated sugars are trapped in the cell. Alt-text readers get 'isocitric acid' where sighted roadmap readers get 'isocitrate'.

*Evidence.* rxn-fad-dehydrogenation alt_text 'Succinic acid converting to fumaric acid' vs roadmap nodes 'Succinate', 'Fumarate'.

*Recommended outcome.* One declared convention for ionisation state, applied across figures, alt text, roadmaps and questions, plus a statement of where ionisation state changes the mechanism. (confidence 0.86)

##### `inst-010` · high · missing-example

*Location:* `oxidative-decarboxylation-of-pyruvate`, `nugget-oxidative-decarboxylation-of-pyruvate`, `rxn-pyruvate-to-acetyl-coa` · anchor: "oxidation and transfer to coenzyme A then complete the sequence"

*Observation.* The pyruvate dehydrogenase sequence stops at the enamine and is finished with 'oxidation and transfer to coenzyme A then complete the sequence'. The oxidant is never named. Lipoic acid / lipoamide appears nowhere in the chapter, and the step in which the enamine attacks the lipoamide disulfide is silently skipped, as is the FAD/NAD+ relay at E3. The closing thesis that the chapter introduces no new reactions survives only because this arrow is not drawn.

*Learner impact.* The junction step between glycolysis and the citric acid cycle is presented with a hole where the actual oxidation happens. Students cannot answer what oxidises the two-carbon unit given that the chapter says NAD+ takes the hydrogens. The same gap recurs unflagged at alpha-ketoglutarate dehydrogenase.

*Evidence.* Nugget expanded ends 'oxidation and transfer to coenzyme A then complete the sequence'; grep for 'lipo' across the package returns nothing.

*Recommended outcome.* The oxidant of the two-carbon unit needs naming and its chemistry showing, or an explicit visible statement that a carrier step is omitted - and if omitted, the 'no new reactions' claim needs qualifying. (confidence 0.9)

##### `inst-011` · high · figure-accuracy

*Location:* `oxidative-decarboxylation-of-pyruvate`, `rxn-thiamine-ylide-addition` · anchor: "The thiamine ylide adds to pyruvate"

*Observation.* The figure titled 'The thiamine ylide adds to pyruvate' draws the intact thiazolium cation on the left with C2-H present, not the ylide. The ylide - the species the title, learning_goal, long_description, prose and question ch29-thiamine-role all identify as the nucleophile - is never depicted anywhere in the chapter. No base is shown, and the C2 hydrogen simply disappears between the two sides. The product, a 2-substituted thiazolium, is drawn correctly.

*Learner impact.* The objective for this section is 'Draw the thiazolium ylide', and the chapter provides no drawing of the thing the student is asked to draw. Students also see a hydrogen vanish without a base, which undercuts the chapter's emphasis on where each proton goes.

*Evidence.* Reactant SMILES retains C2-H ('SC=[N+]1C'); long_description says 'The ring carbon's hydrogen has been removed to give an ylide' - describing a species not in the figure.

*Recommended outcome.* The deprotonation to the ylide needs to be visible as its own step, with the base identified. (confidence 0.88)

##### `inst-012` · high · objective-alignment

*Location:* `biochemical-energy-and-coupled-reactions`, `ch29-atp-bond-cleaved` · anchor: "Coupling requires a shared intermediate"

*Observation.* Several stated learning_objectives have no assessment item: the shared-intermediate definition (the chapter's opening thesis and an explicit trouble_spot); the tautomerisation argument for pyruvate kinase irreversibility; 'State which carbons leave as carbon dioxide in a given turn' (ch29-tca-co2-count asks how many, not which); distinguishing transamination from oxidative deamination; and 'Draw the thiazolium ylide', whose only item is a multi-select.

*Learner impact.* The ideas the chapter argues hardest for are the ones a student can skip without penalty, and the practice they do get rewards recall of pathway facts over the mechanistic reasoning the chapter is built on. An instructor cannot use the bank to check whether the central concept landed.

*Evidence.* 21 unique items over 10 concepts; no question_slug references pyruvate kinase, tautomerisation, shared intermediates, or carbon provenance in the cycle.

*Recommended outcome.* Assessment coverage for the objectives that currently have none, particularly the shared-intermediate definition, the tautomerisation argument, and the provenance of the two carbons released per turn. (confidence 0.92)

##### `inst-013` · medium · chemical-accuracy

*Location:* `beta-oxidation-of-fatty-acids`, `rxn-thiolase-retro-claisen` · anchor: "A thiolate from a second molecule of coenzyme A attacks the ketone carbonyl"

*Observation.* The thiolase step is presented as direct attack by free coenzyme A thiolate. The enzyme runs a ping-pong mechanism through a covalent acyl-enzyme: an active-site cysteine thiolate attacks C3, acetyl-CoA leaves as the stabilised enolate, and only then does CoASH attack the acetyl-cysteine. The chapter is otherwise meticulous about naming covalent catalysis (aldolase lysine, GAPDH cysteine), so the omission is conspicuous.

*Learner impact.* Students learn one covalent-catalysis pattern and are then shown a step where the identical device is used but hidden. The retro-Claisen bookkeeping is correct, but the enzyme they are told about is not the one that exists.

*Evidence.* long_description: 'The thiolate attacks the ketone carbonyl to give a tetrahedral alkoxide'; roadmap step 4 repeats it.

*Recommended outcome.* Either the active-site cysteine and two-stage acyl-enzyme need to appear, consistent with aldolase and GAPDH, or the simplification needs labelling as one. (confidence 0.83)

##### `inst-014` · medium · notation-consistency

*Location:* `citric-acid-cycle-mechanisms`, `site-citrate-synthase`, `ch29-aldol-ledger` · anchor: "A thioester enolate attacks the ketone carbon of oxaloacetate"

*Observation.* The citrate synthase mechanism is taught two incompatible ways. The active-site figure commits to the ENOL (substrate SMILES 'C=C(O)SCCNC(C)=O', Asp375's note says the deprotonation produced the enol). The assessment item on the same step commits to the ENOLATE (molecule_smiles '[CH2-]C(=O)SC', prompt 'A thioester enolate attacks', answer key requiring a formal-charge change from -1 to 0). This is a real mechanistic distinction in the citrate synthase literature, and the chapter takes both sides without acknowledging a choice is being made. The thioester model also changes between the two.

*Learner impact.* A student who learns the figure's enol answer and then meets the ledger question is asked to record a formal-charge change on a species the figure says is neutral, and will get it wrong for a reason the feedback does not address.

*Evidence.* site-citrate-synthase residue note 'that deprotonation is what produced the enol drawn here' vs ch29-aldol-ledger expected row {'charge_changed','0','-1','0'}.

*Recommended outcome.* One stated position on whether the nucleophile is the enol or the enolate, applied to both figure and assessment, ideally with a sentence acknowledging the literature argues about it. (confidence 0.9)

##### `inst-015` · medium · conceptual-support

*Location:* `fatty-acid-biosynthesis`, `rxn-malonyl-decarboxylative-claisen` · anchor: "why the cell pays to add a carboxyl group it immediately discards"

*Observation.* The chapter repeatedly asks what the malonyl carboxyl group buys and answers only that it generates the enolate and drives the equilibrium. It never says where that carboxyl comes from or what it costs: acetyl-CoA carboxylase, a biotin-dependent carboxylation consuming one ATP and bicarbonate. The practice_check poses 'why the cell pays' and the model answer never states what is paid.

*Learner impact.* Students are left with the impression that decarboxylation is a free source of driving force, which is the metabolic version of the 'energy stored in a bond' misconception the chapter opens by attacking.

*Evidence.* No mention of biotin, bicarbonate, ATP or acetyl-CoA carboxylase anywhere in the package.

*Recommended outcome.* The ATP- and biotin-dependent carboxylation that makes malonyl-CoA needs stating where the 'why pay for it' argument is made, so the energy bookkeeping closes. (confidence 0.88)

##### `inst-016` · medium · sequencing

*Location:* `nugget-glycolysis-mechanisms`, `rxn-triose-phosphate-oxidation` · anchor: "an active-site cysteine thiolate adds to the aldehyde to give a thiohemiacetal"

*Observation.* Two figures sit four to six sections after the prose that needs them. rxn-triose-phosphate-oxidation is attached to the tenth section while its three-step mechanism is given in the fourth, which has no figure for it. Likewise rxn-claisen-in-the-flask sits in section ten although the fatty acid biosynthesis section makes the flask-versus-cell comparison its central argument.

*Learner impact.* The glycolysis section carries its densest mechanism as unsupported prose, while the section that already has seven figures gets a third it does not need. Students working linearly meet the comparison argument before the comparison figure exists.

*Evidence.* assets[].nugget_ids: both figures map to nugget-metabolic-step-to-mechanism-inventory; nugget-glycolysis-mechanisms has no GAPDH figure.

*Recommended outcome.* The GAPDH oxidation and the flask Claisen need to be reachable at the point the prose argues from them. (confidence 0.85)

##### `inst-017` · medium · misconception

*Location:* `nugget-metabolic-step-to-mechanism-inventory` · anchor: "There are eliminations, all of them E1cb because hydroxide is too poor a leaving group for anything else"

*Observation.* The inventory section states as a rule that the chapter's eliminations are 'all of them E1cb', with no exception and no evidence for the individual cases. It is well supported for enolase and defensible for the FAS dehydratase, but asserted rather than argued for aconitase (whose Fe-S cluster acts as a Lewis acid on the departing hydroxyl and is never mentioned), and sits uneasily beside succinate dehydrogenase, which the chapter treats as a stereospecific removal of two hydrogens rather than an E1cb.

*Learner impact.* A stated-without-exception rule is exactly what students memorise and over-apply; they will label any biological dehydration E1cb without checking whether the carbanion is actually stabilised.

*Evidence.* Nugget standard: 'There are eliminations, all of them E1cb'. roadmap-citric-acid-cycle step 2 identifies no carbanion-stabilising group and no iron-sulfur cluster.

*Recommended outcome.* Either the per-case justification that makes it a conclusion rather than a rule, or an explicit statement of the condition under which it holds. (confidence 0.8)

##### `inst-018` · medium · conceptual-support

*Location:* `nugget-citric-acid-cycle-mechanisms` · anchor: "isotopic labelling shows that the two carbons released in any given turn come from the oxaloacetate that accepted the acetyl group"

*Observation.* The chapter states the isotope-labelling result correctly but never explains why. The explanation is that citrate is prochiral - its two CH2CO2H arms are enantiotopic - and aconitase, being chiral, distinguishes them. The chapter has the vocabulary available: three sections later it explains exactly this for glycerol's two primary hydroxyls. It does not connect the two.

*Learner impact.* The most counter-intuitive claim in the section is unexplained, and the concept that would explain it is introduced afterwards. Students who ask the obvious question - the molecule looks symmetric, so how can the enzyme tell? - find no answer.

*Evidence.* Nugget expanded first paragraph; the glycerol prochirality argument in nugget-beta-oxidation-of-fatty-acids never links back.

*Recommended outcome.* The prochirality of citrate needs making explicit where the labelling result is stated, connected to the glycerol case the chapter already teaches. (confidence 0.86)

##### `inst-019` · medium · misconception

*Location:* `nugget-glycolysis-mechanisms`, `roadmap-glycolysis` · anchor: "A mutase then relocates the remaining phosphate from O3 to O2"

*Observation.* Phosphoglycerate mutase is described as relocating a phosphate along the chain, implying intramolecular migration. The mammalian cofactor-dependent enzyme does not do that: a phospho-histidine transfers a phosphate to O2 to make a 2,3-bisphosphoglycerate intermediate, from which the O3 phosphate is removed onto the histidine, so the phosphate the substrate leaves with is not the one it arrived with.

*Learner impact.* This is the one glycolytic step the chapter treats as trivial, and the one where the naive reading is wrong. Students who later meet 2,3-BPG in haemoglobin physiology have to unlearn the picture.

*Evidence.* Nugget standard and expanded; roadmap long_description 'one positional transfer of a phosphate'.

*Recommended outcome.* Wording that does not assert intramolecular migration, or a brief note that the transfer runs through an enzyme-bound phosphate and a bisphosphate intermediate. (confidence 0.85)

##### `inst-020` · medium · visual-opportunity

*Location:* `fatty-acid-biosynthesis`, `ch29-synthesis-vs-degradation` · anchor: "The two coenzymes differ by a single phosphate group on one ribose"

*Observation.* The chapter makes a structural claim about NADPH versus NADH, builds a control argument on it, and assesses it, but shows no structure of NADP+/NADPH anywhere. mol-nad-plus shows only the oxidised form; mol-fad likewise, even though the flavin argument turns on what the reduced form looks like.

*Learner impact.* Students are told to distinguish two coenzymes on a structural difference they are never shown, and are tested on it. The reduced forms are the products of half the reactions in the chapter and never appear.

*Evidence.* assets[] contains mol-nad-plus and mol-fad only; no NADP+, NADPH, NADH or FADH2 asset.

*Recommended outcome.* A way for students to see where NADP+ differs from NAD+ and what the reduced flavin looks like, at the points where those differences carry the argument. (confidence 0.88)

##### `inst-021` · medium · assessment-readiness

*Location:* `glycolysis-mechanisms`, `ch29-retro-aldol-product` · anchor: "demo_eligible"

*Observation.* The bank contains 42 entries but only 21 distinct items. Not one has demo_eligible true, so nothing can be surfaced as a worked demonstration. The two mechanism-drawing types are thinly spread: both curved_arrow and both structure_scaffold items sit on glycolysis-mechanisms, so seven of ten concepts have no item in which a student draws or manipulates a structure.

*Learner impact.* An instructor gets one form and one reserve per idea, no demonstrable item, and no way to assess mechanism-drawing on the four pathways that occupy most of the chapter.

*Evidence.* 42 question_sets, 21 with variant_of; sum of demo_eligible true = 0.

*Recommended outcome.* At least one demonstrable item, and mechanism-drawing practice distributed across the pathway concepts rather than concentrated on glycolysis. (confidence 0.93)

##### `inst-022` · low · figure-accuracy

*Location:* `citric-acid-cycle-mechanisms`, `pdb-citrate-synthase` · anchor: "on binding oxaloacetate the small domain rotates against the large one, closing the cleft"

*Observation.* The figure uses PDB 1CTS, the unliganded OPEN form of citrate synthase, and the description explains the induced-fit domain CLOSURE without saying which conformation the image shows.

*Learner impact.* The figure's stated purpose is to answer why water does not hydrolyse the thioester, and the answer is that the site closes; a student shown the open form without that label may conclude the pictured cleft is the water-excluding state, which is the opposite of the argument.

*Evidence.* pdb_id '1CTS'; long_description describes the closure with no statement of the deposited conformational state.

*Recommended outcome.* The figure needs to say which conformational state is displayed. (confidence 0.75)

##### `inst-023` · low · figure-purpose

*Location:* `beta-oxidation-of-fatty-acids`, `rxn-glycerol-to-dhap` · anchor: "The other product of fat hydrolysis: glycerol joins glycolysis"

*Observation.* The asset is identified as rxn-glycerol-to-dhap and its learning_goal promises two steps, but the figure shows only the kinase; dihydroxyacetone phosphate never appears. The second step is asserted in the last sentence of the long_description rather than drawn. The chemistry drawn is correct - the product is (R) sn-glycerol 3-phosphate.

*Learner impact.* A student following the figure sees a one-step transformation under an id and caption that promise two, and the connection to glycolysis - the reason the figure exists - is the part left undrawn.

*Evidence.* SMILES products are glycerol 3-phosphate and ADP; long_description closes 'Oxidation of the remaining secondary alcohol then gives dihydroxyacetone phosphate'.

*Recommended outcome.* Either the oxidation to DHAP needs to be visible, or the title, id and learning_goal need to describe only the phosphorylation. (confidence 0.8)

**Open questions**

- The syn stereochemistry of acyl-CoA dehydrogenase and enoyl-CoA hydratase in inst-002 rests on recalled primary literature I could not consult in this environment. The second half of that finding - that facial relationship alone cannot determine E/Z or enantiomeric outcome in a freely rotating acyclic chain - stands independently.
- site-aspartate-aminotransferase cites PDB 1BKG; the residue numbering is right for E. coli and pig cytosolic AspAT, but I could not verify 1BKG is the intended wild-type entry rather than a mutant.
- I treated 1CTS as the open, unliganded citrate synthase form. If a closed-form entry was intended, the fix is a different PDB id rather than a caption change.
- Is rxn-thiamine-ylide-addition meant to read as an overall transformation or a mechanistic step? inst-011 assumes the latter.
- No new category ids were coined.

#### Struggling Student — 5.4/10

The authored package is genuinely good teaching: careful prose, the best-named misconceptions I have seen in this course, wrong-answer explanations that teach the discriminating criterion, and roadmaps that do real organising work. My problem is what actually reaches me in the reader. The compiled chapter is ten sections, each a single unbroken 300-450 word prose block with figures stacked after it and nothing else: no objectives, no trouble-spot warnings, no practice check, no question, no summary. All ten practice_check items exist in the package and none is compiled; all 42 questions sit at available:false. The hardest section gets three figures and none shows the decarboxylation; compounds I am quizzed on can be absent from the prose entirely; and the terse view of the citric acid cycle tells me both decarboxylations are beta-keto acid decarboxylations, which is exactly the misconception the pyruvate section spends a page destroying. The single_select bank is also solvable without chemistry: the answer is option a in 10 of 10 items and the longest option in 8 of 10.

**Publication blockers:** `stu-001`

**Strengths**

- The wrong-answer explanations name the discriminating criterion instead of restating the key - ch29-tca-co2-count explains why six and three are wrong, ch29-acyl-donor-ranking tells me my ordering principle was right and only the direction wrong.
- The generic_incorrect_explanation on every one of the 42 items is a genuine procedure I can run, not a consolation message.
- The roadmaps attach a reaction type to every arrow, which is exactly the transferable structure the chapter promises.
- The prose repeatedly answers the 'why does the cell bother' question - why aconitase relocates a hydroxyl, why the malonyl carboxyl is added and discarded, why GAPDH stops at an acyl phosphate.
- The authored trouble_spots are unusually precise and are the right misconceptions. My complaint is only that they never reach the reader.
- The three-level detail system is the right affordance for a struggling reader, and the standard variants are well judged as standalone summaries.

**Findings**

##### `stu-001` · blocker · misconception

*Location:* `nugget-citric-acid-cycle-mechanisms`, `citric-acid-cycle-mechanisms` · anchor: "releases two carbons as carbon dioxide by two decarboxylations of beta-keto acids"

*Observation.* The terse variant of the citric acid cycle section states that both carbon dioxides leave by beta-keto acid decarboxylation. Only the isocitrate dehydrogenase step is that. The alpha-ketoglutarate step is an alpha-keto acid oxidative decarboxylation requiring a thiamine ylide, which is what the standard and expanded variants of the same section say and what the preceding concept spends a full section establishing cannot happen by the beta route.

*Learner impact.* A student who has set the reader to terse to reduce load - precisely the student this variant exists for - reads the one sentence that contradicts the chapter's central discrimination. Having just been told an alpha-keto acid cannot decarboxylate the way a beta-keto acid does, I now read that the cycle does it twice by the beta route. I conclude I misunderstood the thiamine section and carry a wrong model into ch29-thiamine-role.

*Evidence.* nuggets[].text.terse for nugget-citric-acid-cycle-mechanisms, contradicted by the same nugget's text.standard and by the oxidative-decarboxylation trouble_spot.

*Recommended outcome.* The terse variant must not describe the alpha-ketoglutarate step as a beta-keto acid decarboxylation. Every detail level needs to preserve the alpha-versus-beta discrimination, because the shortest variant is the one a struggling reader is most likely to be looking at. (confidence 0.95)

##### `stu-002` · high · retrieval-practice

*Location:* `nugget-biochemical-energy-and-coupled-reactions` · anchor: "Coupling, and what an anhydride actually buys"

*Observation.* The compiled reader chapter contains no retrieval opportunity of any kind. Across all ten sections the block types are text, image, molecule, reaction, teaching_asset, video and links - no practice, question, self-check or summary block. All ten authored practice_check items, each with a worked answer, exist in the package and none is compiled. The 42-item bank is also unreachable: available:false, demo_eligible 0.

*Learner impact.* I read 92 minutes of the densest material in the course with no point at which I find out whether I understood any of it. With no checkpoint I cannot tell the difference between following it and recognising the words.

*Evidence.* Reader block_type counts contain no practice or question block; every nugget carries a practice_check in the package.

*Recommended outcome.* Every section needs a place where I stop and try something before moving on, and the worked answers that already exist need to be reachable from the section that taught the material. (confidence 0.94)

##### `stu-003` · high · conceptual-support

*Location:* `nugget-glycolysis-mechanisms` · anchor: "Ten steps, six reaction types"

*Observation.* The compiled reader section object has exactly three keys: id, title, blocks. Learning objectives, prerequisites, trouble_spots, difficulty and duration are all dropped at compile time. The package contains 34 learning objectives and 30 explicitly named misconceptions that never reach the student.

*Learner impact.* Nothing is marked as more important than anything else, so I try to memorise all of it and run out of capacity. And the named wrong moves - Markovnikov on the hydration step, biosynthesis as degradation reversed - are the exact traps I will fall into, and the chapter warns the authoring system about them but never warns me.

*Evidence.* sections[].keys == [blocks, id, title]; concepts[].trouble_spots (30) and nuggets[].learning_objectives (34) absent from compiled output.

*Recommended outcome.* I need to know, before or after each section, what I am supposed to be able to do and which specific wrong move to avoid. (confidence 0.93)

##### `stu-004` · high · worked-example-gap

*Location:* `nugget-oxidative-decarboxylation-of-pyruvate`, `rxn-thiamine-ylide-addition` · anchor: "oxidation and transfer to coenzyme A then complete the sequence"

*Observation.* This section's own prose calls it the point at which the chapter's chemistry becomes least obvious, and it carries the fewest supports of any section: five blocks, no active-site figure, a hidden video. The figures stop at the moment before the hard step - nothing shows carbon dioxide leaving, nothing shows the enamine, and the oxidation-and-transfer stage is one subordinate clause with no mechanism and no named third coenzyme.

*Learner impact.* The objective asks me to state what the ylide addition accomplishes for the decarboxylation that follows, and I am shown the setup but not the payoff. When ch29-thiamine-role's hint tells me three coenzymes act in this sequence, I am asked to reason about a third coenzyme the chapter never named. At that point I guess.

*Evidence.* Section blocks: text | reaction | molecule | reaction | external_link. 'lipoamide' appears zero times in the reader file.

*Recommended outcome.* The step the section exists to explain needs to be traceable step by step, and no question should depend on a coenzyme the chapter never introduces. (confidence 0.9)

##### `stu-005` · high · conceptual-support

*Location:* `nugget-citric-acid-cycle-mechanisms`, `ch29-reaction-family-inventory` · anchor: "Fumarase adds water to fumarate"

*Observation.* Several names that questions quiz me on never appear in the reader prose: gluconeogenesis 0 hits, fumarate 0, thiolase 0, ketoacyl 0, malate 0. Yet ch29-catabolic-anabolic asks me to categorise gluconeogenesis; ch29-reaction-family-inventory asks about thiolase, ketoacyl synthase and fumarase; and ch29-nad-balance, a core item, opens 'Malate dehydrogenase oxidises malate to oxaloacetate'. Some names exist only inside roadmap node labels and figure long_descriptions.

*Learner impact.* When a core-difficulty question names a compound I have never seen, my first conclusion is that I skipped a section, so I reread looking for it - and it is not there. On the second pass I start guessing from the name alone, which is the surface strategy the chapter is trying to train me out of.

*Evidence.* Prose-only extraction of the ten reader text blocks contains none of gluconeogenesis, fumarate, fumarase, thiolase, ketoacyl, malate.

*Recommended outcome.* Anything a question names has to be nameable from the prose a student actually reads, not only from a figure's node label. (confidence 0.92)

##### `stu-006` · high · conceptual-support

*Location:* `nugget-metabolic-step-to-mechanism-inventory` · anchor: "Every arrow drawn in it belongs to a family already covered"

*Observation.* The chapter's organising promise is that nothing here is new, and it repeats that promise without restating the prior mechanism or pointing to where it was taught. The only textbook back-link in the compiled chapter is a single mcmurry_link in section 1 pointing at the OpenStax chapter landing page; the per-section external links all go to Wikipedia, not to the chapter that taught aldol, Claisen, E1cb, imine formation or conjugate addition.

*Learner impact.* I am the student whose prerequisite knowledge is weak, and 'familiar from beta-keto acids' is not true of me. The sentence tells me I should already know this, and there is nowhere to click to check. So I keep reading a mechanism I cannot reconstruct, and the compounding starts.

*Evidence.* Four assertions of prior familiarity in the prose; exactly one mcmurry_link and ten Wikipedia external_links; no cross-reference to chapters 19-23 anywhere.

*Recommended outcome.* Every claim that a mechanism is already familiar needs either a one-line restatement of the arrow pattern in place, or a resolvable route back to where it was taught. (confidence 0.88)

##### `stu-007` · high · assessment-readiness

*Location:* `ch29-plp-electron-sink` · anchor: "It condenses with the amino group to give an imine"

*Observation.* The single_select items are answerable without chemistry. In all ten the correct option id is 'a'. In eight of ten the correct option is also the longest, and in three it is roughly twice the length of every distractor. ch29-thiamine-role, a multi_select, has its three correct statements as options a, b and c.

*Learner impact.* This actively harms me. I already default to test-wiseness under pressure, and this bank rewards it: pick the first option, or the longest one, and I score well on the hardest concepts without having understood them. I then walk into an exam believing I know this chapter. The good wrong-answer explanations never fire because I never select a wrong answer.

*Evidence.* All ten single_select items have correct_option_ids [redacted]; option word counts for ch29-plp-electron-sink are a:31, b:12, c:11, d:11.

*Recommended outcome.* Correct answers need distributing across positions and matching in length to their distractors, so a low-confidence student cannot pass by pattern-matching. (confidence 0.95)

##### `stu-008` · medium · missing-example

*Location:* `nugget-beta-oxidation-of-fatty-acids`, `rxn-thiolase-retro-claisen` · anchor: "Step four: retro-Claisen cleavage releases acetyl CoA"

*Observation.* The beta-oxidation section presents an explicitly numbered figure sequence - Step one, Step two, Step four - with no step three. The NAD+ oxidation of the beta-hydroxy thioester has no figure, even though it creates the substrate the fourth figure consumes.

*Learner impact.* Seeing one, two, four makes me think the page failed to load, so I scroll back and hunt. The missing figure is the one bridging the alcohol to the beta-keto thioester, which is precisely the link ch29-beta-oxidation-order tests.

*Evidence.* Package assets for the concept contain 'Step one', 'Step two', 'Step four' figures; no step-three asset exists.

*Recommended outcome.* A numbered sequence a student is asked to order must not skip a number. (confidence 0.9)

##### `stu-009` · medium · notation-consistency

*Location:* `nugget-glycolysis-mechanisms`, `site-aldolase` · anchor: "condensing an active-site lysine with the C2 ketone to give a protonated Schiff base"

*Observation.* One species gets three names and they are never reconciled. The glycolysis prose says 'protonated Schiff base'; the figure directly beneath says 'iminium'; the amino-acid section uses 'imine', 'internal aldimine' and 'external aldimine'. The word 'imine' never appears in the glycolysis section and 'Schiff base' is never equated to it anywhere in the prose.

*Learner impact.* Imine formation is a chapter-19 mechanism I half-remember under the name imine. Reading 'Schiff base' I do not recognise it as something I have already done, so I treat it as a new mechanism - the opposite of the transfer this chapter is built to produce.

*Evidence.* Reader prose: 'Schiff base' 2 occurrences, 'imine'/'aldimine' only in the transamination section, 'iminium' 0 in prose but present in the site-aldolase description.

*Recommended outcome.* The chapter needs to say once, at first use, that a Schiff base is the imine met earlier and that its protonated form is the iminium, then keep one name per species. (confidence 0.85)

##### `stu-010` · medium · cognitive-load

*Location:* `nugget-coenzymes-as-organic-reagents` · anchor: "A zinc ion binds the alcohol oxygen and lowers its pKa"

*Observation.* The third paragraph introduces five separate new ideas in five sentences: zinc as a Lewis acid, a serine-histidine proton relay, the isoalloxazine ring accepting single electrons, the two cases NAD+ cannot handle, and anti removal giving the E alkene. The zinc/serine/histidine relay is in none of this nugget's objectives, none of its trouble_spots, and none of the chapter's questions.

*Learner impact.* By sentence three I have lost the thread of the paragraph's actual point, which is the NAD+ versus FAD decision. I cannot tell that the zinc relay is optional colour, so I spend my effort on the metal-ion detail and arrive at ch29-coenzyme-choice unable to state the discriminating question.

*Evidence.* Reader text block paragraph 3; no question references zinc, serine or histidine in this context.

*Recommended outcome.* The load-bearing criterion needs separating from the enrichment detail so a struggling reader can tell which to spend effort on. (confidence 0.82)

##### `stu-011` · medium · conceptual-support

*Location:* `nugget-beta-oxidation-of-fatty-acids` · anchor: "which are equivalent in the free molecule but not to an enzyme"

*Observation.* The section opens on glycerol with a sentence that reads as self-contradictory and depends on an unstated prerequisite. Prochirality is the idea being used and it is never named, never explained, and never illustrated.

*Learner impact.* This is the first sentence of the section and I stall on it. 'Two equivalent hydroxyls which are equivalent but not equivalent' reads like a typo. Even after I accept it, I cannot see the mechanism, so I file it as 'enzymes are magic' - which seeds the misconception the final section tries to prevent.

*Evidence.* Reader text block paragraph 1; the word 'prochiral' appears nowhere in the chapter.

*Recommended outcome.* Either the prochirality idea needs to be followable at the point of use, or the glycerol aside should not carry a stereochemical claim a student cannot reconstruct. (confidence 0.84)

##### `stu-012` · medium · cognitive-load

*Location:* `nugget-glycolysis-mechanisms`, `roadmap-glycolysis` · anchor: "Ten intermediates with unfamiliar names make glycolysis look harder than it is."

*Observation.* Every section is compiled as one single text block containing the whole prose - no sub-headings, no chunk boundaries - with all figures after it. The glycolysis section is 451 words naming twelve enzymes and intermediates. The reader's default detail level is 'expanded', the longest variant. The roadmap that assigns a reaction type to each step sits after all five paragraphs of narrative.

*Learner impact.* I meet ten intermediate names inside continuous prose with no visual scaffold in view, which is what the section's own opening sentence says makes glycolysis look hard. By the time I scroll to the roadmap I have already spent my working memory holding names.

*Evidence.* Exactly one text block per section, always blocks[0]; useReaderPersonalization defaults detailLevel to 'expanded'.

*Recommended outcome.* The dense sections need internal chunking and the organising figure needs to be reachable before the narrative that depends on it. (confidence 0.86)

##### `stu-013` · medium · conceptual-support

*Location:* `nugget-glycolysis-mechanisms` · anchor: "so that the transfer potential is retained"

*Observation.* 'Transfer potential' is used twice as a load-bearing explanation and is never defined anywhere in the chapter. The section on ATP and coupling, where such a definition would belong, explains anhydride cleavage in terms of charge repulsion, resonance and solvation but never introduces the phrase.

*Learner impact.* Both times the phrase carries the whole explanation, so when I do not know what it means the sentence collapses into 'this works because of a thing that makes it work'. I do not look it up because it sounds like something I should already know.

*Evidence.* The phrase appears twice, both in nugget-glycolysis-mechanisms, and in no definition.

*Recommended outcome.* A term the explanation rests on needs defining at or before first use. (confidence 0.87)

##### `stu-014` · medium · retrieval-practice

*Location:* `ch29-schiff-base-arrow` · anchor: "The lysine must be in its neutral amine form to have a lone pair at all"

*Observation.* Hint ladders cap at two levels chapter-wide and are not always progressive. In ch29-schiff-base-arrow level 1 already states the polarisation of the carbonyl and level 2 changes subject to the lysine's protonation state, which does not move me closer to deciding where the arrow ends. Separately, ten of the twenty-one v2 variants carry only a single hint, so the retry item is less scaffolded than the item I already failed.

*Learner impact.* On the arrow question I open hint 2 expecting to be walked to the answer and get a sideways fact; at that point I draw at random. On a retry, support decreases exactly when my need for it has just been demonstrated.

*Evidence.* Max hints per question is 2 across all 42 items; hint counts of 1 on ten v2 variants.

*Recommended outcome.* Hints need to step toward the answer on the hardest mechanism items, and a retry variant should carry at least the scaffolding of the item it replaces. (confidence 0.83)

##### `stu-015` · medium · assessment-readiness

*Location:* `oxidative-decarboxylation-of-pyruvate`, `ch29-thiamine-role` · anchor: "Select every statement that correctly describes the role of thiamine diphosphate"

*Observation.* Practice is unevenly distributed against difficulty. Glycolysis gets four unique items, the citric acid cycle and beta-oxidation three each, but oxidative-decarboxylation-of-pyruvate gets exactly one - an advanced five-option multi_select - and transamination and the inventory get one each. There is no core-difficulty entry question for the thiamine concept.

*Learner impact.* On the hardest idea in the chapter my only chance to practise is an advanced multi-select where I must judge five statements at once. There is no easy question to confirm I have the basic shape before I am asked to evaluate five claims.

*Evidence.* Concept distribution of the 21 unique questions runs 4/3/3/2/2/2/2/1/1/1.

*Recommended outcome.* The hardest concept needs a low-stakes first question before the advanced one; practice depth should track concept difficulty rather than run inverse to it. (confidence 0.85)

##### `stu-016` · medium · cognitive-load

*Location:* `nugget-citric-acid-cycle-mechanisms` · anchor: "an anti dehydrogenation by FAD, a conjugate addition of water giving a single enantiomer, and an NAD⁺ oxidation"

*Observation.* Three distinct reactions of the cycle are compressed into a single sentence with no compound named on either side of any of them - succinate, fumarate and malate appear nowhere in the prose, only as roadmap node labels. The same section spends five sentences on three numbered active-site residues of citrate synthase.

*Learner impact.* The weighting is the opposite of what I need. I am asked to hold three residue numbers I will never be tested on, and given one clause for three reactions I am tested on. Since the compound names appear only inside a figure, I read the sentence, recognise none of the three transformations, and skip it.

*Evidence.* Prose-only search: malate 0 hits, fumar 0 hits; roadmap node labels include Succinate, Fumarate, L-Malate; ch29-nad-balance is a core question about malate.

*Recommended outcome.* The three closing steps need at least the same naming and visibility as the residue-level detail that precedes them, because those are the ones the assessment depends on. (confidence 0.86)

##### `stu-017` · low · notation-consistency

*Location:* `nugget-glycolysis-mechanisms`, `roadmap-glycolysis` · anchor: "Ten steps, six reaction types"

*Observation.* The section title and terse text promise six reaction types, and an objective asks me to assign each of ten steps to a type. The roadmap's long_description enumerates seven distinct labels unless the reader knows to merge 'phosphoryl transfer from ATP' and 'phosphate transfer to ADP' into one family.

*Learner impact.* I try to verify the promised count from the figure, get seven, and assume I have mis-assigned a step. A small thing, but at exactly the moment I was using the figure to build confidence, it tells me I am wrong when I am not.

*Evidence.* Nugget title 'Ten steps, six reaction types'; trouble_spot lists six; roadmap long_description enumerates seven.

*Recommended outcome.* The count promised in the title needs to be recoverable from the figure a student uses to check it. (confidence 0.78)

##### `stu-018` · low · conceptual-support

*Location:* `nugget-oxidative-decarboxylation-of-pyruvate` · anchor: "containing sulfur and a nitrogen that bears a positive charge and hence a methyl substituent"

*Observation.* The causal direction is stated backwards. The thiazolium nitrogen bears a positive charge because it is alkylated; the sentence says it bears a methyl substituent because it is positively charged.

*Learner impact.* I am already shaky on why ring nitrogens are sometimes charged, and this teaches me that a positive charge causes a substituent to appear. Two sections later I am asked why the pyridoxal ring nitrogen must be protonated, and I have a broken rule for reasoning about charged ring nitrogens.

*Evidence.* Reader text block, paragraph 3 of the section.

*Recommended outcome.* The charge on the thiazolium nitrogen needs presenting as a consequence of its bonding. (confidence 0.8)

##### `stu-019` · low · cognitive-load

*Location:* `nugget-beta-oxidation-of-fatty-acids`, `video-beta-oxidation-spiral` · anchor: "Four steps, then again"

*Observation.* All five video blocks carry an empty url and is_hidden true. The five briefs target precisely the moments a struggling reader most needs to see something move.

*Learner impact.* Nothing breaks, since the blocks are hidden, but the five hardest transitions are delivered as static prose plus static figures only. The repeating nature of the spiral and the carbon-provenance point are both intrinsically about change over iterations.

*Evidence.* Five video blocks with content.url == '' and is_hidden true.

*Recommended outcome.* The five moments the briefs identify need some form of step-through support beyond a single static frame. (confidence 0.75)

**Open questions**

- Is the omission of practice_check and question blocks from the compiled reader a compiler gap or an intentional split where questions are delivered through a separate LMS surface? If practice is delivered elsewhere, stu-002 and stu-015 drop in severity but the sequencing question remains.
- Are learning_objectives and trouble_spots intended to be surfaced by the reader UI from the package rather than the compiled chapter file?
- The reader default detail level is 'expanded'. Is that deliberate, or should a first-time reader land on 'standard'?
- Is this chapter expected to publish with video absent, or are the hidden blocks placeholders for a later pass?
- ch29-thiamine-role's level-1 hint refers to three coenzymes. Should the chapter name the third (lipoamide), or should the hint stay inside what the chapter teaches?

#### Accessibility Persona — 5.2/10

The authored accessibility content is unusually strong - every one of the 44 assets carries both an alt_text and a genuinely mechanism-level long_description, and the enzyme active-site descriptions are honest that residue positions are schematic. The failure is in delivery, not authorship. The compiled reader carries long_description on all 24 reaction blocks, all 8 molecule blocks and all 9 teaching-asset blocks, but the reader renderer surfaces only alt_text and silently discards the long description for every one of those 41 figures. Only the 3 image blocks get theirs shown. Roughly 14 of the 24 reaction alt_texts name reactants and products and stop there, so what a non-visual learner receives for most mechanism figures is a species list. The 5 roadmaps are worse: every node label, per-arrow enzyme and teaching note is baked as text inside a generated SVG served as an img. On the activity side curved_arrow and bond_change_ledger are genuinely well built, but structure_scaffold is declared keyboard_complete=False and delivered as a Ketcher iframe with no alternative, and the hotspot items ship no named region list.

**Publication blockers:** `access-001`, `access-002`, `access-003`, `access-005`

**Strengths**

- The authored long_description for the reaction figures is genuinely mechanism-level - rxn-thiolase-retro-claisen names the exact bond broken and then explains why the enolate is a tolerable leaving group. The problem is delivery, not authorship.
- The four enzyme_active_site long descriptions explicitly state that residue positions are illustrative and that no distance or angle appears, preventing a non-visual learner from over-reading a schematic as a structural model.
- The two protein_structure descriptions say plainly what the static render does not show, so the learner knows the boundary of the evidence.
- bond_change_ledger is fully non-visual: a table with scoped headers, per-row labelled selects, and a visible atom-numbering list naming each labelled atom.
- curved_arrow items supply chemically meaningful site labels and the renderer exposes them as labelled source/target/kind pickers - an arrow-drawing task fully completable without a pointer.
- The chapter's chemistry is carried in prose, not only in figures: every nugget ships three text tiers and a practice_check whose model answer is a complete prose argument.
- No auto-playing motion ships in version 1, so there is no unstoppable animation or motion-only carrier in the reader as delivered.
- Across all 42 questions the accessible_description states the task rather than the solution, including for the types where leaking would be easiest.
- The three image blocks do render their long description, which demonstrates the delivery pattern the other 41 figures need.

**Findings**

##### `access-001` · blocker · media-equivalence

*Location:* `nugget-biochemical-energy-and-coupled-reactions`, `rxn-atp-phosphoryl-transfer` · anchor: "Described as:"

*Observation.* Every reaction (24) and molecule (8) block in the compiled reader carries a full content.long_description, but the reader never renders it. ReaderBlockRenderer routes both types to StructureCard passing only altText; StructureCard renders one visible line, 'Described as: {altText}'. long_description is read nowhere in that component, and no disclosure control exposes it. The same is true for the 9 teaching_asset blocks. Only the 3 image blocks escape, because ReaderProviderImage is the single component that renders content.long_description.

*Learner impact.* A learner using a screen reader, a text-only or Braille rendering, or reading with images disabled receives, for 41 of the chapter's 44 figures, only the one-sentence alt text. The entire bond-level, electron-flow and why-this-happens layer that the authors wrote - the actual chemistry of this chapter - is present in the data and unreachable in the product.

*Evidence.* [internal source reference — not in this repo] molecule and reaction cases pass only altText; StructureCard renders 'Described as: {altText}' with no long_description reference; TeachingAssetLiveRenderer the same. 24/24 reaction and 8/8 molecule blocks carry a non-empty content.long_description.

*Recommended outcome.* The bond-level description that already exists for every figure must reach the learner in the reader, not only live in the package - the same access the image blocks already have. (confidence 0.96)

##### `access-002` · blocker · alt-text-quality

*Location:* `nugget-beta-oxidation-of-fatty-acids`, `rxn-thiolase-retro-claisen` · anchor: "A beta-keto thioester reacting with a thiol to give two molecules of acetyl thioester."

*Observation.* Because alt_text is the only description the reader surfaces, it has to carry the chemistry alone - and for roughly 14 of the 24 reaction figures it names only the species on each side of the arrow and never states which bond forms or breaks. A minority (rxn-fad-dehydrogenation, rxn-thioester-enol, rxn-acyl-coa-dehydrogenase, rxn-thiamine-ylide-addition) do state the bond change and show what the standard should be.

*Learner impact.* For the figures that carry the chapter's central mechanistic claims - that the C2-C3 bond is the one thiolase cleaves, that the new C-C bond in citrate forms between the acetyl methyl carbon and the oxaloacetate ketone carbon - a non-visual learner is told only which molecules go in and come out. That is what the surrounding prose already gives, so the figure adds nothing.

*Evidence.* assets[].accessibility.alt_text for the 14 assets listed, contrasted with rxn-acyl-coa-dehydrogenase, whose alt text does the job.

*Recommended outcome.* Whatever single description the reader surfaces must state which bond forms and which breaks for every reaction figure. Naming reactants and products is not an equivalent for a reaction scheme. (confidence 0.93)

##### `access-003` · blocker · media-equivalence

*Location:* `nugget-glycolysis-mechanisms`, `roadmap-glycolysis` · anchor: "Glycolysis: ten steps from one hexose to two pyruvates"

*Observation.* The 5 synthesis_roadmap figures render as a single generated SVG in which every node label, per-arrow reagent, per-arrow teaching note and the caveat footer are SVG text elements baked into an image. None is exposed to assistive technology. The long_description - not rendered at all - aggregates rather than enumerates, listing the reaction types by count without saying which arrow is which. The spec's per-step notes carry real teaching content that appears nowhere in either description: 'The committed step of the pathway', 'the charged product cannot leave the cell', 'The tautomerisation, not the phosphate transfer, is what makes the step irreversible'.

*Learner impact.* A learner who cannot see the chain cannot reconstruct the sequence, cannot pair an enzyme with the transformation it catalyses, and never receives the per-arrow notes carrying the chapter's distinguishing claims. These roadmaps are the organising spine for four of the ten concepts.

*Evidence.* [internal source reference — not in this repo] emits node labels, step.reagents, step.note and the caveats as SVG text; AssetPreview renders an Image with alt only.

*Recommended outcome.* A learner who cannot see the roadmap needs the ordered sequence with each arrow's enzyme, cofactor and note attached to the step it belongs to, plus the caveats, as structured navigable text rather than an aggregate summary or an image of text. (confidence 0.94)

##### `access-004` · high · media-equivalence

*Location:* `nugget-glycolysis-mechanisms`, `roadmap-glycolysis` · anchor: "Glycolysis, step by step"

*Observation.* The roadmap SVG is sized from its node count: roadmap-glycolysis has 11 nodes giving an intrinsic width of about 3382 px against a reader column capped at 860 px, and it is rendered with maxH but no maxW. Within the image, per-arrow reagents are 11.5 px and notes 10 px, so any scaling that fits the column reduces the teaching annotations to roughly 2-3 px. There is no zoom, pan, or open-full-size affordance.

*Learner impact.* Learners using screen magnification, a small viewport, or default browser zoom face either two-dimensional scrolling to read one figure or annotation text too small to resolve. This is independent of the screen-reader gap - sighted learners lose the arrow notes too.

*Evidence.* [internal source reference — not in this repo] width formula and font sizes; AssetPreview Image has maxH but no maxW; TopicPackageChapterRenderer column maxW 860px.

*Recommended outcome.* The roadmap's annotation text needs to remain legible at the reader's actual column width and under magnification, and the figure must not force horizontal scrolling. (confidence 0.78)

##### `access-005` · blocker · interactive-fallback

*Location:* `glycolysis-mechanisms`, `ch29-retro-aldol-product` · anchor: "Draw the three-carbon product that contains carbons 1, 2 and 3"

*Observation.* Both structure_scaffold questions use scaffold 'blank_canvas' and are delivered through the ketcher workspace. The platform's own type manifest records AccessibilityBlock(keyboard_complete=False) with the comment that the Ketcher canvas is not yet keyboard-complete. The renderer embeds a same-origin iframe and offers a single alternative - opening the same iframe larger. There is no SMILES entry field and no structured molecule-entry path, although the manifest names structured_molecule_entry as the intended mode.

*Learner impact.* A learner who cannot use a pointer, or who uses a screen reader, cannot answer these two items at all. Structure drawing is the only place in this 42-question set where the learner must construct a structure rather than recognise one, so the affected learner loses the construct entirely.

*Evidence.* [internal source reference — not in this repo] AccessibilityBlock keyboard_complete=False; StructureWorkspaceRenderer offers only the iframe; both slugs carry scaffold blank_canvas with no alternate response mode.

*Recommended outcome.* A required construct-a-structure activity needs a non-pointer, non-visual path to submitting the same answer - the grader already accepts a chemical graph, so the need is an equivalent input route. Until one exists, these items need an alternate activity assessing the same construct. (confidence 0.95)

##### `access-006` · high · interactive-fallback

*Location:* `ch29-conjugate-addition-site` · anchor: "Click the carbon that ends up carrying the new hydroxyl group."

*Observation.* Both hotspot questions ship student_config containing only molecule_smiles and select_count; there is no regions array and no atom_labels. At serve time the renderer takes its atom-button branch: each atom is a real button, so it is keyboard-reachable, but its only accessible name is e.g. 'C atom 2', and the structure image alt is the generic 'Structure for this question'. Nothing states which atom is alpha or beta. The hotspot type manifest declares nonvisual_response_mode 'named_region_list'; this chapter supplies none. The chapter's own curved_arrow items supply labelled sites and its ledger items supply an atom-numbering list.

*Learner impact.* The activity is technically operable by keyboard but not answerable without vision: a learner tabs through a dozen buttons announced only as 'C atom 1 ... C atom 12' with no chemical identity. The on-screen numbering is also offset by one from the internal region ids, so even a learner who inferred SMILES ordering could not verify the mapping.

*Evidence.* Both hotspot slugs' student_config keys are molecule_smiles and select_count only; HotspotActivityRenderer aria-label is `${atom.symbol} atom ${atom.index + 1}`.

*Recommended outcome.* A learner selecting an atom without seeing the structure needs each target identifiable by chemical role, not element symbol and an arbitrary index - the same identification the curved-arrow and ledger items already provide. (confidence 0.9)

##### `access-007` · medium · alt-text-quality

*Location:* `nugget-citric-acid-cycle-mechanisms`, `site-citrate-synthase` · anchor: "both are drawn as neutral imidazoles and labelled general acids"

*Observation.* The long_description for site-citrate-synthase reports that His274 and His320 share one note about being neutral rather than protonated. The spec gives them different notes: His274 donates its N-H proton to the enol oxygen, while His320 polarises the oxaloacetate carbonyl. The description collapses His320's note into His274's, so the reason the oxaloacetate carbonyl becomes electrophilic is absent from the non-visual account.

*Learner impact.* A non-visual learner gets a different figure from the one a sighted learner sees, and specifically loses the carbonyl-polarisation half of the catalytic story for the chapter's flagship aldol addition. It also erodes trust: a description that misreports one on-figure label cannot be relied on for the others.

*Evidence.* site-citrate-synthase spec.residues notes for his274 and his320 versus accessibility.long_description.

*Recommended outcome.* Each residue's on-figure note needs to reach the non-visual learner as the figure actually states it, not merged with a neighbour's. (confidence 0.88)

##### `access-008` · high · media-equivalence

*Location:* `nugget-amino-acid-catabolism-and-transamination`, `site-aspartate-aminotransferase` · anchor: "Schematic active site of aspartate aminotransferase"

*Observation.* The 4 enzyme_active_site figures have long descriptions that do the spatial and mechanistic work well - naming each residue box, which substrate atom it contacts, and explicitly saying positions are illustrative. None reaches the reader: only alt_text is shown, and the alt texts list the residues but not the contacts, the residue notes, or the schematic-not-structural caveat. For site-aspartate-aminotransferase the spec has arrows: [], so no electron flow is drawn at all, and neither description states the flow the learning goal is about.

*Learner impact.* A non-visual learner is told which residues surround the substrate but not what each does, not that the layout is illustrative, and not where the electrons go. For the aminotransferase figure the single idea the figure exists to teach is not available in any surfaced text.

*Evidence.* TeachingAssetLiveRenderer shows only alt_text; site-aspartate-aminotransferase spec.arrows is []; asp222's note appears in long_description but not alt_text.

*Recommended outcome.* The residue roles, contacts, electron flow and the schematic caveat must be part of what a non-visual learner receives - the text already exists and needs a delivery path. (confidence 0.91)

##### `access-009` · medium · color-motion-only

*Location:* `nugget-citric-acid-cycle-mechanisms`, `video-citric-acid-cycle-carbons` · anchor: "with the two acetyl carbons marked in a distinct colour that persists for the whole sequence"

*Observation.* All 5 video briefs are deferred and all 5 compiled blocks are hidden with empty URLs, so no motion content ships - that part is fine. But the briefs are the handoff for later production, and two specify colour as the sole carrier of a distinction. The briefs also carry a narration_outline but no caption, transcript or audio-description deliverable, and no pause/step requirement.

*Learner impact.* As specified, a colour-blind or non-visual learner could not follow the carbon-tracking video - which exists specifically to correct a misconception - and a deaf or hard-of-hearing learner has no stated caption path. Because these are handoff artefacts, the barrier would be built in at production time unless the brief changes first.

*Evidence.* video-citric-acid-cycle-carbons storyboard and production_note; video-thioester-two-properties storyboard; all five briefs lack a transcript/caption field.

*Recommended outcome.* Before production, the distinctions these briefs rely on must not be carried by colour alone, and each needs a stated caption/transcript deliverable and a pause-or-step requirement. (confidence 0.85)

##### `access-010` · low · keyboard-operability

*Location:* `nugget-thioester-activation` · anchor: "Described as:"

*Observation.* Heading levels skip: the chapter title is h1 and section titles are h2, but every block-level heading inside a section is h4. No h3 is produced anywhere, so a screen-reader user navigating by heading jumps h1 to h2 to h4. Separately the one surfaced figure description is rendered at fontSize xs in a muted colour, the smallest and lowest-contrast text on the page.

*Learner impact.* Heading-level navigation is a primary way screen-reader users skim a long chapter; a consistent skipped level makes the outline read as if a level of structure is missing. The xs muted description is the least legible text for the learners most likely to depend on it.

*Evidence.* TopicPackageChapterRenderer h1/h2; ReaderBlockRenderer, StructureCard and TeachingAssetLiveRenderer all h4; StructureCard description fontSize xs muted.

*Recommended outcome.* The heading outline should be continuous, and the figure description a learner is meant to rely on should not be the smallest, lowest-contrast text on the page. (confidence 0.82)

##### `access-011` · low · alt-text-quality

*Location:* `ch29-citrate-alcohol-class-v2` · anchor: "A short answer naming the reaction type in which an enol attacks a ketone carbon"

*Observation.* The accessible_description characterises the reaction as 'an enol attacks a ketone carbon', whereas the prompt says 'forms a new carbon-carbon bond between the methyl carbon of an acetyl thioester and the ketone carbon of oxaloacetate'. Naming the nucleophile as an enol is a step closer to the answer than the prompt provides. It is not a mechanical leak and the deterministic guard would not flag it. The other 41 descriptions are clean on this dimension.

*Learner impact.* Minor and in the learner's favour, but it means the two learners are not answering the same item, which weakens it as a measure and sets a precedent for descriptions that reason ahead of the prompt.

*Evidence.* ch29-citrate-alcohol-class-v2 prompt_text versus accessibility_bundle.accessible_description.

*Recommended outcome.* The non-visual description should convey the same task at the same level of framing as the prompt, without supplying mechanistic characterisation the prompt withholds. (confidence 0.7)

**Open questions**

- Does any other delivery surface - LMS export, PDF/print, Deck Creator, or an accessibility view - render long_description for reaction/molecule/teaching_asset blocks? access-001 is scoped to the /reader topic-chapter path.
- Is there a reader preference or study-tools control that reveals long descriptions on demand?
- The horizontal-overflow behaviour in access-004 is inferred from the SVG intrinsic width and the absence of maxW; I could not run the reader to observe actual reflow. A global img max-width reset would resolve the overflow half but not the illegible-annotation half.
- Both structure_scaffold and one hotspot item are surfaced; their v2 twins are staged. If staged variants are never shown, the blast radius of access-005 and access-006 is one item each, but the construct-level loss is unchanged.
- [internal source reference — not in this repo] names structured_molecule_entry as the intended path and cites [internal PRD reference — not in this repo]. Is that scheduled, and is there an instructor-facing alternate-assessment convention meanwhile?
- I used media-equivalence for access-004, which is really a low-vision perceivability/reflow barrier. A visual-legibility or reflow-oriented category would classify it better if this pattern recurs.

#### Learner with Visual Preference — 6.3/10

This chapter is visually busy but visually quiet: 44 figures across 10 sections, and the figure captions are unusually good at telling the reader what to look at, but in most cases the picture cannot deliver what the caption promises. The 24 reaction figures are unhighlighted reactant-arrow-product renders with no per-atom colour, no marked bond change and an empty arrow. The 5 roadmaps degrade to name-only boxes even though the renderer supports a per-node smiles, and two of them carry learning goals that explicitly ask the reader to follow structural change. The 4 enzyme active-site diagrams are the chapter's strongest visual work; the 2 static PDB renders do not fully earn theirs, because each one's stated goal is a motion a single static state cannot show. The largest gaps are comparative: the chapter repeatedly asks the reader to set two things side by side and never puts them side by side in a figure, while the question bank assesses exactly those comparisons.

**Strengths**

- Figure captions do real instructional work: every asset's learning_goal is an imperative telling the reader precisely what to look for, surfaced in the reader as the block description directly under the render.
- Model compounds are used deliberately to cut clutter - coenzyme A as N-acetylcysteamine, nicotinamide as its 1-methyl model, thiamine as the bare thiazolium ring - and every simplification is disclosed in the figure title.
- The 4 enzyme_active_site diagrams clearly earn their place: the prose names specific catalytic residues and the diagram is the only thing that shows their arrangement relative to the substrate.
- The mitochondrion clipart is used for orientation rather than decoration, establishing cytosol versus matrix before any mechanism is traced.
- Long descriptions are unusually honest about what each figure does not show, so even where a figure underperforms the reader is not misinformed.
- The hotspot, curved-arrow and bond-change-ledger questions carry their own structures, so the visually-dependent question types do not ask students to reason about a molecule they cannot see.

**Findings**

##### `visual-001` · high · visual-opportunity

*Location:* `nugget-biochemical-energy-and-coupled-reactions`, `rxn-atp-phosphoryl-transfer` · anchor: "See what coupling actually means at the level of bonds"

*Observation.* All 24 reaction assets are plain reactant + arrow + product renders. The payload carries only a reaction SMILES plus title/learning_goal/accessibility - there is no atom-map, highlight or per-atom colour field anywhere in the 24 reaction assets, so nothing distinguishes the bond that changed from the dozens that did not. The worst case is rxn-atp-phosphoryl-transfer, where glucose plus full ATP becomes glucose 6-phosphate plus ADP and the single change is at one phosphorus.

*Learner impact.* A reader who navigates by figure has to do the diff by eye across two large structures before any chemistry starts. That inverts the intended work: the figure should carry the localisation so the prose can carry the reasoning, but here the prose has to carry both.

*Evidence.* rxn-atp-phosphoryl-transfer learning_goal promises bond-level insight; the long_description does the localising work in words that the image does not do visually. Same pattern in rxn-transamination, rxn-glutamate-oxidative-deamination, rxn-phosphoglucose-isomerase, rxn-aldolase-retro-aldol.

*Recommended outcome.* The reader needs the changed bonds/atoms to be visually locatable in the reaction figures without first reading the caption, at minimum for the figures where the unchanged remainder is large. (confidence 0.9)

##### `visual-002` · medium · figure-purpose

*Location:* `nugget-beta-oxidation-of-fatty-acids`, `rxn-acyl-coa-dehydrogenase` · anchor: "Step one: making the alkene (FAD named, not drawn)"

*Observation.* Reaction arrows carry no text. Reagents, coenzymes and enzymes appear only in the figure title and the surrounding prose, so the transformation and the agent that performs it are on separate visual layers. Four titles openly disclose the omission.

*Learner impact.* In a chapter whose central question is repeatedly which coenzyme and why, the picture of the transformation never shows the coenzyme choice. It also weakens the figures as revision objects: an arrow with nothing over it cannot be self-quizzed.

*Evidence.* Four asset titles announce the missing reagent. By contrast the roadmap steps[].reagents field does carry enzyme and cofactor onto the arrow, showing the platform already treats arrow annotation as a supported channel.

*Recommended outcome.* The reader needs the reagent that effects each transformation visible in the same glance as the transformation itself, at least where the coenzyme choice is the teaching point. (confidence 0.82)

##### `visual-003` · high · figure-purpose

*Location:* `nugget-beta-oxidation-of-fatty-acids`, `roadmap-beta-oxidation` · anchor: "oxidise, hydrate, oxidise, cleave"

*Observation.* All 5 synthesis_roadmap assets have zero nodes carrying a smiles, verified across all 36 nodes, so every node renders as a name in a box. The renderer supports structures per node and falls back to a text-only node only when no SMILES is given. Two roadmaps then set structural learning goals the name-only render cannot serve.

*Learner impact.* A chain of chemical names is exactly the representation students already find opaque; the roadmap reproduces the memorisation problem the section says it is solving. A reader cannot see the alternating oxidation/hydration pattern, cannot see the beta-keto group that makes the fourth step possible, and cannot see that oxaloacetate returns identical to how it started.

*Evidence.* roadmap-beta-oxidation's five nodes are small, easily drawn structures, none with SMILES; roadmap-citric-acid-cycle, 10 nodes, same. roadmap-glucose-to-carbon-dioxide is a stage map and is defensible as text.

*Recommended outcome.* Where a roadmap's stated goal is to make a structural or oxidation-level pattern visible, the nodes need to carry that structure; where the roadmap is a locator map over many steps, names are the right call. The decision should be per-roadmap. (confidence 0.88)

##### `visual-004` · medium · visual-opportunity

*Location:* `nugget-beta-oxidation-of-fatty-acids`, `beta-oxidation-of-fatty-acids` · anchor: "The third step oxidises that secondary alcohol to a ketone with NAD⁺"

*Observation.* The section presents a four-step cycle and draws steps one, two and four. Step three, the NAD+ oxidation of the 3-hydroxyacyl thioester, has no figure - it exists only as a name-only roadmap node and one prose sentence.

*Learner impact.* The visual sequence has a hole exactly where the pattern is supposed to become memorable, and the missing step creates the beta-keto thioester the fourth figure depends on, so the retro-Claisen figure appears to act on a substrate the reader never saw formed.

*Evidence.* Reader section shows figures titled Step one, Step two, Step four with no Step three. The numbering itself advertises the gap.

*Recommended outcome.* The four-step cycle needs to be completable from the figures alone. (confidence 0.85)

##### `visual-005` · high · visual-opportunity

*Location:* `nugget-fatty-acid-biosynthesis`, `roadmap-fatty-acid-elongation`, `ch29-synthesis-vs-degradation`

*Observation.* The section is built entirely as a comparison and its roadmap goal says explicitly 'Set the two pathways side by side'. Nothing in the chapter sets them side by side. The two roadmaps sit two sections apart, both name-only, and the three differences the reader must extract are never co-visible.

*Learner impact.* The reader must hold a five-node pathway from section 7 in memory while reading a five-node pathway in section 8, then diff them on three attributes - a working-memory task a single comparison view would eliminate. The bank then assesses exactly that diff.

*Evidence.* roadmap-fatty-acid-elongation learning_goal instructs the comparison; ch29-synthesis-vs-degradation is a comparison_matrix over three feature rows with representation_tags ['text'].

*Recommended outcome.* The two pathways and their three differences need to be visible in one view at the point of comparison; a caption instructing the reader to compare is not a substitute for co-visibility. (confidence 0.88)

##### `visual-006` · high · visual-opportunity

*Location:* `nugget-citric-acid-cycle-mechanisms` · anchor: "isotopic labelling shows that the two carbons released in any given turn come from the oxaloacetate"

*Observation.* The chapter's most counterintuitive claim is asserted in prose and appears in no figure. The roadmap nodes are names so carbons cannot be tracked through them; the reaction figures are individual steps with no carbon labelling; the only planned vehicle was the deferred video brief.

*Learner impact.* This is a claim about identity across eight transformations. Prose can state it but cannot let the reader verify it, and the standard misconception is precisely the one a reader will retain if nothing shows otherwise. ch29-tca-co2-count only asks for a count, so nothing in the assessment surfaces the misconception either.

*Evidence.* Section prose; video-citric-acid-cycle-carbons is deferred; roadmap nodes carry no carbon provenance.

*Recommended outcome.* The reader needs to trace which carbons leave a turn rather than being told; this does not require motion but does require a representation in which individual carbons are distinguishable. (confidence 0.87)

##### `visual-007` · medium · visual-opportunity

*Location:* `nugget-metabolic-step-to-mechanism-inventory`, `ch29-reaction-family-inventory` · anchor: "An inventory of the chapter, by reaction type"

*Observation.* The payoff section promises an inventory by reaction type and delivers four prose paragraphs plus three figures, none of which is the inventory. The mapping the section is named for exists only as running text spread over ten sections.

*Learner impact.* The organising claim of the chapter is the thing a reader most needs to see as a structure, because its value is the mapping. Seen as a mapping it becomes the revision object for the whole chapter. The bank assesses it as a sorting task, which is inherently spatial.

*Evidence.* Section figures are a text-only stage roadmap and two individual reactions; ch29-reaction-family-inventory sorts six steps into three families with no figure.

*Recommended outcome.* The step-to-mechanism mapping needs a form the reader can see at once and revise from. (confidence 0.83)

##### `visual-008` · medium · visual-opportunity

*Location:* `nugget-metabolic-step-to-mechanism-inventory` · anchor: "A protonated Schiff base replaces a ketone in class I aldolase"

*Observation.* Four different electron sinks are introduced across four sections and the closing section states they are all the same device. They are never shown together; each appears only inside a separate figure about a separate enzyme.

*Learner impact.* The unifying idea is stated four times in prose and shown zero times as a comparison, so the reader most likely to benefit has nothing to confirm the pattern against. Each sink is likely to be memorised as a separate enzyme fact.

*Evidence.* site-aldolase, rxn-thiamine-ylide-addition, site-aspartate-aminotransferase and rxn-thioester-enol each show one, in different sections.

*Recommended outcome.* The recurring electron-sink pattern needs to be visible as one comparison rather than reconstructed from four separated figures. (confidence 0.8)

##### `visual-009` · medium · visual-opportunity

*Location:* `nugget-thioester-activation` · anchor: "the order runs acyl phosphate, then thioester, then ester, then amide"

*Observation.* This section carries two dense structural arguments in prose alone - the 3p/2p orbital-overlap reason sulfur donates poorly, and a four-member ranking of acyl transfer potential - supported by three figures, none of which shows either.

*Learner impact.* The orbital argument is inherently spatial and is delivered entirely verbally. The ranking is an ordered comparison of four groups the reader must build from a single sentence, then apply for the rest of the chapter; the bank tests it directly.

*Evidence.* Assets are mol-acetyl-coa, rxn-thioester-hydrolysis, rxn-thioester-enol; ch29-acyl-donor-ranking is a rank_order item with representation_tags ['text'].

*Recommended outcome.* The transfer-potential ordering and the structural reason behind it need a representation the reader can see and re-check. (confidence 0.8)

##### `visual-010` · medium · visual-opportunity

*Location:* `nugget-oxidative-decarboxylation-of-pyruvate` · anchor: "The requirement is geometric: the carboxyl group and a carbonyl three atoms away can form a six-membered ring"

*Observation.* The section's core argument is explicitly geometric and is made entirely in words. Its two figures show the overall transformation and the ylide addition, neither of which depicts the transition state or the failed geometry it contrasts with.

*Learner impact.* 'One carbon too close' is a claim about a ring that either closes or does not; a reader who cannot picture the two candidate rings has to accept it. This is the section the chapter itself flags as its least obvious.

*Evidence.* Section assets are rxn-pyruvate-to-acetyl-coa and rxn-thiamine-ylide-addition; the same transition state is invoked again in the citric acid section with no figure there either.

*Recommended outcome.* The contrast between a decarboxylation geometry that works and one that does not needs to be visible, since the rationale for thiamine rests on it. (confidence 0.79)

##### `visual-011` · medium · figure-purpose

*Location:* `nugget-fatty-acid-biosynthesis`, `pdb-fatty-acid-synthase` · anchor: "a flexible carrier arm swings the substrate from one to the next"

*Observation.* Both protein_structure figures set learning goals the static render cannot meet, and both long descriptions say so - the ACP and thioesterase domains are disordered and not visible in 2VZ8, and 1CTS shows neither the bound substrates nor the motion itself.

*Learner impact.* A reader who goes to these figures for the stated point finds a cartoon ribbon they cannot read the claim off, and the caveat arrives only in the long description. The residual information is already fully stated in the prose, so the figures function closer to atmosphere than instruction.

*Evidence.* Both assets' learning_goal and long_description; the citric acid section carries three figures about the same enzyme.

*Recommended outcome.* Either the architectural claims need carrying by something that can show them, or the captions need scaling down to what a single static state conveys. (confidence 0.81)

##### `visual-012` · medium · figure-purpose

*Location:* `nugget-coenzymes-as-organic-reagents`, `rxn-fad-dehydrogenation` · anchor: "Note both facts the drawing carries at once"

*Observation.* The caption asserts that the drawing carries the anti relationship of the two departing hydrogens. The asset is a flat succinate to flat fumarate reaction SMILES; the E geometry is consistent with anti removal but does not depict it, and nothing in the render shows faces.

*Learner impact.* A reader who trusts the caption and looks for the stereochemical course will either invent it or conclude they have missed something. It also quietly teaches that product geometry alone establishes a stereochemical course.

*Evidence.* rxn-fad-dehydrogenation smiles and learning_goal; the identical claim recurs for rxn-acyl-coa-dehydrogenase.

*Recommended outcome.* Where a caption claims a stereochemical course, the figure needs to carry it or the caption needs to stop attributing it to the drawing. (confidence 0.83)

##### `visual-013` · medium · figure-purpose

*Location:* `nugget-metabolic-step-to-mechanism-inventory`, `rxn-triose-phosphate-oxidation` · anchor: "Glyceraldehyde 3-phosphate dehydrogenase oxidises an aldehyde but stops at a mixed anhydride"

*Observation.* Three figures sit in a different section from the prose they support: the GAPDH step and the flask Claisen are both in section 10, and the succinate-to-fumarate figure is in section 2 while that cycle step belongs to section 6.

*Learner impact.* A reader who reads a paragraph and looks down for the matching picture does not find one, and later meets the picture with the explanation gone. It also makes the glycolysis section look better illustrated than it is.

*Evidence.* Reader block order for the glycolysis section contains no GAPDH figure; the inventory section carries rxn-triose-phosphate-oxidation and rxn-claisen-in-the-flask.

*Recommended outcome.* Figures whose explanation lives in another section need to be reachable from that explanation. (confidence 0.78)

##### `visual-014` · medium · visual-opportunity

*Location:* `nugget-biochemical-energy-and-coupled-reactions` · anchor: "The two must share an intermediate"

*Observation.* The chapter's opening concept is energetic coupling and the chapter contains no energy representation of any kind - no free-energy comparison, no reaction-coordinate figure, nothing quantitative or even ordinal. The same idea returns in the closing section again with no visual.

*Learner impact.* Coupling is a claim about the relative sizes of two quantities and their sum, the archetypal case where a picture removes explanation burden. The misconception being corrected - energy stored in a bond - is itself pictorial and is being fought with words only.

*Evidence.* The deferred video brief video-atp-coupling planned exactly this in its final storyboard beat.

*Recommended outcome.* The sum of an uphill and a downhill step needs to be visible as a comparison of magnitudes where coupling is introduced. (confidence 0.8)

##### `visual-015` · low · visual-redundancy

*Location:* `nugget-glycolysis-mechanisms`, `video-aldolase-cleavage` · anchor: "Cutting a hexose in half"

*Observation.* All 5 video briefs are deferred and their reader blocks are hidden with an empty url, so the reader sees no video, no placeholder and no note. Judged on content, four of the five describe discrete bond-level steps a well-designed static series would carry as fully as motion; only the carbon-tracking brief depends on continuity of identity across many steps.

*Learner impact.* The absence is low-impact and silent hiding is right. The risk is the opposite: treating these as pending video keeps four real explanation gaps parked behind a heavyweight intervention the chemistry does not require.

*Evidence.* All five briefs are production_status deferred; the production notes state the chalk pipeline cannot express them.

*Recommended outcome.* The needs these briefs encode should be re-judged on their own terms rather than held for animation. (confidence 0.78)

##### `visual-016` · low · figure-purpose

*Location:* `nugget-glycolysis-mechanisms` · anchor: "Ten steps, six reaction types"

*Observation.* Figure density is uneven relative to conceptual load rather than word count. Sections 4 and 6 carry 7 figures each in about 450 words, presented as a flat sequence with no grouping, while sections 3, 5, 8 and 10 carry 3 each over comparably dense prose.

*Learner impact.* In the dense sections figures compete: a reader meets seven roughly equal-weight cards with nothing marking the roadmap as the frame and the rest as steps within it. In the thin sections the reader runs out of anchors mid-argument.

*Evidence.* Per-section figure counts 3, 5, 3, 7, 3, 7, 6, 3, 4, 3 against word counts 328-454.

*Recommended outcome.* The dense pathway sections need to signal which figure frames the others, and the argument-heavy thin sections need visual support closer to their conceptual load. (confidence 0.7)

**Open questions**

- Does the reader's roadmap render path support per-node structures the same way the deck-side builder does? visual-003 assumes parity; if the reader renderer is text-only the finding stands but the intervention differs.
- Is the roadmap's stepwise-reveal capability available in the reader, or only in deck export?
- Is an 11-node roadmap with a rendered structure per node legible at reader width, or would structure nodes force a wrap that costs more than the names do? This is why visual-003 is scoped to the short roadmaps.
- Are the reaction assets able to carry highlight or atom-map data at all in the current schema?
- I did not verify the chemical correctness of any structure or mechanism claim; visual-012 is about a caption/render mismatch, which belongs to the Instructor persona.

### Orchestrator decisions

For each recommendation: the need, the intervention chosen as the least-complex option that fully addresses it, and why.

#### `rec-001` · blocker · Replace the fabricated 'no hydride available' rationale for FAD

*Need.* The chapter's reason for using FAD rather than NAD+ in the two alpha,beta-dehydrogenations is mechanistically wrong: acyl-CoA dehydrogenase and succinate dehydrogenase both transfer the beta hydrogen as a hydride to flavin N5 while a general base takes the alpha proton. The real reason is the redox potential of the couple.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* The correct explanation is a substitution of reasoning, not of media - the figures and roadmap already show the right transformation. What must move is every restatement of the wrong rationale, which appears in three text tiers, a practice answer, two asset learning_goals, two long_descriptions and a roadmap note. No new asset addresses this.

*Consolidates:* `inst-001`

#### `rec-002` · blocker · Stop deriving alkene geometry and enantiomeric outcome from facial relationship alone

*Need.* The chapter states that anti removal 'is why' the E alkene is the sole product and that anti addition 'produces the S enantiomer only'. In a freely rotating acyclic chain neither inference is valid; the outcome comes from the conformation and face the enzyme enforces. The syn/anti assignments for acyl-CoA dehydrogenase and enoyl-CoA hydratase are also disputed by the reviewer.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* The invalid inference is correctable in prose and is certain; the syn/anti fact is not certain (the reviewer flagged it as unverifiable here). Attributing the outcome to enzyme-enforced conformation is correct either way, so the least-complex fix that fully addresses the verified error is to remove the unsupported causal claims rather than assert a stereochemistry that cannot be checked in this environment.

*Consolidates:* `inst-002`, `visual-012`

#### `rec-003` · blocker · Draw the real thiamine diphosphate and fix its formula

*Need.* The asset titled 'Thiamine diphosphate' carries a SMILES that resolves to a monophosphate (C12H17N4O4PS) while its title, alt_text and long_description all promise a diphosphate, and the formula asserted in the description omits sulfur entirely.

*Chosen intervention.* **prose-edit** → figure

*Why this and not more.* A one-token SMILES correction plus a formula correction restores both the structure and the text; the figure itself is otherwise correct and needs no redesign.

*Consolidates:* `inst-003`

#### `rec-004` · blocker · Remove the invented water from the GAPDH figure description

*Need.* The alt_text and long_description of rxn-triose-phosphate-oxidation state that water is a product. No water is formed; the drawn structures balance to a two-hydrogen difference that NAD+ carries away, which the same paragraph then double-counts.

*Chosen intervention.* **prose-edit** → figure

*Why this and not more.* The SMILES is already right; only the accessibility text disagrees with it. This is a text correction on a figure whose stated purpose is to teach atom accounting.

*Consolidates:* `inst-004`

#### `rec-005` · blocker · Correct the glyceraldehyde 3-phosphate enantiomer in two question items

*Need.* ch29-schiff-base-arrow-v2 and a distractor in ch29-retro-aldol-product display (S)-glyceraldehyde 3-phosphate - the L-isomer - while naming it as the substrate of GAPDH and as the aldolase cleavage fragment. The chapter's own figures correctly use the (R) D-isomer.

*Chosen intervention.* **prose-edit** → assessment

*Why this and not more.* A SMILES substitution in two question configs. No pedagogy changes; the items are otherwise sound and their feedback already fires.

*Consolidates:* `inst-005`

#### `rec-006` · blocker · Fix the terse tier's beta-keto acid claim about the citric acid cycle

*Need.* The terse variant says both carbon dioxides leave by beta-keto acid decarboxylation. Only the isocitrate step is; the alpha-ketoglutarate step is an alpha-keto acid oxidative decarboxylation requiring thiamine - the exact discrimination the previous section establishes.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* One sentence in one text tier. The standard and expanded tiers are already correct, so nothing else needs to move, and the shortest tier is the one a struggling reader is most likely to be reading.

*Consolidates:* `stu-001`

#### `rec-007` · blocker · Deliver the authored long descriptions to the reader

*Need.* Every reaction, molecule and teaching-asset block in the compiled chapter carries a mechanism-level long_description that the reader never renders; only alt_text is surfaced, so 41 of 44 figures deliver a species list where the chemistry was written.

*Chosen intervention.* **text-equivalent** → prose

*Why this and not more.* The text already exists, is already compiled into the blocks, and is already rendered for image blocks by ReaderProviderImage. Making the other three block types use the same pattern is the least-complex intervention that fully addresses the need - strictly smaller than rewriting 24 alt texts, and it benefits every chapter, not just this one.

*Consolidates:* `access-001`, `access-008`

#### `rec-008` · high · Make the reaction alt texts state which bond changes

*Need.* Roughly 14 of the 24 reaction alt texts name only reactants and products, so even after rec-007 the short description a learner meets first does not carry the bond-level claim the figure exists to make.

*Chosen intervention.* **sufficient-alt-text** → figure

*Why this and not more.* Once the long description is delivered (rec-007) the bond-level content is reachable, so this becomes an improvement to the first line rather than a missing equivalent. Strengthening the existing sentence is smaller than authoring a new structured description.

*Consolidates:* `access-002`

#### `rec-009` · blocker · Give the roadmaps a structured text equivalent

*Need.* Every node label, per-arrow enzyme and per-arrow teaching note in the five roadmaps is baked into a generated SVG served as an image, and the long description aggregates the reaction types by count rather than attaching them to steps, so the sequence-to-annotation mapping cannot be reconstructed non-visually.

*Chosen intervention.* **structured-chemical-description** → prose

*Why this and not more.* The roadmap spec already holds the ordered steps with their reagents and notes; emitting that structure as text alongside the figure reuses authored content and is far smaller than re-engineering the SVG renderer for accessibility. It also fixes the low-vision legibility problem, since text scales independently of the raster layout.

*Consolidates:* `access-003`, `access-004`

#### `rec-010` · blocker · Provide a non-visual path for the structure-drawing items

*Need.* Both structure_scaffold items are delivered through a Ketcher iframe the platform itself records as not keyboard-complete, with no structured or text entry alternative, so a learner who cannot use a pointer loses the only construct in the bank that asks them to build a structure.

*Chosen intervention.* **alternate-activity** → assessment

*Why this and not more.* The grader already accepts a chemical graph, so the missing piece is an input route, which is a platform capability this chapter cannot supply. Until it exists, an equivalent-construct alternate item is the least-complex intervention available at chapter level.

*Consolidates:* `access-005`

#### `rec-011` · high · Label the hotspot targets by chemical role

*Need.* Both hotspot items ship only a SMILES and a select count, so the atom buttons are announced as 'C atom 2' with no chemical identity, and the on-screen numbering is offset by one from the internal region ids.

*Chosen intervention.* **text-equivalent** → assessment

*Why this and not more.* The chapter's own curved_arrow and ledger items already supply labelled sites and an atom-numbering list; extending the same authored labelling to the hotspot items reuses an established pattern rather than changing the renderer.

*Consolidates:* `access-006`

#### `rec-012` · high · Redistribute the single_select answer positions and match distractor lengths

*Need.* All ten single_select keys are option a, and the correct option is the longest in eight of ten, so the bank is solvable by test-wiseness on exactly the concepts the chapter works hardest to teach.

*Chosen intervention.* **prose-edit** → assessment

*Why this and not more.* Reordering options and trimming the correct option to distractor length is a mechanical edit to existing items; it needs no new questions and it makes the already-strong wrong-answer feedback reachable.

*Consolidates:* `stu-007`

#### `rec-013` · high · Name in the prose every compound and enzyme the questions name

*Need.* Malate, fumarate, succinate, thiolase, ketoacyl synthase and gluconeogenesis are quizzed - two at core difficulty - but appear nowhere in the prose a student reads; some exist only as roadmap node labels.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* Adding the names to the sentences that already describe those steps closes the gap without new questions or figures, and it fixes the same weighting problem the reviewer raised about the cycle's closing three steps.

*Consolidates:* `stu-005`, `stu-016`

#### `rec-014` · high · Correct the enzymatic decarboxylation mechanism for isocitrate dehydrogenase

*Need.* The chapter transfers the neutral beta-keto acid cyclic transition state wholesale onto the enzymatic step, where the substrate is a carboxylate with no proton to deliver and the decarboxylation is metal-assisted.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* A correction to the mechanistic sentence, keeping the (correct) acetoacetic acid illustration and distinguishing it from the enzymatic case. No new figure is needed to state the distinction.

*Consolidates:* `inst-008`

#### `rec-015` · high · Stop claiming the ylide is drawn, and name the base

*Need.* The figure titled 'The thiamine ylide adds to pyruvate' draws the intact thiazolium with C2-H present; the ylide is never depicted anywhere, and the C2 hydrogen disappears between the two sides with no base shown.

*Chosen intervention.* **prose-edit** → figure

*Why this and not more.* The chapter is elsewhere scrupulous about disclosing what a figure does not show; applying that same disclosure here, and naming the base, is smaller than authoring a separate deprotonation figure and matches the chapter's established convention.

*Consolidates:* `inst-011`, `stu-004`

#### `rec-016` · high · Reconcile the aldolase figures with the direction the prose describes

*Need.* The prose describes the cleavage direction, in which the lysine condenses with the C2 ketone of fructose 1,6-bisphosphate; the active-site figure and the arrow question both act on dihydroxyacetone phosphate, which is the product of that cleavage. Separately the retro-aldol figure draws the cyclic furanose while the caption asks the reader to find a carbonyl and a beta hydroxyl.

*Chosen intervention.* **prose-edit** → figure

*Why this and not more.* Both are disclosure problems rather than wrong chemistry: the curated aldolase site is verified in-repo and the furanose is the correct solution-state structure. Stating the direction and the ring-opening step - exactly what rxn-phosphoglucose-isomerase already does - is the least-complex fix and preserves the verified figures.

*Consolidates:* `inst-006`, `inst-007`

#### `rec-017` · high · Close the small prose gaps the reviewers converged on

*Need.* Six load-bearing terms or arguments are used without being established: 'transfer potential' is never defined; Schiff base, imine and iminium are never reconciled; prochirality is used for glycerol without being named and is never connected to the citrate labelling result; the thiazolium charge is explained backwards; the malonyl carboxyl's ATP-and-biotin origin is never stated; and the mutase step is described as an intramolecular migration.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* All six are sentence-level insertions into prose that already exists, and each was independently flagged. None requires a new asset.

*Consolidates:* `stu-013`, `stu-009`, `stu-011`, `stu-018`, `inst-015`, `inst-018`, `inst-019`

#### `rec-018` · high · Qualify the two over-general rules

*Need.* The inventory section states the chapter's eliminations are 'all of them E1cb' with no exception and no per-case argument, and the closing thesis that the chapter contains no new reactions holds only because the lipoamide step of pyruvate dehydrogenase is silently skipped.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* Both are exceptionless claims that the chapter's own content contradicts; qualifying them costs two sentences and preserves the organising argument rather than abandoning it.

*Consolidates:* `inst-017`, `inst-010`

#### `rec-019` · medium · Scale the two PDB captions to what a static render shows

*Need.* Both protein_structure figures are captioned with a motion - a domain closure and a swinging carrier arm - that a single static state cannot convey, and 1CTS is the open unliganded form without the caption saying so.

*Chosen intervention.* **prose-edit** → figure

*Why this and not more.* The figures do carry real architectural information the prose cannot; scaling the caption and naming the conformational state keeps them useful without commissioning new media.

*Consolidates:* `visual-011`, `inst-022`

#### `rec-020` · medium · Add the missing third step of beta-oxidation

*Need.* The section presents an explicitly numbered figure sequence - Step one, Step two, Step four - and the missing NAD+ oxidation is the step that creates the substrate the fourth figure consumes.

*Chosen intervention.* **new-figure** → figure

*Why this and not more.* This is the one place where a new asset is genuinely the least-complex fix: the numbering advertises the gap, the reaction is a two-species transformation the existing reaction renderer already handles, and renumbering the sequence instead would remove the pattern the section is teaching.

*Consolidates:* `visual-004`, `stu-008`

#### `rec-021` · medium · Correct the citrate synthase description and the enol/enolate inconsistency

*Need.* The site-citrate-synthase long description merges His320's note into His274's, losing the carbonyl-polarisation half of the mechanism, and the active-site figure commits to the enol while the ledger question commits to the enolate without either acknowledging the choice.

*Chosen intervention.* **prose-edit** → figure

*Why this and not more.* Both are text corrections against specs that are already authored; the reviewer notes the enol/enolate distinction is genuinely argued in the literature, so a sentence acknowledging it teaches more than silently picking one.

*Consolidates:* `access-007`, `inst-014`

#### `rec-022` · medium · Declare one ionisation-state convention

*Need.* Figures and alt text name neutral free acids while prose, roadmaps and questions use anion names, and one roadmap specifies HOPO3(2-) for the same phosphate another figure draws as H3PO4.

*Chosen intervention.* **instructor-note** → prose

*Why this and not more.* A stated convention plus a note on where ionisation state changes the mechanism resolves the inconsistency without redrawing 24 figures; redrawing would be a large change for a difference the chapter can simply own.

*Consolidates:* `inst-009`

#### `rec-023` · high · Surface the objectives, trouble spots and practice checks the reader currently drops

*Need.* The compiled reader carries no objectives, no trouble spots and no practice checks, and no retrieval opportunity of any kind; 34 objectives, 30 named misconceptions and 10 worked practice answers exist in the package and never reach a student.

*Chosen intervention.* **added-practice** → practice

*Why this and not more.* The content is authored and only the compile-and-render path is missing, so this is a delivery change rather than new authoring. It is scoped as a platform recommendation rather than a chapter correction because it changes the reader chapter schema for every chapter.

*Consolidates:* `stu-002`, `stu-003`

#### `rec-024` · high · Give the comparative arguments a comparative figure

*Need.* Three of the chapter's central arguments are comparisons the chapter never shows side by side: beta-oxidation against biosynthesis, the four recurring electron sinks, and the step-to-mechanism inventory that the closing section is named for. The bank assesses all three.

*Chosen intervention.* **new-figure** → figure

*Why this and not more.* These are genuine visual gaps rather than description gaps, but each needs a designed comparison view rather than a mechanical fix, so they are recorded as recommendations rather than applied in a correction pass.

*Consolidates:* `visual-005`, `visual-007`, `visual-008`

#### `rec-025` · medium · Re-judge the deferred video briefs and fix their colour dependence before production

*Need.* Four of the five briefs describe stepwise bond-level sequences a static series would carry as fully as motion, so holding them for an animation pipeline that cannot render them parks four explanation gaps indefinitely; two briefs also carry a distinction in colour alone and none specifies a caption or transcript deliverable.

*Chosen intervention.* **static-image-sequence** → figure

*Why this and not more.* Converting the four to static sequences unblocks them now, and the colour and caption constraints must be fixed in the brief before anything is produced, whichever medium is chosen.

*Consolidates:* `visual-015`, `stu-019`, `access-009`

#### `rec-026` · high · Broaden assessment coverage and mark a demonstrable item

*Need.* Five stated objectives have no assessment item, no item is demo_eligible, both mechanism-drawing types sit on one concept, and the hardest concept has a single advanced item with no easier rung beneath it.

*Chosen intervention.* **added-practice** → assessment

*Why this and not more.* This is question authoring rather than error correction, so it is recorded rather than applied; it is grouped because all four gaps are addressed by the same expansion pass.

*Consolidates:* `inst-012`, `inst-021`, `stu-015`, `stu-014`

#### `rec-027` · medium · Relocate or duplicate the three misplaced figures

*Need.* The GAPDH oxidation and the flask Claisen sit in the closing section while the prose that argues from them is four to six sections earlier, and the succinate-to-fumarate figure sits in the coenzymes section while that cycle step belongs to the citric acid section.

*Chosen intervention.* **prose-edit** → figure

*Why this and not more.* Reassigning nugget_ids is a metadata change; the figures themselves are correct and need no redrawing.

*Consolidates:* `visual-013`, `inst-016`

#### `rec-028` · low · Fix the reaction-type count mismatch and the accessible-description framing

*Need.* The glycolysis section title promises six reaction types while the roadmap description enumerates seven, and one accessible_description characterises a reaction as 'an enol attacks a ketone carbon' where the prompt withholds that characterisation.

*Chosen intervention.* **prose-edit** → prose

*Why this and not more.* Two small text corrections, each independently flagged, each fixable in place.

*Consolidates:* `stu-017`, `access-011`

### Merged duplicates

Findings from different personas about the same location, consolidated into one recommendation keeping the strongest severity and both learner impacts:

- **Stop deriving alkene geometry and enantiomeric outcome from facial relationship alone** (`rec-002`) — Instructor + Visual Preference: `inst-002`, `visual-012`. Severity kept at **blocker** (the strongest of the group).
- **Stop claiming the ylide is drawn, and name the base** (`rec-015`) — Instructor + Struggling Student: `inst-011`, `stu-004`. Severity kept at **high** (the strongest of the group).
- **Close the small prose gaps the reviewers converged on** (`rec-017`) — Instructor + Struggling Student: `stu-013`, `stu-009`, `stu-011`, `stu-018`, `inst-015`, `inst-018`, `inst-019`. Severity kept at **high** (the strongest of the group).
- **Scale the two PDB captions to what a static render shows** (`rec-019`) — Instructor + Visual Preference: `visual-011`, `inst-022`. Severity kept at **medium** (the strongest of the group).
- **Add the missing third step of beta-oxidation** (`rec-020`) — Struggling Student + Visual Preference: `visual-004`, `stu-008`. Severity kept at **medium** (the strongest of the group).
- **Correct the citrate synthase description and the enol/enolate inconsistency** (`rec-021`) — Accessibility + Instructor: `access-007`, `inst-014`. Severity kept at **medium** (the strongest of the group).
- **Re-judge the deferred video briefs and fix their colour dependence before production** (`rec-025`) — Accessibility + Struggling Student + Visual Preference: `visual-015`, `stu-019`, `access-009`. Severity kept at **medium** (the strongest of the group).
- **Broaden assessment coverage and mark a demonstrable item** (`rec-026`) — Instructor + Struggling Student: `inst-012`, `inst-021`, `stu-015`, `stu-014`. Severity kept at **high** (the strongest of the group).
- **Relocate or duplicate the three misplaced figures** (`rec-027`) — Instructor + Visual Preference: `visual-013`, `inst-016`. Severity kept at **medium** (the strongest of the group).
- **Fix the reaction-type count mismatch and the accessible-description framing** (`rec-028`) — Accessibility + Struggling Student: `stu-017`, `access-011`. Severity kept at **low** (the strongest of the group).

### Retained disagreements

#### Whether the two static PDB renders should stay

- **Learner with Visual Preference:** visual-011 - each figure's stated goal is a motion a single static state cannot show, the residual information is already fully stated in the prose, so they 'function closer to atmosphere than to instruction'.
- **Organic Chemistry Instructor:** inst-022 - keeps the figure and treats the defect as a missing label: the description explains domain closure without saying that 1CTS is the open, unliganded form.

*Resolution.* Keep both figures and apply both fixes (rec-019). The instructor's point is the narrower and more testable one - a reader cannot anchor the closure argument without knowing which state is shown - and it is a precondition for the visual persona's complaint being fixable at all. The visual persona is right that the caption overclaims, so the caption is scaled to what a static state conveys rather than the figure being cut. Cutting them would lose the one thing the prose genuinely cannot supply: that the site is a deep interdomain cleft rather than a shallow surface pocket.

#### Whether to put structures into the roadmap nodes

- **Learner with Visual Preference:** visual-003 - all 36 nodes are name-only although the renderer supports a per-node SMILES, and two roadmaps set structural learning goals that name-only nodes cannot serve.
- **Accessibility Persona:** access-004 - the roadmap SVG is already about 3382 px wide against an 860 px column with 10 px annotation text; anything that widens it worsens an existing low-vision and reflow barrier.

*Resolution.* Both are right about different roadmaps, and the visual persona anticipated this in an open question. Structure nodes are appropriate only for the short roadmaps (beta-oxidation and fatty acid elongation, five nodes each), where they add the oxidation-level pattern without materially widening the figure; the eleven- and ten-node pathway maps stay text-only. Independently of that choice, the accessibility need is met by the structured text equivalent in rec-009, which scales regardless of what the SVG does - so the two recommendations do not compete.

#### What to do about the five deferred video briefs

- **Learner with Visual Preference:** visual-015 - four of five describe stepwise bond-level sequences that a static series would carry as fully as motion, so holding them for animation parks four explanation gaps behind a pipeline that cannot render them.
- **Struggling Student:** stu-019 - the five moments are precisely the transitions where seeing something move would help most, particularly the repeating spiral and carbon provenance, which are intrinsically about change across iterations.
- **Accessibility Persona:** access-009 - whatever is produced, two briefs currently carry a distinction in colour alone and none specifies a caption or transcript.

*Resolution.* Adopt the visual persona's re-judgement for four briefs and the struggling student's exception for the fifth. The carbon-tracking brief is the one whose content genuinely depends on continuity of identity across steps, which is what the student persona is describing; the other four are sequences. The accessibility constraint is not in tension with either and applies to all five before anything is produced (rec-025).

#### Whether the missing retrieval practice is a chapter defect

- **Struggling Student:** stu-002 - no practice, question or self-check block exists anywhere in the compiled reader, and the ten authored practice checks with worked answers are never compiled.
- **Organic Chemistry Instructor:** inst-012, inst-021 - frames the gap as coverage and demonstrability within the question bank rather than as an absence from the reader.

*Resolution.* Both, but at different layers, and neither is applied in this correction pass. The student persona has identified a compile-and-render gap that affects every chapter in the reader (rec-023); the instructor has identified authoring gaps specific to this chapter's bank (rec-026). Treating the first as a chapter defect would misattribute it, and treating the second as a delivery problem would leave five objectives unassessed even after the reader is fixed.

### Places where a description is sufficient (no new asset)

- The four enzyme active-site diagrams: three personas agreed these earn their place, and their authored long descriptions already convey the arrangement, the contacts and the schematic caveat. Once rec-007 delivers that text, no new asset is needed - only the His320 note correction in rec-021.
- The mitochondrion clipart: used for orientation, correctly described, and explicitly stated to show no pathway chemistry. No change needed.
- The 24 reaction figures as drawings: the chemistry rendered is correct in every case the instructor checked, and the localisation gap the visual persona raised is a description-and-highlighting need, not a reason to redraw them.
- The bond_change_ledger and curved_arrow items: the accessibility persona found both fully operable without a pointer, with labelled sites and a visible atom-numbering list. They are the model the hotspot items should follow, not themselves in need of change.
- The glycolysis and glucose-to-CO2 roadmaps as text-only node maps: the visual persona explicitly judged name-only nodes the right call for a locator map over many steps, so only the short roadmaps are candidates for structure nodes.
- The numeric answer keys and reaction-family assignments: the instructor verified 2 CO2 and 3 NADH per turn, 7 passes for palmitate, and every family assignment in the inventory question as defensible.

### Accessibility blockers

- access-001 - the reader discards the authored long_description for 41 of 44 figures, so the bond-level chemistry is unreachable non-visually.
- access-002 - roughly 14 of 24 reaction alt texts name only species, so the single surfaced description does not carry the bond change.
- access-003 - all roadmap node labels, per-arrow enzymes and teaching notes are baked into a generated SVG and exposed to nothing.
- access-005 - both structure_scaffold items go through a Ketcher iframe the platform records as not keyboard-complete, with no alternative input route. This is the unresolved required-access blocker that forces the verdict to blocked.

### Visual opportunities

- The three comparative arguments the chapter makes and assesses but never shows side by side: beta-oxidation against biosynthesis, the four recurring electron sinks, and the step-to-mechanism inventory.
- Carbon provenance through a turn of the citric acid cycle - currently asserted in prose, shown nowhere, and only counted in assessment.
- Energetic coupling - the chapter's opening concept, with no energy representation of any kind anywhere in the chapter.
- Structures in the short roadmap nodes, where the stated goal is an oxidation-level or structural pattern the name-only render cannot carry.
- Localisation of the changed bond in the large reaction figures, where the unchanged remainder dwarfs the change.

### Regression targets for next run

This is the baseline run, so every finding is new. Recheck these stable ids after revision:

`access-001`, `access-002`, `access-003`, `access-004`, `access-005`, `access-006`, `access-007`, `access-008`, `access-009`, `access-010`, `access-011`, `inst-001`, `inst-002`, `inst-003`, `inst-004`, `inst-005`, `inst-006`, `inst-007`, `inst-008`, `inst-009`, `inst-010`, `inst-011`, `inst-012`, `inst-013`, `inst-014`, `inst-015`, `inst-016`, `inst-017`, `inst-018`, `inst-019`, `inst-020`, `inst-021`, `inst-022`, `inst-023`, `stu-001`, `stu-002`, `stu-003`, `stu-004`, `stu-005`, `stu-006`, `stu-007`, `stu-008`, `stu-009`, `stu-010`, `stu-011`, `stu-012`, `stu-013`, `stu-014`, `stu-015`, `stu-016`, `stu-017`, `stu-018`, `stu-019`, `visual-001`, `visual-002`, `visual-003`, `visual-004`, `visual-005`, `visual-006`, `visual-007`, `visual-008`, `visual-009`, `visual-010`, `visual-011`, `visual-012`, `visual-013`, `visual-014`, `visual-015`, `visual-016`


---

## Post-correction record

**Estimated state: major revision (not a second persona verdict).**

Not a new persona verdict. All six chemistry blockers are resolved and the largest accessibility blocker is fixed at the renderer, but access-005 - no non-visual input path for the two structure-drawing items - is a platform capability this chapter cannot supply, so the required-access blocker that forced 'blocked' is still open. Only a fresh four-persona regression run can issue a new verdict.

### Changes applied

- mol-thiamine-diphosphate: SMILES corrected from a monophosphate to the real diphosphate (RDKit now reports C12H18N4O7P2S, two phosphorus, sulfur present), and the formula stated in the long description corrected to include sulfur. — resolves `inst-003`
- rxn-triose-phosphate-oxidation: removed the invented water from the alt text and the long description, and stated explicitly that the phosphate adds and nothing is lost, so the only unaccounted atoms are the two hydrogens NAD+ carries away. — resolves `inst-004`
- Replaced the 'no hydride available' rationale for FAD everywhere it appeared - three text tiers, the practice answer, a trouble spot, two asset learning goals, two long descriptions, a roadmap step note and a question explanation. The chapter now states that a hydride does transfer to flavin N5 while a base takes the alpha proton, and that NAD+ is ruled out by the redox potential of the couple (near 0 V against about -0.32 V). — resolves `inst-001`
- Removed every claim that a facial relationship determines alkene geometry or enantiomeric outcome, in both nugget prose and the acyl-CoA dehydrogenase, enoyl-CoA hydratase and succinate dehydrogenase figure descriptions. Outcomes are now attributed to the conformation and positions the enzyme enforces. — resolves `visual-012`; partially addresses `inst-002`
- ch29-schiff-base-arrow-v2 and the ch29-retro-aldol-product distractor: replaced (S) L-glyceraldehyde 3-phosphate with the D-(R) isomer the figures use, and re-indexed the curved-arrow sites from 2/4/3 to 2/5/6 to match the new atom ordering. — resolves `inst-005`
- Citric acid cycle terse tier: rewritten so the two decarboxylations are described as one beta-keto acid decarboxylation and one alpha-keto acid oxidative decarboxylation by the same thiamine chemistry used on pyruvate. — resolves `stu-001`
- Reader delivery: StructureCard and TeachingAssetLiveRenderer now render content.long_description, and long_description was declared on MoleculeBlockContent, ReactionBlockContent and TeachingAssetBlockContent. All 41 previously-silent figures now deliver their authored bond-level description; the 3 image blocks already did. — resolves `access-001`, `access-008`; partially addresses `access-002`, `access-003`
- Isocitrate dehydrogenase: the neutral beta-keto acid cyclic transition state is now kept explicitly for acetoacetic acid, and the enzymatic step is described as a metal-stabilised enolate from a carboxylate substrate with a residue protonating afterwards. — resolves `inst-008`
- rxn-thiamine-ylide-addition: the description now states that the reactant is drawn as the intact thiazolium and the ylide is not depicted, names the active-site base that removes the C2 hydrogen, and notes the proton is returned later in the cycle. — resolves `inst-011`; partially addresses `stu-004`
- site-citrate-synthase long description: His320's note (polarising the oxaloacetate carbonyl) is no longer merged into His274's, and each residue's on-figure note is now reported as the figure states it. — resolves `access-007`
- Aldolase figures: the retro-aldol description now states that the ring opens first to expose the C2 ketone, and the active-site figure states it is drawn on the three-carbon fragment so it shows the covalent intermediate rather than the hexose. — resolves `inst-006`; partially addresses `inst-007`
- Thiazolium sentence corrected: the ring nitrogen carries a methyl and therefore, having four bonds, a positive charge - the causal direction was previously stated backwards. — resolves `stu-018`
- Named in prose the compounds and enzymes the questions name: succinate, fumarate, L-malate, succinate dehydrogenase, fumarase, malate dehydrogenase, thiolase and ketoacyl synthase. Gluconeogenesis is now glossed in the question option itself. — resolves `stu-016`; partially addresses `stu-005`
- Six prose gaps closed: transfer potential is defined where anhydride cleavage is introduced; Schiff base, imine and iminium are reconciled as one species at first use; prochirality is named for glycerol and connected to the citrate labelling result; the malonyl carboxyl's ATP- and biotin-dependent origin is stated; and the mutase step no longer reads as an intramolecular migration. — resolves `stu-013`, `stu-009`, `stu-011`, `inst-015`, `inst-018`, `inst-019`
- Qualified the two exceptionless claims: the E1cb generalisation now names the condition it holds under and flags aconitase's iron-sulfur cluster as the exception, and the 'no new reactions' thesis now acknowledges the lipoamide disulfide step, which is also named where the pyruvate sequence previously trailed off. — resolves `inst-017`; partially addresses `inst-010`
- Declared one ionisation-state convention at the head of the inventory section - figures draw neutral acids, prose and roadmaps use anion names - and stated the two places where the difference changes the mechanism. — resolves `inst-009`
- ch29-aldol-ledger prompt now states that the active-site figure draws the neutral enol, that the enol-versus-enolate question is argued in the literature, and that the ledger is to be recorded for the enolate as drawn. — resolves `inst-014`
- Both PDB captions scaled to what a static render shows: 1CTS is now identified as the open, unliganded form with the closure described rather than claimed as visible, and the fatty acid synthase caption states the carrier arm is disordered in this crystal form. — resolves `inst-022`, `visual-011`
- rxn-glycerol-to-dhap caption now says it shows the first of two steps rather than promising both. — resolves `inst-023`
- single_select answer positions redistributed across slots 0-3 (previously option 'a' in all ten items); option ids stay bound to their text so answer keys and wrong-answer match patterns are unchanged. — partially addresses `stu-007`
- Glycolysis roadmap description now enumerates six reaction types across ten arrows, matching the section title, and one accessible description no longer characterises the nucleophile as an enol where the prompt withholds that. — resolves `stu-017`, `access-011`

- reader_chapter_builder._concept_wiki_title: spaces now replaced on both paths, fixing 7 of 10 broken Wikipedia links (orchestrator integrity finding, same defect as chapter 28).

### Verification

- Automated test suite — passed — 143 passed
- Backend service tests — passed — 152 passed
- `compile_topic_package --write-runtime` — 65 slides, 44 assets, 21 surfaced / 21 staged across 12 types, verification_required empty
- `[internal source reference — not in this repo] (ideal submission per item, not the key)` — 42/42 answer keys grade correct
- RDKit: mol-thiamine-diphosphate now C12H18N4O7P2S; both corrected glyceraldehyde 3-phosphate structures now CIP (R)
- package scan: 'no hydride can be removed' / 'no hydride can leave' / 'accept single electrons' / 'opposite faces' all 0 occurrences; the 3 remaining 'no hydride is available' strings are explicit negations correcting the misconception
- `npx tsc --noEmit` — no errors in [internal source reference — not in this repo], [internal source reference — not in this repo] or [internal source reference — not in this repo]
- compiled reader: 41 of 44 figures now carry a long_description the renderer displays (the other 3 are image blocks, which already did)

- `HEAD check of the 10 compiled Wikipedia links` — 10/10 resolve (was 3/10)

### Still recommended

- access-005 - structure_scaffold has no non-visual input route; needs the platform's structured_molecule_entry mode or an alternate item of equivalent construct (rec-010).
- access-003 / access-004 - the roadmaps still carry their node labels and per-arrow notes only inside a generated SVG; the long description now reaches the reader but is still an aggregate rather than a per-step enumeration (rec-009).
- access-002 - roughly 14 reaction alt texts still name only species; the bond-level content is now reachable via the delivered long description, so this is no longer an equivalence gap but remains a first-line quality gap (rec-008).
- access-006 - the two hotspot items still ship no named region list, so their atom buttons announce as 'C atom 2' (rec-011).
- stu-002 / stu-003 - the compiled reader still carries no objectives, trouble spots or practice checks; this is a reader-schema change affecting every chapter (rec-023).
- inst-012 / inst-021 / stu-015 - five objectives remain unassessed, no item is demo_eligible, and mechanism-drawing practice is still concentrated on glycolysis (rec-026).
- visual-005 / visual-007 / visual-008 - the three comparative arguments still have no comparative figure (rec-024).
- visual-004 / stu-008 - the beta-oxidation figure sequence still skips step three (rec-020).
- inst-002 - the syn-versus-anti assignments for acyl-CoA dehydrogenase and enoyl-CoA hydratase were NOT flipped. The invalid inference drawn from them was removed, but the reviewer flagged the underlying fact as unverifiable in this environment, so asserting the opposite stereochemistry without a source would trade one unsupported claim for another. Needs a literature check.
- inst-013 / inst-016 / inst-020 / visual-013 - thiolase's covalent acyl-enzyme, the three misplaced figures, and the absent NADP+/reduced-flavin structures remain as described recommendations.

> The baseline verdict at the top of this file is unchanged. A new verdict requires a fresh
> four-persona regression run.

