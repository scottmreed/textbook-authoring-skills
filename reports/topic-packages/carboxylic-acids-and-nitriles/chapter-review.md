# Chapter review — Carboxylic Acids and Nitriles (`carboxylic-acids-and-nitriles`)

_Reviewed 2026-07-31 · chapter version 1 · personas: Instructor, Struggling Student, Accessibility, Visual Preference_

**Publication readiness: major revision**

This chapter is the strongest of the four in this batch on every axis except one, and it is the only one of the four whose computed readiness is not `blocked`. Its quantitative layer is exceptionally reliable — every pKa, boiling point, bond length, IR wavenumber and NMR shift checks against standard tables, and all 22 asset SMILES plus every structure across the 42 question items parse in RDKit and match the names claimed, including the charged species, the salt, and the aryl regiochemistry of both para-substituted benzoic acids. Its accessibility substrate is the best in the batch: all four structure_scaffold items set `typed_structure_entry: "allowed"`, nothing depends on drag, hover, colour or motion, no `accessible_description` leaks an answer, and no level-1 hint hands one over — the Accessibility persona scored it 7.6 and raised no blocker, the only such return across the four chapters. It also arrived clean on artifact drift: the [commit ref — not in this repo] edit is already back-ported, `wikipedia_title` is authored on all nine concepts, all 10 links verify 200, and callouts already compile in all ten sections. What holds it back is four wrong statements, each of which reaches a student. Section 1 says delocalization "weakens the O–H bond" and makes carboxylic acids acidic — false (the carboxyl O–H BDE is *higher* than an alcohol's, and delocalization in the neutral acid opposes ionization), and it is the exact misconception the chapter's own trouble spot names and section 3 explicitly refutes. `ch20-stronger-than-acetic` keys 4-methoxybenzoic acid (pKa 4.47, a number the chapter itself prints) as NOT stronger than acetic acid (4.76), so a student reasoning correctly from the chapter's own table is graded wrong, and the distractor rationale compounds it by silently switching the reference compound from acetic acid to benzoic acid. The preparation practice check calls neopentyl bromide "primary and unhindered at the reacting carbon" and its cyanide displacement "straightforward" — it is the canonical primary halide that does not do SN2. And the nitrile-IR feedback teaches that the nitrile band sits "above the alkyne range", contradicting the chapter's own 2100–2260 cm⁻¹ alkyne window. Beyond the chemistry, the three mental models the chapter is built on — the cyclic dimer, the carboxylate hybrid, and the diagnostic IR band shape — are carried by prose alone, and the one carboxylate figure actively teaches the misconception the adjacent callout warns against.

### Top blockers

- **[BLOCKER] Section 1 explains carboxylic acid acidity as a weakened O-H bond caused by lone-pair delocalization in the neutral acid.** — `instr-001` (Organic Chemistry Instructor; section_id=`nugget-carboxylic-acid-structure-naming`, concept_slug=`carboxylic-acid-structure-and-naming`, nugget_id=`nugget-carboxylic-acid-structure-naming`)
- **[BLOCKER] The answer key is ['a','b','e'] and treats option c, 4-methoxybenzoic acid, as NOT a stronger acid than acetic acid.** — `instr-002` (Organic Chemistry Instructor; question_slug=`ch20-stronger-than-acetic`, concept_slug=`substituent-effects-on-acidity`)
- **[BLOCKER] The practice check converts 1-bromo-2,2-dimethylpropane (neopentyl bromide) to 3,3-dimethylbutanoic acid and answers that cyanide displacement is 'straightforward' because the halide is 'primary and unhindered at the reacting carbon'.** — `instr-003` (Organic Chemistry Instructor; section_id=`nugget-preparation-of-carboxylic-acids`, nugget_id=`nugget-preparation-of-carboxylic-acids`, concept_slug=`preparation-of-carboxylic-acids`)
- **[BLOCKER] Both the hint ladder and the generic feedback tell the student that the nitrile absorption lies 'above the alkyne range' / 'just above the range in which alkynes absorb'.** — `instr-004` (Organic Chemistry Instructor; question_slug=`ch20-carbonyl-ir-wavenumber-v2`, concept_slug=`spectroscopy-of-carboxylic-acids-and-nitriles`)

### Top 5 recommended changes

1. **Section 1 attributes acidity to a weakened O–H bond** — The carboxyl delocalization must be described for what it actually does, and the acidity claim must be framed by conjugate-base stability so sections 1 and 3 tell one story. → **prose-edit** (prose, blocker)
2. **A multi-select key contradicts the chapter's own pKa table** — The option set's acidity relative to acetic acid must be unambiguous, and the key and distractor rationale must both use the reference compound the prompt names. → **prose-edit** (assessment, blocker)
3. **The practice check says SN2 on neopentyl bromide is straightforward** — The practice check must resolve to the route that actually works for this substrate and say why the SN2 route fails. → **prose-edit** (practice, blocker)
4. **The nitrile-IR feedback separates two overlapping regions** — The feedback needs the discriminator the chapter actually teaches — overlapping positions distinguished by band intensity and by the ≡C–H stretch — not a claim that the regions differ in wavenumber. → **prose-edit** (assessment, blocker)
5. **The only carboxylate figure teaches the misconception the callout warns against** — The equivalence of the two carbon–oxygen bonds, and the bond-length evidence for it, must reach the student rather than being asserted in a caption while the adjacent picture shows the opposite. → **longer-description** (figure, high)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 6.3/10 | 4 | Exceptionally reliable numbers and structures — but four wrong statements reach students, including a key that contradicts the chapter's own pKa table. |
| Struggling Student | 6.6/10 | 0 | pKa used 49 times and never defined; 'oxidation level' carries nine questions' feedback and appears once in the text. |
| Accessibility Persona | 7.6/10 | 0 | The best accessibility substrate in the batch — no blockers, no leaks, typed entry allowed everywhere; the gaps are description and delivery. |
| Learner with Visual Preference | 6.0/10 | 0 | 19 of 20 assets are single molecules, so the dimer, the carboxylate hybrid and the IR band shape cannot be drawn at all. |

### Affected sections & assets

`carboxylic-acid-acidity`, `carboxylic-acid-physical-properties`, `carboxylic-acid-structure-and-naming`, `ch20-acid-reduction-reagent-v2`, `ch20-acidity-rank-v2`, `ch20-carbonyl-ir-wavenumber-v2`, `ch20-carbonyl-ir-wavenumber`, `ch20-inductive-distance-v2`, `ch20-inductive-distance`, `ch20-ir-triple-bond-region`, `ch20-nitrile-hydrolysis-product-v2`, `ch20-nitrile-sn2-arrow-v2`, `ch20-nitrile-sn2-arrow`, `ch20-stronger-than-acetic`, `mol-acetate-ion`, `mol-acetonitrile`, `mol-benzoic-acid`, `mol-butan-1-ol`, `mol-butanoic-acid`, `mol-chloroacetic-acid`, `nitrile-structure-naming-and-preparation`, `nugget-carboxylate-salts-and-extraction`, `nugget-carboxylic-acid-acidity`, `nugget-carboxylic-acid-dimers`, `nugget-carboxylic-acid-structure-naming`, `nugget-nitrile-structure-and-preparation`, `nugget-preparation-of-carboxylic-acids`, `nugget-reactions-of-carboxylic-acids`, `nugget-reactions-of-nitriles`, `nugget-spectroscopy-acids-nitriles`, `nugget-substituent-effects-acidity`, `preparation-of-carboxylic-acids`, `reactions-of-carboxylic-acids`, `reactions-of-nitriles`, `roadmap-nitrile-homologation`, `spectroscopy-of-carboxylic-acids-and-nitriles`, `substituent-effects-on-acidity`, `video-carboxylate-delocalization`, `video-nitrile-hydrolysis`

---
## Full evidence

### Independent persona reports

#### Organic Chemistry Instructor — 6.3/10

Not-go as it stands, but the gap to publishable is small and well-localized. I independently checked every SMILES in the package, reader and compiled question set with RDKit (all 22 assets and all ~60 question structures parse and match the names claimed), and every pKa, boiling point, bond length, IR wavenumber and NMR shift against standard tables - that numeric layer is unusually clean. Four statements are nevertheless chemically wrong and all four reach a student: section 1 tells the reader that carboxylic acids are acidic partly because delocalization weakens the O-H bond, which is false and is the exact misconception section 3 and the concept trouble spots refute; the ch20-stronger-than-acetic answer key marks 4-methoxybenzoic acid (pKa 4.47, a value the chapter itself prints) as NOT stronger than acetic acid (4.76), so a student reasoning correctly from the chapter's own table is graded wrong; the preparation practice check calls neopentyl bromide 'primary and unhindered at the reacting carbon' and its cyanide displacement 'straightforward', when it is the canonical primary halide that does not do SN2; and the nitrile-IR feedback teaches that the nitrile band sits 'above the alkyne range', contradicting the chapter's own 2100-2260 cm-1 alkyne range. Beyond the chemistry, the chapter's three signature mental models - the cyclic dimer, the carboxylate hybrid, and the diagnostic IR spectrum - are carried by prose alone, and all three video briefs compile into reader blocks with an empty url.

**Publication blockers:** `instr-001`, `instr-002`, `instr-003`, `instr-004`

**Strengths**

- The quantitative layer is exceptionally reliable. Every pKa matches standard tables (acetic 4.76, formic 3.75, chloro/dichloro/trichloroacetic 2.86/1.29/0.65, TFA 0.23, the 2-/3-/4-chlorobutanoic 2.86/4.05/4.52 series against butanoic 4.82, benzoic 4.19, 4-nitro 3.44, 4-methoxy 4.47, 4-chloro 3.99, 4-methyl 4.34, carbonic 6.4, phenol 10, ethanol 16), as do the boiling points, bond lengths (formate 127 pm versus 120/134 pm), the acetonitrile dipole, and the spectroscopy (1710/1690/1760, 2250/2230, delta 11-12, delta 165-185 versus 115-130, McLafferty m/z 60).
- All 22 asset SMILES and every structure across the 42 question items parse in RDKit and give the formula and canonical structure the name claims - including the charged species, the salt, the multi-component ledger and curved-arrow stems, and the aryl regiochemistry of both para-substituted benzoic acids.
- The curved-arrow site indices are correct against SMILES atom ordering in both items - the kind of off-by-one that usually slips through.
- The compiled reader and question set are both faithful to the package: all ten sections' prose matches nuggets[].text.expanded byte for byte, and all 42 compiled questions match the package exactly. There is no artifact-only drift to protect before a recompile.
- Trouble spots and practice checks reach the reader as callouts in all ten sections.
- Chain-length bookkeeping is taught deliberately and consistently - which routes add a carbon and which do not is the organizing idea of the preparation section and is reused as the discriminator in five items.
- The hydride-selectivity story is complete and correct in both directions: NaBH4 leaves a carboxylic acid untouched, LiAlH4 reduces past an aldehyde that cannot be isolated, and BH3/THF is selective the opposite way - and the error_repair pair is well designed.
- Fourteen question types are used, including bond_change_ledger, structured_reasoning, comparison_matrix and synthesis_route, with four structure_scaffold items setting typed_structure_entry to 'allowed' and the numeric items using the correct {mode, amount} tolerance shape.

**Findings**

##### `instr-001` — BLOCKER · chemical-accuracy · confidence 0.95

**Location:** section_id=`nugget-carboxylic-acid-structure-naming` · concept_slug=`carboxylic-acid-structure-and-naming` · nugget_id=`nugget-carboxylic-acid-structure-naming` · anchor="The same delocalization weakens the O–H bond and is one reason carboxylic acids are far more acidic than alcohols."

**Observation:** Section 1 explains carboxylic acid acidity as a weakened O-H bond caused by lone-pair delocalization in the neutral acid. This is wrong twice over. The O-H bond of a carboxylic acid is not weaker than an alcohol's - the O-H bond dissociation energy of acetic acid (about 110-112 kcal/mol) exceeds that of methanol/ethanol (about 105 kcal/mol) - and delocalization in the NEUTRAL acid stabilizes the starting material, which if anything opposes ionization. Acidity is a statement about the conjugate base.

**Learner impact:** This is the first mechanistic 'why' a student meets, and it is the misconception the chapter's own trouble spot names ('Attributing the acidity to a weak O-H bond rather than to the stability of the conjugate base') and that section 3 explicitly refutes ('The O-H bonds involved are similar in strength, so the difference cannot be a bond-strength effect'). A student reading sequentially is taught the wrong model, then contradicted two sections later with no reconciliation.

**Evidence:** nuggets[0].text.expanded, reproduced verbatim in compiled reader block blk-xvbwc1jm. Directly contradicted by nuggets[2].text.expanded and concepts[2].trouble_spots[0].

**Recommended outcome (need):** Section 1 needs the carboxyl delocalization described for what it actually does (shorter C-O, longer C=O, less electrophilic carbonyl carbon) without attributing acidity to a weakened O-H bond; the acidity claim must be deferred to, and framed by, conjugate-base stability so sections 1 and 3 tell one story.

##### `instr-002` — BLOCKER · chemical-accuracy · confidence 0.97

**Location:** question_slug=`ch20-stronger-than-acetic` · concept_slug=`substituent-effects-on-acidity` · anchor="Select every compound that is a stronger acid than acetic acid (pKa 4.76)."

**Observation:** The answer key is ['a','b','e'] and treats option c, 4-methoxybenzoic acid, as NOT a stronger acid than acetic acid. 4-Methoxybenzoic acid has pKa 4.47 - the value the chapter itself prints in section 5 and in the mol-4-methoxybenzoic-acid learning goal - which is lower than 4.76, so it IS the stronger acid. Every benzoic acid in the chapter's own table (4.19, 3.99, 4.34, 4.47) is stronger than acetic acid; a para-methoxy group weakens the acid relative to BENZOIC acid, not relative to acetic acid.

**Learner impact:** A student who reasons correctly from the chapter's own pKa data selects c and is marked wrong, and the wrong-answer explanation reinforces the error by comparing 4.47 to benzoic acid instead of to the 4.76 stated in the prompt. This is a graded item on the chapter's central quantitative skill, so it punishes exactly the behaviour the chapter's trouble spot asks for.

**Evidence:** question_sets ch20-stronger-than-acetic answer_key [redacted]; wrong_answer_explanations option c: 'Its pKa of 4.47 is close to that of acetic acid but on the weaker-acid side of benzoic acid.' Identical in compiled/question-set.json. The sibling ch20-stronger-than-acetic-v2 is correct.

**Recommended outcome (need):** The item needs an option set whose acidity relative to acetic acid is unambiguous and a key consistent with the chapter's own pKa table - either 4-methoxybenzoic acid counted as correct, or replaced by a genuinely weaker acid, with the distractor rationale rewritten so the reference point in the explanation is the reference point in the prompt.

##### `instr-003` — BLOCKER · chemical-accuracy · confidence 0.94

**Location:** section_id=`nugget-preparation-of-carboxylic-acids` · nugget_id=`nugget-preparation-of-carboxylic-acids` · concept_slug=`preparation-of-carboxylic-acids` · anchor="the halide is primary and unhindered at the reacting carbon, so cyanide displacement followed by hydrolysis is straightforward"

**Observation:** The practice check converts 1-bromo-2,2-dimethylpropane (neopentyl bromide) to 3,3-dimethylbutanoic acid and answers that cyanide displacement is 'straightforward' because the halide is 'primary and unhindered at the reacting carbon'. Neopentyl halides are the textbook counterexample to 'primary halides do SN2': the adjacent quaternary carbon blocks backside attack and the SN2 rate is about 1e-5 that of ethyl bromide. Grignard carboxylation is the route that works here.

**Learner impact:** The item reaches the reader verbatim as the 'Check yourself before moving on' callout, so a self-studying student is told the wrong outcome with a confident justification. It also cements the chapter's simplification ('cyanide displacement works on methyl and primary halides') as an unconditional rule, which will fail on any exam question using a neopentyl or beta-branched primary substrate.

**Evidence:** nuggets[5].practice_check.answer; compiled reader callout block blk-qm5w50m3. The nugget's standard tier says only 'methyl and primary halides react cleanly' with no beta-branching caveat, and concepts[4].trouble_spots contains no neopentyl entry.

**Recommended outcome (need):** The practice check must resolve to the Grignard route for this substrate and say why the SN2 route fails, and the surrounding text needs the beta-branching limit on cyanide displacement stated once so the 'primary = SN2 works' rule is not left unqualified.

##### `instr-004` — BLOCKER · chemical-accuracy · confidence 0.9

**Location:** question_slug=`ch20-carbonyl-ir-wavenumber-v2` · concept_slug=`spectroscopy-of-carboxylic-acids-and-nitriles` · anchor="The nitrile band sits at the upper end of that triple-bond region, above the alkyne range."

**Observation:** Both the hint ladder and the generic feedback tell the student that the nitrile absorption lies 'above the alkyne range' / 'just above the range in which alkynes absorb'. The chapter's own section 10 states that alkynes absorb between about 2100 and 2260 cm-1, so 2250 cm-1 is INSIDE the alkyne range, not above it. The discriminator the chapter teaches is intensity (nitrile sharp/medium, C-C triple bond weak or absent) plus the terminal alkyne C-H stretch near 3300 cm-1, not position.

**Learner impact:** The feedback hands the student a false decision rule for the most confusable region of the IR spectrum, and it is the rule the concept trouble spot exists to prevent. A student who applies it will confidently misassign an internal alkyne at 2230 cm-1 as a nitrile - precisely the sibling item ch20-ir-triple-bond-region's scenario.

**Evidence:** ch20-carbonyl-ir-wavenumber-v2 feedback_bundle.generic_incorrect_explanation and hints[1]; contradicted by nuggets[9].text.expanded and by ch20-ir-triple-bond-region's own wrong_answer_explanations.

**Recommended outcome (need):** The feedback needs the same discriminator the chapter teaches - overlapping positions distinguished by band intensity and by the presence or absence of the terminal alkyne C-H stretch - rather than a claim that the two regions are separated in wavenumber.

##### `instr-005` — HIGH · visual-opportunity · confidence 0.88

**Location:** section_id=`nugget-carboxylic-acid-dimers` · nugget_id=`nugget-carboxylic-acid-dimers` · concept_slug=`carboxylic-acid-physical-properties` · asset_id=`mol-butanoic-acid` · anchor="closing an eight-membered ring held by two hydrogen bonds"

**Observation:** The cyclic hydrogen-bonded dimer is the single structural idea carrying the whole physical-properties section, the boiling-point comparison, the vapour-density argument, and the very broad 2500-3300 cm-1 O-H band in the spectroscopy section. No asset depicts it. The section's two figures are isolated monomers, neither showing a hydrogen bond, the head-to-head pairing, or the eight-membered ring.

**Learner impact:** Students are asked in ch20-acid-alcohol-hbond-matrix to decide whether each compound 'pairs into a discrete cyclic dimer held by two hydrogen bonds' having never seen one drawn. The distinction the chapter rests on - a discrete two-molecule pair versus an extended alcohol network - is inherently a picture.

**Evidence:** nuggets[1].asset_ids = ['mol-butanoic-acid','mol-butan-1-ol']; assets contains no dimer, no hydrogen-bond depiction and no eight-membered-ring figure.

**Recommended outcome (need):** The physical-properties section needs a representation that makes the two-molecule pairing and its two hydrogen bonds visible and contrastable with an extended alcohol network.

##### `instr-006` — HIGH · figure-purpose · confidence 0.9

**Location:** section_id=`nugget-carboxylic-acid-acidity` · asset_id=`mol-acetate-ion` · concept_slug=`carboxylic-acid-acidity` · anchor="the two contributing resonance structures are related by exchanging which oxygen carries the double bond"

**Observation:** The chapter's central argument is that the carboxylate is a symmetric hybrid with two equivalent C-O bonds at 127 pm. The only carboxylate figure, mol-acetate-ion, is drawn as CC(=O)[O-] with alt text describing 'one double-bonded oxygen and one singly bonded oxygen with a negative charge' - exactly the localized representation the concept trouble spot warns against. Neither the resonance pair nor the delocalized hybrid appears anywhere, and the asset that would have shown it (video-carboxylate-delocalization) is deferred and compiles to an empty-url video block.

**Learner impact:** The single picture a student sees of a carboxylate teaches the misconception the chapter tells them to avoid, with no counter-image. Students then meet ch20-acidity-vs-alcohol-reasoning-v2, which asks them to argue from equal 127 pm bond lengths, with no figure that has ever shown those bonds as equal.

**Evidence:** assets mol-acetate-ion (smiles CC(=O)[O-], accessibility.alt_text); concepts[2].trouble_spots[1]; video_briefs video-carboxylate-delocalization production_status 'deferred'.

**Recommended outcome (need):** The acidity section needs the carboxylate shown as a symmetric hybrid alongside the localized Lewis structure students must still be able to draw, so the figure supports rather than undercuts the trouble spot.

##### `instr-007` — HIGH · figure-purpose · confidence 0.93

**Location:** section_id=`nugget-reactions-of-nitriles` · asset_id=`video-nitrile-hydrolysis` · anchor="Open on pentanenitrile with the C≡N polarization marked"

**Observation:** All three video briefs are production_status 'deferred', yet the compiler still emits a video block for each into the reader with url = '' and with the first storyboard line reused as the block description. Sections nugget-carboxylic-acid-acidity, nugget-preparation-of-carboxylic-acids and nugget-reactions-of-nitriles each carry one.

**Learner impact:** A student sees three empty video players whose descriptions are stage directions, which reads as broken content and promises the mechanism animation these three sections most need. The deferral notes assume 'the reader carries the same content in the nugget', but nothing tells the student that.

**Evidence:** Compiled reader - three blocks with block_type 'video' and content.url == ''; video_briefs[*].production_status == 'deferred'.

**Recommended outcome (need):** Deferred video briefs must not surface to a student as an empty player; the reader needs either the still-figure equivalent the deferral notes claim exists, or suppression of the block.

##### `instr-008` — MEDIUM · sequencing · confidence 0.85

**Location:** concept_slug=`preparation-of-carboxylic-acids` · section_id=`nugget-preparation-of-carboxylic-acids` · asset_id=`roadmap-nitrile-homologation` · anchor="an alkyl halide is first converted to a nitrile by SN2 displacement with cyanide ion"

**Observation:** Concept 5 teaches cyanide SN2 displacement, the nitrile intermediate, nitrile hydrolysis and the SN2 substrate limits in full, and carries the roadmap asset whose concept_slugs include both nitrile concepts. But nitrile-structure-naming-and-preparation is order 7 and reactions-of-nitriles is order 8, and concept 5's prerequisites list only carboxylic-acid-structure-and-naming.

**Learner impact:** A student working the declared order meets pentanenitrile, its SN2 formation and its hydrolysis two sections before nitriles are defined, before they know the nitrile carbon is C1, and before they know why the sp carbon is electrophilic. The prerequisite graph also tells any downstream tool that section 5 is safe to serve first, which it is not.

**Evidence:** concepts: preparation-of-carboxylic-acids order 5 with prerequisites ['carboxylic-acid-structure-and-naming']; nitrile concepts at order 7 and 8; nuggets[5].text.expanded paragraph 3; assets roadmap-nitrile-homologation.

**Recommended outcome (need):** Either the nitrile material concept 5 depends on must be declared as a prerequisite and the ordering adjusted, or section 5 must introduce the nitrile route by forward reference only.

##### `instr-009` — MEDIUM · objective-alignment · confidence 0.87

**Location:** section_id=`nugget-carboxylate-salts-and-extraction` · nugget_id=`nugget-carboxylate-salts-and-extraction` · concept_slug=`carboxylic-acid-acidity` · anchor="Select a base that will deprotonate a carboxylic acid but not a phenol."

**Observation:** The apply-nugget on carboxylate salts declares three learning objectives - choose a base that deprotonates an acid but not a phenol, describe an acid-base extraction, and relate carboxylate salts to soaps. Across all 42 question_sets, the only item touching this material is ch20-draw-carboxylate-v2, a single-step deprotonation draw. Nothing assesses the bicarbonate-versus-phenol selectivity, the extraction workflow, the reacidification step, or the soap connection.

**Learner impact:** Acid-base extraction is the one lab-transferable skill in this chapter and it is taught but never practised. A student can score full marks without ever having decided which layer a carboxylate ends up in or which base distinguishes an acid from a phenol.

**Evidence:** nuggets[3].learning_objectives; question_sets contains no item with an extraction, layer-separation, bicarbonate-selectivity or soap stem across all 42 slugs.

**Recommended outcome (need):** The extraction/carboxylate-salt objectives need graded practice that makes a student choose the base and track the compound between layers, since the point of the section is a procedure rather than a product.

##### `instr-010` — MEDIUM · assessment-readiness · confidence 0.85

**Location:** concept_slug=`reactions-of-nitriles` · question_slug=`ch20-nitrile-sn2-arrow` · section_id=`nugget-reactions-of-nitriles` · anchor="Every reaction of the group therefore opens with addition of a nucleophile to that carbon"

**Observation:** The chapter's organizing mechanistic claim for nitriles is that every reaction begins with nucleophilic addition to the electrophilic sp carbon, producing an sp2 anion with charge on nitrogen. No assessment item exercises that step. The only curved_arrow items draw the cyanide SN2 displacement, which belongs to the alkyl-halide chapter, and the only bond_change_ledger items are proton transfers. Hydrolysis, LiAlH4, DIBAH and Grignard addition are all assessed purely as product-recall.

**Learner impact:** Students can answer every nitrile question by memorizing four reagent-to-product pairs, which is exactly the memorization the prose is trying to replace. Nothing distinguishes a student who understands why DIBAH stops after one addition from one who has memorized 'DIBAH gives aldehyde'.

**Evidence:** nuggets[8].text.expanded; ch20-nitrile-sn2-arrow / -v2 molecule_smiles are both SN2 at the halide carbon; the hydrolysis and reduction items are single_select/short_answer product recall.

**Recommended outcome (need):** The nitrile section needs at least one item that makes the student commit to the addition step itself - the electron source, the atom attacked, where the resulting charge sits.

##### `instr-011` — MEDIUM · visual-opportunity · confidence 0.86

**Location:** section_id=`nugget-spectroscopy-acids-nitriles` · concept_slug=`spectroscopy-of-carboxylic-acids-and-nitriles` · question_slug=`ch20-ir-triple-bond-region` · anchor="The infrared spectrum of a carboxylic acid is one of the most distinctive in organic chemistry."

**Observation:** The spectroscopy section claims the carboxylic acid IR spectrum is 'one of the most distinctive in organic chemistry' and describes a very broad 2500-3300 cm-1 band swamping the C-H region with a strong 1710 cm-1 carbonyl underneath. Its only two assets are plain structures. No spectrum is shown, and both spectroscopy questions are text-only.

**Learner impact:** 'Very broad' and 'sharp and of medium intensity' are shape judgements a student cannot calibrate from words. The point of the section - recognizing a pattern on sight - is never practised on a spectrum, so students are trained to recall wavenumbers rather than read a trace.

**Evidence:** nuggets[9].asset_ids = ['mol-propanoic-acid','mol-benzonitrile']; assets contains no spectrum-type asset; both questions are numeric recall or prose-described bands.

**Recommended outcome (need):** The spectroscopy section needs at least one actual spectrum a student reads, so the broad-O-H-plus-1710 signature and the sharp-versus-weak triple-bond discrimination are learned as visual patterns.

##### `instr-012` — MEDIUM · objective-alignment · confidence 0.8

**Location:** question_slug=`ch20-inductive-distance-v2` · concept_slug=`substituent-effects-on-acidity` · anchor="Acetic acid, fluoroacetic acid, difluoroacetic acid, and trifluoroacetic acid differ only in how many hydrogens"

**Observation:** Several -v2 items are labelled variant_of their parent but assess a different objective, so the pair is not interchangeable. ch20-inductive-distance tests distance decay while its v2 tests cumulative substitution; ch20-nitrile-hydrolysis-product tests hydrolysis while its v2 tests DIBAH reduction; ch20-side-chain-oxidation-product tests side-chain degradation while its v2 tests primary-alcohol oxidation; ch20-carbonyl-ir-wavenumber asks for the C=O band while its v2 asks for the C-N band; ch20-nitrile-reduction-product tests LiAlH4 while its v2 tests Grignard addition.

**Learner impact:** If the platform serves one item per variant pair - which is what variant_of implies - whichever objective lost the draw goes unassessed. The declared objective about inductive fall-off with distance and the side-chain-oxidation objective each survive in only one member of a pair.

**Evidence:** question_sets: the five slug pairs above, each with variant_of set to the parent but a different sub-skill in prompt_text and answer_key; compiled counts 21 surfaced, 21 staged_variants.

**Recommended outcome (need):** Items that test a different sub-skill from their parent should not be registered as interchangeable variants of it; each declared objective needs coverage that survives whichever member is served.

##### `instr-013` — MEDIUM · notation-consistency · confidence 0.83

**Location:** section_id=`nugget-carboxylic-acid-dimers` · concept_slug=`carboxylic-acid-physical-properties` · anchor="solubility falls steeply beyond about six carbons"

**Observation:** The chain-length threshold for water solubility is stated three different ways within the same concept. The trouble spot says solubility falls sharply 'once the hydrocarbon chain exceeds about four carbons'; the standard text tier says 'beyond about six carbons'; the expanded tier (the one compiled into the reader) says formic through butanoic are miscible and 'pentanoic acid is partly soluble', which matches four, not six.

**Learner impact:** Students on different depth settings, and students comparing the reader against a deck built from the standard tier, get different cutoffs for the same fact, and the six-carbon figure is the loose one. Any question built from the standard tier will disagree with the reader.

**Evidence:** concepts[1].trouble_spots[1]; nuggets[1].text.standard versus nuggets[1].text.expanded.

**Recommended outcome (need):** One solubility threshold, consistent across the trouble spot and all three text tiers.

##### `instr-014` — LOW · assessment-readiness · confidence 0.82

**Location:** question_slug=`ch20-carbonyl-ir-wavenumber` · concept_slug=`spectroscopy-of-carboxylic-acids-and-nitriles` · anchor="A saturated, unconjugated carboxylic acid shows a strong C=O infrared absorption."

**Observation:** Both numeric items use tolerance {mode absolute, amount 20}, which is exactly the shift the chapter attributes to conjugation. ch20-carbonyl-ir-wavenumber (key 1710) therefore accepts 1690, the value the chapter gives for a CONJUGATED acid, on a prompt that says 'saturated, unconjugated'; the v2 (key 2250) accepts 2230, the conjugated-nitrile value, on a prompt that says 'unconjugated'.

**Learner impact:** A student who has confused the conjugated and unconjugated values - the exact discrimination both items exist to test - is scored correct, so the item cannot detect the misconception it targets, and its own feedback then explains a distinction the grader just ignored.

**Evidence:** ch20-carbonyl-ir-wavenumber.answer_key [redacted] with feedback 'Conjugation ... shifts it about 20 cm-1 lower'; -v2 {value 2250, tolerance {absolute, 20}}.

**Recommended outcome (need):** The accepted band needs to exclude the conjugated value the prompt rules out, so the tolerance does not swallow the distinction being assessed.

##### `instr-015` — LOW · objective-alignment · confidence 0.84

**Location:** concept_slug=`nitrile-structure-naming-and-preparation` · section_id=`nugget-nitrile-structure-and-preparation` · anchor="Recognize dehydration of a primary amide as the second general preparation."

**Observation:** Two declared objectives in the nitrile section have no assessment. Amide dehydration with SOCl2 or P2O5 is taught as one of the two general nitrile preparations and appears in no question, matching item or synthesis route. Nitrile nomenclature is likewise assessed only through the practice check - both short_answer naming items name carboxylic acids.

**Learner impact:** Students are told amide dehydration matters because it escapes the SN2 substrate limits, and then never asked to use it, so it will not be available when a synthesis problem presents a secondary or tertiary substrate. Nitrile naming is left entirely to self-check despite being an objective and a named trouble spot.

**Evidence:** nuggets[7].learning_objectives[1] and [2]; question_sets contains no item mentioning SOCl2/P2O5 or amide dehydration; both naming items target carboxylic acids.

**Recommended outcome (need):** The amide-dehydration route and nitrile nomenclature each need at least one graded item if they are to remain declared objectives.

##### `instr-016` — LOW · conceptual-support · confidence 0.86

**Location:** section_id=`nugget-preparation-of-carboxylic-acids` · concept_slug=`reactions-of-nitriles` · anchor="Wikipedia — Preparation of carboxylic acids"

**Observation:** Every section's Additional Reading link is titled with the section's own topic but resolves to a single generic Wikipedia article taken from the concept's wikipedia_title, and several do not match the label: 'Preparation of carboxylic acids' goes to Grignard_reagent, 'Reactions of nitriles' goes to Lithium_aluminium_hydride, 'Hydrogen-bonded dimers and physical properties' goes to Hydrogen_bond, and 'Acidity of carboxylic acids and the carboxylate ion' goes to Acid_dissociation_constant and is repeated in two consecutive sections. The only OpenStax link is the chapter landing page.

**Learner impact:** A student following 'Reactions of nitriles' lands on a reagent article covering none of hydrolysis, DIBAH or Grignard addition, and an instructor has no section-level OpenStax reading to point at. Mislabelled links erode trust in the reading apparatus generally.

**Evidence:** Compiled reader external_link blocks across all ten sections (titles versus urls); the single mcmurry_link is the chapter opener.

**Recommended outcome (need):** Additional Reading needs link labels that describe where the link actually goes, and section-level assigned reading rather than a single chapter-opener link.

##### `instr-017` — LOW · assessment-readiness · confidence 0.87

**Location:** question_slug=`ch20-nitrile-sn2-arrow` · concept_slug=`nitrile-structure-naming-and-preparation` · anchor="the reactive electrons are the lone pair on carbon, not on nitrogen"

**Observation:** The v1 curved-arrow item's feedback teaches that cyanide reacts through the carbon lone pair 'not on nitrogen', but the nitrogen is not offered as a selectable site - sites are the cyanide carbon, the C-Br carbon, the bromine and a terminal methyl carbon. The v2 item does offer the nitrogen and is the better-designed of the pair.

**Learner impact:** The item cannot detect the misconception its own feedback is written to correct, and a student who believes nitrogen attacks is never given the chance to reveal it; the feedback addresses a choice they were never shown.

**Evidence:** ch20-nitrile-sn2-arrow.student_config.sites (ids 0, 5, 6, 2; no site for the nitrile nitrogen) versus feedback_bundle.generic_incorrect_explanation; compare -v2 which includes 'Cyanide nitrogen (lone pair)'.

**Recommended outcome (need):** The v1 item needs the nitrogen available as a selectable electron source so the ambidentate-nucleophile misconception its feedback addresses is diagnosable, matching the v2 design.

**Open questions**

- All three video briefs are deferred with production notes asserting 'the reader carries the same content in the nugget'. For the delocalization brief that is not true - no still figure shows the resonance hybrid or the equalized bond lengths. Was a still-figure substitute intended, and is the empty-url video block a compiler behaviour affecting other chapters?
- roadmap-nitrile-homologation carries science_review.status 'not_reviewed' with agent_revised true, and the chapter-level science_review is also 'not_reviewed'. Is a science review expected before seeding?
- All 42 items have demo_eligible false. Deliberate for an unseeded chapter, or an oversight?
- The reader compiles only the expanded tier. Are the terse and standard tiers consumed by any surface a student or instructor sees? That determines whether the four-versus-six-carbon solubility discrepancy is student-facing.
- ch20-acidity-rank asks students to place acetic acid (4.76) above propanoic acid (4.87) - a 0.11 pKa unit gap. Partial credit is on, but is a difference that small intended to be a graded discrimination?

#### Struggling Student — 6.6/10

This chapter is better scaffolded than most: every one of the ten reader sections ships a named-mistakes callout and a self-check prompt, and all 42 bank questions carry two or three progressive hints plus specific wrong-answer explanations. What defeats a shaky student is not the absence of structure but three things underneath it. First, pKa is used 49 times in the rendered reader and never once defined - no Ka, no logarithm, no statement of what one pKa unit means - and the single sentence telling me which direction the scale runs sits in a warning callout three sections after I was first asked to compare 4.76 with 16. Second, 'oxidation level' carries the reasoning in nine questions' graded feedback but appears exactly once in the rendered chapter text and is never explained, so the feedback that is supposed to rescue me uses a tool I was never given. Third, there is no worked example anywhere: every practice answer is a conclusion, never a derivation, and all 20 assets are static single molecules plus one two-step roadmap - no electron-flow figure, no intermediate structure, and the three animations that would have carried the carboxylate, hydrolysis and homologation mechanisms are compiled in as blocks with empty URLs while curved-arrow and bond-ledger items are still graded. Nothing is impossible to complete, so I file no publication blockers, but I would guess on the acidity items and stall outright in the nitrile-reactions section.

**Publication blockers:** _none_

**Strengths**

- Every one of the ten reader sections carries a 'Common ways this goes wrong' callout naming concrete wrong moves - the single most useful thing in the chapter for a student like me, and eight of the ten lists are section-specific and accurate.
- Every one of the 42 bank questions ships two or three progressive text hints, and the hints genuinely ladder: level 1 orients, level 3 nearly finishes the reasoning without stating the answer.
- Wrong-answer explanations are specific rather than generic - ch20-grignard-carboxylation explains separately why the four-carbon acid, the four-carbon alcohol and the five-carbon alcohol each fail, which tells me which mistake I actually made.
- One worked comparator recurs deliberately across three sections (1-bromobutane to pentanenitrile to pentanoic acid, in the preparation prose, the roadmap asset, the nitrile-reactions section and two synthesis_route questions), so the chain-lengthening idea gets the repetition it needs.
- Carbon counting is repeatedly foregrounded as the first move in a synthesis decision, in both the prose and the hint ladders - a concrete, checkable procedure a low-confidence student can execute.
- The chapter says out loud when it is deferring material ('The full development of these substitutions ... belongs to the following chapter'), which stops me hunting for content that is not there.

**Findings**

##### `stud-001` — HIGH · conceptual-support · confidence 0.95

**Location:** section_id=`nugget-carboxylic-acid-acidity` · concept_slug=`carboxylic-acid-acidity` · nugget_id=`nugget-carboxylic-acid-acidity` · anchor="Acetic acid has a pKa of 4.76 and formic acid 3.75, against 16 for ethanol and 10 for phenol."

**Observation:** The rendered reader uses 'pKa' 49 times and never defines it. There is no occurrence of 'Ka', 'acid dissociation constant', 'logarithm', or any statement that one pKa unit corresponds to a factor of ten. The acidity section opens by asking the reader to compare 4.76, 3.75, 16 and 10 in its second sentence. The only statement of which direction the scale runs is buried in a warning callout in the fifth section, two sections after the reader is first asked to reason with the numbers.

**Learner impact:** A student with weak general-chemistry recall reads '4.76 versus 16' and cannot tell whether bigger means more acidic. I invent a rule from the first example, carry it silently through four sections, and then guess on ch20-acidity-rank, ch20-stronger-than-acetic and ch20-inductive-distance-v2 - three items whose whole task is reading the scale in the right direction. When ch20-stronger-than-acetic-v2 deliberately reverses the question ('weaker acid than acetic acid') I have no anchor at all.

**Evidence:** Reader blk-4jkx8xxr (expanded tier); the direction rule appears only in blk-w7cfglsn, section nugget-substituent-effects-acidity; grep of the compiled reader returns 0 hits for 'logarith', 'acid dissociation' and 'equilibrium constant' and 49 for 'pKa'. Both ch20-stronger-than-acetic-v2 and ch20-inductive-distance-v2 place the direction rule in hint level 1, implying the authors knew it was the failure point.

**Recommended outcome (need):** Before the first numerical comparison, a student needs to be told plainly what a pKa number is, that the scale is logarithmic so each unit is a factor of ten, and that smaller means stronger - in the chapter's default reading path, not in a downstream warning callout.

##### `stud-002` — HIGH · conceptual-support · confidence 0.93

**Location:** section_id=`nugget-reactions-of-nitriles` · concept_slug=`reactions-of-nitriles` · question_slug=`ch20-nitrile-hydrolysis-product-v2` · anchor="Selecting between the two reagents is therefore a way of choosing the oxidation level of the product."

**Observation:** 'Oxidation level' is the load-bearing idea in the graded feedback of nine questions, including distractor rebuttals that consist of nothing else ('This is the fully reduced oxidation level', 'The carbon count is right but the oxidation level is not'). In the rendered reader text the phrase occurs exactly once, in the sentence quoted above, and is never explained: the chapter never says how to decide whether one carbon is at a higher oxidation level than another.

**Learner impact:** I get an item wrong, open the explanation hoping to be rescued, and the explanation is written in a vocabulary the chapter never taught me. I cannot self-correct, so I memorise the reagent-to-product pair instead of the reasoning, and I fail the next variant that swaps the reagent.

**Evidence:** Reader blk-by2fv32g is the sole rendered occurrence; the compiled question set contains 16 occurrences across 9 questions.

**Recommended outcome (need):** The chapter needs an explicit, usable account of what 'oxidation level' means for a carbon and how to compare two carbons, positioned before the preparations and reactions sections - otherwise the feedback vocabulary must be rewritten into terms the reader defines.

##### `stud-003` — HIGH · worked-example-gap · confidence 0.9

**Location:** section_id=`nugget-preparation-of-carboxylic-acids` · concept_slug=`preparation-of-carboxylic-acids` · nugget_id=`nugget-preparation-of-carboxylic-acids` · anchor="Either route adds the required carbon, but the halide is primary and unhindered at the reacting carbon"

**Observation:** No section walks a complete problem from start to finish. All ten self-check callouts give a prompt and then a two-sentence conclusion with the reasoning already collapsed: '3-Methylbutanoic acid. The carboxyl carbon is C1...' never shows the chain being traced and numbered; the spectroscopy answer names but-2-enoic acid without showing how C4H6O2 plus a lowered carbonyl leads there. The one multi-step artifact, roadmap-nitrile-homologation, is a three-node schematic, not a worked derivation.

**Learner impact:** The step I get stuck on is always the first one - deciding what to count, where to start numbering, which comparison to set up. Seeing only the finished answer confirms I was wrong without telling me where I went wrong, so I stop attempting the checks and read them as facts to memorise.

**Evidence:** Reader blocks blk-cincpmj5, blk-omel5kf8, blk-xo67uew4, blk-mgvpnzo5, blk-ph3vlaeu, blk-qm5w50m3, blk-10bwyz1m, blk-tlh7hv4r, blk-l6ie2hja, blk-etsdc9ci - every one is prompt plus verdict. Asset inventory: 19 molecule assets and 1 synthesis_roadmap.

**Recommended outcome (need):** At least one problem per major skill needs to be shown being solved step by step, with the decision points a student actually stumbles on made visible rather than assumed.

##### `stud-004` — HIGH · cognitive-load · confidence 0.88

**Location:** section_id=`nugget-reactions-of-nitriles` · asset_id=`video-nitrile-hydrolysis` · question_slug=`ch20-nitrile-sn2-arrow` · anchor="producing an sp² anion in which the charge sits on nitrogen"

**Observation:** The chapter contains no electron-flow or intermediate-structure figure of any kind. Every reaction is carried by prose alone: 'the lone pair on the carbon of cyanide ion - not the lone pair on its nitrogen - attacks the carbon bearing the halogen from the side opposite the leaving group', 'producing an sp2 anion in which the charge sits on nitrogen', 'the intervening imine anion'. None of these species is drawn anywhere. The three video briefs authored to carry exactly this content compile into the reader with empty urls. Meanwhile the bank grades two curved_arrow items and two bond_change_ledger items on this same electron flow.

**Learner impact:** Curved arrows are the representation I am weakest at, and this chapter asks me to produce them and to enumerate bond and charge changes after showing me not one arrow. I try to hold 'sp2 anion', 'imine anion' and 'charge on nitrogen' as words with no picture attached, run out of working memory, and pick the answer that sounds most like the sentence I half-remember.

**Evidence:** Package assets: 19 molecule + 1 synthesis_roadmap, zero mechanism/curved-arrow types. Reader video blocks blk-fa6z5rhw, blk-0ljj3bkv, blk-jc0mqivv all carry url ''. Questions ch20-nitrile-sn2-arrow(-v2), ch20-deprotonation-ledger(-v2).

**Recommended outcome (need):** The electron flow the chapter grades needs to reach the student in some non-prose form, and the intermediates named in the text - the imine anion above all - need to exist as something a student can look at.

##### `stud-005` — MEDIUM · misconception · confidence 0.92

**Location:** section_id=`nugget-carboxylate-salts-and-extraction` · concept_slug=`carboxylic-acid-acidity` · anchor="Drawing a carboxylate with one C=O and one C–O⁻ and treating those bonds as different"

**Observation:** The 'Common ways this goes wrong' callout in the acid-base extraction section is a verbatim copy of the callout in the preceding acidity section - the same three warnings about O-H bond strength, carboxylate bond equivalence and 'strong acid'. This happens because the nugget's section_id is carboxylic-acid-acidity, so it inherits that concept's trouble_spots. None of the three has anything to do with extraction, and the traps that actually catch students here are named nowhere: forgetting that the acid must be re-acidified to be recovered, losing track of which layer holds what, and assuming hydroxide and bicarbonate are interchangeable when the whole point is that they are not.

**Learner impact:** I read the same three warnings twice and skim them the second time, so the section's real hazard passes unflagged. In the lab or on a separation question I shake with bicarbonate, take the aqueous layer, and forget to acidify - the exact move the chapter had a slot to warn me about and spent on a duplicate.

**Evidence:** Reader blk-2hoo49iu is character-identical to blk-xfi32b30; concept carboxylic-acid-acidity trouble_spots is the source for both, and nugget-carboxylate-salts-and-extraction has section_id 'carboxylic-acid-acidity'.

**Recommended outcome (need):** The extraction section needs its own named wrong moves, drawn from what students actually get wrong in a two-layer separation, rather than inheriting the acidity section's list.

##### `stud-006` — MEDIUM · conceptual-support · confidence 0.9

**Location:** section_id=`nugget-carboxylic-acid-structure-naming` · nugget_id=`nugget-carboxylic-acid-structure-naming` · anchor="The carboxyl group, –COOH, places a carbonyl and a hydroxyl group on a single carbon"

**Observation:** Every nugget carries a learning_objectives array (thirty in total) and none reaches the compiled reader - a grep for the objective text returns zero hits, and no block type carries them. The chapter also has no introduction and no summary: section one opens directly on the carboxyl-group sentence and section ten ends on a Wikipedia link. Everything between is three to four paragraphs of equally weighted prose per section.

**Learner impact:** I cannot tell what I am supposed to be able to do when I finish, so I try to remember all of it equally - the pKa of 4-methoxybenzoic acid gets the same weight in my notes as the fact that a smaller pKa means a stronger acid. When I run out of time I have memorised numbers and missed the three ideas the chapter is built on.

**Evidence:** Package nuggets each define learning_objectives; compiled reader block types are limited to text, callout, molecule, teaching_asset, video, mcmurry_link, external_link, with no objective or summary block.

**Recommended outcome (need):** A student needs to know, before reading and again after, what this chapter expects of them and which few ideas carry the rest - the objectives already authored are not reaching the page they were written for.

##### `stud-007` — MEDIUM · retrieval-practice · confidence 0.82

**Location:** section_id=`nugget-carboxylic-acid-structure-naming` · anchor="**Try it.** Give the IUPAC name of (CH₃)₂CHCH₂COOH, and state which carbon is C1."

**Observation:** Each self-check callout puts the prompt and the answer in the same markdown block, one blank line apart, so the answer is on screen the moment the question is. Separately, the 42-item question bank does not surface in the reader at all: the compiled chapter contains no question block of any kind, and all 42 items are demo_eligible false. The reader's entire retrieval offering is therefore ten prompts whose answers are already visible.

**Learner impact:** I read the prompt, my eye lands on the answer, and I feel that I knew it - the illusion of fluency that low-confidence students are most vulnerable to. I never actually retrieve anything between sections, so I arrive at graded work believing I understood the chapter.

**Evidence:** Reader blk-cincpmj5 and its nine siblings; compiled question-set counts show 42 questions / 0 demo_eligible, and no question block type appears in the reader chapter JSON.

**Recommended outcome (need):** A student needs at least one genuine attempt-before-answer opportunity between sections; as compiled, the chapter offers recognition where it intends retrieval.

##### `stud-008` — MEDIUM · cognitive-load · confidence 0.8

**Location:** section_id=`nugget-carboxylic-acid-acidity` · anchor="Accounting for the deprotonation itself is straightforward: exactly one bond breaks"

**Observation:** The third paragraph of the acidity section runs four distinct ideas together with no signposting: an atom-by-atom bond-and-charge ledger of the deprotonation, the sodium formate bond-length evidence (127 pm versus 120 and 134 pm), an inductive contribution from the carbonyl group, and a closing caveat that a pKa near 5 still means under 2 percent dissociation. The ledger passage is written as running prose about atoms that are not drawn anywhere, and nothing tells the reader why it is there.

**Learner impact:** I came to this section for one thing - why carboxylic acids are acidic - and by the end of the paragraph I am tracking three numbers in picometres and a percentage. I lose the resonance argument I had just understood, reread from the top, and if the reread does not help I skip to the callout and take the three warnings as the section's content.

**Evidence:** Reader blk-4jkx8xxr, third paragraph of the rendered expanded tier.

**Recommended outcome (need):** The deprotonation bookkeeping, the structural evidence and the strength caveat each need their own space with a stated purpose, so a reader can finish the core resonance argument before the supporting material arrives.

##### `stud-009` — MEDIUM · misconception · confidence 0.78

**Location:** section_id=`nugget-carboxylic-acid-dimers` · anchor="The alcohol forms an extended hydrogen-bonded network, but the acid forms a discrete two-hydrogen-bond dimer"

**Observation:** The self-check answer justifies the acid's higher boiling point with a contrast that reads backwards to a novice: the alcohol gets an 'extended hydrogen-bonded network' and the acid only a 'discrete' pair of hydrogen bonds, yet the acid is said to boil higher. The answer never explains why a discrete two-bond pair costs more energy to separate than an extended network. The section body uses a different and clearer argument, so the two accounts within one section do not line up.

**Learner impact:** I read 'extended network' as stronger, conclude the answer contradicts itself, and either decide I have misunderstood hydrogen bonding entirely or memorise 'acid boils higher' as a fact with no reason attached. On ch20-dimer-boiling-point-v2 I then cannot distinguish the dimer explanation from the dispersion-forces distractor on reasoning.

**Evidence:** Reader blk-omel5kf8 (answer text) against blk-jwcj69m3 paragraph two ('Vaporization requires separating a pair of molecules rather than one').

**Recommended outcome (need):** The self-check answer needs to use the same mechanism the section body teaches, and to say explicitly why the paired unit is the thing that must be vaporised.

##### `stud-010` — MEDIUM · cognitive-load · confidence 0.85

**Location:** section_id=`nugget-reactions-of-nitriles` · concept_slug=`reactions-of-nitriles` · anchor="Carbon nucleophiles behave like DIBAH."

**Observation:** The nitrile-reactions section introduces 'diisobutylaluminium hydride' by full name in one sentence and then refers to 'DIBAH' in the next without ever stating that the acronym names the same reagent. In the same three paragraphs the reader must absorb 'imine anion' (used four times, never defined and never drawn), 'sp2 anion' and 'aqueous workup' - none explained. A graded item then hands the student 'diisobutylaluminium hydride (DIBAH)' and requires the one-addition behaviour.

**Learner impact:** 'DIBAH' reads as a fifth reagent I missed, so I go back looking for where it was introduced, do not find it, and lose confidence that I am reading carefully enough. 'Imine anion' I cannot picture at all, so the distinction between one hydride addition and two - the entire content of the section - becomes an arbitrary pair of rules to memorise.

**Evidence:** Reader blk-by2fv32g paragraphs three and four; 'imine' also appears in blk-cfqjhod8 and blk-340m5uey with no definition anywhere.

**Recommended outcome (need):** The abbreviation needs to be bound to the name where it is first used, and 'imine anion' needs to be something the student can define and recognise before the section asks them to reason about its fate.

##### `stud-011` — MEDIUM · cognitive-load · confidence 0.83

**Location:** section_id=`nugget-carboxylate-salts-and-extraction` · asset_id=`mol-benzoic-acid` · anchor="Benzoic acid is the reference compound for ring-substituent effects on acidity and the product of side-chain oxidation"

**Observation:** Molecule assets are reused across sections carrying the caption written for their first appearance. In the extraction section the benzoic acid figure is captioned entirely about ring-substituent effects and side-chain oxidation - two topics belonging to other sections and neither yet introduced. In the reactions section the butanoic acid figure is captioned about boiling at 164 degrees because the carboxyl group pairs into a dimer, which has nothing to do with reduction or acyl substitution.

**Learner impact:** I use captions to work out why a picture is on the page. When the caption talks about something the section has not covered, I assume I have missed material, scroll back to look for it, and lose the thread. In the extraction section the caption also forward-references side-chain oxidation, which makes me think oxidation is part of extraction.

**Evidence:** Reader blk-5k9iyki8 and blk-47oi6px4 share an identical description string; blk-awrmz64h and blk-jjggvrkj in nugget-reactions-of-carboxylic-acids carry the boiling-point captions from nugget-carboxylic-acid-dimers.

**Recommended outcome (need):** When a structure is reused, its caption needs to say what that structure is doing in the section the reader is currently in.

##### `stud-012` — MEDIUM · cognitive-load · confidence 0.87

**Location:** section_id=`nugget-carboxylic-acid-dimers` · nugget_id=`nugget-carboxylic-acid-dimers` · anchor="The lower carboxylic acids also have sharp, unpleasant odours"

**Observation:** The three detail tiers are paraphrases rather than nested levels, so the shorter tiers are not subsets of the rendered one. Facts present in 'standard' and absent from the rendered 'expanded' text include the odour hook for physical properties, 'Electrostatic potential maps show the charge divided between the two oxygens' in the acidity section, acetonitrile's 82 degree boiling point, and the names 'dichloroacetic acid' and 'trichloroacetic acid' attached to pKa 1.29 and 0.65 (expanded says only 'a second chlorine gives 1.29, a third 0.65').

**Learner impact:** Turning the detail down is the first thing an overwhelmed student does, and here it does not simplify the same material - it swaps in different material. On ch20-stronger-than-acetic-v2, which names 'Dichloroacetic acid' as an option, I have to map a name I never saw onto 'a second chlorine' from the tier I read.

**Evidence:** _detail_texts comparison in the compiled reader: 'rancid', 'odour', 'Electrostatic', '82', 'dichloroacetic' and 'trichloroacetic' each appear in the standard tier and zero times in the rendered expanded markdown.

**Recommended outcome (need):** The tier a struggling student drops to should contain a subset of the default tier's content, not a partly disjoint set, so lowering detail never removes something the graded work assumes.

##### `stud-013` — MEDIUM · conceptual-support · confidence 0.8

**Location:** section_id=`nugget-substituent-effects-acidity` · concept_slug=`substituent-effects-on-acidity` · question_slug=`ch20-acidity-rank-v2` · anchor="parallels the activating and deactivating ordering established for electrophilic aromatic substitution"

**Observation:** The ring-substituent argument is handed off to a prior chapter in a single clause. Neither 'activating' nor 'deactivating' is defined or exemplified here, and the mapping is stated in compressed form. The graded item ch20-acidity-rank-v2 requires exactly this mapping, and its own feedback repeats the same shortcut: 'read in the corresponding direction'.

**Learner impact:** If the aromatic-substitution chapter did not stick - and for me it did not - this sentence gives me nothing to hold. I cannot recover the ordering, so I guess between nitro and chloro and between benzoic and methoxy, and the wrong-answer feedback sends me back to the same clause that failed me.

**Evidence:** Reader blk-7e0w6n0m paragraph three; ch20-acidity-rank-v2 generic_incorrect_explanation.

**Recommended outcome (need):** The chapter needs to make the ring-substituent ordering usable on its own terms - a student who has forgotten the earlier chapter should still be able to rank 4-nitro, 4-chloro, unsubstituted and 4-methoxy from what is on this page.

##### `stud-014` — MEDIUM · cognitive-load · confidence 0.85

**Location:** section_id=`nugget-spectroscopy-acids-nitriles` · concept_slug=`spectroscopy-of-carboxylic-acids-and-nitriles` · anchor="carboxylic acids with a hydrogen on the γ carbon undergo the McLafferty rearrangement"

**Observation:** The final sentence of the spectroscopy section introduces the gamma carbon, the McLafferty rearrangement, a diagnostic fragment at m/z 60 and alpha cleavage with losses of 17 and 45 mass units - five new items in one sentence, with no setup, no explanation of why m/z 60 results, and no figure. Nothing earlier mentions mass spectrometry, and no learning objective for this nugget covers it.

**Learner impact:** I hit a sentence with five unfamiliar terms at the end of an already dense section and simply stop reading - this is the point where I close the chapter. If I do try to memorise it, I store 60, 17 and 45 as unlinked numbers because nothing shows me where they come from.

**Evidence:** Reader blk-dqbizggc, final sentence of paragraph three; nugget-spectroscopy-acids-nitriles learning_objectives make no reference to mass spectrometry.

**Recommended outcome (need):** Either the mass-spectrometry content needs enough setup for a student to see where the fragment masses come from, or it needs to be marked as reference material rather than dropped into the reading path as expected recall.

##### `stud-015` — MEDIUM · conceptual-support · confidence 0.75

**Location:** section_id=`nugget-reactions-of-carboxylic-acids` · question_slug=`ch20-acid-reduction-reagent-v2` · anchor="because it reacts with the electron-rich carbonyl oxygen of the acid"

**Observation:** Borane's selectivity for the acid over a ketone is explained in half a clause, which appears to contradict what section one taught the same student: that delocalisation 'lowers the electrophilicity of the carbonyl carbon' of a carboxylic acid. Nothing reconciles the two statements or explains that borane attacks a different atom for a different reason.

**Learner impact:** I hold one rule ('the acid carbonyl is less reactive than a ketone') and then meet a reagent that prefers the acid, with a reason I cannot connect to anything. I decide the rule I learned must be unreliable, which undermines my confidence in the whole reactivity ordering.

**Evidence:** Reader blk-r36wgen8 paragraph three, against blk-xvbwc1jm paragraph one; ch20-acid-reduction-reagent-v2 option c is a distractor turning on exactly this point.

**Recommended outcome (need):** A student needs the borane case stated so it does not appear to overturn the reactivity rule established earlier - the two claims are about different atoms and that has to be visible.

##### `stud-016` — LOW · conceptual-support · confidence 0.72

**Location:** question_slug=`ch20-inductive-distance-v2` · section_id=`nugget-substituent-effects-acidity` · anchor="Inductive withdrawal is a scalar effect on charge distribution"

**Observation:** Some wrong-answer feedback rebuts a distractor in vocabulary the chapter never uses: 'Inductive withdrawal is a scalar effect on charge distribution' and 'These three compounds are constitutional isomers'. Separately, ch20-acid-reduction-reagent-v2 offers 'H2 over Pd on carbon' as a distractor, and the chapter contains no discussion of catalytic hydrogenation at all.

**Learner impact:** The distractor I chose is the one that sounded chemically plausible to me, and the correction that arrives is more technical than the question was. I accept it without understanding it and I am no better prepared for the next variant.

**Evidence:** Compiled question set: ch20-inductive-distance-v2 wrong_answer_explanations option c; ch20-inductive-distance generic_incorrect_explanation; ch20-acid-reduction-reagent-v2 option d.

**Recommended outcome (need):** Corrective feedback needs to stay inside the vocabulary the chapter established, and distractors should be rejectable from chapter content wherever possible.

##### `stud-017` — LOW · cognitive-load · confidence 0.7

**Location:** section_id=`nugget-preparation-of-carboxylic-acids` · anchor="Four routes to a carboxylic acid, and which ones add a carbon"

**Observation:** The section is titled 'Four routes to a carboxylic acid' but the rendered expanded text never numbers them; it presents oxidation of primary alcohols, oxidation of aldehydes, side-chain oxidation of an alkylbenzene, Grignard carboxylation and nitrile hydrolysis, grouped as oxidative and chain-lengthening routes. Only the standard tier - which is not the tier that renders - states 'Four preparations cover most of what is needed'.

**Learner impact:** I try to build the list of four the title promised, count five named reactions, and cannot tell which two I am supposed to merge. I write down five and then second-guess my notes, or I drop one arbitrarily - most likely aldehyde oxidation, which is the one the questions do test indirectly.

**Evidence:** Reader section title versus blk-oh2h419s expanded text; the enumerating sentence exists only in the standard tier.

**Recommended outcome (need):** If the title promises a countable list, the rendered text needs to make the same count explicit and labelled.

**Open questions**

- Does the reader UI hide the '**Answer.**' half of each self-check callout behind a reveal at render time? The compiled markdown puts prompt and answer in one block, so if there is no reveal, stud-007 is worse than filed; if there is, that half falls away.
- Are the 42 bank questions surfaced to students through some other reader surface? If they are reachable from the chapter, stud-007's second half softens considerably.
- Is the terse/standard/expanded tier switcher exposed to students, and which tier does a first-time reader land on? stud-012 assumes expanded renders by default and that a student can drop to standard.
- Are the three deferred video briefs expected before publication? If they ship, stud-004 is substantially reduced; if the deferral is permanent, the electron-flow gap needs a non-video answer.
- No coined categories were used - all seventeen findings use ids listed in finding-schema.md.

#### Accessibility Persona — 7.6/10

This is a text-first chapter, and that is its main accessibility asset: every quantitative teaching point (pKa 4.76/2.86/0.23, boiling points, IR bands at 1710 and 2250 cm-1, delta 11-12 for the carboxyl proton, the 120/134 vs 127 pm bond-length argument) is stated in prose, not carried by a figure, and every one of the 42 questions is answerable from its prompt text alone. All four structure_scaffold items set typed_structure_entry to 'allowed', so the drawing questions have a keyboard/screen-reader input path with server read-back; every other workspace this chapter uses is built from labelled selects and buttons, and nothing is gated on drag, hover, colour or motion. No accessible_description leaks an answer and no level-1 hint hands one over. The real gaps are on the description side rather than the operability side: the 42 authored accessible_descriptions are carried in the activity envelope but never rendered or read aloud by the player, so they currently reach no learner; 18 of the 20 assets carry alt_text only, and the reader's images-off setting reduces a molecule figure to that one sentence while discarding the figure's teaching sentence; and the acetate-ion figure - the figure for the chapter's central resonance argument - is described as a localized one-double-one-single structure with no statement that the two C-O bonds are equivalent. None of these makes a required activity impossible, so I record no publication blocker, but the chapter's non-visual apparatus is doing less work than its authoring suggests.

**Publication blockers:** _none_

**Strengths**

- All four structure_scaffold items set typed_structure_entry to 'allowed', so both draw-the-product pairs have a typed SMILES path with server-side read-back instead of a pointer-only Ketcher canvas. This is the setting whose absence blocked ch5 and it is correct here on every item.
- Every question is answerable from text alone: prompts name the substrate and reagents in full, and every option, card, matrix case, matching item, ledger atom and arrow site is identified by a written label rather than by a picture or a position.
- Nothing in the chapter depends on colour, motion, hover or drag. The workspaces are labelled selects and buttons, and the bond-change ledger exposes its atom numbering as a text list rather than as numbers burned into an image.
- No accessible_description gives away an answer - each states the stimulus and the task, and several explicitly name the decision as the task - and no level-1 hint discloses the key; the ladders escalate from strategy to structure.
- The three unproduced videos carry no captionless or transcript-less media obligation today, and the reader honours a hidden flag where one is set.
- The chemistry that would most often be trapped in a figure - pKa values, boiling points, IR band positions and shapes, NMR shifts, the D2O exchange test, the 120/134 vs 127 pm bond lengths, the eight-membered cyclic dimer - is written out in prose, so a non-visual reading of this chapter loses very little.
- trouble_spots and practice_check both reach the reader as callout blocks in all 10 sections, and the roadmap teaching asset carries both alt_text and a full left-to-right long_description that the renderer surfaces as visible text.

**Findings**

##### `access-001` — HIGH · media-equivalence · confidence 0.93

**Location:** question_slug=`ch20-nitrile-sn2-arrow` · anchor="A curved-arrow editor shows cyanide ion and 1-bromobutane with selectable electron sources and targets."

**Observation:** All 42 questions carry an accessibility_bundle.accessible_description, and the compiled question set preserves it, but no player surface renders it. LmsPromptPanel prints only question.promptText; LmsActivityShell's readAloud speaks only promptText; the only two components in frontend/src that read accessibilityBundle.accessible_description are ReactionCoordinateQuestionRenderer and MolecularGeometryRenderer, neither of which is a question type this chapter uses.

**Learner impact:** A learner using a screen reader, or one whose accommodation is a text description of a rendered stimulus, gets the prompt and the raw workspace controls but never the authored orientation sentence that says what the stimulus is and what the task is. The harm is bounded here because every prompt is text-complete, but the chapter is shipping an accessibility layer no learner can hear.

**Evidence:** compiled/question-set.json: 42/42 questions have accessible_description. [internal source reference — not in this repo] renders {question.promptText} and prompt_stimulus assets only. [internal source reference — not in this repo] readAloud: new SpeechSynthesisUtterance(envelope.question.promptText).

**Recommended outcome (need):** The authored per-question description of the stimulus and task needs a delivery path to the learner in whatever surface serves these questions - it must be perceivable, or at minimum programmatically associated with the question region, rather than only present in the payload.

##### `access-002` — MEDIUM · alt-text-quality · confidence 0.88

**Location:** asset_id=`mol-acetate-ion` · nugget_id=`nugget-carboxylic-acid-acidity` · anchor="Acetate ion: a methyl group bonded to a carbon that carries one double-bonded oxygen and one singly bonded oxygen with a negative charge"

**Observation:** The acetate-ion figure is the figure for this section's whole argument, and its alt_text describes only the localized Lewis drawing: one C=O, one C-O with the charge. It never says the two carbon-oxygen bonds are equivalent, which is precisely the point the section makes and which its own trouble spot warns against. The asset carries no long_description.

**Learner impact:** A learner who reaches this figure through its text equivalent alone receives the exact misconception the section is trying to prevent, stated as fact. The corrective sentence exists only in the block's separate description line and in the body prose, so the figure's own description works against the chapter.

**Evidence:** asset mol-acetate-ion: accessibility has alt_text only, no long_description. Compiled block blk-zt2habe2 has alt_text but no long_description, while sibling blk-yrav3mkv (acetic acid) does carry one.

**Recommended outcome (need):** The carboxylate figure needs a text equivalent that states what the drawing cannot: that the two carbon-oxygen bonds are equivalent and the charge is shared, so the described version teaches the same thing the picture is meant to teach.

##### `access-003` — MEDIUM · media-equivalence · confidence 0.86

**Location:** asset_id=`mol-chloroacetic-acid` · nugget_id=`nugget-substituent-effects-acidity` · anchor="A single chlorine on the carbon next to the carboxyl group withdraws electron density inductively and lowers the pKa from 4.76 to 2.86."

**Observation:** When the reader's showImages preference is off, TopicPackageChapterRenderer.applyPrefs replaces each molecule block with a callout built from long_description || alt_text only - the block's description field (the figure's teaching sentence, which carries the pKa change, the boiling-point comparison and the reaction role) is dropped. Because 18 of the 20 assets have no long_description, an images-off learner receives a single structural sentence per figure and loses the sentence that says why the figure is there.

**Learner impact:** Learners who turn images off - a common low-vision, cognitive-load or bandwidth accommodation - lose the per-figure chemistry for 20 figures at once. The loss is partly cushioned because the body prose repeats the pKa and boiling-point values, but the figure-level link between a structure and its number disappears.

**Evidence:** [internal source reference — not in this repo] textEquivalentBlock: const body = (long || alt).trim() - content.description is never consulted. Affected blocks include blk-afvaek1e, blk-mh3r6xoj, blk-l4260mp3, blk-7twa0z4j, blk-43zuehvl, blk-2ar6zokp.

**Recommended outcome (need):** The images-off equivalent of a figure needs to preserve everything the figure block was teaching, not just its structural alt sentence.

##### `access-004` — MEDIUM · alt-text-quality · confidence 0.84

**Location:** nugget_id=`nugget-carboxylic-acid-dimers` · asset_id=`mol-butan-1-ol` · anchor="Butan-1-ol: an unbranched four-carbon chain with a hydroxyl group on the terminal carbon and no carbonyl group."

**Observation:** Several figures exist as members of a comparison, but each alt_text describes one isolated species and none of the comparison figures carries a long_description. The butanoic acid / butan-1-ol pair exists to contrast dimer formation and boiling point; the chloroacetic, trifluoroacetic, 4-nitrobenzoic and 4-methoxybenzoic set exists to show the direction and magnitude of substituent effects; sodium acetate exists to show the solubility switch. Only 2 of 20 assets have a long_description at all.

**Learner impact:** A learner who navigates by figure list - a normal screen-reader strategy - encounters six structurally-described but unrelated molecules and never learns from the figure channel that they form two comparison sets or which direction each comparison runs. The comparison survives only in the running prose.

**Evidence:** assets: only mol-acetic-acid and roadmap-nitrile-homologation have long_description; the seven comparison molecules have alt_text only.

**Recommended outcome (need):** Figures whose teaching point is a relationship between species need a text equivalent that states the relationship and its direction, not only a structural readout of the single molecule drawn.

##### `access-005` — LOW · alt-text-quality · confidence 0.82

**Location:** question_slug=`ch20-stronger-than-acetic` · anchor="Five compounds are listed by name with their structures."

**Observation:** Nine accessible_descriptions tell the learner that answer options are accompanied by structures, but no activity renderer in the codebase reads structure_smiles: a repo-wide search finds it only in the question-bank editor and type definitions, never in an option, card, matrix-case or matching-item renderer. The described structures are not drawn for anyone.

**Learner impact:** A screen-reader user is told a visual element exists beside each option and may spend effort trying to locate or request it. The chemistry itself is not lost, because every option also carries a compound name, but the description misdescribes the stimulus a learner is working with.

**Evidence:** Affected slugs: ch20-stronger-than-acetic(-v2), ch20-grignard-carboxylation(-v2), ch20-prep-reagent-match(-v2), ch20-nitrile-hydrolysis-product(-v2), ch20-borohydride-reduction-error(-v2). frontend/src grep for structure_smiles returns only types and editor files.

**Recommended outcome (need):** Each question's description of its own stimulus needs to match what the learner actually receives - either the option structures need to be rendered or the descriptions need to stop asserting them.

##### `access-006` — LOW · alt-text-quality · confidence 0.79

**Location:** question_slug=`ch20-nitrile-sn2-arrow-v2` · anchor="Cyanide ion converts iodoethane to propanenitrile in a single SN2 step."

**Observation:** Where the curved-arrow workspace renders its reference structure, the image alt is the fixed string 'Reaction system for this arrow question' and the arrow overlay is aria-hidden; the error-repair workspace's structure is likewise 'Structure for the flawed step'. The per-site labels the question authors are good and do carry atom identity into the controls, so the interaction is usable - but the figure itself is announced by a name-only alt.

**Learner impact:** A learner working non-visually can operate the arrow builder from the labelled sites but gets no description of the reaction system as drawn; they must reconstruct it from the prompt sentence. By contrast the bond-change ledger does this well - its reference image takes reaction_display as alt, which is a real description.

**Evidence:** [internal source reference — not in this repo] alt='Reaction system for this arrow question'; [internal source reference — not in this repo] alt='Structure for the flawed step'; contrast [internal source reference — not in this repo] alt={reactionDisplay}.

**Recommended outcome (need):** A rendered stimulus inside a question workspace needs an announced description of what it shows, on the same footing as the ledger's reaction_display, without disclosing which site is the answer.

##### `access-007` — LOW · retrieval-practice · confidence 0.8

**Location:** nugget_id=`nugget-substituent-effects-acidity` · anchor="**Try it.** Rank 4-chlorobenzoic acid, benzoic acid, and 4-methylbenzoic acid in order of decreasing acidity"

**Observation:** Every section's practice_check is authored with separate prompt and answer fields, but the compiler flattens both into a single callout markdown string with no disclosure control, and the reader renders it as one continuous block.

**Learner impact:** A learner reading linearly by screen reader or text-to-speech hears the answer in the same breath as the question and has no way to attempt first; a sighted reader can at least stop their eyes at the bold 'Answer.' A retrieval-practice opportunity that exists for one reading mode does not exist for the other. This affects all 10 sections.

**Evidence:** nugget practice_check: {prompt, answer}. Compiled callouts blk-cincpmj5 and its nine siblings each contain both '**Try it.**' and '**Answer.**' in one markdown string.

**Recommended outcome (need):** The authored separation between a practice prompt and its answer needs to survive into the reader as something a learner can defer in any reading mode, not only by choosing not to look.

##### `access-008` — LOW · keyboard-operability · confidence 0.85

**Location:** section_id=`nugget-carboxylic-acid-structure-naming` · anchor="The carboxyl group and the names of carboxylic acids"

**Observation:** The chapter renders as h1 (chapter title) then h2 (section title) then h4 for every callout heading and every molecule card title; there is no h3 anywhere. The heading level jumps two steps at each figure and each callout.

**Learner impact:** Screen-reader users navigating by heading level, and users of heading-outline tools, see a broken outline in which figures and callouts appear nested two levels below their section with nothing in between; relative depth becomes uninformative for the whole chapter.

**Evidence:** [internal source reference — not in this repo]: Heading as='h1' (chapter), as='h2' (section). [internal source reference — not in this repo]: callout Heading as='h4' and StructureCard Heading as='h4'.

**Recommended outcome (need):** The chapter's heading outline needs to descend one level at a time so heading-based navigation reflects the actual structure of sections, figures and callouts.

**Open questions**

- The curved-arrow and error-repair configs contain molecule_smiles but no rendered molecule object; the renderers only draw a figure when one is supplied at runtime. If that enrichment does not run, the fully-labelled select-based fallback is what learners get and access-006 would not apply.
- The three video briefs are deferred. If they are produced later, each will need captions and a narration that describes the visual changes - the storyboard sentences currently compiled into the block description are single storyboard beats, not descriptions of the finished clip.
- I checked the reader and the LTI activity shell for delivery of accessible_description. I did not inspect the LMS export or any PDF/print path, so access-001 may or may not hold on those surfaces.
- ch20-nitrile-sn2-arrow offers only one lone-pair site while its v2 twin offers two; a learner enumerating the labelled sites can infer the source without reasoning. This is a distractor-design question rather than an access barrier, and I leave it to the instructor persona.
- This chapter is unseeded, so I reviewed the compiled artifacts rather than a live rendering; my judgements about what a learner receives are inferred from the renderers those artifacts feed.

#### Learner with Visual Preference — 6.0/10

The prose is unusually well organized and almost every molecule figure carries a caption naming a specific teaching point rather than just labelling the structure, so the figures that exist mostly earn their place. The problem is what the figure set can and cannot depict. Nineteen of the twenty authored assets are single-molecule RDKit structures, and a single-molecule depiction is structurally incapable of showing the three ideas this chapter is built on: the cyclic two-hydrogen-bond dimer, the delocalized carboxylate, and the shape of an infrared band. All three reach the student as prose only. In the acidity section the situation is worse than a gap - the one figure offered for delocalization (mol-acetate-ion, CC(=O)[O-]) renders as one C=O and one C-O minus, which is precisely the drawing the adjacent 'Watch out' callout tells students not to make, and its own alt text describes the non-equivalent bonds verbatim. Three reader video blocks ship with url set to the empty string and with a producer's storyboard direction as the student-facing description. On the named hazards this chapter is clean: it authors no reaction_coordinate asset, so the BARRIER_HEIGHTS coercion bug cannot fire here (the live high/low instances are in the sibling carboxylic-acid-derivatives and epoxides packages); its one synthesis_roadmap matches the {nodes, steps} contract exactly with three nodes, two steps, no edges list and a strictly linear route; no asset sets annotation_font_scale; and every selected-response item is all-or-none on option structures, so there is no picture-presence answer tell. All twenty assets do compile.

**Publication blockers:** _none_

**Strengths**

- All twenty authored assets compile into reader blocks - nothing is silently dropped by _ASSET_TYPE_TO_BLOCK. The synthesis_roadmap is promoted from 'image' to a live 'teaching_asset' block by _renders_live because it carries spec.nodes, so it renders through TeachingAssetLiveRenderer instead of shipping as an empty image.
- roadmap-nitrile-homologation conforms exactly to the renderer contract: three nodes, two steps that join nodes[i] to nodes[i+1], no authored edges list, and a genuinely linear route - so the strictly-linear-renderer hazard cannot bite here. Its target node is flagged is_target and the arrow captions carry both reagents and the teaching note.
- The chapter authors no reaction_coordinate, conformational_energy_profile or acid_base_energy_diagram asset, so the BARRIER_HEIGHTS coercion bug has no instance in this package - checked the whole package and the compiled artifacts, zero matches for 'barrier'. The live high/low instances are in the sibling carboxylic-acid-derivatives package and in epoxides, not here.
- No asset sets rdkit_options.annotation_font_scale at all, so no figure risks putting labels on top of the structure.
- Every selected-response and multi-select item is all-or-none on option structures - 5 of 5, 4 of 4, 4 of 4 - so the presence of a picture is never an answer tell. ch20-acidity-rank likewise uses condensed formulas uniformly across all four cards.
- Molecule captions are teaching statements rather than labels: 'The nitrile carbon is C1 of the chain, so a four-carbon halide gives a five-carbon nitrile - the point at which the extra carbon enters the skeleton' does real work a bare name would not.
- show_hydrogens is applied selectively and correctly - on acetic acid, acetate, chloroacetic acid and acetonitrile, exactly the figures where the acidic hydrogen or the substituted alpha carbon is the point - rather than globally, which would have cluttered the aromatic figures.
- Alt text is present on every molecule figure and is specific about connectivity; mol-acetic-acid and the roadmap additionally carry a long_description, and the roadmap's narrates the route left to right with both arrow labels.
- The curved_arrow item indexes its hotspots correctly against input-SMILES order, so the visual targets a student clicks match the labels they read.

**Findings**

##### `visual-001` — HIGH · figure-accuracy · confidence 0.95

**Location:** section_id=`nugget-carboxylic-acid-acidity` · concept_slug=`carboxylic-acid-acidity` · asset_id=`mol-acetate-ion` · anchor="Drawing a carboxylate with one C=O and one C–O⁻ and treating those bonds as different; the two carbon–oxygen bonds are equivalent."

**Observation:** The acidity section's misconception callout warns students not to draw a carboxylate with one C=O and one C-O minus, and the figure placed immediately after that callout does exactly that. mol-acetate-ion is authored as SMILES CC(=O)[O-], which RDKit renders as one localized double bond and one localized single bond to a charged oxygen. Its own alt text restates the non-equivalence. The block's description asserts the opposite, so caption and picture disagree. No figure anywhere shows the two resonance contributors, the delocalized hybrid, or the bond-length evidence, even though the section's third learning objective is to use bond-length evidence to argue the two bonds are equivalent.

**Learner impact:** A student who reads figures before prose - or who skims and remembers the picture - leaves the chapter's most important section holding exactly the mental image the chapter twice tells them is wrong. The chapter then relies on that image being correct in three downstream sections, and ch20-draw-carboxylate asks the student to draw the very species the figure misrepresents.

**Evidence:** Asset mol-acetate-ion, smiles CC(=O)[O-]; alt_text 'one double-bonded oxygen and one singly bonded oxygen with a negative charge'; description 'resonance makes the two carbon-oxygen bonds equivalent'; adjacent callout block blk-4jkx8xxr tone 'warning'. Nugget prose cites 127 pm versus 120/134 pm. No asset in the package has a type or spec capable of showing delocalization.

**Recommended outcome (need):** The equivalence of the two carbon-oxygen bonds - and the bond-length evidence for it - needs to reach the student through the visual channel rather than being asserted in a caption while the only picture shows the opposite. At minimum the acetate figure must stop contradicting the callout it sits beside.

##### `visual-002` — HIGH · visual-opportunity · confidence 0.95

**Location:** section_id=`nugget-carboxylic-acid-dimers` · concept_slug=`carboxylic-acid-physical-properties` · asset_id=`mol-butanoic-acid` · anchor="closing an eight-membered ring held by two hydrogen bonds"

**Observation:** The section's first learning objective is to explain why carboxylic acids form cyclic hydrogen-bonded dimers, and the prose describes a specific geometric arrangement: two molecules pairing head to head, each O-H directed at the other's carbonyl oxygen, closing an eight-membered ring. The two figures attached are single isolated molecules whose alt texts describe one molecule each. Nothing in the chapter depicts two molecules, a hydrogen bond, or the eight-membered ring. A single-molecule SMILES asset cannot express an intermolecular contact, so this is not a caption fix.

**Learner impact:** The entire boiling-point argument is a claim about a two-molecule object, and the student is shown only one-molecule objects. Learners are then asked in ch20-acid-alcohol-hbond-matrix to reason about donor and acceptor counts and in the practice check to explain why a discrete dimer differs from an alcohol's extended network - a spatial comparison they have never seen.

**Evidence:** Nugget expanded text: 'a cyclic dimer in which the O-H of each molecule is directed at the carbonyl oxygen of the other, closing an eight-membered ring held by two hydrogen bonds'. Reader blocks blk-2ar6zokp and blk-omel5kf8 are both single-molecule. The package contains no dimer, diagram or clipart asset.

**Recommended outcome (need):** The paired, ring-closed geometry of the dimer - and how it differs from an alcohol's extended network - needs a channel other than prose, because the section's central claim and its assessment both depend on a two-molecule spatial arrangement no current asset type in this chapter can express.

##### `visual-003` — HIGH · figure-purpose · confidence 0.93

**Location:** section_id=`nugget-carboxylic-acid-acidity` · nugget_id=`nugget-preparation-of-carboxylic-acids` · asset_id=`video-carboxylate-delocalization` · anchor="Open on acetic acid with the acidic hydroxyl hydrogen highlighted and the C=O and C–O bond lengths labelled 120 pm and 134 pm."

**Observation:** Three video blocks carry url set to the empty string, because all three briefs are production_status 'deferred'. ReaderBlockRenderer's video case has no empty-url guard: it renders a bordered card with a 'Video - ChemIllusion' badge, the title, the description, and a 'Watch' RouterLink whose target is the empty string, which re-navigates to the current page. Worse, the description compiled into each card is storyboard frame 1 verbatim - a producer's camera direction, not a sentence written for a student. The three deferred videos cover carboxylate delocalization, chain-extension homologation and nitrile hydrolysis - the three most motion-dependent ideas in the chapter.

**Learner impact:** A learner who follows figures first is offered three animations, clicks three times, and gets nothing - the page appears broken rather than incomplete. The card copy compounds this: a student reading 'Open on pentanenitrile with the C-N polarization marked' has no way to tell this is a note to a video producer.

**Evidence:** Reader blocks blk-fa6z5rhw, blk-0ljj3bkv, blk-jc0mqivv with url ''. Package video_briefs all carry production_status 'deferred'. [internal source reference — not in this repo] case 'video' renders a RouterLink to c.url with no url check.

**Recommended outcome (need):** A deferred video must not reach the reader as a clickable card that leads nowhere with producer copy as its description. Either the promised content is delivered in some form the reader can show, or the block does not ship - and in either case the student-facing text must be written for a student.

##### `visual-004` — HIGH · visual-opportunity · confidence 0.9

**Location:** section_id=`nugget-spectroscopy-acids-nitriles` · concept_slug=`spectroscopy-of-carboxylic-acids-and-nitriles` · question_slug=`ch20-ir-triple-bond-region` · anchor="The infrared spectrum of a carboxylic acid is one of the most distinctive in organic chemistry."

**Observation:** The spectroscopy section's two figures are ordinary structure drawings. There is no spectrum anywhere in the chapter, yet every claim in the section is about the shape, width and relative intensity of a band: an O-H stretch broadened from 2500 to 3300 cm-1 that swamps the aliphatic C-H stretches, a strong C=O near 1710 beneath it, a sharp medium nitrile band near 2250, and a weak alkyne band in the same region. The two assessment items make this concrete: one hands the student a verbal description of a spectrum and asks for the conclusion, the other asks for a number.

**Learner impact:** Broad-versus-sharp and strong-versus-weak are properties a learner reads off a trace in a second and must otherwise hold as verbal labels. Because the questions describe the spectrum in words too, the assessed skill silently changes from reading a spectrum to recalling adjectives, and a student who can answer both items may still not recognize a carboxylic acid spectrum on sight.

**Evidence:** Section contains only molecule blocks for mol-propanoic-acid and mol-benzonitrile. Objectives include 'Distinguish a nitrile absorption from an alkyne absorption in the triple-bond region.' ch20-ir-triple-bond-region student_config is four text-only options.

**Recommended outcome (need):** The band-shape discriminations this section teaches and assesses need to be seen at least once before a student is asked to make them, rather than being carried entirely by adjectives in prose and restated as adjectives in the question stem.

##### `visual-005` — MEDIUM · figure-purpose · confidence 0.88

**Location:** question_slug=`ch20-stronger-than-acetic` · concept_slug=`substituent-effects-on-acidity` · anchor="Select every compound that is a stronger acid than acetic acid (pKa 4.76)."

**Observation:** Six questions (twelve with their v2 twins) author a structure on every answer option or case. None of them render. SelectedResponseRenderer reads only option.imageUrl and option.text, and the SelectedResponseOption type is {id, text, imageUrl?} - structure_smiles appears nowhere in the frontend render path. buildDemoEnvelope passes responseConfig through untouched, and nothing maps structure_smiles to imageUrl, so the field is carried all the way to the renderer and then ignored.

**Learner impact:** Items deliberately authored as structure-recognition exercises degrade into name-recognition exercises. A student answering ch20-nitrile-hydrolysis-product chooses between the words 'Pentanoic acid', 'Pentan-1-amine' and 'Butanoic acid' - which tests whether they can map a name to a product, not whether they can see that the nitrile carbon became the carboxyl carbon. The authored structures also encode the chapter's carbon-counting point that names alone obscure.

**Evidence:** compiled/question-set.json: ch20-stronger-than-acetic options a-e each carry structure_smiles. [internal source reference — not in this repo] SelectedResponseOption {id, text, imageUrl?}. [internal source reference — not in this repo] renders {option.imageUrl && ...} then {option.text}.

**Recommended outcome (need):** Structures the chapter deliberately attached to answer options need to reach the student, or the authoring effort should stop being spent on a field the delivery path discards. This is a platform-level gap that silently reverses the intent of six of this chapter's twenty-one distinct items.

##### `visual-006` — MEDIUM · visual-opportunity · confidence 0.85

**Location:** section_id=`nugget-preparation-of-carboxylic-acids` · concept_slug=`preparation-of-carboxylic-acids` · asset_id=`roadmap-nitrile-homologation` · anchor="Four routes to a carboxylic acid, and which ones add a carbon"

**Observation:** The section title states the organizing idea - four routes, sorted by whether they add a carbon - and the roadmap maps exactly one of them. The other three routes are illustrated only by disconnected single-molecule cards: toluene and benzoic acid appear as two separate figures with no arrow or reagent label between them, and primary-alcohol/aldehyde oxidation and Grignard carboxylation have no figures at all. Carboxylation is the weaker case: it is a stated objective, it has its own question, and neither the organomagnesium reagent nor CO2 nor the magnesium carboxylate intermediate appears anywhere.

**Learner impact:** The one thing a student must retain is a sortable map: given a target, which route reaches it and does the carbon count change. That is a classification structure, delivered as a paragraph plus one route drawn in full and three drawn not at all. The asymmetry also implies the nitrile route is the important one, when the prose is explicit that carboxylation and cyanide displacement are interchangeable.

**Evidence:** Section blocks: molecule mol-toluene, molecule mol-benzoic-acid, molecule mol-pentanoic-acid, teaching_asset roadmap-nitrile-homologation. No asset for a Grignard reagent, CO2, a primary alcohol or an aldehyde.

**Recommended outcome (need):** The four-route classification, and specifically the carbon-preserving versus carbon-adding split that names the section, needs to be visible as a structure rather than inferred from a paragraph - and the carboxylation route, which is assessed, should not be the only route with no depiction at all.

##### `visual-007` — MEDIUM · visual-opportunity · confidence 0.85

**Location:** section_id=`nugget-substituent-effects-acidity` · concept_slug=`substituent-effects-on-acidity` · question_slug=`ch20-inductive-distance` · anchor="In the chlorobutanoic acid series the pKa rises from 2.86 for the 2-chloro isomer to 4.05 for the 3-chloro and 4.52 for the 4-chloro compound"

**Observation:** This section carries three separate ordered comparisons in prose - the chloroacetic accumulation series, the chlorobutanoic distance series, and the substituted benzoic series - and presents four unrelated single-molecule cards stacked vertically. Two problems follow. First, the reference compounds every caption quotes against are absent from the section: chloroacetic acid's caption says 'lowers the pKa from 4.76 to 2.86' and the nitrobenzoic caption says 'from 4.19 to 3.44', but neither acetic acid nor benzoic acid has a figure here. Second, the distance series has no figure at all, although explaining inductive fall-off with distance is an explicit objective.

**Learner impact:** Ranking and distance-attenuation are both relational claims: their content is the ordering and the size of the gaps, not any individual structure. Four vertically stacked cards each showing one molecule with a number in its caption gives a learner no way to see the ordering, and no way at all to see three chlorine positions moving away from a carboxyl group.

**Evidence:** Section blocks are molecule cards for mol-chloroacetic-acid, mol-trifluoroacetic-acid, mol-4-nitrobenzoic-acid, mol-4-methoxybenzoic-acid only. Package assets contain no 2-, 3- or 4-chlorobutanoic acid. ch20-inductive-distance names all three isomers in the stem with no structures.

**Recommended outcome (need):** The pKa ordering and the fall-off with distance need to be perceivable as a relationship - including the acetic and benzoic acid reference points the captions measure against - rather than reconstructed from numbers scattered across four independent figure captions.

##### `visual-008` — MEDIUM · figure-purpose · confidence 0.87

**Location:** section_id=`nugget-reactions-of-carboxylic-acids` · concept_slug=`reactions-of-carboxylic-acids` · asset_id=`mol-butanoic-acid` · anchor="Benzoic acid is the reference compound for ring-substituent effects on acidity and the product of side-chain oxidation"

**Observation:** Eight of the twenty-seven molecule blocks are repeat placements of seven assets, and because the compiler emits asset.learning_goal as the caption for every placement, a reused figure carries the caption written for whichever section it was authored in. Two placements are actively off-topic. In the reactions section - about acyl substitution, hydride reduction and alpha-substitution - butanoic acid is captioned entirely about boiling at 164 degrees and dimer vaporization. In the extraction section, benzoic acid is captioned about ring-substituent effects and side-chain oxidation, neither of which that section discusses. Separately, none of the three reaction families named in the reactions section has a product structure: no acid chloride, no ester or amide, no alpha-bromo acid figure anywhere.

**Learner impact:** A caption is the first thing a figure-oriented learner reads, and here it points away from the section. A student scanning figures in the reactions section sees two pictures about boiling points where they expect the products of SOCl2, LiAlH4 and Br2/PBr3 - and finds those three products depicted nowhere.

**Evidence:** Reader blocks blk-awrmz64h and blk-jjggvrkj carry descriptions about boiling points and hydrogen-bond donors. [internal source reference — not in this repo] sets molecule content description from asset.get('learning_goal'), one value per asset regardless of placement.

**Recommended outcome (need):** A figure reused in a second section needs a caption saying what it is doing there, and the reactions section needs its own reaction products to be visible rather than represented by two carried-over physical-property figures.

##### `visual-009` — MEDIUM · visual-opportunity · confidence 0.86

**Location:** section_id=`nugget-reactions-of-nitriles` · concept_slug=`reactions-of-nitriles` · anchor="Diisobutylaluminium hydride is bulky enough to add only once, and the imine anion it produces survives until workup"

**Observation:** This section is a divergence: one nitrile plus four reagent choices gives four different products at three oxidation levels. The reader presents it as four unlinked molecule cards - pentanenitrile, pentanoic acid, butan-1-amine, acetophenone - with no reagents, no arrows, and no indication that they are alternatives from a common starting point rather than a sequence. The coverage is also uneven: three of the four outcomes have a structure, but the DIBAH aldehyde product does not, even though distinguishing LiAlH4 from DIBAH is one of the section's three objectives.

**Learner impact:** The reagent-to-product mapping is the whole content of the section, and a mapping shown as a list of unconnected products has to be reassembled from prose. The missing aldehyde is the sharper problem: a learner comparing figures sees an acid, an amine and a ketone, and can reasonably conclude the aldehyde outcome is minor or does not produce an isolable compound - the opposite of what the objective asks them to distinguish.

**Evidence:** Reader section contains molecule blocks for mol-pentanenitrile, mol-pentanoic-acid, mol-butan-1-amine and mol-acetophenone; the package contains no aldehyde asset.

**Recommended outcome (need):** The one-substrate-many-reagents branching of nitrile chemistry needs to be visible as a branching, and the DIBAH aldehyde outcome needs the same visual standing as the three sibling outcomes that do have structures.

##### `visual-010` — MEDIUM · visual-opportunity · confidence 0.82

**Location:** section_id=`nugget-nitrile-structure-and-preparation` · concept_slug=`nitrile-structure-naming-and-preparation` · asset_id=`mol-acetonitrile` · anchor="bonded to nitrogen by one σ bond and two mutually perpendicular π bonds"

**Observation:** The nitrile section makes four spatial or electronic claims - an sp carbon, two mutually perpendicular pi bonds, a lone pair in the remaining sp orbital on nitrogen, and strong polarization toward nitrogen - and offers three flat skeletal structures. A 2D depiction does convey the collinear C-C-N arrangement, so linearity is served; the perpendicular pi system, the sp lone pair and the charge polarization are not. The polarization matters most, because the next section's opening argument is that the nitrile carbon is electrophilic 'for the same reason' as a carbonyl carbon, and the deferred video's first storyboard frame is literally 'Open on pentanenitrile with the C-N polarization marked'.

**Learner impact:** Every reaction in the following section is justified by where the electrons sit in the C-N unit. A student who has only seen a line-and-three-bars drawing has to take the electrophilicity of that carbon on faith, and ch20-nitrile-sn2-arrow then asks them to distinguish the cyanide carbon lone pair from the nitrogen lone pair as an arrow source - with no orbital ever shown.

**Evidence:** Nugget expanded text on sp hybridization and perpendicular pi bonds; assets mol-acetonitrile, mol-benzonitrile, mol-pentanenitrile are plain molecule blocks; video-nitrile-hydrolysis storyboard[0] names the polarization display and is deferred.

**Recommended outcome (need):** Where the electron density sits in the C-N unit, and which lone pair is which, needs to be visible before the chapter builds three reactions and a curved-arrow item on top of it.

##### `visual-011` — MEDIUM · visual-opportunity · confidence 0.8

**Location:** section_id=`nugget-carboxylate-salts-and-extraction` · concept_slug=`carboxylic-acid-acidity` · anchor="the acid is converted to its carboxylate and partitions into the aqueous layer, while the neutral compound remains in the ether"

**Observation:** An objective of this section is to describe how an acid-base extraction separates a carboxylic acid from a neutral organic compound, and the process described is explicitly spatial and sequential: two liquid layers, a compound moving from one to the other on deprotonation, the layers separated, then acidification moving it back. The section's two figures are a sodium acetate ion pair and a benzoic acid structure. Neither shows layers, direction, or the reversibility that is the point.

**Learner impact:** Extraction is one of the few genuinely procedural, physically located ideas in the chapter - where a molecule is, at which step. Rendering it as prose plus two static structures leaves the learner tracking a location through a paragraph, which is precisely the load a spatial arrangement removes. The micelle description that closes the section has the same character and the same absence of any depiction.

**Evidence:** Reader section contains molecule blocks for mol-sodium-acetate and mol-benzoic-acid only; the nugget prose walks the shake-separate-acidify sequence entirely in words.

**Recommended outcome (need):** The where-is-the-compound-now sequence of an acid-base extraction, and the reversibility of the solubility switch that drives it, need a representation that carries location and order.

**Open questions**

- Should the compiler emit a reader 'video' block at all when the brief's production_status is 'deferred' and url is empty? Three chapters' worth of this pattern would be fixed by one guard in ReaderBlockRenderer or one skip in the builder - is that a chapter-level fix or a platform ticket?
- When a video brief is deferred, is compiling storyboard[0] as the student-facing description intentional? It reads as a camera direction rather than as a description of content.
- Is the reader's .questions.json manifest (student_config null for every item, 21 of 42 questions) the surface students actually answer on, or do they always route through the registered/LTI panel that receives the full compiled config? visual-005 assumes the latter; if the former, the option structures are dropped twice over.
- Is a figure caption expected to be per-placement or per-asset? The builder emits asset.learning_goal for every placement, which is what produces the off-topic captions in visual-008.
- No new category ids were coined. visual-003 and visual-005 sit between figure-purpose and media-equivalence - I filed both as figure-purpose to stay in this persona's lane, and both may deduplicate against the Accessibility persona.

### Orchestrator decisions

#### `rec-001` — Section 1 attributes acidity to a weakened O–H bond (blocker)

- **Need:** The carboxyl delocalization must be described for what it actually does, and the acidity claim must be framed by conjugate-base stability so sections 1 and 3 tell one story.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** One sentence, and the correct account already exists two sections later — section 3 says outright 'The O–H bonds involved are similar in strength, so the difference cannot be a bond-strength effect'. The fix is to stop section 1 contradicting section 3 and the chapter's own trouble spot, not to author anything new.
- **Consolidates:** `instr-001`

#### `rec-002` — A multi-select key contradicts the chapter's own pKa table (blocker)

- **Need:** The option set's acidity relative to acetic acid must be unambiguous, and the key and distractor rationale must both use the reference compound the prompt names.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** 4-Methoxybenzoic acid at pKa 4.47 IS stronger than acetic acid at 4.76; the item marks it wrong and its explanation silently switches the comparison to benzoic acid. Replacing that option with a compound that is genuinely weaker than acetic acid fixes the chemistry while preserving the item's 3-correct/2-incorrect discrimination — simply adding it to the key would leave a 4-of-5 multi-select with almost nothing to discriminate.
- **Consolidates:** `instr-002`

#### `rec-003` — The practice check says SN2 on neopentyl bromide is straightforward (blocker)

- **Need:** The practice check must resolve to the route that actually works for this substrate and say why the SN2 route fails.
- **Chosen intervention:** `prose-edit` → target surface `practice`
- **Why this is the least-complex option that fully addresses the need:** Neopentyl bromide is the textbook counterexample to 'primary halides do SN2' — the adjacent quaternary carbon blocks backside attack and the rate is ~10⁻⁵ that of ethyl bromide. The substrate was almost certainly chosen to teach that, and the answer inverts the lesson. Correcting the answer and adding the β-branching caveat to the surrounding prose is bounded and leaves the well-chosen substrate in place.
- **Consolidates:** `instr-003`

#### `rec-004` — The nitrile-IR feedback separates two overlapping regions (blocker)

- **Need:** The feedback needs the discriminator the chapter actually teaches — overlapping positions distinguished by band intensity and by the ≡C–H stretch — not a claim that the regions differ in wavenumber.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** The chapter's own section 10 puts alkynes at 2100–2260 cm⁻¹, so 2250 is inside that window, not above it. A student applying the feedback's rule will misassign an internal alkyne at 2230 as a nitrile — exactly the scenario of the sibling item ch20-ir-triple-bond-region. Two strings.
- **Consolidates:** `instr-004`

#### `rec-005` — The only carboxylate figure teaches the misconception the callout warns against (high)

- **Need:** The equivalence of the two carbon–oxygen bonds, and the bond-length evidence for it, must reach the student rather than being asserted in a caption while the adjacent picture shows the opposite.
- **Chosen intervention:** `longer-description` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** Reached independently by three personas. A single-molecule SMILES asset cannot draw a delocalized hybrid, so the full fix is a new figure — but the immediate defect is that the figure's own alt text restates the non-equivalence, making the described version teach the error too. Correcting the description stops the figure contradicting the callout now; the hybrid figure is carried as a visual opportunity.
- **Consolidates:** `instr-006`, `visual-001`, `access-002`

#### `rec-006` — Three deferred videos ship as clickable cards that lead nowhere (high)

- **Need:** A deferred video must not reach the reader as an empty player with a producer's camera direction as its student-facing description.
- **Chosen intervention:** `prose-edit` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** All three briefs are production_status 'deferred' with notes asserting the prose carries the content, but the deferral does not suppress the block — the reader renders a 'Watch →' link to an empty string. Marking them hidden, as ch13's deferred brief now is, removes three dead links with no content change.
- **Consolidates:** `instr-007`, `visual-003`, `stud-004`

#### `rec-007` — pKa is used 49 times and never defined (high)

- **Need:** Before the first numerical comparison, a student needs to be told what a pKa number is, that the scale is logarithmic, and that smaller means stronger — in the default reading path.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The chapter asks the reader to compare 4.76, 3.75, 16 and 10 in the acidity section's second sentence, and the only statement of the scale's direction sits in a warning callout three sections later. That two of the graded items put the direction rule in hint level 1 is evidence the authors already knew it was the failure point.
- **Consolidates:** `stud-001`

#### `rec-008` — 'Oxidation level' carries nine questions' feedback and is never explained (high)

- **Need:** The chapter needs a usable account of what oxidation level means for a carbon and how to compare two carbons, before the preparations and reactions sections.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The phrase appears 16 times across 9 questions' graded feedback — including distractor rebuttals that consist of nothing else — and exactly once in the rendered chapter text, undefined. Remedial feedback written in vocabulary the chapter never taught cannot remediate.
- **Consolidates:** `stud-002`

#### `rec-009` — The extraction section inherits the acidity section's warnings verbatim (high)

- **Need:** The extraction section needs its own named wrong moves — forgetting to re-acidify, losing track of which layer holds what, treating hydroxide and bicarbonate as interchangeable.
- **Chosen intervention:** `instructor-note` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The nugget's section_id is carboxylic-acid-acidity, so it renders that concept's trouble_spots — the callout is character-identical to the previous section's and none of its three warnings concerns extraction. Authoring extraction-specific trouble spots is bounded and fills a slot that is currently spent on a duplicate.
- **Consolidates:** `stud-005`

#### `rec-010` — The cyclic dimer, the central claim of the physical-properties section, is drawn nowhere (high)

- **Need:** The two-molecule pairing and its two hydrogen bonds need to be visible and contrastable with an extended alcohol network.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** A single-molecule SMILES asset is structurally incapable of expressing an intermolecular contact, so this is not a caption fix. The boiling-point argument, the vapour-density argument, the broad 2500–3300 cm⁻¹ band and the ch20-acid-alcohol-hbond-matrix item all rest on a two-molecule object the student never sees. Deferred as authoring scope.
- **Consolidates:** `instr-005`, `visual-002`

#### `rec-011` — No spectrum anywhere in a chapter whose spectroscopy section is about band shape (high)

- **Need:** The broad-O–H-over-1710 signature and the sharp-nitrile-versus-weak-alkyne discrimination need to be seen once before a student is asked to make them.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** Both spectroscopy items describe the spectrum in words too, so the assessed skill has silently changed from reading a spectrum to recalling adjectives — a student can pass both and still not recognize a carboxylic acid spectrum on sight, which is what the objective claims to teach. Deferred as authoring scope.
- **Consolidates:** `instr-011`, `visual-004`

#### `rec-012` — The chapter grades electron flow it never draws (high)

- **Need:** The nitrile addition step, the imine anion, and the SN2 electron flow need to exist as something a student can look at before two curved_arrow and two bond_change_ledger items grade them.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** Nineteen of twenty assets are single molecules and there is no arrow, no intermediate, and no charged species other than acetate anywhere. The chapter's own organizing claim for nitriles — that every reaction opens with addition to the sp carbon — is also assessed by nothing. Deferred as authoring scope; it pairs with rec-017.
- **Consolidates:** `stud-004`, `visual-009`, `visual-010`, `instr-010`

#### `rec-013` — Reused figures carry the caption written for their first section (medium)

- **Need:** A figure reused in a second section needs a caption that says what it is doing there.
- **Chosen intervention:** `prose-edit` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** The compiler emits asset.learning_goal as the caption for every placement, one value per asset, so butanoic acid is captioned about boiling points inside the reactions section and benzoic acid about ring-substituent effects inside the extraction section — both forward-referencing topics the reader has not met. Splitting the caption per placement is a compiler question; rewording the two worst offenders to be section-neutral is available now.
- **Consolidates:** `stud-011`, `visual-008`

#### `rec-014` — The solubility threshold is stated three different ways (medium)

- **Need:** One threshold, consistent across the trouble spot and all three text tiers.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The trouble spot says four carbons, the standard tier says six, and the expanded tier's worked list (formic through butanoic miscible, pentanoic partly soluble) matches four. Six is the loose figure — hexanoic acid is already only sparingly soluble — so the tiers should converge on the expanded tier's own data.
- **Consolidates:** `instr-013`

#### `rec-015` — The numeric tolerance swallows the distinction the item tests (medium)

- **Need:** The accepted band must exclude the conjugated value the prompt explicitly rules out.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** Both items use ±20 cm⁻¹, which is exactly the conjugation shift the chapter teaches, so a prompt saying 'saturated, unconjugated' accepts 1690 (the conjugated value) and the nitrile prompt accepts 2230. The item cannot detect the misconception it targets, and its own feedback then explains a distinction the grader just ignored.
- **Consolidates:** `instr-014`

#### `rec-016` — Sequencing: nitrile chemistry is taught in full two concepts before nitriles are introduced (medium)

- **Need:** The nitrile material concept 5 depends on must be declared as a prerequisite, or section 5 must forward-reference rather than teach it.
- **Chosen intervention:** `instructor-note` → target surface `instructor-support`
- **Why this is the least-complex option that fully addresses the need:** Concept 5 teaches cyanide SN2, the nitrile intermediate, hydrolysis and the substrate limits, while the nitrile concepts sit at order 7 and 8 and concept 5's prerequisites name only concept 1. The prerequisite graph tells every downstream tool that section 5 is safe to serve first, which it is not. Declaring the dependency is a two-line data fix that makes the gating honest.
- **Consolidates:** `instr-008`

#### `rec-017` — Objectives assessed by nothing (medium)

- **Need:** Acid–base extraction, amide dehydration, nitrile nomenclature and the nitrile addition step each need at least one graded item, or the objective list overstates what the chapter holds students to.
- **Chosen intervention:** `added-practice` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** Extraction is the one lab-transferable skill in the chapter and is taught but never practised; amide dehydration is presented as the route that escapes the SN2 substrate limits and appears in zero items. Deferred as authoring scope.
- **Consolidates:** `instr-009`, `instr-015`, `instr-010`

#### `rec-018` — Variant pairs that test different objectives (medium)

- **Need:** Items registered as interchangeable variants must test the same sub-skill, or each objective needs coverage that survives whichever member is served.
- **Chosen intervention:** `instructor-note` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** Five -v2 items are labelled variant_of their parent while testing a different objective (distance decay vs cumulative substitution; hydrolysis vs DIBAH; side-chain vs alcohol oxidation; C=O vs C≡N band; LiAlH4 vs Grignard). If one item per pair is served, whichever objective lost the draw goes unassessed. Recorded rather than re-slugged, because splitting the pairs changes the bank's surfaced/staged balance.
- **Consolidates:** `instr-012`

#### `rec-019` — Platform gaps surfaced by this chapter (high)

- **Need:** Authored option structures and authored non-visual descriptions must reach the learner, and the reader's heading outline must be contiguous.
- **Chosen intervention:** `instructor-note` → target surface `instructor-support`
- **Why this is the least-complex option that fully addresses the need:** Not fixable in the package: no renderer reads question `structure_smiles`, so six items authored as structure-recognition degrade to name-recognition; `accessible_description` is consumed by two renderers this chapter does not use, so all 42 are inert; the images-off path drops the figure's teaching sentence; and figure headings skip h2 to h4. Recorded for the platform backlog — this is the third consecutive chapter to surface the same three.
- **Consolidates:** `visual-005`, `access-001`, `access-003`, `access-005`, `access-008`

#### `rec-020` — Polish: undefined DIBAH, self-answering checks, an unnumbered 'four routes', tier drift, and prose-only relational claims (medium)

- **Need:** Bind the abbreviation where it is first used; make the checks attemptable; make the promised count explicit; keep the shorter tiers a subset of the rendered one; and give the relational comparisons a form that shows the relationship.
- **Chosen intervention:** `sufficient-alt-text` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The DIBAH binding, the 'four routes' count, the borane/electrophilicity reconciliation and the self-check answer that reads backwards are exact bounded corrections and are applied. The reveal-on-attempt behaviour of practice_check callouts is a platform-wide compiler pattern, and the tier-disjointness is an authoring-scope rewrite of three text tiers, so both are recorded.
- **Consolidates:** `stud-010`, `stud-007`, `stud-017`, `stud-012`, `stud-009`, `stud-015`, `stud-008`, `stud-013`, `stud-014`, `stud-016`, `stud-003`, `stud-006`, `access-004`, `access-006`, `access-007`, `visual-006`, `visual-007`, `visual-011`, `instr-016`, `instr-017`

### Merged duplicates

- **The only carboxylate figure teaches the misconception the callout warns against** (`rec-005`) — raised independently by 3 personas: Organic Chemistry Instructor `instr-006`; Learner with Visual Preference `visual-001`; Accessibility Persona `access-002`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Three deferred videos ship as clickable cards that lead nowhere** (`rec-006`) — raised independently by 3 personas: Organic Chemistry Instructor `instr-007`; Learner with Visual Preference `visual-003`; Struggling Student `stud-004`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The cyclic dimer, the central claim of the physical-properties section, is drawn nowhere** (`rec-010`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-005`; Learner with Visual Preference `visual-002`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **No spectrum anywhere in a chapter whose spectroscopy section is about band shape** (`rec-011`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-011`; Learner with Visual Preference `visual-004`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The chapter grades electron flow it never draws** (`rec-012`) — raised independently by 3 personas: Struggling Student `stud-004`; Learner with Visual Preference `visual-009`, `visual-010`; Organic Chemistry Instructor `instr-010`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Reused figures carry the caption written for their first section** (`rec-013`) — raised independently by 2 personas: Struggling Student `stud-011`; Learner with Visual Preference `visual-008`. Kept at the strongest severity (`medium`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Platform gaps surfaced by this chapter** (`rec-019`) — raised independently by 2 personas: Learner with Visual Preference `visual-005`; Accessibility Persona `access-001`, `access-003`, `access-005`, `access-008`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Polish: undefined DIBAH, self-answering checks, an unnumbered 'four routes', tier drift, and prose-only relational claims** (`rec-020`) — raised independently by 4 personas: Struggling Student `stud-010`, `stud-007`, `stud-017`, `stud-012`, `stud-009`, `stud-015`, `stud-008`, `stud-013`, `stud-014`, `stud-016`, `stud-003`, `stud-006`; Accessibility Persona `access-004`, `access-006`, `access-007`; Learner with Visual Preference `visual-006`, `visual-007`, `visual-011`; Organic Chemistry Instructor `instr-016`, `instr-017`. Kept at the strongest severity (`medium`); every persona's learner impact is preserved verbatim in the persona reports above.

### Retained disagreements

#### Whether this chapter's text-first delivery is its principal strength or its principal weakness

- **Accessibility Persona:** "This is a text-first chapter, and that is its main accessibility asset: every quantitative teaching point is stated in prose, not carried by a figure, and every one of the 42 questions is answerable from its prompt text alone." Scored 7.6, the highest score any persona gave any chapter in this batch, and raised no blocker.
- **Learner with Visual Preference:** "Nineteen of the twenty authored assets are single-molecule RDKit structures, and a single-molecule depiction is structurally incapable of showing the three ideas this chapter is built on: the cyclic two-hydrogen-bond dimer, the delocalized carboxylate, and the shape of an infrared band. All three reach the student as prose only." Scored 6.0.
- **Struggling Student:** Sides with Visual Preference and sharpens it: the chapter grades curved arrows and bond-change ledgers "after showing me not one arrow" (stud-004, high).

**Orchestrator resolution:** The same structural disagreement appeared in all four chapters of this batch, and this is the instance where it is most decisive, because the two personas are scoring the same property in opposite directions — a 1.6-point spread. The orchestrator holds both: prose-completeness is a real and rare achievement (it is why this chapter is the only one of the four not computed `blocked`, and why its accessibility persona found no barrier), and it is simultaneously why the chapter can grade an arrow it never drew. The two are not in tension as remedies — every figure in rec-010, rec-011 and rec-012 is scoped to duplicate the prose, never to replace it, which preserves exactly the redundancy Accessibility is crediting. The one place they genuinely collide is the acetate figure, and there the resolution runs against Accessibility's general position: rec-005 keeps the figure's description under active correction precisely because a text equivalent that faithfully describes a misleading picture propagates the error into the channel Accessibility relies on.

#### Whether the chapter has a publication blocker at all

- **Organic Chemistry Instructor:** Four blockers (instr-001 through instr-004), all wrong chemistry reaching a student, at overall_score 6.3.
- **Accessibility Persona:** None, at 7.6 — "None of these makes a required activity impossible."
- **Struggling Student:** None, at 6.6 — "Nothing is impossible to complete."
- **Learner with Visual Preference:** None, at 6.0, despite filing four high-severity findings including one (visual-001) that says the chapter's central figure teaches the misconception the adjacent callout warns against.

**Orchestrator resolution:** Three of four personas raised no blocker and the mean score (6.6) is the highest in the batch, yet the verdict is `major revision` rather than `ready with minor revisions`. That is the computed rule working as intended in the opposite direction from ch13: severity is not a vote, and four independently verified wrong chemical statements — each confirmed by the orchestrator against literature values and against the chapter's own text — force at least `major revision` on their own. What they do NOT force is `blocked`: unlike all three sibling chapters, no required activity here is impossible for any learner, so there is no unresolved required-access blocker. This chapter is therefore the batch's one case where the two halves of the readiness rule pull apart cleanly — blockers present, access intact.

#### Whether the acetate figure is a description defect or a figure defect

- **Accessibility Persona:** access-002, medium: the alt_text "describes only the localized Lewis drawing" and never says the two C–O bonds are equivalent — framed as a text-equivalent problem with a text-equivalent fix.
- **Learner with Visual Preference:** visual-001, high: the figure itself "does exactly that" — it renders the drawing the adjacent callout forbids, so "the caption and the picture disagree" and correcting the words leaves the picture still teaching the error.
- **Organic Chemistry Instructor:** instr-006, high: no figure anywhere shows the resonance pair or the hybrid, and the one asset that would have (the deferred delocalization video) compiles to an empty player.

**Orchestrator resolution:** Visual Preference and the Instructor are right that the full remedy is a new figure, and Accessibility is right that the description is independently wrong and independently fixable. The orchestrator does both at different tiers rather than choosing: the description is corrected now (it is the version a screen-reader user receives, and leaving it would mean the misconception reaches BOTH channels), and the hybrid figure is carried as a visual opportunity. This ordering matters — fixing only the figure would still leave the described version wrong, and fixing only the description would leave the picture wrong; the description is corrected first because it is the cheaper of the two and closes the worse of the two failure modes.

### Places where a description is sufficient (no new asset)

- The prose delivery of the chapter's quantitative content: pKa values, boiling points, IR band positions, NMR shifts, the D2O exchange test and the 120/134 vs 127 pm bond lengths are all written out, so a non-visual reading loses very little and no text equivalent needs authoring for them.
- typed_structure_entry on all four structure_scaffold items — already 'allowed'; nothing to add.
- Every response workspace: labelled selects and buttons throughout, with the bond-change ledger exposing atom numbering as a text list. No keyboard alternative or alternate activity needs authoring.
- The 42 accessible_descriptions as written — none leaks an answer, and each states the stimulus and the task. The defect is delivery, not content, so they should not be rewritten.
- The hint ladders: all 42 items escalate from strategy to structure without naming the key, which is the standard the other three chapters in this batch failed.
- The chapter's outbound links: wikipedia_title authored on all nine concepts and 10/10 links verified 200 — the fabricated-link defect that dominated ch9 and ch10 is absent, though four link LABELS do not describe where they go (carried under rec-020).
- The synthesis_roadmap: conforms exactly to the {nodes, steps} renderer contract with a genuinely linear route and is_target set — no correction needed, and it is the counter-example to ch9's broken roadmap.

### Accessibility blockers

- **`none`** — The Accessibility persona raised no publication blocker — the only such return across the four chapters reviewed in this batch. All four structure_scaffold items set typed_structure_entry to 'allowed', no accessible_description leaks an answer, no level-1 hint discloses a key, and nothing is gated on drag, hover, colour or motion. The persona's highest finding (access-001, high) is a platform delivery gap, not a chapter defect: the 42 authored descriptions are inert because no surface this chapter uses renders them.
- **`access-001`** — Recorded as a high-severity platform finding rather than a blocker because every prompt in this chapter is text-complete on its own, so no activity becomes impossible — the loss is the authored orientation layer, not access to the task.

### Visual opportunities

- The cyclic hydrogen-bonded dimer as a two-molecule object with its two hydrogen bonds and eight-membered ring, contrasted with an alcohol's extended network — the claim three sections and one graded matrix item rest on.
- The carboxylate as a symmetric hybrid: the two equal-energy contributors, and/or an equal-bond-length depiction carrying the 120/134 → 127 pm evidence, alongside the localized Lewis structure students must still be able to draw.
- A carboxylic acid IR spectrum showing the very broad 2500–3300 cm⁻¹ O–H over the strong 1710 cm⁻¹ carbonyl, and a nitrile/alkyne pair in the triple-bond region distinguished by intensity rather than position.
- The nitrile section's one-substrate-four-reagents divergence drawn as a branch, with the DIBAH aldehyde product given the same visual standing as the three siblings that do have structures.
- The C≡N polarization and the two orbital-held lone pairs, before three reactions and a curved-arrow item are built on which lone pair attacks.
- The four-route preparation map sorted by whether the carbon count changes — currently one route is drawn in full and three are drawn not at all, including the assessed Grignard carboxylation.
- The pKa orderings as orderings, including the acetic and benzoic acid reference points the captions measure against, and the chlorobutanoic distance series that has no figure at all.
- The acid–base extraction as a located, ordered process — two layers, the compound moving, the layers separated, the acidification moving it back.

### Regression targets for next run

Recheck these stable `finding_id`s after revision:

- `instr-001` (blocker, Organic Chemistry Instructor) — Section 1 needs the carboxyl delocalization described for what it actually does (shorter C-O, longer C=O, less…
- `instr-002` (blocker, Organic Chemistry Instructor) — The item needs an option set whose acidity relative to acetic acid is unambiguous and a key consistent with th…
- `instr-003` (blocker, Organic Chemistry Instructor) — The practice check must resolve to the Grignard route for this substrate and say why the SN2 route fails, and …
- `instr-004` (blocker, Organic Chemistry Instructor) — The feedback needs the same discriminator the chapter teaches - overlapping positions distinguished by band in…
- `access-001` (high, Accessibility Persona) — The authored per-question description of the stimulus and task needs a delivery path to the learner in whateve…
- `instr-005` (high, Organic Chemistry Instructor) — The physical-properties section needs a representation that makes the two-molecule pairing and its two hydroge…
- `instr-006` (high, Organic Chemistry Instructor) — The acidity section needs the carboxylate shown as a symmetric hybrid alongside the localized Lewis structure …
- `instr-007` (high, Organic Chemistry Instructor) — Deferred video briefs must not surface to a student as an empty player; the reader needs either the still-figu…
- `stud-001` (high, Struggling Student) — Before the first numerical comparison, a student needs to be told plainly what a pKa number is, that the scale…
- `stud-002` (high, Struggling Student) — The chapter needs an explicit, usable account of what 'oxidation level' means for a carbon and how to compare …
- `stud-003` (high, Struggling Student) — At least one problem per major skill needs to be shown being solved step by step, with the decision points a s…
- `stud-004` (high, Struggling Student) — The electron flow the chapter grades needs to reach the student in some non-prose form, and the intermediates …
- `visual-001` (high, Learner with Visual Preference) — The equivalence of the two carbon-oxygen bonds - and the bond-length evidence for it - needs to reach the stud…
- `visual-002` (high, Learner with Visual Preference) — The paired, ring-closed geometry of the dimer - and how it differs from an alcohol's extended network - needs …
- `visual-003` (high, Learner with Visual Preference) — A deferred video must not reach the reader as a clickable card that leads nowhere with producer copy as its de…
- `visual-004` (high, Learner with Visual Preference) — The band-shape discriminations this section teaches and assesses need to be seen at least once before a studen…

---
## Post-correction record

**Estimated state: ready with minor revisions (not a second persona verdict).**

Not a new persona verdict. All four blocker-severity findings are resolved and there was never an access blocker, so the baseline `major revision` clears. The estimate reaches `ready with minor revisions` rather than `ready` because three high-severity needs remain open and all three are new figures or platform work rather than defects in what is written: the cyclic dimer, the carboxylate hybrid and an IR spectrum are still drawn nowhere, and the platform still discards question structure_smiles and accessible_description.

### Artifact-drift check (step 6a, before any compile)

- **Performed:** before any compile, per step 6a
- **Result:** CLEAN — the second chapter in this batch with no artifact-only drift. Commit [commit ref — not in this repo] edited this chapter's compiled reader acidity section, but a byte comparison of nuggets[].text.expanded against the compiled markdown returned identical, so the fix had already been back-ported and a recompile could not destroy it. The chapter also arrived with wikipedia_title authored on all 9 concepts (10/10 links verified 200) and callouts already emitting in all 10 sections.
- **Back-ported to the package before compiling:**

### Changes applied

- BLOCKER: section 1 said delocalization 'weakens the O-H bond and is one reason carboxylic acids are far more acidic than alcohols'. Both halves are false - the carboxyl O-H bond dissociation energy is higher than an alcohol's (about 110-112 vs 105 kcal/mol), and stabilizing the neutral acid opposes ionization. Rewritten to say so explicitly and to redirect the acidity claim to conjugate-base stability, which is what section 3 already argues and what the concept's own trouble spot demands. — resolves `instr-001`
- BLOCKER: ch20-stronger-than-acetic keyed 4-methoxybenzoic acid as NOT stronger than acetic acid, but its pKa is 4.47 against acetic acid's 4.76 - a value this chapter prints in two places - so it IS the stronger acid and a student reasoning from the chapter's own table was graded wrong. The distractor rationale compounded it by silently switching the reference compound to benzoic acid. Option c replaced with phenol (pKa 10, genuinely weaker), and the rationale rewritten to use the prompt's own reference and to state explicitly that every benzoic acid in this chapter is stronger than acetic acid. Key ['a','b','e'] is now correct: chloroacetic 2.86, 4-nitrobenzoic 3.44 and formic 3.75 are stronger; phenol 10 and ethanol 16 are weaker. — resolves `instr-002`
- BLOCKER: the preparation practice check called neopentyl bromide 'primary and unhindered at the reacting carbon' and its cyanide displacement 'straightforward'. Neopentyl halides are the canonical primary halides that do NOT do SN2 - the adjacent quaternary carbon blocks backside attack and the rate is about 1e-5 that of ethyl bromide. The answer now resolves to Grignard carboxylation and explains why the SN2 route fails, and the beta-branching qualification was added to the prose so the chapter's 'primary means SN2 works' rule is no longer unqualified. — resolves `instr-003`
- BLOCKER: the nitrile-IR feedback and its level-2 hint both taught that the nitrile band sits 'above the alkyne range'. The chapter's own section 10 puts alkynes at 2100-2260 cm-1, so 2250 is INSIDE that window. Both rewritten to the discriminator the chapter actually teaches: overlapping positions distinguished by band intensity (nitrile sharp and medium, C-C triple bond weak or absent) plus the terminal alkyne C-H stretch near 3300 cm-1. — resolves `instr-004`
- HIGH: the acetate-ion figure's alt text described only the localized one-double-one-single Lewis structure - the exact drawing the adjacent callout forbids - so the described version of the figure taught the misconception too. Rewrote the alt text and authored a long_description that states the two carbon-oxygen bonds are equivalent, the charge is shared, and gives the 127 pm versus 120/134 pm evidence. — resolves `access-002` · partially addresses `visual-001`, `instr-006`
- HIGH: all three deferred video briefs were still emitting reader cards with a live 'Watch' link to an empty URL and a producer's storyboard camera direction as the student-facing description. Marked hidden; verified in the recompiled artifact that all three video blocks are now is_hidden true. — resolves `instr-007`, `visual-003` · partially addresses `stud-004`
- HIGH: pKa was used 49 times in the rendered reader and never defined, with the only statement of the scale's direction sitting in a warning callout three sections after the first numerical comparison. Added a definition before that first comparison: the negative logarithm of the dissociation constant, smaller means stronger, each unit a factor of ten - with the acetic/ethanol gap worked as 10^11 rather than 'eleven'. — resolves `stud-001`
- HIGH: 'oxidation level' carried the graded feedback of nine questions (16 occurrences) and appeared exactly once, undefined, in the rendered chapter. Added an operational account where the preparations begin - count bonds to electronegative atoms against bonds to hydrogen - with the alcohol/aldehyde/acid ladder made explicit. — resolves `stud-002`
- Narrowed both IR numeric tolerances from 20 to 10 cm-1. At 20 the accepted band was exactly the conjugation shift the chapter teaches, so a prompt saying 'saturated, unconjugated' accepted 1690 (the conjugated value) and the nitrile prompt accepted 2230 - the item could not detect the misconception it targets. Verified: the keys still grade correct and both conjugated values now grade incorrect. — resolves `instr-014`
- Resolved the three-way solubility threshold conflict (trouble spot four carbons, standard tier six, expanded tier's worked list four) onto four carbons, matching the expanded tier's own data - hexanoic acid is already only sparingly soluble, so six was the loose figure. — resolves `instr-013`
- Bound the DIBAH abbreviation to diisobutylaluminium hydride where it is first used; stated the promised count of four preparations, grouped as three carbon-preserving and one chain-lengthening, in the tier the reader renders (it existed only in the standard tier); rewrote the dimer self-check answer to use the section's own mechanism, since 'extended network' versus 'discrete' read backwards to a novice; and reconciled borane's selectivity with section 1's electrophilicity rule by naming the different atom it attacks. — resolves `stud-010`, `stud-017`, `stud-009`, `stud-015`
- Added the cyanide nitrogen as a selectable site on ch20-nitrile-sn2-arrow, so the ambidentate-nucleophile misconception its own feedback addresses ('the reactive electrons are the lone pair on carbon, not on nitrogen') is actually diagnosable - matching the v2 design, which already offered it. — resolves `instr-017`
- Declared the nitrile prerequisite on preparation-of-carboxylic-acids, which teaches cyanide SN2, the nitrile intermediate and nitrile hydrolysis two concepts before nitriles are introduced, so the prerequisite graph stops telling downstream tools that section 5 is safe to serve first. — resolves `instr-008`
- Made the two worst reused-figure captions section-neutral. The compiler emits asset.learning_goal as the caption for every placement, so butanoic acid was captioned about boiling points inside the reactions section and benzoic acid about ring-substituent effects and side-chain oxidation inside the extraction section - both forward-referencing topics the reader had not met. — resolves `stud-011` · partially addresses `visual-008`

### Verification

- curl on all 10 emitted outbound links — 10/10 returned 200 (this chapter arrived with wikipedia_title authored on all nine concepts; no link work was needed)
- Byte comparison of nuggets[].text.expanded against the compiled reader markdown for the section [commit ref — not in this repo] edited — identical, confirming no artifact-only drift to back-port
- Topic-package compiler (proprietary toolchain, not in this repo) — clean
- Automated test suite — 173 passed
- numeric_grading.grade_numeric on both IR items — the keyed values (1710, 2250) grade 'correct' and the conjugated values the prompts rule out (1690, 2230) now grade 'incorrect' (before the change both were accepted)
- ch20-stronger-than-acetic re-checked against literature pKa — key ['a','b','e'] is now correct: chloroacetic 2.86, 4-nitrobenzoic 3.44 and formic 3.75 are stronger than acetic 4.76; phenol 10 and ethanol 16 are weaker
- accessibility_guard.find_accessibility_leaks over all 42 questions — 0 flagged (this chapter was clean before correction too; it is the only one of the four with no answer leak in any description or hint)
- Compiled reader inspection — all three deferred video blocks are now is_hidden true, so the three dead 'Watch' links no longer render; 20 callouts still emit across 10 sections
- git diff review — all changed files are chapter-derived; no unrelated aggregate churn

### Still recommended

- rec-010 / rec-011 / rec-012 — the figure work, and the reason this chapter is not `ready`: the cyclic hydrogen-bonded dimer, the carboxylate resonance hybrid and a carboxylic-acid IR spectrum are all drawn nowhere, and a single-molecule SMILES asset is structurally incapable of expressing the first two. The chapter also grades two curved_arrow and two bond_change_ledger items on electron flow it never draws, and the nitrile addition step its whole mechanism rests on is assessed by nothing.
- rec-019 — platform work, now surfaced by three consecutive chapters: no renderer reads question `structure_smiles` (six items here authored as structure-recognition arrive as name-recognition), `accessible_description` is consumed by two renderers this chapter does not use (all 42 are inert), the images-off path drops the figure's teaching sentence, and figure headings skip h2 to h4.
- stud-005 — the extraction section's misconception callout duplicates the acidity section's verbatim. NOT corrected, and the persona's stated mechanism was wrong: `_trouble_spots_block` resolves from `nugget.concept_slugs`, not from `section_id`, so adding extraction-specific traps to the shared carboxylic-acid-acidity concept would surface them in the acidity section too. The clean fix is a separate concept for the extraction nugget, which is a structural change beyond correction scope.
- rec-017 — acid-base extraction (the chapter's one lab-transferable skill), amide dehydration, and nitrile nomenclature are declared objectives with no graded item.
- rec-018 — five -v2 items are registered `variant_of` their parent while testing a different sub-skill, so if one item per pair is served, whichever objective lost the draw goes unassessed.
- stud-012 — the three text tiers are paraphrases rather than nested levels, so dropping to `standard` swaps in different material rather than less of the same. Rewriting three tiers is authoring scope.
- instr-016 — four Additional Reading labels do not describe where the link goes (e.g. 'Reactions of nitriles' resolves to Lithium_aluminium_hydride), and the only OpenStax link is the chapter opener. All 10 links resolve 200, so this is a labelling and granularity issue rather than a dead-link one.
