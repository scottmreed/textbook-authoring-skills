# Chapter review — Nuclear Magnetic Resonance Spectroscopy (`nuclear-magnetic-resonance-spectroscopy`)

_Reviewed 2026-07-31 · chapter version 1 · personas: Instructor, Struggling Student, Accessibility, Visual Preference_

**Publication readiness: blocked**

This is the best-built chapter of the four remaining and the one with the sharpest defects. Its chemistry is verified clean at a level no earlier chapter reached: every 1H and 13C shift matches literature, every signal count checks against RDKit CanonicalRankAtoms across all 24 molecules, every multiplicity matches the real neighbour count, every integration ratio is right, and all 44 answer keys are chemically correct. It is also the only chapter in this batch that arrived with wikipedia_title authored on all seven concepts (8/8 links verified 200), with callouts already compiling, and with no artifact-only drift to back-port. What blocks it is three wrong statements and one broken grader. Two adjacent sentences in the coupling-constants section are both inverted: one says a doublet of doublets has its LARGE J as the outer spacing (the outer gaps are in fact the SMALL J, and the inner gap is J_L - J_S, which is neither coupling), and the very next says UNEQUAL intensities are the tell for a dd - backwards, since a dd is 1:1:1:1 and a quartet is 1:3:3:1. The second sentence contradicts the sentence immediately before it, the chapter's own splitting-tree SVG (labelled 'dd - 1 : 1 : 1 : 1'), that figure's long description, and the ch13-dd-builder feedback. Third, the methyl acrylate spectrum labels its two terminal vinyl protons with the geometry swapped relative to the ester, in the one figure whose stated purpose is that a measured J assigns alkene geometry. Fourth, four of six numeric_with_units items store `tolerance` as a bare float where the shipped grader does `tolerance.get('mode')` - confirmed by execution to raise AttributeError, so a student who answers correctly receives a server error rather than a mark, and the chapter's only quantitative assessment does not run. On the accessibility side four more blockers land: the J-readoff spectrum renders on no surface and its line positions appear in no text, making the item unanswerable by anyone; the 13C peak-assignment dropdown offers C1..C5 against a structure that carries no atom numbers; the integral-reconstruction trace's aria-label states the graded proton counts outright; and the 44 authored accessible_description strings are consumed only by the demo gallery, which every question here is excluded from.

### Top blockers

- **[BLOCKER] Both J-readoff items carry the line positions only inside student_config.** — `access-001` (Accessibility Persona; question_slug=`ch13-j-readoff`, concept_slug=`spin-spin-splitting`)
- **[BLOCKER] The answer key maps peaks to atom_0.** — `access-002` (Accessibility Persona; question_slug=`ch13-c13-peak-assignment`, concept_slug=`c13-nmr-and-dept`)
- **[BLOCKER] NmrIntegralReconstructionRenderer passes asset.** — `access-003` (Accessibility Persona; question_slug=`ch13-integral-reconstruction`, asset_id=`ethyl-bromide-integral-v1`)
- **[BLOCKER] All 44 questions author an accessibility_bundle.** — `access-004` (Accessibility Persona; question_slug=`ch13-equivalence-partition`)
- **[BLOCKER] The expanded text states that a doublet of doublets has an outer spacing equal to the large J and an inner spacing equal to the small J.** — `instr-001` (Organic Chemistry Instructor; section_id=`nugget-coupling-constants`, concept_slug=`spin-spin-splitting`, nugget_id=`nugget-coupling-constants`)
- **[BLOCKER] The intensity test for telling a dd from a quartet is stated backwards.** — `instr-002` (Organic Chemistry Instructor; section_id=`nugget-coupling-constants`, concept_slug=`spin-spin-splitting`, nugget_id=`nugget-coupling-constants`)
- **[BLOCKER] The two terminal vinyl protons of methyl acrylate are labelled with the wrong geometric relationship to the ester; the two labels are swapped.** — `instr-003` (Organic Chemistry Instructor; asset_id=`nmr-spec-methyl-acrylate-vinyl`, section_id=`nugget-coupling-constants`, concept_slug=`spin-spin-splitting`)
- **[BLOCKER] Four of the six numeric_with_units questions store tolerance as a bare number instead of the {mode, amount} object the shipped grader requires.** — `instr-004` (Organic Chemistry Instructor; question_slug=`ch13-delta-ppm-conversion`, concept_slug=`chemical-shift-and-shielding`)
- **[BLOCKER] The methyl acrylate spectrum is authored at 300 MHz over a 3.** — `visual-001` (Learner with Visual Preference; section_id=`nugget-coupling-constants`, nugget_id=`nugget-coupling-constants`, concept_slug=`spin-spin-splitting`, asset_id=`nmr-spec-methyl-acrylate-vinyl`)

### Top 5 recommended changes

1. **Two adjacent sentences invert the dd geometry and the dd/quartet intensity test** — Students need a correct, checkable procedure for reading both couplings off a doublet of doublets, and a single self-consistent intensity test for telling a dd from a quartet. → **prose-edit** (prose, blocker)
2. **Methyl acrylate's terminal vinyl protons are labelled with swapped geometry** — Each terminal proton's label must state a geometric relationship the reader can verify from the coupling shown, and must agree with the asset's own long description and with ch13-dd-builder. → **new-figure** (figure, blocker)
3. **Four numeric items crash the grader** — Every answer key must round-trip through its own grader before the set is assigned. → **prose-edit** (assessment, blocker)
4. **The J-readoff items are unanswerable by anyone** — The line positions these items are graded on must be present in a form every learner can read. → **text-equivalent** (assessment, blocker)
5. **The integral-reconstruction trace announces its own answer** — The trace's text equivalent must convey where signals lie and that they differ in area, without stating the proton counts or region boundaries being graded. → **text-equivalent** (assessment, blocker)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 6.4/10 | 4 | Chemistry verified clean at unusual depth — but two adjacent sentences invert dd geometry and the dd/quartet intensity test, and four numeric items crash the grader. |
| Struggling Student | 6.2/10 | 0 | Good scaffolding rhythm; the gap is between reading about spectra and reading a spectrum — four of eight sections show none. |
| Accessibility Persona | 5.2/10 | 4 | Outstanding reader half; the assessment half has three unanswerable/leaking item pairs and an authored accessibility layer that reaches no student. |
| Learner with Visual Preference | 6.0/10 | 1 | Every label the author wrote reaches the text channel and none reaches the picture — the sighted reader gets less than the screen-reader user. |

### Affected sections & assets

`c13-nmr-and-dept`, `ch13-aldehyde-peak-select-v2`, `ch13-aldehyde-peak-select`, `ch13-c13-peak-assignment`, `ch13-dd-builder`, `ch13-decoupling-propyl-v2`, `ch13-decoupling-propyl`, `ch13-delta-ppm-conversion`, `ch13-equivalence-partition`, `ch13-ethyl-quartet-builder`, `ch13-integral-reconstruction`, `ch13-isomer-reasoning`, `ch13-j-readoff`, `ch13-single-signal-molecule`, `ch13-spin-system-builder`, `chemical-shift-and-shielding`, `ethyl-bromide-integral-v1`, `h1-shifts-and-integration`, `mol-bromoethane`, `mol-cyclohexane`, `nmr-spec-11-dichloroethane-j`, `nmr-spec-bromoethane-60mhz`, `nmr-spec-bromoethane-j`, `nmr-spec-methyl-acrylate-vinyl`, `nmr-structure-determination`, `nmr-theory-basics`, `nugget-c13-dept`, `nugget-coupling-constants`, `nugget-equivalence`, `nugget-nmr-theory`, `nugget-shifts-integration`, `nugget-splitting`, `nugget-structure-determination`, `proton-equivalence-signal-counting`, `spin-spin-splitting`, `video-nuclear-spin-states`

---
## Full evidence

### Independent persona reports

#### Organic Chemistry Instructor — 6.4/10

Not-go as it stands, but the gap to publishable is small and concentrated. The chemistry is unusually clean: I checked every chemical shift, every signal count (RDKit CanonicalRankAtoms on all 24 molecules), every multiplicity against the actual neighbour count, every integration ratio, and every coupling constant against literature, and the shifts (bromoethane 1.68/3.43, 2-bromopropane 1.7/4.3, 1,1-dichloroethane 2.06/5.89, butan-2-one 13C 8/29/37/209, methyl acetate 13C 21/52/171, p-xylene 13C 21/129/135, propanal 9.8/2.4/1.1, ethyl acetate 1.26/2.05/4.12, methyl acrylate 6.40/6.12/5.82 with J 17.3/10.4/1.5) are all correct, as are all 44 answer keys. Four things block assignment. Three are wrong chemistry reaching students: one sentence inverts which spacing in a doublet of doublets is the large J, the very next sentence inverts the intensity test for distinguishing a dd from a quartet (contradicting the chapter's own splitting-tree figure), and the methyl acrylate spectrum labels its two terminal vinyl protons with the wrong geometric relationship to the ester. The fourth is an assessment block: four of six numeric_with_units questions carry a bare-float tolerance, which raises AttributeError in the shipped grader, so a student who answers correctly gets a server error. Beyond those, the chapter under-assesses its own capstone, never treats OH/NH exchange, and gives the 1H correlation chart as prose only.

**Publication blockers:** `instr-001`, `instr-002`, `instr-003`, `instr-004`

**Strengths**

- Chemical shift values are accurate throughout: bromoethane 1.68/3.43, 2-bromopropane 1.7/4.3, 1,1-dichloroethane 2.06/5.89, propanal 9.79/2.46/1.12, ethyl acetate 1.26/2.05/4.12, butan-2-one 13C 8/29/37/209, methyl acetate 13C 21/52/171, p-xylene 13C 21/129/135, methyl acrylate 6.40/6.12/5.82.
- Every signal count is correct against RDKit CanonicalRankAtoms across all 24 molecules used in prose, assets and questions - including the C5H12 one-signal/three-signal/four-signal argument.
- Multiplicities and integration ratios are right everywhere: the ethyl quartet+triplet, the isopropyl doublet+septet, the CH3 doublet / CHCl2 quartet inversion, and the 9:3 and 6:4 integration reductions.
- The coupling-constant nugget separates line-counting from J-measuring, gives a realistic J table, and correctly explains why n + 1 fails for inequivalent neighbours.
- The two 60 MHz figures are pedagogically well judged: at 60 MHz a 7.3 Hz coupling is 0.12 ppm and genuinely resolvable, and pairing each with a 300 MHz twin makes the hertz-versus-ppm point visually rather than by assertion.
- The integral-reconstruction traces are quantitatively faithful: integrating the shipped traces returns 0.594/0.396 for bromoethane (expected 3:2) and 0.741/0.250 for 1,1-dichloroethane (expected 3:1).
- Wrong-answer explanations are specific and diagnostic - the 2100 Hz, 0.007, 22.5 Hz and 7500 Hz distractor explanations each name the precise conversion error.
- The 13C peak-assignment answer keys use the correct RDKit heavy-atom indices, so they grade against the structure the renderer actually draws.

**Findings**

##### `instr-001` — BLOCKER · chemical-accuracy · confidence 0.98

**Location:** section_id=`nugget-coupling-constants` · concept_slug=`spin-spin-splitting` · nugget_id=`nugget-coupling-constants` · anchor="whose outer spacing is the large J and whose inner spacing is the small one"

**Observation:** The expanded text states that a doublet of doublets has an outer spacing equal to the large J and an inner spacing equal to the small J. Both halves are wrong. For a dd with couplings J_L and J_S the four lines sit at plus/minus (J_L+J_S)/2 and plus/minus (J_L-J_S)/2, so the two OUTER gaps each equal the SMALL J, and the inner gap equals J_L - J_S, which is neither coupling. Using the chapter's own case (the =CH- of methyl acrylate, J = 17.3 and 10.4 Hz): lines at -13.85, -3.45, +3.45, +13.85 Hz give gaps of 10.4, 6.9, 10.4 Hz. The large J is recovered as the line 1-to-3 separation, and the total spread is J_L + J_S = 27.7 Hz.

**Learner impact:** This is the operational rule students use to extract J values from a real multiplet. A student who follows it reports the small coupling as the large one and a meaningless difference term as the small one - and on this chapter's own diagnostic (cis about 10 Hz vs trans about 16 Hz) that inversion assigns alkene geometry backwards. It reaches every reader: the reader defaults to the expanded tier.

**Evidence:** nuggets[5].text.expanded; compiled into the reader chapter, section nugget-coupling-constants, block blk-917758d6.

**Recommended outcome (need):** Students need a correct, checkable procedure for reading both couplings off a dd - which adjacent gap equals the small J, which non-adjacent separation equals the large J, and what the total width represents - consistent with the numbers on the chapter's own splitting-tree figure.

##### `instr-002` — BLOCKER · chemical-accuracy · confidence 0.98

**Location:** section_id=`nugget-coupling-constants` · concept_slug=`spin-spin-splitting` · nugget_id=`nugget-coupling-constants` · anchor="Unequal intensities in a four-line multiplet are therefore the tell that you are looking at a dd rather than a quartet"

**Observation:** The intensity test for telling a dd from a quartet is stated backwards. A doublet of doublets has four lines of EQUAL intensity (1:1:1:1); a quartet has UNEQUAL intensities (1:3:3:1). The chapter therefore tells students that unequal intensities indicate a dd, when unequal intensities are exactly the signature of the quartet. The sentence also contradicts the sentence immediately before it in the same paragraph ('four lines of equal intensity - a doublet of doublets'), the chapter's own splitting-tree figure (labelled 'dd - 1 : 1 : 1 : 1'), the fig-splitting-tree-dd long_description, and the ch13-dd-builder feedback.

**Learner impact:** Multiplet recognition is the one skill the section exists to teach. A student following this rule classifies every 1:3:3:1 quartet as a dd and every genuine dd as a quartet, then assigns the wrong number of neighbours. Because the surrounding text and figure say the opposite, a careful student cannot tell which statement the exam will follow.

**Evidence:** nuggets[5].text.expanded, final sentence of the splitting-tree paragraph; live in compiled reader block blk-917758d6. Contradicted by assets fig-splitting-tree-dd (SVG text 'dd - 1 : 1 : 1 : 1') and by ch13-dd-builder generic_incorrect_explanation.

**Recommended outcome (need):** Students need a single self-consistent intensity test across prose, figure and question feedback - equal line heights mean two different couplings (dd), binomial 1:3:3:1 heights mean three equivalent neighbours (quartet).

##### `instr-003` — BLOCKER · chemical-accuracy · confidence 0.95

**Location:** asset_id=`nmr-spec-methyl-acrylate-vinyl` · section_id=`nugget-coupling-constants` · concept_slug=`spin-spin-splitting` · anchor="=CH₂ (trans to ester)"

**Observation:** The two terminal vinyl protons of methyl acrylate are labelled with the wrong geometric relationship to the ester; the two labels are swapped. In CH2=CH-CO2CH3 the terminal proton that is CIS to the ester is TRANS to the internal =CH- proton and therefore carries the 17.3 Hz coupling. The asset assigns 17.3 Hz to the 6.40 peak (correct) but labels it '=CH2 (trans to ester)', and assigns 10.4 Hz to the 5.82 peak (correct) while labelling it '=CH2 (cis to ester)'. The chapter's own questions use the correct convention - ch13-dd-builder offers '=CH2 proton trans to the internal H' with J = 17.3 Hz - so figure and question describe the same proton with opposite geometric words.

**Learner impact:** The stated purpose of this figure is that a measured J assigns alkene geometry. A student who learns from the labels that the 17.3 Hz proton is 'trans to the ester' will place substituents on the wrong side of the double bond and assign E/Z backwards - the exact error the chapter says the cis/trans J gap exists to prevent. The mislabelling is invisible from the J values, which are all correct.

**Evidence:** assets nmr-spec-methyl-acrylate-vinyl spec.peaks labels vs couplings; compare ch13-dd-builder available_partners {id H_trans, label '=CH2 proton trans to the internal H'} with expected j_hz 17.3.

**Recommended outcome (need):** The figure's peak labels need to name each terminal proton by a relationship the reader can verify from the coupling shown - unambiguously stating which partner cis and trans are measured against - and agree with the convention already used in ch13-dd-builder.

##### `instr-004` — BLOCKER · assessment-readiness · confidence 0.99

**Location:** question_slug=`ch13-delta-ppm-conversion` · concept_slug=`chemical-shift-and-shielding` · anchor=""tolerance": 0.05"

**Observation:** Four of the six numeric_with_units questions store tolerance as a bare number instead of the {mode, amount} object the shipped grader requires. [internal source reference — not in this repo] does tolerance = key.get('tolerance') or {} and then tolerance.get('mode'), so a float raises AttributeError. Executing grade_numeric against the compiled set with the answer key itself as the submission: ch13-delta-ppm-conversion (0.05), -v2 (0.02), ch13-j-readoff (0.5) and -v2 (0.5) all raise AttributeError. Only the two questions with no tolerance key grade, and those grade at zero tolerance.

**Learner impact:** Every student who answers these four questions - including the ones who answer correctly - hits a grader exception rather than a score. The two shift-conversion items and both J-read-off items are the only quantitative practice in the chapter, so the delta-scale and hertz-versus-ppm objectives have no working assessment at all.

**Evidence:** compiled/question-set.json answer_key [redacted] / 0.02 / 0.5 / 0.5 across the four slugs; [internal source reference — not in this repo] requires a mapping.

**Recommended outcome (need):** The four numeric answer keys need a tolerance the shipped grader can read, and the chapter needs a pre-publication check that every answer key round-trips through its own grader before the set is assigned.

##### `instr-005` — HIGH · notation-consistency · confidence 0.93

**Location:** question_slug=`ch13-j-readoff` · concept_slug=`spin-spin-splitting` · asset_id=`nmr-spec-bromoethane-j` · anchor="the same ethyl coupling the CH₂ quartet reports, because coupled partners share one J"

**Observation:** Bromoethane's single vicinal coupling is quoted as three different numbers across the chapter, in material that explicitly teaches that coupled partners must report the identical value. The prose, both bromoethane spectra, the molecule caption and ch13-ethyl-quartet-builder all use 7.3 Hz. ch13-j-readoff plots the CH2 quartet with 0.025 ppm line spacing at 300 MHz and keys 7.5 Hz. ch13-j-readoff-v2 plots the CH3 triplet with 0.018 ppm spacing at 400 MHz, keys 7.2 Hz, and its explanation says this is 'the same ethyl coupling the CH2 quartet reports'. A related slip sits in the prose: '0.024 x 300 = 7.3 Hz' (0.024 x 300 = 7.2).

**Learner impact:** The one thing this section wants students to internalise is that a coupling is a single fixed number shared by both partners. A student who does the two read-off questions in sequence measures 7.5 Hz from one end of the ethyl group and 7.2 Hz from the other, is told they must be identical, and concludes either that the rule is approximate or that they made an arithmetic error.

**Evidence:** assets nmr-spec-bromoethane-60mhz / -j (jHz 7.3); ch13-ethyl-quartet-builder expected j_hz 7.3; ch13-j-readoff line positions 3.400/3.425/3.450/3.475 at 300 MHz keyed 7.5; -v2 lines 1.662/1.680/1.698 at 400 MHz keyed 7.2; nuggets[5].text.expanded.

**Recommended outcome (need):** One bromoethane coupling constant needs to be true everywhere - prose, both spectrum figures and both read-off questions - with plotted line positions chosen so the arithmetic a student does returns exactly that number.

##### `instr-006` — HIGH · misconception · confidence 0.9

**Location:** section_id=`nugget-shifts-integration` · concept_slug=`h1-shifts-and-integration` · question_slug=`ch13-decoupling-propyl-v2` · anchor="Hydroxyl and amine protons are variable, appearing anywhere from δ 1 to 5"

**Observation:** The chapter teaches the n + 1 rule as universal and never tells students that O-H and N-H protons usually do not couple to their neighbours because of rapid chemical exchange, nor that a D2O shake identifies them. The only mention of hydroxyl protons is one clause about variable position and breadth. Meanwhile the chapter's own examples put alcohols in front of students: hexan-1-ol is a distractor in ch13-single-signal-molecule, and ch13-decoupling-propyl-v2 uses propan-1-ol but sidesteps the issue with 'consider only the carbon-bound hydrogens'. A student applying the chapter's rules to ethanol predicts an OH triplet and a CH2 multiplet split by the OH; a routine CDCl3 spectrum shows an OH singlet and a clean quartet.

**Learner impact:** Alcohols are the most common functional group students meet in an introductory spectrum, and the exchange exception is the most common way a correctly applied n + 1 rule gives a wrong prediction. The chapter's own hedge in the propan-1-ol question signals that the authors knew the gap existed without closing it.

**Evidence:** nuggets[3].text.expanded; nuggets[4] and [5] state n + 1 with no exchange exception; ch13-decoupling-propyl-v2 prompt_text; ch13-single-signal-molecule option d.

**Recommended outcome (need):** Students need the exchange exception stated where the n + 1 rule is taught - why OH and NH protons normally appear as unsplit, broad, variable-position signals, and how to confirm one experimentally - plus at least one practice item where recognising the exception is what makes the prediction come out right.

##### `instr-007` — HIGH · assessment-readiness · confidence 0.88

**Location:** concept_slug=`nmr-structure-determination` · question_slug=`ch13-isomer-reasoning` · section_id=`nugget-structure-determination`

**Observation:** The chapter's capstone concept - assembling a structure from NMR evidence - is assessed by exactly two questions, and both present the answer as a choice between two named candidates. Since only one variant surfaces per student, the graded elucidation task reduces to a 50% pick plus a two-of-three evidence multi-select. There is no item where a student is given a formula and a spectrum and must produce a structure, and none that requires combining the 1H and 13C spectra of the same unknown, even though the nugget's argument is that the 13C spectrum supplies the final checks.

**Learner impact:** Recognition between two supplied isomers is materially easier than construction, and it is the construction skill that transfers to exams and to later chapters, which the nugget says will 'assume' this workflow. An instructor cannot tell whether a student can elucidate a structure, only whether they can pick between two labelled options.

**Evidence:** 44 items across 15 types; the only nmr-structure-determination items are ch13-isomer-reasoning (acetone vs propanal) and -v2 (ethyl acetate vs methyl propanoate), both structured_reasoning with a two-option claim field.

**Recommended outcome (need):** The chapter needs at least one graded item where the student builds or names a structure from a formula plus spectral evidence rather than choosing between supplied candidates, and at least one that forces 1H and 13C evidence to be combined on the same unknown.

##### `instr-008` — HIGH · visual-opportunity · confidence 0.85

**Location:** section_id=`nugget-shifts-integration` · concept_slug=`h1-shifts-and-integration` · nugget_id=`nugget-shifts-integration`

**Observation:** The section that establishes the 1H correlation regions carries no figure of those regions. Its only assets are two 2D structures. The seven shift windows the chapter relies on for the rest of the chapter exist only as a run-on sentence in prose, and are the content of four separate questions. The 13C regions in nugget-c13-dept have the same problem.

**Learner impact:** The correlation chart is the single artefact a student keeps open while working every spectrum problem in this and every later chapter. Delivered as prose it cannot be scanned, cannot be compared region-to-region, and gives the student nothing to hold against a real spectrum's axis.

**Evidence:** nuggets[3].asset_ids = ['mol-methyl-pivalate','mol-propanal']; compiled section contains only text, callout, two molecule blocks and links. Assessed by ch13-downfield-ranking(-v2) and ch13-shift-region-matching(-v2).

**Recommended outcome (need):** Students need the 1H (and ideally 13C) correlation regions presented against a shared shift axis so the windows can be compared and located at a glance, in the section where they are introduced.

##### `instr-009` — MEDIUM · objective-alignment · confidence 0.9

**Location:** question_slug=`ch13-dd-builder` · concept_slug=`spin-spin-splitting` · anchor="trans coupling runs near 16–17 Hz and cis coupling near 10 Hz"

**Observation:** Several multiplet- and spin-system-builder questions ask for 'a typical' J while their answer keys demand a specific literature value inside the grader's default tolerance, so a student who enters the value the chapter itself teaches loses marks. Running MULTIPLET_GRADER against ch13-dd-builder: the chapter's own table values (trans about 16, cis about 10) score 0.6; even 17.0/10.0 scores 0.667; only 17.3/10.4 scores 1.0. ch13-ethyl-quartet-builder asks for 'a typical vicinal J' and hints 'about 6-8 Hz', but 6.5 or 8.0 scores 0.6 against the 7.3 key. ch13-spin-system-builder hints 'roughly 6-8 Hz' against a 6.1 key with a 0.5 window.

**Learner impact:** A student who has learned the chapter's J table correctly is penalised for using it, and the feedback does not explain that the key wanted the exact literature value for this specific compound. That teaches students to distrust the table they were just told is the diagnostic tool.

**Evidence:** ch13-dd-builder expected_couplings j_hz 17.3 / 10.4 with no grading_rules override; [internal source reference — not in this repo] default tol 0.3; ch13-spin-system-builder expected j_hz 6.1 with default tol 0.5.

**Recommended outcome (need):** The J tolerance a student is graded against needs to match the precision the prompt and hints ask for - either widen the accepted band to the taught range, or state that the exact measured coupling is required and supply it.

##### `instr-010` — MEDIUM · objective-alignment · confidence 0.9

**Location:** concept_slug=`c13-nmr-and-dept` · section_id=`nugget-c13-dept` · anchor="Use DEPT information to classify each carbon by its number of attached hydrogens."

**Observation:** The third learning objective of nugget-c13-dept - using DEPT to classify carbons by attached-hydrogen count - is never assessed. The chapter teaches DEPT-135 phase behaviour, but the only two 13C questions are ch13-c13-peak-assignment, which HANDS the student the DEPT result as a given, and ch13-c13-region-categorize, which is purely about shift regions. No item asks a student to predict which lines vanish, which invert, or to use a DEPT trace to sort a skeleton.

**Learner impact:** DEPT is the tool that converts a carbon spectrum from a list of environments into an atom-by-atom inventory, and the structure-determination nugget explicitly relies on it. A student can pass this question set without ever having used it.

**Evidence:** nuggets[6].learning_objectives[2]; c13-nmr-and-dept questions are only ch13-c13-peak-assignment(-v2) and ch13-c13-region-categorize(-v2); the peak-assignment prompt supplies the DEPT classification.

**Recommended outcome (need):** The DEPT objective needs at least one item where the student derives the CH3/CH2/CH/C classification rather than receiving it, ideally on a molecule whose 13C assignment is ambiguous without it.

##### `instr-011` — MEDIUM · visual-opportunity · confidence 0.85

**Location:** section_id=`nugget-c13-dept` · concept_slug=`c13-nmr-and-dept` · nugget_id=`nugget-c13-dept`

**Observation:** The 13C/DEPT section contains no spectrum of any kind. Its assets are two 2D structures, so the chapter never shows what a proton-decoupled carbon spectrum or a DEPT-135 trace looks like - the one-line-per-environment appearance, the 0-220 ppm spread, or the positive/negative/absent phase pattern. This is more striking because the chapter ships four authored 1H spectrum figures, and the nmr_spectrum asset type already supports a 13C nucleus.

**Learner impact:** Students meet 13C peak positions only as bare numbers in a question's peak list and never see them on an axis, so they arrive at real spectra without a mental picture of the scale or of how sparse a decoupled carbon spectrum is. The DEPT sign convention in particular is a visual fact prose cannot deliver.

**Evidence:** nuggets[6].asset_ids = ['mol-butan-2-one','mol-p-xylene']; compiled section has no teaching_asset or image block; all four nmr_spectrum assets are nucleus '1H'.

**Recommended outcome (need):** The carbon section needs students to see a decoupled 13C spectrum on its 0-220 ppm axis together with the DEPT companion that phases its lines, for a molecule the section already uses.

##### `instr-012` — MEDIUM · figure-accuracy · confidence 0.85

**Location:** asset_id=`nmr-spec-methyl-acrylate-vinyl` · section_id=`nugget-coupling-constants` · anchor="The three vinyl protons each integrate to one proton and each appear as four lines."

**Observation:** The methyl acrylate figure's alt text and long description promise 'three one-proton doublets of doublets' and state that each vinyl proton appears as four lines, but the rendered trace cannot show that for two of the three. The shared builder uses a fixed Lorentzian half-width of 0.008 ppm. At the spec's 300 MHz that is 2.4 Hz, so the 17.3 Hz and 10.4 Hz splittings resolve, but the 1.5 Hz geminal coupling (0.005 ppm) is below the linewidth and merges. The 6.40 and 5.82 signals therefore render as broadened doublets; only the 6.12 internal proton renders as a visible dd.

**Learner impact:** The figure is the section's evidence that every vinyl proton is a dd and that each J appears on exactly two protons. A student comparing picture with description sees two of three claims unsupported, and the small geminal coupling - which the chapter singles out as explaining the narrow extra splitting - is exactly the one that does not appear.

**Evidence:** assets spec spectrometerMHz 300, ppmMin 3.0, ppmMax 7.0, couplings 17.3/10.4/1.5; [internal source reference — not in this repo] LINEWIDTH_PPM = 0.008 and SAMPLES = 600 over a 4 ppm window.

**Recommended outcome (need):** The figure needs to display the structure its caption claims - either a window/field combination in which the 1.5 Hz splitting resolves, an expansion of the vinyl region, or a description matching what the trace can show.

##### `instr-013` — LOW · figure-accuracy · confidence 0.9

**Location:** asset_id=`nmr-spec-bromoethane-j` · section_id=`nugget-coupling-constants` · anchor="each multiplet spans only about 0.05 ppm rather than 0.25 ppm"

**Observation:** The long description of the 300 MHz bromoethane figure gives one multiplet width for both signals, but the two multiplets have different widths. With J = 7.3 Hz the CH3 triplet spans 2J = 14.6 Hz (0.049 ppm at 300 MHz, 0.243 at 60 MHz) while the CH2 quartet spans 3J = 21.9 Hz (0.073 and 0.365). The quoted 'about 0.05 ppm rather than 0.25 ppm' describes only the triplet and understates the quartet by about 50%.

**Learner impact:** Minor, but this figure exists specifically to make students reason quantitatively about ppm-versus-hertz conversion, and a student who checks the stated widths against n x J finds one of the two does not reconcile.

**Evidence:** assets accessibility.long_description; spec peaks 1.68 (2 neighbours) and 3.43 (3 neighbours), both jHz 7.3, spectrometerMHz 300.

**Recommended outcome (need):** The description needs multiplet widths a student can reproduce from n x J for each of the two signals separately.

##### `instr-014` — LOW · missing-example · confidence 0.8

**Location:** section_id=`nugget-nmr-theory` · anchor="Read in McMurry (OpenStax) — Chapter 13"

**Observation:** The compiled reader carries exactly one OpenStax link for the whole chapter, pointing at the generic chapter opener rather than at the specific sections backing each of the eight nuggets. Every other section's only outside reading is a Wikipedia link, and two sections share the identical J-coupling article.

**Learner impact:** A student sent to 'Chapter 13' for support on, say, the doublet-of-doublets construction has to find the relevant section themselves, and an instructor cannot map an assignment to a specific reading.

**Evidence:** Compiled reader: a single mcmurry_link block in nugget-nmr-theory; external_link blocks in nugget-splitting and nugget-coupling-constants both point to the J-coupling article.

**Recommended outcome (need):** Each major section needs a specific verified outside reading target rather than one chapter-level pointer.

##### `instr-015` — LOW · misconception · confidence 0.7

**Location:** asset_id=`nmr-spec-methyl-acrylate-vinyl` · concept_slug=`spin-spin-splitting` · anchor="such second-order spectra are recognized in this course rather than analyzed"

**Observation:** The methyl acrylate figure is drawn as a strictly first-order spectrum with symmetric multiplets, but at 300 MHz the 6.40 and 6.12 signals are only 84 Hz apart with a 17.3 Hz coupling between them (delta-nu/J about 5). A real spectrum shows visible roofing - inner lines taller than outer - in exactly this vinyl region. The chapter warns that patterns distort when shift differences are small compared with J, but never connects that warning to the one spectrum where the effect would be visible.

**Learner impact:** Students told a dd has four equal lines will not recognise a real acrylate vinyl multiplet, and will read the intensity asymmetry as evidence of a different multiplicity.

**Evidence:** assets spec peaks at 6.4 and 6.12 ppm, spectrometerMHz 300, shared jHz 17.3; nuggets[4].text.expanded closing sentence on second-order spectra.

**Recommended outcome (need):** Where the chapter shows a nearly-degenerate coupled pair, students need a pointer that real intensities lean toward the coupled partner, so they can recognise roofing rather than mis-assign the pattern.

**Open questions**

- The peak_assignment renderer offers every heavy atom in the dropdown, so students assigning a 13C spectrum can select the ester or ketone oxygens as the producer of a carbon peak. Is filtering candidates to carbons a chapter-authoring option or a platform change?
- The nugget-nmr-theory video brief is production_status 'deferred' and compiles to a hidden video block. Is the spin-state animation expected before this chapter is assigned?
- practice_check callouts compile with the answer printed directly beneath the prompt. That is a platform-wide compiler pattern, but it removes the retrieval value of all eight self-checks - is a reveal-on-click form available?
- publishing.available and the compiled reader's available flag are both false, and demo_eligible is 0. I reviewed the chapter as authored; I have not verified what an enrolled student would currently see.

#### Struggling Student — 6.2/10

The prose is unusually clear for NMR and the scaffolding skeleton is genuinely good: every one of the eight sections carries a named-mistakes callout and a 'Check yourself before moving on' prompt, all six vocabulary terms I was told to watch for are defined in the expanded tier the reader compiles, and all 44 bank questions ship a hint ladder. Where it fails a student like me is the gap between reading about spectra and reading a spectrum. Four of the eight sections contain zero spectra - including the two I need most, the shift-regions/integration section (which describes an 'integral step' drawn on a spectrum I never see) and the capstone (which contains two structure drawings and no spectrum at all). That capstone opens by telling me to compute degrees of unsaturation first, a step the chapter never defines or demonstrates. The coupling-constants section is 761 words against a ~350-word average, re-teaches J that section 5 already taught, and its named-mistakes callout is a byte-identical copy of section 5's, so the two traps unique to it are never named. Section 2 tells me the induced field opposes the applied field; section 4 says it reinforces it; nothing reconciles them. And the one animation the chapter promises renders as a card with a film-direction sentence and a 'Watch' link pointing at an empty URL.

**Publication blockers:** _none_

**Strengths**

- Every one of the eight sections carries both a 'Common ways this goes wrong' callout and a 'Check yourself before moving on' prompt - a consistent, predictable scaffolding rhythm.
- All six vocabulary terms that graded feedback relies on - shielding, deshielding, upfield, downfield, integration, multiplicity, coupling constant - are defined in the expanded tier the reader compiles, before any question uses them.
- All 44 compiled questions ship a graduated hint ladder (28 with two levels, 16 with three) that moves from a principle to a procedure to a near-answer.
- The delta-scale explanation works the same number two ways (2100/300 and 4200/600 both giving 7.00), which is exactly the demonstration that makes field-independence stick.
- The four nmr_spectrum figures deliberately use 60 MHz where the splitting must be readable and 300 MHz where compression is the point, and their long_descriptions state the reasoning.
- The 1,1-dichloroethane figure explicitly calls out that integrals and multiplicities point in opposite directions, pre-empting a genuine and very common confusion.
- The J-magnitude table renders as a real table and gives cis (~10 Hz) and trans (~16 Hz) far enough apart to be usable.

**Findings**

##### `stud-001` — HIGH · worked-example-gap · confidence 0.95

**Location:** section_id=`nugget-structure-determination` · concept_slug=`nmr-structure-determination` · nugget_id=`nugget-structure-determination` · anchor="A four-question inventory converts spectra into structures"

**Observation:** The chapter's capstone section teaches how to convert a spectrum into a structure and contains no spectrum. Its six blocks are one text block, two callouts, two molecule drawings and an external link. All four nmr_spectrum assets are attached to nugget-splitting and nugget-coupling-constants only, so the four-question inventory is demonstrated entirely on delta values quoted in running prose.

**Learner impact:** I have spent seven sections being told the spectrum is the evidence, and at the moment I am supposed to put the method together I am handed two structure drawings and a paragraph of numbers instead of the spectrum the numbers came from. I cannot rehearse the actual motion - look at a trace, count signals, read integrals off the steps, measure the splittings - so on the first exam spectrum I freeze and start guessing from the answer choices.

**Evidence:** Reader blocks blk-ae42ad72 (text), blk-f3344a3b (callout), blk-d866971c and blk-1886cb4a (molecules), blk-6f1779cb (callout), blk-44174be8 (link). No nmr_spectrum asset has 'nugget-structure-determination' in its nugget_ids.

**Recommended outcome (need):** A student needs to see at least one complete spectrum-to-structure pass performed on a displayed spectrum - signal count, region assignment, integral reading and multiplicity matching applied in order to a visible trace - rather than on delta values recited in prose.

##### `stud-002` — HIGH · conceptual-support · confidence 0.93

**Location:** section_id=`nugget-structure-determination` · concept_slug=`nmr-structure-determination` · anchor="The degrees of unsaturation implied by the molecular formula are computed first"

**Observation:** Step one of the chapter's structure-determination method is computing degrees of unsaturation, but the chapter never states the formula, never works an example, and never links out to it. The concept lists 'structure-determination-strategy' as a prerequisite, but that concept is not in this package's concepts array and no reader block points to it. The term reappears in the section's named-mistakes callout with no more support.

**Learner impact:** The very first instruction of the capstone method is one I cannot execute. I do not remember the formula from the earlier chapter, there is nothing on the page to remind me, and the section gives me no way to check whether I did it right - so I skip step one entirely and fall straight into the peak-by-peak guessing the callout is warning me against.

**Evidence:** Reader block blk-ae42ad72; blk-f3344a3b; package concepts array contains seven slugs, none of them structure-determination-strategy; searching the compiled chapter for the formula returns nothing.

**Recommended outcome (need):** A student needs the degrees-of-unsaturation step to be executable inside this chapter - the computation stated and demonstrated on at least one of the chapter's own formulas - or an explicit in-reader pointer to where it was taught.

##### `stud-003` — HIGH · misconception · confidence 0.9

**Location:** section_id=`nugget-shifts-integration` · concept_slug=`h1-shifts-and-integration` · anchor="the small field this circulation induces reinforces the applied field at the positions of the attached hydrogens"

**Observation:** Section 2 establishes that the induced electron field opposes the applied field. Section 4 then reverses it for pi systems in a single clause, with no explanation of why position relative to the circulation flips the sign and no figure. The chapter's only diagram asset is unrelated.

**Learner impact:** I read two flatly opposite statements about the same induced field two sections apart and cannot tell which is the rule. I stop trying to understand shielding and just memorize 'aromatic is around 7' as an unexplained fact - the fragile model that collapses the first time I meet an anisotropic environment that is not benzene.

**Evidence:** Reader block blk-69ffb22a ('this induced field opposes the applied one') vs blk-42ce8fa1 ('reinforces the applied field at the positions of the attached hydrogens'); callout blk-afaf2a96 repeats 'ring current and anisotropy' without explaining either.

**Recommended outcome (need):** A student needs the opposes-versus-reinforces reversal reconciled where it is introduced - an account tied to where the proton sits relative to the circulating pi electrons - so anisotropy reads as a consequence of the shielding rule rather than an exception that contradicts it.

##### `stud-004` — HIGH · cognitive-load · confidence 0.92

**Location:** section_id=`nugget-coupling-constants` · concept_slug=`spin-spin-splitting` · nugget_id=`nugget-coupling-constants` · anchor="The n + 1 rule carries a hidden assumption: that all n neighbours couple with the same J."

**Observation:** The coupling-constants section is one uninterrupted 761-word text block - 2.1x the ~350-word average of the other seven sections (362, 346, 328, 364, 442, 349, 373). Inside it a student meets, in order: the ppm-to-hertz conversion, the field-independence argument, the case for high-field instruments, spin-system matching by shared J, a six-row J table, the hidden assumption behind n + 1, splitting-tree construction, the doublet of doublets, the dd-versus-quartet intensity test, the three-coupling analysis of methyl acrylate, and the doublet of triplets - with no subheading, checkpoint or break anywhere.

**Learner impact:** This is where I actually give up. Everything before arrives as one manageable idea per section; here eleven ideas arrive in one scroll with no place to stop, and by the doublet of triplets in the last sentence I have lost the splitting-tree procedure from four paragraphs earlier.

**Evidence:** Reader block blk-917758d6, 761 words in eight paragraphs. Every other text block is 328-442 words. nugget-coupling-constants declares four learning objectives, more than any other nugget.

**Recommended outcome (need):** A student needs this section broken into digestible units with intermediate checkpoints - measurement-and-conversion, the J-magnitude table, and the splitting-tree/dd procedure should not have to be absorbed as one continuous read.

##### `stud-005` — HIGH · misconception · confidence 0.94

**Location:** section_id=`nugget-coupling-constants` · concept_slug=`spin-spin-splitting` · anchor="Counting the protons of the signal itself rather than its neighbors"

**Observation:** The 'Common ways this goes wrong' callout in the coupling-constants section is byte-identical to the one in the splitting section - both nuggets map to the single concept spin-spin-splitting, whose two trouble_spots are therefore rendered twice. As a result the two traps belonging specifically to this section are never named: mistaking a 1:1:1:1 dd for a 1:3:3:1 quartet, and reading the table row 'Geminal, two protons on the same sp3 carbon | ~12 Hz' as meaning an ordinary CH2 splits itself. The caveat on the second is buried mid-paragraph and contradicts what section 5 told me.

**Learner impact:** The section teaches an intensity tell, then its warning box tells me something I learned two sections ago. I take the repeat as confirmation that nothing new can go wrong here, walk into the four-line multiplet trap on the homework, and separately start predicting 12 Hz doublets for every CH2 because that is what the table row says.

**Evidence:** Verified byte-identical: the markdown of blk-78edfbe5 (nugget-splitting) equals that of blk-78edfbe5-1 (nugget-coupling-constants). Both nuggets declare concept_slugs ['spin-spin-splitting'].

**Recommended outcome (need):** A student needs the named-mistakes coverage in this section to address this section's own traps - the dd-versus-quartet intensity confusion and the geminal-J caveat - instead of repeating the previous section's warnings verbatim.

##### `stud-006` — HIGH · cognitive-load · confidence 0.96

**Location:** section_id=`nugget-nmr-theory` · asset_id=`video-nuclear-spin-states` · anchor="Open on a scattered field of small compass-needle nuclei pointing in random directions with no applied field."

**Observation:** The chapter's only animation block compiles with an empty url. The reader renders it as a card badged 'Video - ChemIllusion' with a 'Watch' router link pointing at the empty string, and its description carries the first line of the production storyboard rather than a student-facing summary. The package records production_status 'deferred', but the deferral did not suppress the block.

**Learner impact:** The most abstract idea in the chapter - two allowed spin orientations and a field-dependent energy gap - is exactly where I need a picture, and the page tells me a video exists. I click, nothing happens, and I read a sentence about compass needles describing a shot in a film I cannot see. I assume the visual explanation I needed exists somewhere and stop trying to build the model from prose.

**Evidence:** Compiled block blk-5ffd0e32 with url '' and description set to storyboard line 1; [internal source reference — not in this repo] renders the non-external branch as a RouterLink to c.url; video_briefs[0] production_status 'deferred'.

**Recommended outcome (need):** A student needs the page not to advertise a visual that does not exist - either the two-spin-state explanation gets a real visual, or the deferred brief stops emitting a card with a dead link and a storyboard fragment as its description.

##### `stud-007` — HIGH · cognitive-load · confidence 0.91

**Location:** section_id=`nugget-shifts-integration` · concept_slug=`h1-shifts-and-integration` · anchor="so a compact table of regions covers most of organic chemistry"

**Observation:** The section promises 'a compact table of regions' and then delivers eight 1H shift ranges embedded in two prose paragraphs, interleaved with worked examples and mechanism. The 13C regions in section 7 are presented the same way. The chapter demonstrates in section 6 that the reader renders GFM pipe tables correctly - the six-row J table displays as a real table - so the format was available and was not used for the two correlation sets students consult most.

**Learner impact:** This is the reference I come back to on every problem for the rest of the course, and I cannot scan it - I have to reread two paragraphs and mentally extract eight ranges each time. In practice I copy them out wrong, or remember four of the eight, and never notice that OH/NH is variable because that fact is a subordinate clause.

**Evidence:** Reader block blk-42ce8fa1 followed by prose, not a table; blk-c4fbd78b carries the 13C ranges the same way. Contrast blk-917758d6, whose J table renders through [internal source reference — not in this repo] renderTable, whose comment names ch13's coupling constants as the motivating case.

**Recommended outcome (need):** A student needs the 1H and 13C shift correlations in a scannable lookup-shaped form, matching the treatment the same chapter already gives the J-magnitude set.

##### `stud-008` — HIGH · worked-example-gap · confidence 0.9

**Location:** section_id=`nugget-shifts-integration` · concept_slug=`h1-shifts-and-integration` · anchor="drawn on the spectrum as an integral step"

**Observation:** Integration is defined in terms of a visual feature of a spectrum the student has not yet seen and is not shown here. The first four sections contain no spectrum of any kind; the first appears in section 5. The nmr_spectrum asset type supports labelled integral regions - the 1,1-dichloroethane and 300 MHz bromoethane specs both carry regions entries - so the capability exists but is not applied in the section that teaches integration.

**Learner impact:** I am told to read the area under a peak as a step drawn on the trace, and I have never seen a trace or a step. I picture peak height instead - the most common wrong model there is - and nothing corrects me until much later. When the homework asks me to mark integral regions on a real trace, it is the first time I have seen one.

**Evidence:** Reader block blk-42ce8fa1; sections nugget-nmr-theory, nugget-chemical-shift, nugget-equivalence and nugget-shifts-integration contain block_types text/callout/molecule/video/link only; ch13-integral-reconstruction asks the student to mark integral regions.

**Recommended outcome (need):** A student needs to see an integral step on a labelled trace at the point integration is defined, rather than meeting their first spectrum a section later and their first integral only in the graded activity.

##### `stud-009` — MEDIUM · retrieval-practice · confidence 0.88

**Location:** section_id=`nugget-nmr-theory` · anchor="Check yourself before moving on"

**Observation:** All eight 'Check yourself before moving on' callouts render the prompt and its answer as one continuous markdown body with no reveal, collapse or input step. The callout case passes the whole markdown string to RichText, so '**Answer.**' is visible at the same instant as '**Try it.**'. These callouts are the chapter's only in-reader self-check - the compiled reader contains no question or tutorial blocks.

**Learner impact:** I read the question, my eye lands on the answer in the same box before I have attempted anything, and I get the feeling of having known it. Across eight sections that is eight retrieval opportunities converted into eight worked examples.

**Evidence:** blk-a65ed5ff markdown contains both '**Try it.**' and '**Answer.**'; same pattern in blk-eca47e8f, blk-9ff708f9, blk-e8266fb2, blk-6b9e3c61, blk-bebc83b8, blk-c254b1b9, blk-6f1779cb. Compiled block_type counts include no question or tutorial blocks.

**Recommended outcome (need):** A student needs the self-check prompts to require an attempt before the answer becomes visible, so the chapter's only between-section retrieval practice actually functions as retrieval.

##### `stud-010` — MEDIUM · cognitive-load · confidence 0.85

**Location:** section_id=`nugget-equivalence` · concept_slug=`proton-equivalence-signal-counting` · anchor="if the two operations give the same compound, the hydrogens are equivalent (homotopic or enantiotopic"

**Observation:** One paragraph of a core-depth section introduces the substitution test, homotopic, enantiotopic, diastereotopic, stereocenter, achiral solvents and diastereomers - seven terms in four sentences - with no figure, no worked substitution and no practice check on any of them, then closes by saying it 'matters in later courses' and 'appears only occasionally in introductory spectra'. The section's practice check asks only the p-xylene signal count, which the substitution test is not needed for.

**Learner impact:** Four new -topic words arrive at once, none illustrated, and the paragraph ends by telling me they mostly do not matter. I cannot tell whether to learn them, so I skip them - and then the homework's equivalence question tells me to 'Replace each candidate hydrogen with a test group', a procedure I decided was optional.

**Evidence:** Reader block blk-737c3750 paragraph 2, in a nugget whose package depth is 'core'; nugget-equivalence practice_check; ch13-equivalence-partition hint level 3.

**Recommended outcome (need):** A student needs the substitution test either demonstrated concretely once (one molecule, both replacements, the comparison stated) or clearly marked as optional - not introduced with four unfamiliar terms and simultaneously waved off.

##### `stud-011` — MEDIUM · sequencing · confidence 0.86

**Location:** section_id=`nugget-splitting` · concept_slug=`spin-spin-splitting` · anchor="The spacing between adjacent lines of a multiplet is the coupling constant, J, measured in hertz."

**Observation:** The third paragraph of the splitting section already teaches the entire coupling-constant story - J defined, typical vicinal magnitudes, field-independence with the through-bond justification, and shared-J spin-system matching - then adds selective decoupling and second-order spectra. The next section opens by defining the same thing again from scratch and re-arguing field-independence with the bromoethane example.

**Learner impact:** I finish section 5 thinking I have learned J, then section 6 restates its definition as though it is new, so I assume I misunderstood something and reread section 5. The duplication also makes section 5 heavier than its one idea warrants, and buries decoupling and second-order spectra where I will never find them again.

**Evidence:** Reader block blk-484f94d5 paragraph 3 vs blk-917758d6 paragraph 2; both sections map to the same concept slug.

**Recommended outcome (need):** A student needs one place where J is introduced and one place where it is developed; the coupling-constant material should not be taught twice in consecutive sections with the second presented as new.

##### `stud-012` — MEDIUM · conceptual-support · confidence 0.89

**Location:** section_id=`nugget-coupling-constants` · asset_id=`nmr-spec-bromoethane-j` · anchor="This is the same spectrum as the 60 MHz one beside it."

**Observation:** The 300 MHz bromoethane figure's description directs the student to compare it with a 60 MHz spectrum 'beside it', but that figure is attached to the previous section, several blocks and a section boundary earlier. The two spectra are never displayed together anywhere in the reader.

**Learner impact:** The whole point of this pair is a side-by-side: same molecule, same 7.3 Hz, different-looking multiplets. I am told to look beside it, find nothing, and either scroll back hunting for a figure I half remember or give up - so the one demonstration that would make 'J is field-independent' concrete never happens.

**Evidence:** Compiled block blk-952ba88e description; blk-d82aaf75 (60 MHz) sits in section nugget-splitting; the two assets carry different nugget_ids.

**Recommended outcome (need):** A student needs the 60 MHz and 300 MHz bromoethane spectra visible together at the point the field-independence claim is made, or the cross-reference reworded so it does not point at a figure that is not on screen.

##### `stud-013` — MEDIUM · assessment-readiness · confidence 0.87

**Location:** section_id=`nugget-splitting` · question_slug=`ch13-ethyl-quartet-builder` · anchor="Build the multiplet for the CH₂ signal of bromoethane"

**Observation:** Thirty of the 44 compiled questions carry only a generic_incorrect_explanation with no wrong_answer_explanations, and the split is not random: every item of all six interactive NMR types plus peak_assignment, spectrum_peaks, rank_order, matching_pairs, categorize_groups, multi_select, short_answer and structured_reasoning is in that group. Targeted wrong-answer feedback exists only on the 14 single_select and numeric_with_units items, the easiest formats.

**Learner impact:** The activities where I am most likely to be wrong in an interesting, diagnosable way - building a multiplet with the wrong neighbour count, partitioning the wrong hydrogens - give me back the same paragraph regardless of what I did. I retry by changing something at random rather than by correcting a specific misunderstanding.

**Evidence:** Compiled feedback_bundle key sets: 30 questions have (generic_incorrect_explanation, hints); 14 also have wrong_answer_explanations.

**Recommended outcome (need):** A student needs feedback that distinguishes their specific wrong construction from other wrong constructions on the interactive builder items.

##### `stud-014` — MEDIUM · objective-alignment · confidence 0.86

**Location:** section_id=`nugget-splitting` · question_slug=`ch13-decoupling-propyl` · anchor="a selective decoupling experiment that identifies which multiplets are coupled partners"

**Observation:** Two graded items (both difficulty 'advanced', type nmr_decoupling_experiment) assess selective decoupling on 1-bromopropane. In the reader, selective decoupling is a single subordinate clause in the third paragraph of the splitting section. It has no figure, no worked example, no practice check, and appears in none of the learning objectives of any of the eight nuggets.

**Learner impact:** I am asked to reason about which irradiation collapses which multiplets, and when I go back to study for it the entire coverage is half a sentence I did not register as important. I conclude the material was never taught, which is demoralizing in a way a genuinely hard question is not.

**Evidence:** Reader block blk-484f94d5; nugget-splitting learning_objectives cover multiplicity prediction, reading J and the ethyl/isopropyl patterns; ch13-decoupling-propyl difficulty 'advanced'.

**Recommended outcome (need):** A student needs the decoupling experiment either taught to the level at which it is assessed - stated as an objective and demonstrated on a concrete spin system - or dropped from the graded set.

##### `stud-015` — MEDIUM · conceptual-support · confidence 0.83

**Location:** section_id=`nugget-splitting` · anchor="Bromoethane displays the most important pattern in the chapter."

**Observation:** The chapter gives no structural signal of what matters most. All eight sections are built from the identical block sequence, each runs 6-10 minutes, and there is no chapter summary, no key-terms list and no closing recap. The one explicit priority claim in the whole chapter is a sentence in the middle of a paragraph, not reinforced by placement, emphasis or a summary anywhere.

**Learner impact:** Every page looks the same weight, so I study by starting at section 1 and reading until I run out of time - which means I always run out somewhere in the 761-word coupling-constants section and never reach the structure-determination method the exam is actually about.

**Evidence:** Compiled chapter: eight sections each opening with one text block and closing with an external_link; no summary or glossary block; duration_minutes 6,6,6,7,7,8,6,7.

**Recommended outcome (need):** A student needs the chapter to mark its own priorities - which patterns and correlations must be automatic versus which are context - so limited study time lands on the load-bearing material.

##### `stud-016` — MEDIUM · worked-example-gap · confidence 0.85

**Location:** section_id=`nugget-splitting` · concept_slug=`spin-spin-splitting` · anchor="the possible orientation combinations produce three effective fields in a 1:2:1 population ratio"

**Observation:** The origin of multiplet intensities is asserted rather than shown. The section states that two equivalent neighbours give 'three effective fields in a 1:2:1 population ratio' without enumerating the four spin combinations that produce it, then defers to 'intensities follow Pascal's triangle' with no triangle displayed. The splitting tree that would make the mechanism visible exists only in the next section and only for the unequal-J dd case.

**Learner impact:** I memorize 1:2:1 and 1:3:3:1 as arbitrary numbers. When the next section tells me a dd is 1:1:1:1 because 'no two branches land on the same position', the contrast means nothing because I never saw branches landing on the same position in the triplet case - so I cannot use the intensity test.

**Evidence:** Reader block blk-484f94d5; the only tree figure, blk-eca5d1ea, is in nugget-coupling-constants and its long_description covers only the equal-height dd case.

**Recommended outcome (need):** A student needs the 1:2:1 pattern derived where it is introduced - the neighbour spin combinations enumerated and the coincidence that doubles the middle line made visible - so the later dd-versus-quartet intensity test rests on something they have seen.

##### `stud-017` — MEDIUM · worked-example-gap · confidence 0.88

**Location:** section_id=`nugget-c13-dept` · concept_slug=`c13-nmr-and-dept` · anchor="A DEPT-135 experiment phases CH₃ and CH carbons positive and CH₂ carbons negative"

**Observation:** DEPT is taught entirely in one sentence of prose describing a visual convention - positive phasing, negative phasing, disappearance - with no figure of a DEPT trace anywhere in the chapter or package. The section's two figures are structure drawings. Both the section's practice check and a graded item then depend on reading a DEPT result.

**Learner impact:** 'Phases CH2 carbons negative' is describing something on a picture, and I have never seen the picture. I have no idea what a peak pointing downward looks like next to a normal spectrum, so when the practice check asks which carbons vanish I answer from the word 'quaternary' rather than from any understanding of what the experiment shows.

**Evidence:** Reader block blk-c4fbd78b; section nugget-c13-dept blocks are text, callout, molecule, molecule, callout, external_link; practice check blk-c254b1b9; ch13-c13-peak-assignment prompt supplies the DEPT result.

**Recommended outcome (need):** A student needs to see what a DEPT result looks like - the up/down/absent convention on a trace paired with its decoupled companion - before being asked to reason from DEPT information.

**Open questions**

- Both the compiled reader (available: false) and the compiled question set (demo_eligible: 0) are marked unavailable, and science_review.status is 'not_reviewed'. I reviewed the content as authored.
- The compiled reader carries only the 'expanded' tier. If any surface renders 'standard', note that its J table drops the geminal-alkene row and the caveat that geminal protons on a freely rotating sp3 carbon show no splitting.
- The reader block vocabulary includes no question type, so the 44-item bank cannot be embedded between sections. Is inline practice intended to arrive through a 'tutorial' block type?
- I flagged no blocker-severity finding: nothing is impossible to follow, and the dead video card degrades trust and a key explanation rather than making a required step unreachable. If a rendered dead link counts as a publication defect on its own terms, stud-006 is the candidate.

#### Accessibility Persona — 5.2/10

The reader half of this chapter is one of the strongest non-visual builds in this corpus: every one of the four nmr_spectrum figures and the splitting-tree diagram carries a long_description stating shift, multiplicity, intensity ratio, integration and J, and TeachingAssetLiveRenderer prints both alt text and long description as visible text, so a learner who never sees the trace still gets the whole spectrum. Prose, misconception callouts and practice checks are plain text; the undeliverable spin-state video is hidden rather than left as an empty player. The assessment half does not hold up. Three question pairs fail outright for a non-visual learner: ch13-j-readoff(+v2) declares a labelled line-position spectrum that no surface renders and whose positions appear in no text, so the required subtraction has no inputs; ch13-c13-peak-assignment(+v2) asks students to assign peaks to atoms identified only as C1..C5 in a dropdown while the rendered structure carries no atom numbers and a hard-coded generic alt; and ch13-integral-reconstruction(+v2) exposes its trace through an aria-label that states the answer - peak positions and proton counts both. Underneath it all sits a delivery gap: the 44 carefully written accessible_description strings are consumed only by the demo gallery, and every question here is demo_eligible false, so the chapter's entire authored non-visual equivalence layer currently reaches no student. The interactive NMR workspaces themselves are genuinely good - keyboard-complete selects, number steppers and real buttons, with colour always paired with a group letter - which makes the gaps stimulus-side, not interaction-side.

**Publication blockers:** `access-001`, `access-002`, `access-003`, `access-004`

**Strengths**

- All four nmr_spectrum reader figures carry a long_description that is a genuine transcript rather than a caption - shifts, multiplicity, Pascal intensity ratios, integration, line spacing in both ppm and Hz - and the reader prints both alt text and long description as visible text below the trace, so the spectra are fully readable without sight.
- The 60 MHz / 300 MHz bromoethane pair, whose entire teaching point is a visual comparison of multiplet width, quantifies that comparison in text (0.25 ppm vs 0.05 ppm at a fixed 7.3 Hz) rather than leaving it to the eye.
- The fig-splitting-tree-dd long description narrates the branching step by step with both J values and the resulting 1:1:1:1 ratio, and contrasts it with the 1:2:1 triplet case - a static description that fully substitutes for the figure.
- Every interactive workspace is keyboard-complete by construction: multiplet builder, spin-system builder and integral reconstruction run on labelled selects and number fields with steppers; decoupling is two dropdowns over a text list of coupling edges; spectrum_peaks targets are real buttons with aria-pressed; rank_order ships Move up / Move down buttons whose labels state current position. No drag-only or hover-only path anywhere.
- EnvironmentPaintBoard pairs every environment colour with a letter badge on both the palette chip and the painted atom, uses the Okabe-Ito colourblind-safe palette, groups atom tokens by parent carbon, and announces each assignment through an aria-live region - colour is never the sole carrier.
- Chapter prose, the eight misconception callouts and the eight practice checks are plain text with no visual dependency, and each section's links have descriptive titles rather than bare URLs.
- The undeliverable spin-state video is compiled with is_hidden true rather than left as an empty player, and its content is carried by nugget-nmr-theory prose.

**Findings**

##### `access-001` — BLOCKER · media-equivalence · confidence 0.95

**Location:** question_slug=`ch13-j-readoff` · concept_slug=`spin-spin-splitting` · anchor="The spectrum below shows the CH₂ multiplet of bromoethane recorded at 300 MHz, with each line position labelled in ppm."

**Observation:** Both J-readoff items carry the line positions only inside student_config.spectrum.peaks[].label (3.400/3.425/3.450/3.475 ppm; 1.662/1.680/1.698 ppm). numeric_with_units declares workspace 'none', and ActivityWorkspaceRenderer returns null for that workspace; only SpectrumPeakRenderer and PeakAssignmentRenderer read config.spectrum, so nothing renders this stimulus on any surface. The accessible_description says the positions are 'labelled numerically' but does not contain them.

**Learner impact:** A learner using a screen reader - and in fact any learner - is told to subtract one labelled line position from the next, but no channel, visual or textual, ever supplies those positions. The item is not merely hard without sight; it is unanswerable, and the only route to the graded number is the hint ladder plus the wrong-answer explanations, which reveal 0.025 ppm and 0.018 ppm outright.

**Evidence:** Package peaks line_0-line_3 at x = 3.4, 3.425, 3.45, 3.475 with labels '3.400 ppm'...; accessibility_bundle text; [internal source reference — not in this repo]: if (workspace === 'none') return null;

**Recommended outcome (need):** The measurable data these items are graded on - the ordered list of line positions in ppm - must be present in a form a non-visual learner can read, on whatever surface the question ships to. A description that asserts a figure exists is not a substitute for the figure's numbers.

##### `access-002` — BLOCKER · media-equivalence · confidence 0.93

**Location:** question_slug=`ch13-c13-peak-assignment` · concept_slug=`c13-nmr-and-dept` · anchor="Assign each ¹³C signal of butan-2-one, CH₃CH₂COCH₃, to the carbon that produces it."

**Observation:** The answer key maps peaks to atom_0..atom_3. PeakAssignmentRenderer renders those choices as C1, C2, C3, C4 (symbol + index+1) in a dropdown, above a structure image whose alt is the hard-coded string 'Structure for this spectrum'. The SVG comes from render_molecule_visual, which calls drawer.DrawMolecule(mol) with no atom notes - no index labels are drawn on the structure at all. Nothing in the package, the renderer, or the accessible description states which carbon of butan-2-one is C1 versus C4. The type declares requires_molecule_description=True, and no such description is supplied.

**Learner impact:** A non-visual learner is offered five identical-looking option labels with no way to know which structural position each denotes; the assignment is a pure guess. A student who genuinely knows that 209 ppm is the carbonyl still cannot express that knowledge.

**Evidence:** answer_key [redacted]; [internal source reference — not in this repo] alt='Structure for this spectrum' and label {atom.symbol}{atom.index + 1}; [internal source reference — not in this repo] drawer.DrawMolecule(mol); [internal source reference — not in this repo] requires_molecule_description=True.

**Recommended outcome (need):** The atom identifiers a student must choose between need an unambiguous non-visual identity - each numbered position described by what it is bonded to - and that identity must match whatever the figure shows.

##### `access-003` — BLOCKER · alt-text-quality · confidence 0.94

**Location:** question_slug=`ch13-integral-reconstruction` · asset_id=`ethyl-bromide-integral-v1` · anchor="a three-proton triplet near 1.68 ppm and a two-proton quartet near 3.43 ppm"

**Observation:** NmrIntegralReconstructionRenderer passes asset.accessibility.description straight through as the spectrum canvas's ariaLabel. For ethyl-bromide-integral-v1 that string is 'a three-proton triplet near 1.68 ppm and a two-proton quartet near 3.43 ppm' and the answer key is regions 1.6-1.8 ppm = 3 protons and 3.3-3.5 ppm = 2 protons. The v2 asset does the same for 1,1-dichloroethane. The description states both the positions and the graded proton counts. The compile-time leak guard runs over the package's accessible_description, not over an externally referenced /assets/nmr/ asset, so this leak passes the build untouched.

**Learner impact:** A screen-reader user is read the complete answer key before doing any work, so the item measures nothing for them; a sighted student must actually integrate the trace. That is not equivalence, it is a differential that invalidates the item in both directions. The level-3 hint closes the remaining gap.

**Evidence:** frontend/public/assets/nmr/ethyl-bromide-integral-v1/asset.json and dichloroethane-integral-v1/asset.json accessibility.description; [internal source reference — not in this repo] ariaLabel binding; both assets also carry accessibility.table_rows: [], a field no code reads.

**Recommended outcome (need):** The non-visual equivalent for a trace a student is asked to integrate must convey where signals lie and that they differ in area, without stating the proton counts or region boundaries being graded - and the leak check needs to see that channel.

##### `access-004` — BLOCKER · media-equivalence · confidence 0.9

**Location:** question_slug=`ch13-equivalence-partition` · anchor="A three-carbon molecule with a bromine on its central carbon is shown with its seven selectable hydrogens"

**Observation:** All 44 questions author an accessibility_bundle.accessible_description, and the compiled set preserves it. On the delivery path RegisteredChapterHomeworkPanel copies accessibilityBundle into the envelope, but nothing renders it: LmsPromptPanel prints only question.promptText plus prompt_stimulus assets, and a repo-wide search finds accessible_description consumed by exactly three places - MolecularGeometryRenderer, ReactionCoordinateQuestionRenderer, and QuestionTypeDemoPage. None of this chapter's 15 question types is among the first two, and every question here is demo_eligible false.

**Learner impact:** The chapter's entire authored non-visual equivalence layer for assessment is written but undelivered. For text-only items this costs little; for the spectrum- and structure-bearing items it means the described stimulus a non-visual learner is supposed to rely on never reaches them, and the good descriptions in this package cannot be credited as working alternatives.

**Evidence:** [internal source reference — not in this repo] renders only {question.promptText}; [internal source reference — not in this repo] passes accessibilityBundle with no consumer; [internal source reference — not in this repo] is the only service that surfaces accessible_description; every compiled question is demo_eligible false.

**Recommended outcome (need):** Every question that has a visual stimulus needs its authored text equivalent actually presented to the learner on the surfaces this chapter ships to. The chapter should not be treated as accessible on the strength of descriptions no student can read.

##### `access-005` — HIGH · media-equivalence · confidence 0.85

**Location:** question_slug=`ch13-spin-system-builder` · concept_slug=`spin-spin-splitting` · anchor="A two-carbon molecule with both chlorines on one carbon is shown with its four selectable hydrogens"

**Observation:** The equivalence-partition and spin-system workspaces present hydrogens as tokens bucketed by parent_atom_id ('on C1', 'on C2', 'on C3') over a structure image whose alt is hard-coded. Which carbon carries the bromine, the two chlorines, or the chlorine versus the bromine is stated nowhere in text - the accessible descriptions say 'a bromine on its central carbon' and 'both chlorines on one carbon' without binding those to the C1/C2/C3 labels the student actually manipulates.

**Learner impact:** A non-visual learner must reverse-engineer the substitution pattern from hydrogen counts per bucket - an inference the sighted student never has to make, and one that is doing part of the chemical reasoning the item intends to test. For ch13-spin-system-builder-v2 (ClCH2CH2Br) the mapping is not recoverable at all; it happens not to affect grading only because the grader canonicalizes by atom set.

**Evidence:** [internal source reference — not in this repo] and [internal source reference — not in this repo] fixed alt strings; package nmr_asset.molecule.atoms carry parent_atom_id with no substituent statement; both types declare requires_molecule_description=True.

**Recommended outcome (need):** The structure a student is partitioning needs a text identity tying each labelled carbon to what it bears, so the selectable-hydrogen labels are self-describing rather than decoded from the picture.

##### `access-006` — MEDIUM · alt-text-quality · confidence 0.82

**Location:** asset_id=`mol-bromoethane` · section_id=`nugget-splitting` · anchor="drawn with all five hydrogens shown"

**Observation:** Five molecule figures set rdkit_options.show_hydrogens true specifically so learners can see and count hydrogens per carbon. Their alt text announces that hydrogens are shown but never states how many sit on each carbon, and none of the twelve molecule assets carries a long_description - the field StructureCard renders when present.

**Learner impact:** The one piece of information those figures were drawn to add over a plain skeleton - the per-carbon hydrogen count that drives equivalence, integration ratios and n + 1 - is the piece the alt text omits. A non-visual learner reading 'drawn with all five hydrogens shown' learns that hydrogens are visible to someone else.

**Evidence:** assets mol-bromoethane, mol-2-bromopropane, mol-propanal, mol-11-dichloroethane, mol-methyl-acetate: rdkit_options.show_hydrogens true, accessibility contains alt_text only; [internal source reference — not in this repo] passes longDescription to StructureCard and no molecule block supplies one.

**Recommended outcome (need):** Where a figure's teaching value is the hydrogen distribution, the non-visual text needs to carry that distribution per carbon, not merely note that hydrogens are drawn.

##### `access-007` — MEDIUM · assessment-readiness · confidence 0.78

**Location:** question_slug=`ch13-integral-reconstruction` · anchor="Assign 3 protons to the larger integral and 2 to the smaller."

**Observation:** Several hint ladders terminate in the literal answer key rather than a final nudge: ch13-integral-reconstruction L3 states both proton assignments; ch13-ethyl-quartet-builder L2 + L3 together give J about 6-8 Hz and n = 3 (the whole expected_couplings entry); ch13-delta-ppm-conversion L3 is 'Compute 2100 / 300'; ch13-j-readoff L3 plus the wrong-answer explanations disclose the 0.025 ppm spacing.

**Learner impact:** Compounded with access-001 and access-003, a learner who cannot reach the visual stimulus is left with a hint ladder as their only route - and that route hands over the answer, so the item records mastery it never measured. That converts an access barrier into a silently inflated score, which is worse for the student than a blank.

**Evidence:** feedback_bundle.hints for ch13-integral-reconstruction (L3), ch13-ethyl-quartet-builder (L2-3), ch13-delta-ppm-conversion (L3), ch13-j-readoff (L3).

**Recommended outcome (need):** The terminal hint should leave one reasoning step for the student, especially on items where the hint ladder is the only channel a non-visual learner can reach.

##### `access-008` — LOW · keyboard-operability · confidence 0.88

**Location:** question_slug=`ch13-aldehyde-peak-select` · anchor="Click the peak produced by the aldehyde proton."

**Observation:** Prompts and workspace helper text use pointer-only verbs: 'Click the peak produced by the aldehyde proton' and its v2 twin, alongside 'Click a peak to select it' and 'Pick a color, then click the hydrogens'. The underlying controls are real keyboard-operable buttons with aria-pressed, so the wording understates what the interface supports.

**Learner impact:** A keyboard-only or switch user reading an instruction to click may reasonably conclude the task requires a mouse and abandon it, even though tabbing to the peak button and pressing Enter works. This is an instruction defect, not an interaction defect.

**Evidence:** prompt_text of ch13-aldehyde-peak-select and -v2; [internal source reference — not in this repo] selectionSummary and its as='button' peak targets with _focusVisible outlines; [internal source reference — not in this repo] helper text.

**Recommended outcome (need):** Task wording should be device-neutral ('select') so the instruction matches the keyboard-complete controls that are actually shipped.

##### `access-009` — LOW · media-equivalence · confidence 0.72

**Location:** question_slug=`ch13-aldehyde-peak-select-v2` · anchor="A three-peak proton spectrum of a four-carbon ester, with peaks near 4.1, 2.0, and 1.2 ppm"

**Observation:** SpectrumPeakRenderer labels each peak button 'Peak at 4.1 ppm' and never announces the peak's plotted intensity, though the authored intensities encode relative size (0.55/0.8/0.9 here; 0.4/0.7/0.9 in the aldehyde item, where the small aldehyde peak against tall alkyl peaks is itself a teaching cue).

**Learner impact:** Relative peak height is stimulus information present visually and absent from the accessible name. It does not change the answer for either item, since both are decided by position alone, but a non-visual learner reads a flat list of shifts and loses the height/integration cue their classmates use as a cross-check.

**Evidence:** [internal source reference — not in this repo] aria-label={`Peak at ${peak.label}`}; student_config.spectrum.peaks intensities in both items.

**Recommended outcome (need):** Where plotted peak height carries meaning, the accessible name for each peak target should convey relative size along with position - and no spectrum_peaks item whose answer depends on height should ship until it does.

**Open questions**

- I used the existing category assessment-readiness for access-007 (hint ladders terminating in the answer key). No category covers hint-channel leakage; alt-text-quality is scoped to descriptions. If hint leakage recurs, the rubric may want its own id.
- The /assets/nmr/ asset schema has an accessibility.table_rows field that is [] in both integral traces and no code reads it. Was it intended as the non-visual peak table for trace-backed questions? If so it is the natural home for a leak-free text equivalent.
- Is any surface other than QuestionTypeDemoPage meant to display accessible_description? Every question here is demo_eligible false, so I could not find a path by which a student reaches it.
- ch13-j-readoff/-v2 declare a spectrum under a workspace 'none' type. Was a prompt-stimulus slot expected to render it, or was the spectrum meant to be replaced by an inline text line list in the prompt? The answer determines whether access-001 is a rendering gap or an authoring gap.
- PeakAssignmentRenderer offers the ester/ketone oxygen as an assignment target in a 13C question. Whether the option list should also be filtered to carbons is a chemistry/UX call I left to the instructor persona.

#### Learner with Visual Preference — 6.0/10

This chapter is unusually visual for the platform: all 17 authored assets survive compilation into reader blocks (12 molecule blocks, 4 nmr_spectrum teaching_asset blocks, 1 diagram image - no silent asset drop), the splitting-tree SVG is correct and carries its J labels, three interactive widgets are placed, and the two 60 MHz spectra genuinely resolve their multiplets. The problems are concentrated in whether the drawn spectra show what their captions claim. Simulating the shipped trace builder (LINEWIDTH_PPM = 0.008 half-width, 600 samples across the authored window) shows the methyl acrylate figure renders two of its three vinyl signals as plain doublets rather than the doublets of doublets its learning goal, alt text and prose all assert - the 1.5 Hz geminal coupling is 0.005 ppm at 300 MHz, below both the linewidth and the sample step. The same asset labels its terminal vinyl protons with inverted geometry relative to the ester. Compounding this, neither the live canvas nor the SVG exporter draws peak labels or region labels at all, so every spectrum reaches the eye as an unlabeled blue trace with a ppm axis and, in two cases, unexplained green blocks. Separately, the deliberate 60-vs-300 MHz comparison is split across two sections despite its caption saying 'beside it', and the three concepts most dependent on a picture - the shift-region map, integration drawn as an integral step, and DEPT's phasing - have no figure anywhere, while the question bank ships the 13C spectrum the chapter body never shows.

**Publication blockers:** `visual-001`

**Strengths**

- No asset is silently dropped: all 17 authored assets reach the reader - 12 molecule blocks, all 4 nmr_spectrum assets as teaching_asset blocks, and the diagram as an image block whose SVG file exists on disk.
- The 60 MHz teaching spectra are correctly scaled for what they teach. Simulating the shipped builder, nmr-spec-bromoethane-60mhz resolves all seven lines with 3.04% of plot width per line spacing - the field strength was chosen against the splitting rather than for realism.
- The 300 MHz bromoethane figure is deliberately and correctly illegible: it renders as two narrow clusters, which is exactly the point its caption makes about ppm compression. This is the rare case of a figure whose unreadability is the content.
- The splitting-tree SVG is chemically correct and is the only figure in the chapter that labels its own numbers - it carries the J values and 'dd - 1 : 1 : 1 : 1' as drawn text, and is built deterministically by an svg_builder with ai_regeneration_allowed false.
- Structural and spectral data across the 12 molecule assets check out against literature values.
- The question bank uses a zoomed window where the chapter does not: ch13-j-readoff draws the bromoethane CH2 multiplet over 3.37-3.51 ppm with 1:3:3:1 intensities, exactly the treatment nmr-spec-methyl-acrylate-vinyl needed.
- No selected-response item illustrates only some of its options - both attach a structure to every option, so no picture acts as an answer tell.
- The spectra's long_descriptions are unusually rigorous and quantitative - where they disagree with the render, it is the render that is wrong.

**Findings**

##### `visual-001` — BLOCKER · figure-accuracy · confidence 0.93

**Location:** section_id=`nugget-coupling-constants` · nugget_id=`nugget-coupling-constants` · concept_slug=`spin-spin-splitting` · asset_id=`nmr-spec-methyl-acrylate-vinyl` · anchor="Each vinyl proton couples to two inequivalent neighbours, so every one is a doublet of doublets"

**Observation:** The methyl acrylate spectrum is authored at 300 MHz over a 3.0-7.0 ppm window (4 ppm). Only one of its three vinyl signals actually renders as four lines. Two of the three render as two-line doublets, so the figure shows the opposite of the point it is captioned with.

**Learner impact:** A learner comparing the picture with the caption sees two two-line signals labelled as doublets of doublets. The chapter has just taught that 'unequal intensities in a four-line multiplet are the tell that you are looking at a dd rather than a quartet' - the figure meant to make that concrete instead shows what looks like three simple doublets. It also makes the intended exercise (match the three J values across their two partners) impossible from the image.

**Evidence:** Replaying the shipped builder ([internal source reference — not in this repo]: LINEWIDTH_PPM = 0.008 ppm half-width, SAMPLES = 600) on the authored spec: sample step across the 4 ppm window is 0.00668 ppm; J = 1.5 Hz at 300 MHz is 0.0050 ppm, below both the linewidth and one sample step. Simulated local maxima: 6.40 peak gives 2 maxima (6.372, 6.426); 5.82 peak gives 2 maxima (5.805, 5.838); only 6.12 (17.3 + 10.4 Hz) gives 4. In the 480 px SVG export the 1.5 Hz splitting is 0.57 px, 0.12% of the plot width.

**Recommended outcome (need):** The chapter needs a rendering of the methyl acrylate vinyl region in which the 1.5 Hz geminal splitting is actually separable - the drawn window and field strength must be chosen against the smallest coupling the figure claims to show, exactly as the 60 MHz figures already do. If that resolution is not achievable, the caption, learning goal and alt text must describe what the picture really contains.

##### `visual-002` — HIGH · figure-accuracy · confidence 0.86

**Location:** section_id=`nugget-coupling-constants` · nugget_id=`nugget-coupling-constants` · asset_id=`nmr-spec-methyl-acrylate-vinyl` · anchor="=CH₂ (trans to ester)"

**Observation:** The two terminal vinyl protons of methyl acrylate are labelled with inverted geometry relative to the ester group. The 6.40 peak (J = 17.3 Hz) is labelled '=CH2 (trans to ester)' and the 5.82 peak (J = 10.4 Hz) '=CH2 (cis to ester)'. A 17.3 Hz coupling is the trans relationship to the internal =CH- proton; because that carbon also bears the ester, the proton trans to the vinyl H is cis to the ester, and vice versa.

**Learner impact:** The figure's own long_description correctly says '17.3 Hz links the two protons trans across the double bond', so a learner reading label and description together receives two mutually contradictory geometric claims about the same proton. In a section whose stated diagnostic value is that a single measured coupling assigns alkene geometry, an inverted label undermines the exact inference being taught.

**Evidence:** asset peaks[0].label with couplings 17.3 and 1.5; peaks[2].label with couplings 10.4 and 1.5. The shifts and J values match literature; only the geometric descriptor is inverted.

**Recommended outcome (need):** Each terminal vinyl proton needs a label whose stated geometry is unambiguous and correct - either named by the partner it couples to (as the long_description and ch13-dd-builder already phrase it) or by the ester with the relationship corrected. The two phrasings must not disagree across the same asset.

##### `visual-003` — HIGH · figure-purpose · confidence 0.95

**Location:** section_id=`nugget-splitting` · nugget_id=`nugget-splitting` · asset_id=`nmr-spec-bromoethane-60mhz` · anchor="Bromoethane at 60 MHz: the ethyl quartet-plus-triplet"

**Observation:** Every peak label and every integration-region label authored on the four nmr_spectrum assets is dropped by both renderers. The reader draws an unlabeled blue trace with a ppm axis; the two spectra that carry regions draw them as green rectangles with no text. So '-CH2Br', '-CHCl2', '=CH-', '-OCH3', '3H', '2H' and '1H' never reach the eye.

**Learner impact:** The learner cannot tell which drawn signal is which without leaving the figure and re-reading the description above it, which is precisely the explanation burden a labelled spectrum exists to remove. The methyl acrylate figure is worst affected - four signals, none identified. The two green blocks are the chapter's only visible representation of integration and carry no number, so they read as decoration rather than a proton count.

**Evidence:** [internal source reference — not in this repo] draws regions as rect fill only and never renders r.label (declared on SpectrumRegion); it draws no per-peak text. buildNmrSpectrumFigureSvg likewise emits only integer ppm ticks, region rects, markers and the trace path. peak.label is consumed only by describeSpectrum(), which the reader overrides with the asset's alt_text.

**Recommended outcome (need):** The assignments and proton counts the author already wrote need to be visible on the figure itself, adjacent to the signal they describe - the information exists in the package and currently reaches only the text channel, which inverts the usual gap and leaves the sighted reader with less than the screen-reader user.

##### `visual-004` — HIGH · figure-purpose · confidence 0.9

**Location:** section_id=`nugget-coupling-constants` · nugget_id=`nugget-coupling-constants` · asset_id=`nmr-spec-bromoethane-j` · anchor="This is the same spectrum as the 60 MHz one beside it."

**Observation:** The 60 MHz and 300 MHz bromoethane spectra are authored as a controlled comparison but compile into two different reader sections, separated by roughly 3,000 characters of prose, a second spectrum, a diagram and two callouts. The caption's claim that the partner sits 'beside it' is false on screen. The two also differ in a second variable: the 300 MHz spec carries integration regions, the 60 MHz spec does not.

**Learner impact:** The entire value of the pair is that a learner sees one variable change. Split across sections, the comparison becomes an act of memory rather than of looking. The extra green shading on one member introduces a visible difference unrelated to field strength, inviting the inference that high-field spectra are the ones that get integrated.

**Evidence:** Compiled reader: blk-d82aaf75 (60 MHz) is in nugget-splitting; blk-952ba88e (300 MHz) is in nugget-coupling-constants. nmr-spec-bromoethane-j has regions [1.5-1.9 '3H', 3.25-3.62 '2H']; nmr-spec-bromoethane-60mhz has no regions key.

**Recommended outcome (need):** The field-strength comparison needs the two renderings visible together at the moment the prose makes the argument, and the two members must differ only in field strength. Note the reader also carries an interactive spectrum simulator in the same section - the three deliveries of one idea should be consolidated rather than multiplied.

##### `visual-005` — MEDIUM · visual-opportunity · confidence 0.85

**Location:** section_id=`nugget-shifts-integration` · nugget_id=`nugget-shifts-integration` · concept_slug=`h1-shifts-and-integration` · anchor="Vinylic protons therefore absorb at δ 4.5–6.5, and aromatic protons"

**Observation:** Seven numeric shift regions are delivered as two dense prose paragraphs with no figure. The section's only figures are two molecular structures. The upfield/downfield orientation of the axis - which the chapter itself flags as a common error - is likewise described only in words.

**Learner impact:** Shift regions are the one piece of NMR content a learner consults repeatedly while working problems, and reading them out of running prose forces re-parsing every time. Because the regions are contiguous bands on a single axis, prose has to spend a sentence per band to convey what position on one line conveys directly. The 'reversing the direction of the scale' misconception is called out in a warning callout but never contradicted by anything the learner can look at.

**Evidence:** Compiled section nugget-shifts-integration: one text block (2,306 chars), one warning callout, two molecule blocks, one tip callout, one link. The question bank leans on the same regions three times, all text-only.

**Recommended outcome (need):** The learner needs the shift regions available as a single spatial reference keyed to the same inverted delta axis the spectra use, so that downfield and upfield are positions rather than vocabulary.

##### `visual-006` — MEDIUM · visual-opportunity · confidence 0.87

**Location:** section_id=`nugget-c13-dept` · nugget_id=`nugget-c13-dept` · concept_slug=`c13-nmr-and-dept` · anchor="A DEPT-135 experiment phases CH₃ and CH carbons positive and CH₂ carbons negative"

**Observation:** The 13C and DEPT section contains no spectrum of any kind - its only figures are two molecular structures already used earlier in the chapter. DEPT's defining behaviour is a phase pattern (up, down, absent), a purely visual distinction, conveyed only by the words 'positive', 'negative' and 'vanish entirely'. Meanwhile the compiled question bank does ship a drawn 13C spectrum of butan-2-one.

**Learner impact:** A learner meets a real 13C spectrum for the first time in an assessment item rather than in the chapter, so the first time the twenty-fold wider 0-220 ppm axis and the isolated carbonyl line are seen is while being graded. 'Reading a decoupled spectrum beside its DEPT companion' is described as the technique's whole payoff, and there is nothing to read beside anything.

**Evidence:** Compiled section blocks: text, warning callout, mol-butan-2-one, mol-p-xylene, tip callout, external link - no teaching_asset or image. All four nmr_spectrum assets are nucleus '1H'. compiled/question-set.json ch13-c13-peak-assignment carries a drawn nmr_13c spectrum with peaks at 209, 37, 29, 8.

**Recommended outcome (need):** The carbon chapter needs its skeleton claim made visible - that four environments give four lines, that the carbonyl sits alone far downfield, and that DEPT sorts those lines by attached-hydrogen count.

##### `visual-007` — MEDIUM · visual-opportunity · confidence 0.88

**Location:** section_id=`nugget-shifts-integration` · nugget_id=`nugget-shifts-integration` · concept_slug=`h1-shifts-and-integration` · anchor="drawn on the spectrum as an integral step"

**Observation:** The chapter tells the learner that intensity is 'drawn on the spectrum as an integral step', but no figure in the chapter draws one. The integration concept section has no spectrum at all, and the only two spectra carrying integration data render their regions as unlabeled green rectangles in two different, later sections.

**Learner impact:** Integration is introduced as something the learner will see on a printed spectrum, and then it is never seen. A learner arriving at ch13-integral-reconstruction, which asks them to mark integral regions on a trace, has had no prior visual model of what an integral region looks like or what its label means.

**Evidence:** Section nugget-shifts-integration contains no teaching_asset or image block. regions appear only on nmr-spec-bromoethane-j and nmr-spec-11-dichloroethane-j, and GenericSpectrumCanvas draws them without their labels. The prose's 3:1 example appears only as a structure.

**Recommended outcome (need):** The learner needs at least one spectrum in which signal size is visibly tied to a proton count, placed where integration is taught.

##### `visual-008` — MEDIUM · figure-purpose · confidence 0.84

**Location:** section_id=`nugget-nmr-theory` · nugget_id=`nugget-nmr-theory` · concept_slug=`nmr-theory-basics` · anchor="Change the number of neighboring protons and watch where the intensity ratios of a multiplet come from."

**Observation:** The interactive figure placed at the end of the opening theory section is the spin-arrangement/Pascal-ratio widget: it lets the learner vary the number of equivalent neighbouring protons and reports 'n neighbors give n + 1 lines'. The section it sits in is about the two Zeeman orientations of a single nucleus, the field-dependent energy gap and the resonance condition - a different sense of 'spin state'. Splitting and the n + 1 rule are not introduced until three sections later.

**Learner impact:** The one thing a learner can manipulate in the theory section answers a question they have not been asked, using vocabulary that has not been defined, while pre-empting the discovery nugget-splitting is built around. Meanwhile the section's real visual need - two energy levels whose separation grows with field - is left unmet, and the presence of an 'Interactive figure' panel makes that gap look filled.

**Evidence:** [internal source reference — not in this repo] places widgetKind 'nmr_spin_state' on sectionId 'nugget-nmr-theory' with preset {n: 2}; ReaderSpinStateWidget renders buildSpinStateDiagramSvg(n). The section's video brief, which storyboards the two energy shelves and the widening gap, is deferred and compiles hidden.

**Recommended outcome (need):** The opening section needs the two-orientation energy picture its prose spends a paragraph on. A static labelled sequence would carry this; the deferred animation is not a prerequisite. The Pascal-ratio interactive belongs where splitting is taught, not before it.

##### `visual-009` — MEDIUM · visual-opportunity · confidence 0.86

**Location:** section_id=`nugget-structure-determination` · nugget_id=`nugget-structure-determination` · concept_slug=`nmr-structure-determination` · anchor="Identical formulas, identical multiplicity lists, but the shift of one quartet decides the connectivity."

**Observation:** The chapter's closing payoff - that ethyl acetate and methyl propanoate are separated by where one quartet sits - is delivered as two molecular structures and a sentence. Neither spectrum is drawn, so the single distinguishing observation (4.1 versus 2.3 ppm) is never shown.

**Learner impact:** This is the moment the chapter's four tools are supposed to combine into a decision, and the decision is made in prose. A learner is asked in the check-yourself card and again in ch13-isomer-reasoning to choose between two isomers on the basis of one shift, having never seen the two spectra differ.

**Evidence:** Compiled section blocks: text, warning callout, mol-ethyl-acetate, mol-methyl-propanoate, tip callout, external link. The tip callout supplies the discriminating shift list in text only. No nmr_spectrum asset targets this concept.

**Recommended outcome (need):** The learner needs the two isomers' spectra placed against each other so the quartet visibly moves, since 'the shift of one quartet decides the connectivity' is a statement about position on an axis.

##### `visual-010` — MEDIUM · figure-purpose · confidence 0.82

**Location:** section_id=`nugget-equivalence` · nugget_id=`nugget-equivalence` · asset_id=`mol-cyclohexane` · anchor="p-Xylene condenses ten hydrogens into two signals"

**Observation:** The three structures carrying the signal-counting section display hydrogens inconsistently and mark no environments. 2-Bromopropane is drawn with explicit hydrogens; p-xylene and cyclohexane have no rdkit_options and are drawn as a plain ring and a bare hexagon. Cyclohexane's caption says 'twelve equivalent hydrogens in one line' over a figure showing none of them.

**Learner impact:** The section's whole skill is partitioning drawn hydrogens into equivalence sets, and two of the three worked structures show no hydrogens to partition while the third shows all of them - so the learner cannot practise the operation on the figures, and cannot verify the counts the captions assert.

**Evidence:** mol-2-bromopropane has rdkit_options {show_hydrogens: true}; mol-p-xylene and mol-cyclohexane have no rdkit_options block. All three compile into section nugget-equivalence.

**Recommended outcome (need):** Within one comparison set the hydrogen-display convention needs to be uniform, and the equivalence sets the captions count need to be distinguishable on the structure itself.

##### `visual-011` — MEDIUM · visual-opportunity · confidence 0.9

**Location:** question_slug=`ch13-single-signal-molecule` · concept_slug=`proton-equivalence-signal-counting` · anchor="Which of these C₆ compounds shows only ONE signal in its ¹H NMR spectrum?"

**Observation:** Two selected-response items author a structure_smiles on every option, but no renderer reads that key - SelectedResponseRenderer draws only option.text and option.imageUrl, and SelectedResponseOption declares no structure field. The questions therefore present as lists of compound names.

**Learner impact:** A symmetry judgement is being assessed without a structure to inspect, so the item silently converts from 'look at these four skeletons and find the symmetric one' into 'recall the connectivity of four named C6 compounds, then judge symmetry'. That is a harder and different task, and it removes the visual reasoning step the chapter spent a whole section building.

**Evidence:** ch13-single-signal-molecule options a-d each carry structure_smiles; ch13-isomer-reasoning claim options carry structures. [internal source reference — not in this repo] renders only imageUrl and text; grep shows structure_smiles is read nowhere under frontend/src except the question-bank editor.

**Recommended outcome (need):** The structures the author attached need to reach the learner, or the items need re-scoping as recall questions. The option treatment is uniform, so there is no answer tell - the loss is of visual reasoning, not of fairness.

##### `visual-012` — LOW · figure-accuracy · confidence 0.72

**Location:** section_id=`nugget-splitting` · nugget_id=`nugget-splitting` · asset_id=`nmr-spec-11-dichloroethane-j` · anchor="recorded at 60 MHz so both splitting patterns are wide enough to read"

**Observation:** The 1,1-dichloroethane spectrum resolves correctly, but it is drawn over the widest window in the chapter (1.0-6.8 ppm) for the smallest coupling of the three 60 MHz figures (6.0 Hz). Its line spacing is 1.72% of the plot width against 3.04% for the bromoethane 60 MHz figure, and the drawn intensity of the quartet's outer lines falls to about 27% of the inner lines rather than the 33% the description states.

**Learner impact:** The doublet and quartet are readable but at the chapter's tightest margin, and the outer quartet lines are faint enough that a learner counting lines may see three rather than four - the exact count the figure exists to support.

**Evidence:** Replaying the builder: sample step 0.00968 ppm across the 5.8 ppm window; simulated maxima 2.007/2.114 and 5.745/5.841/5.938/6.045 with normalized heights 0.098/0.369/0.363/0.096. At 480 px, 6.0 Hz = 7.86 px versus 13.87 px for bromoethane.

**Recommended outcome (need):** The drawn window should be chosen against the multiplet the figure is teaching rather than the full shift range of the molecule.

##### `visual-013` — LOW · figure-accuracy · confidence 0.83

**Location:** section_id=`nugget-coupling-constants` · nugget_id=`nugget-coupling-constants` · asset_id=`nmr-spec-bromoethane-j` · anchor="each multiplet spans only about 0.05 ppm rather than 0.25 ppm"

**Observation:** The 300 MHz bromoethane description gives one multiplet width for both signals. The figure holds for the triplet (0.049 ppm at 300 MHz, 0.243 at 60 MHz) but not for the quartet, which spans 0.073 and 0.365 ppm respectively - about 50% wider than stated.

**Learner impact:** A learner who takes the description as a measurement and checks it against the drawn quartet finds it does not match, weakening confidence in a figure whose only job is to make a numerical argument about width.

**Evidence:** Computed from the authored spec: triplet = 2 x 7.3/300 = 0.0487 ppm; quartet = 3 x 7.3/300 = 0.0730 ppm.

**Recommended outcome (need):** The stated widths need to distinguish the two multiplets, or be phrased as a ratio rather than two absolute numbers applied to 'each multiplet'.

##### `visual-014` — LOW · figure-accuracy · confidence 0.8

**Location:** question_slug=`ch13-j-readoff` · concept_slug=`spin-spin-splitting` · anchor="The spectrum below shows the CH₂ multiplet of bromoethane recorded at 300 MHz"

**Observation:** The zoomed bromoethane multiplet drawn in the J read-off question places its lines 0.025 ppm apart, which at 300 MHz reads as exactly 7.5 Hz, and the answer key is 7.5 Hz. Every other appearance of bromoethane in the chapter states J = 7.3 Hz.

**Learner impact:** A learner who measures the drawn figure and checks it against the chapter's own figure of the same molecule gets two different numbers for one coupling, in a section whose central claim is that a coupling constant is a fixed property.

**Evidence:** ch13-j-readoff spectrum peaks at 3.400/3.425/3.450/3.475 ppm, answer_key value 7.5; both spectrum assets and mol-bromoethane use 7.3.

**Recommended outcome (need):** The drawn line positions for a molecule the chapter has already characterised should reproduce the chapter's own coupling constant.

##### `visual-015` — LOW · figure-purpose · confidence 0.75

**Location:** section_id=`nugget-splitting` · nugget_id=`nugget-splitting` · anchor="Bromoethane displays the most important pattern in the chapter."

**Observation:** Each section compiles as a single undivided prose block followed by a callout and then the whole figure stack, so no figure is adjacent to the sentence it supports. In nugget-splitting the sentence naming bromoethane as the chapter's most important pattern is followed by roughly half the section's prose and a warning callout before the bromoethane structure and spectrum appear.

**Learner impact:** Connecting a claim to its picture becomes a scroll-and-search operation repeated for every figure. In a chapter where the argument is almost always 'this molecule produces this pattern', the cost falls exactly on the pairing the chapter is built from.

**Evidence:** Compiled reader: every section holds exactly one text block (2,085-4,279 chars) emitted before all callouts, molecules, teaching_assets and images.

**Recommended outcome (need):** The learner needs figures to arrive at the point in the prose where the claim is made rather than batched after it; if the compiler's fixed block order is the constraint, the prose needs to be authored in blocks that let figures land between them.

**Open questions**

- Peak and region labels authored on nmr_spectrum assets currently reach no rendering surface. Is the intent that the reader eventually draws them, or that the asset labels serve only downstream consumers? The answer decides whether visual-002's inverted geometry label is a display defect today or a latent one.
- The renderer's fixed LINEWIDTH_PPM = 0.008 ppm half-width sets a hard floor: at 300 MHz no coupling below roughly 4-5 Hz can resolve at any window width. Is that a documented authoring constraint, and should the compiler warn when an authored jHz falls below it for the chosen field?
- Three surfaces now deliver the field-strength comparison (the two static bromoethane spectra plus the simulator widget). Since the widget is exportPolicy 'exclude', is the 300 MHz static twin retained deliberately for the export path?
- I used no category outside the schema's list. visual-008 and visual-015 are reported under figure-purpose because they concern a figure's placement and fitness rather than its content; they also carry a sequencing flavour another persona may categorise differently.

### Orchestrator decisions

#### `rec-001` — Two adjacent sentences invert the dd geometry and the dd/quartet intensity test (blocker)

- **Need:** Students need a correct, checkable procedure for reading both couplings off a doublet of doublets, and a single self-consistent intensity test for telling a dd from a quartet.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** Both are wrong chemistry in the tier the reader renders by default, and both are single-sentence fixes. The correct statements are already present elsewhere in the chapter - the splitting-tree SVG says 'dd - 1 : 1 : 1 : 1' and the sentence immediately preceding the second error says 'four lines of equal intensity' - so the fix is to make the prose agree with the chapter's own figure rather than to author anything new.
- **Consolidates:** `instr-001`, `instr-002`

#### `rec-002` — Methyl acrylate's terminal vinyl protons are labelled with swapped geometry (blocker)

- **Need:** Each terminal proton's label must state a geometric relationship the reader can verify from the coupling shown, and must agree with the asset's own long description and with ch13-dd-builder.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** Corrected in place by relabelling the two peaks - no new asset. Naming each proton by its relationship to the internal =CH- (the convention the long_description and the question already use) removes the ambiguity entirely, because that is the partner the J value actually reports on.
- **Consolidates:** `instr-003`, `visual-002`

#### `rec-003` — Four numeric items crash the grader (blocker)

- **Need:** Every answer key must round-trip through its own grader before the set is assigned.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** A one-line shape change per item: `tolerance` must be the {mode, amount} object [internal source reference — not in this repo] reads, not a bare float. Confirmed by execution that all four currently raise AttributeError while the two items without a tolerance key grade normally. This is the chapter's only quantitative assessment.
- **Consolidates:** `instr-004`

#### `rec-004` — The J-readoff items are unanswerable by anyone (blocker)

- **Need:** The line positions these items are graded on must be present in a form every learner can read.
- **Chosen intervention:** `text-equivalent` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** The positions currently exist only inside a spectrum config that no surface renders, because numeric_with_units declares workspace 'none'. Putting the ordered line list into the prompt text delivers the stimulus to every learner on every surface without depending on a renderer change, and simultaneously closes the non-visual gap.
- **Consolidates:** `access-001`

#### `rec-005` — The integral-reconstruction trace announces its own answer (blocker)

- **Need:** The trace's text equivalent must convey where signals lie and that they differ in area, without stating the proton counts or region boundaries being graded.
- **Chosen intervention:** `text-equivalent` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** The leak is in an externally referenced /assets/nmr/ asset, which the compile-time guard never inspects - so it must be corrected at the asset and cannot be caught by the build. Rewriting the two description strings is bounded and restores the item for both cohorts.
- **Consolidates:** `access-003`

#### `rec-006` — 13C peak assignment offers unidentifiable atom labels (blocker)

- **Need:** The atom identifiers a student chooses between need an unambiguous non-visual identity that matches what the figure shows.
- **Chosen intervention:** `structured-chemical-description` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** The renderer labels choices C1..C5 from RDKit index order while drawing no atom numbers, and the type declares requires_molecule_description=True with none supplied. Authoring that description - each numbered position named by what it is bonded to - is the chapter-side fix and needs no renderer change; filtering oxygens out of the candidate list remains a platform question.
- **Consolidates:** `access-002`, `access-005`

#### `rec-007` — Bromoethane's coupling constant is three different numbers (high)

- **Need:** One bromoethane J must be true everywhere - prose, both spectrum figures and both read-off questions - with plotted line positions chosen so the arithmetic a student does returns exactly that number.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** The chapter teaches that coupled partners share one J and then quotes 7.3, 7.5 and 7.2 Hz for the same ethyl group, plus an arithmetic slip (0.024 x 300 = 7.2, printed as 7.3). Aligning the drawn line positions to the taught 7.3 Hz makes the measurement reproduce the text, which is the whole point of the exercise.
- **Consolidates:** `instr-005`, `visual-014`

#### `rec-008` — The n + 1 rule is taught with no exchange exception (high)

- **Need:** Students need to know that OH and NH protons normally appear unsplit, broad and variable, why, and how to confirm one experimentally.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** Alcohols are the most common functional group students meet in an introductory spectrum, and exchange is the most common way a correctly applied n + 1 rule gives a wrong prediction. The chapter's own hedge in the propan-1-ol question ('consider only the carbon-bound hydrogens') shows the authors knew the gap existed. A short paragraph closes it.
- **Consolidates:** `instr-006`

#### `rec-009` — The capstone method's first step is undefined and its payoff is undrawn (high)

- **Need:** Degrees of unsaturation must be executable inside this chapter, and the spectrum-to-structure inventory needs to be demonstrated once on a displayed spectrum.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The section opens by instructing students to compute degrees of unsaturation and never states the formula; its declared prerequisite concept does not exist in this package. Stating the computation and working it on one of the chapter's own formulas is bounded. The larger need - a full worked pass on a visible trace - is authoring scope and is carried under visual opportunities.
- **Consolidates:** `stud-001`, `stud-002`, `visual-009`

#### `rec-010` — Anisotropy contradicts the shielding rule with nothing to reconcile them (high)

- **Need:** The opposes-versus-reinforces reversal must be reconciled where it is introduced, tied to where the proton sits relative to the circulating pi electrons.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** Section 2 says the induced field opposes the applied field; section 4 says it reinforces it, in a single clause with no explanation. A student cannot tell which is the rule and defaults to memorising 'aromatic is about 7'. One or two sentences make anisotropy a consequence of the shielding rule rather than an exception to it.
- **Consolidates:** `stud-003`

#### `rec-011` — The coupling-constants section is overloaded and its warnings are duplicated (high)

- **Need:** This section needs to be digestible, and its named-mistakes callout needs to name this section's own traps rather than repeating the previous section's.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** At 761 words against a ~350-word chapter average it carries eleven ideas in one unbroken block; and because both it and nugget-splitting map to the same concept slug, the trouble_spots callout renders byte-identically twice, so the dd-versus-quartet trap and the geminal-J caveat are never flagged. Adding this section's own trouble spots is the smaller half of the fix and is applied; splitting the section is authoring scope.
- **Consolidates:** `stud-004`, `stud-005`, `stud-011`

#### `rec-012` — Hint ladders that terminate in the answer key (high)

- **Need:** The terminal hint must leave one reasoning step for the student, and the J tolerance students are graded against must match the precision the prompt asks for.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** Four ladders hand over the graded value, which matters doubly here because on the items with unrenderable stimuli the ladder is the only reachable channel - converting an access barrier into a silently inflated score. Separately, items asking for 'a typical J' grade against a literature value inside a 0.3 Hz window, so a student using the chapter's own table scores 0.6.
- **Consolidates:** `access-007`, `instr-009`

#### `rec-013` — The dead spin-state video card (high)

- **Need:** The page must not advertise a visual that does not exist.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The brief is production_status 'deferred' with a production_note saying the prose already carries the content, but the deferral did not suppress the block - so the reader renders a 'Watch' link to an empty URL with a storyboard fragment as its description. Marking it hidden, as the deferred videos in every other chapter are, removes the dead link with no content change.
- **Consolidates:** `stud-006`

#### `rec-014` — The correlation charts are prose, and the spectra carry no visible labels (high)

- **Need:** The 1H and 13C shift regions need a scannable form keyed to the delta axis, and the peak and integration labels already authored on the spectra need to be visible on the figures.
- **Chosen intervention:** `longer-description` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The chart is the artefact students keep open for the rest of the course, and the chapter proves in section 6 that the reader renders pipe tables correctly - so converting the region lists to tables is available now and is applied. Drawing peak labels on the trace is a renderer change (GenericSpectrumCanvas never renders r.label), so it is recorded as platform work rather than attempted here.
- **Consolidates:** `instr-008`, `stud-007`, `visual-003`, `visual-005`

#### `rec-015` — The 13C/DEPT section shows no spectrum (high)

- **Need:** Students need to see a decoupled 13C spectrum on its 0-220 ppm axis together with the DEPT companion that phases its lines.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** DEPT's defining behaviour is a phase pattern - up, down, absent - which prose cannot carry, and the section's only figures are two structures already used earlier. The nmr_spectrum asset type already supports a 13C nucleus and the question bank already ships a drawn 13C spectrum, so the capability exists. Deferred as authoring scope.
- **Consolidates:** `instr-011`, `visual-006`, `stud-017`

#### `rec-016` — Methyl acrylate cannot render the splitting it claims (high)

- **Need:** The drawn window and field strength must be chosen against the smallest coupling the figure claims to show.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** The 1.5 Hz geminal coupling is 0.005 ppm at 300 MHz, below both the renderer's fixed 0.008 ppm linewidth and one sample step across the authored 4 ppm window, so two of three vinyl signals render as plain doublets. The chapter's own 60 MHz figures and its own ch13-j-readoff question already demonstrate the right treatment. Deferred because it needs a re-authored window or field, not a text fix.
- **Consolidates:** `visual-001`, `instr-012`

#### `rec-017` — Three objectives are assessed by nothing, and the capstone is a two-option pick (high)

- **Need:** DEPT classification, selective decoupling and structure construction each need an item that requires the skill they name.
- **Chosen intervention:** `added-practice` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** The DEPT objective is never assessed (the one 13C item hands the student the DEPT result); decoupling is graded at 'advanced' difficulty from a single subordinate clause of coverage; and the capstone reduces to a 50% pick between two named isomers with no construction item anywhere. Deferred as authoring scope.
- **Consolidates:** `instr-007`, `instr-010`, `stud-014`

#### `rec-018` — The authored accessibility layer reaches no student (high)

- **Need:** Every question with a visual stimulus needs its authored text equivalent presented on the surfaces this chapter ships to.
- **Chosen intervention:** `instructor-note` → target surface `instructor-support`
- **Why this is the least-complex option that fully addresses the need:** Not fixable in the package: accessible_description is consumed by exactly three places, none of which is a surface this chapter's 15 question types reach, and every question here is demo_eligible false. Recorded for the platform backlog - and it is why the corrected descriptions in rec-004/005/006 cannot be verified in-product.
- **Consolidates:** `access-004`, `visual-011`

#### `rec-019` — The figure/prose pairing and widget placement (medium)

- **Need:** Figures need to arrive where the claim is made, the 60/300 MHz pair needs to be adjacent, and the Pascal-ratio widget belongs where splitting is taught.
- **Chosen intervention:** `prose-edit` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** The 300 MHz caption tells the reader to compare with a figure 'beside it' that sits in the previous section - a false cross-reference, which is corrected here. The widget placement and the compiler's fixed block order (all figures batched after all prose) are structural and are recorded rather than changed.
- **Consolidates:** `stud-012`, `visual-004`, `visual-008`, `visual-015`

#### `rec-020` — Polish: self-checks that print their answers, undifferentiated multiplet widths, missing per-carbon hydrogen counts (medium)

- **Need:** Self-checks should require an attempt; the 300 MHz description should give each multiplet's own width; and alt text on hydrogen-showing figures should state the per-carbon counts.
- **Chosen intervention:** `sufficient-alt-text` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** The multiplet-width and alt-text items are exact, bounded corrections and are applied. The reveal-on-attempt behaviour for practice_check callouts is a platform-wide compiler pattern affecting every chapter, so it is recorded rather than worked around here.
- **Consolidates:** `stud-009`, `instr-013`, `visual-013`, `access-006`, `stud-016`, `stud-010`, `stud-013`, `stud-015`, `instr-014`, `instr-015`, `visual-010`, `visual-012`, `access-008`, `access-009`

### Merged duplicates

- **Methyl acrylate's terminal vinyl protons are labelled with swapped geometry** (`rec-002`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-003`; Learner with Visual Preference `visual-002`. Kept at the strongest severity (`blocker`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Bromoethane's coupling constant is three different numbers** (`rec-007`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-005`; Learner with Visual Preference `visual-014`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The capstone method's first step is undefined and its payoff is undrawn** (`rec-009`) — raised independently by 2 personas: Struggling Student `stud-001`, `stud-002`; Learner with Visual Preference `visual-009`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Hint ladders that terminate in the answer key** (`rec-012`) — raised independently by 2 personas: Accessibility Persona `access-007`; Organic Chemistry Instructor `instr-009`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The correlation charts are prose, and the spectra carry no visible labels** (`rec-014`) — raised independently by 3 personas: Organic Chemistry Instructor `instr-008`; Struggling Student `stud-007`; Learner with Visual Preference `visual-003`, `visual-005`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The 13C/DEPT section shows no spectrum** (`rec-015`) — raised independently by 3 personas: Organic Chemistry Instructor `instr-011`; Learner with Visual Preference `visual-006`; Struggling Student `stud-017`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Methyl acrylate cannot render the splitting it claims** (`rec-016`) — raised independently by 2 personas: Learner with Visual Preference `visual-001`; Organic Chemistry Instructor `instr-012`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Three objectives are assessed by nothing, and the capstone is a two-option pick** (`rec-017`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-007`, `instr-010`; Struggling Student `stud-014`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The authored accessibility layer reaches no student** (`rec-018`) — raised independently by 2 personas: Accessibility Persona `access-004`; Learner with Visual Preference `visual-011`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The figure/prose pairing and widget placement** (`rec-019`) — raised independently by 2 personas: Struggling Student `stud-012`; Learner with Visual Preference `visual-004`, `visual-008`, `visual-015`. Kept at the strongest severity (`medium`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Polish: self-checks that print their answers, undifferentiated multiplet widths, missing per-carbon hydrogen counts** (`rec-020`) — raised independently by 4 personas: Struggling Student `stud-009`, `stud-016`, `stud-010`, `stud-013`, `stud-015`; Organic Chemistry Instructor `instr-013`, `instr-014`, `instr-015`; Learner with Visual Preference `visual-013`, `visual-010`, `visual-012`; Accessibility Persona `access-006`, `access-008`, `access-009`. Kept at the strongest severity (`medium`); every persona's learner impact is preserved verbatim in the persona reports above.

### Retained disagreements

#### Whether the chapter's spectra are its strongest or weakest asset

- **Accessibility Persona:** The four spectra are the chapter's outstanding feature: 'a genuine transcript rather than a caption', printed as visible text, so 'the spectra are fully readable without sight'. Scored the reader half as one of the strongest non-visual builds in the corpus.
- **Learner with Visual Preference:** The same four spectra render with no peak labels and no region labels at all (visual-003, high), one renders two of three signals as the wrong multiplet (visual-001, blocker), and the deliberate 60/300 MHz comparison is split across two sections (visual-004, high).

**Orchestrator resolution:** Both are right, and together they produce an inversion worth naming: for these figures the non-visual learner currently receives MORE information than the sighted one, because every label the author wrote reaches the text channel and none reaches the picture. The orchestrator therefore does not treat the strong long_descriptions as compensating for the unlabelled renders - they are compensating, which is exactly the problem, since it hides the render defect from anyone auditing description coverage. rec-014 keeps the label-drawing gap open as platform work; the long_descriptions are recorded under sufficient_as_is and deliberately left unchanged, because rewriting them would remove the only channel currently carrying the assignments.

#### Whether the dead spin-state video card is a publication blocker

- **Struggling Student:** Filed as stud-006, high, and explicitly raised in open_questions: 'If the reviewing team treats a rendered dead link as a publication defect on its own terms, stud-006 is the candidate.' The persona nonetheless recorded no blockers at all.
- **Learner with Visual Preference:** Treats the same deferred brief as correctly handled in visual-008, noting only that the section's real visual need is unmet - and lists 'the undeliverable video is compiled hidden' as a strength in its sibling section.
- **Accessibility Persona:** Lists the hidden video as a strength: 'compiled with is_hidden: true rather than left as an empty player - the right handling of a deferred asset.'

**Orchestrator resolution:** The Accessibility and Visual personas are describing the correct behaviour elsewhere in the corpus and generalised it; the Struggling Student actually checked this chapter's compiled block and found url '' with a live 'Watch' RouterLink and a storyboard fragment as its description. The orchestrator verified the block and resolved in favour of the Struggling Student on the facts. It is not promoted to blocker - a dead link degrades trust rather than making a required activity impossible - but it is corrected under rec-013, because the fix is to set the flag the other two personas already assumed was set.

#### Whether a chapter with no blocker-severity finding from two of four personas can be `blocked`

- **Struggling Student:** publication_blockers: [] and overall_score 6.2 - the highest struggling-student score in this batch.
- **Learner with Visual Preference:** One blocker (visual-001) and overall_score 6.0.
- **Organic Chemistry Instructor:** Four blockers and overall_score 6.4 - also the highest instructor score in this batch, on the chapter with the most blockers.
- **Accessibility Persona:** Four blockers and overall_score 5.2.

**Orchestrator resolution:** This chapter makes the 'computed, not averaged' rule do real work. Its mean persona score (5.95) is the highest of the four chapters reviewed in this batch, and the Instructor - who found four blockers - also gave it the highest instructor score of the batch, because score measures overall quality while blockers measure specific disqualifying defects. Eight blocker-severity findings across three personas force at least `major revision`; access-001 (an item no learner of any kind can answer) and access-002 (a required activity whose response targets are unidentifiable without sight) are unresolved required-access blockers and force `blocked`. The Struggling Student's empty blocker list is retained verbatim and is consistent: nothing here is impossible to follow as reading, which is that persona's lens.

### Places where a description is sufficient (no new asset)

- All four nmr_spectrum long_descriptions and the splitting-tree long_description: these are genuine transcripts carrying shift, multiplicity, intensity ratio, integration and J, and the reader prints them as visible text. No further description work is needed on these five assets - where they disagree with the render, it is the render that must change.
- Every interactive NMR workspace: keyboard-complete by construction, with no keyboard alternative or alternate activity to author.
- The colour handling in EnvironmentPaintBoard: letter badges plus a colourblind-safe palette plus aria-live announcements - colour is never the sole carrier and nothing needs adding.
- The chapter's outbound links: all seven concepts author a wikipedia_title and all 8 emitted links verify 200, so no link work is required (the defect that dominated ch9 and ch10 is absent here).
- The callout layer: unlike ch9 and ch10, this chapter's artifact already emits all 16 callouts, so the practice checks and trouble spots already reach the reader.
- The 300 MHz bromoethane figure's illegibility: deliberate and correct, since compression is the point its caption makes.

### Accessibility blockers

- **`access-001`** — The J-readoff line positions exist only in a spectrum config that no surface renders (numeric_with_units declares workspace 'none'), and appear in no text. The item is unanswerable by every learner, not merely inaccessible - and the only route to the graded number is a hint ladder that discloses it.
- **`access-002+access-005`** — Structure-bearing interactive items label their targets C1..C5 / 'on C1' from RDKit index order while the rendered structure carries no atom numbers and a hard-coded generic alt. Both types declare requires_molecule_description=True and neither supplies one.
- **`access-003`** — The integral-reconstruction trace's aria-label states both the peak positions and the graded proton counts. The leak lives in an externally referenced /assets/nmr/ asset that the compile-time guard never inspects.
- **`access-004`** — accessible_description is consumed by only three places in the repo, none of which this chapter's 15 question types reach, and every question is demo_eligible false - so all 44 authored non-visual equivalents currently reach no student. This is why the corrected descriptions cannot be verified in-product.

### Visual opportunities

- A 13C decoupled spectrum on its 0-220 ppm axis paired with its DEPT-135 companion, so the up/down/absent phase convention is seen rather than described.
- The 1H and 13C correlation regions drawn against a shared inverted delta axis, so 'upfield' and 'downfield' are positions rather than vocabulary.
- One integral step drawn on a labelled trace at the point integration is defined, rather than the learner meeting their first integral in the graded activity.
- A complete spectrum-to-structure worked pass on a displayed spectrum in the capstone section, which currently contains two structure drawings and no spectrum.
- The ethyl acetate and methyl propanoate spectra placed side by side so the quartet visibly moves between 4.1 and 2.3 ppm.
- Peak and integration labels drawn on the spectra themselves - the labels are already authored in the package and are dropped by both renderers.
- A re-windowed or lower-field methyl acrylate vinyl region in which the 1.5 Hz geminal coupling actually resolves.
- The two-orientation Zeeman energy picture in the opening section, whose only current visual is a Pascal-ratio widget answering a question three sections ahead.

### Regression targets for next run

Recheck these stable `finding_id`s after revision:

- `access-001` (blocker, Accessibility Persona) — The measurable data these items are graded on - the ordered list of line positions in ppm - must be present in…
- `access-002` (blocker, Accessibility Persona) — The atom identifiers a student must choose between need an unambiguous non-visual identity - each numbered pos…
- `access-003` (blocker, Accessibility Persona) — The non-visual equivalent for a trace a student is asked to integrate must convey where signals lie and that t…
- `access-004` (blocker, Accessibility Persona) — Every question that has a visual stimulus needs its authored text equivalent actually presented to the learner…
- `instr-001` (blocker, Organic Chemistry Instructor) — Students need a correct, checkable procedure for reading both couplings off a dd - which adjacent gap equals t…
- `instr-002` (blocker, Organic Chemistry Instructor) — Students need a single self-consistent intensity test across prose, figure and question feedback - equal line …
- `instr-003` (blocker, Organic Chemistry Instructor) — The figure's peak labels need to name each terminal proton by a relationship the reader can verify from the co…
- `instr-004` (blocker, Organic Chemistry Instructor) — The four numeric answer keys need a tolerance the shipped grader can read, and the chapter needs a pre-publica…
- `visual-001` (blocker, Learner with Visual Preference) — The chapter needs a rendering of the methyl acrylate vinyl region in which the 1.5 Hz geminal splitting is act…
- `access-005` (high, Accessibility Persona) — The structure a student is partitioning needs a text identity tying each labelled carbon to what it bears, so …
- `instr-005` (high, Organic Chemistry Instructor) — One bromoethane coupling constant needs to be true everywhere - prose, both spectrum figures and both read-off…
- `instr-006` (high, Organic Chemistry Instructor) — Students need the exchange exception stated where the n + 1 rule is taught - why OH and NH protons normally ap…
- `instr-007` (high, Organic Chemistry Instructor) — The chapter needs at least one graded item where the student builds or names a structure from a formula plus s…
- `instr-008` (high, Organic Chemistry Instructor) — Students need the 1H (and ideally 13C) correlation regions presented against a shared shift axis so the window…
- `stud-001` (high, Struggling Student) — A student needs to see at least one complete spectrum-to-structure pass performed on a displayed spectrum - si…
- `stud-002` (high, Struggling Student) — A student needs the degrees-of-unsaturation step to be executable inside this chapter - the computation stated…
- `stud-003` (high, Struggling Student) — A student needs the opposes-versus-reinforces reversal reconciled where it is introduced - an account tied to …
- `stud-004` (high, Struggling Student) — A student needs this section broken into digestible units with intermediate checkpoints - measurement-and-conv…
- `stud-005` (high, Struggling Student) — A student needs the named-mistakes coverage in this section to address this section's own traps - the dd-versu…
- `stud-006` (high, Struggling Student) — A student needs the page not to advertise a visual that does not exist - either the two-spin-state explanation…
- `stud-007` (high, Struggling Student) — A student needs the 1H and 13C shift correlations in a scannable lookup-shaped form, matching the treatment th…
- `stud-008` (high, Struggling Student) — A student needs to see an integral step on a labelled trace at the point integration is defined, rather than m…
- `visual-002` (high, Learner with Visual Preference) — Each terminal vinyl proton needs a label whose stated geometry is unambiguous and correct - either named by th…
- `visual-003` (high, Learner with Visual Preference) — The assignments and proton counts the author already wrote need to be visible on the figure itself, adjacent t…
- `visual-004` (high, Learner with Visual Preference) — The field-strength comparison needs the two renderings visible together at the moment the prose makes the argu…

---
## Post-correction record

**Estimated state: major revision (not a second persona verdict).**

Not a new persona verdict. All eight blocker-severity findings are resolved, including both required-access blockers, which clears `blocked`. Several high-severity findings remain open by design (new figures, new assessment items, platform wiring), so the estimate does not reach `ready with minor revisions`.

### Artifact-drift check (step 6a, before any compile)

- **Performed:** before any compile, per step 6a
- **Result:** CLEAN — the first chapter in this batch with no artifact-only drift to recover. Commit [commit ref — not in this repo] edited this chapter's compiled reader, but the improved 1,1-dichloroethane description it introduced is already present in topic.package.json (asset learning_goal), so the fix had been back-ported and a recompile could not destroy it. The chapter also arrived with wikipedia_title authored on all 7 concepts and callouts already emitting, so neither the fabricated-link nor the stranded-scaffolding defect that dominated ch9 and ch10 applies here.
- **Back-ported to the package before compiling:**

### Changes applied

- BLOCKER: corrected the doublet-of-doublets read-off procedure. The prose said the outer spacing is the large J and the inner spacing the small one; in fact each OUTER gap equals the SMALL J, the middle gap equals J_large - J_small (not a coupling at all), and the large J is the line-1-to-line-3 separation. Replaced with the correct procedure plus the chapter's own methyl acrylate case worked out (lines at -13.85, -3.45, +3.45, +13.85 Hz; gaps 10.4, 6.9, 10.4; total spread 27.7 Hz). — resolves `instr-001`
- BLOCKER: corrected the dd-versus-quartet intensity test, which was stated exactly backwards ('unequal intensities are the tell for a dd'). A dd is 1:1:1:1 and a quartet is 1:3:3:1. The erroneous sentence contradicted the sentence immediately before it, the chapter's own splitting-tree SVG (labelled 'dd - 1 : 1 : 1 : 1'), that figure's long description, and the ch13-dd-builder feedback. — resolves `instr-002`
- BLOCKER: relabelled the two terminal vinyl protons of the methyl acrylate spectrum. They were labelled 'trans to ester' / 'cis to ester' with the geometry inverted - the proton carrying the 17.3 Hz coupling is trans to the internal =CH- and therefore CIS to the ester. Re-referenced both labels to the internal =CH-, the partner the J value actually reports on, which is the convention the asset's own long_description and ch13-dd-builder already use. — resolves `instr-003`, `visual-002`
- BLOCKER: converted four numeric_with_units tolerances from a bare float to the {mode, amount} object [internal source reference — not in this repo] requires. Verified by execution that ch13-delta-ppm-conversion(-v2) and ch13-j-readoff(-v2) previously raised AttributeError ('float' object has no attribute 'get') and now all six numeric items grade correct at score 1.0. — resolves `instr-004`
- BLOCKER: both J-readoff items now carry their four/three line positions in prompt_text. Previously the positions existed only inside a spectrum config that no surface renders (numeric_with_units declares workspace 'none'), so the item was unanswerable by every learner and the only route to the number was a hint that disclosed it. The line spacings were also re-set so the measurement reproduces the chapter's own 7.3 Hz (now 7.29 and 7.32 Hz) instead of the previous 7.5 and 7.2, and the prose arithmetic slip '0.024 x 300 = 7.3' was corrected to 0.0243. — resolves `access-001`, `instr-005`, `visual-014`
- BLOCKER: authored structured per-atom descriptions for both 13C peak-assignment items, keyed to the 1-based numbering the dropdown announces (C1..C5), naming each numbered position by what it is bonded to. Atom indices were verified against RDKit for CCC(C)=O and CC(=O)OC. The question type declares requires_molecule_description=True and none was supplied, while the rendered structure carries no atom numbers. — resolves `access-002`
- BLOCKER: rewrote the accessibility descriptions of the two /assets/nmr/ integral traces, which were passed straight through as the spectrum canvas's aria-label and stated both the peak positions AND the graded proton counts. They now convey where the signals lie and that the two differ in area, without the counts. This leak lives outside topic.package.json, so the compile-time guard never inspected it. — resolves `access-003`
- Bound each labelled carbon to its substituents in the equivalence-partition and spin-system-builder descriptions, so the 'on C1 / on C2 / on C3' hydrogen buckets are self-describing instead of having to be decoded from the picture. — resolves `access-005`
- Added the two trouble spots that belong specifically to the coupling-constants section - the 1:1:1:1 dd versus 1:3:3:1 quartet confusion, and the fact that the tabulated ~12 Hz geminal coupling does not split an ordinary freely rotating CH2. Because both nuggets map to the single spin-spin-splitting concept, the callout previously rendered byte-identically in both sections, so this section's own traps were never named. — resolves `stud-005` · partially addresses `stud-004`
- Added the OH/NH exchange exception where chemical shifts are taught: why an O-H or N-H proton usually does not couple, the ethanol case (broad OH singlet and clean CH2 quartet rather than the n + 1 prediction), and the D2O shake that confirms one. The chapter previously taught n + 1 as universal while using alcohols in its own examples and hedging around the issue in ch13-decoupling-propyl-v2. — resolves `instr-006`
- Made step one of the capstone method executable: stated the degrees-of-unsaturation formula (2c + 2 - h)/2 and worked it on the chapter's own two formulas (C3H6O and C4H8O2 both give 1). The section previously instructed students to compute it first, never stated it, and declared a prerequisite concept that does not exist in this package. — resolves `stud-002` · partially addresses `stud-001`
- Reconciled anisotropy with the shielding rule established two sections earlier. Section 2 said the induced field opposes the applied field and section 4 said it reinforces it, with nothing to reconcile them; the text now explains that the induced field opposes inside the ring and reinforces outside it, where the attached hydrogens sit. — resolves `stud-003`
- Marked the deferred spin-state video brief hidden, so it stops emitting a reader card with a live 'Watch' link pointing at an empty URL and a production storyboard line as its description. Verified in the recompiled artifact: the video block is now is_hidden true. — resolves `stud-006`
- Rewrote two hint rungs that handed over the graded value - ch13-integral-reconstruction L3 stated both proton assignments, ch13-delta-ppm-conversion L3 performed the arithmetic - replacing each with the procedure. This matters doubly on items whose visual stimulus does not render, where the ladder was the only reachable channel. — resolves `access-007`
- Corrected the 300 MHz bromoethane figure's description, which gave one multiplet width for two multiplets of different widths (the triplet spans 2J, the quartet 3J), and fixed the false 'the 60 MHz one beside it' cross-reference - that twin compiles into the previous section. — resolves `instr-013`, `visual-013`, `stud-012` · partially addresses `visual-004`
- Added per-carbon hydrogen counts to the alt text of the five molecule figures that set show_hydrogens specifically so learners could count them - the one piece of information those figures add over a plain skeleton, and the piece the alt text omitted. — resolves `access-006`

### Verification

- numeric_grading.grade_numeric round-trip over all six numeric_with_units items with the answer key as the submission — 6/6 now return status 'correct' at score 1.0 (pre-correction: 4/6 raised AttributeError)
- J-readoff arithmetic recomputed from the authored line positions — 0.0243 ppm x 300 MHz = 7.29 Hz and 0.0183 ppm x 400 MHz = 7.32 Hz, both matching the chapter's taught 7.3 Hz within the keyed tolerance (pre-correction: 7.5 and 7.2, contradicting each other and the prose)
- RDKit atom-index check on CCC(C)=O and CC(=O)OC — confirms the authored per-atom descriptions match the 1-based C1..C5 labels the peak-assignment dropdown announces
- Topic-package compiler (proprietary toolchain, not in this repo) — clean
- Automated test suite — 173 passed
- accessibility_guard.find_accessibility_leaks over all 44 questions — 0 flagged (note: the guard also returned 0 BEFORE correction; every leak in this chapter was semantic or lived outside the package entirely, so this is a regression check, not the evidence they are fixed)
- Compiled reader inspection — the deferred spin-state video block is now is_hidden true, so the dead 'Watch' link no longer renders
- curl on all 8 emitted outbound links — 8/8 returned 200 (this chapter arrived with wikipedia_title authored on all seven concepts; no link work was needed)
- git diff review — changed files are chapter-derived plus the two /assets/nmr/ trace descriptions; no unrelated aggregate churn

### Still recommended

- rec-014 / rec-015 / rec-016 — the figure work: no 13C or DEPT spectrum anywhere (DEPT's up/down/absent phasing is a visual fact prose cannot carry); the 1H and 13C correlation regions still delivered as prose rather than tables keyed to the delta axis; no integral step drawn where integration is defined; and the methyl acrylate figure still cannot resolve its 1.5 Hz geminal coupling at 300 MHz over a 4 ppm window (the renderer's fixed 0.008 ppm linewidth is a hard floor).
- visual-003 — every peak label and integration-region label authored on the four spectra is dropped by both renderers, so the sighted reader currently gets LESS than the screen-reader user. GenericSpectrumCanvas never renders r.label; this is platform work.
- rec-017 — three objectives assessed by nothing: DEPT classification (the one 13C item hands the student the DEPT result), selective decoupling (graded at 'advanced' from a single subordinate clause of coverage), and structure construction (the capstone is a 50% pick between two named isomers).
- rec-018 / access-004 — the 44 authored accessible_description strings are consumed by only three places in the repo, none of which this chapter's 15 question types reach, and every question is demo_eligible false. This is why the six descriptions corrected above cannot be verified in-product.
- instr-009 — items asking for 'a typical J' grade against a literature value inside a 0.3 Hz window, so a student using the chapter's own table scores 0.6. Left uncorrected because widening the tolerance versus tightening the prompt is a pedagogy call.
- stud-004 — the coupling-constants section remains 761 words against a ~350-word chapter average with eleven ideas in one unbroken block; splitting it is authoring scope.
- stud-009 — all eight practice_check callouts print their answer beneath the prompt with no reveal step. This is a platform-wide compiler pattern affecting every chapter, not a ch13 authoring choice.
