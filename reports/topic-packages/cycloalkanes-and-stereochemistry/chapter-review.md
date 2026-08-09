# Chapter review — Organic Compounds: Cycloalkanes and Their Stereochemistry (`cycloalkanes-and-stereochemistry`)

_Reviewed 2026-07-31 · chapter version 1 · personas: Instructor, Struggling
Student, Accessibility, Visual Preference_

**Publication readiness: major revision**

Chapter 4 is chemically clean and pedagogically undrawn. The instructor persona machine-verified all 13 distinct SMILES across assets and questions against authentic compounds by formula, canonical connectivity and InChIKey (13/13 correct, including the four formula-identical C7H14/C8H16 pairs that are this family's usual trap) and independently re-derived all 20 answer keys (20/20 correct); every number in the prose survives machine checking, including Boltzmann on the 7.6 kJ/mol axial penalty (95.6:4.4 vs the stated 'about 95%') and Eyring on the 45 kJ/mol barrier (8.1e4 vs 'roughly 100,000 times per second'). The `expanded` tier is a genuine superset of `standard` in all six nuggets, so the default-tier trap that caught ch23, ch30 and ch31 does not recur here. What the chapter does not have is a picture of its own subject. Chair pucker, the axial/equatorial families, the ring flip and the 1,3-diaxial contact are depicted nowhere: every figure in the three chair sections is a flat polygon — the exact object the concept's own trouble_spots entry warns students not to reason from — and the two assets that carry real geometric argument both compile to nothing a learner can see, one because `stereochemistry_conversion` has no entry in the reader compiler's asset-to-block map, the other because a conformational profile carries no steps/minima_labels so no spec is inlined. Two personas blocked on that absence. Two further blockers are chapter-local and narrow: a verified ring-strain correction was applied to the compiled reader but never back-ported to the source, so the source still teaches the error and the next recompile would delete the fix; and both nomenclature short-answer prompts contain their own answers verbatim. Readiness is `major revision` rather than `blocked`: the accessibility persona raised no publication blocker and confirmed every one of the nine question types has a keyboard-complete response path, so — uniquely in this chapter family — the standing structure_scaffold input-path ticket does not apply, because ch4 authors no structure_scaffold item.

### Top blockers
- **[BLOCKER] A verified chemistry correction lives only in the build artifact and the next recompile deletes it** — The compiled reader's expanded tier carries a corrected ring-strain sentence (cyclobutane ~110 kJ/mol, nearly cyclopropane's 115; cyclopentane ~26) that topic.package.json does not have, and that neither file applies to the terse or standard tiers. (instr-001, instr-002, struggle-017)
- **[BLOCKER] The chapter's entire subject — chair geometry — is never drawn** — Chair pucker, the axial/equatorial bond families, the up/down alternation, the ring flip's positional exchange, and the 1,3-diaxial contact are asserted in prose and depicted nowhere a student can see. (vis-001, struggle-001, instr-004, access-001, vis-007, struggle-014, vis-002)
- **[BLOCKER] Both nomenclature short-answer prompts contain their own answer** — 'Give the IUPAC name of the compound with SMILES CC1CCCCC1 (a cyclohexane ring bearing one methyl group)' hands over both name parts of the accepted answer `methylcyclohexane`; the variant likewise contains `ethylcyclopropane`. (struggle-018)

### Top 5 recommended changes
1. **A verified chemistry correction lives only in the build artifact and the next recompile deletes it** — The compiled reader's expanded tier carries a corrected ring-strain sentence (cyclobutane ~110 kJ/mol, nearly cyclopropane's 115; cyclopentane ~26) that topic.package.json does not have, and that neither file applies to the terse or standard tiers. → **prose-edit** (prose, blocker)
2. **The chapter's entire subject — chair geometry — is never drawn** — Chair pucker, the axial/equatorial bond families, the up/down alternation, the ring flip's positional exchange, and the 1,3-diaxial contact are asserted in prose and depicted nowhere a student can see. → **new-figure** (figure, blocker)
3. **Both nomenclature short-answer prompts contain their own answer** — 'Give the IUPAC name of the compound with SMILES CC1CCCCC1 (a cyclohexane ring bearing one methyl group)' hands over both name parts of the accepted answer `methylcyclohexane`; the variant likewise contains `ethylcyclopropane`. → **prose-edit** (assessment, blocker)
4. **Seven level-1 hints state the answer, and several items have no second rung** — The first hint frequently determines the graded answer outright — 'the trans isomer has one chair with no axial methyls' (answer 2), 'cis means one axial, one equatorial' (answer 1), 'bulky groups avoid the orientation that points parallel to the ring axis' (the chapter defines axial as exactly that), 'the strain-free geometry is lowest; the ring-flip transition geometry is highest' (fixes all three cards). → **prose-edit** (assessment, high)
5. **The chapter states the 1,3-diaxial counting rule three ways and one of them is wrong** — Prose and one hint correctly place the partners at 'carbons 3 and 5' (two carbons from C1, which is what '1,3-' means); ch4-chair-tbutyl's level-2 hint says 'three carbons away', which points at C4 — the one position with no 1,3-diaxial relationship to C1. → **prose-edit** (assessment, high)

### Persona status cards
| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 6.6/10 | 2 | 13/13 structures and 20/20 answer keys correct; blocked on a correction that lives only in the build artifact. |
| Struggling Student | 4.6/10 | 2 | The prose is kind and the default tier is a true superset — but there is nothing to look at, and no worked example of any graded procedure. |
| Accessibility Persona | 6.8/10 | 0 | Every question type is keyboard-complete and no description leaks; the failures are at the figure layer and the hint layer. |
| Learner with Visual Preference | 3.4/10 | 1 | A chapter about three-dimensional shape in which no three-dimensional shape is drawn. |

### Affected sections & assets
Sections `nugget-cyclo-nomenclature`, `nugget-cyclo-cis-trans`, `nugget-ring-strain`, `nugget-chair`, `nugget-axial-equatorial`, `nugget-substituted`; assets `stereo-cis-trans-dmcp`, `cep-cyclohexane-flip`, `mol-cyclohexane`, `mol-cyclobutane`, `mol-cyclopentane`, `mol-methylcyclohexane`, `mol-dimethylcyclopentane`, `mol-dimethylcyclohexane`; questions `ch4-cycloalkane-name(-v2)`, `ch4-name-structure-match(-v2)`, `ch4-chair-tbutyl(-v2)`, `ch4-equatorial-count(-v2)`, `ch4-conformer-rank(-v2)`, `ch4-methylcyclohexane-chair`, `ch4-ring-flip-multi(-v2)`, `ch4-ring-strain-matrix-v2`; video brief `video-ring-flip`.

---
## Full evidence

### Independent persona reports

_Presented separately and unmerged. Each persona saw only its own rubric and the chapter package._

#### Organic Chemistry Instructor — 6.6/10

_persona_version 1.0.0 · publication_blockers: instr-001, instr-002_

Not-go as it stands, but the gap is narrow and well-defined. The chemistry that is present is unusually clean: I machine-verified all 13 distinct SMILES in assets and questions against authentic compounds by formula, canonical connectivity and InChIKey (13/13 correct, including the four formula-identical C7H14/C8H16 pairs that are the usual trap), and I independently re-derived all 20 answer keys (20/20 correct). Every number in prose checks out — cyclopropane 115 kJ/mol, twist-boat 23, boat 29, half-chair 45, methyl axial penalty 7.6 kJ/mol; Boltzmann on 7.6 kJ/mol gives 95.6:4.4 (prose says 'about 95%'), Eyring on the 45 kJ/mol barrier gives 8.1x10^4 s^-1 (prose says 'roughly 100,000 times per second'), and the chair population is 99.94% (prose says 'more than 99.9%'). The half-chair is correctly described as four ADJACENT coplanar carbons, distinct from the chair's four alternating ones, and the 1,3-diaxial/gauche link is numerically consistent with the alkanes chapter's 3.8 kJ/mol. Two things stop me assigning it. First, a verified chemistry correction (cyclobutane carries ~110 kJ/mol, nearly cyclopropane's 115, not 'moderate net strain' alongside cyclopentane's 26) was applied to the compiled reader in [commit ref — not in this repo] but never back-ported to topic.package.json, and was not applied to the `standard` tier in either file — so the source of truth still teaches the error, the chapter's own question feedback contradicts it, and the next recompile silently reverts the fix. Second, this is a chapter about three-dimensional shape that puts no three-dimensional picture in front of a student: the ring-flip energy profile compiles without a `spec` and therefore renders as italic alt text, the ring-flip video block is empty and hidden, the cis/trans stereochemistry figure is not compiled into the reader at all, and the five remaining figures are flat polygons — in a chapter whose own listed trouble spot is 'drawing a flat hexagon and reasoning from it about strain'. Fix the drift and give the chair, the flip and the cis/trans pair a real depiction and this is a strong assignable chapter.

**Strengths**

- Every structure is right. All 13 distinct SMILES across assets and question options verify against the authentic compounds by molecular formula, canonical connectivity and InChIKey — cyclopropane LVZWSLJZHVFIQJ, cyclobutane PMPVIKIVABFJJI, cyclopentane RGSFGYAAUTVSQA, cyclohexane XDTMQSROBMDMFD, methylcyclohexane UAEPNZWRGJTJPN, 1,2-dimethylcyclopentane RIRARCHMRDHZAR, 1,2-dimethylcyclohexane KVZJLSYJROEPSQ, methylcyclopentane GDOPTJXRTPNYNR, 1,1-dimethylcyclohexane QEGNUYASOUJEHD, ethylcyclohexane IIEWJVIFRVWJOD, 1,2-dimethylcyclopropane VKJLDXGFBJBTRQ, cycloheptane DMEGYFMYUHOHGS, ethylcyclopropane FOTXAJDDGPYIFU. The formula-identical traps (C7H14 methylcyclohexane vs 1,2-dimethylcyclopentane; C8H16 1,1- vs 1,2-dimethylcyclohexane vs ethylcyclohexane) are all correctly discriminated.
- All 20 answer keys are correct on independent re-derivation, including the two that most often go wrong: trans-1,2-dimethylcyclohexane has a diequatorial chair (2 equatorial methyls) and cis-1,2 is ax/eq in either chair (exactly 1), and the chapter's prose states the reason correctly rather than by assertion.
- Every stated number survives machine checking. Boltzmann on the 7.6 kJ/mol axial penalty gives 95.6:4.4 against the prose's 'about 95%'; Eyring on the 45 kJ/mol half-chair barrier gives 8.1x10^4 s^-1 against 'roughly 100,000 times per second'; the degeneracy-corrected chair population is 99.94% against 'more than 99.9%'; and 7.6 kJ/mol is exactly twice the 3.8 kJ/mol gauche value the prerequisite alkanes chapter teaches.
- The half-chair is described correctly and non-trivially — 'four adjacent carbons are forced into a plane' — which is the real distinction from the chair's four alternating coplanar carbons, and is the detail most chapters get wrong by saying five.
- All four declared prerequisite concept slugs (alkane-nomenclature, alkanes-and-isomers, sp3-hybridization, ethane-conformations) resolve to real concepts in the structure-and-bonding and alkanes-and-stereochemistry packages.
- Unlike several chapters in this family, `expanded` is a genuine superset of `standard` in all six nuggets, so nothing taught at the standard tier is lost to the reader's default expanded tier.
- ch4-ring-flip-multi is a genuinely well-built item: it separates what the flip changes (axial/equatorial) from what it preserves (connectivity, faces, cis/trans), and its distractor explanations name the two real misconceptions — bond breaking, and faces flipping — instead of restating the key.

**Findings**

##### `instr-001` — blocker · chemical-accuracy · confidence 0.97

- **Location** — `nugget_id`: nugget-ring-strain; `section_id`: ring-strain; `concept_slug`: ring-strain; `anchor_text`: each trades a little angle strain for relief of torsional strain, leaving moderate net strain
- **Observation** — topic.package.json — the declared source of truth — still lumps cyclobutane with cyclopentane as 'leaving moderate net strain'. Cyclobutane's total ring strain is ~110 kJ/mol, within 5 kJ/mol of cyclopropane's 115, while cyclopentane's is ~26 kJ/mol. The compiled reader was corrected for exactly this in commit [commit ref — not in this repo] ('ch4 cyclobutane was lumped with cyclopentane as "moderate net strain"; it carries ~110 kJ/mol') but the correction was applied only to frontend/public/reader/topic-chapters/cycloalkanes-and-stereochemistry.json and never back-ported. The same commit's two Wikipedia URL repairs (Naming_cycloalkanes -> Cycloalkane, Cis-trans_isomerism_in_cycloalkanes -> Cis%E2%80%93trans_isomerism, from [commit ref — not in this repo]) are likewise reader-only; the package regenerates the dead URLs.
- **Learner impact** — A student reading the current source-of-truth prose concludes cyclobutane is only mildly strained, which is the single most common ring-strain misconception and directly contradicts this chapter's own question feedback ('Cyclobutane retains significant angle and torsional strain even after puckering', ch4-ring-strain-most-v2) and its comparison-matrix answer key. It also silently arms a regression: the next compile of this package reverts a verified chemistry fix and two dead links back into the live reader.
- **Evidence** — topic.package.json nuggets[2].text.expanded vs reader blk-t2w4o9go content.markdown (which now reads '...The trade is not equally good: cyclobutane still carries about 110 kJ/mol of total strain, nearly as much as cyclopropane, whereas cyclopentane's envelope leaves only about 26 kJ/mol.'). git show [commit ref — not in this repo] and [commit ref — not in this repo] touch only the reader file for this chapter.
- **Recommended outcome** — The authored package and the compiled reader must state the same, verified strain figures, and the chapter's Wikipedia targets must be the resolving ones — the corrections that were validated once need to live where recompilation cannot undo them.

##### `instr-002` — high · chemical-accuracy · confidence 0.96

- **Location** — `nugget_id`: nugget-ring-strain; `section_id`: ring-strain; `anchor_text`: Cyclobutane and cyclopentane pucker to relieve part of their strain
- **Observation** — The `standard` text tier still carries the uncorrected lumping in BOTH the package and the compiled reader, even though commit [commit ref — not in this repo] asserted 'Every edit asserted to land in all affected length variants, so terse, standard and expanded stay in agreement.' The standard tier reads 'Cyclobutane and cyclopentane pucker to relieve part of their strain', with no numbers, so any reader or export set to the standard tier still receives the corrected-away claim.
- **Learner impact** — Students on the standard tier (and any downstream deck/LMS surface that pulls the standard variant) get the version of ring strain that the chapter has already ruled wrong, while their classmates on expanded get the corrected one. The chapter then teaches two different answers to 'how strained is cyclobutane?'
- **Evidence** — topic.package.json nuggets[2].text.standard and reader blk-t2w4o9go._detail_texts.standard are byte-identical and both omit the 110 vs 26 kJ/mol distinction that the expanded tier now makes.
- **Recommended outcome** — The cyclobutane strain claim needs to be consistent across all three text tiers wherever it appears, not only in the tier the reader happens to default to.

##### `instr-003` — high · figure-purpose · confidence 0.93

- **Location** — `asset_id`: cep-cyclohexane-flip; `section_id`: cyclohexane-chair; `nugget_id`: nugget-chair; `anchor_text`: Cyclohexane ring-flip energy profile
- **Observation** — The ring-flip energy profile does not draw. The package authors it as a `conformational_energy_profile` with a full 7-conformer spec, but it compiles into the reader as a `reaction_coordinate` block whose content carries only asset_id/title/alt_text/description — no `spec`. ReaderBlockRenderer's ReactionCoordinateCard sets `failed` immediately when `content.spec` is absent (line 280-283) and renders the alt text as italic prose instead of a diagram. The companion `video-ring-flip` block compiles with url:"" and is_hidden:true, and ReaderBlockRenderer returns null for hidden blocks (line 374). Both blocks appear twice (sections nugget-chair and nugget-axial-equatorial) and neither shows anything.
- **Learner impact** — The chair-to-twist-boat-to-half-chair energy ordering — the chapter's one quantitative conformational argument, and the thing ch4-conformer-rank and ch4-conformer-rank-v2 assess — reaches the student only as a one-sentence caption. Students cannot see that the half-chair is a maximum and the twist-boat a shallow minimum, which is precisely the distinction the rank_order items test.
- **Evidence** — Reader blocks blk-4cmtjx9y and blk-ciysf6cq; zero occurrences of "spec" in the entire compiled reader chapter (grep count 0). [internal source reference — not in this repo], 322-325, 374.
- **Recommended outcome** — The conformational energy ordering the chapter states and assesses needs a representation the student can actually perceive on the reader surface, not a caption standing in for a missing figure.

##### `instr-004` — high · visual-opportunity · confidence 0.94

- **Location** — `concept_slug`: cyclohexane-chair; `section_id`: axial-equatorial-ring-flip; `nugget_id`: nugget-axial-equatorial; `anchor_text`: Six axial bonds stand parallel to the ring axis, alternating up and down on successive carbons.
- **Observation** — There is no chair drawing anywhere in the compiled chapter. Every rendering figure is a flat polygon: mol-cyclohexane (C1CCCCC1), mol-methylcyclohexane (CC1CCCCC1) and mol-dimethylcyclohexane (CC1CCCCC1C) all render as hexagons. Axial vs equatorial geometry, the alternating up/down axial pattern, the ring flip's positional exchange, and the 1,3-diaxial contact across the ring are all taught in words alone. The chapter's own listed trouble spot for cyclohexane-chair is 'Drawing a flat hexagon and reasoning from it about strain' — which is exactly what the reader supplies.
- **Learner impact** — Students cannot form the spatial model the chapter's last three concepts depend on. They are then asked in ch4-chair-tbutyl to place a substituent axial or equatorial on a chair they have never been shown, and in ch4-equatorial-count to count equatorial methyls in a chair they have never seen drawn. The hint 'Draw both chairs' asks for a skill the chapter never demonstrates.
- **Evidence** — Reader blocks blk-d69hlje0, blk-4n97fgbg, blk-1fipmwum, blk-8uoppt3t are all flat `molecule` blocks; the only non-flat assets (cep-cyclohexane-flip, video-ring-flip) do not render (instr-003). Trouble spot at concepts[3].trouble_spots[0].
- **Recommended outcome** — The chair geometry, the axial/equatorial distinction, and the flip's positional exchange need a depiction on the student surface — the chapter currently asks students to reason in three dimensions from two-dimensional polygons it has itself warned against.

##### `instr-005` — high · figure-purpose · confidence 0.95

- **Location** — `asset_id`: stereo-cis-trans-dmcp; `section_id`: cycloalkane-cis-trans; `nugget_id`: nugget-cyclo-cis-trans; `concept_slug`: cycloalkane-cis-trans
- **Observation** — The cis/trans concept has no stereochemical figure on the reader surface. The authored `stereochemistry_conversion` asset stereo-cis-trans-dmcp (wedge/wedge vs wedge/dash 1,2-dimethylcyclopentane) is compiled into the deck-creator and LMS-module outputs but is absent from the reader chapter entirely — section nugget-cyclo-cis-trans contains only a text block, one molecule block and a Wikipedia link. The one figure that is present, mol-dimethylcyclopentane, carries the flat SMILES `CC1CCCC1C`; RDKit confirms zero specified stereocenters, so it renders identically for cis and trans. The prose meanwhile instructs the student to read wedges and dashes ('a cis pair appears as two wedges (or two dashes) and a trans pair as one of each') against a drawing that has neither.
- **Learner impact** — The chapter's entire stereochemical vocabulary is delivered without a single stereochemical picture, and its two assessment items (ch4-cis-trans-sort, ch4-cis-trans-sort-v2) are purely verbal face-sorting with no structures either. A student can complete this concept end to end without ever seeing what cis and trans look like — the exact confusion the concept's trouble spot names.
- **Evidence** — grep for stereo-cis-trans-dmcp hits deck-creator, lms-modules and assets.manifest.json but not frontend/public/reader/topic-chapters/cycloalkanes-and-stereochemistry.json. Asset alt_text promises 'Side-by-side wedge-and-dash drawings'. RDKit: CC1CCCC1C -> C7H14, InChIKey RIRARCHMRDHZAR-UHFFFAOYSA-N, no stereo descriptors.
- **Recommended outcome** — The cis/trans distinction needs a representation the student can see and compare side by side on the reader surface, and the assessment for this concept needs at least one item anchored to a depicted structure rather than to synonymous English phrases.

##### `instr-006` — high · retrieval-practice · confidence 0.92

- **Location** — `concept_slug`: cycloalkane-cis-trans; `question_slug`: ch4-cis-trans-sort; `anchor_text`: Confusing configurational cis/trans isomers with interconverting conformations
- **Observation** — The chapter's stated #1 trouble spot — configuration vs conformation — is never assessed under its own concept. Both cycloalkane-cis-trans items (ch4-cis-trans-sort and -v2) only ask the student to recognise that 'both up' and 'same face' are synonyms; neither touches why the isomers cannot interconvert. The nugget's practice_check does ask exactly the right question ('Why can cis- and trans-1,2-dimethylcyclopentane be separated... while conformations of butane cannot?'), but all six practice_checks and all six trouble_spots compile into no reader block at all (zero occurrences of either string in the compiled chapter).
- **Learner impact** — The best retrieval question in the chapter is authored and then discarded before it reaches a student, and the misconception the author explicitly anticipated goes untested. Students who hold it will pass both cis/trans items.
- **Evidence** — Compiled reader: grep -c 'practice_check|trouble_spot' = 0. topic.package.json nuggets[1].practice_check; concepts[1].trouble_spots[0]. Question bank items ch4-cis-trans-sort / -v2 answer keys are pure synonym mapping.
- **Recommended outcome** — The configuration-vs-conformation distinction needs a retrieval opportunity that actually reaches the student, and the six authored practice_checks need a surface — right now the chapter's formative layer exists only in the source file.

##### `instr-007` — medium · notation-consistency · confidence 0.9

- **Location** — `question_slug`: ch4-chair-tbutyl; `concept_slug`: substituted-cyclohexanes; `anchor_text`: Axial substituents clash with the two axial hydrogens three carbons away (1,3-diaxial strain)
- **Observation** — The chapter states the 1,3-diaxial relationship three different ways and one of them is wrong. Prose and ch4-methylcyclohexane-chair both locate the partners correctly ('the axial hydrogens on carbons 3 and 5', 'the axial hydrogens two carbons away'), but ch4-chair-tbutyl hint level 2 says 'the two axial hydrogens three carbons away'. From C1 the axial partners are C3 and C5 — two carbons away, which is what '1,3-' means.
- **Learner impact** — A student who takes the hint literally counts to C4 and looks across the ring at the one position that has NO 1,3-diaxial relationship to C1 — the position whose axial hydrogen points the other way. This is the single most error-prone count in chair analysis, and it is the chapter's own hint that miscounts it.
- **Evidence** — ch4-chair-tbutyl feedback_bundle.hints[1].text vs ch4-methylcyclohexane-chair wrong_answer_explanations[option_id 'b'] ('two carbons away') and nugget-substituted ('the axial hydrogens on carbons 3 and 5').
- **Recommended outcome** — All three surfaces need to name the 1,3-diaxial partners the same way, and the hint's count must match the '1,3-' label the chapter uses everywhere else.

##### `instr-008` — medium · notation-consistency · confidence 0.93

- **Location** — `question_slug`: ch4-ring-strain-matrix-v2; `concept_slug`: ring-strain; `anchor_text`: about 26 kcal/mol of ring strain
- **Observation** — Prose and figure captions use kJ/mol exclusively (115, 110, 26, 23, 29, 45, 7.6). Four question feedbacks switch to kcal/mol without conversion: ch4-ring-strain-matrix-v2 'about 26 kcal/mol' (= 109 kJ/mol, the same cyclobutane strain the prose calls 110), ch4-ring-flip-multi 'about 10 kcal/mol uphill' (= the prose's 45 kJ/mol barrier), ch4-ring-flip-multi-v2 'about 1.8 kcal/mol' (= the prose's 7.6 kJ/mol), ch4-chair-tbutyl 'nearly 5 kcal/mol'. I verified every conversion is numerically right — the values agree, only the units clash.
- **Learner impact** — The collision is worst for cyclobutane: the prose says '110' and the feedback for the very same comparison says '26', which reads as a contradiction unless the student notices the unit change — and 26 is also the number this chapter assigns to cyclopentane in kJ/mol. A student cross-checking the two surfaces will conclude one of them is wrong.
- **Evidence** — ch4-ring-strain-matrix-v2 / ch4-ring-flip-multi / ch4-ring-flip-multi-v2 / ch4-chair-tbutyl feedback_bundle.generic_incorrect_explanation, against nugget-ring-strain, nugget-chair and nugget-substituted prose.
- **Recommended outcome** — One energy unit across prose, captions and question feedback; where a second unit is genuinely useful it must be given as an explicit conversion rather than a bare alternative number.

##### `instr-009` — medium · sequencing · confidence 0.87

- **Location** — `question_slug`: ch4-methylcyclohexane-chair; `concept_slug`: axial-equatorial-ring-flip; `nugget_id`: nugget-axial-equatorial
- **Observation** — Two of the four items tagged to `axial-equatorial-ring-flip` require reasoning the axial-equatorial nugget explicitly defers to the next concept. ch4-methylcyclohexane-chair asks which chair of methylcyclohexane is preferred and its feedback invokes 1,3-diaxial strain and the 7.6 kJ/mol penalty; ch4-ring-flip-multi-v2 asks the student to affirm 'the equatorial-methyl chair is lower in energy' and cites 1.8 kcal/mol. The nugget that concept points at ends by saying only that 'their equilibrium becomes the central tool' — the equatorial preference, the 1,3-diaxial origin and the number all arrive in nugget-substituted, one concept later.
- **Learner impact** — A student working the axial-equatorial concept in isolation (concept-map practice, a spaced-review set, or an assignment scoped to that concept) is asked for a result the chapter has not yet given them, and gets feedback citing a strain interaction they have not met.
- **Evidence** — nugget-axial-equatorial text.expanded final paragraph vs ch4-methylcyclohexane-chair.feedback_bundle and ch4-ring-flip-multi-v2 option 'c'; the equatorial preference and 7.6 kJ/mol first appear in nugget-substituted (order 6).
- **Recommended outcome** — Items must be tagged to the concept that actually teaches what they test, or the axial-equatorial nugget must carry the equatorial-preference result those items depend on.

##### `instr-010` — medium · assessment-readiness · confidence 0.91

- **Location** — `question_slug`: ch4-name-structure-match; `concept_slug`: cycloalkane-nomenclature
- **Observation** — Both matching_pairs items give the answer away in the prompt text. Left items are verbal restatements of the names on the right: 'A four-membered ring, unsubstituted' pairs to 'Cyclobutane'; 'A six-membered ring bearing two CH3 on one carbon' pairs to '1,1-Dimethylcyclohexane'; in the v2 item 'A three-membered ring bearing two CH3 on adjacent carbons' pairs to '1,2-Dimethylcyclopropane'. Every structural feature the name encodes is already stated in English on the left. The structures are attached as structure_smiles (all six verified correct by InChIKey) but are not needed to answer.
- **Learner impact** — The two items intended to assess reading structures and assigning names instead assess knowing that 'four-membered' means 'cyclobut-'. A student who cannot read a skeletal ring at all scores full marks, and the instructor gets no signal on the skill.
- **Evidence** — ch4-name-structure-match student_config.left[*].text vs right[*].text; same pattern in ch4-name-structure-match-v2.
- **Recommended outcome** — The naming items need the structural information to live in the depiction rather than in the item text, so that reading the structure is what the item measures.

##### `instr-011` — medium · objective-alignment · confidence 0.92

- **Location** — `question_slug`: ch4-cycloalkane-name-v2; `concept_slug`: cycloalkane-nomenclature; `anchor_text`: decide whether the ring or the chain is the parent
- **Observation** — The nomenclature objective names a decision the assessment never exercises. All four nomenclature items are cases where the ring wins (methylcyclohexane, ethylcyclopropane with ring 3 >= chain 2, methylcyclopentane, 1,1-dimethylcyclohexane, ethylcyclohexane, 1,2-dimethylcyclopropane, cyclobutane, cycloheptane). The only chain-wins case in the chapter is the worked line in prose (CH3CH2CH2CH2-C3H5 = 1-cyclopropylbutane) and it is never assessed. ch4-cycloalkane-name-v2's hint even says 'Compare the ring size with the chain length to choose the parent' for an item where the comparison is 3 vs 2 and the ring wins anyway.
- **Learner impact** — The half of the objective that is actually hard — recognising when the chain outranks the ring — is taught in one sentence and tested never. Students will apply 'the ring is always the parent' and be right on all four items.
- **Evidence** — concepts[0].learning_objectives / nuggets[0].learning_objectives vs the four nomenclature question_sets; prose anchor in nugget-cyclo-nomenclature text.expanded paragraph 3.
- **Recommended outcome** — At least one nomenclature item must present a compound where the attached chain outranks the ring, so the decision the objective names is the thing being decided.

##### `instr-012` — medium · assessment-readiness · confidence 0.85

- **Location** — `question_slug`: ch4-chair-tbutyl; `concept_slug`: substituted-cyclohexanes
- **Observation** — Both `chair` items are answerable by accepting the interface default. ChairPlacementRenderer initialises the orientation select to 'equatorial' (`value={current?.orientation ?? "equatorial"}`, and updateSubstituent defaults orientation to 'equatorial'), and ChairGrader runs with allow_ring_rotation defaulting to true, so any ring position matches. Both ch4-chair-tbutyl and ch4-chair-tbutyl-v2 expect 'equatorial'. A student who clicks any one of the twelve stubs, or picks any ring position from the select and touches nothing else, is graded correct.
- **Learner impact** — The chapter's only two workspace items — the only place a student manipulates a chair rather than reading about one — have zero discrimination. An instructor reading a class report cannot tell who understands the equatorial preference from who clicked once.
- **Evidence** — [internal source reference — not in this repo], 289; [internal source reference — not in this repo] (allow_ring_rotation default True); both answer keys use orientation 'equatorial'.
- **Recommended outcome** — The chair items need at least one case whose correct answer is not the interface's resting state — for example a disubstituted ring where the student must decide which group goes axial — so that the workspace measures a decision.

##### `instr-013` — medium · conceptual-support · confidence 0.88

- **Location** — `concept_slug`: substituted-cyclohexanes; `nugget_id`: nugget-substituted; `anchor_text`: The 7.6 kJ/mol axial penalty for methyl grows with substituent size
- **Observation** — The 7.6 kJ/mol axial-methyl penalty is asserted, never derived, even though the chapter has already supplied both ingredients. The prose correctly calls the 1,3-diaxial interaction 'a steric strain identical in origin to the gauche interaction of butane', and the prerequisite alkanes package puts gauche butane at 3.8 kJ/mol — so 7.6 is exactly two gauche-type interactions, one with the axial H on C3 and one with the axial H on C5. The chapter states 7.6, states 'carbons 3 and 5', states the gauche connection, and never joins them.
- **Learner impact** — 7.6 kJ/mol becomes a number to memorise rather than a count of interactions. Students who see the 2 x 3.8 decomposition can predict the penalty for any group from its per-interaction value and can reason about 1,3-disubstituted cases; students given only the total cannot.
- **Evidence** — nugget-substituted text.expanded; alkanes-and-stereochemistry package gives 'gauche conformation (60 deg) lies about 3.8 kJ/mol higher'. 2 x 3.8 = 7.6 exactly.
- **Recommended outcome** — The axial penalty should be presented as a count of identifiable interactions the student can reproduce, connecting it to the gauche value they already own, rather than as a bare total.

##### `instr-014` — medium · missing-example · confidence 0.89

- **Location** — `concept_slug`: substituted-cyclohexanes; `question_slug`: ch4-equatorial-count; `anchor_text`: predict the preferred chair of mono- and disubstituted cyclohexanes
- **Observation** — Disubstituted cyclohexane coverage stops at the 1,2 relationship. The prose treats only cis/trans-1,2-dimethylcyclohexane, and both assessment items (ch4-equatorial-count, -v2) are 1,2 cases. The 1,3 and 1,4 patterns — where the axial/equatorial consequences invert relative to 1,2 (cis-1,3 is diequatorial, trans-1,3 is ax/eq; trans-1,4 is diequatorial, cis-1,4 is ax/eq) — never appear, and neither does any substituent-size ordering beyond methyl and tert-butyl. Notably ch4-cis-trans-sort-v2 does use a 1,3 relationship (1,3-dimethylcyclobutane) but only for face vocabulary, never carried into chair analysis.
- **Learner impact** — Students generalise 'cis means one axial one equatorial' from the only case they see, which is true for 1,2 and 1,4 and false for 1,3. This is the highest-frequency downstream error in conformational analysis and it is set up here. It also undercuts the promised carry-forward to sugars and steroids, where 1,3-diaxial relationships dominate.
- **Evidence** — nugget-substituted text.expanded paragraph 2; ch4-equatorial-count and ch4-equatorial-count-v2 both 1,2; ch4-cis-trans-sort-v2 uses a 1,3 ring for face sorting only.
- **Recommended outcome** — The chapter needs at least one worked case and one assessment item where the cis/trans-to-axial/equatorial mapping differs from the 1,2 pattern, so students learn the mapping is position-dependent rather than fixed.

##### `instr-015` — low · sequencing · confidence 0.83

- **Location** — `concept_slug`: substituted-cyclohexanes; `nugget_id`: nugget-substituted; `anchor_text`: a steric strain identical in origin to the gauche interaction of butane
- **Observation** — concepts[5].prerequisites lists only ['axial-equatorial-ring-flip', 'cycloalkane-cis-trans'], but the nugget's central explanation leans on butane gauche strain. The slug `butane-conformations` exists in the alkanes-and-stereochemistry package (I confirmed all four declared prerequisites resolve there or in structure-and-bonding) and is the natural declared dependency.
- **Learner impact** — Concept-map traversal and prerequisite-gated review will not route a student who is shaky on gauche strain back to the material this concept's key analogy assumes.
- **Evidence** — topic.package.json concepts[5].prerequisites; nugget-substituted text.expanded; grep confirms 'butane-conformations' is defined in content/organic/topic-packages/alkanes-and-stereochemistry/topic.package.json.
- **Recommended outcome** — The declared prerequisites should cover what the prose actually assumes, so prerequisite-driven remediation reaches the right earlier material.

##### `instr-016` — low · notation-consistency · confidence 0.8

- **Location** — `nugget_id`: nugget-cyclo-nomenclature; `concept_slug`: cycloalkane-nomenclature; `anchor_text`: is 1-cyclopropylbutane, not butylcyclopropane
- **Observation** — The ring-vs-chain rule is stated as absolute, but it is a textbook convention that current IUPAC recommendations reverse. Under P-52.2.8 of the 2013 recommendations a ring is always senior to a chain, so C3H5-C4H9 is named butylcyclopropane — which is also what PubChem and common structure-drawing software return. The chapter's chosen illustrative example is precisely a case where the two conventions disagree, and it presents the older answer as the only correct one.
- **Learner impact** — A student who looks the compound up, or names it in ChemDraw, gets the answer the chapter calls wrong. Since this example is the chapter's sole illustration of the ring-vs-chain decision, the collision lands on the one case they are most likely to check.
- **Evidence** — nugget-cyclo-nomenclature text.expanded paragraph 3; terse and standard tiers state the same rule.
- **Recommended outcome** — Where the chapter teaches a textbook convention that current IUPAC practice has superseded, students need to know that is what is happening, so an outside lookup reads as a convention difference rather than as an error.

##### `instr-017` — low · figure-accuracy · confidence 0.82

- **Location** — `asset_id`: mol-cyclobutane; `concept_slug`: ring-strain; `anchor_text`: Line structure of cyclobutane, a square of four carbon atoms.
- **Observation** — The alt text for mol-cyclobutane describes 'a square of four carbon atoms' and mol-cyclopentane 'a pentagon of five carbon atoms', while the adjacent prose in the same section explains that cyclobutane folds and cyclopentane adopts an envelope pucker specifically because the planar polygon is not the real geometry. The asset's own learning_goal says 'a four-membered ring that puckers to relieve torsional strain' — the alt text describes the opposite of the teaching point.
- **Learner impact** — The description a student receives reinforces the flat-polygon model the section is written to dislodge, and for a student relying on the description rather than the image it is the only geometric statement they get.
- **Evidence** — assets mol-cyclobutane / mol-cyclopentane accessibility.alt_text vs learning_goal and nugget-ring-strain text.expanded; same strings in reader blocks blk-9275jb28 and blk-qpu2nek2.
- **Recommended outcome** — Figure descriptions for the small rings should say what the drawing is (a skeletal polygon) without asserting a planar geometry the surrounding prose is arguing against.

**Open questions**

- Which surface is authoritative when the compiled reader and topic.package.json disagree? Commits [commit ref — not in this repo] and [commit ref — not in this repo] corrected the reader only, so the pipeline currently treats the compiled artifact as editable. If that is intended, the 'source of truth' label on topic.package.json is misleading; if not, instr-001 is a live regression waiting on the next compile.
- stereo-cis-trans-dmcp compiles into frontend/public/reader/lms-modules/ and the deck-creator output but not into the reader chapter. Is that a compiler gap for the `stereochemistry_conversion` type, or a deliberate exclusion? An earlier chapter (carbohydrates) recorded the same asset type never rendering in the reader, which suggests the former.
- The reaction_coordinate reader block carries no `spec`, which makes the diagram unrenderable by construction. Is the compiler expected to inline the conformational_energy_profile spec into the block, and is `reaction_coordinate` even the right block type for a conformational profile given the repo's own conformational-energy-profile-authoring guidance?
- ch4-equatorial-count uses question_type numeric_with_units for a unitless count of methyl groups. The grader handles it (no expected unit, absolute tolerance 0, so a bare '2' grades correct), but the type name and the 'with units' renderer may prompt students to supply a unit that will fail to parse. Is a plain numeric type available?
- demo_eligible is false on all 20 items, so this chapter contributes nothing to the public demo surface. Intended while publishing.available is false, or an oversight?

#### Struggling Student — 4.6/10

_persona_version 1.0.0 · publication_blockers: struggle-001, struggle-018_

The prose in this chapter is unusually kind to a shaky reader: the sections are short, each opens with a plain topic sentence, and — unlike several sibling chapters — the default `expanded` tier is a genuine superset of `standard`, so every load-bearing term (cis, trans, angle strain, torsional strain, chair, axial, equatorial, ring flip, 1,3-diaxial) is actually defined at the depth a default reader receives. What the chapter does not have is anything to look at. Three of six sections and four of ten graded items reason about the geometry of a chair, and the compiled reader contains no picture of a chair anywhere: cyclohexane is drawn as the flat hexagon the prose tells me not to reason from, the ring-flip energy profile compiles without a `spec` so it renders as italic alt text instead of a diagram, and the ring-flip animation is compiled `is_hidden` with an empty url. The one asset that could have shown cis versus trans (`stereo-cis-trans-dmcp`) never reaches the reader at all, so the paragraph that teaches me to read wedges and dashes sits beside a flat, stereochemistry-free drawing. I am asked to picture axial bonds "parallel to the ring axis" and a substituent "crowding the axial hydrogens on carbons 3 and 5 across the ring" purely from sentences — and at that point I stop reading and start guessing. On top of that there is no worked example of any procedure the chapter grades, the six authored `practice_check` items never compile into the reader so there is no checkpoint between a section and a cold question bank, most hint ladders are a single rung and several of those rungs simply state the answer, and the two nomenclature questions put the answer in the prompt's own parenthetical.

**Strengths**

- The default `expanded` tier is a real superset of `standard` in all six nuggets — every load-bearing term (cis, trans, angle strain, torsional strain, chair, axial, equatorial, ring flip, 1,3-diaxial) is defined at the depth a default reader actually receives. This is the trap that caught ch30 and ch31, and this chapter avoids it.
- Sections are short and evenly sized (5-7 minutes), each opens with a concrete topic sentence, and each ends by pointing forward to the next section ("folding into the three-dimensional chair conformation described next", "carries directly into the analysis of substituted cyclohexanes later in the chapter") — a struggling reader always knows why the current section exists.
- ch4-ring-flip-multi names two genuine wrong models (bonds break during a flip; faces invert during a flip) as distractors and answers each with a specific, non-generic correction rather than a restatement of the right answer.
- The comparison_matrix items (cyclopropane vs chair cyclohexane, two features, two cases) are exactly the right shape for a shaky student: small, structured, and their cell-level wrong-answer explanations point at the physical cause rather than the score.
- Concept prerequisites are declared and correctly ordered, and each concept carries a named trouble spot that matches the real failure mode of that topic.
- The chair question's answer key (`expected_orientations` with position + orientation) matches the platform's `ChairGrader` and its keyboard-complete `ChairPlacementRenderer`, so the one constructed-response item in the chapter is genuinely answerable and gradeable.

**Findings**

##### `struggle-001` — blocker · conceptual-support · confidence 0.95

- **Location** — `section_id`: nugget-chair; `concept_slug`: cyclohexane-chair; `nugget_id`: nugget-chair; `anchor_text`: four carbons define a plane while the remaining two pucker to opposite sides
- **Observation** — The compiled reader contains no depiction of a chair conformation anywhere in the chapter. Every figure in sections `nugget-chair`, `nugget-axial-equatorial`, and `nugget-substituted` is a flat 2D line structure (blk-d69hlje0 cyclohexane hexagon, blk-4n97fgbg / blk-1fipmwum methylcyclohexane, blk-8uoppt3t 1,2-dimethylcyclohexane). The chair itself, the axial bond, the equatorial bond, and the 1,3-diaxial contact are described only in sentences: "Six axial bonds stand parallel to the ring axis, alternating up and down on successive carbons" and "the axial methyl approaches the axial hydrogens on carbons 3 and 5 across the ring". The two blocks that were meant to carry the geometry are both non-functional (see struggle-002). Meanwhile the graded surface DOES have a chair picture: `ChairPlacementRenderer` draws a real chair with clickable axial and equatorial stubs — so the first chair a student ever sees is inside a scored question.
- **Learner impact** — A student who cannot build a 3D object from prose has no way to complete the chapter's required step — locate axial versus equatorial on a ring and see why C1, C3, and C5 axial bonds point the same way. I reread the paragraph two or three times, fail to picture it, and then answer ch4-chair-tbutyl, ch4-methylcyclohexane-chair, ch4-equatorial-count and ch4-conformer-rank by pattern-matching remembered words ("equatorial is the good one") rather than by reasoning. The 1,3-diaxial explanation is unfollowable without a picture, so the chapter's terminal concept is memorized, not understood.
- **Evidence** — frontend/public/reader/topic-chapters/cycloalkanes-and-stereochemistry.json blocks blk-d69hlje0, blk-4n97fgbg, blk-1fipmwum, blk-8uoppt3t are all `block_type: molecule` with flat SMILES; topic.package.json `assets[]` contains no chair asset of any kind; [internal source reference — not in this repo].
- **Recommended outcome** — Three sections and four graded items depend on chair geometry that the chapter never shows; the reader needs a durable, inspectable representation of the chair — the ring shape, one axial and one equatorial bond on the same carbon, and the C1/C3/C5 axial relationship — before the axial/equatorial vocabulary is used to reason.

##### `struggle-018` — blocker · assessment-readiness · confidence 0.9

- **Location** — `question_slug`: ch4-cycloalkane-name; `concept_slug`: cycloalkane-nomenclature; `anchor_text`: Give the IUPAC name of the compound with SMILES CC1CCCCC1 (a cyclohexane ring bearing one methyl group).
- **Observation** — Both nomenclature short-answer items put the answer in the prompt. The parenthetical "(a cyclohexane ring bearing one methyl group)" contains both name parts of the accepted answer `methylcyclohexane`; the variant's parenthetical "(a cyclopropane ring bearing one ethyl group)" likewise contains `ethylcyclopropane`. The only thing left for the student is word order, and the single hint ("The ring is the parent; one substituent requires no number") supplies that too.
- **Learner impact** — I answer both items correctly with no idea whether I can name a cycloalkane, and the chapter's only free-response nomenclature practice tells me I am fine when I may not be. When the same skill is assessed later without the parenthetical, the failure is a surprise — which is the specific way over-cued practice hurts low-confidence students most.
- **Evidence** — compiled/question-set.json ch4-cycloalkane-name `prompt_text` versus `answer_key [redacted]`; ch4-cycloalkane-name-v2 prompt versus `["ethylcyclopropane", ...]`.
- **Recommended outcome** — The prompt's structural gloss — present because SMILES is not rendered as a structure (struggle-015) — hands over the answer; the item needs the student to read the structure rather than the description, without leaving a text-only reader with nothing to work from.

##### `struggle-002` — high · media-equivalence · confidence 0.93

- **Location** — `section_id`: nugget-chair; `asset_id`: cep-cyclohexane-flip; `anchor_text`: Cyclohexane ring-flip energy profile
- **Observation** — Both `reaction_coordinate` blocks compiled from `cep-cyclohexane-flip` (blk-4cmtjx9y and blk-ciysf6cq) carry only asset_id/title/alt_text/description — no `spec`. `ReactionCoordinateCard` sets `failed` immediately when `content.spec` is absent and renders the alt text in italics instead of a diagram, so the ring-flip energy profile is a text card in both sections. In the same two sections the ring-flip video block (blk-chgbfhfg, blk-9o04cps5) is compiled with `"url": ""` and `is_hidden: true`, and ReaderBlockRenderer returns null for hidden blocks. The chapter's one dynamic idea therefore has zero working visual representation.
- **Learner impact** — The three energy values I am graded on (chair 0, twist-boat ~23, boat ~29, half-chair ~45 kJ/mol) exist only as numbers embedded in a paragraph. Ranking them in ch4-conformer-rank becomes a memory task rather than a reading-off-the-diagram task, and a student who is weak at holding four numbers in mind guesses the middle card. The heading "Reaction-coordinate diagram — ChemIllusion" above a sentence also makes me think my browser failed to load something, so I scroll past it.
- **Evidence** — [internal source reference — not in this repo] lines 275-298 (`if (!spec) { setFailed(true); return; }`) and line 374 (`if (block.is_hidden) return null;`); compiled blocks blk-4cmtjx9y, blk-ciysf6cq, blk-chgbfhfg, blk-9o04cps5.
- **Recommended outcome** — The ring-flip energy ordering is currently prose-only; the reader needs the conformer sequence and its relative energies delivered in a form a student can scan and re-check, and the chapter should not display a figure frame that resolves to nothing.

##### `struggle-003` — high · conceptual-support · confidence 0.94

- **Location** — `section_id`: nugget-cyclo-cis-trans; `asset_id`: stereo-cis-trans-dmcp; `anchor_text`: a cis pair appears as two wedges (or two dashes) and a trans pair as one of each
- **Observation** — `stereo-cis-trans-dmcp` (type `stereochemistry_conversion`, authored with the labels "same face = cis" / "opposite faces = trans") does not appear in the compiled reader at all — section `nugget-cyclo-cis-trans` compiles to exactly three blocks: text, one flat molecule (blk-9fqhikri), and a Wikipedia link. The paragraph teaches me to read wedge-and-dash notation and then gives me nothing drawn in wedge-and-dash to read. The accompanying figure is `CC1CCCC1C` with no stereobonds, whose alt text says "cis and trans configurations exist" while the drawing itself distinguishes neither.
- **Learner impact** — Cis/trans is the chapter's first new idea and the vocabulary the last section depends on. Being told what two wedges would look like, while looking at a picture with no wedges, is exactly where I decide the drawing rules are arbitrary and start memorizing the words "same face" and "opposite faces" without attaching them to anything I can draw. On a later exam question that shows a wedge/dash structure I will guess.
- **Evidence** — topic.package.json asset `stereo-cis-trans-dmcp` with `spec.input_representation: "cis-1,2-dimethylcyclopentane (both methyls wedges)"`; compiled section `nugget-cyclo-cis-trans` has no corresponding block.
- **Recommended outcome** — The chapter's core same-face/opposite-face distinction is taught in words next to a stereochemistry-free structure; the reader needs cis and trans of the same ring shown side by side in the notation the prose is teaching me to read.

##### `struggle-004` — high · worked-example-gap · confidence 0.9

- **Location** — `section_id`: nugget-substituted; `concept_slug`: substituted-cyclohexanes; `anchor_text`: draw both chairs, count 1,3-diaxial interactions
- **Observation** — All six nuggets are `type: "explain"`; the package contains no worked example of any kind. The chapter states its central procedure in one clause — "draw both chairs, count 1,3-diaxial interactions, and the chair with fewer axial substituents — weighted by their size — is the preferred conformation" — and never carries it out on a single molecule. The graded items ask me to execute exactly this procedure (ch4-chair-tbutyl / -v2 place a substituent, ch4-equatorial-count / -v2 count equatorial methyls, ch4-methylcyclohexane-chair choose the preferred chair).
- **Learner impact** — The step I actually get stuck on is step one, "draw both chairs" — which the chapter never demonstrates and never shows the output of. With no instance to imitate, I cannot self-check my reasoning, so I skip the drawing entirely, answer from the sentence "substituents prefer equatorial", and get every question right for the wrong reason until a question needs two substituents.
- **Evidence** — topic.package.json nuggets[] — all six have `"type": "explain"`; question slugs ch4-chair-tbutyl, ch4-equatorial-count, ch4-methylcyclohexane-chair.
- **Recommended outcome** — Every procedure the chapter grades (build the chair, place a substituent, count 1,3-diaxial contacts, compare the two chairs) is asserted rather than demonstrated; a shaky student needs at least one instance carried out step by step, with the intermediate state visible, before being scored on it.

##### `struggle-005` — high · retrieval-practice · confidence 0.92

- **Location** — `section_id`: nugget-cyclo-nomenclature; `nugget_id`: nugget-chair; `anchor_text`: Why is the chair conformation of cyclohexane strain-free?
- **Observation** — All six nuggets carry an authored `practice_check` (prompt + answer), and none of them compiles into the reader — every compiled section is text + figures + external links, with no checkpoint block of any kind. There is also no summary or callout block anywhere in the chapter. The only practice that exists is the separate question bank (`available: false`, 10 surfaced items), which is not attached to the section that teaches the material.
- **Learner impact** — I read six sections end to end with no point at which I am asked to produce anything, so I never discover that I did not understand section 4 until I meet a scored question about it. Low-confidence students read passively and mistake fluency for comprehension exactly under these conditions; the authored one-sentence checks that would have interrupted that are sitting in the source file, unreachable.
- **Evidence** — topic.package.json `practice_check` on nugget-cyclo-nomenclature, nugget-cyclo-cis-trans, nugget-ring-strain, nugget-chair, nugget-axial-equatorial, nugget-substituted; no `practice_check` reference anywhere in the compiler (grep over backend/app returns none); compiled reader `sections[].blocks[]` contain only text/molecule/reaction_coordinate/video/link blocks.
- **Recommended outcome** — Six authored retrieval checkpoints reach no student surface; the chapter needs a low-stakes self-check between each section and the next, and the authored checks should not be dead content.

##### `struggle-006` — high · retrieval-practice · confidence 0.88

- **Location** — `question_slug`: ch4-conformer-rank; `anchor_text`: The strain-free geometry is lowest; the ring-flip transition geometry is highest.
- **Observation** — Six of the ten surfaced questions expose exactly one hint, and several single hints state the answer outright. ch4-conformer-rank offers three cards (chair, twist-boat, half-chair) and its only hint fixes both endpoints, which fully determines the order. ch4-equatorial-count's only hint is "Draw both chairs; the trans isomer has one chair with no axial methyls" — with two methyls in the molecule, that is the answer (2). ch4-equatorial-count-v2's only hint, "cis means one substituent up and one out — one axial, one equatorial", is the answer (1). ch4-cycloalkane-name's only hint, "The ring is the parent; one substituent requires no number", completes the name.
- **Learner impact** — There is no rung between "stuck" and "told". I open the hint because I am lost, receive the answer, submit it, and record a success I did not earn — so the item's feedback never fires and I leave with the same gap. When the hint does not click, there is nothing after it, so I guess.
- **Evidence** — compiled/question-set.json feedback_bundle.hints — ch4-cycloalkane-name (1 hint), ch4-cycloalkane-name-v2 (1), ch4-ring-strain-most (1), ch4-ring-strain-most-v2 (1), ch4-conformer-rank (1), ch4-conformer-rank-v2 (1), ch4-methylcyclohexane-chair (1), ch4-equatorial-count (1), ch4-equatorial-count-v2 (1).
- **Recommended outcome** — The hint ladders do not ladder: the first rung is frequently the answer and there is no second rung. Struggling students need a first hint that redirects attention (what to look at / what to draw) and a later one that narrows, so the item still measures something after help is taken.

##### `struggle-007` — high · notation-consistency · confidence 0.93

- **Location** — `question_slug`: ch4-ring-flip-multi-v2; `concept_slug`: substituted-cyclohexanes; `anchor_text`: favors the equatorial chair by about 1.8 kcal/mol
- **Observation** — Every energy in the reader prose is in kJ/mol (7.6, 23, 29, 45, 110, 115, 26). Four question feedback strings switch to kcal/mol for the same quantities without conversion: ch4-ring-flip-multi-v2 gives methylcyclohexane's axial penalty as "about 1.8 kcal/mol" where the prose says "7.6 kJ/mol"; ch4-ring-flip-multi says the flip climbs "about 10 kcal/mol uphill" where the prose says the barrier is 45 kJ/mol; ch4-chair-tbutyl says tert-butyl costs "nearly 5 kcal/mol"; ch4-ring-strain-matrix-v2 gives cyclobutane "about 26 kcal/mol" while the reader prose gives cyclobutane "about 110 kJ/mol" and cyclopentane "about 26 kJ/mol".
- **Learner impact** — I cannot tell whether 1.8 and 7.6 are the same fact or two different facts, and no line in the chapter tells me 1 kcal = 4.184 kJ. The 26 collision is worse: the number 26 belongs to cyclopentane in the reading and to cyclobutane in the feedback, so a student building a strain table from both sources writes down a contradiction and concludes the material is inconsistent. At that point I stop trusting the numbers and stop trying to reason quantitatively at all.
- **Evidence** — reader nugget-substituted "The 7.6 kJ/mol axial penalty for methyl"; nugget-ring-strain "cyclobutane still carries about 110 kJ/mol ... whereas cyclopentane's envelope leaves only about 26 kJ/mol"; question feedback strings in ch4-ring-flip-multi, ch4-ring-flip-multi-v2, ch4-chair-tbutyl, ch4-ring-strain-matrix-v2.
- **Recommended outcome** — The chapter and its question bank must express the same quantities in one unit system, or state the conversion where the switch happens, so a student can reconcile the axial penalty and the flip barrier across surfaces.

##### `struggle-008` — high · misconception · confidence 0.9

- **Location** — `question_slug`: ch4-chair-tbutyl; `concept_slug`: substituted-cyclohexanes; `anchor_text`: Axial substituents clash with the two axial hydrogens three carbons away (1,3-diaxial strain)
- **Observation** — The counting rule behind the name "1,3-diaxial" is stated three different ways. The reader prose says the axial methyl "approaches the axial hydrogens on carbons 3 and 5"; ch4-methylcyclohexane-chair's wrong-answer text says "An axial methyl crowds the axial hydrogens two carbons away"; ch4-chair-tbutyl's level-2 hint says "the two axial hydrogens three carbons away". C1 to C3 is two carbons away, so the hint is wrong, and it is the hint attached to the one item that asks me to actually place a group on a chair.
- **Learner impact** — The whole name "1,3-diaxial" is a counting claim, and I am counting, because that is all I can do without a picture (struggle-001). Two contradictory counts told to me by the same chapter mean I cannot self-check; I conclude the numbering is arbitrary, memorize the phrase, and later mis-apply it to 1,4 or 1,2 relationships.
- **Evidence** — reader nugget-substituted "the axial hydrogens on carbons 3 and 5 across the ring — the 1,3-diaxial interaction"; compiled/question-set.json ch4-methylcyclohexane-chair wrong_answer_explanations option_id b; ch4-chair-tbutyl hints level 2.
- **Recommended outcome** — The chapter needs one consistent statement of which axial positions a substituent at C1 interacts with, expressed the same way in prose, hints, and feedback, since the interaction's name is itself the counting rule.

##### `struggle-009` — high · sequencing · confidence 0.87

- **Location** — `question_slug`: ch4-methylcyclohexane-chair; `concept_slug`: axial-equatorial-ring-flip; `section_id`: nugget-axial-equatorial
- **Observation** — ch4-methylcyclohexane-chair ("Which statement describes the preferred chair conformation of methylcyclohexane?") is tagged to `axial-equatorial-ring-flip`, but nothing in section `nugget-axial-equatorial` says which chair is preferred. That section deliberately stops at "the two chairs differ — one places the group axial, the other equatorial — and their equilibrium becomes the central tool". The equatorial preference, the 1,3-diaxial cause, and the 95:5 ratio are all introduced one section later, in `nugget-substituted`. The item's only hint ("Consider which position avoids crowding the axial hydrogens on C3 and C5") likewise presumes the later section.
- **Learner impact** — If I practise after the section the question is tagged to, the answer is genuinely not derivable from what I have read — and options a and b are equally plausible sentences. I guess, and if I guess wrong the feedback teaches me a concept I have not met yet, in vocabulary I have not met yet. Getting a fair question wrong because it was placed before its explanation is exactly what makes a low-confidence student conclude they cannot do the chapter.
- **Evidence** — compiled/question-set.json ch4-methylcyclohexane-chair `concept_slug: "axial-equatorial-ring-flip"`; reader section nugget-axial-equatorial final paragraph; the causal explanation appears only in nugget-substituted.
- **Recommended outcome** — This item's answer depends on the following section; it needs to be attached to the concept that actually teaches the equatorial preference, or the preceding section needs to state the preference it currently withholds.

##### `struggle-010` — high · misconception · confidence 0.9

- **Location** — `question_slug`: ch4-ring-flip-multi; `section_id`: nugget-axial-equatorial; `anchor_text`: Faces are fixed by connectivity: a substituent on the top face stays on the top face through any number of ring flips.
- **Observation** — The single most common wrong model in this topic — that a ring flip moves a substituent from the top face to the bottom face — is named and corrected only inside a wrong-answer explanation for option e of ch4-ring-flip-multi. No sentence in any reader section says that up/down (face) and axial/equatorial (orientation) are independent, or that a flip changes one and preserves the other. Section `nugget-axial-equatorial` describes the flip purely as "positional exchange" and never mentions faces; section `nugget-cyclo-cis-trans` describes faces and never mentions axial/equatorial.
- **Learner impact** — Two vocabularies for 'where the group points' are taught in separate sections and never reconciled, so I merge them: I read "every axial becomes equatorial" as "everything flips over", and I conclude a ring flip converts cis into trans. That single wrong model breaks ch4-equatorial-count, ch4-ring-flip-multi, and everything in `nugget-substituted`. I only find out I hold it after I have already answered a question wrong.
- **Evidence** — compiled/question-set.json ch4-ring-flip-multi wrong_answer_explanations for `$contains: "e"`; reader sections nugget-cyclo-cis-trans and nugget-axial-equatorial contain no cross-reference between faces and axial/equatorial.
- **Recommended outcome** — The chapter's highest-frequency misconception is corrected only after a student has already committed to it in a scored item; the distinction between a fixed face and an interchangeable axial/equatorial orientation needs to be made explicit where the ring flip is taught.

##### `struggle-014` — high · worked-example-gap · confidence 0.89

- **Location** — `question_slug`: ch4-equatorial-count-v2; `concept_slug`: substituted-cyclohexanes; `anchor_text`: For adjacent carbons, cis means one substituent up and one out — one axial, one equatorial.
- **Observation** — Two graded items require translating a cis/trans configuration into an axial/equatorial pattern on a chair, and the chapter only states the results: "the trans isomer offers a chair with both methyls equatorial ... while the cis isomer must hold one methyl axial in either chair". The derivation is never shown. The one hint that attempts it, on ch4-equatorial-count-v2, is phrased "cis means one substituent up and one out", which mixes the face vocabulary (up) with the orientation vocabulary (out) in a single clause — the exact conflation named in struggle-010.
- **Learner impact** — I am asked for a number I can only get by drawing a chair I have never seen drawn (struggle-001) and applying a rule the chapter asserts but never derives. So I memorize "trans = 2, cis = 1" as a fact about 1,2-dimethylcyclohexane, which fails immediately on any 1,3- or 1,4-disubstituted ring, and the hint's wording actively reinforces the up/down-equals-axial/equatorial confusion.
- **Evidence** — compiled/question-set.json ch4-equatorial-count and ch4-equatorial-count-v2 (`answer_key.value` 2.0 and 1.0); reader nugget-substituted paragraph 2.
- **Recommended outcome** — The cis/trans-to-axial/equatorial mapping is the chapter's terminal skill and is delivered as a memorizable result rather than a reconstructible procedure; a struggling student needs to see the translation performed once on a specific ring, in vocabulary that keeps face and orientation distinct.

##### `struggle-011` — medium · cognitive-load · confidence 0.85

- **Location** — `section_id`: nugget-chair; `nugget_id`: nugget-chair; `anchor_text`: The boat, about 29 kJ/mol up, adds a direct cross-ring interaction between the two 'flagpole' hydrogens.
- **Observation** — The second paragraph of `nugget-chair` introduces four new named geometries (twist-boat, boat, half-chair, plus 'flagpole' hydrogens as a new structural term), three energy values, and the concept of a transition geometry, in four sentences — with no figure of any of the four geometries and a non-rendering energy profile beside it (struggle-002).
- **Learner impact** — By the third sentence I am holding four unlabelled shapes and three numbers with nothing to attach them to. This is where I stop reading for meaning and start highlighting numbers, which is how I arrive at ch4-conformer-rank able to recall that 23 and 45 exist but not which shape owns which.
- **Evidence** — reader block blk-s4l76ims paragraph 2 (identical in `_detail_texts.expanded`).
- **Recommended outcome** — The conformer inventory arrives faster than a shaky reader can build referents for it; the section needs the four geometries introduced with something to attach each name to, or the non-chair geometries deferred until the chair itself is secure.

##### `struggle-012` — medium · cognitive-load · confidence 0.86

- **Location** — `section_id`: nugget-substituted; `anchor_text`: a steric strain identical in origin to the gauche interaction of butane
- **Observation** — Four terms are used at default reading depth without being defined anywhere in the chapter: "the gauche interaction of butane" (the declared prerequisite is `ethane-conformations`, not butane conformers), "steric strain" (the chapter defines angle strain and torsional strain but never this third kind), "Newman projection" ("a Newman projection along any C–C bond shows perfect staggering" — used as evidence for the chapter's key claim, with no Newman figure in the package), and "flagpole" hydrogens.
- **Learner impact** — The gauche comparison is offered as the thing that will make 1,3-diaxial strain make sense, and it is the sentence I understand least, so the explanation lands as a second unknown rather than an anchor. The Newman sentence is worse: it is the proof that the chair is torsion-free, and I cannot evaluate it, so I take 'the chair is strain-free' on authority and have no way to reconstruct it later.
- **Evidence** — reader nugget-substituted "identical in origin to the gauche interaction of butane"; nugget-chair "a Newman projection along any C–C bond shows perfect staggering"; concepts[].prerequisites list `ethane-conformations`, `sp3-hybridization`, `alkane-nomenclature`, `alkanes-and-isomers` only.
- **Recommended outcome** — Terms carried in from earlier chapters are used as load-bearing explanations without a local reminder of what they mean; a struggling reader needs each one either restated in a clause or linked to where it was taught.

##### `struggle-013` — medium · conceptual-support · confidence 0.84

- **Location** — `section_id`: nugget-axial-equatorial; `nugget_id`: nugget-axial-equatorial; `anchor_text`: Each chair carbon carries one axial (vertical) and one equatorial (outward) hydrogen
- **Observation** — The plain-language gloss of the two most important new words in the chapter exists only in the `terse` tier, which no default reader sees. The `terse` text says "one axial (vertical) and one equatorial (outward)"; the default `expanded` tier renders axial as "parallel to the ring axis" and equatorial as "extend outward from the ring's equator, angled only slightly up or down" — geometric descriptions that presuppose I can already see the ring axis and the ring's equator, neither of which is drawn (struggle-001). Everything else about the chapter's tier authoring is sound: `expanded` is a genuine superset of `standard` in all six nuggets.
- **Learner impact** — The one-word handle — axial means straight up and down — is the thing I would repeat to myself while solving problems, and I never receive it. Instead I get 'ring axis' and 'ring equator', two more objects to visualize, so I decode the definition instead of using it, and I mix the two words up under time pressure.
- **Evidence** — topic.package.json nugget-axial-equatorial `text.terse` versus `text.expanded`; [internal source reference — not in this repo].
- **Recommended outcome** — The default-depth text defines axial and equatorial only in terms of geometry a student cannot see; the plain-language gloss that currently exists only at the shortest tier needs to survive at the depth students actually read.

##### `struggle-015` — medium · cognitive-load · confidence 0.87

- **Location** — `question_slug`: ch4-name-structure-match; `anchor_text`: Three rendered cycloalkane structures of different ring sizes and substitution
- **Observation** — Five surfaced/staged items author `structure_smiles` on their options (ch4-name-structure-match, ch4-name-structure-match-v2, ch4-ring-strain-most, ch4-ring-strain-most-v2, ch4-ring-strain-matrix / -v2), and none of those renderers reads the field: MatchingRenderer, CategorizeRenderer, SelectedResponseRenderer and ComparisonMatrixRenderer all read only `imageUrl`. The structures render for nobody, and the accessible descriptions promise structures that are not there ("Three rendered cycloalkane structures ...").
- **Learner impact** — The matching item degrades to matching a verbal description of a ring ("A five-membered ring bearing one CH₃") to a name ("Methylcyclopentane") — which is a vocabulary lookup, not the counting-the-ring-atoms skill the feedback says it is testing. For a student like me, who is trying to build the link between a drawn polygon and a name, the one item designed to practise that link never shows a polygon.
- **Evidence** — [internal source reference — not in this repo] lines 41-43 and 82-83, [internal source reference — not in this repo] lines 41-43, [internal source reference — not in this repo] line 169, [internal source reference — not in this repo] lines 28/108 — all key off `imageUrl`; compiled/question-set.json student_config uses `structure_smiles`.
- **Recommended outcome** — Items authored around structures are being answered from text; the structure-to-name practice these questions are supposed to provide needs the structure actually visible to the student.

##### `struggle-016` — medium · conceptual-support · confidence 0.82

- **Location** — `section_id`: nugget-substituted; `anchor_text`: Background reading on Substituted cyclohexanes. Opens on Wikipedia.
- **Observation** — Nothing in the chapter signals what matters most. There is no summary block, no callout, no objectives shown to the student (the six `learning_objectives` in the package do not compile), and no visual weighting — a 3-paragraph section on nomenclature and a 3-paragraph section on the chair look identical. The only navigational furniture is one Wikipedia link per section, and three of the six point at the identical URL (en.wikipedia.org/wiki/Cyclohexane_conformation) under three different titles, while the single McMurry link goes to the chapter opener (`4-why-this-chapter`) rather than to any specific section.
- **Learner impact** — With everything weighted equally I allocate my study time by paragraph length rather than by importance, so I over-invest in naming rules (which I can already do) and under-invest in the chair (which I cannot). When I click 'Background reading on Substituted cyclohexanes' hoping for help with the part I failed, I land on the same page I already got from 'The chair conformation of cyclohexane', which reads as the chapter having nothing more to offer me.
- **Evidence** — compiled blocks blk-d3rjoeo0, blk-2fhtzerv, blk-8dshura1 all `"url": "https://en.wikipedia.org/wiki/Cyclohexane_conformation"`; blk-9my34ayv `"url": ".../4-why-this-chapter"`; topic.package.json `learning_objectives` appear on every nugget and in no compiled block.
- **Recommended outcome** — The chapter gives a struggling reader no priority signal and no differentiated place to go when stuck; it needs an explicit statement of what the section is for and what to be able to do afterwards, and further-reading targets that differ from each other.

##### `struggle-017` — medium · misconception · confidence 0.88

- **Location** — `section_id`: nugget-ring-strain; `nugget_id`: nugget-ring-strain; `anchor_text`: each trades a little angle strain for relief of torsional strain, leaving moderate net strain.
- **Observation** — The compiled reader and the topic package disagree. The reader's `expanded` text contains a correction the source of truth does not: "The trade is not equally good: cyclobutane still carries about 110 kJ/mol of total strain, nearly as much as cyclopropane, whereas cyclopentane's envelope leaves only about 26 kJ/mol." topic.package.json still ends that paragraph with "leaving moderate net strain", and the `terse` and `standard` tiers were never updated at all. A recompile from source would silently delete the corrected sentence.
- **Learner impact** — "Cyclobutane and cyclopentane pucker to relieve part of their strain ... leaving moderate net strain" leaves me with exactly the misconception the concept itself declares as its trouble spot ("Assuming all rings are strained equally"): that puckering roughly solves the problem for both. A student on the `standard` tier still reads that today, and every reader will read it again after the next recompile. It also collides with ch4-ring-strain-matrix-v2, which insists cyclobutane's strain is 'higher'.
- **Evidence** — diff of `topic.package.json` nuggets[2].text.expanded against the compiled `_detail_texts.expanded` in section nugget-ring-strain; topic.package.json concepts[2].trouble_spots "Assuming all rings are strained equally".
- **Recommended outcome** — The corrected cyclobutane statement lives only in a build artifact; the source text and all three tiers need to carry the same correction so the trouble spot the concept declares is actually addressed and stays addressed.

##### `struggle-019` — medium · conceptual-support · confidence 0.86

- **Location** — `section_id`: nugget-substituted; `asset_id`: mol-dimethylcyclohexane; `anchor_text`: Line structure of 1,2-dimethylcyclohexane, a cyclohexane ring with methyl groups on two adjacent carbons.
- **Observation** — The section whose entire second paragraph contrasts cis-1,2-dimethylcyclohexane with trans-1,2-dimethylcyclohexane illustrates itself with one flat, stereochemistry-free drawing (`CC1CCCCC1C`) whose alt text does not mention cis or trans at all. There is no figure in the chapter in which the trans isomer's both-equatorial chair or the cis isomer's one-axial chair can be seen.
- **Learner impact** — The picture beside the paragraph shows one compound, so I read the paragraph as being about one compound and lose the distinction that the paragraph exists to make. When ch4-equatorial-count then asks about trans and ch4-equatorial-count-v2 about cis, I do not register them as different molecules and answer both with the same number.
- **Evidence** — compiled block blk-8uoppt3t; reader nugget-substituted paragraph 2; topic.package.json asset `mol-dimethylcyclohexane`.
- **Recommended outcome** — The compound the section's key comparison is built on is shown in a form that cannot express the comparison; the cis and trans cases need to be distinguishable where the contrast is made.

##### `struggle-020` — medium · missing-example · confidence 0.83

- **Location** — `question_slug`: ch4-chair-tbutyl; `concept_slug`: substituted-cyclohexanes; `anchor_text`: becomes prohibitive for a tert-butyl group, which locks its ring in the equatorial chair
- **Observation** — The graded item asks me to place `C(CH3)3` on a chair. tert-Butyl is named exactly once in the chapter, in a subordinate clause, and is never drawn or expanded; isopropyl (`CH(CH3)2`, the -v2 substituent) never appears in the chapter at all. The chapter also gives no size ordering beyond methyl 7.6 kJ/mol and 'prohibitive' for tert-butyl, so 'weighted by their size' in the general procedure has no worked scale behind it.
- **Learner impact** — I have to decode `C(CH3)3` into a shape before I can reason about whether it is bulky, and the chapter never showed me one. I answer 'equatorial' because that is the answer to every question in this section, which is the correct answer arrived at without using the reasoning the item is designed to test — and I would answer identically for a fluorine, which is where that habit breaks.
- **Evidence** — compiled/question-set.json ch4-chair-tbutyl `student_config.substituent: "C(CH3)3"` and ch4-chair-tbutyl-v2 `"CH(CH3)2"`; reader nugget-substituted paragraph 1 is the only mention of tert-butyl; no occurrence of isopropyl anywhere in the package.
- **Recommended outcome** — The chapter grades substituent bulk while showing only methyl; students need at least one larger substituent made concrete, and enough of a size scale that 'weighted by their size' is usable rather than a phrase.

**Open questions**

- Is `stereo-cis-trans-dmcp` dropped from the reader deliberately (the compiler appears to emit no block type for `stereochemistry_conversion`) or is this a compile bug? The same asset kind was reported missing from the reader in ch25.
- Are the 10 surfaced questions reachable by a student reading this chapter at all, given `publishing.available: false` and the separate `ChapterHomeworkPanel` gating? If they are not, findings struggle-006, -009, -018 describe latent rather than live harm.
- The `reaction_coordinate` blocks compile without a `spec` — is the compiler expected to translate a `conformational_energy_profile` asset into the reader's reaction-coordinate spec shape (steps + minima_labels), or is `conformational_energy_profile` simply unsupported in the reader today?
- Should `practice_check` ever reach the reader? Six items here are unreachable, and the same gap has now been reported for ch27, ch30 and ch31 — this looks platform-wide rather than chapter-specific.
- No new `category` ids were coined; all findings use ids listed in finding-schema.md.

#### Accessibility Persona — 6.8/10

_persona_version 1.0.0 · publication_blockers: none_

This is an unusually text-robust chapter and, on the two hardest access questions, it passes: every one of the nine question types it uses has a keyboard-complete, select- or button-based response path (including the chair workspace and the rank-order cards), and every stimulus is authored as text — so when the platform silently ignores the authored structure_smiles on matching, select, and comparison-matrix items, no item becomes unanswerable. No accessible_description in the bank leaks its answer. Where it fails is at the figure layer and the hint layer. Not one of the nine assets carries an accessibility.long_description, although the compiler passes that field through and the reader renders it; every figure therefore delivers a shape-naming alt text ('a hexagon of six carbon atoms') and nothing about the chemistry the figure exists to teach. The one asset that distinguishes cis from trans (stereo-cis-trans-dmcp, type stereochemistry_conversion) is silently dropped by the reader compiler and reaches no learner at all, leaving a section whose only figure is a flat, stereochemistry-free pentagon whose alt text nonetheless asserts that 'cis and trans configurations exist'. The ring-flip energy profile does not render either (a conformational profile carries no steps/minima_labels, so no spec is inlined), which makes its alt text the sole representation for every learner — and that alt text mis-describes the boat region as a 'plateau' when the boat is a local maximum. Nowhere in the chapter — figure, long description, or prose — is the chair's positional structure written down (which carbons pucker, the axial up/down alternation, the 1,3-diaxial partner set, or the rule that maps ring faces onto axial/equatorial on adjacent carbons), so the three sections and six questions that depend on that spatial model rest on assertions a non-visual learner can only memorise. Finally, seven level-1 hints state the answer outright, and the existing answer-leak guard inspects only accessible_description, so nothing catches them. No required activity is impossible for any learner here, so I raise no publication blocker; the barriers are to learning, not to answering.

**Strengths**

- Every question type this chapter uses has a genuine non-pointer response path, and I verified each one in the renderer rather than trusting the registry: rank_order is Move up / Move down IconButtons with position-announcing labels (MechanismCardSortRenderer), categorize_groups and matching_pairs are one labelled Select per item, and the chair workspace offers a ring-position/orientation select table beside the clickable diagram. There is no drag-only or pointer-only entry anywhere in the chapter.
- Not one accessible_description in the 20-question bank leaks its answer — including the two chair items, whose descriptions say 'in its most stable orientation' and carefully avoid the word equatorial, and ch4-cis-trans-sort, which says 'sort each into one of two stereochemical categories based on ring faces' without naming cis or trans.
- The chapter authored its stimuli as text: every matching left item, every categorize item, and every select option carries a verbal description, so the platform's silent dropping of structure_smiles across three renderers leaves no item unanswerable. The two short_answer prompts even gloss their SMILES inline ('SMILES CC1CCCCC1 (a cyclohexane ring bearing one methyl group)').
- The `expanded` tier — the reader's default detail level — is a true superset of `standard` in all six nuggets, so no definition or number is lost to a learner reading at the default setting.
- ComparisonMatrixRenderer delivers the two matrix items as a real table with `scope="col"` and `scope="row"` headers and a per-cell aria-label of the form '<feature> for <case>', which is a well-formed non-visual equivalent for a comparison grid.
- The reader prints each figure's description visibly as 'Described as: …', so the alt text is shared with sighted readers rather than hidden in an attribute — the right pattern, currently let down only by how thin the descriptions are.

**Findings**

##### `access-001` — high · media-equivalence · confidence 0.9

- **Location** — `nugget_id`: nugget-axial-equatorial; `section_id`: axial-equatorial-ring-flip; `concept_slug`: axial-equatorial-ring-flip; `asset_id`: mol-methylcyclohexane; `anchor_text`: Six axial bonds stand parallel to the ring axis, alternating up and down on successive carbons.
- **Observation** — The chapter's spatial core — the chair's positional structure — exists nowhere as structured, non-visual content. The compiled reader carries no chair figure at all: the only figures in nugget-chair and nugget-axial-equatorial are flat hexagon line structures of cyclohexane (C1CCCCC1) and methylcyclohexane (CC1CCCCC1), whose alt texts read 'a hexagon of six carbon atoms' and 'a cyclohexane ring bearing one methyl group'. The prose states the axial/equatorial families in general terms but never fixes them to positions: it does not say which carbons pucker above and below the four-carbon plane, that axial bonds point up on C1/C3/C5 and down on C2/C4/C6, that a carbon's equatorial bond points roughly opposite its axial one, or which three carbons form the 1,3-diaxial set for a given position.
- **Learner impact** — A learner who cannot see figures — and equally a learner who could see one if it existed — has no positional model to reason on. A sighted student compensates by sketching a chair and reading positions off the drawing; that route is unavailable without vision, and the chapter supplies no textual substitute. Everything the last three sections assert (the 1,3-diaxial penalty, the equatorial preference, the trans-1,2 double-equatorial chair) becomes a fact to memorise rather than a geometry to reason from.
- **Evidence** — Reader blocks blk-d69hlje0, blk-4n97fgbg, blk-1fipmwum are all `molecule` blocks of flat rings; no asset in `assets[]` has `type` chair or any `accessibility.long_description`. Package prose: 'Six axial bonds stand parallel to the ring axis, alternating up and down on successive carbons. Six equatorial bonds extend outward from the ring's equator' (nugget-axial-equatorial, expanded).
- **Recommended outcome** — The chair's positional structure needs to exist in a form a non-visual learner can hold and reason on: per-carbon axial/equatorial assignment, the up/down alternation, and the 1,3-diaxial partner set stated explicitly rather than left to be read off a drawing that is never drawn.

##### `access-002` — high · media-equivalence · confidence 0.86

- **Location** — `question_slug`: ch4-equatorial-count-v2; `nugget_id`: nugget-substituted; `concept_slug`: substituted-cyclohexanes; `anchor_text`: while the cis isomer must hold one methyl axial in either chair
- **Observation** — The rule that connects the chapter's face vocabulary (cis/trans) to its chair vocabulary (axial/equatorial) is never stated in any nugget. nugget-substituted asserts the two 1,2-dimethylcyclohexane outcomes as results ('the trans isomer offers a chair with both methyls equatorial ... while the cis isomer must hold one methyl axial in either chair') without giving the generalisable relationship — that on adjacent ring carbons a cis pair is necessarily one axial plus one equatorial and a trans pair is either both equatorial or both axial. The only place that rule appears in the entire package is inside a hint of ch4-equatorial-count-v2: 'For adjacent carbons, cis means one substituent up and one out — one axial, one equatorial.'
- **Learner impact** — Both ch4-equatorial-count and ch4-equatorial-count-v2 ask the learner to count equatorial methyls for a named cis or trans isomer. A sighted learner substitutes for the missing rule by drawing two chairs and counting. A non-visual learner has neither the drawing route nor the rule, and can reach the answer only by recalling the two specific sentences the chapter happens to assert — and cannot transfer to a 1,3- or 1,4-disubstituted ring at all, which is exactly what the chapter says it is preparing them for ('This reasoning underlies the conformational analysis of sugars and steroids in later chapters').
- **Evidence** — nugget-substituted `text.expanded` contains no face-to-orientation rule; `question_sets` ch4-equatorial-count-v2 `feedback_bundle.hints[0].text` is the sole statement of it.
- **Recommended outcome** — The face-to-orientation mapping for adjacent (and ideally 1,3-) substituent pairs needs to be available as taught text on the reading surface, not only inside a hint on one question, so the counting items can be reasoned through rather than recalled or drawn.

##### `access-003` — high · alt-text-quality · confidence 0.94

- **Location** — `asset_id`: mol-dimethylcyclohexane; `nugget_id`: nugget-substituted; `concept_slug`: substituted-cyclohexanes; `anchor_text`: Line structure of 1,2-dimethylcyclohexane, a cyclohexane ring with methyl groups on two adjacent carbons.
- **Observation** — None of the chapter's nine assets carries `accessibility.long_description` — the field is absent from every entry in `assets[]`. The compiler explicitly forwards it (reader_chapter_builder._asset_block copies `accessibility.long_description` onto block content) and the reader renders it (StructureCard's `longDescription` prop), so the omission is authorial, not a platform gap. What each figure delivers instead is a shape-naming alt text: 'a triangle of three carbon atoms', 'a square of four carbon atoms', 'a pentagon of five carbon atoms', 'a hexagon of six carbon atoms'. mol-dimethylcyclohexane exists to support the axial/equatorial counting analysis and its description says only that two methyls sit on adjacent carbons.
- **Learner impact** — Every figure in the chapter reduces, for a screen-reader user, to a polygon count they could already infer from the compound's name — which means the figures contribute nothing to their learning. Because the alt text is also printed visibly ('Described as: …'), the same impoverished description is what a low-vision or reading-support user gets as the caption.
- **Evidence** — All nine entries in `assets[]` have `accessibility` objects containing only `alt_text`. ReaderBlockRenderer StructureCard renders `longDescription` when present; reader_chapter_builder copies it with the comment 'Dropping it here left every downstream surface ... with alt text only.'
- **Recommended outcome** — Each figure needs a description that carries the chemistry it was placed there to teach — bond angles and the eclipsing state for the strained rings, substituent positions and orientations for the substituted cyclohexanes — rather than a restatement of the ring size.

##### `access-004` — high · media-equivalence · confidence 0.95

- **Location** — `asset_id`: stereo-cis-trans-dmcp; `nugget_id`: nugget-cyclo-cis-trans; `section_id`: cycloalkane-cis-trans; `concept_slug`: cycloalkane-cis-trans
- **Observation** — stereo-cis-trans-dmcp (`type: stereochemistry_conversion`) reaches no rendering surface. The reader compiler's `_ASSET_TYPE_TO_BLOCK` map has no entry for `stereochemistry_conversion`, so `_asset_block()` returns None and the asset is silently dropped — it appears nowhere in the compiled reader chapter's blocks. Its authored alt text ('Side-by-side wedge-and-dash drawings of cis-1,2-dimethylcyclopentane, with both methyl groups on the same face, and trans-…, with the methyl groups on opposite faces') therefore reaches no learner either. The section is left with a single figure, mol-dimethylcyclopentane, drawn from stereochemistry-free SMILES (CC1CCCC1C) — yet its alt text asserts 'cis and trans configurations exist', a distinction the render does not and cannot carry.
- **Learner impact** — The chapter's only figure-level contrast between cis and trans is invisible to everyone, and the description attached to the surviving figure tells a screen-reader user that stereochemistry is depicted when it is not. A learner who trusts the description and asks what the drawing shows about the faces gets nothing back. The wedge-and-dash convention the prose leans on ('a cis pair appears as two wedges (or two dashes) and a trans pair as one of each') has no accompanying instance in any modality.
- **Evidence** — [internal source reference — not in this repo] lists molecule/reaction/reaction_coordinate/conformational_energy_profile/acid_base_energy_diagram/newman_projection/synthesis_roadmap/orbital_overlay/protein_structure/clipart/diagram/titration_curve/enzyme_active_site — no stereochemistry_conversion. Compiled reader section `nugget-cyclo-cis-trans` contains blocks blk-0w6d2uke (text), blk-9fqhikri (molecule), blk-8y66h1ey (external_link) only.
- **Recommended outcome** — The cis/trans face distinction needs a representation that actually reaches the learner on the reading surface, and the surviving flat-structure description must stop asserting a stereochemical distinction the render does not carry.

##### `access-005` — high · alt-text-quality · confidence 0.9

- **Location** — `asset_id`: cep-cyclohexane-flip; `nugget_id`: nugget-chair; `section_id`: cyclohexane-chair; `anchor_text`: chairs at the two minima, half-chair maxima between them, and a twist-boat/boat plateau in the middle
- **Observation** — cep-cyclohexane-flip compiles to a `reaction_coordinate` block (blocks blk-4cmtjx9y and blk-ciysf6cq) with no `spec`: the compiler inlines a spec only when it contains both `steps` and `minima_labels`, and a conformational profile has neither. ReactionCoordinateCard therefore sets `failed` and renders the alt text in place of any diagram, then repeats it verbatim in the 'Described as:' caption. That alt text is consequently the entire figure, for every learner, and it mis-describes the profile: it calls the middle region 'a twist-boat/boat plateau', but the asset's own conformer list and caveat place the boat (≈29 kJ/mol) above the twist-boats (≈23 kJ/mol), i.e. a local maximum between two shallow minima, not a plateau. The energies themselves live in `spec.scientific_caveats`, which the compiler never forwards, so no number reaches any surface from the figure. The block is also badged 'Reaction-coordinate diagram' for a conformational interconversion.
- **Learner impact** — The only non-visual (and here, the only) representation of the chapter's one energy figure states the wrong shape for the boat region and omits every energy value. A learner building a mental energy ladder from this description will place boat and twist-boat at the same height — which is precisely the discrimination ch4-conformer-rank-v2 asks them to make.
- **Evidence** — reader_chapter_builder: `if isinstance(spec, dict) and "steps" in spec and "minima_labels" in spec:` — cep-cyclohexane-flip's spec has `coordinate`/`scan_smiles`/`conformers`, so no spec is inlined. Asset caveat: 'chair (0) < twist-boat (≈23 kJ/mol) < boat (≈29 kJ/mol) < half-chair (≈45 kJ/mol)'.
- **Recommended outcome** — The ring-flip profile needs a textual equivalent that states the actual ordering and the energy values, since no diagram renders; and the description must match the profile's real shape (boat as a maximum between twist-boat minima) rather than flattening it.

##### `access-006` — high · assessment-readiness · confidence 0.88

- **Location** — `question_slug`: ch4-chair-tbutyl; `concept_slug`: substituted-cyclohexanes; `anchor_text`: A cyclohexane chair drawing with a selectable substituent orientation on each ring carbon
- **Observation** — Seven of the ten surfaced items (and their variants) give the answer away at hint level 1. ch4-chair-tbutyl: 'Bulky groups avoid the orientation that points parallel to the ring axis' — the chapter defines axial as 'parallel to the ring axis', so the hint names the wrong answer by definition, leaving equatorial. ch4-chair-tbutyl-v2: 'Bulky groups avoid 1,3-diaxial strain.' ch4-equatorial-count: 'Draw both chairs; the trans isomer has one chair with no axial methyls' — no axial methyls means both equatorial, the answer 2. ch4-equatorial-count-v2: 'For adjacent carbons, cis means one substituent up and one out — one axial, one equatorial' — the answer 1. ch4-conformer-rank: 'The strain-free geometry is lowest; the ring-flip transition geometry is highest' — with three cards, fixing first and last fixes the whole order. ch4-methylcyclohexane-chair: 'Consider which position avoids crowding the axial hydrogens on C3 and C5.' ch4-cis-trans-sort level 2: '"Both up" and "same face" describe the same geometry.' The existing answer-leak guard (find_accessibility_leaks) inspects only `accessible_description`, so none of these is caught.
- **Learner impact** — Hints are the scaffold a learner reaches for when the figure channel is unavailable to them — which in this chapter is every learner without vision, since no chair is ever drawn. Handing them the answer at the first rung removes the only graduated support they have and converts the item into a recall check they cannot learn from. It also silently inflates their score relative to their understanding.
- **Evidence** — feedback_bundle.hints in ch4-chair-tbutyl, ch4-chair-tbutyl-v2, ch4-equatorial-count, ch4-equatorial-count-v2, ch4-conformer-rank, ch4-methylcyclohexane-chair, ch4-cis-trans-sort. Guard scope: [internal source reference — not in this repo] only.
- **Recommended outcome** — The level-1 hints on these items need to point at the reasoning step (what to compare, which interaction to count) without naming or uniquely determining the graded answer, so a learner who depends on hints still has to do the chemistry.

##### `access-007` — medium · media-equivalence · confidence 0.92

- **Location** — `question_slug`: ch4-cycloalkane-name; `anchor_text`: Type the IUPAC name of a cyclohexane ring bearing a single methyl group.
- **Observation** — All 20 questions author an `accessibility_bundle.accessible_description`, and none of it reaches a learner. Across the frontend only ReactionCoordinateQuestionRenderer reads `accessibilityBundle.accessible_description` (MolecularGeometryRenderer uses its own catalog field); none of this chapter's nine question types — short_answer, single_select, multi_select, matching_pairs, categorize_groups, comparison_matrix, rank_order, numeric_with_units, chair — consumes it. The field is dead metadata for the whole bank.
- **Learner impact** — A screen-reader user gets `prompt_text` plus whatever the renderer's own aria-labels supply, and nothing the author wrote as their non-visual equivalent. This chapter survives it because its prompts are self-describing (SMILES are glossed inline, every option and matching item is verbal), so no item is unanswerable — but the safety margin is accidental, and any future item that leans on a rendered stimulus would have no fallback at all.
- **Evidence** — grep across frontend/src for `accessibilityBundle` returns only [internal source reference — not in this repo] as a consumer; all 20 entries in `question_sets[]` carry `accessibility_bundle.accessible_description`.
- **Recommended outcome** — The authored non-visual description needs to actually reach the learner on the question surfaces this chapter uses, or the authoring pipeline needs to stop treating a field no renderer reads as the accessibility deliverable.

##### `access-008` — medium · assessment-readiness · confidence 0.85

- **Location** — `question_slug`: ch4-chair-tbutyl-v2; `concept_slug`: substituted-cyclohexanes; `anchor_text`: Place the isopropyl group on the cyclohexane chair in its most stable orientation.
- **Observation** — Both chair items grade to `equatorial`, and ChairPlacementRenderer's Orientation select is pre-set to that value: `value={current?.orientation ?? "equatorial"}` with Equatorial as the first option. The non-pointer path — the select table that the type's registry declares as its `ring_position_table` nonvisual response mode — therefore opens with the correct answer already chosen; picking any ring position and submitting scores correct without the learner ever touching the graded field. Separately, the grader accepts any ring position (`allow_ring_rotation` defaults to True in ChairGrader), but neither the prompt nor the workspace says so, and the position select opens on an empty 'Choose…' that must be filled before an answer is emitted at all.
- **Learner impact** — For a keyboard or screen-reader user working down the form, the item reads as 'choose a ring position, orientation already set' — the assessment measures nothing, and the learner gets no signal about whether they understood the equatorial preference. The unexplained ring-position requirement adds a decision that carries no chemistry: a learner using the table has no basis for preferring C1 over C4 and may reasonably think the choice is being graded.
- **Evidence** — [internal source reference — not in this repo] lines 288-301 (orientation Select default) and 219-220 (`complete = next.position >= 1 && next.position <= 6`); [internal source reference — not in this repo]. Both items' answer keys specify `orientation: "equatorial"`.
- **Recommended outcome** — The chair items need a response path whose default state is not the graded answer, and the learner needs to be told that any ring position is acceptable so the position choice does not read as part of what is being assessed.

##### `access-009` — medium · keyboard-operability · confidence 0.78

- **Location** — `question_slug`: ch4-chair-tbutyl; `anchor_text`: Click a bond position on the chair to place
- **Observation** — ChairPlacementRenderer emits twelve absolutely-positioned buttons ('C1 axial' … 'C6 equatorial') with `bg="transparent"` and `borderColor="transparent"` when unplaced, and they sit in the tab order ahead of both the explanatory text ('Click a bond position on the chair to place … Or use the table below') and the select table that is the declared nonvisual response mode. The chair SVG itself is `role="img"` with the aria-label 'Cyclohexane chair with clickable axial and equatorial positions on carbons one through six' — it names the picture without describing any of its geometry.
- **Learner impact** — A keyboard or screen-reader user must traverse twelve invisible controls, announced only as position/orientation pairs and preceded by no explanation of what they do, before reaching the two selects that are the intended accessible path. There is no skip. Sighted mouse users see nothing at those coordinates until focus lands, so the controls are discoverable only by tabbing — which makes the friction fall entirely on the keyboard user.
- **Evidence** — [internal source reference — not in this repo] lines 160-193 (the twelve `as="button"` boxes) render before the instruction Text (line 248) and the label selects (line 257 onward); SVG aria-label at line 110.
- **Recommended outcome** — The keyboard route needs to reach the accessible response path first, or the twelve positional targets need to be skippable, and the chair graphic needs a description of its structure rather than a name.

##### `access-010` — medium · color-motion-only · confidence 0.82

- **Location** — `asset_id`: video-ring-flip; `nugget_id`: nugget-axial-equatorial; `anchor_text`: Fold a planar hexagon into the chair and mark the axial and equatorial hydrogens in two colors.
- **Observation** — The video brief makes colour the sole carrier of the axial/equatorial distinction ('mark the axial and equatorial hydrogens in two colors', then 'show every axial label now equatorial'), and plans no captions, transcript, or audio description. The `narration_outline` is three conceptual beats ('Explain why the chair is strain-free', 'Follow the energy profile across the 45 kJ/mol half-chair barrier', 'Conclude that the flip interchanges axial and equatorial positions') — it never describes the visual changes the storyboard depends on, so narration alone would not convey which positions moved. There is also no plan for pausing, stepping, or a static-sequence equivalent. The video is unproduced and both compiled video blocks carry `url: ""` with `is_hidden: true` (which ReaderBlockRenderer honours), so no learner is affected today.
- **Learner impact** — As briefed, the finished animation would carry its central teaching point — that every axial position becomes equatorial — in colour and motion only, with narration that talks over the change rather than describing it. Learners with colour-vision differences, low vision, or no vision, and learners who need to step through rather than watch, would get the chapter's one dynamic explanation of the ring flip and take nothing from it.
- **Evidence** — video_briefs[0] `storyboard` and `narration_outline`; compiled blocks blk-chgbfhfg and blk-9o04cps5 (`url: ""`, `is_hidden: true`); [internal source reference — not in this repo].
- **Recommended outcome** — Before this video is produced, the axial/equatorial distinction needs a carrier other than colour, the narration needs to describe the geometric changes as they happen, and the flip needs a steppable or static-sequence equivalent for learners who cannot use the animation.

##### `access-011` — low · alt-text-quality · confidence 0.88

- **Location** — `question_slug`: ch4-name-structure-match; `anchor_text`: Three rendered cycloalkane structures of different ring sizes and substitution; pair each with its IUPAC name.
- **Observation** — The two matching_pairs items describe a stimulus that does not exist. MatchingRenderer reads only `imageUrl` from each entry (`readEntries` in [internal source reference — not in this repo]), never the authored `structure_smiles`, so the three structures in ch4-name-structure-match and ch4-name-structure-match-v2 render for nobody — yet both accessible_descriptions open 'Three rendered cycloalkane structures of different ring sizes and substitution'. The same silent drop applies to the `structure_smiles` on ch4-ring-strain-most / -v2 options (SelectedResponseRenderer reads `imageUrl` only) and on the ch4-ring-strain-matrix / -v2 cases (ComparisonMatrixRenderer likewise).
- **Learner impact** — Low in practice, because every left item, option, and case also carries a verbal text label ('A five-membered ring bearing one CH₃'), so the items remain fully answerable. The cost is a description that promises a figure the learner will then hunt for and not find — and, were the description ever surfaced, it would misdescribe the page.
- **Evidence** — [internal source reference — not in this repo] returns `{id, text, imageUrl}`; [internal source reference — not in this repo]; [internal source reference — not in this repo]. Six questions in this bank supply `structure_smiles`.
- **Recommended outcome** — Descriptions must match what the learner will actually encounter: either the structures need to reach the renderer, or the descriptions need to stop asserting rendered figures.

##### `access-012` — low · keyboard-operability · confidence 0.8

- **Location** — `section_id`: cyclohexane-chair; `nugget_id`: nugget-chair; `anchor_text`: The strain-free chair
- **Observation** — Heading levels skip a rank throughout the reader chapter: TopicPackageChapterRenderer emits the chapter title as `h1` and each section title as `h2`, and every figure card inside a section (StructureCard, ReactionCoordinateCard, the video and tutorial cards) emits its title as `h4`. No `h3` is ever produced. Separately, SelectedResponseRenderer gives each option `role="radio"` on an individually tabbable button inside a `role="radiogroup"` with no roving tabindex or arrow-key handling, so the group does not behave as the ARIA radiogroup pattern its roles announce.
- **Learner impact** — Heading-based navigation reports a gap in every one of the six sections, which makes the figure headings read as nested two levels deeper than they are. In the answer choices, a screen-reader user told they are in a radiogroup will reach for arrow keys, which do nothing; each option is instead a separate tab stop. Neither blocks completion.
- **Evidence** — [internal source reference — not in this repo] lines 118 (`Heading as="h1"`) and 140 (`Heading as="h2"`); [internal source reference — not in this repo] lines 188, 304, 514 (`Heading as="h4"`); [internal source reference — not in this repo] lines 136-153.
- **Recommended outcome** — Figure headings need to sit one level below their section rather than two, and the answer-choice group needs interaction behaviour that matches the roles it announces.

**Open questions**

- Is `stereochemistry_conversion` intended to be reader-renderable at all, or is it a deck-only asset kind? The answer decides whether access-004 is a compiler gap to close or an authoring choice that needs a different asset type on the reading surface.
- Where are this chapter's 20 questions actually delivered to students? In the reader, ChapterHomeworkPanel is gated behind hasTeacherPreviewAccess, so I could not confirm the student-facing surface or its focus management, error announcement, and submit-feedback behaviour.
- The six nuggets' `practice_check` items and the six concepts' `trouble_spots` appear in no block of the compiled reader chapter. I could not determine whether any surface renders them, so I could not assess their accessibility.
- I filed the hint answer-leaks (access-006) and the chair default-answer defect (access-008) under `assessment-readiness`. The rubric assigns answer-leak neutrality to `alt-text-quality`, but that category is scoped to descriptions and figure alt text; no listed category covers a hint ladder. Flagging the choice so the next run can reuse it consistently.
- The ring-flip block is badged 'Reaction-coordinate diagram — ChemIllusion' for a conformational interconversion, because conformational_energy_profile maps onto the reaction_coordinate block type. Whether that mislabel is worth correcting for screen-reader users is a call I have left to the orchestrator rather than filing separately.

#### Learner with Visual Preference — 3.4/10

_persona_version 1.0.0 · publication_blockers: vis-001_

This chapter's entire subject is three-dimensional shape — chair geometry, axial versus equatorial bonds, the ring flip, ring puckering, and the two faces of a ring — and not one of those geometries is drawn anywhere a student can see. I traced all nine authored assets into the compiled reader: seven are `molecule` assets that render as flat RDKit 2D polygons (a triangle, a square, a pentagon, and hexagons), and four of those nine rendered figures are byte-identical repeats of an earlier one. The two assets that carry actual geometric argument both compile to nothing usable: `stereo-cis-trans-dmcp` (stereochemistry_conversion) is not in the reader compiler's `_ASSET_TYPE_TO_BLOCK` map at all, so `_asset_block` returns None and the cis/trans figure is silently dropped — the cis-trans section ships with a flat ring drawn from a SMILES that has no stereobonds, so the same-face/opposite-face distinction the whole section teaches appears in zero pixels. `cep-cyclohexane-flip` compiles to a `reaction_coordinate` block whose `spec` is deliberately withheld (the builder inlines a spec only when it has `steps` AND `minima_labels`), so ReactionCoordinateCard fails and prints the alt text twice under a badge reading 'Reaction-coordinate diagram' — a mislabel of a conformational profile, and a figure with no figure in it, repeated in two sections. Both ring-flip video blocks are `is_hidden: true` with `url: ""` and render nothing. The net result: the section titled 'The strain-free chair' contains one picture, a planar hexagon, captioned 'Show the strain-free six-membered ring' — precisely the object the concept's own `trouble_spots` entry warns students not to reason from. The one place a real chair is drawn in this entire package is inside the `chair` question widget (ChairPlacementRenderer, which is genuinely good: true chair projection, numbered carbons, clickable axial and equatorial stubs, keyboard-complete), i.e. a student meets the chair for the first time while being graded on it. Separately, six questions author `structure_smiles` on their options/cases, and MatchingRenderer, SelectedResponseRenderer, and ComparisonMatrixRenderer all read only `imageUrl` — so 'Match each structure to its IUPAC name' presents no structures. The prose is careful and well written; it is doing all of the work alone.

**Strengths**

- The `chair` question type is the strongest geometric surface in the package: ChairPlacementRenderer draws a true chair projection (parallel opposite ring bonds, vertical alternating axials, equatorials parallel to their ring bonds), numbers every carbon, gives each carbon a visible axial and equatorial stub, and makes every target a real focusable button with an accessible select-table equivalent. ch4-chair-tbutyl and ch4-chair-tbutyl-v2 land the axial/equatorial distinction visually and operably.
- The prose is genuinely well written and does the explanatory work honestly — 'four carbons define a plane while the remaining two pucker to opposite sides' and 'six equatorial bonds extend outward from the ring's equator, angled only slightly up or down' are as close as sentences can get to a picture.
- The `expanded` detail tier is a true superset of `standard` in all six nuggets — every number, ratio and caveat in the standard text survives into the tier the reader shows by default. That is the failure mode this platform has repeatedly hit and this chapter does not.
- The wrong-answer explanations on ch4-ring-flip-multi do a clean visual-reasoning contrast in words — separating what the flip changes (axial/equatorial) from what it preserves (faces, cis/trans, every sigma bond) — and directly name the 'substituents move to the other face' misconception.
- Every asset carries alt text, and for the flat structures those descriptions accurately match what is drawn.
- The chapter's own metadata predicted this gap: concepts[3] and concepts[4] declare preferred_representations including `conformational_energy_profile`, and the trouble_spots name the flat-hexagon error precisely. The authoring intent was right; the rendering pipeline is where it was lost.

**Findings**

##### `vis-001` — blocker · visual-opportunity · confidence 0.97

- **Location** — `section_id`: nugget-chair; `concept_slug`: cyclohexane-chair; `nugget_id`: nugget-axial-equatorial; `anchor_text`: Six axial bonds stand parallel to the ring axis, alternating up and down on successive carbons.
- **Observation** — The chapter's four central geometric claims — the chair fold, the axial/equatorial bond families, the ring flip, and the 1,3-diaxial clash — are asserted only in prose. I traced every block of the compiled reader: the sections 'The strain-free chair', 'Axial and equatorial positions interchange in the ring flip', and 'Substituents prefer equatorial positions' contain, between them, one flat hexagon (blk-d69hlje0), two flat methylcyclohexanes (blk-4n97fgbg, blk-1fipmwum), one flat 1,2-dimethylcyclohexane (blk-8uoppt3t), two energy-profile cards that render no diagram (blk-4cmtjx9y, blk-ciysf6cq), and two hidden video blocks that render nothing (blk-chgbfhfg, blk-9o04cps5). No chair is drawn. No axial or equatorial bond is drawn or labelled. The phrase 'alternating up and down on successive carbons' describes an alternation the student is never shown.
- **Learner impact** — A student who does not already hold the chair in their head has no external representation to build one from. Every downstream task in the chapter — deciding which chair is preferred, counting equatorial methyls in trans-1,2-dimethylcyclohexane (ch4-equatorial-count), placing tert-butyl (ch4-chair-tbutyl) — requires mentally constructing a figure the chapter declined to provide. The first chair drawing they encounter is inside a graded question widget. This also lands hardest on exactly the students the chapter says it is worried about: the concept's own trouble_spot is 'Drawing a flat hexagon and reasoning from it about strain', and a flat hexagon is what the chapter hands them.
- **Evidence** — concepts[3].trouble_spots = ['Drawing a flat hexagon and reasoning from it about strain']; concepts[4] 'axial-equatorial-ring-flip' has preferred_representations ['molecule','conformational_energy_profile'] and its two authored assets are mol-methylcyclohexane (flat) and cep-cyclohexane-flip (renders no diagram — see vis-004). Reader sections nugget-chair / nugget-axial-equatorial / nugget-substituted contain no block that depicts a non-planar ring.
- **Recommended outcome** — The chapter needs the chair geometry itself visible on the page: a puckered six-membered ring with its axial set distinguished from its equatorial set, and the same ring shown after the flip so the interchange is something a student can see rather than infer. Note for the orchestrator that of the reader-renderable kinds, only `molecule`/`reaction` (RDKit 2D, which cannot draw a chair), `reaction_coordinate` carrying a steps+minima_labels spec, `newman_projection`/`synthesis_roadmap`/`orbital_overlay` (routed live via `teaching_asset`), `enzyme_active_site`, and image-family kinds WITH a hosted `image_url` actually paint pixels in the reader — so this need can only be met by a kind on that list; the platform already contains a correct chair projection ([internal source reference — not in this repo]) that no reader surface currently consumes.

##### `vis-002` — high · figure-accuracy · confidence 0.93

- **Location** — `section_id`: nugget-chair; `asset_id`: mol-cyclohexane; `concept_slug`: cyclohexane-chair; `anchor_text`: Show the strain-free six-membered ring, the reference cycloalkane.
- **Observation** — In the section 'The strain-free chair', whose prose says 'A planar cyclohexane would combine 120° internal angles with twelve eclipsed C–H bonds', the only structure shown is a planar hexagon rendered from SMILES C1CCCCC1, and the caption the reader prints directly under it is 'Show the strain-free six-membered ring, the reference cycloalkane.' The picture and the caption together assert that the drawn planar geometry is the strain-free one, which is the opposite of the section's thesis. The same mismatch recurs in the ring-strain section: mol-cyclobutane and mol-cyclopentane are drawn as a regular square and a regular pentagon in the same paragraph that says 'Cyclobutane folds slightly and cyclopentane adopts an envelope pucker'.
- **Learner impact** — The figure teaches the misconception the text is arguing against, and figures outlast paragraphs in memory. A student skimming for the picture takes away 'cyclohexane = flat hexagon = strain-free' and 'cyclobutane = flat square', which is exactly the reasoning error the chapter later needs them not to make when comparing chairs.
- **Evidence** — assets[3] mol-cyclohexane learning_goal 'Show the strain-free six-membered ring, the reference cycloalkane', compiled as blk-d69hlje0 in section nugget-chair; assets[1] mol-cyclobutane alt_text 'a square of four carbon atoms'; nugget-ring-strain prose 'Cyclobutane folds slightly and cyclopentane adopts an envelope pucker'.
- **Recommended outcome** — Where the prose's point is that the ring is NOT planar, the accompanying figure must not be a regular planar polygon presented as the compound's shape — either the figure needs to carry the fold it is being cited for, or its caption must stop describing the drawn planar shape as the strain-free/relaxed geometry.

##### `vis-003` — high · media-equivalence · confidence 0.96

- **Location** — `section_id`: nugget-cyclo-cis-trans; `asset_id`: stereo-cis-trans-dmcp; `concept_slug`: cycloalkane-cis-trans; `anchor_text`: Wedge-and-dash drawings make the relationship explicit
- **Observation** — The authored side-by-side cis/trans figure never reaches the reader. `stereochemistry_conversion` is absent from `_ASSET_TYPE_TO_BLOCK` in [internal source reference — not in this repo] returns None and the asset is dropped without warning — the compiled section nugget-cyclo-cis-trans contains only a text block, one molecule block, and a Wikipedia link. The surviving figure, mol-dimethylcyclopentane, is drawn from SMILES 'CC1CCCC1C', which specifies no stereocentres, so RDKit draws plain bonds: no wedge, no dash, no face. The section whose entire subject is same-face versus opposite-face therefore depicts neither. Independently, the asset's spec would not render even where the kind is supported: AssetPreview's stereochemistry_conversion branch reads `spec.molecules[].smiles`, and this asset's spec carries `input_representation`/`output_representation` prose strings instead, so it would produce an empty card there too.
- **Learner impact** — Wedge-and-dash is a notation students are being asked to read for the first time in this chapter, and the chapter explains it in words while showing no example of it. Students who cannot yet translate 'two wedges versus one wedge and one dash' into a mental picture have nothing to calibrate against, and the cis/trans questions (ch4-cis-trans-sort) are then answerable purely by matching the words 'same face' to 'cis' without any geometry ever entering.
- **Evidence** — [internal source reference — not in this repo] (lines 15-33) has no 'stereochemistry_conversion' key; `_asset_block` returns None for unmapped types. assets[7].spec = {input_representation, output_representation, show_rs_annotation, labels}. [internal source reference — not in this repo].
- **Recommended outcome** — The cis/trans face distinction needs to exist as a drawing the student can look at, in a form the reader actually emits a block for — and the fact that an authored, validated, schema-legal asset can be silently discarded by the reader compiler should be surfaced, since the package's own asset manifest reports this chapter as having a cis/trans figure that no student will ever see.

##### `vis-004` — high · figure-purpose · confidence 0.96

- **Location** — `section_id`: nugget-chair; `asset_id`: cep-cyclohexane-flip; `nugget_id`: nugget-axial-equatorial; `anchor_text`: Rank chair, twist-boat, boat, and half-chair geometries along the ring-flip coordinate.
- **Observation** — The ring-flip energy profile renders as an empty card. The compiler maps `conformational_energy_profile` to a `reaction_coordinate` block but inlines the spec only when it contains both `steps` and `minima_labels`; this spec has `coordinate`/`scan_smiles`/`conformers`/`scientific_caveats`, so no `spec` reaches the block (verifiable in the compiled JSON: blk-4cmtjx9y and blk-ciysf6cq carry only asset_id, title, alt_text, description). ReactionCoordinateCard then sets `failed` and renders the alt text in italics where the diagram should be, followed by 'Described as: …' — the same sentence printed twice, under a blue badge reading 'Reaction-coordinate diagram — ChemIllusion'. That badge is also a category error: this is a conformational profile, not a reaction coordinate, and the platform's own authoring guidance treats conflating the two as a mistake. This dead card appears in both nugget-chair and nugget-axial-equatorial.
- **Learner impact** — The one figure that would let a student see the shape of the flip — two minima, a barrier between them, the boat sitting above the twist-boat — is absent, so the numbers 23, 29 and 45 kJ/mol stay as three unrelated quantities in a paragraph. Students are then asked to rank exactly these conformers (ch4-conformer-rank, ch4-conformer-rank-v2) with no depiction of the ordering they are ranking. The visible artefact is worse than nothing: a bordered, badged card that looks like a figure and contains a duplicated sentence, twice in the chapter.
- **Evidence** — [internal source reference — not in this repo] lines 149-164 (`if isinstance(spec, dict) and 'steps' in spec and 'minima_labels' in spec`); [internal source reference — not in this repo] ReactionCoordinateCard lines 275-334 (`if (!spec) { setFailed(true); return; }`, then alt_text rendered at 322-325 and again at 332-334).
- **Recommended outcome** — The energy ordering of chair / twist-boat / boat / half-chair needs to be visible as a shape, not only as three numbers in a sentence, and the reader must stop presenting an alt-text-only card as though it were a rendered diagram. Note that a renderer for this asset kind already exists and is used elsewhere (renderConformationalProfile / buildConformationalEnergyProfileSvg in [internal source reference — not in this repo] is in AssetPreview's INLINE_SVG_TYPES) — the reader path is the only surface that drops it, because `_LIVE_RENDERED_FIELDS` lists only synthesis_roadmap, newman_projection and orbital_overlay.

##### `vis-005` — medium · figure-accuracy · confidence 0.85

- **Location** — `asset_id`: cep-cyclohexane-flip; `question_slug`: ch4-conformer-rank-v2; `anchor_text`: { "label": "twist-boat", "relative_energy": "medium" }
- **Observation** — Even if the profile were wired up, the authored spec cannot express what the chapter teaches. The qualitative renderer maps relative_energy through ENERGY_LEVEL = {low: 0.14, medium: 0.5, high: 0.9}; this spec labels both 'twist-boat' and 'boat' as 'medium', so they would plot at identical heights — while the prose (23 vs 29 kJ/mol) and question ch4-conformer-rank-v2 both require the student to see the boat above the twist-boat. Two further hazards in the same spec: seven points across a ~316px plot area with labels like 'twist-boat' and 'chair (flipped)' at font-size 11 will collide, and three consecutive points at the same y will stack their labels on each other; and because the spec carries `scan_smiles: "C1CCCCC1"`, renderConformationalProfile takes the RDKit relaxed-torsion-scan branch first and ignores `coordinate: "ring_flip"` entirely — a dihedral scan of a ring bond is not the ring-flip pathway, so the smooth curve it returns would be captioned as a torsion scan and mistaken for the flip profile.
- **Learner impact** — A student reading the diagram would either see two conformers drawn as equally stable (contradicting the ranking they are graded on), or see a torsion-scan curve presented as the ring-flip pathway. Both are worse than the current absence, because a wrong diagram is trusted.
- **Evidence** — [internal source reference — not in this repo] line 175 ENERGY_LEVEL; lines 264-296 (label placement, no collision handling); lines 368-383 (`if (spec.scan_smiles) { torsionScanApi.scan(...) }` runs before the schematic fallback and never consults `spec.coordinate`). Package asset spec conformers 3 and 4 are both relative_energy 'medium'.
- **Recommended outcome** — Before this profile is made visible, its energy encoding needs to be able to separate the boat from the twist-boat, its labels need room not to overlap, and the ring-flip coordinate must not be silently rendered as a torsion scan.

##### `vis-006` — medium · visual-redundancy · confidence 0.94

- **Location** — `section_id`: nugget-substituted; `asset_id`: mol-methylcyclohexane; `anchor_text`: Show the monosubstituted cyclohexane whose two chairs differ in energy.
- **Observation** — Four of the nine figure blocks in the chapter are exact repeats. mol-methylcyclohexane renders three times (blk-mcgwfytm in nomenclature, blk-4n97fgbg in axial/equatorial, blk-1fipmwum in substituted cyclohexanes) with identical title, identical caption and identical alt text; mol-cyclohexane renders twice (blk-wjf3dcy9, blk-d69hlje0), likewise identical; the dead ring-flip card renders twice; the hidden video block is emitted twice. Each repeat adds no information — the caption 'Show the monosubstituted cyclohexane whose two chairs differ in energy' promises two chairs and shows a flat structure, three separate times.
- **Learner impact** — Repetition without variation trains students to stop looking at the figures, which is costly in a chapter where the few remaining figures already carry very little. It also creates a false impression of visual density: the chapter appears to have nine illustrations and actually has five distinct ones, none of them three-dimensional.
- **Evidence** — Compiled reader blocks blk-mcgwfytm / blk-4n97fgbg / blk-1fipmwum all have content {name: 'Methylcyclohexane', smiles: 'CC1CCCCC1', description: 'Show the monosubstituted cyclohexane whose two chairs differ in energy.'}; blk-wjf3dcy9 and blk-d69hlje0 are identical cyclohexane blocks.
- **Recommended outcome** — A structure re-shown in a later section should carry the marking that section's argument needs (the axial/equatorial labelling, the two competing chairs, the diaxial contact) or should not be re-shown at all; identical repeats should be reduced rather than multiplied.

##### `vis-007` — medium · visual-opportunity · confidence 0.9

- **Location** — `section_id`: nugget-substituted; `concept_slug`: substituted-cyclohexanes; `anchor_text`: draw both chairs, count 1,3-diaxial interactions
- **Observation** — The chapter's most procedural instruction — 'The analysis generalizes: draw both chairs, count 1,3-diaxial interactions, and the chair with fewer axial substituents … is the preferred conformation' — instructs the student to produce a drawing that the chapter never demonstrates. Neither chair of methylcyclohexane is drawn, the 1,3-diaxial contact between an axial methyl and the axial hydrogens on C3 and C5 is never shown, and the trans-both-equatorial versus cis-one-axial comparison for 1,2-dimethylcyclohexane exists only as a sentence. The concept's own trouble_spot is 'Missing the 1,3-diaxial origin of the axial substituent penalty', which is a spatial relationship (three axial bonds pointing the same way on alternate carbons) that a sentence cannot carry.
- **Learner impact** — The 7.6 kJ/mol penalty becomes a number to memorise rather than a crowding a student can see, and the trans-versus-cis conclusion becomes a fact rather than a consequence. Students then meet ch4-equatorial-count and ch4-equatorial-count-v2, whose own hint says 'Draw both chairs' — advice they have never seen carried out.
- **Evidence** — nugget-substituted expanded text; concepts[5].trouble_spots; question ch4-equatorial-count hint level 1 'Draw both chairs; the trans isomer has one chair with no axial methyls.'
- **Recommended outcome** — The two-chairs-side-by-side comparison and the diaxial contact that decides between them need to be depicted at least once, so that 'count the 1,3-diaxial interactions' names something the student has watched being counted.

##### `vis-008` — medium · media-equivalence · confidence 0.93

- **Location** — `question_slug`: ch4-name-structure-match; `anchor_text`: Match each structure to its IUPAC name.
- **Observation** — Six questions author `structure_smiles` on their options, cases, or matching items, and no question renderer reads that field. MatchingRenderer (line 41-43) and ComparisonMatrixRenderer (line 28) build their items from `imageUrl` only; SelectedResponseRenderer renders `option.imageUrl` at line 169 and nothing else. No upstream layer maps structure_smiles to an image — the compiled question-set preserves the field verbatim. The affected items are ch4-name-structure-match, ch4-name-structure-match-v2, ch4-ring-strain-most, ch4-ring-strain-most-v2, ch4-ring-strain-matrix, ch4-ring-strain-matrix-v2. The matching prompt reads 'Match each structure to its IUPAC name' while the left column shows only sentences ('A five-membered ring bearing one CH₃'), so the question asks about structures it does not display.
- **Learner impact** — Students never practise reading a ring structure and producing its name — they practise translating one verbal description into another, which is a different skill and a strictly easier one. The nomenclature and ring-strain questions lose the representation they were designed around, and the prompt's promise of a structure is unmet, which reads as a broken page.
- **Evidence** — [internal source reference — not in this repo], 82-83; [internal source reference — not in this repo], 108-110; [internal source reference — not in this repo]. Compiled question-set.json retains structure_smiles in student_config for the six slugs listed.
- **Recommended outcome** — Questions whose stem promises a structure need the structure to reach the screen; until the option-level structure channel renders, the chapter should not depend on it to carry the visual half of a naming or comparison task. This is a platform-level gap, not a chapter authoring error.

##### `vis-009` — medium · visual-opportunity · confidence 0.86

- **Location** — `section_id`: nugget-ring-strain; `concept_slug`: ring-strain; `anchor_text`: giving a total strain near 115 kJ/mol
- **Observation** — The ring-strain section makes a quantitative comparison across four ring sizes — roughly 115 kJ/mol for cyclopropane, about 110 for cyclobutane, about 26 for cyclopentane, and zero for cyclohexane — and shows three flat polygons that carry none of it. The three figures are interchangeable in appearance; nothing about the triangle looks more strained than the pentagon. The comparison itself, which is the section's whole point, exists only as numbers embedded in a paragraph.
- **Learner impact** — The counter-intuitive part of this section is that strain is not monotonic in ring size — cyclobutane is nearly as bad as cyclopropane, then it collapses at five and six. That non-monotonic shape is exactly what a reader loses when the numbers stay in prose, and it is the misconception the concept's trouble_spot names ('Assuming all rings are strained equally').
- **Evidence** — concepts[2].trouble_spots = ['Assuming all rings are strained equally, or that cyclohexane is strained at all']; compiled reader blk-t2w4o9go text; assets mol-cyclopropane / mol-cyclobutane / mol-cyclopentane are the section's only figures.
- **Recommended outcome** — The strain-versus-ring-size comparison needs a form in which the relative magnitudes can be seen at once rather than accumulated across three sentences.

##### `vis-010` — low · alt-text-quality · confidence 0.88

- **Location** — `asset_id`: mol-dimethylcyclopentane; `section_id`: nugget-cyclo-cis-trans; `anchor_text`: cis and trans configurations exist
- **Observation** — Two alt texts describe something other than the image. mol-dimethylcyclopentane's alt text ends '…; cis and trans configurations exist', but the rendered figure shows neither configuration — the SMILES has no stereobonds, so a student relying on the description is told about a distinction the picture does not contain. mol-cyclobutane's alt text calls the ring 'a square of four carbon atoms' in a section that says cyclobutane folds, so the description asserts a planarity the prose denies. Separately, because cep-cyclohexane-flip currently renders as alt text only (vis-004), its alt text is doing the entire job of the figure while omitting the quantities the prose supplies (23 / 29 / 45 kJ/mol) and the fact that the boat lies above the twist-boat.
- **Learner impact** — Descriptions that promise more than the figure delivers leave a student unable to tell whether they have failed to see something. And where alt text is the only surviving channel, its omissions become the chapter's omissions.
- **Evidence** — assets[5].accessibility.alt_text; assets[1].accessibility.alt_text; assets[8].accessibility.alt_text vs nugget-chair prose. Overlaps the Accessibility persona's remit.
- **Recommended outcome** — Each description needs to match what its figure actually shows, and any figure currently reaching students only through its description needs that description to carry the full teaching content of the diagram it replaces.

##### `vis-011` — low · figure-purpose · confidence 0.84

- **Location** — `section_id`: nugget-cyclo-nomenclature; `concept_slug`: cycloalkane-nomenclature; `anchor_text`: is 1-cyclopropylbutane, not butylcyclopropane
- **Observation** — The nomenclature section draws cyclohexane and methylcyclohexane — the two structures a reader least needs help with — while the one decision the prose flags as 'specific to rings', choosing between the ring and a longer attached chain as parent (1-cyclopropylbutane versus butylcyclopropane), gets no figure at all. The same asymmetry shows in the concept's trouble_spot, 'Choosing the ring as parent when an attached chain has more carbons', which no figure addresses.
- **Learner impact** — Figure attention is spent where the difficulty is not. A student who already reads a hexagon fine gets two pictures of easy cases and no picture of the case they are actually going to get wrong.
- **Evidence** — concepts[0].trouble_spots; nugget-cyclo-nomenclature asset_ids ['mol-cyclohexane','mol-methylcyclohexane']; compiled blocks blk-wjf3dcy9, blk-mcgwfytm.
- **Recommended outcome** — The ring-versus-chain parent decision is the section's hard case and is the one that would benefit from being shown side by side; the trivial cases do not need two dedicated figures.

##### `vis-012` — low · color-motion-only · confidence 0.82

- **Location** — `asset_id`: video-ring-flip; `section_id`: nugget-axial-equatorial; `anchor_text`: mark the axial and equatorial hydrogens in two colors
- **Observation** — The ring-flip video brief is the chapter's designated home for the axial/equatorial interchange, and its storyboard encodes the two bond families by colour alone: 'mark the axial and equatorial hydrogens in two colors' and 'show every axial label now equatorial'. There is no second channel (line style, label, position callout) specified. The brief is also the only planned depiction of the interchange, and both its compiled blocks are `is_hidden: true` with an empty url, so today it shows nothing; the finding is a forward-looking constraint on production rather than a current on-screen defect.
- **Learner impact** — If produced as briefed, viewers who cannot distinguish the two chosen hues lose the entire distinction the animation exists to make, and any still frame or GIF export inherits the same single-channel encoding.
- **Evidence** — video_briefs[0].storyboard entries 1 and 3; compiled blocks blk-chgbfhfg and blk-9o04cps5 (url: "", is_hidden: true).
- **Recommended outcome** — When the ring-flip depiction is produced, the axial/equatorial distinction needs a channel that survives colour loss and a still frame — and the chapter should not be left depending on an unproduced motion asset as the sole carrier of its central geometric claim.

##### `vis-013` — low · media-equivalence · confidence 0.88

- **Location** — `section_id`: nugget-cyclo-cis-trans; `asset_id`: stereo-cis-trans-dmcp; `anchor_text`: cycloalkanes-and-stereochemistry
- **Observation** — The chapter has a complete asset manifest at frontend/public/content/organic/chapters/chapter-cycloalkanes/assets.manifest.json listing all nine assets, and ChapterAssetGallery exists to render exactly that manifest as a public 'everything we have for this chapter' media index. But READER_SLUG_TO_CONTENT_CHAPTER in [internal source reference — not in this repo] contains a single entry, 'alkenes-structure-and-reactivity' → 'chapter-03', so `hasAssetGallery` is false for this slug and the gallery never mounts. The one surface that would have shown the dropped stereochemistry figure and the conformational profile alongside the chapter is not wired to it.
- **Learner impact** — There is no fallback route to the chapter's figures — a student who wants to look at the pictures again has the reader page and nothing else, and the reader page is missing two of the nine.
- **Evidence** — [internal source reference — not in this repo] lines 122-124 and 229; manifest present on disk with all nine asset ids.
- **Recommended outcome** — Either the chapter's asset index needs to be reachable, or the manifest should not be presented as a shipped surface for this chapter; as it stands the package reports figures it has no path to display.

**Open questions**

- The compiled reader's ring-strain text contains a sentence that is not in topic.package.json ('The trade is not equally good: cyclobutane still carries about 110 kJ/mol of total strain, nearly as much as cyclopropane, whereas cyclopentane's envelope leaves only about 26 kJ/mol.'). The compiled artifact and the stated source of truth have drifted — which is authoritative, and was the reader rebuilt from a newer package than the one committed?
- Is the ring-flip video actually scheduled for production? Both blocks compile with url: "" and is_hidden: true, and two of the chapter's six sections currently point at it as their motion asset. If it is not being produced, the chapter needs a static carrier for that argument.
- Routing `conformational_energy_profile` to `teaching_asset` in [internal source reference — not in this repo] (as synthesis_roadmap/newman_projection/orbital_overlay already are) would make this chapter's energy profile render live with no new asset authored. Is a reader-compiler change in scope for a chapter-level correction pass, or should this chapter work around it?
- Should the validator reject an asset whose type has no reader block mapping (stereochemistry_conversion), rather than letting the compiler drop it silently? Every chapter authoring that type is shipping an invisible figure and reporting it as present.
- The chapter is available:false and unseeded; I reviewed the compiled artifacts as-is. If a reader-side render of `mol-*` assets can be given per-figure rdkit_options (the block content supports it), is there an approved route to a chair depiction through the molecule path, or must a chair figure go through a hosted `diagram` image_url?

### Orchestrator decisions

For each recommendation: the need, the chosen intervention and why it is the least-complex option that fully addresses that need, the target surface, and the persona findings it consolidates.

#### rec-001 — A verified chemistry correction lives only in the build artifact and the next recompile deletes it (blocker)

- **Need** — The compiled reader's expanded tier carries a corrected ring-strain sentence (cyclobutane ~110 kJ/mol, nearly cyclopropane's 115; cyclopentane ~26) that topic.package.json does not have, and that neither file applies to the terse or standard tiers. The source of truth therefore still teaches the uncorrected 'leaving moderate net strain', which is precisely the concept's own declared trouble spot, and any recompile silently reverts the fix.
- **Chosen intervention** — `prose-edit` on the **prose** surface
- **Why this is the least-complex option that fully addresses it** — The correct text already exists and has been verified; it only needs to live in the source, in every tier that states the claim. No new asset, no schema change, and it must precede any recompile or the compile step itself destroys the fix.
- **Source findings** — instr-001, instr-002, struggle-017

#### rec-002 — The chapter's entire subject — chair geometry — is never drawn (blocker)

- **Need** — Chair pucker, the axial/equatorial bond families, the up/down alternation, the ring flip's positional exchange, and the 1,3-diaxial contact are asserted in prose and depicted nowhere a student can see. Every figure in the three chair sections is a flat polygon, which is the exact object the concept's own trouble_spots entry warns students not to reason from. Four graded items then require reasoning on a chair the chapter never showed; the first chair a student meets is inside a graded widget.
- **Chosen intervention** — `new-figure` on the **figure** surface
- **Why this is the least-complex option that fully addresses it** — No description can substitute: the need is a spatial model, and three personas independently found that its absence breaks the chapter's last three sections. A longer description was considered and rejected as insufficient (it is rec-004's job for a different need). Of the asset kinds the reader compiler actually paints, the `diagram` type with a generated image_url is the least-complex route that needs no compiler change — the ch28 precedent.
- **Source findings** — vis-001, struggle-001, instr-004, access-001, vis-007, struggle-014, vis-002

#### rec-003 — Both nomenclature short-answer prompts contain their own answer (blocker)

- **Need** — 'Give the IUPAC name of the compound with SMILES CC1CCCCC1 (a cyclohexane ring bearing one methyl group)' hands over both name parts of the accepted answer `methylcyclohexane`; the variant likewise contains `ethylcyclopropane`. The chapter's only free-response naming practice measures word order, and reports competence a student may not have.
- **Chosen intervention** — `prose-edit` on the **assessment** surface
- **Why this is the least-complex option that fully addresses it** — The gloss exists because SMILES does not render as a structure, so deleting it would make the item unanswerable for a text-only reader. Rewording the gloss to describe the skeleton without naming its parts ('a six-membered ring carrying a one-carbon branch') keeps every learner able to answer while restoring what the item measures.
- **Source findings** — struggle-018

#### rec-004 — Seven level-1 hints state the answer, and several items have no second rung (high)

- **Need** — The first hint frequently determines the graded answer outright — 'the trans isomer has one chair with no axial methyls' (answer 2), 'cis means one axial, one equatorial' (answer 1), 'bulky groups avoid the orientation that points parallel to the ring axis' (the chapter defines axial as exactly that), 'the strain-free geometry is lowest; the ring-flip transition geometry is highest' (fixes all three cards). There is no rung between stuck and told, and the platform's answer-leak guard inspects only accessible_description, so nothing catches them.
- **Chosen intervention** — `prose-edit` on the **assessment** surface
- **Why this is the least-complex option that fully addresses it** — Hints are the scaffold a learner reaches for precisely because this chapter's visual channel is empty; handing over the answer removes the only graduated support they have. Rewriting level 1 to redirect attention and adding a narrowing level 2 is bounded editing of existing fields.
- **Source findings** — access-006, struggle-006

#### rec-005 — The chapter states the 1,3-diaxial counting rule three ways and one of them is wrong (high)

- **Need** — Prose and one hint correctly place the partners at 'carbons 3 and 5' (two carbons from C1, which is what '1,3-' means); ch4-chair-tbutyl's level-2 hint says 'three carbons away', which points at C4 — the one position with no 1,3-diaxial relationship to C1. The interaction's name is itself the counting claim, so a contradiction here removes the student's only self-check.
- **Chosen intervention** — `prose-edit` on the **assessment** surface
- **Why this is the least-complex option that fully addresses it** — A verified factual error in one string; the correct wording already exists elsewhere in the chapter.
- **Source findings** — instr-007, struggle-008

#### rec-006 — Question feedback switches to kcal/mol against kJ/mol prose, and one number collides (high)

- **Need** — Prose uses kJ/mol exclusively (0 kcal occurrences); four feedback strings use kcal/mol with no conversion given. Every converted value is numerically correct, but cyclobutane's 'about 26 kcal/mol' collides head-on with the prose's 'cyclopentane's envelope leaves only about 26 kJ/mol' — the same numeral naming two different compounds across two surfaces.
- **Chosen intervention** — `prose-edit` on the **assessment** surface
- **Why this is the least-complex option that fully addresses it** — The chemistry is right and only the unit presentation is wrong, so normalising the feedback to kJ/mol (retaining kcal as an explicit parenthetical conversion where it helps) fully resolves it without touching any answer key.
- **Source findings** — instr-008, struggle-007

#### rec-007 — The cis/trans figure reaches no learner, and the surviving figure's description claims stereochemistry it does not carry (high)

- **Need** — `stereochemistry_conversion` has no entry in the reader compiler's _ASSET_TYPE_TO_BLOCK, so _asset_block returns None and stereo-cis-trans-dmcp is dropped without warning. The section teaching wedge-and-dash notation therefore contains no wedge and no dash; its only figure is drawn from CC1CCCC1C, which specifies no stereocentres, while that figure's alt text asserts 'cis and trans configurations exist'.
- **Chosen intervention** — `new-figure` on the **figure** surface
- **Why this is the least-complex option that fully addresses it** — Mapping the type in the compiler alone would not render it: AssetPreview's stereochemistry_conversion branch reads spec.molecules[].smiles and this asset's spec carries prose strings instead. A drawn cis/trans pair on a reader-renderable kind is the least-complex route that actually reaches a student, and the misleading alt text is corrected in the same pass.
- **Source findings** — vis-003, access-004, instr-005, vis-010, struggle-019

#### rec-008 — The ring-flip energy profile renders nothing, and the alt text standing in for it is wrong (high)

- **Need** — A conformational_energy_profile has no steps/minima_labels, so the compiler inlines no spec and ReactionCoordinateCard fails to an italic alt-text card, twice in the chapter. That alt text is therefore the whole figure for every learner — and it calls the middle region a 'twist-boat/boat plateau' when the asset's own caveat puts the boat (~29 kJ/mol) above the twist-boats (~23), i.e. a local maximum between two shallow minima. The spec also buckets both at 'medium', so they would plot at equal height if it ever did render. This is exactly the discrimination ch4-conformer-rank-v2 grades.
- **Chosen intervention** — `structured-chemical-description` on the **figure** surface
- **Why this is the least-complex option that fully addresses it** — Making the diagram render is a reader-compiler change and out of scope for a chapter correction pass. But because the description IS the figure here, correcting it to state the true ordering and the actual energies fully serves every learner today, at no platform risk; the degenerate spec buckets are fixed alongside so a future render is not wrong.
- **Source findings** — access-005, vis-004, vis-005, instr-003

#### rec-009 — Not one of the nine assets carries a long_description (high)

- **Need** — Every figure delivers a shape-naming alt text ('a hexagon of six carbon atoms') and nothing about the chemistry it was placed there to teach. The compiler forwards accessibility.long_description and the reader renders it, so the omission is authorial, not a platform gap — and the reader prints descriptions visibly as 'Described as: …', so the thinness costs sighted readers too.
- **Chosen intervention** — `longer-description` on the **figure** surface
- **Why this is the least-complex option that fully addresses it** — The delivery path is already built and proven; only the content is missing. This is the least-complex intervention that turns nine inert figures into teaching ones, and it is the field every chapter from ch24 onward populates.
- **Source findings** — access-003, instr-017, vis-010

#### rec-010 — Two items are graded on a concept taught one section later (high)

- **Need** — ch4-methylcyclohexane-chair asks which chair of methylcyclohexane is preferred and is tagged to `axial-equatorial-ring-flip`, but that nugget deliberately stops before the equatorial preference; the preference, its 1,3-diaxial cause and the 7.6 kJ/mol number all arrive in `nugget-substituted`. ch4-ring-flip-multi-v2 option c has the same dependency. A student practising the tagged concept cannot derive the answer.
- **Chosen intervention** — `prose-edit` on the **assessment** surface
- **Why this is the least-complex option that fully addresses it** — Retagging the affected items to the concept that actually teaches them is a one-field change and preserves the author's deliberate sequencing, whereas moving the content forward would collapse two concepts the chapter separates on purpose.
- **Source findings** — instr-009, struggle-009

#### rec-011 — Both chair workspace items are answerable by accepting the interface default (high)

- **Need** — ChairPlacementRenderer initialises the orientation select to 'equatorial' (line 289, and updateSubstituent defaults to it at line 217), and ChairGrader accepts any ring position (allow_ring_rotation defaults True). Both ch4-chair-tbutyl and -v2 key 'equatorial'. A student who picks any ring position and submits scores correct without touching the graded field, so the chapter's only constructed-response items have zero discrimination.
- **Chosen intervention** — `added-practice` on the **assessment** surface
- **Why this is the least-complex option that fully addresses it** — Rewording cannot fix a defect that lives in the interface's resting state. The bounded fix is one item whose correct answer is not the default — a case where a substituent must go axial — which measures a decision rather than a click. Changing the renderer default is the platform-side alternative and is recorded, not taken, because it would silently alter every chair item in every chapter.
- **Source findings** — instr-012, access-008

#### rec-012 — Both matching items are answerable without reading a structure (medium)

- **Need** — Left items are verbal restatements of the names on the right — 'A four-membered ring, unsubstituted' pairs to 'Cyclobutane'. The authored structure_smiles is real and verified but no renderer reads it, so the items intended to assess reading a skeletal ring instead assess knowing that four-membered means cyclobut-.
- **Chosen intervention** — `instructor-note` on the **assessment** surface
- **Why this is the least-complex option that fully addresses it** — The root cause is a platform gap (MatchingRenderer, SelectedResponseRenderer and ComparisonMatrixRenderer all read only imageUrl), already recorded against ch31. Rewriting the left items to be non-synonymous is possible but would make them unanswerable for a text-only reader while the structure channel stays dark, so the honest action is to record the dependency and correct the accessible_descriptions that promise 'three rendered structures'.
- **Source findings** — instr-010, vis-008, struggle-015, access-011

#### rec-013 — The nomenclature objective names a decision the assessment never exercises (medium)

- **Need** — All four naming items are cases where the ring wins. The only chain-wins case — the chapter's own 1-cyclopropylbutane line — is never assessed, so 'the ring is always the parent' scores full marks. The chapter also presents that textbook convention as absolute although current IUPAC recommendations reverse it, and it chose for its sole illustration the one case where a student's outside lookup will disagree.
- **Chosen intervention** — `prose-edit` on the **prose** surface
- **Why this is the least-complex option that fully addresses it** — Flagging the convention difference is a one-clause edit that prevents a student's ChemDraw or PubChem lookup from reading as the chapter being wrong. The additional chain-wins assessment item is left as a recommendation because bank expansion needs sign-off.
- **Source findings** — instr-011, instr-016, vis-011

#### rec-014 — Faces and axial/equatorial are taught in separate sections and never reconciled (high)

- **Need** — The chapter's highest-frequency misconception — that a ring flip moves a substituent to the other face — is named and corrected only inside a wrong-answer explanation. No section states that face (up/down) and orientation (axial/equatorial) are independent, that a flip changes one and preserves the other, or the rule that on adjacent carbons a cis pair is necessarily one axial plus one equatorial. That last rule exists only inside a hint, and two graded items depend on it.
- **Chosen intervention** — `prose-edit` on the **prose** surface
- **Why this is the least-complex option that fully addresses it** — Both facts are single sentences the chapter already knows and states elsewhere in non-teaching fields; promoting them into the nuggets that teach the flip and the substituted rings is the least-complex fix and converts two memorised results into a reconstructible rule.
- **Source findings** — struggle-010, access-002, struggle-014

#### rec-015 — Six practice checks, six trouble spots and every learning objective reach no reader surface (high)

- **Need** — The chapter's whole formative layer — including the best retrieval question in it ('Why can cis- and trans-1,2-dimethylcyclopentane be separated while conformations of butane cannot?') — exists only in the source file. A student reads six sections with no point at which they are asked to produce anything.
- **Chosen intervention** — `instructor-note` on the **instructor-support** surface
- **Why this is the least-complex option that fully addresses it** — This is a compiler/reader gap, not an authoring omission, and it is now recorded identically for ch27, ch30, ch31 and ch4. Fixing it means emitting new reader block types, which is a platform change well outside a chapter correction pass.
- **Source findings** — instr-006, struggle-005

#### rec-016 — Disubstituted coverage stops at the 1,2 relationship (medium)

- **Need** — Prose and both counting items treat only 1,2-dimethylcyclohexane. The 1,3 and 1,4 patterns — where the cis/trans-to-axial/equatorial mapping inverts — never appear, so students generalise 'cis means one axial one equatorial' from the only case they see, which is true for 1,2 and 1,4 and false for 1,3. This also undercuts the promised carry-forward to sugars and steroids, where 1,3-diaxial relationships dominate.
- **Chosen intervention** — `added-practice` on the **practice** surface
- **Why this is the least-complex option that fully addresses it** — A worked 1,3 case plus one item is the smallest change that stops the false generalisation, but it is genuine bank expansion, so it is recorded for sign-off rather than applied in this pass.
- **Source findings** — instr-014

#### rec-017 — Four of nine figure blocks are byte-identical repeats (medium)

- **Need** — mol-methylcyclohexane renders three times and mol-cyclohexane twice, each with identical title, caption and alt text; the dead energy card and the hidden video block each render twice. The caption 'Show the monosubstituted cyclohexane whose two chairs differ in energy' promises two chairs and shows a flat structure, three separate times. The chapter appears to have nine illustrations and has five distinct ones.
- **Chosen intervention** — `new-figure` on the **figure** surface
- **Why this is the least-complex option that fully addresses it** — Resolved as a consequence of rec-002 rather than by deletion: a structure re-shown in a later section should carry the marking that section's argument needs, which is exactly what the chair figures supply. Deleting the repeats without adding the chair would leave the sections with no figure at all.
- **Source findings** — vis-006

#### rec-018 — Terms carried from earlier chapters are load-bearing but never glossed (medium)

- **Need** — 'the gauche interaction of butane', 'steric strain', 'Newman projection' and 'flagpole' hydrogens all appear at default reading depth with no local definition. The Newman sentence is the chapter's proof that the chair is torsion-free, and a student who cannot evaluate it takes the central claim on authority. The declared prerequisites list ethane-conformations but not butane-conformations, which is what the gauche analogy actually assumes.
- **Chosen intervention** — `prose-edit` on the **prose** surface
- **Why this is the least-complex option that fully addresses it** — Each is a clause-length gloss plus one prerequisite slug, and the 7.6 kJ/mol axial penalty becomes derivable rather than memorised once the gauche link is explicit (it is exactly 2 x 3.8 kJ/mol, one interaction to C3 and one to C5).
- **Source findings** — struggle-012, instr-013, instr-015

#### rec-019 — Small-ring alt text asserts the planar geometry the surrounding prose is arguing against (medium)

- **Need** — mol-cyclobutane is described as 'a square of four carbon atoms' and mol-cyclopentane as 'a pentagon of five carbon atoms' in the same section that explains both pucker; mol-cyclohexane's caption calls the drawn planar hexagon 'the strain-free six-membered ring' in the section whose thesis is that planar cyclohexane is strained.
- **Chosen intervention** — `sufficient-alt-text` on the **figure** surface
- **Why this is the least-complex option that fully addresses it** — The figures are correct skeletal drawings; only the descriptions overclaim. Saying what the drawing is without asserting a geometry fully resolves it, and no figure change is warranted.
- **Source findings** — instr-017, vis-002

#### rec-020 — Further-reading targets do not differ from one another (medium)

- **Need** — Three of six Wikipedia links point at the identical URL under three different titles, and the single McMurry link goes to the chapter opener rather than to any specific section. A student who clicks 'Background reading on Substituted cyclohexanes' after failing that section lands where 'The chair conformation' already sent them.
- **Chosen intervention** — `prose-edit` on the **prose** surface
- **Why this is the least-complex option that fully addresses it** — The standing repo rule is 1-6 specific OpenStax section links per chapter, and this chapter has none; candidate-and-verify section links plus distinct Wikipedia targets is bounded link editing with no schema impact.
- **Source findings** — struggle-016

#### rec-021 — The video brief makes colour the sole carrier of the axial/equatorial distinction (low)

- **Need** — The storyboard says 'mark the axial and equatorial hydrogens in two colors' with no second channel, and the narration_outline describes concepts rather than the visual changes, so narration alone would not convey which positions moved. Both compiled video blocks are is_hidden with an empty url, so no learner is affected today.
- **Chosen intervention** — `instructor-note` on the **instructor-support** surface
- **Why this is the least-complex option that fully addresses it** — The asset does not exist yet, so this is a production constraint to record rather than a defect to repair. Recording it now is what prevents the single-channel encoding from being built in.
- **Source findings** — vis-012, access-010

#### rec-022 — Reader heading levels skip a rank and the answer-choice group does not behave as the radiogroup it announces (low)

- **Need** — TopicPackageChapterRenderer emits h1/h2 and every figure card emits h4, so no h3 is ever produced and heading navigation reports a gap in all six sections. SelectedResponseRenderer gives each option role=radio inside a role=radiogroup with no roving tabindex or arrow-key handling. Neither blocks completion.
- **Chosen intervention** — `instructor-note` on the **instructor-support** surface
- **Why this is the least-complex option that fully addresses it** — Both are platform-wide renderer defects affecting every chapter, not ch4 authoring; fixing them here would be an undisclosed cross-chapter change. Recorded for the accessibility backlog.
- **Source findings** — access-012, access-009

### Merged duplicates

Findings from different personas anchored to the same location, consolidated keeping the strongest severity and every learner impact:

- **rec-001** (blocker) merges instr-001, instr-002, struggle-017 — A verified chemistry correction lives only in the build artifact and the next recompile deletes it.
- **rec-002** (blocker) merges vis-001, struggle-001, instr-004, access-001, vis-007, struggle-014, vis-002 — The chapter's entire subject — chair geometry — is never drawn.
- **rec-004** (high) merges access-006, struggle-006 — Seven level-1 hints state the answer, and several items have no second rung.
- **rec-005** (high) merges instr-007, struggle-008 — The chapter states the 1,3-diaxial counting rule three ways and one of them is wrong.
- **rec-006** (high) merges instr-008, struggle-007 — Question feedback switches to kcal/mol against kJ/mol prose, and one number collides.
- **rec-007** (high) merges vis-003, access-004, instr-005, vis-010, struggle-019 — The cis/trans figure reaches no learner, and the surviving figure's description claims stereochemistry it does not carry.
- **rec-008** (high) merges access-005, vis-004, vis-005, instr-003 — The ring-flip energy profile renders nothing, and the alt text standing in for it is wrong.
- **rec-009** (high) merges access-003, instr-017, vis-010 — Not one of the nine assets carries a long_description.
- **rec-010** (high) merges instr-009, struggle-009 — Two items are graded on a concept taught one section later.
- **rec-011** (high) merges instr-012, access-008 — Both chair workspace items are answerable by accepting the interface default.
- **rec-012** (medium) merges instr-010, vis-008, struggle-015, access-011 — Both matching items are answerable without reading a structure.
- **rec-013** (medium) merges instr-011, instr-016, vis-011 — The nomenclature objective names a decision the assessment never exercises.
- **rec-014** (high) merges struggle-010, access-002, struggle-014 — Faces and axial/equatorial are taught in separate sections and never reconciled.
- **rec-015** (high) merges instr-006, struggle-005 — Six practice checks, six trouble spots and every learning objective reach no reader surface.
- **rec-018** (medium) merges struggle-012, instr-013, instr-015 — Terms carried from earlier chapters are load-bearing but never glossed.
- **rec-019** (medium) merges instr-017, vis-002 — Small-ring alt text asserts the planar geometry the surrounding prose is arguing against.
- **rec-021** (low) merges vis-012, access-010 — The video brief makes colour the sole carrier of the axial/equatorial distinction.
- **rec-022** (low) merges access-012, access-009 — Reader heading levels skip a rank and the answer-choice group does not behave as the radiogroup it announces.

### Retained disagreements

#### Does the total absence of any chair depiction block publication?

- **Learner with Visual Preference** — Blocker (vis-001). 'A student who does not already hold the chair in their head has no external representation to build one from... The first chair drawing they encounter is inside a graded question widget.' Scored the chapter 3.4.
- **Struggling Student** — Blocker (struggle-001). Three of six sections and four of ten graded items reason about chair geometry that is depicted nowhere; 'at that point I stop reading and start guessing.' Scored 4.6.
- **Accessibility Persona** — Explicitly not a blocker. 'No required activity is impossible for any learner here, so I raise no publication blocker; the barriers are to learning, not to answering.' Filed the same evidence as access-001 at `high`, and scored the chapter 6.8 — the highest of the four.
- **Organic Chemistry Instructor** — High, not blocker (instr-004). Blocked instead on the source/compiled drift and the untier-ed strain claim.

**Resolution.** Kept as a blocker, and the accessibility persona's dissent is upheld on its own terms rather than overruled. The two positions are answering different questions: Accessibility asks whether any learner is barred from completing a required activity (they are not — every item is answerable from text, which is why this chapter escapes the `blocked` verdict its siblings receive), while Visual and Struggling Student ask whether the chapter teaches what it claims to teach. On the second question the evidence is overwhelming and was found independently three times, so readiness is `major revision`. Crucially, the dissent changes the verdict: with no required-access blocker, the computed ceiling is `major revision` and not `blocked`.

#### What to do about the four byte-identical repeated figure blocks.

- **Learner with Visual Preference** — vis-006, medium: 'identical repeats should be reduced rather than multiplied' — repetition without variation trains students to stop looking at the figures.
- **Accessibility Persona** — Did not file it, and its access-003 logic cuts the other way: each rendered block is an independent text equivalent for the section it sits in, so removing one removes that section's only figure description.

**Resolution.** Neither deletion nor duplication. Resolved through rec-002 instead: the repeated structure in each later section is replaced by a figure carrying the marking that section's argument actually needs (the axial/equatorial labelling, the two competing chairs, the diaxial contact). That satisfies the visual persona's objection to information-free repetition while preserving a per-section text equivalent, which is what the accessibility position protects.

#### Whether the hidden, unproduced ring-flip video blocks are a live defect.

- **Learner with Visual Preference** — vis-012, low, and explicitly scoped as 'a forward-looking constraint on production rather than a current on-screen defect'.
- **Accessibility Persona** — access-010, medium, same framing: 'The video is unproduced and both compiled video blocks carry url: "" with is_hidden: true (which ReaderBlockRenderer honours), so no learner is affected today.'

**Resolution.** No disagreement on the facts, and both personas correctly refuted the 'dead media affordance' claim that was raised and rejected on identical evidence in ch28 and ch31 — block-level is_hidden is honoured at [internal source reference — not in this repo] before the switch. Retained at the lower severity as a production constraint (rec-021), not a current defect.

### Places where a description is sufficient (no new asset)

- The seven flat `molecule` assets are correct skeletal drawings and need no replacement — only rec-019's description edits and rec-009's long descriptions.
- mol-cyclopropane's alt text ('a triangle of three carbon atoms') is accurate: cyclopropane genuinely is planar, so unlike cyclobutane and cyclopentane it needs no geometric hedge.
- The two comparison_matrix items are the right shape for a shaky student and their cell-level explanations already point at physical causes; no change needed.
- ComparisonMatrixRenderer's table markup (scope=col/scope=row headers plus a per-cell aria-label) is already a well-formed non-visual equivalent for a comparison grid.
- The chair items' answer-key shape (expected_orientations with position + orientation) correctly matches ChairGrader's placement-equivalence mode; the defect in rec-011 is the interface default, not the key.
- Both short_answer answer_text lists already accept reasonable spelling variants; no grading-tolerance change is needed.

### Visual opportunities

- rec-002 — chair geometry, the axial/equatorial families and the ring flip's positional exchange (blocker; three personas independently).
- rec-007 — a drawn cis/trans wedge-and-dash pair, since the authored one never reaches the reader.
- rec-008 — the ring-flip energy ordering as a shape rather than three numbers in a sentence.
- rec-016 — a 1,3-disubstituted worked case, where the cis/trans-to-axial/equatorial mapping inverts.
- The ring-strain comparison across four ring sizes is non-monotonic (115, 110, 26, 0 kJ/mol) and that shape is lost when the numbers stay in prose (vis-009).
- The ring-versus-chain parent decision is the nomenclature section's hard case and has no figure, while the two trivial cases have one each (vis-011).

### Consensus strengths

- Zero wrong structures and zero wrong answer keys at baseline: 13/13 SMILES and 20/20 keys verified independently, including the formula-identical C7H14 and C8H16 traps.
- Every quantitative claim in the prose survives machine checking, and the half-chair is described correctly and non-trivially as four ADJACENT coplanar carbons — the detail most treatments get wrong by saying five.
- The `expanded` tier is a true superset of `standard` in all six nuggets, so nothing taught at standard depth is lost to the reader's default tier. All four personas noted this independently.
- Every question type has a genuine non-pointer response path — rank_order is move-up/move-down buttons, categorize and matching are labelled selects, and the chair workspace ships a ring-position/orientation select table beside the clickable diagram. There is no drag-only or pointer-only entry anywhere in the chapter.
- No accessible_description in the 20-question bank leaks its answer, including the two chair items, whose descriptions say 'in its most stable orientation' and avoid the word equatorial.
- Sections are short and evenly sized, each opens with a concrete topic sentence and ends by pointing forward, so a struggling reader always knows why the current section exists.
- ch4-ring-flip-multi is a genuinely well-built item: it separates what the flip changes from what it preserves, and its distractors name the two real misconceptions rather than restating the key.

### Regression targets for next run

Recheck these stable `finding_id`s after revision: `instr-001`, `instr-002` (source/compiled drift and the untier-ed strain claim); `vis-001`, `struggle-001`, `instr-004`, `access-001` (chair depiction); `struggle-018` (naming prompts contain their answers); `access-006`, `struggle-006` (hint ladders); `instr-007`, `struggle-008` (1,3-diaxial count); `instr-008`, `struggle-007` (unit collision); `vis-003`, `access-004` (dropped cis/trans asset); `access-005`, `vis-004`, `vis-005` (energy-profile description and spec); `access-003` (long descriptions); `instr-009`, `struggle-009` (concept tagging); `instr-012`, `access-008` (chair default answer).

> Platform-level findings that no chapter edit can clear, and that should be diffed against the next chapter rather than this one: `instr-006`/`struggle-005` (practice_check, trouble_spots and learning_objectives reach no reader surface — now recorded identically for ch27, ch30, ch31 and ch4); `vis-008`/`struggle-015`/`access-011`/`instr-010` (`structure_smiles` is read by no question renderer — recorded for ch27 and ch31); `access-007` (`accessible_description` is consumed only by ReactionCoordinateQuestionRenderer); `vis-003`/`access-004` (`stereochemistry_conversion` has no reader block mapping — first recorded for ch25); `access-012`/`access-009` (heading-rank skip and radiogroup behaviour).

---
## Post-correction record

**Estimated state: ready with minor revisions (not a second persona verdict).**

Not a new persona verdict. All four baseline blockers are closed and machine-verified, and no required-access blocker was ever raised for this chapter — uniquely in this family, because ch4 authors no structure_scaffold item, so the standing input-path ticket that holds ch1/11/15-19/23/25-28 at `blocked` does not apply. What keeps it from `ready` is that every remaining high-severity item is a platform gap no chapter edit can clear: `structure_smiles` renders in no question renderer, `practice_check`/`trouble_spots`/`learning_objectives` reach no reader surface, `accessible_description` is read by one renderer, and a conformational profile still draws no diagram. A new verdict requires a separate four-persona regression run.

### Changes applied

- Back-ported the verified ring-strain correction from the compiled reader into topic.package.json, where it had never existed, and extended it to the `standard` tier which neither file carried: cyclobutane is now stated to retain about 110 kJ/mol of strain, nearly cyclopropane's 115, against cyclopentane's 26, replacing "leaving moderate net strain". Confirmed after recompiling that the sentence now originates in the source rather than surviving only in the build artifact.
 - _resolves_ `instr-001`, `instr-002`, `struggle-017`

- Built and wired four new `diagram` figures, all drawn from the diamond-lattice chair model in `[internal source reference — not in this repo]chair-axial-equatorial.svg` (the chair with all twelve C–H bonds, six axial solid/vertical alternating up at C1,C3,C5 and down at C2,C4,C6, six equatorial dashed and splayed), `chair-ring-flip.svg` (the same molecule before and after a flip, showing orientation inverting while face is preserved), `methylcyclohexane-two-chairs.svg` (the two chairs with the two 1,3-diaxial contacts numbered and the 3.8 + 3.8 = 7.6 kJ/mol arithmetic shown), and `cis-trans-dimethylcyclopentane.svg` (the wedge/wedge and wedge/dash pair). New builder `[internal source reference — not in this repo]vis-001`, `struggle-001`, `instr-004`, `access-001`, `vis-007`, `struggle-014`, `vis-002`, `vis-003`, `access-004`, `instr-005`, `vis-006`; _partially addresses_ `vis-009`, `vis-011`

- De-leaked both nomenclature short-answer prompts. The structural gloss now describes the skeleton without naming its parts — "a six-membered carbon ring carrying a single one-carbon branch" and "a three-membered carbon ring carrying a single two-carbon branch" — so a text-only reader can still answer while the item once again measures naming. The matching accessible_descriptions were reworded the same way.
 - _resolves_ `struggle-018`

- Rewrote the seven answer-giving level-1 hints and added second rungs, taking the bank from 24 hints to 30. Level 1 now redirects attention ("Draw the trans isomer in one chair, label each methyl axial or equatorial, then flip the ring and label them again") and level 2 narrows without stating the count. The chair, equatorial-count, conformer-rank, methylcyclohexane-chair and cis-trans-sort items are all covered.
 - _resolves_ `access-006`, `struggle-006`

- Corrected the 1,3-diaxial miscount. `ch4-chair-tbutyl` hint level 2 said the partners were "three carbons away", which points at C4 — the one position with no 1,3-diaxial relationship to C1. It now reads "the axial hydrogens on C3 and C5 — two carbons away on each side, which is what the name 1,3-diaxial records", matching the prose and the other hint.
 - _resolves_ `instr-007`, `struggle-008`

- Normalised energy units. All four question feedbacks that used bare kcal/mol now lead with the kJ/mol value the prose uses and carry the kcal figure as an explicit parenthetical: cyclobutane 110 kJ/mol (26 kcal/mol), the flip barrier 45 kJ/mol (about 10 kcal/mol), the methyl penalty 7.6 kJ/mol (about 1.8 kcal/mol), tert-butyl about 20 kJ/mol (nearly 5 kcal/mol). This clears the collision in which the numeral 26 named cyclobutane in the feedback and cyclopentane in the reading.
 - _resolves_ `instr-008`, `struggle-007`

- Rewrote the ring-flip energy profile's description, which is the whole figure because the block renders no diagram. It had called the middle region a "twist-boat/boat plateau"; it now walks all seven stationary points with their energies and states that the boat at about 29 kJ/mol is a local MAXIMUM between two twist-boat minima at about 23. The spec's degenerate low/medium/high buckets, which would have plotted boat and twist-boat at the same height, were replaced with exact fractions of the 45 kJ/mol barrier (0.0 / 0.51 / 0.64 / 1.0), and a caveat records that this is the ring-flip pathway and not a torsional scan.
 - _resolves_ `access-005`, `vis-005`; _partially addresses_ `vis-004`, `instr-003`

- Authored an `accessibility.long_description` for all thirteen assets, where previously none of the nine had one, so every figure now carries the chemistry it was placed there to teach instead of a polygon count. Also stopped four alt texts overclaiming: cyclobutane and cyclopentane are no longer described as a "square" and a "pentagon" in the section explaining that both pucker, and the two plain-bond disubstituted structures now say explicitly that they specify no stereochemistry rather than asserting that "cis and trans configurations exist".
 - _resolves_ `access-003`, `instr-017`, `vis-010`

- Added the two rules that existed only inside a hint or a distractor explanation. `nugget-axial-equatorial` now separates face from orientation explicitly — a flip changes axial/equatorial every time and can never change which face a group is on, because nothing in a flip breaks a bond — and states that the equatorial chair is always the favoured one, so the two items tagged to that concept are derivable from it. `nugget-substituted` now gives the generalisable adjacent-carbon rule (a cis pair must be one axial and one equatorial; a trans pair is both-axial or both-equatorial) and warns that the mapping inverts for 1,3-related carbons.
 - _resolves_ `struggle-010`, `access-002`, `instr-009`; _partially addresses_ `struggle-009`, `instr-014`

- Glossed the four terms used at default reading depth without definition — the gauche interaction of butane, steric strain, the Newman projection, and flagpole hydrogens — and derived the axial penalty rather than asserting it: an axial methyl has exactly two gauche-type contacts, one to C3 and one to C5, and 2 × 3.8 = 7.6 kJ/mol is the observed value. Added `butane-conformations` to the `substituted-cyclohexanes` prerequisites, which the gauche analogy assumes and which resolves in the alkanes package.
 - _resolves_ `struggle-012`, `instr-013`, `instr-015`

- Replaced `ch4-chair-tbutyl-v2`, whose answer was the interface's resting state. It was "place the isopropyl group in its most stable orientation" keyed to equatorial, which ChairPlacementRenderer pre-selects. It is now cis-1-tert-butyl-4-methylcyclohexane, where the cis-1,4 relationship forces exactly one group axial and the student must decide which — testing the size-weighting the chapter states but never exercised. Verified against the real ChairGrader: the correct placement scores 1.0, a ring-rotated equivalent scores 1.0, and the swapped assignment, the naive both-equatorial answer and accepting the single default all score 0.0.
 - _resolves_ `instr-012`, `access-008`; _partially addresses_ `struggle-020`, `instr-014`

- Flagged the ring-versus-chain naming convention. The chapter taught larger-fragment-wins as absolute while illustrating it with the one case where current IUPAC recommendations reverse the answer; it now says so, and tells the student a PubChem or ChemDraw lookup returning butylcyclopropane is a convention difference rather than an error.
 - _resolves_ `instr-016`; _partially addresses_ `instr-011`

- Set an explicit verified `wikipedia_title` on all six concepts. Three previously resolved to the same Cyclohexane conformation article under three different names, and recompiling revealed that the remaining ones were being derived from concept titles and would have shipped two 404s (Naming_cycloalkanes, The_chair_conformation_of_cyclohexane). The six targets are now distinct and all resolve, with `Ring flip` and `A value` carrying genuinely different material for the flip and substituted-ring sections.
 - _resolves_ `struggle-016`

- Reconciled the asset-to-nugget links in both directions after the figure rewiring, so no asset claims a section that does not render it and no section references an asset that does not claim it. `mol-methylcyclohexane` had declared three nuggets while appearing in one. Also corrected the two matching items' accessible_descriptions, which promised "three rendered cycloalkane structures" that no renderer draws.
 - _resolves_ `access-011`; _partially addresses_ `vis-008`, `struggle-015`, `instr-010`

### Verification

- Topic-package compiler (proprietary toolchain, not in this repo) — clean
- Automated test suite — 184 passed
- Proprietary toolchain verification (not in this repo)
- RDKit read-back on the cis/trans figure — cis C[C@H]1CCC[C@H]1C is (R,S), meso, same face; trans C[C@H]1CCC[C@@H]1C is (S,S), not meso, opposite faces; both C7H14; the drawn wedge codes read back to the intended isomers
- ChairGrader replay on the rewritten chair item — correct placement 1.0, ring-rotated equivalent 1.0, swapped assignment 0.0, both-equatorial 0.0, accepting the interface default 0.0
- Live HTTP check of all 7 compiled external links — 7/7 return 200, 6 distinct Wikipedia targets
- Compiled reader audit — 5 of 5 image blocks resolve to a real URL (0 empty), 13 of 13 assets carry a long_description, asset/nugget links agree in both directions, 0 dangling asset references
- Rasterised all four SVGs at 1.4x and inspected them; two rounds of layout corrections applied for clipped labels and overlapping text before acceptance
- git diff of the aggregate catalogs (deck-creator/manifest.json, reader/topic-chapters/catalog.json) — changes confined to this chapter's own rows plus a regenerated timestamp; no unrelated churn

### Still recommended

- rec-012 / vis-008, struggle-015, access-011, instr-010 — PLATFORM: `structure_smiles` is read by no question renderer (MatchingRenderer, SelectedResponseRenderer and ComparisonMatrixRenderer all key off `imageUrl`), so six items' authored structures reach nobody. Descriptions were corrected; the items still cannot assess structure-reading. Recorded identically for ch27 and ch31.
- rec-015 / instr-006, struggle-005 — PLATFORM: six `practice_check` items, six `trouble_spots` and every `learning_objective` compile into no reader block, so the chapter's entire formative layer is unreachable. Same gap recorded for ch27, ch30 and ch31.
- access-007 — PLATFORM: `accessible_description` is consumed only by ReactionCoordinateQuestionRenderer, so all 20 authored descriptions reach no learner on this chapter's nine question types. Harmless here only because every prompt is self-describing.
- rec-008 residual / vis-004, instr-003 — PLATFORM: a `conformational_energy_profile` still renders no diagram, because the reader inlines a spec only when it carries `steps` and `minima_labels`. The description now carries the full argument, but routing this kind through `teaching_asset` (as synthesis_roadmap, newman_projection and orbital_overlay already are) would make it draw with no re-authoring.
- rec-016 / instr-014 — the 1,3 and 1,4 disubstituted patterns are now stated as a rule in prose but still have no worked case and no assessment item; bank expansion needs sign-off.
- rec-013 residual / instr-011 — no nomenclature item presents a compound where the chain outranks the ring, so 'the ring is always the parent' still scores full marks on all four naming items.
- rec-021 / vis-012, access-010 — the unproduced ring-flip video brief still encodes the axial/equatorial distinction in colour alone and its narration outline describes concepts rather than the visual changes. No learner is affected today (both blocks are `is_hidden` with an empty url) but the constraint should reach production.
- rec-022 / access-012, access-009 — reader heading levels skip h3 in every section and the answer-choice radiogroup has no roving tabindex or arrow-key handling. Platform-wide, not ch4.
- access-009 residual — ChairPlacementRenderer puts twelve invisible positional buttons ahead of the explanatory text and the select table that is the declared non-visual response path, with no skip.

> The baseline verdict at the top of this file is unchanged. This record describes what
> was corrected afterwards; only a new four-persona regression run can issue a new verdict.
