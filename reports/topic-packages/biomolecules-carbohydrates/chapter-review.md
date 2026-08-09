# Chapter review — Biomolecules: Carbohydrates (`biomolecules-carbohydrates`)

_Reviewed 2026-07-30 · chapter version 1 · personas: Instructor, Struggling Student, Accessibility, Visual Preference_

**Publication readiness: blocked**

Chemically this is the strongest chapter reviewed in this series so far - the instructor persona machine-verified all 30 asset SMILES and all 34 distinct question structures, hydrolysed all four disaccharides in silico, and found 29 of 30 structures and every numeric claim correct, including the dual-anomeric sucrose linkage that carbohydrate chapters normally get wrong. It is nevertheless BLOCKED, on nine persona blockers in four groups. (1) Two verified wrong-chemistry defects: mol-beta-d-xylopyranose ships the ALPHA anomer, disproving the caption, the prose and a question key that all depend on it being all-equatorial; and a comparison_matrix cell keys 'free glucose survives prolonged 1 M NaOH', which the same chapter refutes two sections later via the Lobry de Bruyn-van Ekenstein rearrangement, so a student who read the chapter is marked wrong. (2) Two items that cannot be answered correctly by anyone: both curved_arrow questions expect a lone_pair source while the renderer emits site.kinds[0] = 'atom', and both chair items score full marks for placing a single substituent. (3) A graphical answer tell - two single_select items illustrate only the key - which is the ch15 defect class recurring, invisible to the text-only leak guard. (4) Required-access blockers: hotspot atoms are exposed only as RDKit indices ('C atom 5' is sugar C1) with no connectivity, and structure_scaffold offers a Ketcher iframe the registry itself marks not keyboard-complete, with no alternative and no disclosure. Beneath the blockers sit two structural themes all four personas reached independently: the chapter teaches three drawing conventions (Fischer, Haworth, chair) and draws none of them, and an entire authored layer - 10 practice checks, 31 long descriptions, 54 of 56 accessible descriptions - never reaches any learner because no renderer consumes it.

### Top blockers

- **[BLOCKER] beta-D-xylopyranose figure is actually the alpha anomer** — The figure carrying the chapter's all-equatorial-pentose argument must be the anomer the caption, prose and question key all name. (instr-001)
- **[BLOCKER] Base-stability matrix cell contradicts the chapter's own enediol chemistry** — The row must discriminate the two compounds the way the chapter's chemistry actually does - the acetal survives base, the free hemiacetal does not. (instr-002, ss-002)
- **[BLOCKER] Both curved_arrow items are ungradable as authored** — A correctly drawn arrow must grade correct through the interface the learner actually sees. (access-006)
- **[BLOCKER] Illustrated-option answer tell in four items** — The picture panel must carry no information about which option is correct. (vis-001, vis-002)
- **[BLOCKER] Both chair items score full marks for one placed substituent** — An item that claims to assess axial/equatorial placement across a ring must not be satisfiable by placing a single group. (instr-007, vis-009, access-009, ss-001)
- **[BLOCKER] Figure descriptions do not distinguish the figures they are asked to compare** — Two figures a learner is asked to compare must never resolve to the same words. (access-001, ss-005, vis-019)
- **[BLOCKER] Hotspot atoms are exposed only as RDKit indices** — Clicking an atom must be answerable from chemically meaningful targets, or an equivalent alternative must exist. (access-003)
- **[BLOCKER] structure_scaffold has no non-pointer response path** — A keyboard-only or screen-reader learner must be able to answer, or be told at assignment time that they cannot. (access-004)

### Top 5 recommended changes

1. **beta-D-xylopyranose figure is actually the alpha anomer** — The figure carrying the chapter's all-equatorial-pentose argument must be the anomer the caption, prose and question key all name. → **prose-edit** (figure, blocker)
2. **Base-stability matrix cell contradicts the chapter's own enediol chemistry** — The row must discriminate the two compounds the way the chapter's chemistry actually does - the acetal survives base, the free hemiacetal does not. → **prose-edit** (assessment, blocker)
3. **Both curved_arrow items are ungradable as authored** — A correctly drawn arrow must grade correct through the interface the learner actually sees. → **prose-edit** (assessment, blocker)
4. **Illustrated-option answer tell in four items** — The picture panel must carry no information about which option is correct. → **prose-edit** (assessment, blocker)
5. **Both chair items score full marks for one placed substituent** — An item that claims to assess axial/equatorial placement across a ring must not be satisfiable by placing a single group. → **alternate-activity** (assessment, blocker)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 7.6/10 | 2 | 29/30 structures and every number verified correct; two wrong-chemistry blockers and a positionally guessable bank |
| Struggling Student | 5.6/10 | 2 | Excellent prose and hint ladders; the chapter's own hardest step is asserted, not worked, and a keyed cell punishes reading the chapter |
| Accessibility Persona | 5.5/10 | 4 | Best non-visual prose in the series; four required-activity blockers and an entire authored description layer that reaches nobody |
| Learner with Visual Preference | 4.4/10 | 1 | Three concepts about drawings that are never drawn; one graphical answer tell; the only relationship figure draws the wrong relationship |

### Affected sections & assets

`anomers-and-mutarotation`, `carbohydrate-classification`, `ch25-anomer-comparison-v2`, `ch25-anomer-comparison`, `ch25-anomeric-effect-reasoning`, `ch25-assign-d-or-l`, `ch25-beta-glucose-chair`, `ch25-build-d-glucose-fischer`, `ch25-cellulose-vs-starch`, `ch25-disaccharide-linkage-match`, `ch25-draw-cyclic-hemiacetal`, `ch25-epimer-relationship`, `ch25-glycoside-error-repair-v2`, `ch25-haworth-beta-anomer`, `ch25-hemiacetal-bond-ledger`, `ch25-identify-anomeric-carbon-v2`, `ch25-identify-anomeric-carbon`, `ch25-identify-ketohexose`, `ch25-mutarotation-percent-v2`, `ch25-mutarotation-percent`, `ch25-mutarotation-profile`, `ch25-rank-stereocenter-count`, `ch25-reducing-sugar-select`, `ch25-ring-closure-arrow`, `cyclic-hemiacetal-formation`, `d-l-configuration-and-families`, `di-and-polysaccharides`, `fischer-projections`, `glycoside-formation`, `haworth-projections`, `mol-alpha-d-glucopyranose`, `mol-alpha-d-mannopyranose`, `mol-beta-d-glucopyranose`, `mol-beta-d-xylopyranose`, `mol-d-erythrose`, `mol-d-gluconic-acid`, `mol-d-glyceraldehyde`, `mol-dihydroxyacetone`, `pyranose-chair-conformation`, `rc-mutarotation`, `sugar-oxidation-and-reduction`, `video-fischer-to-haworth-to-chair`, `video-ring-closure`

---
## Full evidence

### Independent persona reports

_Presented separately and unmerged. Each reviewer saw only its own rubric._

#### Organic Chemistry Instructor — 7.6/10 (blockers: instr-001, instr-002)

Not-go as it stands, but the gap to publishable is small and surgical. This is the most chemically careful carbohydrate chapter I have reviewed here: I parsed all 30 molecule SMILES in assets[] plus all 34 distinct SMILES in question student_config with RDKit, assigned CIP labels, and additionally hydrolysed all four disaccharides in silico against verified monosaccharide references - maltose, cellobiose, lactose and sucrose are all correct in sugar identity, linkage carbon AND anomeric configuration, which is where chapters of this kind normally fail. Every numeric claim I could check is right, and the authoring even gets the hard details right - ribitol is correctly named without a D- prefix while D-arabinitol is correctly chiral, and the chapter's own 'beta = same face as the reference arm' rule survives the furanose test I ran on beta-D-fructofuranose in 3D. Three things block assignment. (1) mol-beta-d-xylopyranose is drawn as alpha-D-xylopyranose, so the one figure the chapter uses to make its all-equatorial point shows an axial anomeric hydroxyl and contradicts its own caption, the prose, and a question key. (2) The comparison_matrix answer key asserts that free beta-D-glucopyranose survives prolonged 1 M NaOH, flatly contradicting the Lobry de Bruyn-van Ekenstein passage the same chapter teaches two sections later. (3) The chapter's closing claim that humans secrete no beta-glucosidase at all is an exceptionless rule the chapter itself breaks by naming lactase. Separately, the question bank is positionally guessable: every single_select keys to option 'a', every matching_pairs is perfectly diagonal, every rank_order ships pre-sorted, and every structured_reasoning claim is both first-listed and longer than its distractors - and I found no shuffling in any renderer.

**Strengths**

- Stereochemical fidelity of the monosaccharides is excellent: all 30 molecule SMILES machine-verified with rdCIPLabeler, and 29 of 30 carry exactly the configuration their title, alt text and prose claim - including alpha- versus beta-D-glucopyranose, beta-D-galactopyranose, alpha-D-mannopyranose, beta-D-ribofuranose, beta-D-fructofuranose with its quaternary anomeric carbon, both methyl glucosides, and 2-deoxy-D-ribose where the CIP descriptor legitimately flips relative to ribose.
- All four disaccharides survive in-silico hydrolysis against verified references, with the correct anomeric configuration of the donor ring in all four and the dual-anomeric 1-to-2 linkage of sucrose right. This is the thing carbohydrate chapters usually get wrong.
- The chapter states its alpha/beta rule against the sugar's reference arm rather than as 'beta is up', and explicitly claims the arm-based version survives translation to furanoses. Tested in 3D: in beta-D-fructofuranose the anomeric OH does sit on the same face as the C6 arm. The pedagogical claim is not just careful, it is correct.
- Numeric claims check out across the board: rotations for glucose and galactose, sucrose inversion, the 0.9 kcal/mol A-value and the 20 percent it predicts, 2^n stereoisomer counting, amylose's 6-residue helix, amylopectin's 25-residue branching and glycogen's 3-fold denser branching.
- Two easily-missed alditol subtleties are handled correctly: ribitol is labelled without a D- prefix (confirmed meso) while D-arabinitol is correctly treated as chiral.
- Assessment breadth is genuinely strong: 28 base items plus 28 variants across 19 question types, every one of the 10 concepts assessed, and the type choices are apt.
- Two defect classes that recurred in earlier chapters are fixed here: error_repair answer keys carry both the target_id and expected_target forms, and every numeric_with_units tolerance uses the {mode, amount} dict shape.
- The Kiliani-Fischer synthesis_route items are chemically exact - D-arabinose verified, the gluco cyanohydrin correct, the partial reduction correctly specified, and the epimeric pairs correctly stated.
- The prose repeatedly builds mechanism rather than asserting outcome: the entropic argument for intramolecular hemiacetal formation, the planar-carbonyl argument for mutarotation, the n-to-sigma* geometry of the anomeric effect, and the ring-flip cost argument for galactose's axial C4.

| id | sev | category | location | observation |
|---|---|---|---|---|
| `instr-001` | blocker | chemical-accuracy | `mol-beta-d-xylopyranose` | The SMILES on mol-beta-d-xylopyranose is alpha-D-xylopyranose, not beta. Its anomeric configuration is inverted relative to the named compound. Two independent checks agree: its RDKit canonical form matches an alpha reference built by inverting only the anomer… |
| `instr-002` | blocker | chemical-accuracy | `ch25-anomer-comparison-v2` | The answer key marks feature f_base as 'yes' for case_sugar (free beta-D-glucopyranose): the free sugar is asserted to survive prolonged 1 M aqueous NaOH at room temperature. It does not. A free reducing sugar in 1 M hydroxide opens to the aldehyde, is deproto… |
| `instr-003` | high | misconception | `nugget-di-and-polysaccharides` | This exceptionless claim is stated three times (standard tier, expanded tier, and the nugget practice_check answer) and it is not exceptionless. Humans express lactase-phlorizin hydrolase at the brush border, whose phlorizin-hydrolase domain is a beta-glucosid… |
| `instr-004` | high | assessment-readiness | `ch25-identify-ketohexose` | The correct answer is encoded in position across essentially the whole bank. All 12 single_select items key to option 'a' (first-listed). Both 5-option multi_selects other than ch25-fischer-legal-manipulations key to the first three options contiguously. All 4… |
| `instr-005` | high | chemical-accuracy | `mol-alpha-d-mannopyranose` | The long_description states the anomeric carbon is R. The asset's own SMILES gives C1 = S under rdCIPLabeler (full set C1 S, C2 S, C3 S, C4 S, C5 R), which is the correct alpha assignment. R at C1 would be the beta anomer. The structure is right and the descri… |
| `instr-006` | medium | sequencing | `nugget-glycoside-formation` | concepts[].prerequisites for glycoside-formation lists only ['anomers-and-mutarotation'], but the nugget's expanded prose explicitly builds its central mechanistic argument on the anomeric effect, which is introduced in pyranose-chair-conformation (order 7). A… |
| `instr-007` | medium | objective-alignment | `ch25-haworth-beta-anomer` | Three stated learning objectives are never assessed at the level at which they are stated. (a) Both haworth items set positions = [1], so the student only places the anomeric H/OH; no item asks for the C2/C3/C4 faces of a whole sugar. (b) Both chair items redu… |
| `instr-008` | medium | chemical-accuracy | `ch25-glycoside-error-repair-v2` | Both the flawed_work passage and the keyed correct repair enumerate the acylatable hydroxyls of methyl alpha-D-glucopyranoside as C2, C3 and C4, omitting the primary hydroxyl at C6. Acetic anhydride/pyridine acetylates the C6 primary alcohol fastest of all fou… |
| `instr-009` | medium | assessment-readiness | `ch25-reducing-sugar-select` | feedback_bundle.wrong_answer_explanations contains an entry matched to a specific option_id, and that option_id [redacted] is in answer_key.correct_option_ids. Every other wrong_answer_explanation in the chapter is keyed to a genuinely incorrect option. Either this explanatio… |
| `instr-010` | medium | retrieval-practice | `nugget-carbohydrate-classification` | None of the ten authored practice_check items reaches the compiled reader, and none of the 31 asset long_description texts does either. Molecule blocks carry only alt_text and the short description (the asset learning_goal). Ten well-written self-checks and 31… |
| `instr-011` | low | notation-consistency | `video-ring-closure` | The video brief instructs the animation to label the seven-membered ring from C6 attack as 'strained'. The nugget expressly rejects that framing: the ring is 'neither strained enough to be impossible nor favourable enough to compete: the ends of a seven-member… |
| `instr-012` | low | notation-consistency | `nugget-cyclic-hemiacetal-formation` | The open-chain population of aqueous glucose is quoted at four different precisions across the chapter: 'less than 0.02 percent', 'Fewer than two molecules in ten thousand', 'well under one molecule in a thousand', 'well under 0.1 percent', and 'far below one … |
| `instr-013` | low | objective-alignment | `ch25-mutarotation-percent` | The prose performs the weighted-average calculation, gets 36 percent alpha, then states the measured value as 38/62 and attributes the gap to trace furanose forms. The question keys 63.7 percent beta with a tolerance of 2. A student who has memorised the chapt… |
| `instr-014` | low | misconception | `mol-dihydroxyacetone` | The asset title claims dihydroxyacetone is 'the only achiral ketose' and the long_description that it is 'the only monosaccharide' with no stereocenter. Both are unqualified absolutes that are only true inside the chapter's implicit restriction to 2-ketoses of… |
| `instr-015` | low | conceptual-support | `mol-d-gluconic-acid` | The figure's learning_goal says the aldonic acid 'can no longer close a six-membered hemiacetal ring', while the nugget two paragraphs later says 'Aldonic acids readily cyclize to five- or six-membered lactones.' Both statements are correct - a lactone is not … |
| `instr-016` | low | assessment-readiness | `ch25-hemiacetal-bond-ledger` | The four atom_labels use ids 1-4 that do not correspond to the atom indices of the supplied molecule_smiles: for O=CCCCCO the aldehyde carbon is index 1 but the carbonyl oxygen is index 0 while being labelled '2', and the hydroxyl oxygen is index 6 while being… |

**Open questions**

- Does any delivery surface shuffle option, card, or matching-row order at render time? No shuffle/randomise/Math.random found in the renderers, which is why instr-004 is rated high - if shuffling happens server-side before payload assembly, that finding drops to low.
- How does the grader treat a wrong_answer_explanations entry whose match resolves to an option that is in correct_option_ids (ch25-reducing-sugar-select, option [redacted])?
- Is the non-delivery of practice_check and long_description to the compiled reader a tracked platform gap, or specific to this compile?
- Can the haworth question type accept a full set of ring positions, or is the single-position form a renderer limitation that constrains what instr-007 can ask for?
- In ch25-anomeric-effect-reasoning the distractor e_mp ('The axial anomer has the higher melting point') is not merely irrelevant but factually false for glucose (alpha 146 C, beta 150 C), and the feedback rebuts it only on relevance grounds. Should a false distractor be corrected as false?

#### Struggling Student — 5.6/10 (blockers: ss-001, ss-002)

The prose in this chapter is, sentence for sentence, some of the friendliest I have read: it names the mistake I am about to make before I make it, it justifies rules instead of just stating them, and the hint ladders on nearly every question genuinely go from strategy to narrowing to specifics rather than restating the prompt. But what I actually receive as a reader is 8,000 words of continuous text illustrated by thirty generic skeletal structures, with no checkpoint, no objective list, no summary, and - in a chapter whose entire spine is three named drawing conventions - not one picture of a Fischer projection, a Haworth projection, or a chair. The Haworth-to-chair conversion, which the text itself calls 'the single most common error in the conversion,' is asserted rather than worked, illustrated by nothing, and assessed by a question that hands me the answer in its own prompt. Every one of the ten authored practice_check items is missing from the compiled reader, so I go from reading straight to graded questions with nothing in between. On top of that, a comparison-matrix cell requires me to answer that free glucose survives prolonged 1 M NaOH, which is the opposite of what two other sections of this same chapter teach me - so studying the chapter makes me get that item wrong. And because the three detail tiers are alternatives rather than a sequence, a student who picks 'terse' or 'standard' to reduce the load loses facts the questions grade on: the ketose-stereocenter rule, the Kiliani-Fischer sequence, the anomeric-effect bond-length evidence, and the weighted-average rotation calculation are all expanded-only.

**Strengths**

- The hint ladders are the best scaffolding in the package and they genuinely escalate: ch25-identify-ketohexose goes strategy to what-to-look-at to the discriminating count, and ch25-identify-anomeric-carbon moves from history-dependent to a structural test I can run without the history.
- Wrong-answer explanations on the single- and multi-select items teach the criterion rather than asserting the key - ch25-assign-d-or-l explains for each distractor which stereocenter was inverted and why that one does not decide the letter.
- The prose names common wrong moves before I make them and explains why they are wrong, not just that they are.
- The Fischer-to-Haworth conversion IS properly worked, carbon by carbon, in both the standard and expanded tiers of nugget-haworth-projections, with the C6-arm result called out as a fact worth memorising separately. This is the model the chair section should have followed.
- Importance is signposted honestly, including the unusually candid 'It is a plausible account rather than a proven cause, and it should be offered as such' about glucose's biological prevalence.
- Each new relationship is tied back to one I already have instead of being introduced as a new species - 'anomers are simply epimers at one particular carbon'.
- The generic_incorrect_explanations on the multi-part questions, though not per-cell, are written as procedures I can rerun.

| id | sev | category | location | observation |
|---|---|---|---|---|
| `ss-001` | blocker | worked-example-gap | `ch25-beta-glucose-chair` | The Haworth-to-chair conversion is stated as a rule and then its result is asserted, never derived, and the chapter contains no drawing of a chair or of a Haworth projection to check the assertion against. The prose tells me the up direction 'alternates betwee… |
| `ss-002` | blocker | misconception | `ch25-anomer-comparison-v2` | The comparison_matrix ch25-anomer-comparison-v2 requires the cell f_base / case_sugar to be marked 'Applies' - i.e. that free beta-D-glucopyranose survives prolonged treatment with 1 M aqueous NaOH at room temperature. Two other sections of this same chapter t… |
| `ss-003` | high | conceptual-support | `ch25-rank-stereocenter-count` | The rule that decides several questions - in a ketose the carbonyl carbon is not a stereocenter, so a ketose has one fewer stereocenter than the aldose of the same chain length - appears in exactly one place in the whole chapter: the expanded tier of nugget-ca… |
| `ss-004` | high | cognitive-load | `ch25-anomeric-effect-reasoning` | The three detail tiers are alternatives, so a student who shortens the reading to manage load loses graded content, and nothing in the chapter warns them. Verified expanded-only items that questions require: (a) the anomeric-effect bond-length evidence is abse… |
| `ss-005` | high | cognitive-load | `mol-beta-d-glucopyranose` | All 31 assets in the chapter are generic renderings: 30 are molecule assets drawn from SMILES and one is a reaction-coordinate diagram. There is no Fischer projection figure, no Haworth projection figure and no chair figure anywhere, even though those three co… |
| `ss-006` | high | retrieval-practice | `nugget-carbohydrate-classification` | All ten authored practice_check items are absent from the compiled reader chapter, as are all thirty learning objectives, all thirty trouble_spots, and every asset long_description. Searching the compiled reader for 'practice_check', 'learning_objectives', 'tr… |
| `ss-007` | high | worked-example-gap | `ch25-identify-anomeric-carbon-v2` | The chapter insists three separate times that the alpha/beta rule must be phrased against the sugar's reference arm rather than as 'beta is up', because the arm-relative version survives translation to L-sugars and to furanoses - and then never demonstrates th… |
| `ss-008` | medium | conceptual-support | `nugget-cyclic-hemiacetal-formation` | Two whole prior chapters are imported as assumed knowledge with no refresher and no declaration. nugget-cyclic-hemiacetal-formation opens with 'Chapter 19 established that an alcohol adds reversibly to an aldehyde to give a hemiacetal' and builds the entire se… |
| `ss-009` | medium | worked-example-gap | `ch25-mutarotation-percent-v2` | The weighted-average rotation calculation is the only quantitative procedure in the chapter and is graded by two advanced questions, but it is shown exactly once - as a bare equation embedded mid-sentence in the expanded tier of nugget-anomers-and-mutarotation… |
| `ss-010` | medium | cognitive-load | `nugget-sugar-oxidation-and-reduction` | This section is budgeted at 7 minutes for 989 words and carries four learning objectives - more than any other nugget - while introducing roughly fifteen new named things in one pass: Tollens' reagent, Benedict's reagent, reducing sugar, enediol, the Lobry de … |
| `ss-011` | medium | retrieval-practice | `ch25-anomer-comparison` | Thirty of the 56 questions carry no wrong_answer_explanations at all and rely entirely on a single generic_incorrect_explanation paragraph. For the single-answer types that is workable, but it breaks down on the multi-part items: the two comparison_matrix ques… |
| `ss-012` | medium | cognitive-load | `video-ring-closure` | All five video blocks in the compiled reader render with an empty url, so the four authored video briefs reach the student as titles and captions with nothing behind them. Three of the four are attached to the sections I found hardest - ring closure, mutarotat… |
| `ss-013` | low | cognitive-load | `nugget-cyclic-hemiacetal-formation` | The same two quantities are given in several different forms across the chapter. The open-chain population appears as 'less than 0.02 percent', 'Fewer than two molecules in ten thousand', 'present in solution at well under one percent', 'well under 0.1 percent… |
| `ss-014` | low | misconception | `ch25-ring-closure-arrow` | The seven-membered-ring alternative is characterised three different ways. The expanded prose is careful and correct: 'neither strained enough to be impossible nor favourable enough to compete' because 'the ends of a seven-membered chain meet rarely'. The wron… |

**Open questions**

- Is the empty video url in the compiled reader a per-chapter authoring gap or a platform-wide delivery gap? Every one of the compiled reader chapters shows the same empty-string pattern, which suggests platform - I have reported ss-012 at medium rather than high on that basis.
- Same question for ss-006: practice_check, learning_objectives, trouble_spots and asset long_description are all authored here and all absent from the compiled reader. If the compiler has no block type for them, then the ten practice checks in this package are dead content and the fix is a platform one.
- ss-002 (the 1 M NaOH cell) is a chemistry-accuracy judgement as much as a pedagogical one; the Organic Chemistry Instructor persona should confirm whether 1 M NaOH at room temperature genuinely degrades/epimerizes free glucose on the timescale implied.
- In ch25-anomeric-effect-reasoning, the required evidence option e_carbocycle is not stated in any tier of any nugget - it exists only inside a concept trouble_spot, which the reader does not render. Should required evidence in a structured_reasoning item always be traceable to delivered prose?
- ch25-beta-glucose-chair states in its prompt that all five substituents share one orientation and then grades a single label. Is that a deliberate difficulty setting, or has the interactive chair type simply not got a per-position answer key available?

#### Accessibility Persona — 5.5/10 (blockers: access-001, access-003, access-004, access-006)

The prose layer of this chapter is the strongest non-visual chemistry writing I have reviewed here: all three projections (Fischer, Haworth, chair) are taught as explicit verbal rules, and at every detail tier the text states which side of a Fischer projection each D-glucose hydroxyl sits on, which face each Haworth substituent occupies, and which chair positions are axial or equatorial. All 168 hints are text; every selected-response option, matching item, categorize item and rank card carries a real text label rather than a 'Structure A/B/C/D' placeholder; bond_change_ledger ships a fully described non-visual workspace; and the automated leak guard flags 0 of 56 questions. The figure and question layers do not match that standard. Every figure ships a rich atom-by-atom long_description, but the compiled reader carries only alt_text, and the alt_text for 17 of 31 assets is identical modulo the compound's name. Both hotspot questions expose atoms only as 'C atom 5' RDKit indices with no connectivity, both structure_scaffold questions are a bare Ketcher iframe the registry itself marks not keyboard-complete with no alternative and no disclosure, and both curved_arrow questions render only the molecule-click path, which emits a source kind the answer key cannot match while the labelled site-select fallback that IS the declared non-visual mode never renders. Fifty-four of the 56 authored accessible_description strings are never displayed to any learner.

**Strengths**

- The prose carries all three representations in words, at every detail tier. nugget-haworth-projections states the conversion rule and then applies it carbon by carbon, and nugget-pyranose-chair-conformation names the axial/equatorial outcome for four named sugars explicitly. A non-visual learner can determine every one of these from the text alone.
- The terse and standard detail tiers both retain the load-bearing rules (horizontal-toward/vertical-away, right-becomes-down, up-stays-up-but-changes-name, beta-is-on-the-C6-arm-face). A learner using a reduced-density tier as a cognitive accommodation loses none of those rules.
- All 168 hints across the 56 questions are kind text. There is not one image-only, highlight-only or animation-only hint in the chapter.
- Every selected-response option, categorize item, matching item, rank card, comparison-matrix case and synthesis-route intermediate carries a real text label. The 'Structure A/B/C/D' anti-pattern that broke ch15 and ch16 does not appear anywhere.
- Both bond_change_ledger items are a model of non-visual authoring: reaction_display narrates the transformation in prose, atom_labels names each of the four participating atoms in words, and the renderer exposes them as a labelled list plus a labelled editable table.
- The Fischer and Haworth builders are genuinely keyboard-complete, and this chapter uses them in the mode where that holds - per-stereocenter and per-face selects alongside the drag affordance rather than instead of it.
- find_accessibility_leaks flags 0 of 56 questions; I ran it directly against the authored package. Descriptions consistently state the stimulus and the task and stop there.
- The four deferred videos are compiled with is_hidden true and an empty URL, so no learner meets a dead player, and each production_note records its accessibility requirements up front.
- No meaning in the chapter rests on colour, motion or hover. The only colour language in the prose is genuine chemistry - the Benedict's blue-to-brick-red transition and the Tollens' silver mirror - and it is always paired with the underlying redox statement.

| id | sev | category | location | observation |
|---|---|---|---|---|
| `access-001` | blocker | alt-text-quality | `mol-alpha-d-glucopyranose` | The accessibility.alt_text of 17 of the 31 assets is identical to at least one other asset's alt text once the compound name is removed, so the stereochemical difference the figure exists to show is absent from the only description a learner receives. Six clus… |
| `access-002` | high | media-equivalence | `mol-beta-d-glucopyranose` | All 31 assets carry a substantial accessibility.long_description (211-572 characters, atom-by-atom, with configurations), but the compiled reader chapter's molecule blocks contain only name, smiles, alt_text, description (which is the asset's learning_goal), g… |
| `access-003` | blocker | interactive-fallback | `ch25-identify-anomeric-carbon` | Both hotspot questions ship only molecule_smiles and a correct_option_ids [redacted]; neither carries a regions list. HotspotActivityRenderer's molecule branch therefore renders one button per atom with the accessible name 'symbol atom index+1' - which are RDKi… |
| `access-004` | blocker | keyboard-operability | `ch25-draw-cyclic-hemiacetal` | Both structure_scaffold questions use scaffold blank_canvas. The registry marks the type keyboard_complete=False with the explicit comment 'honest: Ketcher canvas is not yet (PRD 17)' and declares nonvisual_response_mode 'structured_molecule_entry'. StructureW… |
| `access-005` | high | media-equivalence | `ch25-build-d-glucose-fischer` | All 56 questions carry a well-written accessibility_bundle.accessible_description, and the compiled bank and the LMS envelope both deliver it. Exactly one renderer consumes it: ReactionCoordinateQuestionRenderer, which uses it as the SVG aria-label. No other a… |
| `access-006` | blocker | interactive-fallback | `ch25-ring-closure-arrow` | Both curved_arrow items declare five well-labelled sites and an answer key whose arrow source is kind lone_pair at site 9 (and site 7 in the v2). Their sites entries declare kinds ['atom','lone_pair'] in that order. Because student_config carries molecule_smil… |
| `access-007` | high | media-equivalence | `ch25-disaccharide-linkage-match` | In several items the discriminating stereochemistry lives only in the rendered structure image, while the item's text label is a bare compound name and the image alt is that same name. ch25-disaccharide-linkage-match asks the learner to match Maltose, Cellobio… |
| `access-008` | medium | objective-alignment | `ch25-assign-d-or-l` | The workaround that makes structure-bearing options nominally accessible - labelling each option with the compound's name - hands the answer to every learner in two items. ch25-assign-d-or-l asks which sugar belongs to the L series and labels the options 'L-Gl… |
| `access-009` | medium | interactive-fallback | `ch25-beta-glucose-chair` | The chair type declares keyboard_complete=False in the registry, but ChairPlacementRenderer's own docstring says 'Keyboard-complete by construction (selects only)' and it does render a labelled ring-position plus orientation select pair per substituent, which … |
| `access-010` | medium | alt-text-quality | `mol-d-erythrose` | The chapter contains no Fischer projection, no Haworth projection and no chair figure. All 31 assets are molecule (RDKit skeletal renders) except one reaction_coordinate. Several descriptions nonetheless assert facts about a projection the learner is not being… |
| `access-011` | medium | media-equivalence | `nugget-haworth-projections` | All ten nuggets carry a practice_check with a text prompt and a text answer, and every one of them is fully non-visual. None of them is delivered: the compiled reader chapter contains no practice-check block, and its section block types are limited to text, mo… |
| `access-012` | low | keyboard-operability | `nugget-pyranose-chair-conformation` | Heading order skips a level: TopicPackageChapterRenderer emits h1 for the chapter title and h2 for each section, then StructureCard and ReactionCoordinateCard emit h4 for each figure - no h3 exists. Within a section, the entire prose body is a single markdown … |
| `access-013` | low | alt-text-quality | `ch25-mutarotation-profile` | The two reaction_coordinate_reasoning descriptions - the only ones actually rendered to learners - supply exact energy values and explicitly characterise the second barrier as 'a lower peak'. The rendered diagram has no axis ticks and no numeric labels. The qu… |
| `access-014` | low | alt-text-quality | `mol-d-glyceraldehyde` | StructureCard sets the rendered image's alt to the figure's alt text and then renders the identical string again as a visible caption prefixed 'Described as:'. ReactionCoordinateCard does the same. |

**Open questions**

- Is this chapter intended to ship with no Fischer, Haworth or chair figure at all? Several long_descriptions are written as though such figures exist (access-010).
- Does anything outside ReactionCoordinateQuestionRenderer plan to consume accessible_description? Findings access-003, access-004 and access-007 would all be materially reduced if the authored descriptions were rendered.
- The chair grader accepts expected_label if the set of submitted orientations has exactly one member - which appears to score correct when only one of the five substituents has been placed. I could not confirm whether normalize_chair_state requires full placement.
- I did not verify behaviour of the two hotspot items under a live screen reader - my conclusion in access-003 is from the rendered aria-labels and the enrichment payload, not from an AT session.
- No new category identifiers were coined; every finding uses a value already listed in finding-schema.md.

#### Learner with Visual Preference — 4.4/10 (blockers: vis-001)

This chapter is written with unusual care about spatial relationships and then declines to draw a single one of them. Ten sections carry 53 figure cards, 30 of them distinct, and every one is an RDKit skeletal depiction of a single compound; the one non-molecule figure is the mutarotation energy profile. Three of the ten concepts - fischer-projections, haworth-projections, pyranose-chair-conformation - are about representations that the chapter never renders. Five figure captions actively describe a drawing that is not on screen. The chapter's single energy diagram renders alpha and beta glucopyranose at identical energy with identical barriers, contradicting both its own alt text and the 38/62 equilibrium the prose derives. Layout compounds this: the compiler emits exactly one text block per section followed by a bank of 4-8 figures, so no figure is ever adjacent to the sentence it supports. Two multiple-choice items illustrate only the correct option, which is a visual answer tell independent of any chemistry. Against that, the asset alt texts are honest about what is actually drawn, the hotspot items are genuinely answerable from the depiction, and the alpha/beta comparison matrix isolates the difference correctly.

**Strengths**

- rc-mutarotation is the one figure in the chapter that carries a relationship rather than a compound, and it is specified correctly to render inline - spec has both steps and minima_labels, plus minima_molecules that put structures at all three minima. The shape it draws is wrong (vis-007), but the authoring instinct and the machinery are right.
- Every molecule asset carries a specific learning_goal that the compiler emits as a visible caption, so no figure in the chapter is decorative or unexplained.
- The alt texts on the molecule assets describe the skeletal drawing that is actually rendered, accurately and at the right level of detail. It is the captions and long descriptions, not the alt texts, that overclaim.
- Both hotspot items are genuinely answerable from the depiction alone: the anomeric carbon is the unique ring carbon bonded to two oxygens, which is exactly the visual criterion the prose teaches.
- The 5-hydroxypentanal / 2-hydroxytetrahydropyran pair is a well-chosen figure pair - a stripped-down model that isolates ring closure from sugar stereochemistry, and the only place in the chapter where a before and an after are both drawn.
- ch25-anomer-comparison and ch25-disaccharide-linkage-match are built around side-by-side visual comparison, which is the correct instinct for material whose distinctions are single-position differences.
- When the Haworth builder does appear, its drawing follows the conventions the chapter's prose states, so the platform is capable of drawing the representation the reader omits.

| id | sev | category | location | observation |
|---|---|---|---|---|
| `vis-001` | blocker | figure-purpose | `ch25-cellulose-vs-starch` | In ch25-cellulose-vs-starch exactly one of four options carries a structure_smiles, and it is the key (option a, cellobiose). The identical pattern appears in ch25-glycosylation-outcome-v2, where only option a is illustrated and option a is the key. Both survi… |
| `vis-002` | high | figure-purpose | `ch25-epimer-relationship` | In ch25-epimer-relationship and ch25-glycosylation-outcome, two of four options carry a structure_smiles and the other two do not; the key is one of the two illustrated options in both cases. |
| `vis-003` | high | visual-opportunity | `nugget-fischer-projections` | The Fischer section spends 594 words defining a cross with a viewer convention, then walks three spatial manipulations, then does an R/S assignment that turns on which arm the lowest-priority H sits on. Its figures are RDKit line-angle depictions with no verti… |
| `vis-004` | high | visual-opportunity | `nugget-haworth-projections` | The Haworth section gives four explicit drawing conventions plus the right-means-down / left-means-up conversion rule applied carbon by carbon to D-glucose. Its five figures are RDKit ring depictions that satisfy none of the four conventions and encode face in… |
| `vis-005` | high | visual-opportunity | `nugget-pyranose-chair-conformation` | This is the longest section in the chapter (827 words) and it is entirely about geometry a flat depiction cannot express: up alternating between axial and equatorial around the ring, all five substituents equatorial, galactose forced to carry C4 axial, mannose… |
| `vis-006` | high | figure-accuracy | `mol-beta-d-xylopyranose` | Five asset learning_goal strings - which the compiler emits into the reader as the visible caption line under each figure - describe features of a representation that the rendered image is not. mol-d-erythrose: 'both carry the hydroxyl on the right in a Fische… |
| `vis-007` | high | figure-accuracy | `rc-mutarotation` | rc-mutarotation is the chapter's only relationship figure and it renders inline. But the spec supplies two steps with equal default magnitude (1.0) and identical barrier 'large'. The renderer computes minima as 0.0, +1.6, 0.0 and both peaks as max(flank)+2.0, … |
| `vis-008` | high | figure-purpose | `ch25-haworth-beta-anomer` | ch25-haworth-beta-anomer sets student_config.positions = [1], and HaworthBuilderRenderer draws substituent stubs only at the configured positions. The rendered stimulus is therefore a bare hexagon with a ring O glyph, a bold front edge, and two empty slots at … |
| `vis-009` | high | figure-accuracy | `ch25-beta-glucose-chair` | ch25-beta-glucose-chair sets student_config.ring = 'pyranose', but ChairPlacementRenderer ignores that field and draws a plain cyclohexane chair whose six vertices are all numbered 1 through 6 as carbons, each offering an axial and an equatorial stub, with the… |
| `vis-010` | high | media-equivalence | `video-fischer-to-haworth-to-chair` | All four video briefs are production_status 'deferred' and compile to video blocks with url empty and is_hidden true, so the reader shows no moving media. Each deferral note asserts the reader carries the same content. For video-ring-closure and video-mutarota… |
| `vis-011` | high | figure-purpose | `sugar-oxidation-and-reduction` | The compiler emits exactly one text block per section - 536 to 989 words - followed by the section's entire figure bank. No figure is ever placed next to the sentence it supports in any of the ten sections. The oxidation section is the extreme case: 989 words … |
| `vis-012` | medium | visual-redundancy | `mol-beta-d-glucopyranose` | The reader emits 53 molecule blocks for 30 distinct assets - 23 repeats, every one a byte-identical depiction with an identical caption. beta-D-glucopyranose appears 6 times, open-chain D-glucose and alpha-D-glucopyranose 4 times each. The two consecutive sect… |
| `vis-013` | medium | visual-opportunity | `d-l-configuration-and-families` | This section carries eight figures - the most in the chapter - and every one is a standalone RDKit zigzag of a single sugar. The relationships the section exists to teach are never drawn: D versus L as mirror images, C2 epimers and C4 epimers as one-position d… |
| `vis-014` | medium | visual-opportunity | `di-and-polysaccharides` | The closing section asserts three shape claims in prose and draws none of them: cellulose's flat stacked chains, amylose's left-handed helix, and the bushy branched polymers. Its seven figures are monomer and disaccharide depictions. Separately, the maltose/ce… |
| `vis-015` | medium | figure-accuracy | `mol-d-erythrose` | Only 3 of the 30 molecule assets set rdkit_options.show_hydrogens. The inconsistency lands hardest inside nugget-fischer-projections, where D-glyceraldehyde renders with its stereocenter hydrogen visible while D-erythrose, D-threose and open-chain D-glucose - … |
| `vis-016` | medium | figure-purpose | `ch25-hemiacetal-bond-ledger` | ch25-hemiacetal-bond-ledger displays only the starting material (molecule_smiles O=CCCCCO, no show_hydrogens) and describes the product in a prose reaction_display string. Two of the four atoms the learner must build ledger rows from are not visible: atom 4 is… |
| `vis-017` | medium | visual-opportunity | `ch25-beta-glucose-chair` | All 168 hints across the 56 question sets are kind 'text'. The platform supports non-text hint kinds (structure, highlight, projection label, region focus), and none is used anywhere in the chapter - including on the items whose whole difficulty is spatial. |
| `vis-018` | medium | visual-opportunity | `cyclic-hemiacetal-formation` | The ring-closure section presents five figures as five independent cards in sequence with nothing indicating that card 2 is the product of card 1, or that cards 4 and 5 are the two products of card 3. The prose asks the learner to count ring atoms and to see w… |
| `vis-019` | low | figure-purpose | `ch25-anomer-comparison` | ch25-anomer-comparison is correctly built as a two-column comparison, but the two column headers are full RDKit depictions whose only difference is the wedge/dash on one bond at C1. Nothing marks that carbon, and the same undifferentiated pair is used as the s… |

**Open questions**

- The schema has no category for a graphical answer tell. vis-001 and vis-002 are filed under figure-purpose, but the harm is an answer leak carried by figure placement rather than by text; the orchestrator may want a distinct id so this class diffs cleanly across chapters - this repo has hit it before (ch15).
- ch25-beta-glucose-chair sets student_config.ring = 'pyranose' and ChairPlacementRenderer ignores it, drawing an all-carbon cyclohexane. Is that a platform gap to file separately, or is the chair workspace expected to be ring-aware and simply not wired for this chapter?
- Do the fischer, haworth and chair builder workspaces reach a reader-surface learner at all, or only the LMS/question-preview surfaces?
- Asset long_description fields are not emitted into the compiled reader chapter. Several long descriptions contain the chapter's only statements of axial/equatorial and Haworth-face detail - is their non-delivery the known platform gap?
- rc-mutarotation is the only asset kind in the chapter besides molecule. Was a Fischer/Haworth/chair asset kind considered and found unavailable in the topic-package schema, or was it simply not authored?

### Orchestrator decisions

**rec-001 — beta-D-xylopyranose figure is actually the alpha anomer** (blocker, figure) 
_Need:_ The figure carrying the chapter's all-equatorial-pentose argument must be the anomer the caption, prose and question key all name. 
_Chosen intervention:_ **prose-edit** — The defect is one SMILES string; replacing it with the verified beta structure fixes the figure, its caption, its description and the question key simultaneously. No new asset is needed. 
_Consolidates:_ instr-001

**rec-002 — Base-stability matrix cell contradicts the chapter's own enediol chemistry** (blocker, assessment) 
_Need:_ The row must discriminate the two compounds the way the chapter's chemistry actually does - the acetal survives base, the free hemiacetal does not. 
_Chosen intervention:_ **prose-edit** — Flipping the free-sugar cell to 'does not apply' and rewriting the feature text and the level-3 hint makes the item agree with the chapter and turns a wrong key into the section's best discriminating row. 
_Consolidates:_ instr-002, ss-002

**rec-003 — Both curved_arrow items are ungradable as authored** (blocker, assessment) 
_Need:_ A correctly drawn arrow must grade correct through the interface the learner actually sees. 
_Chosen intervention:_ **prose-edit** — The renderer takes the source kind from site.kinds[0]; listing 'lone_pair' first on the nucleophilic oxygen sites makes the emitted arrow match the key. This is the pattern ch24 already uses and needs no platform change. 
_Consolidates:_ access-006

**rec-004 — Illustrated-option answer tell in four items** (blocker, assessment) 
_Need:_ The picture panel must carry no information about which option is correct. 
_Chosen intervention:_ **prose-edit** — Making illustration uniform within each option set removes the tell without changing the chemistry assessed. This is the ch15 defect class recurring and the text-only leak guard cannot see it. 
_Consolidates:_ vis-001, vis-002

**rec-005 — Both chair items score full marks for one placed substituent** (blocker, assessment) 
_Need:_ An item that claims to assess axial/equatorial placement across a ring must not be satisfiable by placing a single group. 
_Chosen intervention:_ **alternate-activity** — expected_label mode grades the set of distinct orientations, so it cannot require completeness. Switching to expected_orientations with ring rotation disabled makes all five placements load-bearing; the accompanying prompt must stop claiming a ring oxygen the renderer does not draw. 
_Consolidates:_ instr-007, vis-009, access-009, ss-001

**rec-006 — Figure descriptions do not distinguish the figures they are asked to compare** (blocker, figure) 
_Need:_ Two figures a learner is asked to compare must never resolve to the same words. 
_Chosen intervention:_ **sufficient-alt-text** — The distinguishing content already exists in each long_description; folding the one differentiating clause into the alt text closes the gap at the surface the reader actually delivers, without waiting on the long_description delivery gap. 
_Consolidates:_ access-001, ss-005, vis-019

**rec-007 — Positional answer bias across the whole bank** (high, assessment) 
_Need:_ Correct answers must not be recoverable from ordering or option length. 
_Chosen intervention:_ **prose-edit** — No renderer shuffles, so the keys must be distributed at authoring time: redistribute single_select keys across positions, break the diagonal on matching items, and ship rank_order cards unsorted. 
_Consolidates:_ instr-004

**rec-008 — Anomeric CIP stated wrongly in an accessibility-only channel** (high, figure) 
_Need:_ The structured description must report the configuration the drawn structure actually has. 
_Chosen intervention:_ **structured-chemical-description** — One descriptor is wrong (C1 R should be S) in a field only non-visual learners read - the same accessibility-channel-only error class ch24 hit. Machine-check every CIP claim in every description rather than fixing one by eye. 
_Consolidates:_ instr-005

**rec-009 — 'Humans secrete no beta-glucosidase at all' is refuted by the chapter's own lactase example** (high, prose) 
_Need:_ The digestibility contrast must survive the chapter's own counterexample. 
_Chosen intervention:_ **prose-edit** — Narrowing the claim to the enzyme that cleaves beta-1,4 glucan chains keeps the pedagogical payoff and removes a false absolute a biochemistry course would have to un-teach. 
_Consolidates:_ instr-003

**rec-010 — Captions describe representations the chapter never draws** (high, figure) 
_Need:_ Every caption must describe what is actually on screen. 
_Chosen intervention:_ **prose-edit** — Five learning_goal strings claim Fischer/Haworth/chair features of skeletal renders. Rewriting them to claim only what a skeletal depiction shows is the least-complex fix; authoring projection figures is the larger open recommendation (rec-014). 
_Consolidates:_ vis-006, access-010

**rec-011 — The mutarotation energy profile draws both anomers isoenergetic** (high, figure) 
_Need:_ Reading the curve must give the same answer as reading the paragraph beside it. 
_Chosen intervention:_ **prose-edit** — The spec omits per-step magnitudes so the renderer defaults to equal drops and equal barriers. Supplying magnitudes and differentiated barriers makes the drawn shape match the 38/62 equilibrium and the alt text. 
_Consolidates:_ vis-007

**rec-012 — Graded content that exists only in the expanded tier** (high, prose) 
_Need:_ Every fact the bank grades must reach a student at whichever tier they are reading, and required evidence must exist somewhere in the chapter. 
_Chosen intervention:_ **prose-edit** — The tiers are alternatives, not a sequence. Moving the ketose-stereocenter rule into all three tiers and adding the all-carbon-ring control (currently in no tier at all, yet a required selection) is a bounded prose edit. 
_Consolidates:_ ss-003, ss-004

**rec-013 — Wrong-answer feedback keyed to a correct option, and an acylation miscount** (medium, assessment) 
_Need:_ Feedback must not contradict the grade, and a keyed repair must match the structure it displays. 
_Chosen intervention:_ **prose-edit** — Two bounded authoring errors: move the fructose explanation out of wrong_answer_explanations, and add the C6 primary alcohol to the acylation inventory the chapter's own prose already lists. 
_Consolidates:_ instr-009, instr-008

**rec-014 — The chapter teaches three drawing conventions and draws none of them** (high, figure) 
_Need:_ A learner must see a Fischer cross, a Haworth hexagon and a chair before being asked to produce one. 
_Chosen intervention:_ **static-image-sequence** — All four personas reached this independently. It cannot be closed by description alone and it is the largest single lever on this chapter, but it needs a projection asset kind the topic-package schema does not have - so it is recorded as the headline open recommendation rather than applied in a correction pass. 
_Consolidates:_ vis-003, vis-004, vis-005, ss-005, vis-010

**rec-015 — Hotspot atoms are exposed only as RDKit indices** (blocker, interactive) 
_Need:_ Clicking an atom must be answerable from chemically meaningful targets, or an equivalent alternative must exist. 
_Chosen intervention:_ **keyboard-alternative** — Platform-level: molecule_visuals emits no adjacency and the renderer names atoms by index, so sugar C1 is announced as 'C atom 5'. The authored item cannot fix this; it needs named regions or meaningful atom naming in the platform. 
_Consolidates:_ access-003

**rec-016 — structure_scaffold has no non-pointer response path** (blocker, interactive) 
_Need:_ A keyboard-only or screen-reader learner must be able to answer, or be told at assignment time that they cannot. 
_Chosen intervention:_ **text-equivalent** — The registry marks the type keyboard_complete=False and the declared structured_molecule_entry mode is unimplemented. Same platform blocker recorded on ch1/11/15/16/17/18/19; not fixable inside this chapter. 
_Consolidates:_ access-004

**rec-017 — An entire authored layer never reaches any learner** (high, instructor-support) 
_Need:_ Authored practice checks, structured figure descriptions and per-question accessible descriptions must reach the surfaces they were written for. 
_Chosen intervention:_ **instructor-note** — 10 practice checks, 31 long descriptions and 54 of 56 accessible descriptions have no consumer in the reader or the activity shell. This is a platform delivery gap seen across chapters; recorded, not worked around, because a chapter-local workaround would hide it. 
_Consolidates:_ ss-006, instr-010, access-002, access-005, access-011

**rec-018 — Minor internal inconsistencies** (low, prose) 
_Need:_ One stated value per quantity, and one stated reason per phenomenon, across prose, captions and video briefs. 
_Chosen intervention:_ **prose-edit** — Bounded consistency edits: the open-chain fraction quoted five ways, the seven-membered ring called 'strained' only in a video brief, the unqualified 'only achiral ketose', and the aldonic-acid lactone/hemiacetal apparent contradiction. 
_Consolidates:_ ss-013, instr-012, ss-014, instr-011, instr-014, instr-015

### Merged duplicates

| Location | Personas | Consolidation |
|---|---|---|
| `ch25-anomer-comparison-v2` base-stability cell | Instructor (instr-002, blocker) + Struggling Student (ss-002, blocker) | One recommendation (rec-002) at blocker severity. Both learner impacts kept: the Instructor's chemistry case (enediol/Lobry de Bruyn) and the Student's motivational case (reading the chapter makes you get it wrong). |
| Chair items | Instructor (instr-007) + Visual (vis-009) + Accessibility (access-009) + Struggling Student (ss-001, blocker) | One recommendation (rec-005) at blocker severity, carrying all four impacts: objective not assessed, renderer draws the wrong ring, pointer path broken for 5 substituents, and the chapter's declared hardest step neither demonstrated nor assessed. |
| Undelivered authored layer | Struggling Student (ss-006) + Instructor (instr-010) + Accessibility (access-002, access-005, access-011) | One recommendation (rec-017) at high severity — see the retained disagreement on severity below. |
| No projection figures | Visual (vis-003, vis-004, vis-005, vis-010) + Struggling Student (ss-005) + Accessibility (access-010) | One recommendation (rec-014). Accessibility's angle (descriptions assert projections that do not exist) folded into rec-010 as the bounded caption fix; the figure gap itself stays open. |
| Open-chain fraction quoted inconsistently | Struggling Student (ss-013) + Instructor (instr-012) | Merged into rec-018; Instructor's measured value (~0.003%) adopted as the anchor. |
| Seven-membered ring called 'strained' | Struggling Student (ss-014) + Instructor (instr-011) | Merged into rec-018; both identify the video brief as the only out-of-step source. |
| Illustrated-option tell | Visual (vis-001, blocker; vis-002, high) | Merged into rec-004 at blocker severity — vis-001 (1-of-4 illustrated) and vis-002 (2-of-4) are the same defect at two strengths. |

### Retained disagreements

**Whether the reduced detail tiers are safe for a learner who uses them as a load accommodation**

- _Accessibility Persona:_ 'The terse and standard detail tiers - which are alternatives, not summaries - both retain the load-bearing rules (horizontal-toward/vertical-away, right-becomes-down, up-stays-up-but-changes-name, beta-is-on-the-C6-arm-face). A learner using a reduced-density tier as a cognitive accommodation loses none of the chemistry.'
- _Struggling Student:_ 'Because the three detail tiers are alternatives rather than a sequence, a student who picks terse or standard to reduce the load loses facts the questions grade on: the ketose-stereocenter rule, the Kiliani-Fischer sequence, the anomeric-effect bond-length evidence, and the weighted-average rotation calculation are all expanded-only.'

_Orchestrator resolution:_ Both are right about different things, and the distinction matters for the fix. Accessibility is correct that the four conversion RULES survive into every tier - I verified this. Struggling Student is correct that specific GRADED FACTS do not. The remedy therefore is not to rewrite the tiers wholesale but to move the handful of graded facts down into the shorter tiers (rec-012), which preserves Accessibility's finding that the tiers are a usable accommodation.

**Whether naming an option after the compound helps or harms**

- _Accessibility Persona:_ access-007 wants a text equivalent attached to options whose discriminating feature is visible only in the drawing; access-008 simultaneously notes that naming the compound hands the answer away in two items.
- _Learner with Visual Preference:_ vis-001/vis-002 want illustration made uniform across an option set, which pushes toward MORE structures rather than more text.

_Orchestrator resolution:_ Adopt both, at different layers: make illustration uniform (rec-004) so the picture carries no positional information, and attach the discriminating STRUCTURAL FEATURE - not the classification - to each option's text. That satisfies Accessibility's equivalence requirement without reintroducing the giveaway it flagged in access-008.

**Severity of the empty video blocks and the undelivered practice checks**

- _Struggling Student:_ Rated ss-012 and ss-006 at medium, explicitly because the same empty-url pattern appears in every compiled reader chapter and therefore looks platform-wide rather than chapter-specific.
- _Organic Chemistry Instructor:_ Rated the same non-delivery (instr-010) at medium but framed it as content that 'exists in the package and is invisible to the student', i.e. a real loss regardless of cause.

_Orchestrator resolution:_ Kept at high in the synthesis (rec-017). The personas correctly identified the cause as platform-level, but the learner impact is the whole retrieval-practice surface of the chapter plus its entire structured-description layer, which is a high-severity loss even when the cause is not chapter-local. Recording it at the severity of its cause would hide it.

### Places where a description is sufficient (no new asset)

- The bond_change_ledger items: reaction_display narrates the transformation in prose and atom_labels names each participating atom in words - Accessibility calls this a model of non-visual authoring. No new asset needed (the numbering mismatch in instr-016 is a labelling fix, not a media gap).
- The prose treatment of all three projections: at every detail tier the text states which side each Fischer hydroxyl sits on, which face each Haworth substituent occupies and which chair positions are axial. A non-visual learner can determine every one of these from the text alone - the prose does not need supplementing, the figures need adding.
- The four deferred video briefs' accessibility requirements: each production_note already records captions, narration naming every visual change, spoken numbers for any charted quantity, and a prohibition on colour/motion-only distinctions. No further specification needed before production.
- Asset alt texts as descriptions of what is drawn: they accurately describe the skeletal render. Only the pairwise-distinguishability problem (rec-006) needs work, not the general quality.
- The hotspot items' chemistry: the anomeric carbon genuinely is the unique ring carbon bonded to two oxygens, so the item is answerable from the depiction for a sighted learner. The barrier is the atom naming (rec-015), not the question design.

### Visual opportunities

- A Fischer projection drawn to convention, with at least one of the three legal/illegal manipulations performed on it (vis-003).
- A Haworth hexagon drawn to the four conventions the prose states, plus the glucose/galactose C4 contrast as the single flipped vertical line (vis-004).
- The all-equatorial beta-D-glucopyranose chair with positions labelled, against one contrast (galactose C4 axial or the alpha anomeric OH) (vis-005).
- Epimeric and enantiomeric pairs aligned so the one differing position is the only thing that moves, instead of eight isolated depictions (vis-013).
- The alpha/beta linkage difference marked where it occurs in the maltose/cellobiose pair, and the chain-shape consequence made visible (vis-014).
- At least one non-text hint level on the spatial items - all 168 hints are currently text (vis-017).

### Accessibility blockers

- `access-003` — hotspot atoms named only by RDKit index with no adjacency exposed; sugar C1 is announced as 'C atom 5', and the stated criterion (a ring carbon bonded to two oxygens) is exactly what the interface withholds.
- `access-004` — structure_scaffold renders a Ketcher iframe the registry marks keyboard_complete=False, with no structured-entry alternative and no disclosure to learner or instructor.
- `access-006` — both curved_arrow items lose their declared electron_action_list non-visual mode because the molecule branch returns before the labelled selects render - and the same early return makes the item ungradable for everyone.
- `access-001` — 17 of 31 figure alt texts are indistinguishable from a sibling figure's once the compound name is removed, in a chapter whose sections are built on comparing exactly those pairs.

### Regression targets for next run

Recheck these stable `finding_id`s after revision: `instr-001`, `instr-002`, `instr-003`, `instr-004`, `instr-005`, `instr-008`, `instr-009`, `ss-002`, `ss-003`, `ss-004`, `access-001`, `access-003`, `access-004`, `access-006`, `vis-001`, `vis-002`, `vis-006`, `vis-007`, `vis-009`, `vis-010`.

> No prior `chapter-review.json` exists for this chapter, so this run establishes the baseline; the regression block in the machine report is empty by design.

---
## Post-correction record

**Estimated state: blocked (not a second persona verdict).**

Not a new persona verdict. Every chapter-authored blocker is resolved and machine-verified; the estimate stays 'blocked' solely because two required-access blockers are platform-level and cannot be fixed inside a topic package: access-003 (hotspot atoms exposed only as RDKit indices) and access-004 (structure_scaffold has no non-pointer response path — the same ticket already recorded on ch1/11/15/16/17/18/19). Setting those aside, the chapter-local state is estimated 'ready with minor revisions', with the Fischer/Haworth/chair figure gap (rec-014) as the headline open item.

### Changes applied

- mol-beta-d-xylopyranose SMILES corrected from O[C@@H]1[C@@H](O)[C@@H](O)OC[C@H]1O (the ALPHA anomer) to O[C@@H]1[C@@H](O)[C@H](O)OC[C@H]1O. Verified two ways: the anomeric oxane CIP is now R, matching published beta-D-xylopyranose (2R,3R,4S,5R), and the same method reproduces the published alpha/beta glucopyranose names as a control. — resolves `instr-001`
- ch25-anomer-comparison-v2: the f_base row was reworded from 'Survives prolonged treatment with 1 M aqueous NaOH' to 'Its anomeric carbon still has the configuration it started with after a day in 1 M aqueous NaOH', the free-sugar cell flipped from yes to no, the level-3 hint rewritten to stop asserting the free sugar has no base-accessible proton, and the generic explanation rewritten to teach the enediol contrast. — resolves `instr-002`, `ss-002`
- Both curved_arrow items: nucleophilic oxygen sites now declare kinds ['lone_pair','atom'] instead of ['atom','lone_pair']. CurvedArrowRenderer emits site.kinds[0] as the source kind, so the previous ordering made a correct arrow ungradable for every learner. Verified by grading a submission built the way the renderer builds it. — resolves `access-006`
- Illustration made uniform across four option sets (ch25-cellulose-vs-starch, ch25-glycosylation-outcome-v2, ch25-epimer-relationship, ch25-glycosylation-outcome). No single_select item now has a subset of options illustrated. This is the ch15 answer-tell class, invisible to the text-only leak guard. — resolves `vis-001`, `vis-002`
- Both chair items switched from expected_label to expected_orientations naming all five (four in the variant) placements, with allow_ring_rotation and allow_ring_flip disabled. Verified: a single placed substituent now grades incorrect where it previously scored 1.0. Prompts and accessible descriptions rewritten to stop asserting a ring oxygen the renderer does not draw, and to disclose that limitation. — resolves `ss-001`; partially addresses `instr-007`, `vis-009`, `access-009`
- Seventeen asset alt texts rewritten so no two figures a learner is asked to compare resolve to the same words: the four ring hexoses, the four open-chain hexoses, the erythrose/threose pair, the glyceraldehyde pair, the two methyl glucosides, and maltose/cellobiose now each state the configuration that distinguishes them. — resolves `access-001`; partially addresses `ss-005`, `vis-019`
- Positional answer bias removed. Keys are now spread evenly across option positions (index distribution 5/4/2/3/2 across positions 0-4, previously 16/16 at index 0), no matching_pairs item is diagonal, and no rank_order item ships in solved order. A first attempt that merely avoided index 0 was rejected because it relocated the bias to index 3. — resolves `instr-004`
- mol-alpha-d-mannopyranose long_description corrected from 'C1 R' to 'C1 S' to match the drawn structure. Every CIP claim in every asset description was then machine-checked against its SMILES; this was the only mismatch. — resolves `instr-005`
- The 'humans secrete no beta-glucosidase at all' absolute was narrowed to 'no cellulase - no enzyme that cleaves the beta-1,4 linkages of a glucan chain' in all three places it appeared (standard tier, expanded tier, practice_check answer), each noting that lactase is a beta-glycosidase we do make. — resolves `instr-003`
- Five figure captions (learning_goal, which the compiler emits as the visible caption) rewritten to claim only what a skeletal depiction shows, instead of asserting Fischer/Haworth/chair features of drawings that are not those representations. — resolves `vis-006`; partially addresses `access-010`
- rc-mutarotation gained per-step magnitudes and a differentiated second barrier. Without them the renderer drew both anomers at identical energy with identical barriers, contradicting the figure's own alt text and the 38/62 equilibrium in the adjacent prose. — resolves `vis-007`
- The ketose-stereocenter rule was added to the terse and standard tiers (it was expanded-only while gating a core-difficulty item), and the all-carbon-ring control experiment was added to the standard and expanded tiers - it was a REQUIRED evidence selection in ch25-anomeric-effect-reasoning while appearing in no tier of any nugget. — resolves `ss-003`; partially addresses `ss-004`
- ch25-reducing-sugar-select: the fructose/enediol explanation was moved out of wrong_answer_explanations (it was keyed to [redacted grading-pattern detail], which is CORRECT) and into the generic explanation where it reaches the learner without contradicting the grade. — resolves `instr-009`
- ch25-glycoside-error-repair-v2: the acylation inventory now includes the C6 primary alcohol in the stimulus, the keyed repair and the accessible description, matching the chapter's own prose. — resolves `instr-008`
- The open-chain glucose fraction is now quoted as about 0.003 percent everywhere (previously five different values spanning a factor of fifty across prose tiers, a learning objective, a figure description and a concept trouble spot). — resolves `ss-013`, `instr-012`
- video-ring-closure's storyboard no longer instructs the animation to label the seven-membered ring 'strained'; it now gives the entropic reason the prose gives. video-fischer-to-haworth-to-chair's deferral note no longer claims reader equivalence, because the reader carries no Fischer, Haworth or chair figure. — resolves `instr-011`, `ss-014`; partially addresses `vis-010`
- Scoped absolutes and glosses: dihydroxyacetone's 'only achiral ketose' narrowed to the common 2-ketoses; D-gluconic acid's caption now says it cyclizes to a lactone rather than a hemiacetal, resolving an apparent contradiction with the prose; ch25-mutarotation-percent tolerance widened from 2 to 3 so the chapter's own headline 62 percent is comfortably inside; the e_mp distractor reworded from a factually false melting-point claim to a true-but-irrelevant one. — resolves `instr-014`, `instr-015`, `instr-013`
- concepts['glycoside-formation'].prerequisites now declares pyranose-chair-conformation, the dependency its prose actually creates by building the oxocarbenium argument on the anomeric effect. — resolves `instr-006`

### Verification

- `Proprietary toolchain verification (not in this repo)
- `[internal source reference — not in this repo] --write-runtime - surfaced 28, types 19, all artifacts rewritten`
- re-graded all 56 questions through the live registry graders, building the curved_arrow submission the way the RENDERER builds it - 56/56 correct (4 structured_reasoning return manual_review by type design, objective_score 1.0)
- chair: all placements -> correct, ONE placement -> incorrect (previously scored 1.0)
- beta-D-xylopyranose anomeric oxane CIP = R, matching published (2R,3R,4S,5R); method validated against the published alpha/beta glucopyranose names
- every CIP claim in every asset description machine-checked against its SMILES - 0 mismatches remaining
- wrong_answer_explanations keyed to a correct option - 0 remaining
- key position distribution across select items: {0:5, 1:4, 2:2, 3:3, 4:2}; diagonal matching_pairs 0/4; rank_order in solved order 0/2
- `pytest tools/topic_packages/tests/ -q - 62 passed`
- `pytest backend question-set + sugar-form suites -q - 224 passed`
- `npx vitest run src/data/__tests__ - 11 passed`
- topic-package-textbook-profiles.json re-merged after the compiler clobber - 260 chapter entries retained

### Still recommended

- rec-014 - no Fischer projection, Haworth projection or chair figure exists anywhere in the chapter, while three concepts teach exactly those representations. All four personas reached this independently. Needs a projection asset kind the topic-package schema does not have.
- rec-015 / access-003 - hotspot atoms are named only by RDKit index; platform fix.
- rec-016 / access-004 - structure_scaffold has no non-pointer response path; platform ticket already open on seven earlier chapters.
- rec-017 - 10 practice checks, 31 long descriptions and 54 of 56 accessible descriptions have no consumer in the reader or the activity shell; platform delivery gap.
- instr-007 - the Haworth items still place only the anomeric substituent, so the full right-to-down conversion is still not assessed; the haworth renderer draws stubs only at configured positions, so widening it needs a renderer check first.
- vis-011 - the compiler emits one text block per section followed by a figure bank, so no figure sits beside the sentence it supports.

> The baseline verdict at the top of this file (**blocked**) is unchanged. A new verdict requires a fresh four-persona regression run.

### Follow-up pass (2026-07-30, after the post-correction record above)

- **Upstream data fix — `backend/app/data/sugar_forms.json`.** Two independent anomer-label bugs found while tracing instr-001, both now fixed and verified. (1) All four D-aldopentopyranose pairs (xylo, lyxo, ribo, arabino) had alpha and beta swapped - this is what put the wrong structure in ch25. (2) All four D-ketopyranose pairs (fructo, psico, sorbo, tagato) were also swapped, found by a D/L enantiomer-consistency check; the L entries were correct and the D entries wrong. Only smiles/canonical_smiles were exchanged; ids, names, anomer fields and highlights untouched (verified identical atom ordering, and no distribution fields on the affected entries).
 Verification: every alpha/beta pair confirmed to differ at the anomeric carbon and nowhere else, before swapping; post-fix: every D/L label pair is a true enantiomer pair (0 exceptions across 128 forms); post-fix spot-checks vs published IUPAC oxane names: beta-D-fructopyranose 2R,3S,4R,5R; alpha-D-fructopyranose 2S,3S,4R,5R; beta-D-fructofuranose 2R,3S,4S,5R; beta-D-xylopyranose 2R,3R,4S,5R; beta-D-glucopyranose 2R,3R,4S,5S - all match; pytest [internal source reference — not in this repo] -q: 47 passed
- **A fourth instance of the answer-tell class.** Sweeping illustration-vs-correctness across every
 option-bearing type (not just `single_select`) found `ch25-sort-aldose-ketose-v2`, where the two
 polysaccharides were the only unillustrated items — so "has no picture" placed them in the right
 group with no chemistry. Illustration removed from all six items.
- **Approved.** `publishing.available` flipped to `true` for this chapter and for chapter 24, on
 explicit maintainer approval; both recompiled. The Pending badge on `/reader/organic` is cleared for
 both. Neither chapter's question bank is seeded, so the reader homework preview stays empty until
 a seed run is approved separately.

> The baseline verdict (**blocked**) is still unchanged — see the explanation of the post-correction
> estimate: it is held there by two platform blockers, not by anything left in the chapter.
