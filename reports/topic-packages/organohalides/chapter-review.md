# Chapter review — Organohalides (`organohalides`)

_Reviewed 2026-07-31 · chapter version 1 · personas: Instructor, Struggling Student, Accessibility, Visual Preference_

**Publication readiness: blocked**

The prose in this chapter is among the best in the family — the two independent halogen trends are separated explicitly, the Hammond reactivity–selectivity argument is built rather than asserted, umpolung is derived rather than stated, and all 24 answer keys are chemically correct. The defects are concentrated in the layers between that prose and the student. Two hard chemistry blockers converge from independent personas: the asset captioned 'the selective bromination product' is 2-bromo-2-methylpropane (C4) while the substrate it sits beside is 2-methylbutane (C5), so the flagship radical-bromination figure — and the video storyboard built on the same pair — depicts a substitution that loses a carbon and contradicts the chapter's own error_repair key; and the level-3 worked_step hint on ch10-monochlorination-count enumerates the hydrogen environments of 2-methylbutane incorrectly, counting the two methyls on C2 as distinct and omitting C4 entirely, so it reaches the right answer, 4, by an equivalence analysis that will fail on the very next molecule. RDKit confirms both (symmetry classes [1,4,1,3,0]). Four more blocker-severity findings sit in the accessibility layer: both structure_scaffold items state their product in `accessible_description` and both hotspot items name the target atom, and the compile-time guard passes all 24 because it matches answer ids and numbers, never product names. Removing the hotspot leak leaves that item unanswerable without vision — the atom buttons announce only 'C atom N' with no connectivity — which is an unresolved required-access blocker and forces `blocked`. Underneath it all, the compiled artifact is the sixth confirmed recompile-revert: commit [commit ref — not in this repo] replaced all seven fabricated Wikipedia URLs with real articles in the artifact only, and the 2026-07-30 recompile put the 404s back. The chapter also has zero callout blocks (7 practice checks and 14 trouble spots reach nobody), three empty video players, and 17 assets that are all static single-molecule renders — so the early-versus-late transition state and the delocalized allylic radical, the chapter's two hardest ideas, are drawn nowhere.

### Top blockers

- **[BLOCKER] Both structure_scaffold questions put the graded product into accessible_description as an explicit answer statement.** — `access-001` (Accessibility Persona; section_id=`nugget-halides-from-alcohols`, concept_slug=`alkyl-halides-from-alcohols`, question_slug=`ch10-draw-pbr3-product`)
- **[BLOCKER] Both hotspot descriptions state the rule the question exists to test.** — `access-002` (Accessibility Persona; section_id=`nugget-allylic-bromination`, concept_slug=`allylic-bromination`, question_slug=`ch10-allylic-site-hotspot-v2`)
- **[BLOCKER] The asset presented as the outcome of selective radical bromination is 2-bromo-2-methylpropane (CC(C)(C)Br, C4H9Br), but the only substrate in that nugget is 2-methylbutane (CC(C)CC, C5H12).** — `instr-001` (Organic Chemistry Instructor; asset_id=`mol-tert-butyl-bromide`, nugget_id=`nugget-radical-halogenation`, concept_slug=`radical-halogenation-of-alkanes`)
- **[BLOCKER] The level-3 worked_step hint enumerates the wrong set of hydrogen environments in 2-methylbutane.** — `instr-002` (Organic Chemistry Instructor; question_slug=`ch10-monochlorination-count`, concept_slug=`radical-halogenation-of-alkanes`)
- **[BLOCKER] The level-3 worked_step hint enumerates the wrong set of distinct hydrogen environments in 2-methylbutane.** — `stud-001` (Struggling Student; question_slug=`ch10-monochlorination-count`, concept_slug=`radical-halogenation-of-alkanes`)
- **[BLOCKER] All seven authored practice_check prompts and all fourteen concept trouble_spots are absent from the compiled reader, which contains only text, molecule, video, external_link and mcmurry_link blocks across all seven sections — no callout, practice or question block anywhere, and no question from the 12-item surfaced bank embedded in the reading flow.** — `stud-002` (Struggling Student; section_id=`nugget-organohalide-structure`, nugget_id=`nugget-organohalide-structure`)

### Top 5 recommended changes

1. **The 'selective bromination product' figure loses a carbon** — The product depicted for radical bromination must be the product of the substrate depicted beside it, and the video brief and the graded error_repair item must name the same compound. → **new-figure** (figure, blocker)
2. **The deepest hint teaches a wrong symmetry analysis** — The final rung of the monochlorination hint ladder must model a hydrogen-environment count that is itself correct and that matches the four products the item's own explanation names. → **prose-edit** (assessment, blocker)
3. **Both structure_scaffold items state their own answer** — The non-visual equivalent of a draw-the-product item must convey the substrate, the reagent and the task, and must not name the product. → **text-equivalent** (assessment, blocker)
4. **Hotspot items name the answer atom, and are unanswerable without vision once that is removed** — A non-visual learner must be able to locate the allylic carbon by applying the definition, which requires the structure's connectivity keyed to the labels the atom buttons announce — without being told which atom qualifies. → **structured-chemical-description** (assessment, blocker)
5. **Seven fabricated Wikipedia links, reverted by recompile for the second time** — Every offered background-reading target must resolve to a real, on-topic page, and the fix must survive the next compile. → **prose-edit** (prose, high)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 6.0/10 | 2 | Good prose, correct keys — but the flagship bromination figure loses a carbon and the deepest hint teaches a wrong symmetry count. |
| Struggling Student | 5.1/10 | 2 | Seven walls of undifferentiated prose; every practice check and trouble spot is stranded; the rung I climb to when stuck is wrong. |
| Accessibility Persona | 6.0/10 | 2 | Excellent keyboard substrate; the failures are authored text — four answer leaks the compile guard cannot see. |
| Learner with Visual Preference | 4.6/10 | 0 | 17 assets, all isolated line structures: no energy profile, no mechanism, no transformation anywhere. |

### Affected sections & assets

`alkyl-halides-from-alcohols`, `allylic-bromination`, `allylic-radical-resonance`, `ch10-allylic-site-hotspot-v2`, `ch10-allylic-site-hotspot`, `ch10-allylic-two-products`, `ch10-bromination-selectivity-error`, `ch10-classify-tertiary-halide`, `ch10-cx-bond-strength-match`, `ch10-draw-pbr3-product`, `ch10-grignard-vs-gilman`, `ch10-halide-to-alkane-route`, `ch10-monochlorination-count`, `ch10-radical-stability-rank-v2`, `ch10-radical-stability-rank`, `grignard-and-organometallic-reagents`, `mol-1-bromo-2-butene`, `mol-1-butanol`, `mol-2-methylbutane`, `mol-but-1-ene`, `mol-hexane`, `mol-tert-butyl-bromide`, `mol-tert-butyl-chloride`, `nugget-allylic-bromination`, `nugget-allylic-resonance`, `nugget-coupling-oxidation-state`, `nugget-grignard`, `nugget-halides-from-alcohols`, `nugget-organohalide-structure`, `nugget-radical-halogenation`, `organohalide-structure-and-naming`, `organometallic-coupling-and-oxidation-state`, `radical-halogenation-of-alkanes`, `video-allylic-resonance`, `video-radical-halogenation`

---
## Full evidence

### Independent persona reports

#### Organic Chemistry Instructor — 6.0/10

Not a go for instructor use yet. The prose is genuinely good — the two independent halogen trends are separated cleanly, the Hammond early/late transition-state argument is correct and well motivated, umpolung is explained rather than asserted, and all 24 answer keys check out chemically. But the defects live in the layers a student actually touches. Two are hard blockers: the figure the chapter calls 'the selective bromination product' is 2-bromo-2-methylpropane (C4) while the substrate it is paired with is 2-methylbutane (C5), so the flagship radical-bromination figure and its video storyboard depict a reaction that loses a carbon and contradicts the chapter's own error_repair item; and the level-3 worked_step hint on ch10-monochlorination-count enumerates the wrong four hydrogen environments of 2-methylbutane, teaching the right count by a wrong equivalence analysis. Beyond those, the chapter tells students that chlorination reacts 'in rough proportion' to hydrogen counts, which is quantitatively false; one product is misnamed 3-chloro-2-methylbutane; the compiled reader carries seven auto-generated Wikipedia URLs that all 404, three empty video blocks, and none of the seven practice checks or fourteen trouble spots. Every one of the 17 assets is a static molecule render, so the early-versus-late transition state and the delocalized allylic radical reach the student as prose only. Three learning objectives are never assessed by any of the 24 items.

**Publication blockers:** `instr-001`, `instr-002`

**Strengths**

- All 24 answer keys are chemically correct as verified item by item, including both allylic-bromination product pairs, both hotspot atom indices, both monochlorination counts, and the cuprate primary-versus-tertiary matrix.
- The naming section separates the two halogen trends explicitly and names the exact confusion it is preventing ('the most polar bond, C-F, is also the strongest, not the easiest to break').
- The reactivity-selectivity treatment builds a mechanistic why rather than asserting an outcome, ending on the general principle that the less reactive reagent is the more selective one.
- The Grignard section teaches umpolung as the organizing idea and derives both the operating conditions and the R-X to R-H reduction from it, rather than presenting 'keep it dry' as a rule to memorize.
- Every question carries a three-level hint ladder and per-distractor explanations that name the specific misreading — the vicinal-dibromide distractor is answered with the low-[Br2] argument rather than a restatement of the key.
- textbook_matching is honest about texts that do not map cleanly, including an explicit empty-chapter entry with the reason stated, and the compiled question set matches the package field for field with no drift.

**Findings**

##### `instr-001` — BLOCKER · chemical-accuracy · confidence 0.98

**Location:** asset_id=`mol-tert-butyl-bromide` · nugget_id=`nugget-radical-halogenation` · concept_slug=`radical-halogenation-of-alkanes` · anchor="2-Bromo-2-methylpropane, the selective bromination product"

**Observation:** The asset presented as the outcome of selective radical bromination is 2-bromo-2-methylpropane (CC(C)(C)Br, C4H9Br), but the only substrate in that nugget is 2-methylbutane (CC(C)CC, C5H12). Bromination of 2-methylbutane gives 2-bromo-2-methylbutane (C5H11Br). The figure pair shows a substitution that removes a carbon. The same wrong pairing is baked into video-radical-halogenation, whose storyboard reads 'abstracting a hydrogen from 2-methylbutane' then 'funnels to the tertiary bromide' over visual_asset_ids [mol-2-methylbutane, mol-tert-butyl-bromide].

**Learner impact:** A student sees the chapter's central selectivity claim illustrated by a product that cannot come from the substrate shown. It directly contradicts ch10-bromination-selectivity-error, whose correct repair states the major product is 2-bromo-2-methylbutane, so a student who trusts the figure answers that graded item wrong.

**Evidence:** assets mol-tert-butyl-bromide smiles 'CC(C)(C)Br' with learning_goal 'See the tertiary bromide favored by radical bromination'; asset_ids of nugget-radical-halogenation = [mol-2-methylbutane, mol-tert-butyl-bromide]; video_briefs video-radical-halogenation storyboard steps 2 and 4; question ch10-bromination-selectivity-error repair_options fix_tertiary '2-bromo-2-methylbutane'.

**Recommended outcome (need):** The radical-bromination section needs a product depiction whose carbon skeleton is the brominated 2-methylbutane, so substrate, figure, video brief and the error_repair item all name the same compound.

##### `instr-002` — BLOCKER · chemical-accuracy · confidence 0.97

**Location:** question_slug=`ch10-monochlorination-count` · concept_slug=`radical-halogenation-of-alkanes` · anchor="The distinct positions are C1, the tertiary C2-H, C3, and the branch methyl; that is four."

**Observation:** The level-3 worked_step hint enumerates the wrong set of hydrogen environments in 2-methylbutane. C1 and the branch (2-methyl) group are both methyls attached to C2 and are therefore the SAME environment. The genuinely distinct fourth position, C4 (the terminal methyl of the ethyl arm, giving 1-chloro-3-methylbutane), is missing. The hint arrives at the right number, 4, by double-counting one environment and dropping another. The wrong-answer explanation for '3' compounds this by asserting 'the two end methyls are not equivalent to each other in this skeleton' with no indication which two methyls are meant.

**Learner impact:** This is precisely the skill the item exists to build. A student who follows the worked step learns an incorrect equivalence rule and will mis-count environments on every later isomer-counting, NMR-signal-counting and monosubstitution problem. It also contradicts the item's own generic_incorrect_explanation, which correctly lists 1-chloro-3-methylbutane among the four products.

**Evidence:** feedback_bundle.hints[2].kind='worked_step'; generic_incorrect_explanation lists the four correct products; wrong_answer_explanations match.number=3.

**Recommended outcome (need):** The worked step needs to name the four environments that actually exist (the two equivalent methyls on C2 as one position, the tertiary C2-H, the C3 methylene, and the C4 methyl), and the '3' distractor explanation needs to say which methyls it is contrasting.

##### `instr-003` — HIGH · notation-consistency · confidence 0.95

**Location:** question_slug=`ch10-monochlorination-count` · anchor="3-chloro-2-methylbutane"

**Observation:** The product of chlorinating C3 of 2-methylbutane, (CH3)2CH-CHCl-CH3, is misnamed. Both numbering directions give the locant set {2,3}, so the tie is broken by giving the lower locant to the substituent cited first alphabetically — chloro. The correct name is 2-chloro-3-methylbutane, not 3-chloro-2-methylbutane.

**Learner impact:** The name appears in the explanation every student sees after answering, so students reproduce an incorrect IUPAC name on exams. It also silently teaches the wrong tie-break rule for equal locant sets.

**Evidence:** generic_incorrect_explanation of ch10-monochlorination-count: '...1-chloro-2-methylbutane, 2-chloro-2-methylbutane, 3-chloro-2-methylbutane, and 1-chloro-3-methylbutane.'

**Recommended outcome (need):** The product name needs correcting, and the chapter needs the alphabetical tie-break rule stated in the naming nugget, which currently only covers 'first point of difference'.

##### `instr-004` — HIGH · chemical-accuracy · confidence 0.93

**Location:** question_slug=`ch10-bromination-selectivity-error` · nugget_id=`nugget-radical-halogenation` · anchor="Statistical counting describes chlorination, not bromination."

**Observation:** The chapter twice teaches that chlorination is purely statistical: the expanded prose says chlorination 'reacts at all available positions in rough proportion to how many of each there are', and the fix_count distractor explanation says 'statistical counting describes chlorination'. Chlorine atoms abstract with relative per-hydrogen reactivities of roughly 1 : 3.5 : 5 for primary : secondary : tertiary. For 2-methylpropane statistics predicts 90:10 while the observed ratio is about 64:36.

**Learner impact:** Students taught pure head-counting compute chlorination product ratios wrong on any problem set asking for percentages. It also weakens the chapter's own argument: chlorine is less selective than bromine, not unselective, and that distinction is what the Hammond analysis predicts.

**Evidence:** nugget-radical-halogenation text.expanded; ch10-bromination-selectivity-error wrong_answer_explanations match.repair='fix_count'.

**Recommended outcome (need):** The chlorination selectivity claim needs stating as weak-but-real rather than absent — a per-hydrogen reactivity weighting that lets a student compute an actual product ratio.

##### `instr-005` — HIGH · conceptual-support · confidence 0.96

**Location:** section_id=`nugget-organohalide-structure` · concept_slug=`organohalide-structure-and-naming` · anchor="https://en.wikipedia.org/wiki/The_carbon-halogen_bond_and_how_alkyl_halides_are_named_and_classified"

**Observation:** No concept authors a wikipedia_title, so the reader builder falls back to the concept title verbatim and emits seven 'Background reading' links whose URLs are sentence-length concept titles. All seven resolve to non-existent articles. Separately the only textbook link in the chapter is a single chapter-level OpenStax 'why this chapter' page, not the 1-6 specific section links the Additional Reading convention calls for.

**Learner impact:** Every section ends with a dead further-reading link. A student hits seven 404s, and an instructor spot-checking the chapter reads the whole further-reading layer as untended.

**Evidence:** All seven external_link blocks in the compiled reader; [internal source reference — not in this repo] 'title = concept.get("wikipedia_title") or concept["title"]'; concepts[] contain no wikipedia_title key.

**Recommended outcome (need):** Each concept needs an authored, verified target for its background-reading link, and the chapter needs section-level rather than chapter-level assigned-reading anchors.

##### `instr-006` — HIGH · retrieval-practice · confidence 0.94

**Location:** section_id=`nugget-organohalide-structure` · nugget_id=`nugget-organohalide-structure` · anchor="Is the C-I bond stronger or weaker than the C-F bond, and which of the two is more polar?"

**Observation:** All seven authored practice_checks and all fourteen concept trouble_spots are absent from the compiled reader. The builder emits them as 'Check yourself before moving on' and 'Common ways this goes wrong' callouts, but the committed artifact contains zero callout blocks in any of its seven sections.

**Learner impact:** Students read seven long sections with no retrieval stop between them, and the chapter's sharpest diagnostic content — 'assuming the most polar C-X bond is also the strongest', 'writing a two-electron arrow for a step that moves a single electron' — never warns the student at the point of risk. These are the misconceptions the questions then penalize.

**Evidence:** Block-type census of all seven sections yields only text, molecule, video, mcmurry_link, external_link; [internal source reference — not in this repo] _practice_check_block and _trouble_spots_block are wired into _build_section.

**Recommended outcome (need):** The student-facing chapter needs its authored retrieval checkpoints and named misconceptions present at the point of use; the compiled artifact is stale relative to the builder that emits them.

##### `instr-007` — HIGH · media-equivalence · confidence 0.95

**Location:** section_id=`nugget-radical-halogenation` · asset_id=`video-radical-halogenation` · anchor=""url": "", "is_external": false"

**Observation:** Three sections carry a video block whose url is the empty string: video-radical-halogenation, video-allylic-resonance and video-grignard-carbanion, all still status 'needs_review'.

**Learner impact:** The three ideas assigned to video are the three the prose can least carry alone — fishhook single-electron arrows through the chain, the SOMO overlapping the double bond, and the polarity flip at carbon. Nothing in the section substitutes.

**Evidence:** video blocks in sections nugget-radical-halogenation, nugget-allylic-resonance, nugget-grignard each have content.url ''; video_briefs status 'needs_review' for all three.

**Recommended outcome (need):** Either the three storyboarded explanations need a working representation in the reader, or the content needs delivering another way and the empty blocks removed.

##### `instr-008` — HIGH · visual-opportunity · confidence 0.9

**Location:** nugget_id=`nugget-radical-halogenation` · concept_slug=`radical-halogenation-of-alkanes` · anchor="by Hammond the transition state is early and reactant-like"

**Observation:** The chapter's central explanatory move — an early, reactant-like transition state for the exothermic chlorine abstraction versus a late, radical-like one for the endothermic bromine abstraction — is delivered entirely as prose. All 17 assets are static single-molecule renders; there is no energy-versus-progress figure anywhere.

**Learner impact:** 'Late transition state resembles the product' is a claim about the shape of two energy curves. Without seeing them side by side most students memorize 'bromine is selective' and cannot transfer the argument to any other reactivity-selectivity pair.

**Evidence:** nugget-radical-halogenation text.expanded; assets[] contains 17 entries, all type 'molecule'; video-radical-halogenation storyboard step 4 is the only comparative treatment and its reader block has an empty url.

**Recommended outcome (need):** The chapter needs the early-versus-late transition-state comparison in a form where the student can see the two profiles and where the transition state sits along each.

##### `instr-009` — HIGH · visual-opportunity · confidence 0.92

**Location:** nugget_id=`nugget-allylic-resonance` · concept_slug=`allylic-radical-resonance` · anchor="We represent this with two resonance structures, one showing the radical on the near carbon"

**Observation:** The delocalized allylic radical is never depicted. The section's three assets are but-1-ene and the two bromide products; the radical itself, its two resonance structures, the double-headed resonance arrow and the singly occupied p orbital appear only in prose and in the unrendered video. The same gap applies to the fishhook arrow: the concept names 'writing a two-electron arrow for a step that actually moves a single electron' as a trouble spot, yet no figure or question shows a single-barbed arrow.

**Learner impact:** The chapter's own trouble spot is 'treating the two resonance structures as separate molecules that interconvert' — a misconception created by text and cured by a picture. Students are asked in ch10-allylic-two-products to predict both products from a delocalization they have never seen drawn.

**Evidence:** nugget-allylic-resonance asset_ids = [mol-but-1-ene, mol-3-bromo-1-butene, mol-1-bromo-2-butene]; concept trouble_spots; no asset has type other than 'molecule'.

**Recommended outcome (need):** The chapter needs the allylic radical shown as one delocalized species with spin at both ends, and at least one place where fishhook notation is demonstrated rather than only warned about.

##### `instr-010` — HIGH · objective-alignment · confidence 0.93

**Location:** concept_slug=`radical-halogenation-of-alkanes` · question_slug=`ch10-bromination-selectivity-error` · anchor="Lay out the initiation, propagation, and termination steps of radical halogenation."

**Observation:** Three authored learning objectives are never assessed by any of the 24 questions. (1) 'Lay out the initiation, propagation, and termination steps' — no item asks a student to produce, order or classify a chain step. (2) 'Choose HX, PBr3, or SOCl2 to convert a given alcohol to its halide' — both items on that concept simply apply PBr3, and SOCl2 appears in zero questions. (3) 'Assign whether a transformation is an oxidation or a reduction' — assessed only by the practice_check, which does not reach the reader.

**Learner impact:** A student can score fully without ever writing a propagation step, choosing between the three alcohol-to-halide reagents, or classifying a redox change — the three skills the chapter says it is building.

**Evidence:** nugget-radical-halogenation learning_objectives[0]; nugget-halides-from-alcohols learning_objectives[0]; nugget-coupling-oxidation-state learning_objectives[2]; 24 items across 12 types.

**Recommended outcome (need):** The bank needs coverage of the chain-step sequence, of reagent choice across HX/PBr3/SOCl2, and of oxidation-versus-reduction assignment.

##### `instr-011` — MEDIUM · chemical-accuracy · confidence 0.85

**Location:** question_slug=`ch10-cx-bond-strength-match` · nugget_id=`nugget-organohalide-structure` · anchor="roughly 480 kilojoules per mole for C-F down to about 210 for C-I"

**Observation:** The C-X bond dissociation energies are drifted from standard values at both ends. Commonly tabulated CH3-X values are about 460 (C-F), 350 (C-Cl), 294 (C-Br) and 239 (C-I) kJ/mol; the chapter uses 480, 340, 285 and 210. The C-I figure is roughly 30 kJ/mol low and C-F about 20 high, and the same four numbers are what a student must match in ch10-cx-bond-strength-match.

**Learner impact:** The trend is correct but students memorize the numbers from a matching exercise and find them contradicted by their textbook's table, with the biggest discrepancy on C-I, the bond this chapter most wants them to think of as weak.

**Evidence:** nugget-organohalide-structure text.expanded; ch10-cx-bond-strength-match student_config.right values.

**Recommended outcome (need):** The four C-X bond energies need to agree with a citable standard table, since they are presented as memorizable values rather than a bare ordering.

##### `instr-012` — MEDIUM · notation-consistency · confidence 0.9

**Location:** nugget_id=`nugget-radical-halogenation` · question_slug=`ch10-radical-stability-rank-v2` · anchor="C-H bond dissociation energies fall from about 105 kilocalories per mole for methane"

**Observation:** The chapter reports carbon-halogen bond strengths in kJ/mol and carbon-hydrogen bond strengths in kcal/mol, with no conversion offered and both described as 'bond dissociation energy'. Section 1 uses kJ/mol (480, 340, 285, 210); sections 2 and 4 use kcal/mol (105, 101, 98, 88).

**Learner impact:** A student cannot place the 88 kcal/mol allylic C-H against the 285 kJ/mol C-Br without noticing the unit switch, and many will not — they will conclude a C-Br bond is three times stronger than a C-H bond.

**Evidence:** nugget-organohalide-structure text.expanded (kJ/mol) versus nugget-radical-halogenation text.standard and nugget-allylic-resonance text.terse (kcal/mol).

**Recommended outcome (need):** The chapter needs one energy unit throughout, or every value dual-labeled, so bond strengths are directly comparable.

##### `instr-013` — MEDIUM · notation-consistency · confidence 0.88

**Location:** question_slug=`ch10-allylic-two-products` · asset_id=`mol-but-1-ene` · anchor="Allylic bromination (NBS, light) of but-1-ene"

**Observation:** Alkene locant placement is inconsistent within single items. ch10-allylic-two-products uses 2013 style in its prompt ('but-1-ene') and older style in its own options ('3-Bromo-1-butene', '1-Bromo-2-butene'); its v2 uses '1-pentene' in the prompt and '3-Bromo-1-pentene' in the options. Assets mix the two as well.

**Learner impact:** Students reading a prompt and its options in the same breath see two conventions and reasonably conclude one is a typo. It also leaves them unsure which style a short-answer item will accept.

**Evidence:** ch10-allylic-two-products prompt_text versus student_config.options; assets mol-but-1-ene, mol-allyl-bromide, mol-3-bromo-1-butene, mol-1-bromo-2-butene.

**Recommended outcome (need):** The chapter needs one locant convention across prose, asset titles, prompts and options, with any accepted alternative stated where a student types a name.

##### `instr-014` — MEDIUM · misconception · confidence 0.82

**Location:** question_slug=`ch10-grignard-vs-gilman` · concept_slug=`organometallic-coupling-and-oxidation-state` · anchor="Carbon is a strong base (deprotonates water rapidly)"

**Observation:** The comparison matrix keys 'Carbon is a strong base' as No for R2CuLi while keying 'Is destroyed by protic solvents such as water' as Yes for R2CuLi, and the distractor explanation attributes the second to 'reactive carbon-metal bonds' rather than to basicity. But a cuprate is destroyed by water precisely because its carbon is protonated — it is less basic than a Grignard reagent, not non-basic.

**Learner impact:** Students are handed two cells that read as contradictory with a non-explanation to reconcile them, which blocks the section's actual lesson: coupling works because the cuprate's basicity is lower, on a continuum, not because it is switched off.

**Evidence:** ch10-grignard-vs-gilman answer_key.expected_cells strongly_basic.case_gilman='no' and quenched_by_water.case_gilman='yes'; wrong_answer_explanations.

**Recommended outcome (need):** The basicity row needs to distinguish degree rather than presence, so 'less basic than a Grignard' and 'still destroyed by water' stop reading as a contradiction.

##### `instr-015` — MEDIUM · missing-example · confidence 0.86

**Location:** nugget_id=`nugget-coupling-oxidation-state` · asset_id=`mol-hexane` · anchor="Hexane, a homocoupling product"

**Observation:** The only worked illustration of diorganocopper coupling is 1-bromopropane joined to a propyl group to give hexane — a homocoupling. The section's own objective is to show 'R and R' joined into R-R'', and with both fragments the same a student cannot tell which came from the cuprate. The Gilman reagent R2CuLi is never depicted anywhere, and neither is NBS despite being named repeatedly.

**Learner impact:** Students cannot practise the actual synthetic skill — deciding which partner to make into the cuprate — from a symmetric example, and leave unable to recognize either signature reagent on sight.

**Evidence:** assets mol-1-bromopropane and mol-hexane, the only two on nugget-coupling-oxidation-state; no asset or question renders N-bromosuccinimide or a diorganocopper reagent.

**Recommended outcome (need):** The coupling section needs a cross-coupling example where the two carbon fragments are distinguishable, and the chapter needs NBS and R2CuLi visible somewhere.

##### `instr-016` — MEDIUM · sequencing · confidence 0.84

**Location:** concept_slug=`radical-halogenation-of-alkanes` · nugget_id=`nugget-radical-halogenation` · anchor="prerequisites"

**Observation:** concepts[radical-halogenation-of-alkanes].prerequisites lists only 'organohalide-structure-and-naming', but the section assumes homolysis, bond dissociation energy, exothermic-versus-endothermic steps, transition-state structure and the Hammond postulate — which is invoked by name without ever being stated. Separately, concept 3 (allylic-bromination) justifies its selectivity by resonance stabilization, which is concept 4.

**Learner impact:** A student who has not met Hammond's postulate gets a named authority with no content, and the reactivity-selectivity argument degrades to 'because the book says so'.

**Evidence:** concepts[].prerequisites; nugget-radical-halogenation text.expanded 'can be analyzed with the Hammond postulate'; nugget-allylic-bromination 'developed fully in the next section'.

**Recommended outcome (need):** The prerequisite lists need to name the energetics ideas the prose assumes, and the Hammond postulate needs a one-line statement in place or an explicit pointer.

##### `instr-017` — MEDIUM · missing-example · confidence 0.87

**Location:** nugget_id=`nugget-radical-halogenation` · concept_slug=`radical-halogenation-of-alkanes` · anchor="about 105 kilocalories per mole for methane to about 101 for a primary and 98 for a secondary"

**Observation:** The section never gives a tertiary C-H bond dissociation energy (about 96-97 kcal/mol) even though the paragraph's conclusion is that bromination delivers the tertiary bromide. It never says why only Cl2 and Br2 are used — fluorination is uncontrollably exothermic, iodination endothermic. And it never notes that the planar radical intermediate destroys stereochemical information, so halogenation at a stereocenter gives racemic product.

**Learner impact:** The BDE argument stops one rung short of the case it is used to justify. The halogen-scope and stereochemistry points are standard exam material in every treatment of this reaction.

**Evidence:** nugget-radical-halogenation text.standard and .expanded list only methane, primary, secondary and allylic BDEs; ch10-radical-stability-rank-v2 cards; no occurrence of F2, I2, racem- or stereo- in the radical-halogenation content.

**Recommended outcome (need):** The section needs the tertiary C-H energy that closes its own argument, a statement of which halogens the reaction is practical for and why, and the stereochemical consequence of a planar radical.

##### `instr-018` — MEDIUM · assessment-readiness · confidence 0.83

**Location:** question_slug=`ch10-classify-tertiary-halide` · anchor=""surfaced": 12, "staged_variants": 12"

**Observation:** Of the 24 items only 12 surface. Those 12 are distributed 4 on organohalide structure and naming, 3 on radical halogenation, and exactly 1 each on allylic bromination, allylic radical resonance, alcohols to halides, Grignard reagents and organometallic coupling. Concept 1, the easiest and most mechanical, gets a third of the practice.

**Learner impact:** A student gets one attempt at allylic product prediction, one at PBr3, one at the Grignard route and one at coupling — no second chance to consolidate any transferable skill, while over-practising primary/secondary/tertiary labelling four ways.

**Evidence:** compiled counts {questions: 24, surfaced: 12, staged_variants: 12}; concept_slug census.

**Recommended outcome (need):** The surfaced set needs practice weighted toward the concepts carrying the chapter's transferable skills rather than its opening classification vocabulary.

##### `instr-019` — LOW · assessment-readiness · confidence 0.85

**Location:** question_slug=`ch10-allylic-site-hotspot-v2` · anchor="Focus on the carbon between the double bond and the methyl branch."

**Observation:** The hint ladder does not escalate. Level 2 both names the answer in words and highlights the single correct atom via region_focus target_ids ['atom_2'], leaving level 3 with nothing to add. The v1 twin handles this correctly, focusing both sp3 candidates.

**Learner impact:** A student who opens hint 2 for a nudge is handed the answer, so the item stops measuring whether they can locate an allylic position.

**Evidence:** ch10-allylic-site-hotspot-v2 hints[1] region_focus target_ids ['atom_2'] with answer_key.correct_option_ids [redacted]; contrast v1 target_ids ['atom_2','atom_3'].

**Recommended outcome (need):** The level-2 hint needs to narrow the field without singling out the answer, matching its own v1 twin.

**Open questions**

- instr-005 (dead further-reading links) has no good category id; none covers link resolvability, and this failure mode has recurred across chapters. Recommend adding a `reference-integrity` id or folding link checks into a compile-time guard.
- Is the compiled reader artifact simply stale relative to the current builder (which does emit practice_check and trouble_spots callouts), or were those suppressed deliberately? If stale, note the standing hazard that a recompile can revert any correction applied only to the artifact.
- The three video briefs are all status 'needs_review' and produce empty reader players. Should the video blocks be suppressed rather than emitted with an empty url?
- Every asset is a static molecule render, with no reaction-coordinate, resonance or mechanism figure. Was that a scoping decision, or did the figure types the prose leans on simply never get authored?
- The two allylic-bromination product questions ignore E/Z geometry in 1-bromo-2-butene and 1-bromo-2-pentene (both form predominantly E). Acceptable at this level, but worth confirming the course does not expect geometry.

#### Struggling Student — 5.1/10

The prose is clear, well sequenced, and unusually good at naming the trap before I fall into it. The scaffolding around that prose is where a shaky student falls off. In the compiled reader I get seven walls of continuous prose (1685-2764 characters each, no headings, no emphasis, no summary) followed by a row of unlabeled standalone structures, three empty video players, and a dead Wikipedia link. Every practice_check and every trouble_spot is stranded: the reader emits only text, molecule, video, external_link and mcmurry_link blocks, so I can never self-test while reading. The chapter also switches silently between kJ/mol and kcal/mol, which makes the C-H bond numbers look weaker than the C-I bond, and it argues the single hardest idea (early vs late transition state, Hammond) entirely in words with no energy picture and no prerequisite ever declared. Worst of all, the deepest hint on the monochlorination-count question — the exact rung I climb to when I am stuck — enumerates the hydrogen environments of 2-methylbutane incorrectly, teaching me a counting method that will fail on the next molecule.

**Publication blockers:** `stud-001`, `stud-002`

**Strengths**

- Every one of the 24 questions carries a three-level hint ladder plus targeted wrong-answer explanations, and most name the specific misconception rather than restating the answer.
- The prose repeatedly pre-empts the exact trap I would fall into, most notably 'Do not confuse the two trends; the most polar bond, C-F, is also the strongest, not the easiest to break.'
- The two error_repair items are genuinely good for a shaky student: they separate reagent, mechanism and selectivity and tell me explicitly that two of the three are fine, teaching diagnostic reading rather than pattern matching.
- Concept ordering and prerequisite chaining are clean, and the expanded tier the reader emits is a true superset of the standard tier rather than a different text.
- Every figure carries specific, teaching-oriented alt text that names the classification point rather than just the compound.

**Findings**

##### `stud-001` — BLOCKER · worked-example-gap · confidence 0.97

**Location:** question_slug=`ch10-monochlorination-count` · concept_slug=`radical-halogenation-of-alkanes` · anchor="The distinct positions are C1, the tertiary C2-H, C3, and the branch methyl; that is four."

**Observation:** The level-3 worked_step hint enumerates the wrong set of distinct hydrogen environments in 2-methylbutane. In CH3-CH(CH3)-CH2-CH3 the C1 methyl and the branch methyl are symmetry-equivalent (RDKit CanonicalRankAtoms on 'CC(C)CC' returns classes [1,4,1,3,0], putting atoms 0 and 2 in the same class), so counting them as two distinct positions is wrong, and the hint omits C4, the terminal methyl of the ethyl arm, which gives 1-chloro-3-methylbutane. The correct four are C1 (= the branch methyl), C2, C3 and C4 — exactly the four products the question's own generic_incorrect_explanation lists.

**Learner impact:** The worked step is the last rung, the one a low-confidence student opens after already failing twice. It hands back the right number, 4, obtained by a wrong method, so I walk away believing the two methyls on C2 are inequivalent and that the ethyl terminus does not count. Applied to the next substrate — or to the v2 isobutane item, whose whole point is that three methyls are equivalent — that method gives the wrong answer.

**Evidence:** topic.package.json ch10-monochlorination-count hints level 3 kind worked_step; same text in compiled/question-set.json. Contrast the item's generic_incorrect_explanation naming all four products.

**Recommended outcome (need):** The deepest hint must model a symmetry-counting procedure that is itself correct and matches the four products named in the item's own explanation; a student who follows it needs to arrive at the answer by valid reasoning, not coincidence.

##### `stud-002` — BLOCKER · retrieval-practice · confidence 0.96

**Location:** section_id=`nugget-organohalide-structure` · nugget_id=`nugget-organohalide-structure` · anchor="Is the C-I bond stronger or weaker than the C-F bond, and which of the two is more polar?"

**Observation:** All seven authored practice_check prompts and all fourteen concept trouble_spots are absent from the compiled reader, which contains only text, molecule, video, external_link and mcmurry_link blocks across all seven sections — no callout, practice or question block anywhere, and no question from the 12-item surfaced bank embedded in the reading flow.

**Learner impact:** As I read I have no way to check whether I understood a section before moving on, and no warning at the moment I am about to make the mistake the authors already anticipated (for example 'Calling a halide primary, secondary, or tertiary from the halogen instead of from the carbon it is attached to'). Students like me do not spontaneously self-quiz; if the checkpoint is not on the page, it does not happen.

**Evidence:** Compiled reader block-type census per section, e.g. nugget-organohalide-structure 7 blocks (1 text, 4 molecule, 1 mcmurry_link, 1 external_link). Package nuggets each carry a populated practice_check (7 total) and each of the 7 concepts carries 2 trouble_spots.

**Recommended outcome (need):** The retrieval and misconception scaffolding that already exists in the package needs to reach the reading surface at the point of use.

##### `stud-003` — HIGH · notation-consistency · confidence 0.93

**Location:** nugget_id=`nugget-radical-halogenation` · concept_slug=`organohalide-structure-and-naming` · anchor="about 105 kilocalories per mole for methane"

**Observation:** The chapter reports bond energies in two different units without flagging the switch or converting. Section 1 gives carbon-halogen strengths in kJ/mol and the matching question uses kJ/mol; sections 2 and 4 give C-H bond dissociation energies in kcal/mol (105, 101, 98, 88), as does the feedback on ch10-radical-stability-rank-v2.

**Learner impact:** I put the numbers side by side, because that is what the chapter trains me to do. I read C-I as 210 and an allylic C-H as 88 and conclude C-H bonds are more than twice as easy to break as the weakest carbon-halogen bond, which is backwards (88 kcal/mol is about 368 kJ/mol). On top of that, the matching question asks for C-Cl (340) and C-Br (285) values that appear nowhere in the prose.

**Evidence:** nugget-organohalide-structure text.expanded; nugget-radical-halogenation text.standard and .expanded; nugget-allylic-resonance text.expanded; ch10-cx-bond-strength-match right options.

**Recommended outcome (need):** Bond-energy numbers need to be on one comparable footing across the chapter, or the unit change made explicit at the moment it happens.

##### `stud-004` — HIGH · conceptual-support · confidence 0.9

**Location:** nugget_id=`nugget-radical-halogenation` · concept_slug=`radical-halogenation-of-alkanes` · anchor="its transition state can be analyzed with the Hammond postulate"

**Observation:** The central argument of section 2 rests on vocabulary the chapter never introduces and never declares as a prerequisite. 'Transition state', 'strongly exothermic', 'endothermic', 'early/reactant-like' versus 'late/product-like' and the Hammond postulate all arrive in a single paragraph; the concept's prerequisites list is only ['organohalide-structure-and-naming']. 'Hyperconjugation' appears for the first and only time in the feedback of ch10-radical-stability-rank, never in the prose.

**Learner impact:** This is the paragraph where I stop reading and start highlighting. I cannot picture what makes a transition state 'early', so I convert the whole thing into a slogan and memorize it. Then ch10-bromination-selectivity-error asks me to diagnose exactly this reasoning in someone else's work, which a slogan cannot do.

**Evidence:** concepts[].prerequisites for radical-halogenation-of-alkanes; nugget-radical-halogenation text.expanded; ch10-radical-stability-rank generic_incorrect_explanation.

**Recommended outcome (need):** The early/late transition-state argument needs stated prerequisites, a plain-language definition, and a way to see the energy comparison rather than only read it.

##### `stud-005` — HIGH · conceptual-support · confidence 0.94

**Location:** section_id=`nugget-radical-halogenation` · asset_id=`video-radical-halogenation` · anchor="they are drawn with fishhook (single-barbed) arrows, not the two-electron arrows of ionic mechanisms"

**Observation:** The chapter's core mechanism exists only as prose. All 17 assets are type 'molecule' — isolated structures with no arrows, no radicals drawn, no intermediates. The prose tells me radical steps use fishhook arrows and the concept's trouble_spot is 'Writing a two-electron arrow for a step that actually moves a single electron', but no figure ever shows a fishhook arrow, an unpaired electron or a propagation cycle. The only planned visual compiles to a video block with an empty url and a description that is just the first storyboard line.

**Learner impact:** I am told I will be graded on a notation I have never seen. I also cannot tell from two static structures that anything cyclic or chain-like happened between them. When the reader shows me an empty player captioned with a stage direction, I assume the site is broken and stop expecting help from the media.

**Evidence:** Compiled reader nugget-radical-halogenation blocks: 1 text, 2 molecule, 1 video with content.url '', 1 external_link. video_briefs status 'needs_review' for all three; identical empty-url blocks in nugget-allylic-resonance and nugget-grignard.

**Recommended outcome (need):** A student needs to see one full radical chain with single-electron arrows before being asked to reproduce or critique one, and the reader must not present an empty player plus a storyboard fragment as though it were the explanation.

##### `stud-006` — HIGH · conceptual-support · confidence 0.92

**Location:** section_id=`nugget-allylic-bromination` · anchor="https://en.wikipedia.org/wiki/Allylic_bromination_with_NBS"

**Observation:** Every section's 'Background reading' link is built by pasting the concept title into a Wikipedia URL, producing seven addresses that are not real article titles. The only other outbound support is a single OpenStax link in section 1 pointing at the chapter's landing page rather than any specific section; sections 2 through 7 have no working outside reading at all.

**Learner impact:** When the prose loses me — and section 2 does — the visible next move is the 'Background reading' link at the bottom of the section. It 404s. Every time. After the second dead link I stop clicking, so the one built-in escape hatch is gone.

**Evidence:** Compiled reader external_link blocks, all seven sections; mcmurry_link appears only in nugget-organohalide-structure.

**Recommended outcome (need):** Each section needs an outside-reading target that actually resolves and is specific enough to cover that section's idea.

##### `stud-007` — HIGH · worked-example-gap · confidence 0.93

**Location:** section_id=`nugget-allylic-resonance` · nugget_id=`nugget-allylic-resonance` · asset_id=`mol-but-1-ene` · anchor="one in which bromine sits on the carbon that lost the hydrogen, and one in which bromine sits on the far carbon"

**Observation:** The section the chapter itself calls 'the classic exam trap' contains no worked example. The prose never names a single molecule — not but-1-ene, not either product — and describes the two-product outcome only in generic 'near carbon / far carbon' language. Three concrete figures are attached and appear in the reader, but nothing in the prose references them, and no figure shows the delocalized radical or the two resonance structures the learning objective asks me to draw.

**Learner impact:** I cannot map 'the far carbon while the double bond has migrated' onto an actual structure because the paragraph gives me none. Three drawings appear below with names I must reverse-engineer, so I memorize the product pair and have no procedure when the exam uses 1-pentene — which is exactly what the v2 asks.

**Evidence:** nugget-allylic-resonance text tiers contain no compound name; compiled reader section blocks; learning_objectives[0] 'Draw the two resonance structures of an allylic radical'.

**Recommended outcome (need):** The two-product prediction needs walking once on a named, drawn substrate inside the reading itself, with the existing figures anchored to the sentences that use them.

##### `stud-008` — HIGH · cognitive-load · confidence 0.88

**Location:** section_id=`nugget-halides-from-alcohols` · nugget_id=`nugget-halides-from-alcohols` · anchor="If the alcohol is tertiary, HX is fast and clean. If it is primary or secondary, use PBr3 to make a bromide or SOCl2 to make a chloride."

**Observation:** The chapter teaches at least six transformations and contains zero reaction figures — no starting material, reagent, arrow, product anywhere in the 17 assets. In this section the reader shows 1-butanol, 1-bromobutane and 2-chloro-2-methylpropane as three separate captioned structures with no reagent attached, and no figure for tert-butyl alcohol even though the prose's tertiary example names it. The decision rule the section exists to deliver is a single sentence in the fourth paragraph with no table, emphasis or summary.

**Learner impact:** Reagent selection is a matching task and I need to see the pairs. Instead I hold prose in working memory while scrolling past three structures that do not tell me which reagent produced which, and on ch10-draw-pbr3-product-v2 I hesitate over whether HBr would have been acceptable.

**Evidence:** assets[] — all 17 type 'molecule'; compiled reader section blocks: 1 text (1879 chars), 3 molecule, 1 external_link; text.expanded names tert-butyl alcohol with no corresponding asset.

**Recommended outcome (need):** The substrate-class-to-reagent decision needs to be visible as a rule at a glance, and the transformations need showing as transformations rather than unconnected structures.

##### `stud-009` — HIGH · conceptual-support · confidence 0.87

**Location:** question_slug=`ch10-grignard-vs-gilman` · concept_slug=`organometallic-coupling-and-oxidation-state` · anchor="Is destroyed by protic solvents such as water"

**Observation:** One matrix cell — diorganocopper reagent, destroyed by water — has an expected answer of 'yes' that the chapter never supports. nugget-coupling-oxidation-state says nothing about cuprate stability toward protic solvents. The fact appears only in the level-3 hint and the wrong-answer explanation, and the chapter's own stated reason for preferring copper ('softer and far less basic than a Grignard reagent') pushes a reasoning student toward 'no'.

**Learner impact:** I fill the two rows I can justify and stall on the third, because the chapter just told me the cuprate is the mild, less basic reagent. Reasoning from what I was taught gives the wrong cell, and the lesson I take away is that reasoning from the text does not pay — corrosive for a student whose confidence is already low.

**Evidence:** nugget-coupling-oxidation-state text.expanded contains no mention of water, moisture or protic solvent for R2CuLi; answer_key [redacted]; hint level 3.

**Recommended outcome (need):** Any cell a student is graded on needs to be derivable from the chapter's own prose; if cuprates share the Grignard's moisture sensitivity, the reading must say so.

##### `stud-010` — MEDIUM · cognitive-load · confidence 0.82

**Location:** section_id=`nugget-coupling-oxidation-state` · nugget_id=`nugget-coupling-oxidation-state` · anchor="Two threads close the chapter: one new reaction that forms carbon-carbon bonds, and a bookkeeping skill"

**Observation:** The final section openly bundles two unrelated topics into one six-minute nugget with three learning objectives: Gilman reagent formation and coupling, and oxidation-state bookkeeping for carbon. Its single practice_check covers only the second.

**Learner impact:** Two new ideas in one sitting is one too many at the end of a chapter that has already introduced radicals, resonance, reagent selection and umpolung. Since the only checkpoint tests oxidation bookkeeping, the Gilman coupling — the actual new reaction — goes unpractised and unchecked.

**Evidence:** nuggets[] nugget-coupling-oxidation-state, duration_minutes 6, 3 learning_objectives covering both topics; practice_check addresses only oxidation state; concept difficulty 'advanced'.

**Recommended outcome (need):** The coupling reaction and the oxidation-state skill each need their own checkpoint, and the section needs a structure signalling they are two separate things to learn.

##### `stud-011` — MEDIUM · retrieval-practice · confidence 0.85

**Location:** concept_slug=`grignard-and-organometallic-reagents` · question_slug=`ch10-halide-to-alkane-route`

**Observation:** Of the 12 surfaced questions, 8 belong to the first two concepts. The four later concepts get exactly one surfaced item each, and three of those four are difficulty 'advanced'. There is no core-difficulty item anywhere for the back half of the chapter, and nothing practises the chapter's most emphasized operating rule — that a Grignard reagent cannot be made or used in a protic solvent.

**Learner impact:** My only rehearsal of Grignard chemistry is a two-step synthesis-route puzzle rated advanced. There is no low-stakes item where I simply confirm that R-MgX is destroyed by ethanol, so I never get the confidence-building success that would make me attempt the harder one.

**Evidence:** compiled counts.surfaced = 12; surfaced difficulty split 3 core, 4 standard, 5 advanced, with all three core items on concept 1. nugget-grignard practice_check asks about ethanol but no question does.

**Recommended outcome (need):** The later concepts need an entry-level rehearsal each, especially the dry/aprotic Grignard rule the prose flags as the practical takeaway.

##### `stud-012` — MEDIUM · assessment-readiness · confidence 0.9

**Location:** question_slug=`ch10-allylic-site-hotspot-v2` · anchor="Focus on the carbon between the double bond and the methyl branch."

**Observation:** The level-2 hint both states the answer in words and highlights it: a region_focus hint whose target_ids [redacted], the sole entry in answer_key.correct_option_ids. In 3-methyl-1-butene there is only one carbon 'between the double bond and the methyl branch', so the hint is a full solution at the middle rung. The parent item focuses two candidates and leaves the discrimination to the student.

**Learner impact:** The ladder collapses: I never do the reasoning step the item exists to train, and level 3 has nothing left to add. I also learn to open hint 2 immediately on every hotspot item, which removes the productive struggle from the parent version too.

**Evidence:** ch10-allylic-site-hotspot-v2 hints[1] target_ids ['atom_2'] vs answer_key.correct_option_ids [redacted]; compare v1 target_ids ['atom_2','atom_3'].

**Recommended outcome (need):** The middle hint needs to narrow the field without resolving it, matching the parent item's pattern.

##### `stud-013` — MEDIUM · sequencing · confidence 0.8

**Location:** section_id=`nugget-allylic-bromination` · nugget_id=`nugget-allylic-bromination` · anchor="which is developed fully in the next section"

**Observation:** Section 3 defers its own central justification to section 4 while still expecting the student to accept the site selectivity, and it leaves the initiation of the NBS chain circular: the text says the small amount of HBr generated in the substitution reacts with NBS to liberate Br2, then says initiation produces a bromine atom, without ever saying where the first bromine atom or the first HBr comes from.

**Learner impact:** Two 'take my word for it' moments in one short section. The circular initiation is the kind of gap where I reread the paragraph four times looking for the sentence I must have missed, then conclude I am too slow for chemistry. The concept's own trouble_spot about NBS supplying a low steady Br2 concentration never reaches the reader.

**Evidence:** nugget-allylic-bromination text.expanded paragraphs 2 and 3; concept allylic-bromination trouble_spots[1]; compiled section contains no callout block.

**Recommended outcome (need):** The section needs enough of the stability reason at the moment of use to make the site selection feel justified, and the chain's starting point stated so initiation is not self-referential.

##### `stud-014` — MEDIUM · cognitive-load · confidence 0.86

**Location:** section_id=`nugget-radical-halogenation` · anchor="Radical halogenation is the classic way to put a halogen on an unfunctionalized alkane"

**Observation:** Nothing in the compiled reader signals relative importance. Each section is a single continuous text block of 1685-2764 characters with zero markdown headings, zero bold or emphasis, and no key-takeaways or summary anywhere; the chapter has seven sections and no recap.

**Learner impact:** When everything looks equally important I highlight everything, which is the same as highlighting nothing. Reviewing before an exam means rereading roughly 15,000 characters of undifferentiated prose with no map, which is exactly when I give up and go find a video instead.

**Evidence:** Compiled reader text blocks: 2059, 2764, 1685, 2064, 1879, 2196, 2196 characters; markdown heading count 0 and bold-marker count 0 in every one; no summary section.

**Recommended outcome (need):** A student needs visible structure and an explicit signal of what matters most, within sections and at chapter close, so review is targeted rather than a full reread.

**Open questions**

- The C-X bond dissociation energies put C-I noticeably below the values usually tabulated for CH3-I; is 210 an intentional teaching approximation, and should the intermediate C-Cl and C-Br values also appear in the prose, where they currently do not?
- Are the three video briefs scheduled for production before publication, or is the reader expected to ship with three empty-url video blocks?
- Is the absence of practice_check and trouble_spot callouts a compiler-coverage gap a recompile would fix, or a deliberate decision to keep those fields off the reader surface?
- The reader emits the 'expanded' tier; are the 'terse' and 'standard' tiers reachable by an overloaded student, and is that switch discoverable?

#### Accessibility Persona — 6.0/10

The platform substrate under this chapter is unusually good: every question type it uses resolves to a keyboard-complete renderer, both structure_scaffold items set typed_structure_entry to allowed so the one keyboard_complete=false type has its documented keyboard route open, all seventeen assets carry non-empty alt text that is also shown visibly as 'Described as', and the chapter's hardest ideas are carried in prose rather than in a figure, so they are natively available non-visually. What fails is authored text, not machinery. Two structure_scaffold questions state their answer verbatim inside accessible_description, and the compile-time guard passes all 24 items because it matches answer ids, verdict vocabulary and answer-key numbers, not product names. The two hotspot items hand a non-visual student the discrimination the question tests while simultaneously giving that student no way to act on it: the stimulus image alt is the literal string 'Structure for this question' and the atom buttons are named 'C atom 1'..'C atom 4' from input-SMILES order with no bonding information. Several hint rungs also name the answer outright, including a level-2 region_focus hint whose target_ids is exactly the single correct atom id. Finally, zero of the seventeen assets author long_description even though the reader renders that field.

**Publication blockers:** `access-001`, `access-002`

**Strengths**

- Every question type this chapter uses resolves to a keyboard-complete renderer: matching and categorize render one labeled native Select per item, rank_order gives Move up / Move down buttons with position announced in the accessible name rather than drag-only, comparison_matrix is a semantic table of keyboard-reachable selects, and hotspot atoms are real buttons with aria-pressed plus a text read-back. No required activity depends on dragging, hovering or color.
- Both structure_scaffold items set typed_structure_entry to 'allowed', which opens the documented typed-SMILES route into the one question type whose contract declares keyboard_complete=false. This is the setting whose absence blocked an earlier chapter, and it is correct here on both parent and variant.
- All 17 assets carry non-empty alt text that names the compound and states the structural feature the figure exists to show; the reader also renders it visibly as 'Described as', so the description is available to every reader.
- The chapter's most difficult content is text-native: the initiation/propagation/termination chain, the Hammond early-versus-late argument, the radical stability ordering, and the resonance origin of two allylic products are all carried in prose and reach a non-visual learner in full.
- The three unproduced videos compile as blocks with is_hidden true rather than shipping empty players, so no learner meets a dead media control.

**Findings**

##### `access-001` — BLOCKER · alt-text-quality · confidence 0.97

**Location:** section_id=`nugget-halides-from-alcohols` · concept_slug=`alkyl-halides-from-alcohols` · question_slug=`ch10-draw-pbr3-product` · anchor="The expected answer is 1-bromobutane, a four-carbon chain with a bromine on the terminal carbon."

**Observation:** Both structure_scaffold questions put the graded product into accessible_description as an explicit answer statement. ch10-draw-pbr3-product reads 'Draw the product of treating 1-butanol with phosphorus tribromide. The expected answer is 1-bromobutane, a four-carbon chain with a bromine on the terminal carbon.' The v2 reads '...The expected answer is bromocyclohexane, a six-membered ring bearing one bromine.' The description is supposed to be the non-visual equivalent of the stimulus; here it is the worked solution.

**Learner impact:** A screen-reader user is told the product before drawing it and does no chemistry. The accommodation inverts into an unearned advantage, making the item unusable for grading that cohort and giving an instructor a reason to withhold the accessible path.

**Evidence:** topic.package.json question_sets ch10-draw-pbr3-product / -v2 accessibility_bundle.accessible_description; identical strings in compiled/question-set.json. find_accessibility_leaks over all 24 compiled questions returns 0 flags, because the answer_key is {'smiles': 'CCCCBr'} and the guard matches answer ids, verdict vocabulary and answer-key numbers — never a product name.

**Recommended outcome (need):** The non-visual equivalent of a draw-the-product item must convey the starting material, the reagent and the drawing task and stop there; the graded product must not appear in any field a student can read before submitting.

##### `access-002` — BLOCKER · alt-text-quality · confidence 0.92

**Location:** section_id=`nugget-allylic-bromination` · concept_slug=`allylic-bromination` · question_slug=`ch10-allylic-site-hotspot-v2` · anchor="Select the saturated carbon adjacent to the double bond, the branch-point carbon, whose hydrogen is removed in allylic bromination."

**Observation:** Both hotspot descriptions state the rule the question exists to test. ch10-allylic-site-hotspot asks which carbon's hydrogen NBS abstracts and its description answers it — 'Select the saturated carbon adjacent to the double bond' — which is verbatim the level-1 hint. The v2 goes further and appends 'the branch-point carbon', which in 3-methyl-1-butene uniquely designates one atom, so the description names the single correct target.

**Learner impact:** A non-visual student is handed the definitional mapping, and in v2 the specific atom, that a sighted student must supply from memory. The item stops measuring anything for that cohort, and the leak is asymmetric between variants, so a student who sees v2 gets more help than one who sees v1.

**Evidence:** ch10-allylic-site-hotspot accessible_description vs hints level 1; -v2 description against answer_key.correct_option_ids [redacted], which for SMILES C=CC(C)C is exactly the branch-point carbon. Both pass find_accessibility_leaks because 'allylic' and 'branch-point' are not in the verdict vocabulary.

**Recommended outcome (need):** The hotspot's non-visual equivalent must describe the structure well enough to locate every selectable atom without describing which atom satisfies the criterion in the prompt.

##### `access-003` — HIGH · media-equivalence · confidence 0.88

**Location:** section_id=`nugget-allylic-bromination` · concept_slug=`allylic-bromination` · question_slug=`ch10-allylic-site-hotspot` · anchor="Click the carbon of but-1-ene whose hydrogen NBS abstracts during allylic bromination."

**Observation:** The hotspot stimulus offers no non-visual structural readout. student_config carries only {molecule_smiles, select_count}; the renderer gives the whole picture the alt string 'Structure for this question', and each atom button is named symbol + 'atom' + index+1 — 'C atom 1' through 'C atom 4' for but-1-ene. Nothing says which carbons are doubly bonded, which are saturated, or which are adjacent. The hotspot type declares nonvisual_response_mode 'named_region_list', but the authored config supplies no regions[] with chemical names.

**Learner impact:** A blind student who knows exactly what 'allylic' means still cannot tell which of four identically-shaped buttons is the allylic carbon, because the only handle is an atom ordinal following the order the author happened to type the SMILES in. Here it happens to coincide with IUPAC numbering; nothing guarantees or states that, so the student cannot verify their own answer.

**Evidence:** [internal source reference — not in this repo] lines 235-241 and 268; [internal source reference — not in this repo] builds ids as atom_{index} over RDKit atom order; [internal source reference — not in this repo] declares nonvisual_response_mode='named_region_list'; student_config has no regions[].

**Recommended outcome (need):** Every selectable atom needs a chemically meaningful, connectivity-bearing identity available in text, keyed to the same labels the workspace controls announce. Without that the click target is reachable but not identifiable.

##### `access-004` — HIGH · interactive-fallback · confidence 0.9

**Location:** section_id=`nugget-allylic-bromination` · concept_slug=`allylic-bromination` · question_slug=`ch10-allylic-site-hotspot-v2` · anchor="Focus on the carbon between the double bond and the methyl branch."

**Observation:** The region_focus hints on both hotspot items address the student in raw internal ids that do not match the workspace controls. HintPanel renders targetIds as bare badges after 'Look at:', so the student sees 'Look at: atom_2, atom_3' while the buttons are named 'C atom 3' and 'C atom 4' — the ids are zero-based and the accessible names one-based. The same mismatch affects the error_repair level-3 hint. Separately the v2 level-2 rung sets target_ids to the single value ['atom_2'], the whole answer, two rungs into a three-rung ladder.

**Learner impact:** For a screen-reader user the hint is the fallback when the picture is unavailable, and here it points at a name that does not exist in the interface; following it lands one atom off. Sighted students are misdirected identically, since the renderer never highlights region_focus targets.

**Evidence:** [internal source reference — not in this repo] renders targetIds under 'Look at:'; [internal source reference — not in this repo] names buttons with index+1 while [internal source reference — not in this repo] ids them with index; ch10-allylic-site-hotspot hints level 2 target_ids ['atom_2','atom_3'], -v2 ['atom_2'] against correct_option_ids [redacted].

**Recommended outcome (need):** A hint that points at part of the workspace must name that part the way the workspace names it, and must narrow the search rather than collapse it.

##### `access-005` — HIGH · alt-text-quality · confidence 0.85

**Location:** section_id=`nugget-radical-halogenation` · concept_slug=`radical-halogenation-of-alkanes` · question_slug=`ch10-radical-stability-rank` · anchor="Order by increasing substitution: methyl, primary, secondary, tertiary."

**Observation:** Several hint ladders end by stating the graded answer, which the repo's own hint contract forbids. ch10-radical-stability-rank level 3 gives the correct ordering in the exact card order against correct_order [c_me, c_1, c_2, c_3]. ch10-monochlorination-count-v2 level 3 states 'One primary environment plus one tertiary environment gives two products' against answer_key.value 2. ch10-cx-bond-strength-match level 3 plus level 2's monotonic-ordering statement determines all four pairs.

**Learner impact:** Students who lean hardest on the hint ladder are the ones for whom the primary channel is degraded — screen-reader users working a rank list or matching grid without the visual gestalt. When the last rung is the answer, those students get scaffolding and integrity traded off against each other.

**Evidence:** feedback_bundle.hints: ch10-radical-stability-rank L3; ch10-radical-stability-rank-v2 L3; ch10-monochlorination-count-v2 L3; ch10-cx-bond-strength-match L2+L3. Contract: question-hint-authoring SKILL.md 'Never name the answer'.

**Recommended outcome (need):** Final hint rungs need to state the discriminating principle and leave the ordering, count or assignment for the student to execute.

##### `access-006` — MEDIUM · alt-text-quality · confidence 0.86

**Location:** section_id=`nugget-allylic-resonance` · concept_slug=`allylic-radical-resonance` · asset_id=`mol-1-bromo-2-butene` · nugget_id=`nugget-allylic-resonance` · anchor="Line structure of 1-bromo-2-butene: an internal double bond with a bromine on the terminal carbon"

**Observation:** None of the seventeen assets author accessibility.long_description; the field is empty across the whole chapter. The reader compiles it onto molecule blocks and StructureCard renders it beneath the figure when present, and the images-off path prefers long_description over alt_text. So the deeper-description affordance exists and this chapter leaves it blank, while every topic package from ch22 onward fills it on 100% of assets.

**Learner impact:** A learner working from text alone gets one sentence per figure and no route to more. For the resonance triad the whole teaching point is that the double bond has migrated between two products, and a single-sentence alt per molecule leaves the reader to hold three separate descriptions in working memory and diff them — precisely the work the picture does for a sighted reader.

**Evidence:** assets[*].accessibility contains only alt_text (0/17 long_description); [internal source reference — not in this repo] passes longDescription into StructureCard; [internal source reference — not in this repo] lines 253-255 compile it when authored; TopicPackageChapterRenderer textEquivalentBlock prefers long_description.

**Recommended outcome (need):** The figures whose teaching point is a relationship rather than a single species need a description that carries the connectivity change, not just a one-line identification of each molecule on its own.

##### `access-007` — MEDIUM · alt-text-quality · confidence 0.83

**Location:** section_id=`nugget-radical-halogenation` · concept_slug=`radical-halogenation-of-alkanes` · asset_id=`mol-2-methylbutane` · nugget_id=`nugget-radical-halogenation` · anchor="with primary and secondary hydrogens elsewhere"

**Observation:** This asset's declared learning_goal is 'Identify primary, secondary, and tertiary C-H environments in one molecule', and it is the substrate the whole selectivity section and two questions are built on. Its alt text names the tertiary position but places the other two only as 'elsewhere', so it names the categories without locating them. The word 'central' is also imprecise for 2-methylbutane, where the tertiary carbon is C2 rather than the middle of the drawn skeleton.

**Learner impact:** A non-visual learner is given the figure's conclusion for one of three environments and nothing for the other two, so the counting exercise the figure was built to support cannot be done from the description. That the same molecule is the stimulus of ch10-monochlorination-count and ch10-bromination-selectivity-error makes the gap load-bearing.

**Evidence:** assets mol-2-methylbutane learning_goal and accessibility.alt_text, SMILES CC(C)CC; referenced by ch10-monochlorination-count (answer_key.value 4.0) and ch10-bromination-selectivity-error.

**Recommended outcome (need):** The description of a figure whose purpose is to expose several hydrogen environments has to enumerate those environments by position.

##### `access-008` — MEDIUM · media-equivalence · confidence 0.8

**Location:** section_id=`nugget-allylic-resonance` · concept_slug=`allylic-radical-resonance` · asset_id=`video-allylic-resonance` · nugget_id=`nugget-allylic-resonance` · anchor="Fade between the two resonance structures, then merge them into a single delocalized picture"

**Observation:** The three video briefs carry a storyboard and a narration_outline but no caption, transcript or accessibility field, and the split is the wrong way round for non-visual access: the meaningful visual changes live in the storyboard while narration_outline states conclusions about them. All three compile into the reader as video blocks with url '' and is_hidden true, so nothing is broken today, but the briefs as written would be produced with narration that talks about the visuals rather than describing them.

**Learner impact:** When produced, a learner who cannot see the animation will hear that the arrows move one electron without hearing what is moving from where to where, and will hear the word umpolung without the charge flip that defines it. That is the entire content of the allylic-resonance video, the chapter's only treatment of why two products form.

**Evidence:** video_briefs keys are storyboard, narration_outline, formats, status 'needs_review' — no transcript or accessibility key. Compiled blocks blk-7ptuptk9, blk-pvumshtv, blk-8q97zw4i all url '' and is_hidden true.

**Recommended outcome (need):** Before production each brief needs a committed text equivalent that narrates the state changes themselves — what moves, from which atom to which — since the information is in the motion, not in speech.

##### `access-009` — LOW · keyboard-operability · confidence 0.82

**Location:** section_id=`nugget-organohalide-structure` · nugget_id=`nugget-organohalide-structure` · anchor="A polar C-X bond, and three ways to classify the carbon that carries it"

**Observation:** Heading levels skip a rank in the compiled reader view. TopicPackageChapterRenderer emits the chapter title as h1 and each section title as h2, then every figure card inside a section is an h4. There is no h3 anywhere, so a screen-reader user navigating by heading level jumps h2 to h4 seven times.

**Learner impact:** Heading navigation is the main way a screen-reader user skims a long chapter, and a skipped level makes the outline read as if content is nested one level deeper than it is.

**Evidence:** [internal source reference — not in this repo] lines 179 and 202; [internal source reference — not in this repo] lines 188, 304, 382, 404, 515, 542, 586 all Heading as='h4'. Applies to all 7 sections.

**Recommended outcome (need):** Figure and link cards inside a section need to sit one level below their section heading. This is a platform-level layout property, not something this chapter's package can express.

**Open questions**

- The compiled reader contains zero callout blocks, so the 14 trouble_spots and 7 practice_check items reach no reader surface. The builder does emit both as callouts, but that code landed after the artifact was last written. Is a recompile planned, and will the artifact be diffed against the package first, given this chapter has previously received corrections applied only to the compiled file?
- The hotspot pattern behind access-003 is cohort-wide: all 13 topic packages with hotspot items supply only {molecule_smiles, select_count} and none author a named regions[] list. Should the fix be authored per question, or should the renderer derive connectivity-bearing accessible names from the bond topology it already receives?
- All 24 questions are demo_eligible=false and publishing.available=false, and the static reader preview carries 12 prompt-only cards with no student_config and no accessibility_bundle. If those preview cards ever become answerable, the missing accessible descriptions there would be a separate gap.
- I did not verify whether matching_pairs left-hand structure_smiles actually renders in MatchingRenderer. If it does not, the item degrades to text names only — harmless for this persona, but it means sighted and non-visual students get the same stimulus for a reason no one intended.

#### Learner with Visual Preference — 4.6/10

The prose is unusually clear and the alt text consistently well written, but the chapter is visually monotonous in a way that leaves its hardest ideas unsupported. All 17 authored assets are of one type (molecule), and they compile into 19 reader blocks that are each a single isolated line structure. There is no energy profile, no mechanism sequence, no orbital or resonance picture, and no transformation figure anywhere — yet five of the seven sections teach a transformation, and the chapter's central explanatory move (Hammond early-vs-late transition state deciding Cl/Br selectivity) is carried entirely by a paragraph that literally refers to 'the Hammond picture'. The three visuals that would have covered the radical chain, allylic delocalization and the Grignard polarity reversal exist only as video_briefs with status needs_review; they compile to url '' blocks flagged is_hidden true, and only storyboard[0] survives into the block. Several figures cannot deliver their own stated learning_goal because no highlight, annotation or hydrogen-display option is used. One figure pair reads as a substrate/product pair that loses a carbon. On the assessment side, every authored structure_smiles in the question set is dropped by the renderers, so six questions tagged representation_tags ['molecule'] reach students as text-only name-recognition items. None of the checked recurring hazards apply here — no reaction_coordinate asset to mis-coerce, no synthesis_roadmap, no annotation_font_scale — and no selected-response question illustrates only some of its options.

**Publication blockers:** _none_

**Strengths**

- Every one of the 17 authored assets compiles into a reader block — no asset type is silently dropped, because all assets are the fully-supported molecule type.
- Alt text is present on all 17 assets and is genuinely informative rather than a restatement of the title; several entries name the specific carbon and the reason it matters, so the images-off reader path preserves real chemistry.
- The three chemistry-specific figures that are structurally subtle are correct: mol-vinyl-chloride is the only asset that needed explicit hydrogens and is the only one that sets show_hydrogens; mol-3-bromo-1-butene and mol-1-bromo-2-butene correctly show the shifted double bond distinguishing the two allylic products.
- None of the recurring figure hazards apply: no reaction_coordinate asset with an out-of-range barrier height, no synthesis_roadmap with an unread edges list, and no annotation_font_scale above 1.0 anywhere.
- No selected-response question illustrates only some of its options — every option list is uniformly illustrated or uniformly text.
- The hotspot questions are the one place the chapter gets structure-based interaction right: molecule_smiles is enriched into a renderable molecule with per-atom regions, so the atom the learner must identify is genuinely visible and clickable.

**Findings**

##### `visual-001` — HIGH · visual-opportunity · confidence 0.94

**Location:** section_id=`nugget-radical-halogenation` · concept_slug=`radical-halogenation-of-alkanes` · nugget_id=`nugget-radical-halogenation` · anchor="so by Hammond the transition state is early and reactant-like"

**Observation:** The chapter's central explanatory argument — that chlorination is unselective because its hydrogen-abstraction transition state is early and reactant-like, while bromination is selective because its transition state is late and radical-like — is delivered entirely as prose. The package contains no energy-profile asset of any kind; all 17 assets are type molecule.

**Learner impact:** A learner has to hold two hypothetical transition-state geometries, their relative positions along a reaction coordinate, and their differing sensitivity to radical stability entirely in working memory while reading a 400-word paragraph. Two graded items and ch10-radical-stability-rank-v2 test exactly this reasoning, so the gap is between what the chapter explains and what it assesses.

**Evidence:** nugget-radical-halogenation expanded text. The video brief's own narration outline says 'Explain the reactivity-selectivity trade with the Hammond picture' — a picture the chapter never provides. [internal source reference — not in this repo] maps reaction_coordinate to a reader block and [internal source reference — not in this repo] renders it, so the capability exists and is unused.

**Recommended outcome (need):** The exothermic/endothermic contrast and the early-vs-late transition-state position need to be visible as a comparison of two profiles rather than reconstructed from prose.

##### `visual-002` — HIGH · visual-opportunity · confidence 0.93

**Location:** section_id=`nugget-halides-from-alcohols` · concept_slug=`alkyl-halides-from-alcohols` · asset_id=`mol-1-butanol` · anchor="Phosphorus tribromide reacts with the alcohol to convert the OH into a phosphorus-bearing leaving group"

**Observation:** Not one transformation in the chapter is drawn as a transformation. Every figure block is a single isolated species with no arrow, no reagent, and no pairing to the species it comes from or becomes. Five of seven sections teach a conversion, and in each case the reader sees only two or three unlinked structures stacked vertically.

**Learner impact:** The learner must infer the arrow, the reagent and the direction of every reaction from prose that sits above the figures. Reagent-to-substrate matching — the actual skill assessed in ch10-draw-pbr3-product and ch10-halide-to-alkane-route — is the one relationship no figure shows.

**Evidence:** Compiled blocks in nugget-halides-from-alcohols: blk-c26g7bqs, blk-xwkq40bk, blk-4ei5y6cg — three standalone molecule blocks, no reagent named in any caption. Same pattern in nugget-grignard and nugget-coupling-oxidation-state. [internal source reference — not in this repo] asset type to a reader reaction block, so this shape is supported and unused.

**Recommended outcome (need):** Each conversion needs the substrate, the reagent and the product visible as one connected statement rather than adjacent independent pictures.

##### `visual-003` — HIGH · figure-accuracy · confidence 0.86

**Location:** section_id=`nugget-radical-halogenation` · asset_id=`mol-tert-butyl-bromide` · anchor="2-Bromo-2-methylpropane, the selective bromination product"

**Observation:** The two figures in the radical-halogenation section are adjacent and captioned as substrate and product, but they are not a matched pair. mol-2-methylbutane ('a substrate with several kinds of C-H', C5) is immediately followed by mol-tert-butyl-bromide titled '2-Bromo-2-methylpropane, the selective bromination product' (C4). Read in sequence — which is how a two-figure section reads — they assert that brominating 2-methylbutane gives a product with one fewer carbon.

**Learner impact:** A learner scanning the figures before or instead of the paragraph takes away a wrong product skeleton for the chapter's headline selective reaction. The chapter's own assessment contradicts the figure pair, so a student who trusted the figures is set up to fail the item.

**Evidence:** Compiled blocks blk-n6i167px (CC(C)CC) then blk-3cu6nc2n (CC(C)(C)Br), with no substrate named in the second caption. ch10-bromination-selectivity-error states 'The major product is the tertiary bromide, 2-bromo-2-methylbutane'. The video brief pairs the same two assets.

**Recommended outcome (need):** The selective-bromination product shown must be the product of the substrate shown, or the two figures must be visibly decoupled so no substrate-to-product reading is invited.

##### `visual-004` — HIGH · figure-purpose · confidence 0.95

**Location:** section_id=`nugget-radical-halogenation` · asset_id=`mol-2-methylbutane` · anchor="Identify primary, secondary, and tertiary C-H environments in one molecule."

**Observation:** Four figures state a learning goal their rendering cannot deliver, because no asset except mol-vinyl-chloride sets any rdkit_options and none uses highlighting or atom annotation. mol-2-methylbutane asks the learner to identify primary/secondary/tertiary C-H environments in a skeletal structure that draws no hydrogens at all. mol-propene is titled 'showing the allylic position' and mol-cyclohexene says 'Identify the allylic carbons flanking the ring double bond', but neither marks any carbon. mol-hexane says 'See the C-C bond formed by joining two three-carbon fragments' while rendering a plain unbranched hexane in which the new bond is indistinguishable.

**Learner impact:** Each figure asks the learner to see something that is not drawn, so it adds nothing beyond its caption and quietly signals 'you should be able to see this' when there is nothing to see. For the C-H environment figure this is the difference between a countable picture and a counting exercise done from scratch — and ch10-monochlorination-count grades exactly that count.

**Evidence:** assets mol-2-methylbutane (CC(C)CC, no rdkit_options), mol-propene (CC=C), mol-cyclohexene (C1=CCCCC1), mol-hexane (CCCCCC). Only mol-vinyl-chloride carries rdkit_options {show_hydrogens: true}. Compiled blocks confirm no highlight payload reaches the reader.

**Recommended outcome (need):** Where a caption names a specific atom, bond or hydrogen set as the thing to notice, the learner needs that feature distinguishable in the picture itself — otherwise the figure should claim only what a bare structure can show.

##### `visual-005` — HIGH · visual-opportunity · confidence 0.96

**Location:** section_id=`nugget-allylic-resonance` · asset_id=`video-allylic-resonance` · anchor="they are drawn with fishhook (single-barbed) arrows"

**Observation:** The chapter's three most spatially demanding ideas — the radical chain drawn with fishhook arrows, the singly occupied p orbital overlapping the double bond, and the reversal of partial charge going from R-X to R-MgX — are assigned exclusively to three video_briefs, all status needs_review. The compiler emits them as video blocks with url '' and is_hidden true, and copies only storyboard[0] into the block description, discarding the remaining beats and the whole narration outline. No static figure covers any of the three.

**Learner impact:** Three sections that promise a visual deliver nothing at all, and the authored sequence — which would have served as a usable step-by-step even without animation — is discarded at compile.

**Evidence:** video-radical-halogenation, video-allylic-resonance, video-grignard-carbanion all status needs_review with 3-4 storyboard beats each. Compiled blocks blk-7ptuptk9, blk-pvumshtv, blk-8q97zw4i each url '' and is_hidden true; [internal source reference — not in this repo] returns null for hidden blocks; [internal source reference — not in this repo] sets description to storyboard[0].

**Recommended outcome (need):** Single-electron arrow flow, the p-orbital overlap that delocalizes the allylic radical, and the polarity flip at carbon all need to reach the reader in some visible form; a rendered sequence of labeled static steps would satisfy each without waiting on video production.

##### `visual-006` — HIGH · figure-purpose · confidence 0.88

**Location:** question_slug=`ch10-classify-tertiary-halide` · concept_slug=`organohalide-structure-and-naming` · anchor="Which of these compounds is a tertiary alkyl halide?"

**Observation:** Six questions author structure_smiles on their options or structures (14 occurrences, all surviving into compiled/question-set.json), but no renderer reads that field. SelectedResponseRenderer renders only option.imageUrl and option.text; MatchingRenderer, CategorizeRenderer and RouteBuilderRenderer contain no reference to smiles at all. Nothing in the backend maps structure_smiles to imageUrl.

**Learner impact:** Questions tagged representation_tags ['molecule'] reach students as text lists. 'Which of these compounds is a tertiary alkyl halide?' becomes a name-parsing exercise — '2-chloro-2-methylpropane' already announces the answer in its name — instead of the structure-reading skill the section teaches. The multi-select allylic items lose the double-bond migration that is the point of the question.

**Evidence:** Affected: ch10-classify-tertiary-halide (3 options), -v2 (3), ch10-allylic-two-products (4), -v2 (4), ch10-cx-bond-strength-match-v2 (4 left items), ch10-halide-to-alkane-route and -v2. [internal source reference — not in this repo]; [internal source reference — not in this repo]. A repo-wide grep for structure_smiles in frontend/src returns only the question-bank editor and reasoning-part forms.

**Recommended outcome (need):** Where the chapter's own tags say a question is answered from a structure, the structure has to be visible at answer time; otherwise these items silently test nomenclature decoding.

##### `visual-007` — MEDIUM · figure-purpose · confidence 0.85

**Location:** section_id=`nugget-organohalide-structure` · nugget_id=`nugget-organohalide-structure` · anchor="Look only at the carbon bearing the halogen and count how many other carbons are attached to it"

**Observation:** Every figure in every section is appended after the complete section prose, never beside the sentence it supports, and no figure is numbered or referenced from the text. Section 1 ends with four consecutive full-width single-structure cards (secondary, tertiary, primary, vinylic) that are conceptually one comparison but are presented as four unrelated pictures a screen apart.

**Learner impact:** The comparison the section is built around — that classification is decided by the carbon, not the halogen — is exactly the kind of relationship a side-by-side makes obvious and a vertical stack does not. A learner must scroll back through four paragraphs to connect a structure to the sentence that explains it.

**Evidence:** Compiled section nugget-organohalide-structure: blk-o2iwmre3 (2059-char text) then blk-eqjks3m7, blk-cblptuxb, blk-byaym1yt, blk-qydi8u8n. [internal source reference — not in this repo] _build_section appends all assets after the single text block by construction. No occurrence of the word 'figure' anywhere in the package prose.

**Recommended outcome (need):** The primary/secondary/tertiary/vinylic contrast needs to be seeable in one glance rather than assembled from four separately-scrolled cards.

##### `visual-008` — MEDIUM · visual-redundancy · confidence 0.9

**Location:** section_id=`nugget-halides-from-alcohols` · asset_id=`mol-tert-butyl-chloride` · anchor="tert-butyl alcohol plus HCl gives tert-butyl chloride essentially on mixing"

**Observation:** Two assets are reused in a second section carrying the caption and learning_goal written for their first appearance. In nugget-halides-from-alcohols, mol-tert-butyl-chloride still reads 'Recognize a tertiary carbon bearing the halogen' rather than identifying it as the HX product, and mol-1-bromobutane reads 'Follow a primary halide into organometallic chemistry' in the section where it is the PBr3 product. Meanwhile tert-butyl alcohol, the starting material the prose names, is not shown at all.

**Learner impact:** The section that teaches 'which reagent for which alcohol class' shows a chloride whose caption says nothing about HX, a bromide whose caption points forward to a different section, and no tertiary alcohol — so the figures cannot be read as the reagent-selection story the prose tells.

**Evidence:** Compiled blk-4ei5y6cg and blk-xwkq40bk in nugget-halides-from-alcohols carry byte-identical name/description to blk-cblptuxb (section 1) and blk-p7964bwh (section 6). Package assets each list two nugget_ids but one caption.

**Recommended outcome (need):** A figure reused in a second section needs a caption explaining its role there; and the alcohol the prose uses as its worked HX example should be visible alongside the halide it produces.

##### `visual-009` — MEDIUM · visual-opportunity · confidence 0.9

**Location:** section_id=`nugget-grignard` · concept_slug=`grignard-and-organometallic-reagents` · anchor="so it is electron rich and behaves like a carbanion"

**Observation:** The Grignard reagent itself is never depicted. The section's two figures are 1-bromobutane and butane — the species before and after — while R-MgX, the new species the section exists to introduce, and the polarity reversal that defines it, appear only in words. The same is true of R2CuLi in the following section.

**Learner impact:** The umpolung is a claim about where electron density sits on one carbon, which is a property of a drawing more than of a sentence. Learners are asked to accept the inversion, then apply it in two graded items, without ever having seen the two polarities side by side. The chapter's own trouble spot names this exact confusion.

**Evidence:** Concept trouble spot: 'Forgetting that the carbon of R-MgX is electron rich, the opposite polarity of the carbon in R-X'. Section assets are only mol-1-bromobutane and mol-butane. video-grignard-carbanion storyboard beat 2 is unrendered and hidden.

**Recommended outcome (need):** The learner needs to see the same carbon carrying opposite partial charges in R-X and R-MgX; the reversal is the section's single most important idea and has no visual anchor.

##### `visual-010` — MEDIUM · visual-opportunity · confidence 0.91

**Location:** section_id=`nugget-allylic-resonance` · concept_slug=`allylic-radical-resonance` · anchor="with half the spin density at each end when the two ends are equivalent"

**Observation:** The delocalized allylic radical — the object the whole section is about — is never drawn. The section shows the alkene and the two products, but neither the pair of resonance structures nor the merged delocalized picture the prose describes at length. The section's own trouble spot warns against 'Treating the two resonance structures as separate molecules that interconvert', which is precisely the misconception a single delocalized drawing corrects and two prose paragraphs do not.

**Learner impact:** The learner is shown a starting alkene and two products with no visible intermediate connecting them, so the reason there are two products has to be taken on faith. This is the chapter's stated 'classic exam trap' and is graded twice.

**Evidence:** Section assets mol-but-1-ene, mol-3-bromo-1-butene, mol-1-bromo-2-butene — all closed-shell species. Expanded text: 'it is spread across the first and third carbons... Neither drawing alone is the molecule'.

**Recommended outcome (need):** The learner needs to see the radical species itself — both the two-structure representation and the fact that it is one delocalized species — positioned between the substrate and the two products.

##### `visual-011` — MEDIUM · visual-opportunity · confidence 0.83

**Location:** section_id=`nugget-halides-from-alcohols` · concept_slug=`alkyl-halides-from-alcohols` · anchor="The decision rule is compact."

**Observation:** This section teaches a two-dimensional decision (alcohol class x reagent -> product halogen) and explicitly calls it 'a compact decision rule', but presents it as three isolated structures and a paragraph. Nothing in the reader shows the mapping HX->tertiary, PBr3->bromide, SOCl2->chloride as a single visible structure.

**Learner impact:** Reagent selection is the skill assessed by ch10-draw-pbr3-product and its variant, and it is the kind of small lookup relationship a learner would otherwise re-derive from prose every time.

**Evidence:** Expanded text: 'If the alcohol is tertiary, HX is fast and clean. If it is primary or secondary, use PBr3 to make a bromide or SOCl2 to make a chloride.' Section figures name no reagent.

**Recommended outcome (need):** The substrate-class-to-reagent mapping needs to be visible as a single compact comparison, since the chapter itself frames it as a lookup rule.

##### `visual-012` — LOW · figure-purpose · confidence 0.8

**Location:** question_slug=`ch10-halide-to-alkane-route` · anchor="butylmagnesium bromide"

**Observation:** In both synthesis_route variants the intermediate list is asymmetrically illustrated: the correct step-1 product (m_grignard) is the only intermediate authored without structure_smiles, while the two distractor/target intermediates both carry one. Harmless in the current reader, since RouteBuilderRenderer renders intermediates as plain option text, but the authored asymmetry marks the correct answer as the odd one out and would become a visible tell the moment intermediates are illustrated.

**Learner impact:** If these options are ever rendered as drawn structures, a learner who notices one choice looks different can select the step-1 answer without reasoning about Grignard formation at all.

**Evidence:** ch10-halide-to-alkane-route intermediates: m_grignard (no structure_smiles), m_butane (CCCC), m_octane (CCCCCCCC); same shape in -v2. Answer key first step is {reagent_id: r_mg, product_id: m_grignard}.

**Recommended outcome (need):** Options in one list should be presented in a uniform representation so visual difference never correlates with correctness.

##### `visual-013` — LOW · alt-text-quality · confidence 0.82

**Location:** asset_id=`mol-hexane` · section_id=`nugget-coupling-oxidation-state` · anchor="the product of coupling two propyl fragments through a diorganocopper reagent"

**Observation:** Two alt texts describe content the corresponding image does not contain. mol-hexane's alt asserts provenance ('the product of coupling two propyl fragments') that is unrecoverable from an unbranched hexane; mol-2-methylbutane's alt describes 'one hydrogen (tertiary), with primary and secondary hydrogens elsewhere' in a skeletal drawing where no hydrogen is rendered.

**Learner impact:** A learner comparing caption to picture looks for a feature that is not there and may assume they have missed something. Conversely the alt text is carrying chemistry the figure was supposed to carry, which hides the figure's weakness from anyone auditing alt-text coverage.

**Evidence:** assets mol-hexane and mol-2-methylbutane accessibility.alt_text; neither carries long_description, and no asset in the chapter does.

**Recommended outcome (need):** Descriptions should describe what is drawn; where the description carries a relationship the figure cannot show, the figure needs to make that relationship visible.

**Open questions**

- The compiled reader artifact appears to predate the current compiler: zero callout blocks, so 14 trouble spots and 7 practice checks reach no reader. Outside my rubric, but it means any recompile will change the block list I reviewed — and the reverse-risk noted elsewhere in this repo (a recompile discarding artifact-only corrections) should be checked before recompiling.
- All 7 external_link blocks point at Wikipedia URLs generated from the concept title. These are almost certainly dead. Not a visual finding, so I did not file it, but it affects every section.
- Is mol-hexane intended to teach cross-coupling or homocoupling? The prose emphasizes joining R and R' into R-R', while the asset is titled 'a homocoupling product'.
- Is there another rendering surface (deck, LMS tutorial player, print export) that does convert question structure_smiles into a drawn structure? I verified the activity-renderer path only, so visual-006 is scoped to that surface.

### Orchestrator decisions

#### `rec-001` — The 'selective bromination product' figure loses a carbon (blocker)

- **Need:** The product depicted for radical bromination must be the product of the substrate depicted beside it, and the video brief and the graded error_repair item must name the same compound.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** Corrected in place by changing the asset's SMILES and title from the C4 tert-butyl bromide to the C5 2-bromo-2-methylbutane. That single edit realigns the figure, the video storyboard that references the asset id, and the error_repair key simultaneously — no new asset and no prose change is required.
- **Consolidates:** `instr-001`, `visual-003`

#### `rec-002` — The deepest hint teaches a wrong symmetry analysis (blocker)

- **Need:** The final rung of the monochlorination hint ladder must model a hydrogen-environment count that is itself correct and that matches the four products the item's own explanation names.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** The item's number is right and its generic explanation is right; only the worked step's enumeration is wrong. Rewriting that one hint text — plus the ambiguous '3' distractor explanation — is the least-complex fix and leaves the answer key untouched.
- **Consolidates:** `instr-002`, `stud-001`

#### `rec-003` — Both structure_scaffold items state their own answer (blocker)

- **Need:** The non-visual equivalent of a draw-the-product item must convey the substrate, the reagent and the task, and must not name the product.
- **Chosen intervention:** `text-equivalent` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** There is no spatial stimulus to reconstruct for these items — the prompt is a sentence — so a corrected text equivalent fully addresses the need. The compile guard structurally cannot catch this class (the key is a SMILES under `smiles`), so it needs an author-side fix.
- **Consolidates:** `access-001`

#### `rec-004` — Hotspot items name the answer atom, and are unanswerable without vision once that is removed (blocker)

- **Need:** A non-visual learner must be able to locate the allylic carbon by applying the definition, which requires the structure's connectivity keyed to the labels the atom buttons announce — without being told which atom qualifies.
- **Chosen intervention:** `structured-chemical-description` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** Deleting the leaked clause alone would convert an answer giveaway into an access blocker, because the buttons announce only 'C atom N'. A structured per-atom readout authored against the same 1-based input-SMILES numbering closes the leak and restores independent access in one edit — the remedy already used for ch8 and ch9 — with no renderer change.
- **Consolidates:** `access-002`, `access-003`

#### `rec-005` — Seven fabricated Wikipedia links, reverted by recompile for the second time (high)

- **Need:** Every offered background-reading target must resolve to a real, on-topic page, and the fix must survive the next compile.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** Commit [commit ref — not in this repo] already established seven correct targets, but wrote them into the compiled artifact only, so the 2026-07-30 recompile restored the 404s. Authoring `wikipedia_title` on all seven concepts back-ports those verified targets into the source, which is the only form of the fix a recompile cannot undo.
- **Consolidates:** `instr-005`, `stud-006`

#### `rec-006` — All 7 practice checks and 14 trouble spots reach no reader (high)

- **Need:** The authored self-checks and named-trap warnings must appear in the reading flow at the section they belong to.
- **Chosen intervention:** `added-practice` → target surface `practice`
- **Why this is the least-complex option that fully addresses the need:** The content exists and is correct; the compiled artifact simply predates the callout emitter and contains zero callout blocks. A recompile surfaces all 21 items with no authoring work — but only after the artifact-drift back-port in rec-005, or the recompile would destroy the link fixes.
- **Consolidates:** `instr-006`, `stud-002`

#### `rec-007` — Chlorination is taught as purely statistical (high)

- **Need:** Students must be able to compute a real chlorination product ratio, which requires the per-hydrogen reactivity weighting rather than a head count.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The claim as written is quantitatively false (per-H reactivity is roughly 1 : 3.5 : 5, so 2-methylpropane gives about 64:36 rather than the 90:10 statistics predicts) and it undercuts the chapter's own Hammond argument, which predicts reduced-but-real selectivity. Stating the weighting in the prose and softening the distractor explanation is bounded and needs no new item.
- **Consolidates:** `instr-004`

#### `rec-008` — Mixed energy units make C-H bonds look weaker than C-X bonds (high)

- **Need:** Bond strengths quoted across the chapter must be directly comparable, since the chapter repeatedly trains students to compare them.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** Section 1 quotes C-X in kJ/mol and sections 2 and 4 quote C-H in kcal/mol with no conversion, so an allylic C-H at 88 reads as far weaker than a C-Br at 285 when it is in fact stronger. Dual-labelling the values costs a few characters and removes an order-of-magnitude error the chapter otherwise invites.
- **Consolidates:** `instr-012`, `stud-003`

#### `rec-009` — A product is misnamed and the tie-break rule is never stated (high)

- **Need:** The IUPAC name in the explanation every student reads must be correct, and the alphabetical tie-break for equal locant sets needs stating where naming is taught.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** '3-chloro-2-methylbutane' should be 2-chloro-3-methylbutane: both directions give the locant set {2,3}, so the lower locant goes to the alphabetically first substituent. One string fix plus one sentence in the naming nugget.
- **Consolidates:** `instr-003`

#### `rec-010` — Hint ladders that end on the answer (high)

- **Need:** A hint ladder must escalate without ever handing over the ordering, count or atom the item grades.
- **Chosen intervention:** `prose-edit` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** Five rungs across four items state the graded answer, and the v2 hotspot's level-2 region_focus targets the single correct atom while its own v1 twin correctly focuses two candidates. The v1 behaviour is the model; matching it is a text and target-list edit.
- **Consolidates:** `access-005`, `access-004`, `instr-019`, `stud-012`

#### `rec-011` — A graded matrix cell is not derivable from the chapter (high)

- **Need:** Every cell a student is graded on must be answerable from the chapter's own prose.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The cuprate/water cell is keyed 'yes' while the prose says only that copper is 'far less basic than a Grignard reagent', which argues the other way; the fact appears solely in a hint. Stating in the prose that a cuprate is less basic but still protonated by water fixes both the derivability gap and the apparent contradiction between the two matrix rows.
- **Consolidates:** `stud-009`, `instr-014`

#### `rec-012` — Prerequisites omit the energetics the argument stands on (high)

- **Need:** The Hammond postulate and the transition-state vocabulary the selectivity argument uses must be either declared as prerequisites or stated in place.
- **Chosen intervention:** `instructor-note` → target surface `instructor-support`
- **Why this is the least-complex option that fully addresses the need:** The consumer is concept-map sequencing and instructor planning. Adding the missing prerequisite slugs plus a one-line in-place statement of Hammond makes the gating honest without restructuring the section.
- **Consolidates:** `instr-016`, `stud-004`

#### `rec-013` — Figures promise a feature they do not draw (high)

- **Need:** Where a caption names a specific atom, bond or hydrogen set as the thing to notice, that feature must be distinguishable in the picture.
- **Chosen intervention:** `sufficient-alt-text` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** Four captions ask the learner to see something the bare skeletal render cannot show. The cheapest honest fix is to make the descriptions state positions explicitly (which also closes access-007) and to stop claiming what the render cannot deliver; adding highlights to four figures is the better outcome but is authoring scope, so it is carried as a visual opportunity.
- **Consolidates:** `visual-004`, `access-007`, `visual-013`

#### `rec-014` — The chapter's two hardest ideas are drawn nowhere (high)

- **Need:** The early-versus-late transition-state comparison, the delocalized allylic radical with fishhook notation, and the R-X to R-MgX polarity flip need to be visible where the arguments that depend on them are made.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** A description cannot substitute: these are claims about the shape of two energy curves, about spin density on one delocalized species, and about where charge sits on one carbon. All three are assigned to unproduced videos, so nothing reaches the student today. Static labelled figures would carry all three without waiting on video production. Deferred as authoring scope.
- **Consolidates:** `instr-008`, `instr-009`, `visual-001`, `visual-005`, `visual-009`, `visual-010`, `stud-005`

#### `rec-015` — No transformation in the chapter is drawn as a transformation (high)

- **Need:** Each of the five conversions the chapter teaches needs substrate, reagent and product visible as one connected statement.
- **Chosen intervention:** `new-figure` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** All 17 assets are isolated species; the reader already supports a `reaction` block type and the chapter authors zero. Reagent-to-substrate matching is the skill two items assess and the one relationship no figure shows. Deferred as authoring scope, same class as ch8 and ch9.
- **Consolidates:** `visual-002`, `visual-011`, `stud-008`

#### `rec-016` — Three learning objectives are assessed by nothing (high)

- **Need:** The chain-step sequence, reagent choice across HX/PBr3/SOCl2, and oxidation-versus-reduction assignment each need an item that requires the decision they name.
- **Chosen intervention:** `added-practice` → target surface `assessment`
- **Why this is the least-complex option that fully addresses the need:** A student can currently score fully without ever writing a propagation step, choosing among the three alcohol-to-halide reagents (SOCl2 appears in zero of 24 items), or classifying a redox change. Three items is the minimum that aligns assessment to the declared objectives. Deferred as authoring scope.
- **Consolidates:** `instr-010`, `instr-018`, `stud-011`

#### `rec-017` — Three empty video players (medium)

- **Need:** A section must not present a titled player with no source, and each planned animation needs a committed text equivalent before production.
- **Chosen intervention:** `transcript` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** The three briefs already compile as is_hidden, so no learner meets a dead control today — the live gap is that the briefs commit to no caption or transcript, and their narration outlines state conclusions about the visuals rather than describing them. Committing the storyboard beats as the text equivalent costs nothing now and is the difference between a usable and an unusable animation later.
- **Consolidates:** `instr-007`, `access-008`

#### `rec-018` — Missing supporting content in the radical section (medium)

- **Need:** The tertiary C-H bond energy that closes the chapter's own argument, the reason only Cl2 and Br2 are used, and the racemization consequence of a planar radical all need stating.
- **Chosen intervention:** `prose-edit` → target surface `prose`
- **Why this is the least-complex option that fully addresses the need:** The BDE ladder stops one rung short of the tertiary case the paragraph concludes with, and the halogen-scope and stereochemistry points are standard exam material absent from the whole package. Three sentences. Deferred below the blockers but cheap.
- **Consolidates:** `instr-017`

#### `rec-019` — Platform display gaps surfaced by this chapter (high)

- **Need:** Authored structures must reach the learner in the surfaces that already carry them, and the reader's heading outline must be contiguous.
- **Chosen intervention:** `instructor-note` → target surface `instructor-support`
- **Why this is the least-complex option that fully addresses the need:** Not fixable in the package: no renderer reads question `structure_smiles`, so 14 authored structures across six items are dropped and questions tagged representation_tags ['molecule'] arrive as text lists; region_focus target ids are zero-based while the atom buttons announce one-based names; figure headings skip h2 to h4. Recorded for the platform backlog so the chapter is not held hostage to it.
- **Consolidates:** `visual-006`, `access-009`, `visual-012`

#### `rec-020` — Polish: locant conventions, reused captions, symmetric coupling example, no long descriptions (medium)

- **Need:** One IUPAC locant convention across prose and options; captions that explain a figure's role in the section reusing it; a coupling example where the two fragments are distinguishable; a fuller description for figures whose point is a relationship.
- **Chosen intervention:** `longer-description` → target surface `figure`
- **Why this is the least-complex option that fully addresses the need:** The long_description gap is real and bounded (0/17 assets, against 100% coverage from ch22 onward) and is applied. The locant sweep and the homocoupling-to-cross-coupling change are left as recommendations: both conventions are valid, and rewriting option text risks disturbing answer matching for no chemical gain.
- **Consolidates:** `access-006`, `instr-013`, `instr-015`, `visual-007`, `visual-008`, `stud-010`, `stud-013`, `stud-014`, `instr-011`

### Merged duplicates

- **The 'selective bromination product' figure loses a carbon** (`rec-001`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-001`; Learner with Visual Preference `visual-003`. Kept at the strongest severity (`blocker`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The deepest hint teaches a wrong symmetry analysis** (`rec-002`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-002`; Struggling Student `stud-001`. Kept at the strongest severity (`blocker`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Seven fabricated Wikipedia links, reverted by recompile for the second time** (`rec-005`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-005`; Struggling Student `stud-006`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **All 7 practice checks and 14 trouble spots reach no reader** (`rec-006`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-006`; Struggling Student `stud-002`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Mixed energy units make C-H bonds look weaker than C-X bonds** (`rec-008`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-012`; Struggling Student `stud-003`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Hint ladders that end on the answer** (`rec-010`) — raised independently by 3 personas: Accessibility Persona `access-005`, `access-004`; Organic Chemistry Instructor `instr-019`; Struggling Student `stud-012`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **A graded matrix cell is not derivable from the chapter** (`rec-011`) — raised independently by 2 personas: Struggling Student `stud-009`; Organic Chemistry Instructor `instr-014`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Prerequisites omit the energetics the argument stands on** (`rec-012`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-016`; Struggling Student `stud-004`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Figures promise a feature they do not draw** (`rec-013`) — raised independently by 2 personas: Learner with Visual Preference `visual-004`, `visual-013`; Accessibility Persona `access-007`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **The chapter's two hardest ideas are drawn nowhere** (`rec-014`) — raised independently by 3 personas: Organic Chemistry Instructor `instr-008`, `instr-009`; Learner with Visual Preference `visual-001`, `visual-005`, `visual-009`, `visual-010`; Struggling Student `stud-005`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **No transformation in the chapter is drawn as a transformation** (`rec-015`) — raised independently by 2 personas: Learner with Visual Preference `visual-002`, `visual-011`; Struggling Student `stud-008`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Three learning objectives are assessed by nothing** (`rec-016`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-010`, `instr-018`; Struggling Student `stud-011`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Three empty video players** (`rec-017`) — raised independently by 2 personas: Organic Chemistry Instructor `instr-007`; Accessibility Persona `access-008`. Kept at the strongest severity (`medium`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Platform display gaps surfaced by this chapter** (`rec-019`) — raised independently by 2 personas: Learner with Visual Preference `visual-006`, `visual-012`; Accessibility Persona `access-009`. Kept at the strongest severity (`high`); every persona's learner impact is preserved verbatim in the persona reports above.
- **Polish: locant conventions, reused captions, symmetric coupling example, no long descriptions** (`rec-020`) — raised independently by 4 personas: Accessibility Persona `access-006`; Organic Chemistry Instructor `instr-013`, `instr-015`, `instr-011`; Learner with Visual Preference `visual-007`, `visual-008`; Struggling Student `stud-010`, `stud-013`, `stud-014`. Kept at the strongest severity (`medium`); every persona's learner impact is preserved verbatim in the persona reports above.

### Retained disagreements

#### Whether prose-only delivery of the chapter's mechanisms is an accessibility strength or a learning defect

- **Accessibility Persona:** "The chapter's most difficult content is text-native: the initiation/propagation/termination chain, the Hammond early-versus-late transition-state argument, the radical stability ordering, and the resonance origin of two allylic products are all carried in prose and reach a non-visual learner in full without any figure standing between them and the chemistry." Filed as a top strength.
- **Learner with Visual Preference:** "There is no energy profile, no mechanism sequence, no orbital or resonance picture, and no transformation figure anywhere — yet five of the seven sections teach a transformation." Filed as visual-001, visual-002, visual-005, visual-010, all high.
- **Organic Chemistry Instructor:** Sides with Visual Preference: instr-008 and instr-009, both high — 'Late transition state resembles the product' is a claim about the shape of two energy curves.

**Orchestrator resolution:** Identical in structure to the ch9 disagreement and resolved the same way, which is itself evidence the tension is systemic rather than chapter-specific. Accessibility is measuring redundancy — no information exists only in a figure, a genuine and unusual strength — while the other three are measuring sufficiency. Both are retained: the strength stands, and rec-014 stays at high severity, scoped so any new figure duplicates rather than replaces the prose. There is no trade-off to adjudicate because adding figures cannot reduce the prose redundancy Accessibility is crediting.

#### Whether the chapter has a hard publication blocker at all, and where it lies

- **Learner with Visual Preference:** publication_blockers: [] — despite scoring the chapter lowest of the four at 4.6/10 and filing seven high-severity findings.
- **Organic Chemistry Instructor:** publication_blockers: [instr-001, instr-002] — the wrong-carbon-count product figure and the wrong symmetry analysis in the deepest hint.
- **Struggling Student:** publication_blockers: [stud-001, stud-002] — the same wrong hint, plus the total absence of retrieval scaffolding from the reader.
- **Accessibility Persona:** publication_blockers: [access-001, access-002] — answer leaks in the structure_scaffold and hotspot items.

**Orchestrator resolution:** The Visual persona's empty blocker list is retained verbatim and is not treated as dissent: its lens is figure quality, and it is coherent to judge a chapter visually impoverished without judging any single figure disqualifying — note it nonetheless filed visual-003 (the carbon-losing figure pair) at high, independently corroborating the Instructor's blocker. Readiness is computed, not voted: six blocker-severity findings across three personas force at least `major revision`, and the access-002/access-003 pair — a required activity no non-visual learner can complete on the merits once the leak is closed — forces `blocked`. The lowest overall score in the set belongs to the persona that raised no blocker, which is exactly why the rule is 'computed, not averaged'.

#### Whether the hotspot items are the chapter's best or worst structure-based interaction

- **Learner with Visual Preference:** "The hotspot questions are the one place the chapter gets structure-based interaction right: molecule_smiles is enriched into a renderable molecule with per-atom regions, so the atom the learner must identify is genuinely visible and clickable." Filed as a strength.
- **Accessibility Persona:** access-003, high: the same items give a non-visual learner four identically-named buttons ('C atom 1'..'C atom 4') over an image whose alt is the literal string 'Structure for this question', with no bonding information at all.

**Orchestrator resolution:** Both are correct and the conflict is instructive: the hotspot is simultaneously the only item type in the chapter whose visual stimulus actually renders and the only one whose stimulus is unavailable non-visually. The orchestrator keeps both records. The fix in rec-004 is deliberately additive — a structured per-atom description — precisely so it does not disturb the visual rendering the Visual persona is crediting. Had the remedy been to strip the molecule and substitute a named region list, it would have traded one persona's strength for the other's access, which is the outcome this resolution exists to avoid.

### Places where a description is sufficient (no new asset)

- The 17 alt texts as a body: they name the compound and the structural feature the figure exists to show rather than restating the title, and the reader surfaces them visibly as 'Described as'. Only the two that describe features the render does not contain (mol-2-methylbutane, mol-hexane) need changing.
- Every response workspace in the chapter: matching and categorize are labelled selects, rank_order uses Move up / Move down with position in the accessible name, comparison_matrix is a semantic table, and hotspot atoms are real aria-pressed buttons. No keyboard alternative or alternate activity needs authoring.
- typed_structure_entry on both structure_scaffold items — already 'allowed' on parent and variant; nothing to add.
- The three unproduced videos as compiled: is_hidden with an empty url is correct behaviour, and no information currently depends on them existing.
- The concept ordering and the expanded-tier text: expanded is a true superset of standard, so the ch23/ch30/ch31 default-tier trap does not recur here and no tier needs rewriting.
- Both rank_order items: independently checked against the MechanismCardSortRenderer pre-solve trap — authored card order differs from correct_order, so neither ships pre-solved.

### Accessibility blockers

- **`access-002+access-003`** — Both hotspot descriptions state the rule the item tests (v2 uniquely designates the answer atom), and removing that clause leaves the item unanswerable without vision because the buttons announce only 'C atom N' with no connectivity. This unresolved required-access blocker is why the computed readiness is `blocked` rather than `major revision`.
- **`access-001`** — Both structure_scaffold items append 'The expected answer is ...' naming the product outright.
- **`access-004`** — region_focus hints address zero-based internal ids while the workspace announces one-based names, so following a hint lands one atom off; the v2 level-2 rung also targets the single correct atom.
- **`access-005`** — Five hint rungs across four items state the graded ordering, count or assignment, against the repo's own 'never name the answer' hint contract.

### Visual opportunities

- Two energy profiles side by side showing the early (exothermic, Cl) versus late (endothermic, Br) transition state — the chapter's own video narration calls this 'the Hammond picture' and never supplies it.
- The delocalized allylic radical drawn as one species with spin at both ends, plus its two resonance structures with the double-headed arrow, positioned between the substrate and the two products.
- One place where fishhook (single-barbed) arrow notation is actually demonstrated, since the chapter warns against misusing it and never shows it.
- The same carbon carrying opposite partial charges in R-X and R-MgX, to anchor umpolung.
- A transformation figure per reaction section — substrate, labelled arrow, product — using the reader's existing `reaction` block type, which this chapter uses zero times.
- Highlighted atoms on mol-2-methylbutane (the three C-H environments), mol-propene and mol-cyclohexene (the allylic positions), and mol-hexane (the new C-C bond), so those four captions describe something visible.
- A cross-coupling example where the two carbon fragments differ, plus renders of NBS and R2CuLi, the chapter's two signature reagents, which appear in no figure.

### Regression targets for next run

Recheck these stable `finding_id`s after revision:

- `access-001` (blocker, Accessibility Persona) — The non-visual equivalent of a draw-the-product item must convey the starting material, the reagent and the dr…
- `access-002` (blocker, Accessibility Persona) — The hotspot's non-visual equivalent must describe the structure well enough to locate every selectable atom wi…
- `instr-001` (blocker, Organic Chemistry Instructor) — The radical-bromination section needs a product depiction whose carbon skeleton is the brominated 2-methylbuta…
- `instr-002` (blocker, Organic Chemistry Instructor) — The worked step needs to name the four environments that actually exist (the two equivalent methyls on C2 as o…
- `stud-001` (blocker, Struggling Student) — The deepest hint must model a symmetry-counting procedure that is itself correct and matches the four products…
- `stud-002` (blocker, Struggling Student) — The retrieval and misconception scaffolding that already exists in the package needs to reach the reading surf…
- `access-003` (high, Accessibility Persona) — Every selectable atom needs a chemically meaningful, connectivity-bearing identity available in text, keyed to…
- `access-004` (high, Accessibility Persona) — A hint that points at part of the workspace must name that part the way the workspace names it, and must narro…
- `access-005` (high, Accessibility Persona) — Final hint rungs need to state the discriminating principle and leave the ordering, count or assignment for th…
- `instr-003` (high, Organic Chemistry Instructor) — The product name needs correcting, and the chapter needs the alphabetical tie-break rule stated in the naming …
- `instr-004` (high, Organic Chemistry Instructor) — The chlorination selectivity claim needs stating as weak-but-real rather than absent — a per-hydrogen reactivi…
- `instr-005` (high, Organic Chemistry Instructor) — Each concept needs an authored, verified target for its background-reading link, and the chapter needs section…
- `instr-006` (high, Organic Chemistry Instructor) — The student-facing chapter needs its authored retrieval checkpoints and named misconceptions present at the po…
- `instr-007` (high, Organic Chemistry Instructor) — Either the three storyboarded explanations need a working representation in the reader, or the content needs d…
- `instr-008` (high, Organic Chemistry Instructor) — The chapter needs the early-versus-late transition-state comparison in a form where the student can see the tw…
- `instr-009` (high, Organic Chemistry Instructor) — The chapter needs the allylic radical shown as one delocalized species with spin at both ends, and at least on…
- `instr-010` (high, Organic Chemistry Instructor) — The bank needs coverage of the chain-step sequence, of reagent choice across HX/PBr3/SOCl2, and of oxidation-v…
- `stud-003` (high, Struggling Student) — Bond-energy numbers need to be on one comparable footing across the chapter, or the unit change made explicit …
- `stud-004` (high, Struggling Student) — The early/late transition-state argument needs stated prerequisites, a plain-language definition, and a way to…
- `stud-005` (high, Struggling Student) — A student needs to see one full radical chain with single-electron arrows before being asked to reproduce or c…
- `stud-006` (high, Struggling Student) — Each section needs an outside-reading target that actually resolves and is specific enough to cover that secti…
- `stud-007` (high, Struggling Student) — The two-product prediction needs walking once on a named, drawn substrate inside the reading itself, with the …
- `stud-008` (high, Struggling Student) — The substrate-class-to-reagent decision needs to be visible as a rule at a glance, and the transformations nee…
- `stud-009` (high, Struggling Student) — Any cell a student is graded on needs to be derivable from the chapter's own prose; if cuprates share the Grig…
- `visual-001` (high, Learner with Visual Preference) — The exothermic/endothermic contrast and the early-vs-late transition-state position need to be visible as a co…
- `visual-002` (high, Learner with Visual Preference) — Each conversion needs the substrate, the reagent and the product visible as one connected statement rather tha…
- `visual-003` (high, Learner with Visual Preference) — The selective-bromination product shown must be the product of the substrate shown, or the two figures must be…
- `visual-004` (high, Learner with Visual Preference) — Where a caption names a specific atom, bond or hydrogen set as the thing to notice, the learner needs that fea…
- `visual-005` (high, Learner with Visual Preference) — Single-electron arrow flow, the p-orbital overlap that delocalizes the allylic radical, and the polarity flip …
- `visual-006` (high, Learner with Visual Preference) — Where the chapter's own tags say a question is answered from a structure, the structure has to be visible at a…

---
## Post-correction record

**Estimated state: major revision (not a second persona verdict).**

Not a new persona verdict. All six blocker-severity findings are resolved and the required-access blocker is addressed, which clears `blocked`. Several high-severity findings remain open by design (new figures, new assessment items, platform wiring), so the estimate does not reach `ready with minor revisions`.

### Artifact-drift check (step 6a, before any compile)

- **Performed:** before any compile, per step 6a
- **Result:** CRITICAL — 6th confirmed recompile-revert instance. Commit [commit ref — not in this repo] replaced all seven fabricated Wikipedia URLs with real articles (Haloalkane, Free-radical halogenation, N-Bromosuccinimide, Allyl group, Haloalkane, Grignard reagent, Gilman reagent) in frontend/public/reader/topic-chapters/organohalides.json ONLY, touching no package. The 2026-07-30 recompile at [commit ref — not in this repo] restored all seven 404s. Every curated value was classified and back-ported to topic.package.json as concepts[].wikipedia_title BEFORE compiling, so this recompile preserves rather than destroys them.
- **Back-ported to the package before compiling:**
 - 7 verified Wikipedia link targets, now authored as concepts[].wikipedia_title
- **Note:** Unlike ch9, ch10 had no artifact-only barrier fix to recover — the package authors no reaction_coordinate asset at all.

### Changes applied

- BLOCKER: the asset captioned 'the selective bromination product' held 2-bromo-2-methylpropane (CC(C)(C)Br, C4) while the substrate beside it was 2-methylbutane (C5). Renamed mol-tert-butyl-bromide to mol-2-bromo-2-methylbutane with SMILES CCC(C)(C)Br and a corrected title and alt text; both references (the nugget asset_ids and the video brief's visual_asset_ids) updated. Figure, video storyboard and the error_repair answer key now name the same compound. — resolves `instr-001`, `visual-003`
- BLOCKER: the level-3 worked_step hint on ch10-monochlorination-count counted the two methyls on C2 as distinct environments and omitted C4 entirely, reaching the right answer (4) by a wrong symmetry analysis. RDKit CanonicalRankAtoms on 'CC(C)CC' returns [1,4,1,3,0], confirming atoms 0 and 2 share a class. Hint rewritten to group the equivalent methyls first and to name all four real environments; the ambiguous '3' distractor explanation disambiguated. — resolves `instr-002`, `stud-001`
- BLOCKER: both structure_scaffold items appended 'The expected answer is ...' naming the product. Removed and replaced with the response-format instruction only. — resolves `access-001`
- BLOCKER: both hotspot descriptions named the target ('the saturated carbon adjacent to the double bond', and in v2 'the branch-point carbon', which uniquely designates the answer atom). Replaced with structured per-atom connectivity readouts giving bonding and hydrogen counts for every selectable atom, authored against the 1-based numbering the buttons announce and verified atom by atom against RDKit for both C=CCC and C=CC(C)C. Closes the leak without creating an access blocker. — resolves `access-002`, `access-003`
- Authored wikipedia_title on all 7 concepts, back-porting the targets from commit [commit ref — not in this repo]. All 7 emitted URLs HTTP-verified 200, replacing 7 fabricated titles verified 404. — resolves `instr-005`, `stud-006`
- Rewrote the chlorination selectivity claim: 'reacts at all available positions in rough proportion to how many of each there are' replaced with the per-hydrogen reactivity weighting (roughly 1 : 3.5 : 5 for primary : secondary : tertiary), including the worked 2-methylpropane ratio of about 64:36 against the 90:10 a bare head count predicts. The matching distractor explanation corrected. — resolves `instr-004`
- Dual-labelled the mixed energy units: the kcal/kJ relationship is now stated where the C-X values are given, again where the C-H values are given, and the allylic 88 kcal/mol is annotated with its kJ equivalent, so a student comparing an allylic C-H against a C-Br cannot conclude the C-H is weaker. — resolves `instr-012`, `stud-003`
- Corrected '3-chloro-2-methylbutane' to '2-chloro-3-methylbutane' in the explanation every student reads: both numbering directions give the locant set {2,3}, so the lower locant goes to the alphabetically first substituent (chloro). — resolves `instr-003`
- Rewrote five hint rungs that stated the graded answer (ch10-radical-stability-rank L3 gave the exact ordering; -v2 L3 fixed the last position; ch10-monochlorination-count-v2 L3 gave the count; ch10-cx-bond-strength-match L3 gave the assignment) to state the discriminating principle instead. Widened the ch10-allylic-site-hotspot-v2 level-2 region_focus from the single correct atom to the three sp3 candidates, matching the behaviour of its own v1 twin. — resolves `access-005`, `instr-019`, `stud-012` · partially addresses `access-004`
- Added the cuprate's moisture sensitivity to the coupling prose — less basic does not mean non-basic, R2CuLi is protonated by water just as a Grignard is, and the difference is one of degree — so the graded matrix cell keyed 'yes' is now derivable from the chapter, and the two matrix rows stop reading as contradictory. — resolves `stud-009`, `instr-014`
- Stated the Hammond postulate in place rather than invoking it by name, and declared the two energetics prerequisites (bond-dissociation-energy, reaction-energetics-and-transition-states) the section's reasoning assumes. — resolves `instr-016`, `stud-004`
- Closed the three gaps in the radical section: added the tertiary C-H bond dissociation energy (about 96 kcal/mol) that the paragraph's own conclusion depends on, stated why only Cl2 and Br2 are practical (fluorination uncontrollable, iodination endothermic), and stated that the planar radical intermediate makes halogenation at a stereocenter racemic. — resolves `instr-017`
- Rewrote the two alt texts that described features the render does not draw: mol-2-methylbutane now locates all three C-H environments (and states which two methyls are equivalent) instead of saying 'elsewhere', and mol-hexane no longer asserts a provenance the drawing cannot show. — resolves `access-007`, `visual-013` · partially addresses `visual-004`
- Authored long_description on all 17 assets (was 0/17, against 100% coverage in every package from ch22 onward), with the relational figures — the two allylic products, the alcohol/halide pair, the Grignard precursor and its quench product — describing the connectivity change rather than identifying each molecule in isolation. — resolves `access-006`
- Recompiled the chapter, which surfaced all 7 practice checks and 14 trouble spots as 14 callout blocks. The pre-correction artifact contained ZERO callout blocks. — resolves `instr-006`, `stud-002`

### Verification

- curl on all 7 emitted Wikipedia URLs plus the OpenStax link — 8/8 returned 200 (pre-correction: 7/8 returned 404)
- RDKit CanonicalRankAtoms('CC(C)CC') = [1,4,1,3,0] — confirms atoms 0 and 2 share a symmetry class and atom 4 is distinct, establishing the corrected hint's four environments
- RDKit per-atom readout of C=CCC and C=CC(C)C — confirms both authored hotspot descriptions match the real connectivity and hydrogen counts, atom for atom, under the 1-based numbering the buttons announce
- Topic-package compiler (proprietary toolchain, not in this repo) — clean
- Automated test suite — 173 passed
- accessibility_guard.find_accessibility_leaks over all 24 questions — 0 flagged (note: the guard also returned 0 BEFORE correction; all four leaks were semantic and invisible to it, so this is a regression check, not the evidence they are fixed)
- Compiled reader block census — callout blocks 0 -> 14; all 7 practice checks and 14 trouble spots now reach the student
- Corrected bromination SMILES CCC(C)(C)Br confirmed present in the compiled deck-creator artifact, with no occurrence of the old CC(C)(C)Br remaining
- git diff review — all changed files are chapter-derived; no unrelated aggregate churn, no reviewed asset status or curated spec replaced by generic package output

### Still recommended

- rec-014 — the chapter's two hardest ideas are still drawn nowhere: no energy profile for the early-vs-late transition state, no delocalized allylic radical, no fishhook arrow anywhere, no R-X to R-MgX polarity flip. All three are assigned to unproduced videos.
- rec-015 — no transformation in the chapter is drawn as a transformation: all 17 assets are isolated species and the reader's `reaction` block type is used zero times.
- rec-016 — three learning objectives assessed by nothing: the chain-step sequence, reagent choice across HX/PBr3/SOCl2 (SOCl2 appears in zero of 24 items), and oxidation-versus-reduction assignment.
- rec-019 — platform work no chapter edit clears: no renderer reads question `structure_smiles`, so 14 authored structures across six items are dropped and questions tagged representation_tags ['molecule'] arrive as text lists; region_focus target ids are zero-based while the atom buttons announce one-based names (access-004 is only partly addressed for this reason); figure headings skip h2 to h4.
- rec-013 (partial) — four figure captions still name a feature the bare skeletal render does not draw; the descriptions were corrected but adding highlights to mol-2-methylbutane, mol-propene, mol-cyclohexene and mol-hexane remains open.
- rec-020 (partial) — the mixed IUPAC locant conventions and the symmetric homocoupling example were deliberately NOT changed: both naming conventions are valid and rewriting option text risks disturbing answer matching for no chemical gain.
