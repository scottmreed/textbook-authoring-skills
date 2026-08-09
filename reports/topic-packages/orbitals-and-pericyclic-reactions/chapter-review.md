# Chapter review — Orbitals and Organic Chemistry: Pericyclic Reactions (`orbitals-and-pericyclic-reactions`)

_Reviewed 2026-07-31 · chapter version 1 · personas: Instructor, Struggling Student, Accessibility, Visual Preference_

**Publication readiness: major revision**

The chemistry is the strongest part of this chapter and none of the four reviewers could break it: every SMILES, every stereochemical claim, all four canonical electrocyclic results, the endo assignment by 3D test, and all 22 answer keys verified correct, and the instructor called the accuracy the best in the series. The accessibility review scored it 8.3 and the highest in this package family, singling out the decision to carry the polyene molecular orbitals as a prose rule rather than an inaccessible picture. What holds the chapter back is the delivery of that chemistry, in two distinct ways. First, a blocker: the reader defaults to the expanded detail tier, and this chapter's expanded tier was authored as commentary on the standard tier rather than as a self-contained treatment, so a student on default settings is never given the definitions of conrotatory, disrotatory, HOMO, LUMO, suprafacial, antarafacial, the [i,j] counting rule, the 4n versus 4n+2 statement, or even the definition of an electrocyclic reaction - section 5 opens by advising against memorising a table the student has never seen. Second, and agreed by three personas independently, the object every prediction is read off - the two terminal lobes of a polyene frontier orbital - is depicted nowhere, and neither is the rotation the rules predict, the endo/exo stacking, the chair transition state, or the s-cis gate; the five video briefs that would have carried the motion are all deferred and compile hidden. Underneath both sits a pipeline gap the chapter cannot author around: thirty authored trouble spots and ten worked practice_checks never reach the reader at all. Verified errors were corrected in this pass, including two question items that asserted a thermal four-electron ring closure the chapter's own prose denies - a contradiction introduced when the reaction direction was corrected without grepping the question bank.

### Top blockers

- **[BLOCKER] The default reading path never defines the chapter's own vocabulary** — a student on the reader's default detail tier is never given conrotatory, disrotatory, HOMO, LUMO, suprafacial, antarafacial, the [i,j] rule, or the 4n vs 4n+2 statement; all of them live only in the standard tier. (Struggling Student, `struggle-001`, orbital-symmetry-selection-rules)

### Top 5 recommended changes

1. **The default reading path never defines the chapter's own vocabulary** — A student on the reader's default detail tier is never given the definitions of conrotatory and disrotatory, HOMO and LUMO spelled out, suprafacial and antarafacial, the [i,j] counting proce… → **prose-edit** (prose, blocker)
2. **The object every prediction is read off is never depicted** — The chapter's whole predictive chain runs through the sign relationship of the two terminal lobes of butadiene psi-2 and hexatriene psi-3, and no figure anywhere shows a polyene orbital with… → **new-figure** (figure, high)
3. **Conrotatory versus disrotatory motion is carried only by two similes** — The rotation the entire selection-rule apparatus predicts is never shown. The section's nine figures are all starting materials or products; the only planned depiction is a deferred video wh… → **static-image-sequence** (figure, high)
4. **The two drawing questions cannot autograde the stereochemistry they exist to assess** — A wrong-diastereomer submission returns requires_manual_review and is escalated to status manual_review with no score; a correct-skeleton-no-stereochemistry submission returns 'unsupported'.… → **instructor-note** (instructor-support, high)
5. **The typed-structure route cannot express or confirm the feature it is graded on** — Both drawing items allow typed entry, but the typed read-back calls describeStructure at a skill level whose summary emits no stereochemistry, so the answer key and the graded distractor pro… → **text-equivalent** (assessment, high)

### Persona status cards

| Persona | Score | Blockers | Findings | Headline |
|---|---|---|---|---|
| Organic Chemistry Instructor | 7.6/10 | 0 | 14 | Chemistry is the best in the series and unbreakable; delivery of it is what holds the chapter back. |
| Struggling Student | 5.2/10 | 1 | 12 | The scaffolding exists in the package and almost none of it reaches me; I would stall in section 3. |
| Accessibility Persona | 8.3/10 | 0 | 12 | The most accessible chapter in this family, accessible by design; the one real gap is a feedback loop, not a missing route. |
| Learner with Visual Preference | 6.0/10 | 0 | 15 | Unusually well written and unusually poorly seen — the least illustrated chapter relative to what it asks a learner to picture. |

### Affected sections & assets

**Sections/concepts:** `cope-and-claisen-rearrangements`, `cycloaddition-reactions`, `diels-alder-stereochemistry`, `electrocyclic-reactions`, `homo-lumo-and-fmo-theory`, `nugget-electrocyclic-reactions`, `nugget-orbital-symmetry-selection-rules`, `nugget-pericyclic-reaction-basics`, `nugget-pi-molecular-orbitals`, `orbital-symmetry-selection-rules`, `pericyclic-reaction-basics`, `pericyclic-reactions-in-biology`, `pi-molecular-orbitals`, `sigmatropic-rearrangements`

**Assets:** `mol-5-methylcyclopentadiene`, `mol-7-dehydrocholesterol`, `mol-butadiene`, `mol-endo-norbornene-anhydride`, `mol-prephenate`, `orb-benzene-pi-cloud`, `orb-carbon-p-orbital`, `orb-carbonyl-pi-star`, `orb-ethylene-pi`, `rcd-diels-alder-concerted`, `rxn-cope-divinylcyclobutane`, `rxn-electrocyclic-4pi-thermal`, `rxn-vitamin-d-ring-opening`

**Questions:** `ch30-draw-photochemical-closure`, `ch30-draw-photochemical-closure-v2`, `ch30-electrocyclic-ring-size-sort`, `ch30-electrocyclic-ring-size-sort-v2`, `ch30-endo-adduct-statements`, `ch30-fmo-role-match`, `ch30-selection-rules-matrix`, `ch30-selection-rules-matrix-v2`, `ch30-sigmatropic-order`, `ch30-triene-filled-pi-mos`

### Consensus strengths

- Chemical accuracy verified independently by two reviewers against RDKit and PubChem: all 36 assets' structures, the five biological molecules by InChIKey, the endo adduct by 3D geometry, all four canonical electrocyclic results with their meso/racemic analysis, and all 22 answer keys.
- Every one of the 36 assets carries both a content-bearing alt_text and a substantial long_description, and the reader renders those descriptions as visible body text rather than screen-reader-only strings - so where a picture is missing or unreadable, the words usually are not.
- All 11 surfaced questions are answerable from text alone, all 66 hints are text or worked_step, every concept retains at least one keyboard-complete question, and both drawing items allow typed entry with a gradeable SMILES key. No answer leaks in any of the 22 accessible descriptions.
- The chapter is honest about its own model boundaries: frontier theory named as an approximation, the secondary-orbital account for endo selectivity flagged as contested, every orbital figure labelled a qualitative cartoon rather than a computed wavefunction, asynchronous carefully separated from stepwise, and the decision not to draw the polyene orbital sets stated openly instead of quietly omitted.
- It holds the line between what symmetry decides (the motion) and what thermodynamics decides (the direction) throughout, including the harder and more honest choice of showing the four-electron case as the ring OPENING that heat can actually drive rather than the tidy closure most treatments draw.
- The trouble_spots and the question feedback are unusually precise about the actual mistake rather than the topic, and the wrong-answer explanations teach rather than scold.

---
## Full evidence

### Independent persona reports

The four reviews were produced in isolation — each subagent received only its own rubric and never saw another persona's prompt or findings. They are presented separately below and were merged only at synthesis. The verbatim envelopes are preserved in [`persona-reviews.json`](persona-reviews.json).

#### Organic Chemistry Instructor — 7.6/10

persona_version 1.0.0 · publication_blockers: none_

Go, with reservations - I would assign the reading as it stands and I would not yet assign the question set unsupervised. The chemistry is the strongest part of this chapter and I could not break it: every molecule and reaction SMILES verified with RDKit, including the three that usually go wrong. 7-Dehydrocholesterol is (3S,9S,10R,13R,14R,17R,20R); previtamin D3 and vitamin D3 both reproduce exactly the sp3 configuration obtained by performing the ring opening and the [1,7] shift as graph edits on that verified 7-DHC, and vitamin D3 comes out (3S,5Z,7E); chorismate is (3R,4R) and the prephenate given is the suprafacial product of it; the cyclopentadiene/maleic anhydride adduct is genuinely endo by 3D test, not merely labelled endo; every cis/trans cyclobutene and cyclohexadiene, every selection-rule statement, and every answer key checked is right. Sequencing is sound and the trouble_spots are unusually well chosen. What holds it back is not chemistry but delivery of the chemistry. The entire chapter reasons about the terminal lobes of one molecular orbital, and no figure shows a polyene molecular orbital or the conrotatory-versus-disrotatory motion; the only planned visuals for those are video briefs that compile to hidden blocks. The chapter's own opening promise of a single unifying principle stated at the end is never kept, and the bridge that would deliver it (disrotatory is suprafacial, conrotatory is antarafacial) is never stated. And the two structure-drawing questions cannot autograde the stereochemistry they assess: the grader returns manual review with no score for the very epimer the question is built to catch.

**Strengths**

- Chemical accuracy is the best in this series; every machine-checkable structure is right, including 7-dehydrocholesterol, previtamin D3, vitamin D3, chorismate, prephenate and the genuinely-endo adduct.
- All four canonical electrocyclic results are correct and correctly paired with their diastereomers, and the meso/racemic analysis is right.
- Every answer key checked is correct, including the thermal/photochemical matrix, the four-cell rotation-mode matrix and both reactivity rankings.
- The trouble_spots are unusually well chosen and are the real ones.
- The chapter distinguishes cleanly and repeatedly between what symmetry decides (the motion) and what thermodynamics decides (the direction).
- Honesty about model boundaries is exemplary: frontier theory named as an approximation, the secondary-orbital account flagged as contested, the orbital figures labelled qualitative cartoons, asynchronous separated from stepwise.
- Prerequisites form a correct acyclic ordering, and the biology section is load-bearing rather than decorative.

**Findings**

##### `inst-001` — HIGH · visual-opportunity · confidence 0.93

- **Location:** concept_slug=`pi-molecular-orbitals` · nugget_id=`nugget-orbital-symmetry-selection-rules`
- **Anchor:** "Which motion occurs is decided by the terminal lobes of the frontier orbital."
- **Observation:** Every predictive argument in the chapter runs through the sign relationship of the two terminal lobes of a polyene frontier orbital, and no figure shows a polyene molecular orbital or those terminal lobes. The four orbital_overlay assets are a single carbon p orbital, the ethylene pi bond, a carbonyl pi*, and the benzene pi cloud. None is psi-1..psi-4 of butadiene or psi-1..psi-6 of hexatriene, which are the orbitals the chapter reasons with in sections 2, 3, 4 and 5.
- **Learner impact:** The chapter's remedy is a counting rule applied in prose. A student who cannot already picture a four-lobe alternating orbital has nothing to check that sentence against, so the counting rule degrades into a memorised parity trick - exactly the failure the concept's first trouble_spot warns about. It lands hardest on anyone who reasons visually.
- **Evidence:** nugget-pi-molecular-orbitals expanded tier concedes the gap explicitly. The package's own OpenStax link for 30.1 says the same from the other side. orbital-presets.manifest.json offers only six presets (ethene, ethyne, formaldehyde, allyl cation, benzene, ammonia) - no polyene preset exists for such a figure to be built on.
- **Recommended outcome (need):** A student needs to be able to see, not just be told, the phase pattern of psi-2 of butadiene and psi-3 of hexatriene with the two terminal lobes identifiable, so the node-counting rule can be checked against an object rather than trusted.

##### `inst-002` — HIGH · visual-opportunity · confidence 0.94

- **Location:** concept_slug=`orbital-symmetry-selection-rules` · asset_id=`rxn-electrocyclic-4pi-thermal`
- **Anchor:** "conrotatory is two wheels on a shared axle turning together; disrotatory is the two covers of a book opening"
- **Observation:** The conrotatory/disrotatory motion is never depicted. Section 5 carries nine static figures - two dienes, the triene, and the four diastereomeric ring products - every one a starting material or a product, none showing the rotation that connects them. The only asset intended to show the motion is video-conrotatory-vs-disrotatory, emitted with url empty and is_hidden true.
- **Learner impact:** The observable outcome (cis or trans on the ring) is shown and the cause (which way the ends turn) is not. Students learn 'four-electron thermal gives trans' as products rather than as motions - precisely the failure mode the chapter warns against. Any question with inward-pointing terminal substituents will then be answered wrongly with full confidence.
- **Evidence:** Compiled reader section nugget-orbital-symmetry-selection-rules: 12 blocks, the video block {title: 'Watching the ends turn', url: ''} with is_hidden true. All six video blocks are hidden with empty urls.
- **Recommended outcome (need):** A student needs the two rotation modes distinguishable as motions - both ends turning the same way sends one substituent up and one down while opposite senses bring both to one face - inside the section that teaches the rule, without depending on an unproduced video.

##### `inst-003` — HIGH · assessment-readiness · confidence 0.92

- **Location:** question_slug=`ch30-draw-photochemical-closure` · concept_slug=`orbital-symmetry-selection-rules`
- **Observation:** The chapter's only two structure-drawing questions cannot autograde the stereochemistry that is the whole point of them. Both set grading_rules.structure_engine 'rdkit'. A submission of the wrong diastereomer returns status 'partially_correct', score_suggested 1.0, requires_manual_review True, diff_categories ['stereo_mismatch']; StructureGrader maps requires_manual_review to status 'manual_review' with score_given None. A right-skeleton-no-stereochemistry submission returns status 'unsupported' with empty diff_categories.
- **Learner impact:** The two authored wrong-answer explanations that carry the teaching will not be delivered, because neither submission is graded incorrect. A student drawing the trans cyclobutene gets 'Submitted for teacher review' instead of the sentence that would fix the misconception, and an instructor assigning these as self-check homework gets a queue of manual reviews on exactly the item they most wanted automated.
- **Evidence:** Reproduced in the proprietary grading service (not in this repo):
- **Recommended outcome (need):** The chapter's central skill needs an assessment path that returns a verdict and the authored explanation when a student gets the stereochemistry wrong.

##### `inst-004` — HIGH · missing-example · confidence 0.9

- **Location:** nugget_id=`nugget-pericyclic-reaction-basics` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "All three obey a single underlying principle, stated at the end of the chapter"
- **Observation:** The unifying principle the chapter promises in section 1 is never stated. The last section closes on vitamin D and chorismate mutase and states no such principle. The student receives three separately worded rules, and the sentence that welds them into one - that a disrotatory closure IS the suprafacial option and a conrotatory closure IS the antarafacial one - appears nowhere. 'Woodward-Hoffmann rules' never appears in student-facing prose either.
- **Learner impact:** The chapter's three rules look like three unrelated facts to be memorised separately, the opposite of what the chapter sets out to do, and directly undercuts the aim of regenerating the table rather than memorising it. A student meeting a cheletropic reaction, an eight-electron system, or any exam question in the general suprafacial/antarafacial form has no rule to apply.
- **Evidence:** The promise is in nugget-pericyclic-reaction-basics expanded. No nugget delivers it. The concept trouble_spot actively blocks the bridge ('the words conrotatory and disrotatory ... are meaningless for a cycloaddition'). textbook_matching.overrides.openstax note claims 'every numbered section of the chapter is represented by at least one concept', but no concept covers 30.9, A Summary of Rules for Pericyclic Reactions.
- **Recommended outcome (need):** A student needs the chapter to close the loop it opens: one statement, inside the chapter, that makes the three family rules visibly one rule about electron count and facial relationship, with the vocabulary equivalence that makes it work and the name the rest of the world uses. The textbook_matching coverage claim needs to match what is delivered.

##### `inst-005` — MEDIUM · assessment-readiness · confidence 0.88

- **Location:** question_slug=`ch30-endo-adduct-statements` · concept_slug=`diels-alder-stereochemistry`
- **Observation:** Not one question in the chapter shows the student a structure. All 22 items carry representation_tags ['text'] except the two structure_scaffold items, whose 'molecule' tag refers to the student's own canvas rather than a stimulus. Stereochemistry questions are asked entirely from names and condensed formulae.
- **Learner impact:** Every stereochemical question begins with an un-assessed translation step: read a stereodescriptor, build the folded conformer mentally, then apply the chemistry being tested. Students who can do the chemistry but not the translation are scored as if they cannot do the chemistry. The chapter has 25 molecule and 16 reaction figures available to reuse.
- **Evidence:** representation_tags is ['text'] for 20 of 22 items. ch30-dienophile-reactivity-rank describes maleic anhydride in words although mol-maleic-anhydride exists in the same package.
- **Recommended outcome (need):** The stereochemistry and reactivity items need the structures they are about present in the item, so the student is tested on pericyclic reasoning rather than on decoding a name into a three-dimensional arrangement.

##### `inst-006` — MEDIUM · misconception · confidence 0.86

- **Location:** question_slug=`ch30-electrocyclic-ring-size-sort`
- **Anchor:** "Each compound below is offered as a candidate for a single thermal electrocyclic ring closure"
- **Observation:** Two places in the question set treat a thermal four-electron ring closure as something that happens, contradicting the chapter's prose. ch30-electrocyclic-ring-size-sort asks the student to sort buta-1,3-diene and (2E,4E)-hexa-2,4-diene as 'candidates for a single thermal electrocyclic ring closure', and the wrong-answer explanation in ch30-draw-photochemical-closure calls trans-3,4-dimethylcyclobutene 'the product of the thermal closure. Under heat alone a four-electron system closes with both ends turning the same way'.
- **Learner impact:** The chapter teaches that the four-electron system runs in the opening direction thermally and that only light can drive it closed; a student who has absorbed that will find both items incoherent, and a student who has not will believe butadiene cyclises on heating. It weakens the chapter's most useful discrimination - that direction is thermodynamics and rotation mode is symmetry.
- **Evidence:** nugget-electrocyclic-reactions standard: 'cyclobutenes open to dienes rather than the reverse'. nugget-orbital-symmetry-selection-rules expanded: 'light can drive the four-electron system uphill in the closing direction, which heat cannot.' Contrast with the two items named.
- **Recommended outcome (need):** The two items need to stop asserting a thermal four-electron closure - either by framing the ring-size question as counting the ring a closure would give without claiming it is thermal, or by naming the rotation mode rather than a thermal 'product' in the distractor explanation.

##### `inst-007` — MEDIUM · sequencing · confidence 0.82

- **Location:** concept_slug=`electrocyclic-reactions` · asset_id=`rxn-electrocyclic-4pi-thermal`
- **Anchor:** "the next section works out how to predict them"
- **Observation:** Two sections carry figures whose titles and long descriptions deliver the following section's content. rxn-electrocyclic-4pi-thermal is titled 'Thermal four-electron ring opening: conrotatory' and sits in concept electrocyclic-reactions (order 4); its long_description defines and applies conrotatory motion in full, although conrotatory and disrotatory are introduced in order 5. The same repeats at section 8, which carries the Cope and Claisen figures introduced in order 9.
- **Learner impact:** The section-4 prose deliberately withholds the prediction to set up the payoff, and the figure beside it gives the answer away, so the section-5 derivation arrives as confirmation rather than discovery. In section 8 a student meets 'Cope' and 'Claisen' as unexplained proper nouns one section before they are defined.
- **Evidence:** Compiled reader section nugget-electrocyclic-reactions contains the block 'Thermal four-electron ring opening: conrotatory' whose alt_text reads 'the ends must rotate in the same sense, conrotatory'. Section nugget-sigmatropic-rearrangements contains both [3,3] reaction blocks.
- **Recommended outcome (need):** The withheld result needs to stay withheld until the section that derives it, and section 8 needs sigmatropic figures that do not depend on names section 9 introduces - or the prose needs to stop promising a payoff its own figures have already spent.

##### `inst-008` — MEDIUM · figure-purpose · confidence 0.85

- **Location:** asset_id=`mol-endo-norbornene-anhydride` · concept_slug=`diels-alder-stereochemistry`
- **Observation:** The endo/exo distinction, a whole learning objective, has no figure that can convey it. mol-endo-norbornene-anhydride and the product side of rxn-diels-alder-endo render as flat RDKit depictions in which endo and exo differ only in the wedge-versus-dash sense of four explicit hydrogens. Rendered at reader scale the two diastereomers are visually near-indistinguishable; the picture cannot show what the learning_goal claims.
- **Learner impact:** Endo versus exo is intrinsically about which side of a bridged framework a group sits on, and a flat depiction is the one representation that cannot answer it. The long_description carries the entire teaching load while the figure looks the same as its counterexample. The concept's own first trouble_spot is that students confuse endo with cis - a distinction the figure is powerless to settle.
- **Evidence:** Confirmed by 3D embedding that the anhydride carbonyls sit anti to the CH2 bridge and syn to the alkene bridge (genuinely endo) and that the epimer is exo; rendered as 420x360 PNGs the two differ in bytes but not perceptibly. The planned alternative video-endo-vs-exo compiles to a hidden block.
- **Recommended outcome (need):** A student needs the endo and exo orientations distinguishable at a glance, which means the stacking or the bridged product needs to be shown in a way that carries depth rather than in a flat skeletal projection.

##### `inst-009` — MEDIUM · conceptual-support · confidence 0.84

- **Location:** question_slug=`ch30-sigmatropic-order` · asset_id=`mol-5-methylcyclopentadiene`
- **Anchor:** "bonds to the far end of the diene"
- **Observation:** The chapter describes the same [1,5] hydrogen shift in a cyclopentadiene two incompatible ways and never resolves the tension. ch30-sigmatropic-order says the hydrogen 'leaves the sp3 carbon and bonds to the far end of the diene', while mol-5-methylcyclopentadiene says 'the hydrogen on carbon 5 moves to an adjacent carbon of the diene'. Both are true, but the chapter never says that the [i,j] indices are counted along the array whose electrons move and not through the ring.
- **Learner impact:** A student looking at the ring sees donor and acceptor carbons bonded to each other and reasonably writes [1,2], or counts one intervening atom and writes [1,3]. The distractor list anticipates both, which shows the author expected the error, but the explanation asserts the count without giving the rule that makes it larger than three. This is the most mechanical skill in the section and the one left underexplained.
- **Evidence:** ch30-sigmatropic-order prompt_text versus mol-5-methylcyclopentadiene long_description; the question's wrong_answer_explanations include entries for '[1,3]' and '[1,2]'. The nugget works the count only for the acyclic penta-1,3-diene case, never the ring case the question asks about.
- **Recommended outcome (need):** A student needs it made explicit that the [i,j] count follows the conjugated array that reorganises, not the shortest path through the ring, worked on the cyclopentadiene case itself - and the two descriptions of the same event need to stop contradicting each other.

##### `inst-010` — MEDIUM · missing-example · confidence 0.83

- **Location:** concept_slug=`cope-and-claisen-rearrangements` · asset_id=`rxn-cope-divinylcyclobutane`
- **Observation:** The only Cope rearrangement figure in the chapter is the one case that breaks the chapter's own rule about the transition state. Its long_description states the ring tether forces a boat-like transition state instead of the chair. There is no figure of a plain 1,5-diene Cope, so the chair transition state that the concept teaches as the norm and that ch30-aromatic-claisen-reasoning grades as the one-word answer is never illustrated on a substrate that adopts it.
- **Learner impact:** The student's mental image of a Cope rearrangement is formed by the exception. Worse, ch30-aromatic-claisen-reasoning marks 'boat' wrong while the chapter's only Cope picture is a boat - a student who studied the figure and answers 'boat' is penalised for having read the chapter.
- **Evidence:** rxn-cope-divinylcyclobutane is the only asset with 'Cope' in its title; concept trouble_spot: 'The [3,3] transition state is a chair-like six-membered ring'. ch30-aromatic-claisen-reasoning expected_text ['chair'] with a wrong-answer explanation for 'boat'.
- **Recommended outcome (need):** The chapter needs a Cope example on an ordinary 1,5-diene alongside the ring-expansion special case, so the chair transition state is instantiated somewhere and the divinylcyclobutane boat reads as the exception the prose says it is.

##### `inst-011` — MEDIUM · missing-example · confidence 0.86

- **Location:** concept_slug=`cycloaddition-reactions` · question_slug=`ch30-selection-rules-matrix-v2`
- **Anchor:** "photochemical [2+2] reactions are the standard laboratory route to cyclobutanes"
- **Observation:** The chapter has no [2+2] cycloaddition figure of any kind, although the thermally forbidden / photochemically allowed [2+2] contrast is one of the two pillars of the concept and is assessed directly. Both cycloaddition reaction assets are Diels-Alder reactions. No asset shows two alkenes, a cyclobutane product, or the mismatched orbital overlap.
- **Learner impact:** The most memorable fact in the section - alkenes dimerise in sunlight and not in a hot flask - is text only, and the orbital argument for it has no picture to sit against, in a chapter whose entire method is looking at where lobes point.
- **Evidence:** Of 36 assets the reaction assets are the Diels-Alder archetype, two electrocyclic, the endo Diels-Alder, a Cope, two Claisens and three biology reactions; none is a [2+2]. ch30-selection-rules-matrix-v2 grades case_2plus2 as thermally forbidden and photochemically allowed.
- **Recommended outcome (need):** A student needs the [2+2] case visible - two alkenes, the four-electron array, and the end-to-end sign mismatch that forbids it thermally - since it is the counterexample that gives the [4+2] result its meaning.

##### `inst-012` — MEDIUM · objective-alignment · confidence 0.87

- **Location:** concept_slug=`sigmatropic-rearrangements` · question_slug=`ch30-sigmatropic-order`
- **Observation:** Several stated learning objectives have no surfaced assessment. pi-molecular-orbitals LO2 (draw the phase pattern of pi and pi* of ethylene) is not assessed. sigmatropic-rearrangements LO2 (compute the electron count and use it to decide whether a thermal suprafacial pathway is allowed) and LO3 (why [1,5]-H is common and [1,3]-H is not) are not assessed - the surfaced item asks only for the [i,j] label. cope-and-claisen LO2 (predict the product of a Claisen of an allyl vinyl ether and an allyl aryl ether) is not assessed.
- **Learner impact:** The concepts a student is told to master and the items they practise come apart in three places, on the parts students actually get wrong on exams. With only 11 of 22 items surfaced, most concepts have exactly one live item, so a coverage gap is total rather than thin.
- **Evidence:** compiled question-set counts {questions 22, surfaced 11, staged_variants 11}. ch30-electrocyclic-ring-size-sort-v2 (electron counting) is itself a staged variant and its five items are all electrocyclic.
- **Recommended outcome (need):** The objectives carrying the chapter's transferable skills - sigmatropic electron counting used to decide a pathway, and predicting a Claisen product - need live practice, and the ethylene phase-pattern objective needs either an assessment or removal.

##### `inst-013` — LOW · notation-consistency · confidence 0.9

- **Location:** question_slug=`ch30-electrocyclic-ring-size-sort-v2`
- **Anchor:** "3,4-Dimethylcyclobutene opening to (2E,4E)-hexa-2,4-diene"
- **Observation:** The first item names '3,4-Dimethylcyclobutene' with no cis or trans descriptor while specifying the product as (2E,4E)-hexa-2,4-diene. Only the trans diastereomer gives the E,E diene on conrotatory opening; the cis diastereomer gives (2E,4Z)-hexa-2,4-diene, as the chapter itself is careful to state.
- **Learner impact:** Minor for the electron count being asked, but the chapter has just established that the two diastereomeric cyclobutenes give two different dienes and that this is what makes the experiment diagnostic. Dropping the descriptor in the next item quietly undoes that care.
- **Evidence:** nugget-orbital-symmetry-selection-rules expanded states both pairings explicitly. Assets mol-trans-dimethylcyclobutene and mol-cis-dimethylcyclobutene both exist and are correctly encoded.
- **Recommended outcome (need):** Stereochemical descriptors need to be carried consistently wherever a specific diastereomeric product is named.

##### `inst-014` — LOW · conceptual-support · confidence 0.8

- **Location:** nugget_id=`nugget-cycloaddition-reactions` · asset_id=`orb-benzene-pi-cloud`
- **Anchor:** "Transition states of this kind are described as aromatic"
- **Observation:** The aromatic-transition-state idea is the closest thing the chapter has to the unifying principle it promises, and it appears only in the expanded tier of nugget-cycloaddition-reactions and in the long_description of orb-benzene-pi-cloud. A student reading the terse or standard tier never meets it, and it sits in section 6 rather than where a summary would.
- **Learner impact:** The one explanation that tells a student why 4n+2 is the magic count across all three families - rather than asserting it separately three times - is optional reading attached to a single section.
- **Evidence:** The word 'antiaromatic' occurs exactly once in the whole package, in that paragraph.
- **Recommended outcome (need):** The reason 4n+2 is privileged needs to reach a student on the default reading path and be positioned where it can unify the three families.

**Open questions**

- Which detail tier does the reader render by default? Each compiled text block carries _detail_texts plus a content.markdown holding the expanded text.
- Are the five video_briefs expected to be produced before release to instructors? Three findings are gaps only while they remain unproduced.
- Is a polyene orbital preset on the roadmap? inst-001 may be a platform capability request rather than an authoring gap.
- Could not independently confirm the published InChIKey for cholecalciferol without network access; the verdict rests on deriving it from the package's verified 7-DHC and on RDKit CIP labels.

#### Struggling Student — 5.2/10

persona_version 1.0.0 · publication_blockers: `struggle-001`_

The authored source package is unusually kind to a weak student: every concept carries three named trouble spots, every nugget a practice_check with a worked answer, every question a three-rung hint ladder plus specific wrong-answer explanations, every figure a caption and long description. Almost none of that reaches me. The reader defaults to the expanded detail tier, and in this package expanded is written as commentary layered on standard rather than as a superset, so the default view never defines conrotatory, disrotatory, HOMO, LUMO, suprafacial, antarafacial, the [i,j] numbering rule, or the 4n / 4n+2 rule - it opens section 5 with 'the safest way to use these rules is not to memorise the four boxes' before I have ever met a box. On top of that the 30 trouble spots and 10 practice_checks are dropped by the compiler, all five videos are deferred and hidden, the promised selection-rule table and the closing 'single underlying principle' never appear, and the one picture the chapter turns on is not drawn anywhere while a hint tells me to sketch it. The chemistry and the writing are strong; the delivered chapter is a wall of advanced commentary with the scaffolding stripped out. I would stall in section 3 and start guessing by section 5.

**Strengths**

- Every one of the 22 questions carries a three-rung hint ladder, a generic_incorrect_explanation, and 3-6 targeted wrong-answer explanations keyed to specific submissions; the distractors name actual confusions rather than being filler.
- The wrong-answer explanations teach rather than scold ('that is the right sequence read backwards').
- Every figure carries a learning_goal that compiles into a caption saying what to look at, plus a long_description explaining the structure in words.
- The prose signals importance constantly and honestly, so once I am reading the right tier I can tell what matters.
- The chapter offers a regenerate-it procedure instead of a table to memorise, and warns that the rule predicts a motion and never a product label.
- ch30-dienophile-reactivity-rank describes maleic anhydride in words inside the card text, so the question is answerable as delivered.
- The trouble_spots are unusually precise about the mistake rather than the topic, and would be genuinely useful if a student could see them.

**Findings**

##### `struggle-001` — BLOCKER · conceptual-support · confidence 0.96

- **Location:** section_id=`nugget-orbital-symmetry-selection-rules` · concept_slug=`orbital-symmetry-selection-rules` · nugget_id=`nugget-orbital-symmetry-selection-rules`
- **Anchor:** "The safest way to use these rules under exam conditions is not to memorise the four boxes but to regenerate them"
- **Observation:** The reader's default detail level is expanded, and the compiled chapter's every text block carries content.markdown equal to the expanded tier. In this package the expanded tier is a commentary layer that presumes the standard tier has been read, so on default settings the chapter's core vocabulary is never defined. Verified term-by-term: the definitions of conrotatory and disrotatory, HOMO and LUMO spelled out, suprafacial/antarafacial, the [i,j] numbering procedure, the 4n / 4n+2 rule statement, and the three defining features of a pericyclic reaction all appear only in standard. Every section therefore opens mid-argument, and section 8 delivers the exception before the rule.
- **Learner impact:** A low-confidence student reads five hundred words of caveats about a rule they have never been given, cannot find the definition of the two words the section title asks about, and has no way to know a slider is hiding the explanation. The required step of learning what conrotatory means is genuinely impossible from the delivered default view.
- **Evidence:** Compiled reader: all 10 text blocks have content.markdown == _detail_texts.expanded. useReaderPersonalization default detailLevel 'expanded'. Term presence per tier confirmed across all ten nuggets.
- **Recommended outcome (need):** The default reading path must contain the definitions and base derivations, not only commentary on them - a student who never touches the detail control must still meet conrotatory/disrotatory, HOMO/LUMO, suprafacial/antarafacial, the [i,j] procedure and the 4n vs 4n+2 statement before any section that uses them.

##### `struggle-002` — HIGH · cognitive-load · confidence 0.93

- **Location:** section_id=`nugget-pi-molecular-orbitals` · concept_slug=`pi-molecular-orbitals` · asset_id=`orb-carbon-p-orbital`
- **Anchor:** "the honest representation is the node count and the terminal-lobe rule just given"
- **Observation:** Every prediction is read off one object - the terminal lobes of butadiene psi-2 or hexatriene psi-3 - and that object is never drawn. The four orbital figures are a lone p orbital, ethylene's pi bond, a carbonyl pi* and the benzene cloud; none is a polyene set. The animation that would have carried the motion is deferred and its reader blocks are is_hidden, so turning on 'show videos' does not reveal them.
- **Learner impact:** I cannot integrate a purely verbal instruction about signs on lobes I have never seen arranged in a chain. I would take 'odd nodes means the terminal lobes are opposite' as a fact to memorise rather than a picture to regenerate - precisely the failure the chapter's own trouble spot warns about.
- **Evidence:** Four orbital_overlay assets with manifest_ids p_orbital / pi_bond_alkene / carbonyl_pi_star / benzene_pi_cloud. Six video blocks, all is_hidden true. Hint 1 of ch30-selection-rules-matrix: 'sketch the diene HOMO and the triene HOMO and look at their ends'.
- **Recommended outcome (need):** The chapter's load-bearing object - a polyene pi molecular-orbital set with terminal lobes and node count visible, and the two rotation modes acting on those lobes - needs to be something the student has seen, not only described.

##### `struggle-003` — HIGH · conceptual-support · confidence 0.94

- **Location:** section_id=`nugget-pericyclic-reaction-basics` · nugget_id=`nugget-pericyclic-reaction-basics`
- **Anchor:** "All three obey a single underlying principle, stated at the end of the chapter"
- **Observation:** The chapter makes three forward promises and keeps none. Section 1 promises 'a single underlying principle, stated at the end of the chapter'; the last section closes on metabolism and states none. Section 2 promises the terminal-lobe rule will 'generate the entire table of electrocyclic selection rules in the next section'; no table exists and the platform's ReaderBlockType has no table type. Section 3 says 'the chapter's tables always have two rows' and a trouble_spot warns against 'memorising the four boxes of the table' - referring to an artefact never shown.
- **Learner impact:** I read to the end waiting for the promised principle and finish believing I missed something. When a question asks me to fill a 2x2 matrix I go looking for 'the table', cannot find it, and write the four cells from a half-remembered sentence. There is no consolidated summary to revise from.
- **Evidence:** Compiled reader block census: text 10, molecule 25, reaction 16, reaction_coordinate 2, teaching_asset 7, video 6 (all hidden), external_link 10, mcmurry_link 1 - no table, no callout, no summary.
- **Recommended outcome (need):** The chapter needs to deliver the two things it tells the student to expect - a consolidated selection-rule reference and a closing statement of the unifying principle - or the forward references need to stop promising them.

##### `struggle-004` — HIGH · retrieval-practice · confidence 0.95

- **Location:** section_id=`nugget-orbital-symmetry-selection-rules` · nugget_id=`nugget-orbital-symmetry-selection-rules`
- **Anchor:** "A student runs the reaction of butadiene with ethylene in hexane and then repeats it in dimethyl sulfoxide"
- **Observation:** All ten nuggets carry an authored practice_check with a 150-250 word worked answer, and not one reaches the reader. The compiled chapter has no block containing any practice_check text, no callout blocks, no per-section summary, and exactly one text block per section with no internal heading. The question bank is itself off (available false, demo_eligible 0), so there is no retrieval practice anywhere in the student-facing chapter.
- **Learner impact:** I have no way to find out whether I understood a section before moving to the next one that depends on it, and the dependency chain is total. My confidence tracks how fluent the prose felt rather than what I can do.
- **Evidence:** 10 nuggets each with a populated practice_check; zero occurrences of 'dimethyl sulfoxide' in the compiled reader; zero callout blocks; compiled question-set available false.
- **Recommended outcome (need):** A shaky student needs a retrieval stop inside each section - the authored practice_check content already exists and never reaches them.

##### `struggle-005` — HIGH · misconception · confidence 0.92

- **Location:** concept_slug=`pi-molecular-orbitals` · section_id=`nugget-pi-molecular-orbitals`
- **Anchor:** "Confusing an orbital's phase with an electrical charge"
- **Observation:** The package declares 30 trouble spots, three per concept, and they are the sharpest named-mistake list for this topic. None reaches the reader: the compiled chapter contains no occurrence of any trouble_spot string and has no callout blocks to carry them. What survives is only whatever the author independently wove into the expanded prose, so the phase-is-not-charge warning (its own paragraph in the standard tier) is absent from the default view, as are the conrotatory/disrotatory mix-up and [4+2]-is-not-atoms warnings.
- **Learner impact:** The wrong moves stay available as traps rather than being named and closed off. The phase-as-charge error would silently poison every later section: if I read the lobe colours as charge, 'lobes of the same sign must be brought together' becomes electrostatically absurd. The one mitigation is real - orb-carbon-p-orbital's description carries the correction - but a caption under a figure is not where I look for a warning.
- **Evidence:** 30 trouble_spots across 10 concepts; grep for three of them in the compiled reader returns 0.
- **Recommended outcome (need):** The chapter's named misconceptions need to be visible at the point of risk, not held only in package metadata.

##### `struggle-006` — HIGH · worked-example-gap · confidence 0.9

- **Location:** question_slug=`ch30-selection-rules-matrix` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "sketch the diene HOMO and the triene HOMO and look at their ends"
- **Observation:** The hint ladder on the chapter's central question instructs a stuck student to perform a step the chapter never models. No figure shows a diene or triene molecular orbital, and section 2 explicitly declines to draw one. The comparison_matrix question grades all four cells and the structure_scaffold question grades stereochemistry, so this is where the missing representation becomes a graded failure rather than a reading difficulty.
- **Learner impact:** A hint that tells me to draw something I have never seen drawn does not unstick me, it confirms I am missing a prerequisite everyone else has. I would guess con/dis/dis/con from the shape of the table.
- **Evidence:** ch30-selection-rules-matrix hint[0]; ch30-draw-photochemical-closure hint[1] and wrong_answer_explanations[1]. No asset depicts a butadiene or hexatriene MO.
- **Recommended outcome (need):** The step the hints ask for needs to have been demonstrated in the chapter before it is required under grading; a hint cannot be the first place a representation appears.

##### `struggle-007` — MEDIUM · cognitive-load · confidence 0.87

- **Location:** section_id=`nugget-orbital-symmetry-selection-rules` · nugget_id=`nugget-orbital-symmetry-selection-rules`
- **Anchor:** "It is worth seeing the four canonical results together, because questions are built from them."
- **Observation:** Section 5 is the heaviest in the chapter and has no internal structure: nine assets and one 550-word text block of four unheaded paragraphs, one of which is a single ~330-word paragraph enumerating all four canonical results, then a meso-versus-racemate aside, then a vocabulary caution. The six molecule figures render as a flat vertical stack of six unrelated structures; which pairs with which exists only inside each caption.
- **Learner impact:** Four results, two electron counts, two conditions, two rotation modes, two diastereomer labels plus meso/racemic and a vocabulary warning, all in one undifferentiated block. This is where I would give up on understanding and start memorising - the failure mode the chapter's own trouble spot identifies.
- **Evidence:** nuggets[4] duration_minutes 10, asset_ids length 9, text.expanded 550 words in 4 paragraphs. ReaderBlockType supports 'callout' and TextBlockContent supports 'heading'; neither is used anywhere in this chapter.
- **Recommended outcome (need):** The four canonical results and the six look-alike structures need to be organised for a reader who cannot hold them all at once - segmented, paired, and with the takeaway marked.

##### `struggle-008` — MEDIUM · worked-example-gap · confidence 0.85

- **Location:** question_slug=`ch30-draw-photochemical-closure` · asset_id=`rxn-electrocyclic-4pi-thermal` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "Photochemical closure of (2E,4E)-hexa-2,4-diene is disrotatory and gives cis-3,4-dimethylcyclobutene"
- **Observation:** Of the four canonical results the section says questions are built from, only the two thermal ones have a reaction figure. Neither photochemical result is drawn as a reaction anywhere - the photochemical products exist only as isolated product structures whose captions state what they came from. The chapter then sets an advanced structure_scaffold asking the student to draw the stereochemistry of the photochemical four-electron closure, and grades it.
- **Learner impact:** The thing I need most before drawing a stereochemical product is one fully worked example of that exact transformation. I have two worked thermal examples and am asked to produce a photochemical one.
- **Evidence:** The electrocyclic reaction assets are rxn-electrocyclic-4pi-thermal and rxn-electrocyclic-6pi-thermal only. ch30-draw-photochemical-closure difficulty 'advanced', graded by rdkit.
- **Recommended outcome (need):** The photochemical direction needs a worked example the student can study before it is assessed.

##### `struggle-009` — MEDIUM · retrieval-practice · confidence 0.83

- **Location:** question_slug=`ch30-endo-adduct-statements` · concept_slug=`diels-alder-stereochemistry`
- **Anchor:** "Select every statement that is true of that reaction and its major product."
- **Observation:** The surfaced set is 11 items: 2 core, 6 standard, 3 advanced. Eight of the ten concepts have no core-difficulty question, and two concepts are tested only at advanced: diels-alder-stereochemistry (a five-statement multi_select whose distractors encode the endo-equals-cis conflation and the single-enantiomer error) and cope-and-claisen-rearrangements (a three-field structured_reasoning). For the two hardest sections my first and only practice contact is the hardest item format.
- **Learner impact:** A multi_select where several distractors encode exactly the confusions I hold is a fine diagnostic and a poor first attempt: partial knowledge scores zero and I read that as knowing nothing.
- **Evidence:** Difficulty by concept: core only for pericyclic-reaction-basics (2) and pi-molecular-orbitals (1); diels-alder-stereochemistry advanced x2; cope-and-claisen advanced x2.
- **Recommended outcome (need):** The two hardest concepts need an entry-level rung before their advanced item.

##### `struggle-010` — MEDIUM · conceptual-support · confidence 0.86

- **Location:** concept_slug=`pericyclic-reaction-basics` · section_id=`nugget-orbital-symmetry-selection-rules`
- **Anchor:** "The cis products in both series are meso compounds"
- **Observation:** The chapter states no external prerequisites and offers no route back to them. Every concept's prerequisites point only inside this chapter, yet the default text leans on meso compounds, internal mirror planes, racemic mixtures, enantiomers, E/Z descriptors, s-cis versus s-trans, ring strain, tautomerisation, enol ethers, silyl ketene acetals and the aromaticity argument, with no gloss and no link. The only textbook link is the generic chapter landing page; the per-section 'read more' for section 5 is the Woodward-Hoffmann Wikipedia article, which is harder than the chapter.
- **Learner impact:** When 'meso' appears in the section I am already struggling with, I have no idea whether I am supposed to know it, and the only 'read more' drops me into an article that opens with orbital correlation diagrams. So I skip the sentence - which happens to be the one explaining why the trans products are racemic.
- **Evidence:** concepts[0].prerequisites = []; all others reference only in-chapter slugs. Exactly 1 mcmurry_link block pointing at 30-why-this-chapter.
- **Recommended outcome (need):** A student arriving with weak prerequisites needs to be told what to refresh before section 1 and needs a level-appropriate route back for the stereochemistry and aromaticity vocabulary the chapter reuses.

##### `struggle-011` — MEDIUM · cognitive-load · confidence 0.88

- **Location:** section_id=`nugget-electrocyclic-reactions` · concept_slug=`electrocyclic-reactions` · nugget_id=`nugget-electrocyclic-reactions`
- **Anchor:** "The reason electrocyclic reactions repay careful study out of proportion to how often they are run in a laboratory"
- **Observation:** Section 4's default view never says what an electrocyclic reaction is. The definition, the electron-counting instruction, the conjugation requirement with the hexa-1,5-diene counterexample, the s-cis requirement and the reason cyclobutene opens are all in standard; the expanded tier opens on why the family repays study, then sets up a labelling experiment, then introduces torquoselectivity - a refinement on a rule the default reader has not been given.
- **Learner impact:** I reach the end of the section that is supposed to define electrocyclic reactions still not knowing which bonds change, and I have picked up a piece of specialist vocabulary I now assume is examinable. Section 5 depends entirely on section 4, so I carry the gap forward.
- **Evidence:** The definition sentence, the counterexample and the s-cis requirement are in text.standard only; text.expanded contains the torquoselectivity paragraph.
- **Recommended outcome (need):** The section that names the family has to define it on the default path, and a specialist refinement should not reach a student before the rule it refines.

##### `struggle-012` — LOW · cognitive-load · confidence 0.6

- **Location:** question_slug=`ch30-triene-filled-pi-mos`
- **Anchor:** "Enter a number only, with no unit."
- **Observation:** The item asks how many pi molecular orbitals of hexa-1,3,5-triene contain electrons (answer 3) and supplies student_config.placeholder 'e.g. 5'. Five is a plausible-looking wrong answer: the prompt contains 'six' twice, and a student who miscounts often lands adjacent to six.
- **Learner impact:** On the chapter's second-easiest question a student with no confidence reads the greyed-out example as a suggestion of the expected magnitude and either anchors on it or second-guesses a correct answer of 3. This is one of only two places a struggling student can bank an early win.
- **Evidence:** student_config [redacted]; answer_key [redacted] Same placeholder in the v2 variant.
- **Recommended outcome (need):** A placeholder in a numeric field needs to demonstrate the format without suggesting a value in the answer's neighbourhood.

**Open questions**

- Is the reader's expanded default intended, and are chapters expected to author expanded as a superset of standard? If the platform default is what should change, struggle-001 is a platform fix rather than a chapter rewrite - but the delivered default view is missing its definitions either way.
- Are per-nugget practice_checks and per-concept trouble_spots intended to reach the reader at all, or authored only for instructor and deck surfaces?
- All six video blocks are is_hidden because the briefs are deferred. Should the storyboard's content be delivered another way in the meantime?
- struggle-012 was filed under cognitive-load; a placeholder that could be read as a hint may belong to a different persona's scope.

#### Accessibility Persona — 8.3/10

persona_version 1.0.0 · publication_blockers: none_

This is the most accessible chapter in this package family, and accessible by design rather than by metadata compliance. All 36 assets carry both a content-bearing alt_text and a long_description that teaches the figure; every one of the 11 surfaced questions is answerable from text alone; all 66 hints are text or worked_step; every concept retains at least one keyboard-complete question; and both structure_scaffold items set typed_structure_entry 'allowed' with a SMILES answer key, so the keyboard route is live on both delivery surfaces. Most striking, the chapter deliberately refuses to draw the butadiene/hexatriene MO sets and makes the node-count and terminal-lobe-parity rule the primary representation in prose, which removes what would otherwise have been this chapter's biggest non-visual barrier. Nothing here is a publication blocker. The one serious problem is not that the keyboard route is missing but that it cannot be checked: the typed-SMILES read-back returns byte-identical text for the answer key and for the graded distractor, so the only feature being assessed is the one feature a non-visual learner cannot confirm. The remaining findings are platform-level ones this chapter surfaces sharply: wavefunction phase carried by hue alone, the reaction-coordinate card discarding its long_description, the 'show images' toggle deleting 32 of 36 figures together with their text equivalents, and raw Unicode subscripts reaching the DOM in question renderers.

**Strengths**

- Every one of the 36 assets carries both an alt_text and a long_description, and every alt_text is content-bearing rather than a label, all within the 250-character guidance.
- The chapter refuses to make an inaccessible figure the primary carrier of its central rule, stating the node-count and terminal-lobe-parity rule in prose and saying so explicitly. That single authoring decision removes what would have been the largest non-visual barrier and makes the load-bearing content text-first for every learner.
- All 11 surfaced questions are answerable from text alone; none requires reading a figure, a spectrum, a colour, a position or an animation, and none depends on hover, drag or fine pointer input.
- Every one of the 10 concepts retains at least one keyboard-complete surfaced question, and the types that could have been drag-only are not: labelled Selects per item, Move up/Move down buttons whose labels include the current position, and a real Table with scope=col and scope=row.
- Both structure_scaffold items set typed_structure_entry 'allowed' with a SMILES answer_key, and the keyboard route is wired on both delivery surfaces including the reader path.
- All 66 hints are kind 'text' (49) or 'worked_step' (17); there is not a single image, highlight, projection-label or animation hint.
- No answer leaks: find_accessibility_leaks flags 0 of 22, and reading them by hand confirms each states the task and withholds the verdict.
- The comparison_matrix accessible_description matches the rendered table orientation exactly - easy to fluff and the difference between an orienting description and a misleading one.
- The rank_order item uses text-only cards, sidestepping the known limitation that rank_order does not render card structures.
- The reader surfaces long_description as visible body text for every molecule and reaction block and for all four orbital overlays, so the phase-versus-charge correction is read by sighted and non-sighted learners alike.
- Every orbital figure's description ends with the qualitative-cartoon disclaimer, so a learner relying on the description is not misled about the figure's authority.
- The prose uses no markdown headings or lists, which matters because RichText supports only paragraphs, bold and code.

**Findings**

##### `access-001` — HIGH · interactive-fallback · confidence 0.95

- **Location:** question_slug=`ch30-draw-photochemical-closure` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "A typed structure is accepted."
- **Observation:** Both structure_scaffold questions allow typed entry, so a keyboard-only or non-visual learner can submit a typed SMILES and be graded by RDKit. But the typed-entry read-back - the non-visual substitute for glancing at the canvas - cannot distinguish the correct answer from the graded distractor. TypedStructureRenderer calls describeStructure with skill_level 'intro', which normalizes to 'orgo1', and build_orgo1_summary emits no stereochemistry. Running the service on this question's key and its first wrong-answer SMILES returns identical output for both, character for character; common_name and iupac_name are None for both and the molecular formula is identical (C6H10). The same holds for the v2 pair.
- **Learner impact:** A sighted student answering on the canvas sees their wedge and dash and can check the one thing being graded before submitting. A blind, low-vision or keyboard-only student typing SMILES gets a confirmation line provably blind to cis-versus-trans, so they must submit on faith about the sole assessed feature. This is the assessment equivalent of an unlabelled control: the route exists, the feedback loop does not.
- **Evidence:** typed_structure_entry 'allowed'; answer_key.smiles C[C@H]1[C@@H](C)C=C1; wrong-answer match C[C@H]1[C@H](C)C=C1. TypedStructureRenderer passes skill_level 'intro', detail 'brief'. [internal source reference — not in this repo] build_orgo1_summary contains no stereo clause.
- **Recommended outcome (need):** A learner using the typed route needs to be able to confirm, before submitting, the exact feature the question grades. The confirmation must discriminate between the answer key and the graded distractors on both items.

##### `access-002` — MEDIUM · interactive-fallback · confidence 0.86

- **Location:** question_slug=`ch30-draw-photochemical-closure-v2` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "Mark the two methyl groups with a wedge and a dash so their relationship is unambiguous."
- **Observation:** Everything the two structure_scaffold questions say about HOW to express the answer assumes drawing: 'Draw the product, showing clearly how the two methyl groups are arranged'; 'Mark the two methyl groups with a wedge and a dash'; hint 3 'read off whether the methyls finish on the same face'. The typed alternative is announced but nowhere is the learner told how to say cis or trans in typed form, and the input's helper text illustrates SMILES only with two achiral examples.
- **Learner impact:** A learner routed to the typed alternative is asked to encode the graded feature in a notation nobody has taught them, while every piece of scaffolding is phrased for the drawing route they are not using. The accommodation is reachable but not self-sufficient.
- **Evidence:** prompt_text of both items; wrong-answer explanations for the stereochemistry-free skeletons; TypedStructureRenderer FormHelperText 'CCO is ethanol, c1ccccc1 is benzene'; student_config carries no typed_structure_entry_note although the renderer displays one when present.
- **Recommended outcome (need):** A learner using the typed route needs a stated way to express the relative stereochemistry the question grades, and wrong-answer feedback whose remedy applies to the route they used.

##### `access-003` — MEDIUM · color-motion-only · confidence 0.9

- **Location:** asset_id=`orb-carbonyl-pi-star` · concept_slug=`pi-molecular-orbitals` · nugget_id=`nugget-pi-molecular-orbitals`
- **Observation:** In all four orbital_overlay figures the sign of the wavefunction - the quantity the chapter's entire symmetry argument turns on - is drawn as hue and nothing else. The library SVGs fill lobes with .orb-lobe-pos (#0072B2) and .orb-lobe-neg (#D55E00) and carry no '+'/'-' glyph, no hatch and no differing stroke, even though each manifest declares phaseConvention positiveLabel '+' and negativeLabel '-'. The hues separate under red-green deficiencies but their relative luminance is close, so the distinction collapses in greyscale, print and achromatopsia. It bites hardest on orb-carbonyl-pi-star, where the point is that the phase reverses across the node and the four lobes are geometrically identical in pairs.
- **Learner impact:** A student with colour-vision deficiency, on a greyscale display, or working from a photocopied handout sees four figures differing only in lobe geometry and cannot extract the in-phase versus out-of-phase distinction the chapter is built on. They are pushed onto the caption while classmates read the picture, and the printed-handout case has no caption at all.
- **Evidence:** The four committed SVGs contain only orb-lobe-pos/orb-lobe-neg paths and a dashed .orb-node line, zero <text> elements; each manifest's phaseConvention declares labels that are never drawn.
- **Recommended outcome (need):** The sign of the wavefunction needs to be recoverable from the figure itself without relying on hue discrimination, in every surface the figure reaches.

##### `access-004` — MEDIUM · media-equivalence · confidence 0.94

- **Location:** asset_id=`rcd-diels-alder-concerted` · section_id=`nugget-pericyclic-reaction-basics` · nugget_id=`nugget-cycloaddition-reactions`
- **Observation:** The chapter's only energy diagram carries an authored 152-word long_description, compiled into both reader blocks. The reader never shows it. ReactionCoordinateCard reads only content.alt_text - as the Image alt, as the visible 'Described as:' line, and as the render-failure fallback - and has no long_description branch. StructureCard in the same file renders longDescription for every molecule and reaction block, and TeachingAssetLiveRenderer renders it for the orbital overlays, so this figure type is the only one whose extended equivalent is authored and then dropped.
- **Learner impact:** The alt text carries the headline, so this is a loss of depth rather than of fact. What is discarded is the reasoning a non-visual learner most needs from a curve they cannot see: that a stepwise route would show a dip, that a species in that dip would live long enough to rotate a bond and scramble stereochemistry, and that the diagram is schematic.
- **Evidence:** Compiled block content keys include long_description for both instances; ReaderBlockRenderer ReactionCoordinateCard references content.alt_text three times and content.long_description zero times.
- **Recommended outcome (need):** The authored extended description of the energy profile needs to reach a learner in the reader, on the same footing as the molecule and reaction descriptions.

##### `access-005` — MEDIUM · media-equivalence · confidence 0.88

- **Location:** section_id=`nugget-orbital-symmetry-selection-rules` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "trans-3,4-Dimethylcyclobutene: a cyclobutene ring carrying a methyl group on each of the two saturated carbons, one on each face of the ring."
- **Observation:** The reader's own personalization control removes this chapter's text equivalents along with its figures. applyPrefs drops any block whose type is in IMAGE_TYPES (molecule, reaction, reaction_coordinate, image) when showImages is false - the whole block, so alt_text and long_description go with it. For this chapter that is 32 of 36 assets. Only the four orbital overlays survive because teaching_asset is not in IMAGE_TYPES. The worst-affected section loses 9 of its 12 blocks and with them every description of which face each methyl group ends on.
- **Learner impact:** A learner who turns images off to make the chapter usable silently loses the chemistry rather than just the pictures, and has no way to know that descriptions existed and were discarded.
- **Evidence:** TopicPackageChapterRenderer IMAGE_TYPES set and the applyPrefs early return; DEFAULT_READER_PREFS.showImages true.
- **Recommended outcome (need):** Suppressing figures must not suppress their text equivalents.

##### `access-006` — MEDIUM · media-equivalence · confidence 0.8

- **Location:** question_slug=`ch30-electrocyclic-ring-size-sort` · concept_slug=`electrocyclic-reactions`
- **Anchor:** "Buta-1,3-diene, CH2=CH-CH=CH2"
- **Observation:** The chapter's question text uses Unicode subscript and superscript characters for formulas and orbital indices - 41 subscripts and 7 superscripts across 8 questions - and the question renderers hand them to the DOM as raw code points. The reader's prose path converts them via RichText to <sub>/<sup>, but SelectedResponseRenderer, MatchingRenderer, CategorizeRenderer, ComparisonMatrixRenderer, MechanismCardSortRenderer and the PublicQuestionSetPanel prompt line all render plain Text with no ChemText call, although ChemText exists and is used by six other activity renderers. Announcement of U+2080-U+2089 is inconsistent and several screen readers drop them silently.
- **Learner impact:** A screen-reader user may hear formulas with the hydrogen counts stripped and orbital labels reduced to a bare 'psi'. Every item also gives the compound NAME, so the questions remain answerable, but the learner must reconstruct what everyone else reads directly.
- **Evidence:** Per-question counts: ch30-fmo-role-match 12/0, ch30-electrocyclic-ring-size-sort 12/3, ch30-dienophile-reactivity-rank 7/0, and others; grep for renderChemFormula across activity-renderers returns only five components, none used by this chapter.
- **Recommended outcome (need):** Chemical formulas and orbital indices in question prompts, options, cards and match lists need to reach assistive technology with their subscripts intact, matching the treatment reader prose gets.

##### `access-007` — LOW · keyboard-operability · confidence 0.85

- **Location:** section_id=`nugget-pi-molecular-orbitals`
- **Anchor:** "A single carbon p orbital, and what its two colours mean"
- **Observation:** The reader chapter's heading outline skips a level. TopicPackageChapterRenderer renders the chapter title as h1 and each section title as h2, but every figure card renders its own title as h4 - StructureCard, ReactionCoordinateCard, the video card and TeachingAssetLiveRenderer all use h4, as do the text and callout headings. No h3 is emitted anywhere, so h2 is followed directly by h4 in all ten sections.
- **Learner impact:** A screen-reader user navigating by heading level sees a gap at every section and cannot tell whether an h4 is a child of the preceding h2 or of something that failed to render. With 36 figure cards this is encountered constantly.
- **Evidence:** TopicPackageChapterRenderer h1/h2; ReaderBlockRenderer as='h4' at five sites; TeachingAssetLiveRenderer as='h4'.
- **Recommended outcome (need):** The chapter's heading levels need to descend without gaps so heading-based navigation reflects the real nesting.

##### `access-008` — LOW · media-equivalence · confidence 0.72

- **Location:** question_slug=`ch30-selection-rules-matrix` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "sketch the diene HOMO and the triene HOMO and look at their ends"
- **Observation:** Three hint ladders instruct the learner to produce and inspect a drawing with no equivalent inside the ladder itself. The non-drawing route exists and the chapter states it well - count nodes, then read parity - but it appears in the prose of two nuggets, not in the hint the learner is looking at while stuck. The hints that follow do supply the flip rule, so the ladder recovers.
- **Learner impact:** A learner who cannot sketch is told at the first level of help to do the one thing they cannot do, and has to reach level 2 before being offered a route they can follow. A worse first experience of help rather than a blocked question.
- **Evidence:** hints level 1 of ch30-selection-rules-matrix; level 2 of ch30-draw-photochemical-closure-v2; contrast with the node-parity rule in nugget prose and the level-2 hint.
- **Recommended outcome (need):** The first rung of help for a frontier-orbital symmetry question needs to be usable without producing a drawing.

##### `access-009` — LOW · alt-text-quality · confidence 0.75

- **Location:** asset_id=`mol-7-dehydrocholesterol` · concept_slug=`pericyclic-reactions-in-biology`
- **Anchor:** "labelled A through D"
- **Observation:** The steroid and seco-steroid descriptions narrate the figure using ring letters the figure does not draw. mol-7-dehydrocholesterol says 'labelled A through D. Ring A carries a hydroxyl group ... what distinguishes this compound from cholesterol is ring B'; previtamin D3, vitamin D3 and the ring-opening reaction do the same. These are RDKit renders from bare SMILES with no annotations, so no A/B/C/D labels appear in the image.
- **Learner impact:** For a screen-reader user the lettering is a net help - it teaches the convention. The cost falls on the low-vision or magnifier user who reads the description as a guide to the picture: they hunt the enlarged image for labels that do not exist.
- **Evidence:** long_description of the three steroid molecules and the ring-opening reaction; the assets carry only 'smiles' with no annotation directives.
- **Recommended outcome (need):** A description that names ring A through D must either match what the figure shows or make clear the letters are the naming convention rather than drawn labels.

##### `access-010` — LOW · alt-text-quality · confidence 0.7

- **Location:** asset_id=`orb-carbonyl-pi-star` · nugget_id=`nugget-homo-lumo-and-fmo-theory`
- **Observation:** The pi* figure's description omits a visible asymmetry. The committed SVG draws the lobes on the first bonded atom noticeably larger (half-height 88 units) than those on the second (58 units), and the library manifest's teachingClaim names this explicitly. The asset's alt_text and long_description describe the four lobes, the node and the sign reversal but never mention that the carbon lobes are bigger or why.
- **Learner impact:** A sighted learner sees an obvious size difference and either uses it or is puzzled by it; a learner working from the description alone is told the figure is symmetric where it is not, and misses the coefficient argument. Low impact because this chapter reframes the figure's relevance as energetic rather than as site selectivity.
- **Evidence:** carbonyl_pi_star.svg left-atom lobes to +-88, right-atom lobes to +-58; manifest teachingClaim names the larger lobe on carbon.
- **Recommended outcome (need):** The description needs to account for every distinction the drawing makes, or the figure should not draw a distinction the description withholds.

##### `access-011` — LOW · alt-text-quality · confidence 0.74

- **Location:** question_slug=`ch30-fmo-role-match` · concept_slug=`homo-lumo-and-fmo-theory`
- **Anchor:** "Four descriptions of frontier orbitals for a conjugated diene are listed on the left, and four orbital descriptions are listed on the right."
- **Observation:** The accessible_description for both matching_pairs items describes a spatial layout the delivered control does not have. MatchingRenderer renders one stacked card per left-hand item, each with a labelled Select whose options are the right-hand entries and whose aria-label is 'Match for {item text}' - there is no left column and no right column at any breakpoint.
- **Learner impact:** A screen-reader user builds a mental model of two columns and then meets a sequence of dropdowns, and has to work out that the mapping is one-directional and answered in place. It costs orientation time rather than blocking the question.
- **Evidence:** accessible_description of both matching items; MatchingRenderer renders a VStack of Boxes each with a FormLabel and one Select, aria-label 'Match for {item.text}'.
- **Recommended outcome (need):** A question's accessible description needs to orient the learner to the interaction they will actually meet.

##### `access-012` — LOW · media-equivalence · confidence 0.68

- **Location:** concept_slug=`orbital-symmetry-selection-rules` · section_id=`nugget-electrocyclic-reactions`
- **Anchor:** "Watching the ends turn"
- **Observation:** All five video briefs are deferred and the compiler handles that correctly - blocks carry url '' and is_hidden true, and the renderer returns null, so no learner meets a dead 'Watch' link. The forward-looking gap is in the briefs themselves: their storyboards lean on colour as a carrier ('highlighted in a contrasting colour', 'shown in phase colours', 'recolouring') and the narration_outlines state conclusions without describing the visual events that justify them. No brief mentions captions, audio description or pause/step controls.
- **Learner impact:** Nothing degrades today. If these animations are produced as written, a learner who cannot see them will hear narration that asserts outcomes without describing the changes, and a learner with colour-vision deficiency will lose the phase distinctions - reproducing at video scale the colour-only problem the static figures already have.
- **Evidence:** video_briefs production_status 'deferred'; the storyboard lines quoted; compiled video blocks hidden with empty url.
- **Recommended outcome (need):** Before any of these animations is produced, each brief needs to commit to how a learner who cannot see it or cannot separate the phase colours will get the same information, and whether the motion can be paused or stepped.

**Open questions**

- Does the reader's detail-level control expose the tiers as keyboard-reachable, labelled controls, and is the tier change announced?
- At the terse tier, nugget-pi-molecular-orbitals keeps the node-counting rule but drops the terminal-lobe parity rule. Is terse intended as a self-sufficient reading path?
- Is there any print or PDF export path, and does it carry the long_descriptions? access-003 and access-005 get materially worse on paper.
- Whether a Ketcher canvas that fails to load still leaves the typed-entry field reachable could not be verified statically.

#### Learner with Visual Preference — 6.0/10

persona_version 1.0.0 · publication_blockers: none_

This chapter is unusually well written and unusually poorly seen. Its predictive machinery is a chain of three spatial claims - count nodes in psi_n, read the sign relationship of the two terminal lobes, translate that into a rotation sense and then into a face - and not one link in that chain is depicted. The four orbital_overlay figures all show systems of two centres or fewer, so no figure contains an orbital with an interior and two distinguishable ends; the concept of a terminal lobe has no picture at any point. Conrotatory versus disrotatory is carried by two verbal analogies and one deferred video whose reader block is hidden. The same is true of the endo/exo stacking (no exo structure exists in the package), the chair-like [3,3] transition state (asserted in five places, drawn nowhere), the s-cis conformational gate (named as a standing trap; the one butadiene figure renders in the non-reacting extended conformation), and the [2+2]-forbidden lobe mismatch. What the chapter does have is 36 well-chosen, correctly-drawn figures with excellent long descriptions - but they are almost all reactant-and-product snapshots of transformations whose teaching point is the motion in between, and several sections repeat species already drawn inside an adjacent reaction card. The authored justification for the polyene gap is honest but over-covers: an energy ladder with occupancy, a phase pattern on four circles, a rotation-sense sketch and an endo/exo stacking sketch are none of them orbital-lobe cartoons, and ALLOWED_ASSET_TYPES already carries `diagram`, which this chapter uses zero times. Nothing blocks publication; the prose is complete and the descriptions are sufficient to learn from. But this is the chapter where a figure would carry the most weight, and it is the least illustrated relative to what it asks a learner to picture.

**Strengths**

- Accessibility text is the best-developed part of the figure layer: all 36 assets carry both alt_text and a substantial long_description, and several do real teaching. Where a picture is missing, the description usually is not.
- Every orbital figure carries an explicit epistemic disclaimer, and the polyene-picture decision is stated openly rather than quietly omitted. That is the right way to handle a capability limit.
- The four orbital overlays that exist are chemically correct and use valid preset/overlay pairings, with correct phase assignments: the bonding figure has matching phases above both carbons, the pi* figure reverses phase across the C-O node.
- The stereochemical structure pairs render clearly and are easy to tell apart at a glance: one-wedge-one-hash versus two-wedges for both the cyclobutenes and the cyclohexadienes. The two thermal electrocyclic schemes are clean and correctly oriented.
- The chapter shows the four-electron case in the direction that actually runs - cyclobutene ring OPENING rather than a diene closure heat cannot drive - and says so in the figure's own learning goal. That is a harder and more honest choice than the tidy 2x2 most treatments draw.
- Deferred videos degrade cleanly rather than shipping broken players, and every brief carries a complete storyboard plus a specific production_note naming the pipeline limitation.
- rcd-diels-alder-concerted pins molecules to both minima, so the energy profile carries the reactant and product structures on the curve rather than bare labels.

**Findings**

##### `visual-001` — HIGH · visual-opportunity · confidence 0.93

- **Location:** section_id=`pi-molecular-orbitals` · concept_slug=`pi-molecular-orbitals` · nugget_id=`nugget-pi-molecular-orbitals`
- **Anchor:** "the terminal-lobe relationship alternates as you go up the ladder"
- **Observation:** The chapter's entire predictive chain runs through the sign relationship between the two TERMINAL lobes of a polyene frontier orbital, and that relationship is never depicted. All four orbital_overlay assets show systems of two centres or fewer, and the benzene cloud is drawn as two continuous doughnut lobes with no per-atom lobes at all. None has an interior with two distinguishable ends. The alternation rule and the even/odd node argument appear only as prose.
- **Learner impact:** A learner who reasons by inspecting a picture has no picture to inspect for the one inference the chapter uses most. Every prediction becomes a chain of four remembered verbal steps with no visual checkpoint at which a wrong step becomes obvious. The chapter tells the student to regenerate the rules rather than memorise the table, which is good advice that presumes they can picture what they are regenerating.
- **Evidence:** Four orbital_overlay entries; orbital-library.manifest.json contains no polyene MO set; orbital-presets.manifest.json offers only six presets. The terminal-lobe rule lives in prose in two nuggets, and nugget-pi-molecular-orbitals expanded states the deliberate choice.
- **Recommended outcome (need):** A learner needs to SEE, for at least butadiene psi_2 and hexatriene psi_3, that the two end lobes on one face either match or oppose, and that this alternates with node count. The need is for the sign pattern and node positions to be inspectable, not for a computed molecular orbital - a schematic showing phase signs at each carbon with nodes marked between carbons would satisfy it. Note ALLOWED_ASSET_TYPES already includes `diagram`, which this chapter uses zero times.

##### `visual-002` — HIGH · visual-opportunity · confidence 0.94

- **Location:** section_id=`orbital-symmetry-selection-rules` · concept_slug=`orbital-symmetry-selection-rules` · nugget_id=`nugget-orbital-symmetry-selection-rules`
- **Anchor:** "conrotatory is two wheels on a shared axle turning together; disrotatory is the two covers of a book opening"
- **Observation:** Conrotatory and disrotatory motion - a rotation of two groups about two axes, an intrinsically spatial relation - is conveyed entirely by two verbal analogies plus reactant/product snapshots. The only planned depiction is deferred; the compiled reader emits its block with url '' and is_hidden true, so nothing about the motion is shown. The section's nine figures show flat starting materials and flat products.
- **Learner impact:** The learner must construct the rotation mentally from two similes and map it onto a wedge/dash outcome with no external representation to check against. The two motions are easy to conflate precisely because their products differ only in which face two methyl groups sit on.
- **Evidence:** video_briefs[0] production_status 'deferred'; compiled blocks in two sections both carry url '' and is_hidden true; the section's asset list contains no figure of the motion.
- **Recommended outcome (need):** The learner needs the two rotation senses distinguishable by looking rather than by recall, and needs to see how each delivers the end substituents to the same or opposite faces. Motion is not required - a sequenced or annotated static comparison of the same starting frame turned two ways would carry it.

##### `visual-003` — HIGH · figure-purpose · confidence 0.9

- **Location:** asset_id=`mol-endo-norbornene-anhydride` · section_id=`diels-alder-stereochemistry` · concept_slug=`diels-alder-stereochemistry`
- **Anchor:** "The anhydride ring is oriented on the same side as the two-carbon bridge that carries the double bond - the endo arrangement"
- **Observation:** Two figures state in their titles and learning goals that they show the endo orientation, and neither can. Both are flat RDKit renders in which the CH2 bridge crosses the ring, all four ring-fusion bonds carry wedges or hashes, and there is no visual cue for which side of the bridged system the anhydride leans towards. Nor is there any exo structure in the package, so the contrast the section turns on has no second member. The endo/exo video is deferred and was the only asset going to show the stacked approach or the secondary overlap.
- **Learner impact:** The section asserts that the more crowded adduct forms faster, that endo and cis answer different questions, and that a secondary orbital interaction stabilises only one transition state - three claims about a three-dimensional stacking relationship, none of which the learner can see once. A learner who checks claims against figures finds the figure captioned 'endo' indistinguishable from what an exo adduct would look like.
- **Evidence:** Rendered both assets with RDKit: drawn as a flat bicycle with the anhydride fused edge-on. No asset carries an exo structure. video-endo-vs-exo deferred; its storyboard is the missing figure.
- **Recommended outcome (need):** The learner needs the two stacking orientations visually contrastable, and the endo relationship locatable in a drawing rather than asserted in a caption. The two-barrier energy comparison is a second, separable need.

##### `visual-004` — HIGH · figure-purpose · confidence 0.91

- **Location:** section_id=`orbital-symmetry-selection-rules` · nugget_id=`nugget-orbital-symmetry-selection-rules` · concept_slug=`orbital-symmetry-selection-rules`
- **Anchor:** "It is worth seeing the four canonical results together, because questions are built from them."
- **Observation:** The section explicitly asks the learner to see four canonical results together, and the figures do not put them together: nine cards in flat serial order after one long prose block. Only the two thermal cases exist as transformations. The two photochemical results appear only as orphan product structures with no arrow, no hv condition and no adjacency to their substrate. The substrate-to-product pairing for every result exists only in prose.
- **Learner impact:** The section's content is a 2x2 comparison whose whole value is in seeing that the pattern flips. As one prose block plus nine independent cards, the learner must hold four pairings in working memory while scrolling. The chapter's own question is literally a 2x2 grid, so the assessment format and the figure layout disagree.
- **Evidence:** The section's nine asset_ids listed; both reaction assets are thermal; no photochemical transformation asset exists; compiled section is one text block followed by nine figure cards, a hidden video and a link.
- **Recommended outcome (need):** The learner needs the four canonical results visible as one comparison in which substrate, condition and product stereochemistry are adjacent, and the two photochemical results presented as transformations under hv rather than unattached product structures.

##### `visual-005` — MEDIUM · visual-redundancy · confidence 0.88

- **Location:** section_id=`homo-lumo-and-fmo-theory` · nugget_id=`nugget-homo-lumo-and-fmo-theory` · concept_slug=`homo-lumo-and-fmo-theory`
- **Anchor:** "A photon promotes exactly one electron from the HOMO into the LUMO."
- **Observation:** The HOMO/LUMO section has no figure of its own. Its three assets are all verbatim repeats of cards the reader has just scrolled past, and none depicts occupancy, energy ordering, a frontier pair, or an excitation. The section's two central ideas are about relative energies and electron counts, which no orbital-shape cartoon can express.
- **Learner impact:** A learner scrolling this section sees three familiar pictures that answer none of its questions, which trains the habit of skipping figures. The excited-state argument is a bookkeeping picture that is easy to draw and easy to get wrong from prose alone, and it is the step that inverts every stereochemical prediction in the rest of the chapter.
- **Evidence:** asset_ids ['orb-ethylene-pi','orb-carbonyl-pi-star','mol-butadiene'] - all three also appear in the preceding nugget's asset_ids.
- **Recommended outcome (need):** This section needs at least one figure that does its own work - the energy ordering of psi_1 to psi_4 with the electrons shown where they sit, before and after promotion - and the three repeats need either a distinct job here or removal. An energy-ladder figure is not an orbital-shape claim and is unaffected by the library constraint.

##### `visual-006` — MEDIUM · figure-accuracy · confidence 0.85

- **Location:** asset_id=`orb-ethylene-pi` · section_id=`pi-molecular-orbitals`
- **Anchor:** "a pair of merged lobes is superimposed, one lobe spanning both carbons above the plane and a matching lobe spanning both carbons below"
- **Observation:** The long description of orb-ethylene-pi does not match what the committed SVG draws, and the mismatch falls on the load-bearing feature. pi_bond_alkene.svg draws FOUR discrete teardrop lobes (one above and one below each carbon, fill-opacity .55) plus two spanning ellipses at cloud opacity .20; the description says the lobes are merged into one continuous lobe above and one below. The continuity that makes the orbital bonding is therefore carried visually only by a 20%-opacity ellipse behind four crisp separate lobes. Its contrast partner carbonyl_pi_star.svg also draws four crisp lobes and differs only by the absence of those clouds, a thin grey dashed node line, and a phase-colour swap on the right-hand atom.
- **Learner impact:** The most important visual discrimination in the chapter - node between the bonded atoms versus no node - is between two figures that look nearly identical, with the difference carried by a translucent fill, a hairline dash and a colour swap. A learner may reasonably conclude that a pi bond is also two separate lobes per atom, which is precisely the misreading the section's phase warning tries to prevent. Separately, a learner using the description and a learner using the picture are told different things about the same figure.
- **Evidence:** pi_bond_alkene.svg draws four orb-lobe paths anchored at x=-50 and x=+50 plus two orb-cloud ellipses; carbonyl_pi_star.svg draws four orb-lobe paths plus one orb-node dashed line at x=0.
- **Recommended outcome (need):** The bonding-versus-antibonding distinction needs to be the visually dominant difference between these two figures rather than a low-contrast one, and the figure's description needs to describe the lobes the figure actually draws. Whichever moves, they must agree.

##### `visual-007` — MEDIUM · figure-accuracy · confidence 0.95

- **Location:** asset_id=`rcd-diels-alder-concerted` · section_id=`pericyclic-reaction-basics`
- **Anchor:** "The barrier is high, which is why this unsubstituted example needs roughly 200 degrees Celsius."
- **Observation:** The chapter's only reaction-coordinate figure specifies barrier 'high', which is not a value the renderer accepts. BarrierSize is small | medium | large, and the backend silently coerces any unrecognised value to DEFAULT_BARRIER 'medium' (height 1.2, against 2.0 for 'large'). The figure therefore renders a medium barrier while its title description, alt text and long description all say the barrier is high, and the valid 'large' setting goes unused. The coercion is silent, so nothing in the pipeline flags it.
- **Learner impact:** The figure is used to make two points: the shape (one maximum, no dip) and the height (why the unsubstituted Diels-Alder needs 200 degrees). The shape renders correctly; the height, which the surrounding prose leans on twice, renders as unremarkable. A learner reading the curve against the caption gets a contradiction on exactly the quantitative claim the figure was placed to support.
- **Evidence:** spec.steps = [{'type':'exergonic','barrier':'high'}]; [internal source reference — not in this repo] BarrierSize type; [internal source reference — not in this repo] BARRIER_HEIGHTS, DEFAULT_BARRIER and the coercion branch. Same spec appears twice in the compiled reader.
- **Recommended outcome (need):** The drawn barrier needs to agree with the caption that describes it, using a value the renderer recognises. More generally the compile step needs to notice an unrecognised enum value in an asset spec instead of letting it degrade silently.

##### `visual-008` — MEDIUM · visual-opportunity · confidence 0.86

- **Location:** asset_id=`mol-butadiene` · section_id=`electrocyclic-reactions` · concept_slug=`electrocyclic-reactions`
- **Anchor:** "A diene held s-trans by a ring cannot close at all, no matter how favourable the electron count, and this is a standing trap in problems."
- **Observation:** The s-cis / s-trans conformational gate is invoked in three sections and twice named as a standing trap or a favourite exam question, and it is never shown. mol-butadiene is the only butadiene figure and RDKit lays C=CC=C out in the extended, s-trans-like zigzag, so the single picture of the chapter's reference diene shows it in the conformation that CANNOT react. Cyclopentadiene's locked s-cis geometry is described but never contrasted visually, and no figure shows the coiled reacting conformation of any polyene, including the octatriene, drawn fully extended with its ends pointing away from each other.
- **Learner impact:** A learner checking 'can the two ends reach each other?' - which the chapter says to check before applying any symmetry rule - has a picture in front of them that says no. The geometric prerequisite is the cheapest thing in the chapter to show and the thing whose absence most directly misleads.
- **Evidence:** Rendered mol-butadiene with explicit hydrogens: an extended zigzag with the terminal CH2 groups pointing apart. The s-cis requirement is stated in two nuggets. rxn-electrocyclic-6pi-thermal renders the triene fully extended.
- **Recommended outcome (need):** The learner needs the s-cis and s-trans arrangements of the same diene visually comparable, and at least one depiction of a polyene folded into the geometry from which closure is possible.

##### `visual-009` — MEDIUM · figure-purpose · confidence 0.88

- **Location:** section_id=`sigmatropic-rearrangements` · nugget_id=`nugget-sigmatropic-rearrangements` · concept_slug=`sigmatropic-rearrangements`
- **Anchor:** "substituted cyclopentadienes scramble their substituents around the ring at room temperature"
- **Observation:** The sigmatropic section's figures are about a different reaction from the one the section teaches. Its subject is the [i,j] numbering rule and the [1,5]-versus-[1,3] contrast; its two reaction figures are both [3,3] rearrangements that belong to and are also assigned to the following section. No figure in the chapter shows a hydrogen shift of any kind. The walking-substituent demonstration is represented by a single static structure with the successive positions described only in the long description.
- **Learner impact:** A learner who uses figures to anchor a rule is anchored to the wrong example: the two schemes on screen are the [3,3] cases, so the [i,j] counting the section calls mechanical has no worked picture, and the walking-methyl demonstration must be imagined from a single frame. The [1,3]-forbidden case has no representation at all.
- **Evidence:** asset_ids ['mol-13-pentadiene','mol-5-methylcyclopentadiene','rxn-cope-divinylcyclobutane','rxn-claisen-allyl-vinyl-ether']; the latter two also appear in the next nugget. video_brief_ids is empty for this nugget.
- **Recommended outcome (need):** The learner needs at least one hydrogen shift shown as a transformation with the migrating hydrogen identifiable and the outward numbering visible, and the walking-substituent equilibration shown as successive positions. The allowed [1,5] and disallowed [1,3] cases need to be contrastable.

##### `visual-010` — MEDIUM · visual-opportunity · confidence 0.87

- **Location:** section_id=`cope-and-claisen-rearrangements` · concept_slug=`cope-and-claisen-rearrangements` · nugget_id=`nugget-cope-and-claisen-rearrangements`
- **Anchor:** "proceeds through a chair-like six-membered transition state"
- **Observation:** The chair-like [3,3] transition state is asserted in at least five places and drawn nowhere. It carries real explanatory load: it is why substituted Cope products are stereochemically predictable, it is what the divinylcyclobutane case violates (forced boat), and it is the shape chorismate mutase pays to pre-organise. Every one of those points depends on the learner picturing a folded six-membered array, and the only planned depiction is deferred.
- **Learner impact:** The chair/boat distinction is a conformational picture; asserted verbally it becomes vocabulary. The divinylcyclobutane exception is unlearnable from prose alone if the learner has never seen the chair it is an exception to, and the chorismate mutase mechanism reduces to 'the enzyme holds a shape' with the shape unseen.
- **Evidence:** 'chair-like' appears in four assets and one practice_check; rxn-cope-divinylcyclobutane's description names the boat exception; video-claisen-chair-transition-state deferred; no asset depicts a folded six-membered transition state.
- **Recommended outcome (need):** The learner needs the folded six-atom [3,3] array visible at least once, with the breaking and forming bonds identifiable at opposite corners, so the chair claim, the boat exception and the enzyme argument share a picture.

##### `visual-011` — MEDIUM · figure-purpose · confidence 0.87

- **Location:** asset_id=`rxn-vitamin-d-ring-opening` · section_id=`pericyclic-reactions-in-biology` · concept_slug=`pericyclic-reactions-in-biology`
- **Anchor:** "one bond of ring B has broken so that the ring is opened out into a chain of three conjugated double bonds"
- **Observation:** The before/after pair for the vitamin D ring opening does not make the ring opening visible. Rendering both SMILES shows the two structures laid out in different, effectively flipped arrangements with the A ring migrated to the far side; no ring is labelled A to D, no bond is marked as the one that breaks, and the retained rings are not in corresponding positions. The same applies to the previtamin-to-vitamin figure, where the migrating hydrogen and the new exocyclic methylene are not marked.
- **Learner impact:** This is the chapter's payoff section, and its claim - the same atoms, C27H44O both sides, only the connectivity differs - is exactly the kind of claim a learner verifies by comparing two pictures. Two independently auto-laid-out drawings of a 27-carbon polycyclic frame do not support that comparison; a learner is likely to read them as two unrelated compounds.
- **Evidence:** Rendered both molecules and the reaction with RDKit and compared: retained ring systems appear in non-corresponding positions and orientations. The long_description promises 'labelled A through D' which the drawing does not deliver. video_briefs[4] deferred.
- **Recommended outcome (need):** The learner needs before and after structures comparable - consistent orientation of the retained rings, the A to D labelling the description claims, and the bond that breaks identifiable.

##### `visual-012` — MEDIUM · visual-opportunity · confidence 0.9

- **Location:** question_slug=`ch30-endo-adduct-statements` · section_id=`diels-alder-stereochemistry`
- **Anchor:** "Endo and cis mean the same thing here, so calling the adduct endo is just another way of saying the two carbonyls are cis."
- **Observation:** No question in the compiled set carries a visual stimulus. All 22 have representation_tags ['text'] except the two structure_scaffold items, tagged 'molecule' only because the STUDENT draws; their prompts supply the substrate as a condensed formula. The heaviest cases are the endo/cis discrimination item, the ring-size sort with five condensed formulas, and the drawing item whose substrate is the string 'CH3-CH=CH-CH=CH-CH3 with both double bonds E'.
- **Learner impact:** Every question in a chapter about spatial relationships is answered by parsing text. That adds a formula-reading step in front of the reasoning step being assessed, and a learner who understood the chapter through its structures has to re-encode each stem before starting.
- **Evidence:** student_config keys across the set are options / left+right / groups+items / cases+features / cards / fields / placeholder - no figure or asset field anywhere. ch30-dienophile-reactivity-rank describes maleic anhydride in words although the asset exists in the same package.
- **Recommended outcome (need):** Questions whose reasoning is about a structure or a spatial relationship need that structure present in the stem rather than named in prose - especially the endo/cis item and the two drawing items, where the substrate is already an authored asset. This is a reuse need, not a new-figure need.

##### `visual-013` — MEDIUM · visual-redundancy · confidence 0.83

- **Location:** section_id=`pericyclic-reactions-in-biology` · nugget_id=`nugget-pericyclic-reactions-in-biology`
- **Anchor:** "A Claisen rearrangement in metabolism: chorismate to prephenate"
- **Observation:** Several sections pad their figure list with standalone renders of species already drawn inside a reaction card in the same section. The biology section carries eight cards for three transformations: all five molecule cards appear again inside the three reaction cards. The Diels-Alder section carries five cards, three of which are inside rxn-diels-alder-endo, and the fifth is the archetype appearing for the third time. mol-butadiene appears as an identical card in four separate sections.
- **Learner impact:** Long runs of near-duplicate cards after a single prose block make the figure strip feel like an appendix rather than part of the argument, and they push the figures that DO carry unique information further from the sentence they support. A learner who has learned that the cards repeat stops reading them.
- **Evidence:** The biology nugget's 8 asset_ids and the 3 reaction assets that contain all 5 molecules; mol-butadiene in four nuggets' asset_ids; rxn-diels-alder-archetype in three.
- **Recommended outcome (need):** Where a standalone card adds nothing the adjacent reaction card does not already show, the chapter needs fewer figures - or the standalone card needs a job the reaction card cannot do. Note the tension with the accessibility lens: each standalone card carries its own long_description, so removals should not silently drop a description the reaction card does not cover.

##### `visual-014` — LOW · figure-purpose · confidence 0.72

- **Location:** asset_id=`orb-carbon-p-orbital` · section_id=`pi-molecular-orbitals`
- **Anchor:** "This is the building block from which every pi molecular orbital in the chapter is assembled."
- **Observation:** The figure meant to establish the isolated basis orbital draws it on a molecule whose pi bond is already formed. The ethene preset SVG draws the C=C as a full double line, and the p_orbital overlay is anchored on the left carbon only, so the picture is one p orbital on one carbon of an intact ethylene with the partner carbon's p orbital absent.
- **Learner impact:** The figure's job is to prevent one misconception - that the lobe colours are charges - and it does that well in its description. But as a picture of a basis orbital it is ambiguous, and the ambiguity lands on a learner about to be asked to imagine n such orbitals combining into n molecular orbitals.
- **Evidence:** ethene_orbital_ready_v1.svg draws two parallel bond lines plus explicit C and H labels; the preset anchors p_orbital at the single atomRole 'p_center'.
- **Recommended outcome (need):** The learner needs the basis p orbital distinguishable from a half-drawn pi bond - either by not drawing a formed pi bond underneath it, or by making explicit in the figure that this is one contributing orbital of a set.

##### `visual-015` — LOW · figure-purpose · confidence 0.74

- **Location:** asset_id=`mol-prephenate` · section_id=`pericyclic-reactions-in-biology`
- **Anchor:** "the new carbon-carbon bond forms on the same face of the ring that the oxygen departed from"
- **Observation:** mol-prephenate's learning goal is 'the suprafacial outcome made visible in a metabolite', and the figure pair does not make it visible. Rendering the reaction shows the cyclohexadiene ring in two different orientations across the arrow, and the substituents whose faces are compared sit on non-corresponding carbons - 1,2 on the left and 1,4 on the right - so the wedge/hash pattern flips for layout reasons rather than chemical ones.
- **Learner impact:** A learner using the figure to check the suprafacial claim gets a misleading answer, and the claim is load-bearing because the section uses it to tie the metabolic reaction back to Diels-Alder stereospecificity.
- **Evidence:** Rendered rxn-chorismate-to-prephenate with RDKit: the ring is drawn in a different orientation on each side, chorismate's ether oxygen is hashed while prephenate's side chain is wedged, and the compared substituents are 1,2 versus 1,4.
- **Recommended outcome (need):** Either the figure needs a consistent ring orientation with the departing and forming faces indicated, or the asset's learning goal needs to stop claiming the outcome is visible and let the description carry it.

**Open questions**

- Is the `diagram` asset type available to this chapter in practice? If so, the polyene phase pattern, the MO energy ladder, the rotation-sense comparison, the chair transition state and the endo/exo stacking are all expressible today without authoring a single new orbital SVG, and the 'carry it as a node-counting rule in prose' decision was broader than the orbital-library constraint required.
- Should the standalone molecule cards that duplicate species already drawn inside an adjacent reaction card be removed, or do they serve an accessibility purpose? Each carries its own long_description. Flagged as a need rather than a removal; the Accessibility persona may reasonably take the opposite position.
- Does the reader's reaction_coordinate block render for a logged-out student? Could not verify without running the app.
- Which surface does an instructor actually teach the selection rules from - the reader section or a deck built from these assets? The fix for visual-004 differs depending on the answer.

#### Orchestrator findings

From the pre-dispatch integrity check on compiled links, identifiers and cross-surface consistency. Nine of eleven compiled external links resolved directly; section/nugget ids, deck_chapter_id, reader_slug, asset references and question concept references all reconciled with no drift, and every asset carries alt_text.

##### `orch-001` — LOW · notation-consistency · confidence 0.8

- **Location:** section_id=`nugget-orbital-symmetry-selection-rules`
- **Observation:** Two of the eleven compiled external links carry a raw en dash in the URL path, because the concept wikipedia_title values use the typographically correct 'Woodward–Hoffmann rules' and 'Diels–Alder reaction' and the reader builder only replaces spaces with underscores. Both targets resolve with HTTP 200 once the path is percent-encoded, and browsers encode automatically, so no learner-facing link is broken today.
- **Learner impact:** No impact in a browser. The exposure is to consumers that do not normalise a non-ASCII path - a link checker, a PDF or print export, or an LMS that passes the href through verbatim - where the two most important articles in the chapter are the ones that would fail.
- **Evidence:** Orchestrator link check of the compiled reader: 9 of 11 links returned 200 directly; the two en-dash URLs required urllib.parse.quote before they would resolve, then returned 200. Hyphen and percent-encoded variants also return 200.
- **Recommended outcome (need):** Generated hrefs need to be percent-encoded at build time so a non-ASCII article title does not depend on the client to repair the URL.

### Orchestrator decisions

For each recommendation: the need, the chosen intervention, and why it is the least-complex option that fully addresses that need. The personas stated needs; the choice of intervention is the orchestrator's.

#### `rec-001` — The default reading path never defines the chapter's own vocabulary

- **Severity:** blocker · **target surface:** prose
- **Consolidates:** `struggle-001`, `struggle-011`
- **Need:** A student on the reader's default detail tier is never given the definitions of conrotatory and disrotatory, HOMO and LUMO spelled out, suprafacial and antarafacial, the [i,j] counting procedure, the 4n versus 4n+2 statement, or the definition of an electrocyclic reaction. Every one of those lives only in the standard tier, while the reader defaults to expanded, which in this package is commentary layered on standard rather than a superset. Section 5 opens by advising against memorising 'the four boxes' before the student has met a box.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** Two fixes were available. Changing the reader's default tier is a platform change touching all 32 compiled chapters and would alter every other chapter's delivered reading level as a side effect. Making THIS chapter's expanded tier carry its own definitions is bounded to one file, fixes the problem for every reader today regardless of their slider position, and costs nothing elsewhere - so it is both the least-complex and the more complete of the two. The systemic half (that no chapter authors expanded as self-contained, and the reader defaults to it) is escalated separately as rec-017's sibling rather than solved here.

#### `rec-002` — The object every prediction is read off is never depicted

- **Severity:** high · **target surface:** figure
- **Consolidates:** `inst-001`, `struggle-002`, `visual-001`, `struggle-006`, `access-008`
- **Need:** The chapter's whole predictive chain runs through the sign relationship of the two terminal lobes of butadiene psi-2 and hexatriene psi-3, and no figure anywhere shows a polyene orbital with an interior and two distinguishable ends. Three personas found this independently, and a question hint instructs a stuck student to sketch the very thing that is never drawn.
- **Chosen intervention:** **new-figure**
- **Why this is the least-complex sufficient option:** A description cannot substitute here: the need is to make a sign pattern INSPECTABLE, which is what a picture does and prose cannot. Crucially this does not require the prohibited orbital-lobe cartoon - a schematic of phase signs at each carbon with nodes marked between them is a different object, and the `diagram` asset type (a hosted static ChemIllusion figure) already exists in ALLOWED_ASSET_TYPES and is used zero times by this chapter. Recorded rather than applied in this pass because authoring a hand-built diagram is new-asset work, not correction of a verified error.

#### `rec-003` — Conrotatory versus disrotatory motion is carried only by two similes

- **Severity:** high · **target surface:** figure
- **Consolidates:** `inst-002`, `visual-002`
- **Need:** The rotation the entire selection-rule apparatus predicts is never shown. The section's nine figures are all starting materials or products; the only planned depiction is a deferred video whose reader block compiles hidden. Students then learn 'four-electron thermal gives trans' as a product pairing rather than as a motion, which is exactly the failure the chapter's own prose warns against.
- **Chosen intervention:** **static-image-sequence**
- **Why this is the least-complex sufficient option:** Motion is not required to carry this and an animation is the most expensive option: an annotated static comparison of the same starting frame turned two ways shows both senses and where each sends the end substituents. The deferred video brief already contains that storyboard, so the sequence can be lifted from it without new design work.

#### `rec-004` — The two drawing questions cannot autograde the stereochemistry they exist to assess

- **Severity:** high · **target surface:** instructor-support
- **Consolidates:** `inst-003`, `access-001`
- **Need:** A wrong-diastereomer submission returns requires_manual_review and is escalated to status manual_review with no score; a correct-skeleton-no-stereochemistry submission returns 'unsupported'. Neither is graded incorrect, so neither of the two authored wrong-answer explanations that carry the teaching is ever delivered, and an instructor gets a manual-review queue on the one item they most wanted automated.
- **Chosen intervention:** **instructor-note**
- **Why this is the least-complex sufficient option:** The root cause is platform (structure_grading_service escalates stereo_mismatch by design, so a chapter cannot configure its way out), and changing that default would affect every drawing question in the corpus. The bounded action available to this chapter is to tell the instructor, in the package, that these two items land in manual review - so the behaviour is expected rather than discovered. The platform change is escalated, not attempted here.

#### `rec-005` — The typed-structure route cannot express or confirm the feature it is graded on

- **Severity:** high · **target surface:** assessment
- **Consolidates:** `access-001`, `access-002`
- **Need:** Both drawing items allow typed entry, but the typed read-back calls describeStructure at a skill level whose summary emits no stereochemistry, so the answer key and the graded distractor produce byte-identical confirmation text. Every piece of scaffolding - prompt, hints, wrong-answer feedback - is also phrased for wedge-and-dash drawing, and the learner is never told how to say cis or trans in typed form.
- **Chosen intervention:** **text-equivalent**
- **Why this is the least-complex sufficient option:** The keyboard route already exists and is correctly declared; what is missing is the confirmation loop and the notation guidance. A typed_structure_entry_note (a field the renderer already displays) plus stereochemistry in the read-back summary addresses it without changing the assessment. The note is authorable here; the read-back summary is a platform fix and is escalated.

#### `rec-006` — The chapter makes three forward promises and keeps none of them

- **Severity:** high · **target surface:** prose
- **Consolidates:** `inst-004`, `struggle-003`, `inst-014`
- **Need:** Section 1 promises 'a single underlying principle, stated at the end of the chapter' and no such statement exists. Section 2 promises a selection-rule table that is never shown and that the platform has no block type for. Section 3 refers to 'the chapter's tables'. The bridge that would deliver the principle - that a disrotatory closure is the suprafacial option and a conrotatory one the antarafacial - appears nowhere, and 'Woodward-Hoffmann' never reaches student-facing prose. The textbook crosswalk separately claims every numbered OpenStax section is represented, but 30.9 is not.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** The promises are the cheapest thing in the chapter to make true: the unifying statement is three sentences the author already had the pieces for, and the unkept table reference can be reworded to point at what the chapter actually delivers. Adding a table block type would be a platform change for a need prose can meet.

#### `rec-017` — The chapter's scaffolding never reaches the reader at all

- **Severity:** high · **target surface:** practice
- **Consolidates:** `struggle-004`, `struggle-005`
- **Need:** Thirty authored trouble spots and ten authored practice_checks with worked answers exist in the package and appear nowhere in the compiled chapter, which has no callout block and no per-section checkpoint. The named misconceptions the chapter is best at - phase is not charge, [4+2] is not an atom count, endo is not cis - are held only in metadata, and there is no retrieval stop between a 500-word section and the next section that depends on it.
- **Chosen intervention:** **added-practice**
- **Why this is the least-complex sufficient option:** This is a compiler and reader capability gap rather than an authoring omission: the content is written and correct, and no edit to this package surfaces it. It is the single largest gap between what the chapter contains and what a student receives, and it recurs across chapters, so it is escalated as a pipeline change rather than worked around here.

#### `rec-007` — Two question items assert a thermal four-electron ring closure the chapter denies

- **Severity:** medium · **target surface:** assessment
- **Consolidates:** `inst-006`, `inst-013`
- **Need:** The ring-size sort asks students to treat butadiene and (2E,4E)-hexa-2,4-diene as candidates for a 'thermal electrocyclic ring closure', and a wrong-answer explanation calls trans-3,4-dimethylcyclobutene 'the product of the thermal closure'. Both contradict the chapter's corrected teaching that cyclobutene strain makes opening the thermally accessible direction and that only light drives the closure.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** A direct internal contradiction introduced when the prose direction was corrected without grepping the question bank. Both items are fixed by rewording: the sort is really a ring-counting task and needs no 'thermal' claim, and the distractor should name the rotation mode rather than assert a thermal product.

#### `rec-008` — The energy diagram renders a medium barrier while its caption says high

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `visual-007`
- **Need:** The only reaction-coordinate asset specifies barrier 'high', which is not a member of the renderer's enum (small | medium | large); the backend silently coerces it to medium. The figure's title, alt text and long description all describe a high barrier, and the surrounding prose leans twice on the 200 degrees this reaction needs.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** A one-word fix to a valid enum value ('large') makes the drawing agree with the three descriptions already written for it. That the coercion is silent is a separate platform observation worth recording, but the asset itself is simply wrong and is corrected.

#### `rec-009` — The pi-bond figure's description contradicts what the committed SVG draws

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `visual-006`
- **Need:** orb-ethylene-pi's long description says the lobes are merged into one continuous lobe above and one below; the SVG draws four discrete teardrop lobes plus two faint spanning ellipses at 20% opacity. The continuity that makes the orbital bonding - the feature the description calls 'what is absent' - is therefore the least visible thing in the picture, and its antibonding contrast partner looks nearly identical.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** The description is the wrong half of the pair: the drawing is a reviewed committed asset and the description is authored here, so aligning the description to the drawing is both bounded and correct. Making the bonding/antibonding contrast visually dominant is a change to a reviewed library SVG and is escalated instead.

#### `rec-010` — Endo versus exo cannot be seen in a flat skeletal render

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `inst-008`, `visual-003`
- **Need:** Two assets claim in their titles and learning goals to show the endo orientation, and a flat RDKit depiction cannot: rendered at reader scale the endo adduct and its exo epimer are near-indistinguishable, and no exo structure exists in the package at all, so the contrast the section turns on has no second member. The concept's own first trouble spot is that students confuse endo with cis.
- **Chosen intervention:** **static-image-sequence**
- **Why this is the least-complex sufficient option:** The need is depth perception, which the current representation cannot supply at any description length. A two-panel stacked-approach comparison is the least-complex thing that carries it; the deferred endo/exo video's storyboard already specifies it. Recorded rather than applied, as new-asset work.

#### `rec-011` — The only Cope figure is the boat exception, while a question marks 'boat' wrong

- **Severity:** medium · **target surface:** assessment
- **Consolidates:** `inst-010`, `visual-010`
- **Need:** The chapter's single Cope asset is cis-1,2-divinylcyclobutane, whose own description explains that the ring tether forces a boat-like transition state. The chair transition state taught as the norm is drawn nowhere, and ch30-aromatic-claisen-reasoning grades 'chair' correct and 'boat' wrong - so a student who studied the chapter's only Cope picture and answered 'boat' is penalised for having read it.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** Two needs sit here. The grading trap is a verified defect and is fixed now by making the 'boat' wrong-answer explanation name the divinylcyclobutane case explicitly, so a student who reasoned from the figure is corrected rather than merely marked wrong. Adding a plain 1,5-diene Cope figure, and drawing the chair array, are new-asset needs and are recorded.

#### `rec-012` — No question in a chapter about spatial relationships shows a structure

- **Severity:** medium · **target surface:** assessment
- **Consolidates:** `inst-005`, `visual-012`
- **Need:** All 22 items are answered by parsing text; the two 'molecule'-tagged items are tagged for the student's own canvas, not a stimulus. The endo/cis discrimination item asks about an adduct it never shows, and the rank_order item describes maleic anhydride in words although the asset exists in the same package. Every stereochemical item therefore begins with an un-assessed name-to-geometry translation.
- **Chosen intervention:** **new-figure**
- **Why this is the least-complex sufficient option:** This is a reuse need rather than an authoring need - the 36 figures the chapter already has include every structure involved - but wiring stimulus figures into question stems changes the items themselves, so it is recorded rather than applied.

#### `rec-013` — Turning images off deletes the text equivalents along with the figures

- **Severity:** medium · **target surface:** prose
- **Consolidates:** `access-005`
- **Need:** The reader's showImages preference drops whole blocks whose type is molecule, reaction, reaction_coordinate or image - 32 of this chapter's 36 assets - and their alt_text and long_description go with them. The worst-affected section loses 9 of 12 blocks and with them every description of which face each methyl group ends on. A learner who turns images off to reduce clutter silently loses the chemistry.
- **Chosen intervention:** **text-equivalent**
- **Why this is the least-complex sufficient option:** Platform: the fix belongs in the reader's applyPrefs, which should suppress the image and keep its description rather than dropping the block. No authoring change in this chapter can prevent it. Escalated.

#### `rec-014` — The energy diagram's authored long description never reaches the reader

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `access-004`
- **Need:** The asset carries a 152-word long_description, the compiler puts it in the block, and ReactionCoordinateCard reads only alt_text - the one figure type in the chapter whose extended equivalent is authored and then dropped, while StructureCard renders it for every molecule and reaction.
- **Chosen intervention:** **longer-description**
- **Why this is the least-complex sufficient option:** Platform: a one-line renderer change to pass long_description through, matching what the sibling card already does. Escalated; nothing to fix in the package.

#### `rec-015` — Wavefunction phase is carried by hue alone in all four orbital figures

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `access-003`
- **Need:** The committed library SVGs distinguish positive from negative lobes only by fill colour, with no plus/minus glyph, hatch or stroke difference, although every manifest declares positiveLabel '+' and negativeLabel '-'. The two hues are close in luminance, so the distinction collapses in greyscale, in print and for achromatopsia - and it is the single quantity the chapter's whole argument turns on.
- **Chosen intervention:** **structured-chemical-description**
- **Why this is the least-complex sufficient option:** The right fix is to draw the declared phase labels, which is a change to reviewed library assets and outside this chapter's scope. What this chapter already does mitigates it substantially: every orbital figure's long_description states the phase relationship in words and is rendered as visible body text, so the information is not lost - only the redundancy is. Escalated as a library change.

#### `rec-016` — Unicode subscripts in question text reach the DOM unconverted

- **Severity:** medium · **target surface:** assessment
- **Consolidates:** `access-006`
- **Need:** 41 subscripts and 7 superscripts across eight questions are handed to plain Text by five activity renderers that never call the ChemText conversion the reader's prose path uses, so a screen reader may drop the hydrogen counts and read orbital indices as a bare 'psi'. Every affected item also gives the compound name, so nothing is unanswerable.
- **Chosen intervention:** **text-equivalent**
- **Why this is the least-complex sufficient option:** Platform: ChemText already exists and is used by six other renderers; the fix is to route these five through it. Authoring around it by spelling formulas out in words would make the questions worse for everyone else. Escalated.

#### `rec-018` — The [i,j] count is never worked for a ring, which is where the question asks it

- **Severity:** medium · **target surface:** prose
- **Consolidates:** `inst-009`
- **Need:** The chapter defines the counting rule on an acyclic pentadiene and then asks about 5-methylcyclopentadiene, where the donor and acceptor carbons are directly bonded through the ring. Two places in the package describe the same shift incompatibly - 'bonds to the far end of the diene' versus 'moves to an adjacent carbon' - and the chapter never says that the indices follow the reorganising array rather than the shortest path through the ring. The question's own distractor list anticipates [1,2] and [1,3], so the error was expected.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** The missing sentence is one rule, and stating it resolves both the pedagogical gap and the apparent contradiction between the two descriptions. Cheaper and more complete than adding a figure.

#### `rec-019` — Five descriptions claim to show things their figures do not

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `access-009`, `access-010`, `access-011`, `visual-015`, `visual-011`
- **Need:** The steroid descriptions narrate rings 'labelled A through D' on renders that carry no labels; the pi* description omits the unequal lobe sizes the SVG visibly draws; both matching_pairs accessible descriptions describe left and right columns although the renderer emits one labelled dropdown per item; the prephenate figure's learning goal claims the suprafacial outcome is visible when the two rings are drawn in non-corresponding orientations; and the vitamin D pair is auto-laid-out so differently that the ring-B opening cannot be seen.
- **Chosen intervention:** **sufficient-alt-text**
- **Why this is the least-complex sufficient option:** These are description defects, not figure defects, and each is fixed by making the description honest about what the drawing shows - either by naming the convention as a convention or by dropping a claim of visibility the render cannot support. Re-laying out the steroid figures to a common orientation would be the better outcome for the vitamin D pair but requires per-figure coordinate control the molecule asset type does not expose, so that part is recorded.

#### `rec-020` — Three learning objectives have no live assessment, and the two hardest concepts open at advanced

- **Severity:** medium · **target surface:** practice
- **Consolidates:** `inst-012`, `struggle-009`
- **Need:** Sigmatropic electron counting used to decide a pathway, why [1,5]-H is common and [1,3]-H is not, predicting a Claisen product, and drawing the ethylene phase pattern all lack a surfaced item. Separately, eight of ten concepts have no core-difficulty question, and diels-alder-stereochemistry and cope-and-claisen are each tested only at advanced - so a student's first contact with the two hardest sections is the hardest item format.
- **Chosen intervention:** **added-practice**
- **Why this is the least-complex sufficient option:** Both halves need new questions, which is question-bank expansion rather than error correction. Recorded with the specific objectives named so the gap is actionable.

#### `rec-021` — Two sections carry figures that spend the next section's payoff

- **Severity:** medium · **target surface:** prose
- **Consolidates:** `inst-007`, `visual-009`
- **Need:** The electrocyclic section's prose deliberately withholds the prediction ('the next section works out how to predict them') while the figure beside it is titled 'conrotatory' and defines and applies the motion in full. The sigmatropic section similarly carries both [3,3] figures, so a student meets 'Cope' and 'Claisen' as unexplained proper nouns one section before they are defined.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** Either the figure moves or the promise goes. Moving the figure would leave the electrocyclic section with no worked transformation, so the cheaper repair is to stop promising a payoff the section has already spent - recorded rather than applied, since it is a judgement about pacing rather than a factual error.

#### `rec-022` — The chapter's heaviest section is one long paragraph plus nine look-alike cards

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `struggle-007`, `visual-004`, `struggle-008`
- **Need:** Section 5 delivers four canonical results, two electron counts, two conditions, two rotation modes, a meso-versus-racemate aside and a vocabulary caution in a single 550-word block with no internal heading, followed by six molecule cards that all look alike and whose pairings exist only inside their captions. Only the two thermal results are drawn as transformations; the photochemical ones are orphan product structures. The chapter's own question on this material is a 2x2 grid, so the assessment format and the figure layout disagree.
- **Chosen intervention:** **static-image-sequence**
- **Why this is the least-complex sufficient option:** The prose can be segmented cheaply, but the real need - seeing the four results as one comparison with substrate, condition and product adjacent - is a layout or figure need. Recorded together so the two halves are not solved separately.

#### `rec-023` — The chapter has no [2+2] figure although the forbidden case is assessed

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `inst-011`
- **Need:** The thermally-forbidden / photochemically-allowed [2+2] contrast is one of the two pillars of the cycloaddition concept and is graded directly, yet both cycloaddition assets are Diels-Alder reactions. Nothing shows two alkenes, a cyclobutane, or the end-to-end sign mismatch that forbids the thermal case.
- **Chosen intervention:** **new-figure**
- **Why this is the least-complex sufficient option:** The counterexample is what gives the [4+2] result its meaning, and 'alkenes dimerise in sunlight but not in a hot flask' is the section's most memorable fact. A simple reaction figure would carry it; recorded as new-asset work.

#### `rec-024` — The s-cis gate is named as a trap and the one butadiene figure shows the non-reacting conformation

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `visual-008`
- **Need:** The chapter says three times to check whether the two ends can reach each other before applying any symmetry rule, and RDKit lays butadiene out in the extended, s-trans-like zigzag, so the single picture of the reference diene shows the conformation that cannot react. The octatriene reaction figure is likewise drawn fully extended.
- **Chosen intervention:** **new-figure**
- **Why this is the least-complex sufficient option:** This is the cheapest missing figure in the chapter and the one whose absence most directly misleads, because the drawn conformation actively contradicts the reacting one. Recorded rather than applied: forcing a coiled depiction needs coordinate control the molecule asset type does not expose.

#### `rec-026` — The chapter assumes stereochemistry and aromaticity vocabulary with no route back

- **Severity:** medium · **target surface:** instructor-support
- **Consolidates:** `struggle-010`
- **Need:** Every concept's prerequisites point only inside this chapter and concept 1's is empty, yet the default text uses meso, internal mirror plane, racemic, E/Z, s-cis, ring strain, tautomerisation and the aromaticity argument with no gloss. The only textbook link is the generic chapter landing page, and the section-5 'read more' is the Woodward-Hoffmann Wikipedia article, which is harder than the chapter.
- **Chosen intervention:** **instructor-note**
- **Why this is the least-complex sufficient option:** A named refresher list is cheaper and more useful than glossing each term inline, and it belongs where an instructor can act on it. Recorded.

#### `rec-029` — Several sections repeat structures already drawn inside an adjacent reaction card

- **Severity:** medium · **target surface:** figure
- **Consolidates:** `visual-013`, `visual-005`
- **Need:** The biology section carries eight cards for three transformations, with all five molecule cards also appearing inside the three reaction cards; the Diels-Alder section repeats three species that are inside its own reaction figure; mol-butadiene appears as an identical card in four sections. Long runs of near-duplicates push the figures that carry unique information further from the sentence they support.
- **Chosen intervention:** **sufficient-alt-text**
- **Why this is the least-complex sufficient option:** Deliberately NOT acted on. Each standalone card carries its own long_description, and removing the card removes a text equivalent the reaction card's description does not replace - so the cheapest-looking fix would trade a usability gain for an access loss. Kept as a documented disagreement instead; if these are ever pruned, the descriptions must be preserved first.

#### `rec-025` — A numeric placeholder sits next to the answer's neighbourhood

- **Severity:** low · **target surface:** assessment
- **Consolidates:** `struggle-012`
- **Need:** ch30-triene-filled-pi-mos answers 3 and shows the placeholder 'e.g. 5', on a prompt that says 'six' twice - so on one of only two core-difficulty items a low-confidence student may anchor on the example or second-guess a correct 3.
- **Chosen intervention:** **prose-edit**
- **Why this is the least-complex sufficient option:** A placeholder should demonstrate format, not magnitude; changing it to a value that cannot be mistaken for an answer is a one-token fix.

#### `rec-027` — The reader's heading outline skips h3 in every section

- **Severity:** low · **target surface:** prose
- **Consolidates:** `access-007`
- **Need:** Section titles render as h2 and every figure card title as h4, with no h3 anywhere, so a screen-reader user navigating by heading level meets a gap at each of the ten sections - and with 36 figure cards it is encountered constantly.
- **Chosen intervention:** **keyboard-alternative**
- **Why this is the least-complex sufficient option:** Platform: a heading-level change in the reader components, not something a package can influence. Escalated.

#### `rec-028` — The video briefs lean on colour and promise no accessible equivalent

- **Severity:** low · **target surface:** interactive
- **Consolidates:** `access-012`
- **Need:** All five briefs are deferred and degrade cleanly today, but their storyboards carry meaning in 'contrasting colour', 'phase colours' and 'recolouring', their narration outlines assert outcomes without describing the visual events, and none mentions captions, audio description or pause and step controls.
- **Chosen intervention:** **transcript**
- **Why this is the least-complex sufficient option:** Nothing degrades until the animations are produced, so the cheapest effective action is to fix the briefs now, before production, rather than remediate finished video later. Recorded as a production precondition.

#### `rec-030` — The basis p orbital is drawn on a molecule whose pi bond is already formed

- **Severity:** low · **target surface:** figure
- **Consolidates:** `visual-014`
- **Need:** orb-carbon-p-orbital establishes the building block before anything is combined, but the ethene preset draws the C=C as a full double line and the overlay sits on one carbon only, so the picture competes with a reading of 'one half of the pi bond already drawn'.
- **Chosen intervention:** **sufficient-alt-text**
- **Why this is the least-complex sufficient option:** The figure's real job - preventing the phase-as-charge misconception - is done well by its description, and the ambiguity is mild. The preset is a reviewed library asset, so the least-complex sufficient action is to let the description carry the distinction, which it already partly does.

### Merged duplicates

Findings from different personas about the same location, consolidated into one recommendation keeping the strongest severity and every learner impact:

- **rec-001** (blocker) merges `struggle-001`, `struggle-011` — raised independently by: Struggling Student.
- **rec-002** (high) merges `inst-001`, `struggle-002`, `visual-001`, `struggle-006`, `access-008` — raised independently by: Accessibility Persona, Learner with Visual Preference, Organic Chemistry Instructor, Struggling Student.
- **rec-003** (high) merges `inst-002`, `visual-002` — raised independently by: Learner with Visual Preference, Organic Chemistry Instructor.
- **rec-004** (high) merges `inst-003`, `access-001` — raised independently by: Accessibility Persona, Organic Chemistry Instructor.
- **rec-005** (high) merges `access-001`, `access-002` — raised independently by: Accessibility Persona.
- **rec-006** (high) merges `inst-004`, `struggle-003`, `inst-014` — raised independently by: Organic Chemistry Instructor, Struggling Student.
- **rec-007** (medium) merges `inst-006`, `inst-013` — raised independently by: Organic Chemistry Instructor.
- **rec-010** (medium) merges `inst-008`, `visual-003` — raised independently by: Learner with Visual Preference, Organic Chemistry Instructor.
- **rec-011** (medium) merges `inst-010`, `visual-010` — raised independently by: Learner with Visual Preference, Organic Chemistry Instructor.
- **rec-012** (medium) merges `inst-005`, `visual-012` — raised independently by: Learner with Visual Preference, Organic Chemistry Instructor.
- **rec-017** (high) merges `struggle-004`, `struggle-005` — raised independently by: Struggling Student.
- **rec-019** (medium) merges `access-009`, `access-010`, `access-011`, `visual-015`, `visual-011` — raised independently by: Accessibility Persona, Learner with Visual Preference.
- **rec-020** (medium) merges `inst-012`, `struggle-009` — raised independently by: Organic Chemistry Instructor, Struggling Student.
- **rec-021** (medium) merges `inst-007`, `visual-009` — raised independently by: Learner with Visual Preference, Organic Chemistry Instructor.
- **rec-022** (medium) merges `struggle-007`, `visual-004`, `struggle-008` — raised independently by: Learner with Visual Preference, Struggling Student.
- **rec-029** (medium) merges `visual-013`, `visual-005` — raised independently by: Learner with Visual Preference.

### Retained disagreements

Both positions are kept verbatim; the minority view is never deleted.

#### Whether the standalone molecule cards that duplicate species already drawn inside an adjacent reaction card should be removed

- **Learner with Visual Preference:** Several sections pad their figure list with verbatim repeats - the biology section carries eight cards for three transformations, with all five molecule cards also appearing inside the three reaction cards, and mol-butadiene appears as an identical card in four sections. Long runs of near-duplicate cards make the figure strip feel like an appendix and push the figures that carry unique information further from the sentence they support; a learner who has learned that the cards repeat stops reading them. (Flagged with the caveat that each carries its own long_description and the Accessibility persona may take the opposite position.)
- **Accessibility Persona:** Did not file this as a defect, and the reasoning cuts the other way: the reader surfaces long_description as visible body text for every molecule and reaction block, so each standalone card is an independent text equivalent. A reaction card's single description does not decompose into per-species descriptions, and suppressing figures already destroys text equivalents elsewhere (access-005).

**Orchestrator resolution:** Not acted on, and recorded as rec-029 with the disagreement intact. The visual-redundancy cost is real but reversible - a reader can scroll past a repeated card - whereas removing a card removes a description that nothing else supplies, which is not reversible for the learner who depended on it. The visual persona itself anticipated this and framed its finding as a need rather than a removal. If these are ever pruned, the per-species descriptions must be folded into the surviving reaction card's description first.

#### Whether declining to draw the polyene molecular orbitals was the right call

- **Accessibility Persona:** It is the chapter's single best authoring decision: making the node-count and terminal-lobe-parity rule the primary representation 'removes what would otherwise have been this chapter's biggest non-visual barrier' and means the load-bearing content is text-first for every learner.
- **Learner with Visual Preference:** The stated justification is honest but 'over-covers': an energy ladder with occupancy, a phase pattern on four circles, a rotation-sense sketch and an endo/exo sketch are none of them orbital-lobe cartoons, and the `diagram` asset type already exists and is used zero times, so the prohibition on new orbital SVGs did not require carrying the whole thing in prose.

**Orchestrator resolution:** Both are right and the resolution is additive rather than a choice. The prose rule stays as the primary and accessible representation - it is listed under sufficient_as_is precisely so no one deletes it when a figure arrives - and rec-002 adds a phase-sign schematic as redundancy for learners who reason by inspection. The visual persona is also factually correct that the constraint was read too broadly: the ban covers orbital-lobe SVGs authored in-app, not a hand-built sign-pattern diagram, and that distinction should be recorded for the next chapter that hits the same limit.

#### How serious the expanded-tier gap is

- **Struggling Student:** A publication blocker: on default settings the required step of learning what conrotatory means is 'genuinely impossible from the delivered default view', and the slider that would fix it is unsignposted and inverted in effect.
- **Organic Chemistry Instructor:** Filed no finding on it at all and scored the chapter 7.6 with no blockers, noting only as an open question which tier the reader renders by default - an instructor reading all three tiers sees a complete chapter.

**Orchestrator resolution:** The struggling student's reading is upheld and drives the verdict. The instructor's view is what the package looks like to someone who reads the source; the student's is what the compiled default actually delivers, and the compiled default is what ships. Verified directly: the reader's default detailLevel is 'expanded', and a term-by-term check confirmed that 8 of 10 load-bearing definitions appear only in the standard tier, with 0 of 10 nuggets carrying expanded as a superset of standard. The gap is real, it is this chapter's to fix, and it is corrected in this pass.

### Places where a description is sufficient (no new asset)

Listed explicitly so nothing here gets over-built:

- The polyene molecular orbitals as an ACCESSIBLE representation: the node-count and terminal-lobe-parity rule in prose is sufficient and was praised as removing the chapter's largest non-visual barrier. rec-002 adds a redundant visual for learners who reason by inspection - it does not replace the prose rule, and the prose rule must survive any figure that is added.
- All 36 alt_texts and long_descriptions are sufficient as written except the five specific mismatches in rec-019; no figure needs a longer description merely for length.
- The rank_order item's text-only cards are sufficient and were the right call, since rank_order does not render card structures - do not convert them to figures.
- The deferred videos' current handling is sufficient: hidden blocks with empty urls, so no learner meets a dead player. They need no interim placeholder.
- orb-carbon-p-orbital's phase-versus-charge job is fully carried by its existing description (rec-030); the mild basis-orbital ambiguity does not warrant a new asset.
- The comparison_matrix accessible description already matches the rendered table orientation exactly and should be left alone.

### Visual opportunities

- rec-002 - a phase-sign schematic for butadiene psi-2 and hexatriene psi-3 with nodes marked between carbons; expressible today as a `diagram` asset without touching the prohibited orbital-SVG library.
- rec-003 - a static two-panel comparison of conrotatory and disrotatory closure of the same starting frame, liftable from the deferred video's storyboard.
- rec-010 - a two-panel endo/exo stacked-approach comparison, plus the two-barrier energy sketch that makes the kinetic-versus-thermodynamic point visible.
- rec-022 - the four canonical electrocyclic results laid out as one 2x2 comparison with substrate, condition and product stereochemistry adjacent, matching the shape of the question that assesses them.
- rec-023 - a [2+2] figure showing two alkenes and the end-to-end sign mismatch that forbids the thermal case.
- rec-024 - the s-cis and s-trans arrangements of the same diene side by side, since the only butadiene figure currently shows the conformation that cannot react.
- rec-005 (visual half) - an energy ladder with occupancy for psi-1 to psi-4 before and after promotion, which the HOMO/LUMO section currently has no figure of its own for.

### Accessibility blockers

None. The Accessibility persona reported no publication blocker: every surfaced question is answerable from text alone, every concept retains a keyboard-complete item, both drawing items allow typed entry with a gradeable key, and all 66 hints are text or worked_step. The access findings that remain are a missing confirmation loop (`access-001`, `access-002`), phase redundancy (`access-003`), and four platform defects (`access-004` – `access-007`) — barriers to degrees of access, not to access itself. This is an AI review, not an audit of record, and makes no claim of formal WCAG conformance either way.

### Regression targets for next run

No prior `chapter-review.json` existed, so this run is the baseline and the regression block is empty. Recheck these stable ids after revision:

- **Corrected in this pass, expect resolved:** `struggle-001`, `struggle-011`, `inst-004`, `inst-006`, `inst-009`, `inst-013`, `inst-014`, `visual-006`, `visual-007`, `struggle-003`, `struggle-012`, `access-009`, `access-010`, `access-011`, and the grading-trap half of `inst-010`.
- **Expect unchanged until new assets are authored:** `inst-001`, `inst-002`, `inst-008`, `inst-011`, `struggle-002`, `struggle-006`, `struggle-007`, `struggle-008`, `visual-001`, `visual-002`, `visual-003`, `visual-004`, `visual-005`, `visual-008`, `visual-010`, `visual-011`.
- **Expect unchanged until the platform changes:** `access-001`, `access-003`, `access-004`, `access-005`, `access-006`, `access-007`, `inst-003`, `struggle-004`, `struggle-005`, `orch-001`.
- **Expect unchanged until the question bank is extended:** `inst-005`, `inst-012`, `struggle-009`, `visual-012`.


---
## Post-correction record

**Estimated state: major revision (not a second persona verdict).**

The baseline verdict and every persona finding above are preserved unchanged. The blocker is resolved and verified; the estimate stays at `major revision` because roughly a dozen high-severity findings remain open, several of them raised independently by three personas. A new verdict requires a fresh four-persona regression run.

### Changes applied (14)

- Made the `expanded` text tier a superset of `standard` in all ten nuggets. The reader defaults to the expanded tier, and this chapter had authored expanded as commentary ON standard rather than a superset OF it, so a student on default settings was never given the definitions of conrotatory, disrotatory, HOMO, LUMO, suprafacial, antarafacial, the [i,j] counting procedure, the 4n vs 4n+2 rule, or 'electrocyclic reaction' itself. Verified after the change: all twelve load-bearing definitions are now present in the default tier and 10 of 10 nuggets carry standard within expanded, in the order define-then-comment.
 - **Resolves:** `struggle-001`, `struggle-011`
 - **Partially addresses:** `struggle-005`, `inst-014`
- Added the chapter's promised unifying principle as the close of the final nugget: the general Woodward-Hoffmann selection rule stated in terms of electron count and facial relationship, named as such, plus the translation that makes the three family rules one rule (a disrotatory closure is the suprafacial option, a conrotatory one the antarafacial). 'Woodward-Hoffmann' now reaches student-facing prose for the first time.
 - **Resolves:** `inst-004`, `struggle-003`
 - **Partially addresses:** `inst-014`
- Removed three forward references to a selection-rule 'table' the platform has no block type for and the chapter never showed: section 2 now promises to generate 'every one of the electrocyclic selection rules', section 3 says each rule 'comes in two versions' rather than referring to tables with two rows, and the section-5 prose and the concept trouble spot now say 'the four cases' rather than 'the four boxes of the table'.
 - **Resolves:** —
 - **Partially addresses:** `struggle-003`
- Corrected the OpenStax crosswalk note, which claimed every numbered section of chapter 30 was represented by a concept. Section 30.9 is not a concept; the note now says so and states that its content is delivered as the closing statement of the final concept and linked from Additional Reading.
 - **Resolves:** —
 - **Partially addresses:** `inst-004`
- Removed two assertions of a thermal four-electron ring closure, which contradicted this chapter's own corrected teaching that cyclobutene strain makes opening the thermally accessible direction. The ring-size sort no longer calls the closure thermal and now says explicitly that the item is only about counting; the photochemical-closure distractor explanation now names the conrotatory motion and points out that the thermal direction for that compound is the ring OPENING, instead of calling the trans isomer 'the product of the thermal closure'. This contradiction was introduced during production when the reaction direction was corrected in the prose without grepping the question bank.
 - **Resolves:** `inst-006`
- Restored the missing 'trans-' descriptor on '3,4-Dimethylcyclobutene opening to (2E,4E)-hexa-2,4-diene' in the electron-count sorting variant. Only the trans diastereomer gives the E,E diene on conrotatory opening.
 - **Resolves:** `inst-013`
- Changed the reaction-coordinate asset's barrier from 'high' to 'large'. 'high' is not a member of the renderer's enum (small | medium | large) and was silently coerced to medium, so the figure drew an unremarkable barrier while its title, alt text, long description and the surrounding prose all described a high one.
 - **Resolves:** `visual-007`
- Rewrote orb-ethylene-pi's long description to match what the committed SVG actually draws: four discrete lobes plus two faint spanning clouds, with the spanning cloud identified as the feature that carries continuity, and an explicit comparison to the antibonding figure (same four lobes, no clouds, dashed node, phase reversal). The description previously claimed merged continuous lobes.
 - **Resolves:** `visual-006`
- Added the rule that the [i,j] indices are counted along the reorganising conjugated array rather than by the shortest route through the molecule, worked on the cyclopentadiene case the question actually asks about, and reconciled mol-5-methylcyclopentadiene's description with the question prompt so the two no longer appear to contradict each other about where the hydrogen goes.
 - **Resolves:** `inst-009`
- Rewrote the 'boat' wrong-answer explanation on the aromatic Claisen reasoning item so that a student who answered 'boat' after studying the chapter's only Cope figure - which is the ring-tethered divinylcyclobutane case, genuinely a boat - is corrected rather than merely marked wrong. The explanation now names that substrate and explains why an open-chain [3,3] system folds into a chair instead.
 - **Resolves:** —
 - **Partially addresses:** `inst-010`
- Fixed five descriptions that claimed to show things their figures do not: the steroid ring letters A-D are now flagged as the naming convention rather than drawn labels (three molecules and one reaction), the pi-star description now accounts for the unequal lobe sizes the SVG visibly draws and says why carbon's are larger, both matching_pairs accessible descriptions now describe the labelled-chooser-per-item control the renderer actually emits instead of two columns, and mol-prephenate's learning goal no longer claims the suprafacial outcome is visible in a render whose two rings are drawn in different orientations.
 - **Resolves:** `access-009`, `access-010`, `access-011`, `visual-015`
 - **Partially addresses:** `visual-011`
- Changed the numeric placeholder on both hexatriene orbital-count items from 'e.g. 5' to 'whole number, e.g. 12', so the greyed-out example no longer sits next to the answer (3) on a prompt that says 'six' twice.
 - **Resolves:** `struggle-012`
- Added a typed_structure_entry_note to both drawing items - a field the renderer already displays - giving the SMILES notation for expressing which face each methyl group is on, with the two diastereomeric forms written out, plus permission to describe the relationship in words for hand marking. The typed route was declared and gradeable but the learner was never told how to say cis or trans in it.
 - **Resolves:** —
 - **Partially addresses:** `access-002`, `access-001`
- Added an instructor note to both drawing items recording that a wrong-diastereomer or stereochemistry-free submission is routed to manual review rather than marked incorrect, and that the authored wrong-answer explanations will therefore not be shown automatically - so the behaviour is expected rather than discovered in a review queue.
 - **Resolves:** —
 - **Partially addresses:** `inst-003`

### Verification

- Topic-package compiler (proprietary toolchain, not in this repo) — clean: 10 concepts, 10 nuggets, 36 assets, 5 videos, 13 textbook mappings, 22 questions (11 surfaced / 11 staged, 10 types, 0 demo_eligible), zero science-review warnings, empty verification_required.
- Automated test suite — passed — 144 passed.
- Automated test suite — passed — 147 passed.
- `python .[internal source reference — not in this repo] --synthesized reports/topic-packages/orbitals-and-pericyclic-reactions/chapter-review.json` — valid.
- Blocker fix verified directly against the compiled package: all twelve load-bearing definitions (conrotatory, disrotatory, HOMO, LUMO, suprafacial, antarafacial, the [i,j] rule, 4n/4n+2, the three pericyclic features, the electrocyclic definition, the Woodward-Hoffmann name, the suprafacial/antarafacial bridge) are present in the default `expanded` tier, and 10 of 10 nuggets now carry `standard` within `expanded`.
- Aggregate-catalog check: topic-package-textbook-profiles.json held 390 chapter entries across 13 textbooks before and after the recompile, with no loss; frontend/public/deck-creator/manifest.json (38 chapters) and frontend/public/reader/topic-chapters/catalog.json (32 entries) both still carry the concurrently-compiled synthetic-polymers chapter as well as this one, so no unrelated aggregate churn was introduced.

### Still recommended (not applied)

- rec-002 / inst-001 + struggle-002 + visual-001 (high, three personas independently) - the terminal-lobe sign pattern of butadiene psi-2 and hexatriene psi-3 is still depicted nowhere. This is the chapter's single most valuable outstanding item, and the visual persona established that it does NOT require the prohibited orbital-SVG library: a phase-sign schematic is expressible today as a `diagram` asset, which this chapter uses zero times.
- rec-003 / inst-002 + visual-002 (high) - conrotatory versus disrotatory motion is still carried only by two verbal analogies; the deferred video remains the only planned depiction.
- rec-017 / struggle-004 + struggle-005 (high) - the thirty authored trouble spots and ten worked practice_checks still reach no student. This is a compiler and reader capability gap, not an authoring omission, and is the largest remaining gap between what the package contains and what a learner receives.
- rec-004 / inst-003 and rec-005 / access-001 (high) - a stereochemistry mismatch still escalates to manual review with no score, and the typed-structure read-back still cannot express stereochemistry. Both need platform changes; the chapter-side mitigations (instructor note, notation note) are applied above.
- rec-010, rec-023, rec-024, rec-022, rec-005 visual half (medium) - endo/exo, the [2+2] counterexample, the s-cis gate, the four-canonical-results comparison and an MO energy ladder all still need figures.
- rec-013, rec-014, rec-015, rec-016, rec-027, orch-001 (platform) - figures stripped with their text equivalents when images are off; the energy diagram's long description dropped by the reader; phase carried by hue with the declared +/- labels never drawn; Unicode subscripts unconverted in five question renderers; the h2-to-h4 heading gap; and en-dash hrefs relying on client percent-encoding.
- rec-012, rec-020 (medium) - questions still carry no structure stimuli, three learning objectives still have no live assessment, and the two hardest concepts still open at advanced with no core rung.
- rec-021, rec-026, rec-028, rec-029, rec-030 - sequencing, prerequisite signposting, video-brief accessibility preconditions, the duplicate-figure disagreement, and the basis-orbital ambiguity, all recorded and deliberately not acted on.

### Scope discipline

Corrections were confined to verified errors and bounded fixes: chemical and factual contradictions, descriptions that misdescribed their own figures, an invalid enum value, a false coverage claim, unkept forward references, an answer-adjacent placeholder, and two authorable notes that make an existing accommodation self-sufficient. Deliberately NOT done: authoring the five or six new figures the visual and instructor personas asked for, expanding the question bank, changing reader or grader platform behaviour, or pruning the duplicate figure cards - that last one because the Visual Preference and Accessibility lenses genuinely conflict on it and the disagreement is recorded rather than silently resolved in favour of one side.


---
## Second correction pass — figures, scaffolding delivery, and publication

**Estimated state: ready with minor revisions (not a second persona verdict).**

Not a new persona verdict. The blocker was resolved in the first pass; this pass closed the highest-severity remaining items — the missing frontier-orbital figure that three personas raised independently, the rotation-mode figure, the scaffolding that reached no student, the text equivalents destroyed by the images-off setting, the typed read-back that could not discriminate what it graded, and the three unassessed objectives plus the two missing core rungs. What remains is platform work (stereo grading escalation, the orbital library's hue-only phase, the energy-diagram description, subscript rendering, heading levels) plus three still-undrawn figures. Only a fresh four-persona regression run can issue a new verdict.

The baseline verdict and every persona finding above remain unchanged.

### Changes applied (7)

- Built the figure three personas independently asked for: `fig-polyene-frontier-lobes`, a phase-sign schematic of butadiene ψ2 and hexatriene ψ3 with every lobe's sign printed as a + or - glyph as well as coloured, every internode drawn between the atoms it separates, lobe heights proportional to the orbital coefficient, the two terminal lobes ringed, and the ψ1-to-ψ4 parity rule worked underneath. Built deterministically in [internal source reference — not in this repo]: every sign, node position and lobe size is computed from the Huckel coefficients c_r = sin(r j pi/(N+1)) and the derived node count and terminal relationship are ASSERTED against the chemistry the chapter teaches, so a figure contradicting the prose cannot be written. Rasterised and visually inspected before wiring in, which caught a first layout whose read-off text collided with the atom labels.
 - **Resolves:** `inst-001`, `struggle-002`, `visual-001`, `struggle-006`, `access-008`
 - **Partially addresses:** `visual-005`, `inst-014`
- Built `fig-electrocyclic-rotation-modes`: conrotatory and disrotatory closure of the same s-cis diene on an explicit four-column grid, with a curved arrow over each terminal carbon whose arrowhead direction encodes the rotation sense, and the product drawn with wedge/wedge for the cis outcome and wedge/hash for the trans. Replaces the motion the deferred video was going to carry.
 - **Resolves:** `inst-002`, `visual-002`
 - **Partially addresses:** `struggle-007`, `visual-004`
- The reader now delivers the authored scaffolding. reader_chapter_builder emits a warning callout per section carrying that section's concepts' trouble spots, placed directly under the prose that creates the risk, and a tip callout carrying the nugget's practice check with its worked answer, placed after the figures at the end of the section. All 30 trouble spots and all 10 practice checks now reach a student; previously they reached none. Three regression tests added.
 - **Resolves:** `struggle-004`, `struggle-005`
 - **Partially addresses:** `struggle-007`
- Turning images off no longer deletes the chemistry. TopicPackageChapterRenderer.applyPrefs previously dropped the whole block for molecule/reaction/reaction_coordinate/image when showImages was false, discarding alt_text and long_description with it — 32 of this chapter's figures. It now converts each suppressed figure into an info callout carrying its long description (falling back to alt text), so the text equivalents survive precisely the setting that makes them matter.
 - **Resolves:** `access-005`
- The typed-structure read-back can now discriminate what it grades. TypedStructureRenderer requested `sections: []`, and the intro-tier summary deliberately says nothing about stereochemistry (a contract its own tests enforce), so the read-back returned byte-identical text for the answer key and for the graded distractor. It now requests `sections: ["stereochemistry"]` and appends it. Verified: cis key, trans distractor and the stereochemistry-free skeleton now produce three different read-backs. Fixed in the caller rather than by redefining the intro tier, which would have changed prose for every other consumer.
 - **Resolves:** `access-001`
 - **Partially addresses:** `access-002`
- Six new surfaced questions with six variants (22 to 34 entries, 11 to 17 surfaced) closing the assessment gaps: sigmatropic electron counting used to decide a thermal suprafacial pathway; why a [1,5]-H shift runs and a [1,3]-H shift does not; predicting the Claisen product of an allyl vinyl ether and of an allyl aryl ether (typed entry allowed, with a note); a core-difficulty first-contact item on each of the two concepts that previously opened at advanced; and the ethylene π/π* phase pattern assessed as text-only reasoning so it needs no image stimulus. Core items rose from 2 to 5. Every new key was graded from the ideal submission and all 51 authored wrong-answer patterns were replayed as submissions to confirm none is dead.
 - **Resolves:** `inst-012`, `struggle-009`
 - **Partially addresses:** `inst-005`, `visual-012`
- Seeded to production question bank and flipped publishing.available to true. Re-running the seeder reports all 17 unchanged, confirming idempotency.
 - **Resolves:** —

### Verification

- Topic-package compiler (proprietary toolchain, not in this repo) — clean
- Automated test suite — 147 passed
- Automated test suite — 188 passed
- cd frontend && npx vitest run [internal source reference — not in this repo] [internal source reference — not in this repo] — 14 passed; npx tsc --noEmit clean on both touched components.
- Figures rasterised with cairosvg and visually inspected at reader width before wiring in; the Huckel-derived node counts and terminal-lobe relationships are asserted inside the builder.
- Typed read-back discrimination verified directly: the cis key, the trans distractor and the stereochemistry-free skeleton now return three different strings for both drawing items.
- Reader delivery verified on the compiled chapter: 20 callout blocks (10 warning carrying all 30 trouble spots, 10 tip carrying all 10 practice checks), 5 image blocks for the two new figures, 0 image blocks with an empty url.
- Proprietary toolchain verification (not in this repo)
- Aggregate catalogs preserved: topic-package-textbook-profiles.json held 403 chapter entries across 13 textbooks before and after; manifest.json (38 chapters) and reader catalog (32 entries) both still carry synthetic-polymers as well as this chapter.

### Still open

- rec-004 / inst-003 (high, platform) — a stereochemistry mismatch still escalates to manual_review with no score, so the authored wrong-answer explanations on the drawing items are not delivered automatically. Deliberately NOT changed: _MANUAL_REVIEW_CATEGORIES is a platform default and altering it would change grading on every drawing question in the corpus, including already-seeded chapters. The chapter-side mitigations (instructor note, typed-entry note) are in place and the read-back gap is now closed.
- rec-015 / access-003 (medium, library) — the four committed orbital-library SVGs still carry phase by hue alone, and their manifests still declare +/- labels that are never drawn. The two new figures in this chapter do print the glyphs, so the chapter is no longer wholly dependent on hue, but the library assets themselves are unchanged. They also remain reviewStatus scientific_review rather than verified, which is a chemistry-reviewer action.
- rec-014 / access-004 (medium, platform) — ReactionCoordinateCard still reads only alt_text and drops the authored long_description for the energy diagram.
- rec-016 / access-006 (medium, platform) — five question renderers still hand raw Unicode subscripts to the DOM instead of routing through ChemText.
- rec-027 / access-007 (low, platform) — the reader heading outline still jumps h2 to h4 with no h3.
- rec-010, rec-023, rec-024 (medium) — endo/exo stacking, the [2+2] counterexample and the s-cis gate are still undrawn. The endo/exo and [2+2] cases now have a working deterministic figure pipeline to build on ([internal source reference — not in this repo]).
- rec-021, rec-026, rec-028, rec-029, rec-030 — sequencing, prerequisite signposting, video-brief accessibility preconditions, the retained duplicate-figure disagreement, and the basis-orbital ambiguity: all still recorded and not acted on.
- No science review record exists, so the compiler warns that available is true without one. Left honest rather than fabricated: the reviewers here were AI personas, not a human of record, and every other live chapter in the repo (ch17, ch18, ch25) carries available: true with no review record either. A human sign-off should be recorded when it happens.

### Publication state

- Seeded to Supabase on 2026-07-31: **17 published items** and 17 staged variants, owned by user id 1. Re-running the seeder reports all 17 unchanged.
- `publishing.available` is now **True**, so the chapter is live on `/reader/organic/orbitals-and-pericyclic-reactions` and the Pending badge is cleared.
- No science review record was written. The reviewers in this workflow were AI personas rather than a human of record, and fabricating a reviewer entry would assert a sign-off that did not happen; the compiler's warning to that effect is expected and is the same state every other live chapter in the repo is in.

