# Chapter 6 — An Overview of Organic Reactions: chapter review

**Topic package:** `overview-of-organic-reactions` · **version:** 1 · **run:** 2026-07-31T00:00:00Z 
**Baseline publication readiness:** **BLOCKED**

> This is an AI review, not an accessibility audit of record. It reports specific barriers.

---

## Compact editorial view

### Executive summary

Chapter 6 is blocked. Four independent reviewers returned six publication blockers and the orchestrator integrity check found a seventh class of defect they could not see from the artifact alone: three verified corrections made in commit [commit ref — not in this repo] were reverted by a later recompile, restored once, and reverted again, because they were written into the compiled reader only and never back into topic.package.json. As shipped today the chapter has all six Wikipedia further-reading links resolving to fabricated URLs that return HTTP 404; a two-step energy diagram whose barrier values 'high' and 'low' are not in the renderer enum and silently coerce to 'medium', so the chapter's flagship figure draws two transition states at identical height with products at exactly reactant energy, contradicting its own alt text, its prose, its concept trouble spot and its video brief; a question prompt asserting that heating an alkyl bromide with base gives the alkene plus HBr; three accessible_descriptions that hand a screen-reader user an answer a sighted student must derive; and two rank_order items whose cards are authored in the correct order and whose renderer does not shuffle, so both submit correct untouched. Underneath the blockers the chapter's prose is the strongest part of the package and all 14 SMILES verify correct. The recurring structural theme is that authored scaffolding does not reach the student: all six practice checks, all twelve trouble spots and all eighteen learning objectives are stranded, and the chapter contains no figure of any transformation at all.

### Persona scores

| Persona | Score | Blockers raised |
|---|---:|---|
| Organic Chemistry Instructor | 5.5 | inst-001, inst-002 |
| Struggling Student | 4.4 | sstud-001, sstud-002 |
| Accessibility Persona | 5.4 | access-001, access-002, access-003 |
| Learner with Visual Preference | 4.4 | vis-001 |

Scores are advisory. Readiness is computed, not averaged: any blocker forces at least major revision.

### Ranked recommendations

| # | Recommendation | Severity | Intervention | Surface | Sources |
|---|---|---|---|---|---|
| 001 | Restore the six verified Wikipedia targets durably, in the source package | blocker | `prose-edit` | prose | inst-008, sstud-006, access-011 |
| 002 | Correct the two-step energy diagram's barrier vocabulary in the source package | blocker | `prose-edit` | figure | inst-001, vis-001, sstud-008, access-005 |
| 003 | Fix the base-mediated elimination prompt | blocker | `prose-edit` | assessment | inst-002 |
| 004 | Remove the three answer leaks from accessible descriptions | blocker | `text-equivalent` | assessment | access-001, access-002, access-003 |
| 005 | Unseed the two rank_order items | blocker | `added-practice` | assessment | access-007 |
| 006 | Recompile so practice checks, trouble spots and objectives reach the reader | high | `added-practice` | practice | inst-007, sstud-003, sstud-004, access-008, sstud-016 |
| 007 | Reassign or support the two bond-dissociation-energy questions | high | `instructor-note` | assessment | inst-003, sstud-002, sstud-019 |
| 008 | Give the chapter at least one figure showing a transformation | high | `new-figure` | figure | inst-005, sstud-005, sstud-007, vis-002, vis-006, vis-016, sstud-018 |
| 009 | Add longer descriptions to the two energy profiles | high | `longer-description` | figure | access-005, vis-017, sstud-013 |
| 010 | Resolve the two dangling prerequisite slugs | medium | `prose-edit` | instructor-support | inst-009, sstud-012 |
| 011 | Deduplicate the repeated one-step energy figure | low | `instructor-note` | figure | vis-005, inst-014, sstud-013 |

### Why each intervention was chosen

**rec-001 — Restore the six verified Wikipedia targets durably, in the source package** 
*Need:* All six further-reading links 404. The correct targets were verified and applied in commit [commit ref — not in this repo] but only to the compiled artifact, so two later recompiles reverted them. 
*Chosen:* `prose-edit` — The least-complex fix that actually holds: author wikipedia_title on each of the six concepts so _concept_wiki_title stops falling back to the concept's prose title. Adding new figures or resources would not address the defect, and re-patching the artifact would be reverted again by the next compile.

**rec-002 — Correct the two-step energy diagram's barrier vocabulary in the source package** 
*Need:* The chapter's flagship figure renders with two equal transition states and zero net free-energy change, contradicting everything written about it, because 'high' and 'low' are not valid BarrierSize values and coerce to medium. 
*Chosen:* `prose-edit` — A two-token data fix in the authored spec (high->large, low->small) restores the intended geometry. This was also applied artifact-only in [commit ref — not in this repo] and reverted; writing it into the package is what makes it durable. No new figure is needed - the existing one renders correctly once the values are valid.

**rec-003 — Fix the base-mediated elimination prompt** 
*Need:* The prompt states that heating 2-bromo-2-methylpropane with a base gives 2-methylpropene plus HBr. With a base present HBr is not a product. 
*Chosen:* `prose-edit` — The sibling item ch6-name-reaction-class already states the same transformation correctly and neutrally, so the safe phrasing exists in the package; adopt it in both the prompt and the accessible description so the two channels do not diverge.

**rec-004 — Remove the three answer leaks from accessible descriptions** 
*Need:* Three accessible_descriptions give a screen-reader user what a sighted student must derive: the two structure_scaffold descriptions name the product, and ch6-sort-cleavage supplies the exact grading key as a gloss. 
*Chosen:* `text-equivalent` — Rewriting three description strings so they carry the stimulus and task only is sufficient and fully addresses the need. The compile guard cannot catch this class because it matches only answer ids, a verdict vocabulary and answer-key numbers, so the fix has to be authored.

**rec-005 — Unseed the two rank_order items** 
*Need:* Both ranking items author their cards in exactly the correct order and MechanismCardSortRenderer does not shuffle, seeding the answer with that order on mount, so each submits correct without the student touching a control. 
*Chosen:* `added-practice` — Reordering the authored cards is the least-complex fix and works on every input modality, including the Move up/down keyboard loop where a learner has no cue the arrangement is already the key.

**rec-006 — Recompile so practice checks, trouble spots and objectives reach the reader** 
*Need:* All six practice checks, all twelve trouble spots and all eighteen objectives are stranded in the package; the compiled reader contains no callout blocks at all. 
*Chosen:* `added-practice` — The compiler already emits these as callouts (_trouble_spots_block and _practice_check_block); this artifact simply predates that change. A recompile is sufficient and no new authoring is needed - but it must happen after rec-001 and rec-002 land in the package, or it will re-revert those fixes.

**rec-007 — Reassign or support the two bond-dissociation-energy questions** 
*Need:* Both questions tagged to the thermodynamics concept assess bond dissociation energy and radical stability, which the chapter never teaches, while its three actual objectives are assessed by nothing. 
*Chosen:* `instructor-note` — This is a scope decision, not a verified error: either the prose gains a bond-strength and radical-stability treatment or the items move to a chapter that teaches them. Recording it for the author rather than choosing unilaterally, since both routes change the chapter's declared scope.

**rec-008 — Give the chapter at least one figure showing a transformation** 
*Need:* The chapter has twelve figure blocks and not one shows a reaction: no arrow, no bond cleaving, no before/after pair linked. The curved-arrow section, which the prose calls the most transferable skill in the subject, contains no curved arrow. 
*Chosen:* `new-figure` — All four personas converged here independently. A reaction-type block already exists in the reader's supported types, so the surface is available and unused. This is a genuine authoring addition and is left as a recommendation rather than applied, since it is new content rather than a correction.

**rec-009 — Add longer descriptions to the two energy profiles** 
*Need:* Neither reaction-coordinate asset carries a long_description, so each reduces to one sentence, and the two-step alt never states that the intermediate sits above the reactants. 
*Chosen:* `longer-description` — A structured readout of the trace is the least-complex intervention: it needs no new figure and serves both screen-reader users and anyone who turns images off, where the alt text is currently all that survives.

**rec-010 — Resolve the two dangling prerequisite slugs** 
*Need:* functional-group-recognition and electronegativity resolve to no concept anywhere in the corpus, and the package sets include_in_concept_maps true, so the chapter enters the graph with two edges pointing at nothing. 
*Chosen:* `prose-edit` — A slug correction is bounded and mechanical, but choosing the right target concept is an authoring judgement about sequence, so it is recorded rather than guessed.

**rec-011 — Deduplicate the repeated one-step energy figure** 
*Need:* rc-one-step is emitted twice in consecutive sections with byte-identical content, in the two sections that exist to separate thermodynamics from kinetics. 
*Chosen:* `instructor-note` — Either annotate each instance for what its section asks the reader to read off it, or drop the second. Left as a recommendation because which of the two is correct depends on authoring intent.

### Sufficient as is (do not over-build)

- The molecule alt texts for the simple structures are adequate for identification and need no expansion.
- The prose treatment of curved arrows is self-sufficient for a non-visual learner: it narrates the mechanism arrow by arrow, so the absent figure costs a screen-reader user nothing even though it costs a sighted learner a great deal.
- The hidden video block needs no accessibility work while it remains unproduced and suppressed; the renderer correctly returns null for hidden blocks.
- The three detail tiers are correctly authored with the default expanded tier a genuine superset, so no chemistry is lost when a learner reduces detail.

### Consensus strengths

- All 14 SMILES across assets and question options verify correct in RDKit for formula, charge, radical count and hydrogen count, including the tert-butyl cation with a correct empty valence.
- The curved-arrow prose is mechanistically disciplined: tail on the electron source, an explicit prohibition on starting an arrow at a positive charge, double-barbed versus fishhook separated, and every electron accounted for across the worked example.
- The rate-limiting-step treatment is more precise than most textbooks at this level: the highest transition state, not the tallest individual barrier measured from its own valley.
- The thermodynamics/kinetics separation is handled as the chapter's central caution rather than an aside, with a well-chosen combustion example.
- Every question type renders keyboard-complete with no drag-only path, and both structure_scaffold items allow typed structure entry so no learner is locked out of the drawing tasks.
- Every authored asset reaches the compiled reader as a real block, with no empty placeholder figures, and no annotation_font_scale above 1.0 anywhere.
- No distractor is accidentally also correct in any selected-response item, and wrong-answer explanations name the specific wrong idea rather than merely negating.

### Accessibility blockers

- `access-001`
- `access-002`
- `access-003`
- `access-011`
- `access-005`

### Visual opportunities

- A worked curved-arrow transformation showing where each arrow starts and ends, with the departing bromide present so the electron bookkeeping is checkable.
- A before/after bond change for each of the four reaction classes, especially elimination and rearrangement, which currently have no structural depiction at all.
- Activation-energy and free-energy-change guides on the reaction coordinates (show_activation_labels and show_delta_labels are supported and both default off).
- A structure pinned to the intermediate minimum via minima_molecules, which the renderer supports and rc-two-step does not use.
- A catalysed-versus-uncatalysed profile on shared axes, which would correct the named catalyst trouble spot in one glance.

### Disagreements retained

**Whether the absent curved-arrow figure is a blocker**

- *Learner with Visual Preference:* High severity: the chapter grades barb-counting on arrowheads no student has ever been shown.
- *Accessibility Persona:* Explicitly a strength, not a defect: the prose narrates the mechanism arrow by arrow, so a non-visual learner loses nothing.

*Resolution:* Both are right about their own learner and neither is overridden. Kept as rec-008 at high severity rather than blocker: the access channel is genuinely intact, so this degrades learning for sighted learners rather than denying access to anyone. Recorded in sufficient_as_is that the description layer here needs no work.

**Whether the bond-dissociation-energy items are a blocker or a scope question**

- *Struggling Student:* Blocker: the answer is not reachable from the chapter, and with partial credit off a student who reasons three-quarters correctly scores zero.
- *Organic Chemistry Instructor:* High: chemically correct orderings that are simply tagged to the wrong chapter.

*Resolution:* Recorded as high, not blocker, and left uncorrected as rec-007. The chemistry is right and only the placement is wrong, so the least-complex fix is an editorial decision about scope that belongs to the author, not a verified error the orchestrator should resolve unilaterally.

**Severity of the reverted catalyst sentence**

- *Struggling Student:* Medium: 'consumed and regenerated' collides with the general-chemistry definition students arrive with.
- *Organic Chemistry Instructor:* Not raised; the instructor read the catalyst treatment as correct and complete.

*Resolution:* Both readings are defensible - the compressed phrasing is technically correct. Restored the more precise wording anyway because it is a previously reviewed correction that a recompile reverted, so this is regression repair rather than a new editorial choice.

---

## Full evidence view

Every finding from all four independent persona reviews, grouped by persona and ordered by severity. Persona reviews were isolated: each subagent saw only its own rubric and the chapter files.

### Organic Chemistry Instructor (score 5.5)

Not-go as it stands. Prose is the strongest part: the curved-arrow section is unusually disciplined, the catalyst treatment is correct, and the rate-limiting-step subtlety is stated more precisely than most texts. All 14 SMILES parse to the species their labels claim. But the chapter's central figure, the two-step energy diagram, is authored with barrier values not in the renderer enum, so both coerce to medium and it renders with two equal transition states and zero net free-energy change. A question prompt also states that heating an alkyl bromide with base gives the alkene plus HBr. Beyond the blockers, thermodynamics has zero questions on its objectives, no question asks a student to read an energy diagram or draw a curved arrow, all practice checks and trouble spots are stranded, and all six further-reading links 404.

#### `inst-001` — BLOCKER · figure-accuracy
*Location:* `asset_id`=rc-two-step · `nugget_id`=nugget-intermediates · `section_id`=nugget-intermediates
*Anchor:* “a high first barrier rises to an intermediate sitting in a shallow valley”

**Observation.** rc-two-step authors steps[0].barrier 'high' and steps[1].barrier 'low'. Neither exists in the renderer enum; BARRIER_HEIGHTS is {small:0.6, medium:1.2, large:2.0} and unrecognized values silently coerce to medium. Running the pipeline returns minima Reactants 0.0, Intermediate +1.6, Products 0.0 and peaks 2.8 and 2.8.

**Learner impact.** Every claim the chapter makes about this figure is false in the figure the student sees: two equal peaks with no identifiable highest transition state, and a zero overall free-energy change, in the one figure meant to teach which step is rate-limiting.

**Evidence.** topic.package.json rc-two-step spec; [internal source reference — not in this repo] BARRIER_HEIGHTS and the coercion at line 111; compiled reader block blk-6qsichzg carries the same spec verbatim. rc-one-step uses a valid 'medium' and renders correctly.

**Need.** The two-step profile must render with a first transition state higher than the second and a non-zero overall free-energy change, and the authored barrier vocabulary must be constrained to values the renderer recognizes so a silent coercion cannot again flatten a pedagogically loaded figure. *(confidence 0.97)*

#### `inst-002` — BLOCKER · chemical-accuracy
*Location:* `question_slug`=ch6-classify-reaction-type-v2 · `concept_slug`=reaction-classes
*Anchor:* “Heating 2-bromo-2-methylpropane with a base gives 2-methylpropene plus HBr”

**Observation.** The prompt states the products of a base-promoted dehydrohalogenation as the alkene 'plus HBr'. With a base explicitly present HBr is not a product: the base removes the proton to give its conjugate acid and the halide departs as bromide.

**Learner impact.** This is exactly the conflation later elimination chapters have to un-teach. A student who internalizes it will write HBr as a product of E2 reactions run in hydroxide or alkoxide.

**Evidence.** topic.package.json ch6-classify-reaction-type-v2 prompt_text, repeated in accessibility_bundle. The sibling ch6-name-reaction-class states the same transformation correctly and neutrally as 'A single reactant loses HBr from adjacent carbons'.

**Need.** The prompt needs to state the transformation in a way that is true of the conditions it names, and the accessible description needs the same correction so the two channels do not diverge. *(confidence 0.93)*

#### `inst-003` — HIGH · objective-alignment
*Location:* `concept_slug`=thermodynamics-of-reactions · `nugget_id`=nugget-thermo · `question_slug`=ch6-rank-bde

**Observation.** The thermodynamics concept's three objectives are assessed by nothing. Its only two questions ask students to rank bond dissociation energies, a topic absent from the prose: 'dissociation' 0 hits, 'bond strength' 0, 'stability' 0, 'tertiary/secondary/primary' 0.

**Learner impact.** A student who studies this chapter cannot answer either question tagged to its thermodynamics concept, and both are partial_credit false so three of four correct positions still scores zero on untaught content.

**Evidence.** Question-concept census: reaction-classes 4, bond-changes 4, curved-arrow 4, thermodynamics 2, kinetics 2, energy-diagrams 2. The two thermodynamics items are ch6-rank-bde and ch6-rank-bde-v2. Both orderings are chemically correct; neither is taught.

**Need.** The thermodynamics concept needs assessment reaching its own objectives, and the BDE items need either supporting prose added or reassignment to a chapter that teaches them. *(confidence 0.94)*

#### `inst-004` — HIGH · conceptual-support
*Location:* `nugget_id`=nugget-thermo · `concept_slug`=thermodynamics-of-reactions
*Anchor:* “A reaction whose standard free-energy change is negative has an equilibrium constant greater than one”

**Observation.** The chapter contains no quantitative or symbolic apparatus: no relation between the equilibrium constant and the free-energy change beyond its sign, no symbols, and no energy values anywhere ('kJ' and 'kcal' each occur zero times).

**Learner impact.** The stated objective is to relate the equilibrium constant to the standard free-energy change, but a student can only relate them as 'negative means greater than one' and cannot do the standard exercises in any of the mapped textbooks.

**Evidence.** nugget-thermo all three tiers; nugget-kinetics names activation energy but never quantifies a barrier; textbook_matching maps one-to-one onto OpenStax chapter 6, whose energetics sections are explicitly quantitative.

**Need.** The energetics sections need enough quantitative anchoring for a student to connect a sign to a magnitude and a magnitude to an observable outcome. *(confidence 0.88)*

#### `inst-005` — HIGH · visual-opportunity
*Location:* `nugget_id`=nugget-arrows · `concept_slug`=curved-arrow-notation · `section_id`=nugget-arrows
*Anchor:* “using them correctly is the single most transferable skill in the subject”

**Observation.** The chapter contains no reaction figure of any kind: zero figures showing a transformation, zero curved arrows, zero depictions of reactants converting to products. The curved-arrow section is illustrated by three disconnected static molecule cards.

**Learner impact.** Curved-arrow notation is a graphical skill taught here entirely in words, and the concept's own trouble spots are errors of drawing that are never shown correctly or incorrectly anywhere.

**Evidence.** Reader block census: 6 text, 10 molecule, 3 reaction_coordinate, 6 external_link, 1 mcmurry_link, 1 video. Concept curved-arrow-notation declares preferred_representations ['molecule'].

**Need.** The curved-arrow worked example needs to be rendered as a transformation with electron flow shown, and each of the four reaction classes needs to be visible as a bond change. *(confidence 0.92)*

#### `inst-006` — HIGH · assessment-readiness
*Location:* `concept_slug`=energy-diagrams-and-intermediates · `nugget_id`=nugget-intermediates · `question_slug`=ch6-ts-vs-intermediate-v2
*Anchor:* “Reading these features from a diagram is the practical payoff of the chapter”

**Observation.** No question in the eighteen-item set shows a student an energy diagram or asks them to identify a rate-limiting step, and no question asks them to place a curved arrow.

**Learner impact.** The chapter's two stated payoffs are reading energy diagrams and pushing arrows, and a student can score 18/18 without doing either.

**Evidence.** Question type census: 9 types x 2 variants. Only the two structure_scaffold items involve chemical drawing, both product structures. No question references rc-one-step or rc-two-step.

**Need.** The assessment needs at least one item requiring a student to read an energy profile and one requiring them to place curved arrows. *(confidence 0.91)*

#### `inst-007` — HIGH · retrieval-practice
*Location:* `section_id`=nugget-classes · `nugget_id`=nugget-classes
*Anchor:* “Hydrogen bromide reacts with but-2-ene to give 2-bromobutane”

**Observation.** All six authored practice_check items and all twelve trouble_spots are stranded in the source package and reach no reader; the compiled chapter contains no callout blocks of any kind.

**Learner impact.** Every section is uninterrupted prose followed by figures and links, so a student is never asked to produce anything, and the chapter's own diagnosis of what students get wrong never reaches them.

**Evidence.** topic.package.json defines a practice_check on each of six nuggets and two trouble_spots on each of six concepts; compiled reader block types contain no callout.

**Need.** The authored self-checks and trouble spots need to reach the reader at the point in the section where they belong. *(confidence 0.95)*

#### `inst-008` — HIGH · conceptual-support
*Location:* `section_id`=nugget-classes
*Anchor:* “Wikipedia — The four classes of organic reactions”

**Observation.** All six further-reading links are fabricated Wikipedia URLs built by slugifying concept titles, and all six return HTTP 404. The chapter has exactly one textbook link, a generic OpenStax landing page in section 1, so five of six sections have no textbook anchor.

**Learner impact.** Every outbound reading link a student can click in this chapter is dead, and each is labelled 'Background reading on ...' as if vetted.

**Evidence.** Compiled reader external_link blocks; curl -L on each returns 404. mcmurry_link to the OpenStax why-this-chapter page returns 200 and is the only textbook link.

**Need.** Every outbound link needs to resolve before this ships, and sections 2 through 6 need their own specific textbook anchors. *(confidence 0.98)*

#### `inst-009` — MEDIUM · sequencing
*Location:* `concept_slug`=reaction-classes
*Anchor:* “functional-group-recognition”

**Observation.** Two declared prerequisites resolve to no concept anywhere in the corpus: 'functional-group-recognition' and 'electronegativity' are not among the 262 distinct concept slugs. The prose also assumes pi/sigma bonding, the octet rule, lone pairs and formal charge, none declared.

**Learner impact.** The package sets include_in_concept_maps true, so the chapter enters the concept graph with two edges pointing at nothing, and the skills most likely to be the actual gap are not flagged at all.

**Evidence.** Concept slug inventory across all topic packages: no 'functional-group-recognition', no 'electronegativity'. The same dangling slug also appears in the organohalides package.

**Need.** Declared prerequisites need to resolve to concepts that exist and to cover what the prose actually assumes. *(confidence 0.9)*

#### `inst-010` — MEDIUM · sequencing
*Location:* `concept_slug`=curved-arrow-notation · `nugget_id`=nugget-thermo

**Observation.** The slug curved-arrow-notation is defined twice in the corpus, here and in acids-bases-and-curved-arrows, with different titles and prerequisites. That earlier package also owns electron-pair-donors-acceptors and free-energy-and-equilibrium-constants, all three re-taught here from scratch.

**Learner impact.** A student following the canonical sequence meets curved arrows, the nucleophile/electrophile framing, and free energy versus the equilibrium constant twice, both as first introductions.

**Evidence.** Both packages set include_in_concept_maps true and both define curved-arrow-notation.

**Need.** One chapter needs to own each idea, with the other explicitly building on it, and the duplicated slug needs to resolve to a single node. *(confidence 0.85)*

#### `inst-011` — MEDIUM · missing-example
*Location:* `concept_slug`=reaction-classes · `nugget_id`=nugget-classes · `asset_id`=mol-tert-butyl-bromide
*Anchor:* “A rearrangement, the fourth class, converts a molecule into a constitutional isomer”

**Observation.** The chapter is named for four reaction classes and depicts only one as a transformation. Elimination gets a substrate but no product, substitution's product sits in a different section, and rearrangement has no example at all.

**Learner impact.** Rearrangement is the class students most reliably fail to recognize and the chapter's own trouble spot says so, yet a student meets it as one sentence and two distractors.

**Evidence.** nugget-classes asset_ids are mol-but-2-ene, mol-2-bromobutane, mol-tert-butyl-bromide. No asset depicts a rearranged skeleton or an elimination product.

**Need.** Each of the four classes needs at least one concrete worked case, with rearrangement in particular needing an example showing the skeleton change. *(confidence 0.87)*

#### `inst-012` — MEDIUM · misconception
*Location:* `nugget_id`=nugget-bonds · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “That fragment becomes a negatively charged anion, while the fragment left behind becomes a positively charged cation”

**Observation.** Heterolytic cleavage is stated as an absolute rule producing one anion and one cation, with no qualification that this holds for a neutral substrate.

**Learner impact.** Students soon meet heterolysis of charged substrates, where products are a cation and a neutral molecule; taught absolutely, they either reject those steps or invent a charge.

**Evidence.** nugget-bonds standard and expanded tiers both state the rule without a neutral-substrate qualifier.

**Need.** The heterolysis rule needs scoping to the neutral-substrate case it actually describes. *(confidence 0.82)*

#### `inst-013` — MEDIUM · notation-consistency
*Location:* `nugget_id`=nugget-kinetics · `asset_id`=rc-one-step
*Anchor:* “the energy required to reach that maximum from the reactants is the activation energy”

**Observation.** 'Activation energy' is attached to barriers on diagrams whose axis is declared free_energy, without distinguishing the free energy of activation from the Arrhenius quantity. The equilibrium constant is also defined as 'concentrations' in the standard tier and 'activities' in the expanded tier.

**Learner impact.** Students moving between this chapter and the mapped textbooks will not know whether 'activation energy' means the same quantity, and a student switching depth tier gets two different definitions with no note.

**Evidence.** Both RC assets declare energy_axis free_energy; nugget-thermo standard vs expanded differ on concentrations vs activities.

**Need.** The barrier needs naming consistently with the axis it is drawn against, and the equilibrium-constant definition needs to be the same quantity at every tier. *(confidence 0.8)*

#### `inst-014` — LOW · visual-redundancy
*Location:* `asset_id`=rc-one-step · `section_id`=nugget-kinetics · `nugget_id`=nugget-kinetics

**Observation.** rc-one-step is emitted twice in consecutive sections with identical title, alt text and spec. The kinetics section also carries a hidden video block describing a two-step diagram that does not appear until the next section.

**Learner impact.** The repeated figure reads as a rendering glitch and costs the kinetics section the chance to show anything new.

**Evidence.** Reader blocks blk-bfmih8sd and blk-z9clr47a both carry asset_id rc-one-step with identical content; blk-7577paa7 has empty url and is_hidden true.

**Need.** Each section needs a figure that does work specific to that section, and the unproduced video brief needs a resolution. *(confidence 0.83)*

#### `inst-015` — LOW · assessment-readiness
*Location:* `question_slug`=ch6-sort-cleavage · `concept_slug`=bond-changes-radical-vs-polar

**Observation.** Two of four items in ch6-sort-cleavage restate the definitions being tested rather than requiring application. The electron-count items are also authored as numeric_with_units with a null unit hint for what is a pure count.

**Learner impact.** With partial credit on, half the sorting item is free, and the numeric type invites students to type a unit and be marked wrong.

**Evidence.** ch6-sort-cleavage items i3 and i4 are definition restatements; ch6-arrow-electron-count uses numeric_with_units with unit_hint null.

**Need.** The sorting item needs all four entries to be concrete events, and the electron-count items need a type suited to a bare count. *(confidence 0.78)*

#### `inst-016` — LOW · notation-consistency
*Location:* `asset_id`=mol-but-2-ene · `question_slug`=ch6-match-terms
*Anchor:* “But-2-ene: a four-carbon chain with a carbon-carbon double bond between the central carbons.”

**Observation.** mol-but-2-ene uses SMILES CC=CC with unspecified geometry and neither title nor alt text mentions cis/trans. Separately ch6-match-terms is tagged to kinetics-and-transition-states but two of its four pairs belong to energy-diagrams-and-intermediates.

**Learner impact.** A student just taught that structure distinguishes molecules meets an alkene whose geometry is drawn but never named, and a student practising by concept meets an intermediate question tagged to a concept that has not introduced intermediates.

**Evidence.** Asset mol-but-2-ene smiles CC=CC; ch6-match-terms concept_slug kinetics-and-transition-states with left option 'Intermediate'.

**Need.** The alkene needs its geometry specified and named or explicitly set aside, and the matching item needs tagging to the concept it assesses. *(confidence 0.75)*

**Strengths noted by this persona**

- All 14 SMILES across assets and question options verified with RDKit for formula, charge, radical count and hydrogen count, including the tert-butyl cation with a correct empty valence.
- The curved-arrow prose is mechanistically disciplined: tail on the electron source, explicit prohibition on starting at a positive charge, double-barbed vs fishhook separated, and every electron accounted for.
- The rate-limiting-step treatment is more precise than most textbooks: the highest transition state, not the tallest individual barrier measured from its own valley.
- The catalyst discussion is correct and complete and is correctly connected to a trouble spot and two questions.
- The thermodynamics/kinetics separation is handled as the chapter's central caution with a well-chosen combustion example.
- The assessment set is structurally clean: 9 types x 2 variants, all 18 slugs present in both package and compiled artifact with no drift, every variant carrying variant_of.
- No distractor is accidentally also correct in any selected-response item.
- The two bond-dissociation orderings, though untaught here, are chemically correct.
- Wrong-answer explanations are specific and teach rather than merely negate.

**Open questions**

- I coined the category 'resource-integrity' for inst-008 but remapped it to 'conceptual-support' to stay schema-valid; flagging so the id is either adopted or normalized before regression diffing.
- The invalid barrier vocabulary behind inst-001 is not unique to this chapter: 'high'/'low' also appears in alkynes-organic-synthesis, epoxides, and carboxylic-acid-derivatives.
- Do multi_select options actually render structure_smiles? If the selected-response renderer ignores the field, those questions are text-only.
- Is water intended purely as a distractor in ch6-select-nucleophiles-v2? An advanced student could defend selecting it.
- publishing.available is false and science_review.status is not_reviewed; reviewed as pre-publication.
- Do reaction_coordinate blocks render for an anonymous reader? If the render call needs a JWT the three energy figures may be invisible without an account.

### Struggling Student (score 4.4)

The prose is unusually well-written for a shaky student, but almost none of the scaffolding a struggling student needs actually reaches the reader. All six practice_check items and all twelve concept trouble_spots exist in the package and appear nowhere in the compiled reader. The curved-arrow section contains not one drawn arrow. Three of the four reaction classes are never shown, only described. Every background-reading link points at a fabricated Wikipedia article. Two hard blocks: a numeric question whose placeholder is the answer, and two bond-dissociation-energy ranking questions requiring knowledge the chapter never mentions.

#### `sstud-001` — BLOCKER · assessment-readiness
*Location:* `question_slug`=ch6-arrow-electron-count · `concept_slug`=curved-arrow-notation
*Anchor:* “e.g. 2”

**Observation.** The numeric_with_units question 'How many electrons does a single full (double-barbed) curved arrow represent in a polar mechanism?' has answer_key [redacted] and student_config.placeholder = 'e.g. 2'. Its variant ch6-arrow-electron-count-v2 asks the fishhook version with value = 1.0 and placeholder = 'e.g. 1'. Both leaks survive compilation.

**Learner impact.** A low-confidence student who does not know whether an arrow means one or two electrons reads the greyed-out example and types it, scores correct, gets no corrective feedback, and carries an untested mental model of arrow notation into every mechanism for the rest of the course.

**Evidence.** topic.package.json ch6-arrow-electron-count: placeholder 'e.g. 2' with value 2.0; ch6-arrow-electron-count-v2: placeholder 'e.g. 1' with value 1.0. Same in compiled/question-set.json.

**Need.** The placeholder text on a numeric question must not be readable as the answer; these two items need an input affordance that shows format without showing the value. *(confidence 0.97)*

#### `sstud-002` — BLOCKER · objective-alignment
*Location:* `question_slug`=ch6-rank-bde-v2 · `concept_slug`=thermodynamics-of-reactions
*Anchor:* “Rank these C-H bonds from strongest to weakest bond dissociation energy”

**Observation.** Both rank_order items assess bond dissociation energy, which the chapter never teaches. ch6-rank-bde requires the halogen bond-strength trend; ch6-rank-bde-v2 requires radical-stability ordering. The strings 'bond dissociation', 'bond strength' and 'radical stability' appear zero times in any nugget text tier and zero times in the compiled reader. Radical stability is never mentioned anywhere.

**Learner impact.** The student re-scans all six sections for a table they must have missed, finds nothing, then guesses. partial_credit is false on both items so a single inversion returns zero, and the level-2 hint asserts a fact never shown.

**Evidence.** ch6-rank-bde and ch6-rank-bde-v2 in topic.package.json and compiled/question-set.json; grep for 'dissociation' returns 0 hits in the compiled reader.

**Need.** Either the chapter must teach bond dissociation energy and radical stability, or these two items must be re-scoped to what the six sections do teach. As shipped the answer is not reachable from the chapter. *(confidence 0.94)*

#### `sstud-003` — HIGH · retrieval-practice
*Location:* `nugget_id`=nugget-classes · `section_id`=nugget-classes
*Anchor:* “Hydrogen bromide reacts with but-2-ene to give 2-bromobutane, with no small molecule lost. Which class is this?”

**Observation.** Every one of the six nuggets carries a practice_check with prompt and answer. None reach the compiled reader; grepping for 'practice_check' or 'callout' returns zero hits. There is no checkpoint of any kind between the start of the chapter and the end.

**Learner impact.** The student reads six long prose blocks with nothing asking them to stop and produce an answer, finishes feeling they understood because they recognized the words, then cannot do any of the question bank.

**Evidence.** topic.package.json nuggets nugget-classes, nugget-bonds, nugget-arrows, nugget-thermo, nugget-kinetics, nugget-intermediates each have a practice_check; the compiled reader contains none of these strings.

**Need.** The six authored self-checks already exist and are good; they need to surface as checkpoints inside the reading so a shaky reader gets interleaved retrieval instead of an unbroken wall of prose. *(confidence 0.96)*

#### `sstud-004` — HIGH · misconception
*Location:* `concept_slug`=curved-arrow-notation · `section_id`=nugget-arrows
*Anchor:* “Drawing a curved arrow from a positive charge instead of from the electron source”

**Observation.** All six concepts declare trouble_spots - twelve named wrong moves. Zero reach the compiled reader as a distinct flagged warning. A few are restated mid-paragraph with no visual weight; several are not restated at all.

**Learner impact.** The chapter privately knows the exact five things the student will get wrong and tells them none in a form they would notice. They make the standard error and have no idea it was a documented, expected error rather than personal failure.

**Evidence.** concepts[].trouble_spots in topic.package.json (12 entries across 6 concepts); no 'trouble' or 'callout' string in the compiled reader.

**Need.** The named wrong moves need to reach the reader as visually distinct warnings attached to the section that teaches the rule. *(confidence 0.95)*

#### `sstud-005` — HIGH · worked-example-gap
*Location:* `section_id`=nugget-arrows · `nugget_id`=nugget-arrows · `concept_slug`=curved-arrow-notation
*Anchor:* “using them correctly is the single most transferable skill in the subject”

**Observation.** The section on curved arrows contains no curved arrow. Its four visual blocks are three separate unconnected static structures plus a dead external link. The entire two-arrow worked example is delivered verbally. The reader never shows where a tail sits, where a head points, or what two arrows look like on one drawing. Bromide, the co-product, is not shown.

**Learner impact.** This is the single place a struggling student would quit. Told this is the most important skill in organic chemistry, given a three-paragraph verbal description of a picture, then asked to produce a product on a blank canvas.

**Evidence.** Section nugget-arrows blocks: blk-dgrj1bpn (text), blk-ga6ay38x, blk-44rek1nv, blk-o6pirqko (three isolated molecule blocks), blk-jjm0ge0j (external_link).

**Need.** The hydroxide + bromomethane step needs a representation in which the two electron-pair movements are visible and located on the structures. *(confidence 0.93)*

#### `sstud-006` — HIGH · conceptual-support
*Location:* `section_id`=nugget-classes · `asset_id`=blk-09dge7hl
*Anchor:* “https://en.wikipedia.org/wiki/The_four_classes_of_organic_reactions”

**Observation.** All external_link blocks point to Wikipedia URLs generated by slugifying the concept title rather than naming a real article. None are Wikipedia article titles; two contain a colon, which Wikipedia reserves for namespaces. Each is labeled 'Background reading'.

**Learner impact.** The 'Background reading' link is the first thing a stuck student clicks. Every one lands on 'Wikipedia does not have an article with this exact name.' After the second dead link the student stops trusting the chapter's supporting material entirely.

**Evidence.** Blocks blk-09dge7hl, blk-n1eskfzv, blk-jjm0ge0j, blk-k1rynreb, blk-fe5g69ob in the compiled reader; each content.url is the concept title with underscores.

**Need.** Each section's background-reading link must resolve to a real article; an unauthored title-to-URL derivation cannot be trusted, and a 404 is worse for a struggling reader than no link. *(confidence 0.92)*

#### `sstud-007` — HIGH · missing-example
*Location:* `section_id`=nugget-classes · `concept_slug`=reaction-classes
*Anchor:* “commonly through the migration of a hydrogen or an alkyl group to a neighboring, electron-poor atom”

**Observation.** The section defining four reaction classes shows a worked instance of exactly one. Rearrangement gets no structure at all, only a sentence. Yet 'Rearrangement' is offered as a distractor in both classify items, and the concept's own trouble spot warns against treating rearrangement as rare.

**Learner impact.** The student can classify addition because they were shown one. For the other three they pattern-match on question wording rather than chemistry. Rearrangement is a word read and never seen, so they default to eliminating it - a guessing strategy.

**Evidence.** Compiled reader section nugget-classes blocks blk-n6cjnrwt, blk-5kh1km8m, blk-p12kspwl; no structure anywhere for a rearrangement or for 2-methylpropene.

**Need.** Each of the four classes needs a concrete shown-not-told instance with starting material and product, especially rearrangement. *(confidence 0.9)*

#### `sstud-008` — HIGH · misconception
*Location:* `asset_id`=rc-two-step · `section_id`=nugget-intermediates · `concept_slug`=energy-diagrams-and-intermediates
*Anchor:* “the first step is rate-limiting”

**Observation.** The only multistep energy profile is specced step 1 endergonic/high and step 2 exergonic/low, and its alt text ends 'the first step is rate-limiting.' The concept names as a trouble spot 'Assuming a two-step profile always has a rate-limiting first step' - and that warning never reaches the reader.

**Learner impact.** The student generalizes from the one picture given. They will confidently answer 'the first step' on any future rate-limiting question, and the chapter will have taught that error rather than prevented it.

**Evidence.** assets[] entry rc-two-step spec and accessibility.alt_text; concept energy-diagrams-and-intermediates trouble_spots[1]; compiled reader block blk-6qsichzg.

**Need.** The chapter needs a contrasting profile or explicit counterexample so 'highest transition state wins' is learned as a rule; the authored warning also needs to reach the reader. *(confidence 0.88)*

#### `sstud-009` — MEDIUM · misconception
*Location:* `section_id`=nugget-kinetics · `nugget_id`=nugget-kinetics
*Anchor:* “It is consumed and regenerated, and it lowers the barrier equally in both directions”

**Observation.** The expanded text shown in the reader describes a catalyst as 'consumed and regenerated'. Technically correct but the compressed phrasing collides with the definition every student arrives with - 'a catalyst is not consumed'. The standard and terse tiers omit the clause entirely, so framing is inconsistent across tiers.

**Learner impact.** The student either decides their general-chemistry definition was wrong and starts answering that catalysts are used up, or decides the chapter contradicts itself and loses confidence in the section.

**Evidence.** nugget-kinetics text.expanded third paragraph; compiled reader block blk-hmwc5eca; the standard tier says only 'it lowers the barrier for the forward and reverse directions equally'.

**Need.** The consumed-then-regenerated point needs enough unpacking that it reconciles with 'not consumed overall' rather than contradicting it. *(confidence 0.82)*

#### `sstud-010` — MEDIUM · cognitive-load
*Location:* `section_id`=nugget-thermo · `nugget_id`=nugget-thermo
*Anchor:* “the ratio of product to reactant activities once the system has settled”

**Observation.** The reader shows the expanded tier, which defines the equilibrium constant using 'activities' and never defines it. The standard tier says 'the ratio of product to reactant concentrations at equilibrium', which is actionable for an introductory student.

**Learner impact.** 'Activities' is the first noun in the definition of the chapter's central thermodynamic quantity and the student has never met it. They either guess-substitute 'concentrations' or decide the section is above them and skim the rest.

**Evidence.** nugget-thermo text.expanded first paragraph vs text.standard first sentence; compiled reader block blk-zw47cwys.

**Need.** The reader-facing tier needs the equilibrium constant defined in a term already available to the reader, or 'activities' needs an inline gloss at first use. *(confidence 0.85)*

#### `sstud-011` — MEDIUM · cognitive-load
*Location:* `section_id`=nugget-bonds · `nugget_id`=nugget-bonds
*Anchor:* “Radical reactions are chains of such single-electron steps and are drawn with single-barbed fishhook arrows.”

**Observation.** nugget-bonds is a core 7-minute section introducing eleven new terms across three paragraphs with no checkpoint. Two of those terms are arrow notation introduced one full section before nugget-arrows teaches what an arrow tail and head mean, with no cross-reference.

**Learner impact.** By paragraph three the student is still holding homolytic vs heterolytic and is asked to also hold nucleophile/electrophile. When arrows are mentioned before being defined, they assume they missed a section and scroll backwards.

**Evidence.** nugget-bonds text.expanded (3 paragraphs) and learning_objectives (3); compiled reader section nugget-bonds has one text block, three static molecules, no checkpoint.

**Need.** The two separable ideas need breaking apart with a consolidation point between, and the forward reference to arrow notation needs signposting. *(confidence 0.8)*

#### `sstud-012` — MEDIUM · conceptual-support
*Location:* `section_id`=nugget-bonds · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “Which fragment keeps the electrons is decided by electronegativity: the more electronegative atom retains the pair.”

**Observation.** The rule deciding the entire outcome of heterolytic cleavage rests on electronegativity, declared a prerequisite but never stated, trended, or exemplified anywhere in the chapter. prerequisites never reaches the compiled reader.

**Learner impact.** The student can recite the rule and still cannot apply it, because they do not reliably know whether carbon or bromine is more electronegative. They pass ch6-sort-cleavage by pattern-matching on wording without exercising the rule.

**Evidence.** concepts[1].prerequisites = ['electronegativity']; no electronegativity trend or value in any nugget text; no prerequisite block in the compiled reader.

**Need.** The reader needs the electronegativity comparison made concrete at the point of use, or an explicit pointer to where it can be refreshed. *(confidence 0.86)*

#### `sstud-013` — MEDIUM · cognitive-load
*Location:* `asset_id`=rc-one-step · `section_id`=nugget-intermediates
*Anchor:* “The height of the maximum above the reactants is the activation energy and fixes the rate”

**Observation.** The two reaction-coordinate figures carry only minima labels. Neither labels the transition state, the activation energy, or the overall free-energy change - yet the prose asks the reader to locate exactly those three unlabeled quantities. rc-one-step is also placed identically in two consecutive sections with identical title and caption.

**Learner impact.** Mapping a sentence onto an unannotated curve is exactly the multi-representation integration this student fails at, so the figure adds load rather than removing it. The duplicated diagram makes them think they scrolled backwards.

**Evidence.** assets[] rc-one-step and rc-two-step spec.minima_labels; compiled reader blocks blk-bfmih8sd, blk-z9clr47a (identical), blk-6qsichzg.

**Need.** The energy profiles need the quantities the prose names to be findable on the figure itself, and the two consecutive identical figures need differentiating. *(confidence 0.87)*

#### `sstud-014` — MEDIUM · assessment-readiness
*Location:* `question_slug`=ch6-draw-substitution-product
*Anchor:* “The product is methanol, CO in SMILES.”

**Observation.** Several hint ladders terminate in the answer rather than a reasoning move. Level 3 hints hand over the graded SMILES string directly on both structure_scaffold items.

**Learner impact.** The ladder trains the student to click three times instead of thinking. Because typed_structure_entry is allowed, they can paste 'CO' from hint 3 and be marked correct on an advanced item without forming a single idea about nucleophilic displacement.

**Evidence.** feedback_bundle.hints for ch6-draw-substitution-product, ch6-draw-substitution-product-v2, ch6-classify-reaction-type.

**Need.** The terminal hint needs to leave one reasoning step for the student rather than handing over the graded string. *(confidence 0.84)*

#### `sstud-015` — MEDIUM · notation-consistency
*Location:* `section_id`=nugget-thermo · `concept_slug`=thermodynamics-of-reactions
*Anchor:* “the standard free-energy change”

**Observation.** The chapter discusses the equilibrium constant, standard free-energy change, enthalpy, entropy, and activation energy entirely in words. No symbol appears anywhere in the reader and no relationship is written as an equation, yet the assigned OpenStax chapter presents all of these as symbols in equations.

**Learner impact.** The student opens the assigned reading and hits an equation having never been shown that the symbol is the thing the chapter called 'the standard free-energy change'. They cannot connect the two documents and assume they are behind.

**Evidence.** No occurrence of these symbols in the compiled reader; mcmurry_link block blk-31fb7sjk points at OpenStax chapter 6.

**Need.** The reader needs at least one binding of each named quantity to the symbol the student will meet in the textbook and lecture. *(confidence 0.8)*

#### `sstud-016` — MEDIUM · conceptual-support
*Location:* `section_id`=nugget-intermediates
*Anchor:* “Locating that highest point, and identifying the intermediates that flank it, is what allows a chemist to predict which step controls the reaction and where its energy is spent.”

**Observation.** The chapter ends on the last sentence of the last prose block. No summary, no key-ideas list, no consolidation. The nuggets declare 18 learning_objectives and none reach the reader, so no section announces what the reader should be able to do afterwards.

**Learner impact.** On finishing there is no way to check what to take away and no list to study from, so revision defaults to rereading the whole thing - the least effective strategy.

**Evidence.** nuggets[].learning_objectives (18 across 6 nuggets); compiled reader has 6 sections each ending in an external_link block, no summary or objectives block.

**Need.** A reader needs per-section objectives up front and an end-of-chapter consolidation; the authored objectives already exist and reach nobody. *(confidence 0.89)*

#### `sstud-017` — MEDIUM · worked-example-gap
*Location:* `asset_id`=video-energy-diagram · `section_id`=nugget-kinetics
*Anchor:* “Walking a two-step energy diagram”

**Observation.** The package's only video brief is a four-beat walkthrough of a two-step profile with status needs_review. It compiles into the reader as a block with empty url and is_hidden true. The chapter therefore contains zero guided walkthroughs.

**Learner impact.** The one asset designed to walk the student through the chapter's central tool does not exist. Nothing else in the chapter models the act of reading a profile - it only asserts what the parts mean.

**Evidence.** video_briefs[0] status needs_review; compiled reader block blk-7577paa7 with empty content.url and is_hidden true.

**Need.** The chapter needs some step-by-step traversal of a two-step energy profile that models the reading process. *(confidence 0.86)*

#### `sstud-018` — MEDIUM · cognitive-load
*Location:* `section_id`=nugget-classes · `asset_id`=mol-but-2-ene
*Anchor:* “The addition of hydrogen bromide to but-2-ene to give 2-bromobutane illustrates the pattern.”

**Observation.** The addition example is two independent molecule blocks stacked with no arrow, no plus sign, and no depiction of HBr at all. Their captions are the only link. The same holds in the curved-arrow section with three separate unlinked pictures.

**Learner impact.** The student must hold both structures in memory, mentally supply the reagent never drawn, and diff them atom by atom - precisely the operation they are worst at, on the chapter's first example.

**Evidence.** Compiled reader blocks blk-n6cjnrwt, blk-5kh1km8m; section nugget-arrows blocks blk-ga6ay38x, blk-44rek1nv, blk-o6pirqko. No reaction-type block exists anywhere in the chapter.

**Need.** The two flagship transformations need to be shown as transformations - reactants, reagent, and product in one visual relationship. *(confidence 0.83)*

#### `sstud-020` — MEDIUM · conceptual-support
*Location:* `section_id`=nugget-classes · `asset_id`=blk-31fb7sjk
*Anchor:* “Read in McMurry (OpenStax) — Chapter 6”

**Observation.** Exactly one mcmurry_link block exists, in the first section, pointing at the chapter's front matter page rather than at any section that teaches the material. The five later sections carry no textbook link at all.

**Learner impact.** When the kinetics section loses the student there is no route to the textbook from within that section; they must scroll to the top, land on a front-matter page, then navigate the textbook's own table of contents.

**Evidence.** Only blk-31fb7sjk is block_type mcmurry_link; its url is the 6-why-this-chapter page; five sections have no textbook link.

**Need.** Each section needs a route to the corresponding passage of the assigned textbook, landing on the covering section rather than front matter. *(confidence 0.85)*

#### `sstud-019` — LOW · assessment-readiness
*Location:* `question_slug`=ch6-rank-bde
*Anchor:* “Rank these carbon-halogen bonds from strongest to weakest bond dissociation energy.”

**Observation.** Both rank_order items set grading_rules.partial_credit false, while every other multi-part item in the bank sets it true. A student who orders three of four cards correctly scores zero on these two only.

**Learner impact.** All-or-nothing scoring is where a shaky student's effort stops paying back. 'Incorrect' with no indication they were one swap away reads as 'you understand none of this'.

**Evidence.** ch6-rank-bde and ch6-rank-bde-v2 grading_rules.partial_credit false in compiled/question-set.json; all other multi-part types use true.

**Need.** Ordering items need to distinguish 'nearly right' from 'no idea' the way the chapter's other multi-part items already do. *(confidence 0.78)*

**Strengths noted by this persona**

- The prose explicitly flags what matters most instead of weighting everything equally.
- The thermodynamics-versus-kinetics distinction is taught with a concrete beginner-holdable anchor: room-temperature hydrocarbon combustion.
- Addition and elimination are deliberately taught as a paired opposite, halving memory load for two of the four classes.
- Every question in the bank ships a hint ladder - no item leaves a stuck student with nothing to click.
- Both structure_scaffold items set typed_structure_entry allowed, so a student who cannot operate a drawing canvas is not locked out.
- Wrong-answer explanations name the specific wrong idea rather than returning a generic 'not quite'.
- The transition-state-versus-intermediate distinction is stated three separate ways - the right redundancy for the chapter's most confusable pair.

**Open questions**

- Which detail tier does the reader render by default? Assumed expanded, since that is what compiled content.markdown carries; findings sstud-010 and sstud-008 depend on it.
- Are question sets meant to appear inline in the reader chapter, or only in a separate practice surface? The compiled reader contains no question blocks at all.
- Used category objective-alignment for sstud-002; assessment-readiness would also fit. Flagging in case the orchestrator wants these normalized across personas.
- Do the structure_smiles values on the multi_select options actually render as structures, or do those items present as text-only?
- publishing.available and the reader's available are both false and science_review.status is not_reviewed - reviewed as pre-publication content.

### Accessibility Persona (score 5.4)

The platform is genuinely accessible: all nine question types render keyboard-complete, both structure_scaffold items allow typed structure entry, and the reader surfaces every alt text as visible 'Described as:' text preserved when images are off. What fails is chapter authoring. Three accessible_descriptions hand a screen-reader user the answer a sighted student must derive, and none trip the compile guard because find_accessibility_leaks matches only answer ids, a verdict vocabulary, and answer-key numbers. No asset carries a long_description, so both energy diagrams reduce to one sentence each, and the two-step alt never states that the intermediate sits above the reactants.

#### `access-001` — BLOCKER · alt-text-quality
*Location:* `question_slug`=ch6-draw-substitution-product · `concept_slug`=curved-arrow-notation
*Anchor:* “Draw the product of hydroxide displacing bromide from bromomethane in the structure editor: methanol.”

**Observation.** The accessible_description ends by naming the product, 'methanol'. The answer key is smiles CO and the prompt never names it, so the description states the solution rather than the task.

**Learner impact.** A screen-reader user is told what to draw while a sighted student must work out that hydroxide's oxygen replaces bromide. It is also the content the author gated behind hint level 3, given away free.

**Evidence.** topic.package.json ch6-draw-substitution-product: prompt_text, answer_key [redacted], accessible_description as quoted, hints[2]. accessibility_guard.find_accessibility_leaks checks only id-like tokens, VERDICT_VOCABULARY and answer-key numbers, so 'methanol' passes.

**Need.** The non-visual description must convey the stimulus and task without naming or identifying the product. *(confidence 0.97)*

#### `access-002` — BLOCKER · alt-text-quality
*Location:* `question_slug`=ch6-draw-substitution-product-v2 · `concept_slug`=curved-arrow-notation
*Anchor:* “Draw the product of methoxide displacing bromide from bromomethane: dimethyl ether.”

**Observation.** The same leak in the staged variant: the description names 'dimethyl ether', exactly the answer key smiles COC, which the prompt does not name.

**Learner impact.** Both of the chapter's only two structure-drawing items are pre-answered for screen-reader users, and these are its only advanced-difficulty items.

**Evidence.** topic.package.json ch6-draw-substitution-product-v2: answer_key [redacted], accessible_description as quoted, hints[2].

**Need.** This item needs a description stating reagents and the drawing task only, withholding the product identity exactly as the visual prompt does. *(confidence 0.97)*

#### `access-003` — BLOCKER · alt-text-quality
*Location:* `question_slug`=ch6-sort-cleavage · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “Sort four bond-breaking descriptions into homolytic (even, radicals) or heterolytic (uneven, ions).”

**Observation.** The description glosses the group labels as 'homolytic (even, radicals)' and 'heterolytic (uneven, ions)'. Those glosses appear nowhere in the stimulus, and the four items are phrased in exactly that vocabulary, so the gloss resolves all four assignments mechanically.

**Learner impact.** A screen-reader user can complete the categorization by keyword-matching with no chemistry reasoning, while a sighted student must recall what the terms mean. The same mapping is what the author gated as hints 1 and 2.

**Evidence.** topic.package.json ch6-sort-cleavage: groups carry only 'Homolytic'/'Heterolytic'; items i3/i4 restate the definitions; accessible_description as quoted; hints levels 1 and 2.

**Need.** The description needs to enumerate the four descriptions and the two category names as the sighted learner sees them, with no definition of what each category means. *(confidence 0.93)*

#### `access-005` — HIGH · media-equivalence
*Location:* `asset_id`=rc-two-step · `section_id`=nugget-intermediates · `concept_slug`=energy-diagrams-and-intermediates
*Anchor:* “A two-step free-energy profile: a high first barrier rises to an intermediate sitting in a shallow valley”

**Observation.** Neither reaction-coordinate asset carries a long_description. For rc-two-step the alt omits the most load-bearing spatial fact: the first step is authored endergonic so the intermediate sits above the reactants, but the alt says only 'in a shallow valley'. The one-step alt never names the activation energy or identifies it as a height.

**Learner impact.** A blind or low-vision learner, and anyone who turns images off, is given the conclusions but never the landmark data needed to practise the diagram-reading skill the objectives require, and in the two-step case is actively misled about where the intermediate sits.

**Evidence.** topic.package.json rc-two-step and rc-one-step have alt_text only, no long_description; TopicPackageChapterRenderer textEquivalentBlock falls back to long_description || alt_text.

**Need.** Both profiles need a full non-visual readout of the trace: ordered landmarks with relative heights, what each axis measures, and that the profile is schematic. *(confidence 0.9)*

#### `access-007` — HIGH · assessment-readiness
*Location:* `question_slug`=ch6-rank-bde · `concept_slug`=thermodynamics-of-reactions
*Anchor:* “Rank these carbon-halogen bonds from strongest to weakest bond dissociation energy.”

**Observation.** Both rank_order items author their cards in exactly the correct order, and MechanismCardSortRenderer does not shuffle: its order memo falls back to cards.map(c=>c.id) and it seeds the answer with that order on mount, so the item submits correct untouched.

**Learner impact.** A keyboard-only or screen-reader user reaching these through a Move up/Move down loop has no cue the pre-seeded arrangement is already the key. Neither item carries partial credit, so a student who reasons and one who pressed Submit are indistinguishable.

**Evidence.** ch6-rank-bde cards [c_cf,c_ccl,c_cbr,c_ci] == correct_order; ch6-rank-bde-v2 cards [c_me,c_1,c_2,c_3] == correct_order; MechanismCardSortRenderer order memo and mount effect.

**Need.** Both ordering items need a presented arrangement that is not already the answer, on every input modality. *(confidence 0.88)*

#### `access-004` — MEDIUM · alt-text-quality
*Location:* `question_slug`=ch6-select-nucleophiles · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “Select all that can act as electron-pair-donating nucleophiles.”

**Observation.** Both multi_select descriptions add a definitional gloss to the term being tested, each verbatim the level-1 hint.

**Learner impact.** A screen-reader user receives, without a hint-usage penalty, the definition that is the first step of the reasoning.

**Evidence.** ch6-select-nucleophiles description vs hints[0] 'A nucleophile donates a pair of electrons'; ch6-select-nucleophiles-v2 description vs hints[0].

**Need.** These descriptions need to carry only what a sighted learner sees, leaving the operational definition in the hint ladder. *(confidence 0.82)*

#### `access-006` — MEDIUM · media-equivalence
*Location:* `asset_id`=mol-2-bromobutane · `section_id`=nugget-classes · `concept_slug`=reaction-classes
*Anchor:* “2-Bromobutane: a four-carbon chain with a bromine on the second carbon and no double bond.”

**Observation.** The addition example is two separate molecule figures with no reaction block joining them. The product alt never mentions the hydrogen that added. The two are also rendered with different hydrogen-display conventions.

**Learner impact.** A learner working from the alt-text chain can never recover the other half of what 'adds across the double bond' means, and the mismatched hydrogen display makes cross-figure comparison unreliable when magnified.

**Evidence.** mol-but-2-ene has rdkit_options show_hydrogens true, mol-2-bromobutane has none; no reaction or scheme block exists anywhere in the compiled chapter.

**Need.** The addition example needs a non-visual equivalent linking substrate to product as one transformation, stating both atoms that added and where. *(confidence 0.83)*

#### `access-008` — MEDIUM · retrieval-practice
*Location:* `section_id`=nugget-classes · `concept_slug`=reaction-classes
*Anchor:* “Hydrogen bromide reacts with but-2-ene to give 2-bromobutane”

**Observation.** All six practice_check items and all twelve trouble_spots are absent from the compiled reader: zero callout blocks and none of their text, despite the reader renderer supporting the callout type.

**Learner impact.** The practice checks are plain text with a plain text answer, the most universally accessible activity format the chapter has, needing no figure, pointer or colour. Their absence removes the fallback every learner with a perceptual or motor constraint could have used.

**Evidence.** nuggets[].practice_check on all six; concepts[].trouble_spots on all six; compiled reader has no callout entries; ANNOTATABLE_TYPES includes 'callout'.

**Need.** The authored self-checks and trouble spots need to reach the reader in a text-native form. *(confidence 0.86)*

#### `access-011` — MEDIUM · media-equivalence
*Location:* `section_id`=nugget-classes
*Anchor:* “https://en.wikipedia.org/wiki/The_four_classes_of_organic_reactions”

**Observation.** All six external_link blocks point at Wikipedia URLs built by slugifying the concept title; none is a real article title and two retain colons. Their link text promises 'Background reading on <topic>'.

**Learner impact.** Every background-reading link dead-ends, and the cost falls hardest on learners who rely on supplementary reading to compensate for a modality gap. Descriptive link text that resolves to nothing is worse than no link, because a screen-reader user navigating by link list cannot tell before following it.

**Evidence.** Compiled reader external_link blocks; each content.url is the concept title with spaces underscored and punctuation retained. The one mcmurry_link is by contrast a real OpenStax URL.

**Need.** Every outbound reading link needs to resolve to a real verified resource on the topic it names, or be removed. *(confidence 0.92)*

#### `access-009` — LOW · interactive-fallback
*Location:* `asset_id`=video-energy-diagram · `section_id`=nugget-kinetics
*Anchor:* “Open on the reactant valley and animate the climb to the first transition state”

**Observation.** The one planned moving asset compiles with empty url and is_hidden true, so nothing plays today. The brief records no captions, transcript, or audio description, its storyboard is four visual stage directions, and its narration outline does not narrate the on-screen motion.

**Learner impact.** No learner is blocked now, but if produced as specified a blind learner would hear three general statements over an animation whose meaning is carried by which peak is highlighted and when.

**Evidence.** video_briefs[0] storyboard[3] has no corresponding narration line; compiled block blk-7577paa7 url empty, is_hidden true, description equals storyboard[0].

**Need.** Before production the brief needs narration describing the visual changes, a time-independent equivalent, and learner playback control. *(confidence 0.75)*

#### `access-010` — LOW · alt-text-quality
*Location:* `asset_id`=mol-hydroxide · `section_id`=nugget-bonds · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “A hydroxide ion, an oxygen bearing a negative charge and lone pairs, acting as an electron-pair donor.”

**Observation.** Several alt texts assert electronic features the RDKit render does not draw: lone pairs on hydroxide, partial positive charge on bromomethane's carbon.

**Learner impact.** A screen-reader user told the figure shows lone pairs will look for them in a shared or printed copy and not find them, and cannot tell which cues are drawn and which are inferred, in a chapter whose whole subject is where electrons are.

**Evidence.** mol-hydroxide, mol-bromomethane and mol-tert-butyl-cation alt texts; ReaderBlockRenderer prints them verbatim as 'Described as:'.

**Need.** Figure descriptions need to separate what the rendering shows from the electronic interpretation being taught. *(confidence 0.7)*

**Strengths noted by this persona**

- Every question type renders keyboard-complete with no drag-only path: rank_order via Move up/down IconButtons with aria-live position readout, and categorize_groups, matching_pairs and comparison_matrix via labeled Selects.
- Both structure_scaffold items set typed_structure_entry 'allowed', so the only construct-a-structure tasks never require a pointer.
- All ten assets carry non-empty alt text, surfaced both as img alt and as visible 'Described as:' text.
- Turning images off converts each figure into a callout carrying its description rather than deleting it.
- The prose is self-sufficient on the hardest visual topic: nugget-arrows narrates the mechanism arrow by arrow, so the absent curved-arrow figure costs a non-visual learner nothing.
- All three detail tiers are authored for every nugget and the default expanded tier is a genuine superset.
- Every multi_select option carrying a structure also carries a text name, so no option's identity depends on a rendered structure.

**Open questions**

- access-011 is filed under media-equivalence as a best fit; no listed category covers an outbound link whose text describes content the URL does not resolve to.
- The reader nests figure-card headings at h4 directly under h2, skipping h3, at all thirteen figure cards. That is platform-wide rather than chapter-authored so I did not file it.
- I could not determine whether the rendered reaction-coordinate SVG carries its minima labels as text; if baked into the SVG they are unavailable to a screen reader regardless of alt text, which would raise access-005's priority.
- publishing.available is false and demo_eligible is 0, so I judged the questions as authored artifacts rather than a live experience.
- ch6-select-nucleophiles-v2 gives structure_smiles to three of four options but not to 'Proton, H+'; not filed because the text label carries identity either way.

### Learner with Visual Preference (score 4.4)

Mechanically well-wired: all ten assets reach the reader, none are empty placeholders, no annotation_font_scale inflates glyphs, and the unproduced video is correctly hidden. The problem is what the figures are of. Twelve figure blocks and not one shows a transformation. The flagship two-step energy profile is broken as rendered: its 'high'/'low' barriers are not valid values, both coerce to medium, and the diagram draws two transition states at the same height with products at reactant energy, contradicting the alt text beneath it.

#### `vis-001` — BLOCKER · figure-accuracy
*Location:* `asset_id`=rc-two-step · `section_id`=nugget-intermediates · `concept_slug`=energy-diagrams-and-intermediates
*Anchor:* “a high first barrier rises to an intermediate sitting in a shallow valley”

**Observation.** The two-step diagram does not render the shape it claims. Its 'high' and 'low' barriers are not valid BarrierSize values so both coerce to medium and the two transition states draw at identical height, with products at exactly reactant energy.

**Learner impact.** A learner reading the picture sees two equal peaks and cannot identify the highest transition state, the exact operation the section's third objective requires, while the description beneath asserts otherwise.

**Evidence.** [internal source reference — not in this repo] BarrierSize is small|medium|large; [internal source reference — not in this repo] line 111 coerces unknown values; running the normalizer on this spec returns both peaks at 2.8 and minima Reactants 0.0, Intermediate 1.6, Products 0.0.

**Need.** The two-step profile must show one barrier taller than the other and a non-zero reactant-to-product change, and its caption must describe the figure that renders. *(confidence 0.97)*

#### `vis-002` — HIGH · visual-opportunity
*Location:* `section_id`=nugget-arrows · `concept_slug`=curved-arrow-notation
*Anchor:* “using them correctly is the single most transferable skill in the subject”

**Observation.** The curved-arrow section contains no curved arrow: three static unconnected molecule cards with no arrow, no plus sign and no reaction block. Bromide, the second product, is not shown at all.

**Learner impact.** Arrow-pushing is a notational skill that is entirely spatial, and here it exists only as sentences the learner must convert into a picture unaided; the claim that the arrows conserve every electron cannot be checked against anything.

**Evidence.** Reader blocks blk-ga6ay38x, blk-44rek1nv, blk-o6pirqko are all molecule type; no reaction or arrow-bearing figure exists in the chapter; the concept declares preferred_representations ['molecule'].

**Need.** Electron flow across a single transformation needs to be visible, with the departing bromide present so the bookkeeping is checkable. *(confidence 0.95)*

#### `vis-003` — HIGH · visual-opportunity
*Location:* `question_slug`=ch6-arrow-electron-count · `concept_slug`=curved-arrow-notation
*Anchor:* “How many electrons does a single full (double-barbed) curved arrow represent in a polar mechanism?”

**Observation.** Three questions grade a purely visual discrimination, how many barbs an arrowhead has, that the chapter never depicts. Neither arrowhead appears in any reader figure or any question.

**Learner impact.** A learner is asked to distinguish a double-barbed arrowhead from a fishhook when neither has been drawn for them, so the item is answerable only as vocabulary recall, not the notational recognition it tests.

**Evidence.** ch6-arrow-electron-count, its v2, and ch6-sort-cleavage-v2; no figure key on any of the 18 questions; no reader block renders either arrow type.

**Need.** The visual difference between a one-electron and a two-electron arrowhead must be shown somewhere before it is graded. *(confidence 0.94)*

#### `vis-004` — HIGH · figure-purpose
*Location:* `asset_id`=rc-one-step · `section_id`=nugget-kinetics · `concept_slug`=kinetics-and-transition-states
*Anchor:* “the energy needed to climb from the reactants to it is the activation energy”

**Observation.** Neither diagram labels a single energy quantity. The renderer supports show_activation_labels and show_delta_labels; both default false and neither asset sets them, and peaks carry only a bare double-dagger because no ts_label is authored.

**Learner impact.** The prose does the pointing the diagram should do, so a learner must measure two heights by eye on a curve carrying only 'Reactants' and 'Products'. The one thing an energy diagram is good for, making a quantity a visible distance, is switched off.

**Evidence.** [internal source reference — not in this repo] defines both flags defaulting false; [internal source reference — not in this repo] draws a dashed guide and label when show_activation_labels is set; neither asset includes either key.

**Need.** The activation energy and the overall free-energy change need to be identifiable on the picture itself. *(confidence 0.93)*

#### `vis-006` — HIGH · visual-opportunity
*Location:* `section_id`=nugget-classes · `concept_slug`=reaction-classes
*Anchor:* “Addition and elimination are therefore best learned together as opposites”

**Observation.** The four reaction classes are conveyed by prose plus three standalone molecule cards. No figure shows a reaction; there is no elimination product structure and rearrangement has no figure at all.

**Learner impact.** Classification here is defined by net structural change, so it is inherently a before/after comparison and no before/after is drawn; two of four classes are pictured with nothing, quietly signalling they matter less.

**Evidence.** Section nugget-classes contains three unlinked molecule blocks; the reader's IMAGE_TYPES set includes a 'reaction' block type, so the surface exists and is unused; four of eighteen questions grade this classification.

**Need.** The defining bond change of each class needs to be visible side by side, especially elimination and rearrangement. *(confidence 0.92)*

#### `vis-007` — HIGH · figure-accuracy
*Location:* `asset_id`=mol-hydroxide · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “an oxygen bearing a negative charge and lone pairs, acting as an electron-pair donor”

**Observation.** Two figures state purposes the rendered image cannot deliver: mol-hydroxide promises lone pairs, which RDKit does not draw and for which no option exists, and mol-bromomethane promises a partially positive carbon with no partial charge or polarity cue drawn.

**Learner impact.** The one visual cue that would make the nucleophile/electrophile distinction readable is described but not drawn, so a learner comparing caption to picture finds the caption describing something that is not there.

**Evidence.** mol-hydroxide learning_goal and alt_text with smiles [OH-]; mol-bromomethane alt_text with smiles CBr; supported rdkit_options include no lone-pair or partial-charge rendering.

**Need.** Either the promised electron-density information must be visible or the captions must stop asserting it. *(confidence 0.88)*

#### `vis-005` — MEDIUM · visual-redundancy
*Location:* `asset_id`=rc-one-step · `section_id`=nugget-thermo
*Anchor:* “Single-step exergonic reaction”

**Observation.** The identical one-step diagram is embedded twice in consecutive sections with byte-identical title, alt text, description and spec.

**Learner impact.** The two sections exist to separate thermodynamics from kinetics, and illustrating both with the same unannotated picture works against that separation; a repeated figure that changes nothing also trains learners to scroll past figures.

**Evidence.** Blocks blk-bfmih8sd and blk-z9clr47a both carry asset_id rc-one-step with identical content; the package lists it under both nuggets.

**Need.** Either the two instances must call out different features or the second should be dropped. *(confidence 0.9)*

#### `vis-008` — MEDIUM · visual-redundancy
*Location:* `asset_id`=mol-chlorine · `section_id`=nugget-bonds
*Anchor:* “Molecular chlorine, a bond that cleaves homolytically”

**Observation.** Four of ten assets are one- or two-heavy-atom structures conveying nothing beyond the name in the caption, and hydroxide is embedded twice.

**Learner impact.** A card, badge, heading, description and rendered image are spent showing a learner the two letters Cl-Cl, competing with the relationships that get no figure at all and setting an expectation that figures here are not worth stopping for.

**Evidence.** SMILES ClCl, [OH-], CBr, CO; mol-hydroxide rendered by both blk-6maxpx2g and blk-44rek1nv; twelve figure blocks total, none depicting a transformation.

**Need.** These figures should be reduced or absorbed into the figure showing the process they participate in. *(confidence 0.85)*

#### `vis-009` — MEDIUM · notation-consistency
*Location:* `asset_id`=mol-but-2-ene · `section_id`=nugget-classes · `concept_slug`=reaction-classes

**Observation.** Within one section the substrate and product of the same addition are drawn in different conventions: mol-but-2-ene sets show_hydrogens true while the product carries no rdkit_options and renders skeletal. mol-chlorine also sets show_hydrogens on a molecule with no hydrogens.

**Learner impact.** The two cards a learner is meant to compare differ in drawing style as well as bond change, so the difference being taught is buried in one that is not.

**Evidence.** mol-but-2-ene has rdkit_options {show_hydrogens: true}; mol-2-bromobutane and mol-tert-butyl-bromide have none; _resolve_show_hydrogens returns False when absent.

**Need.** Structures a learner compares need to be drawn the same way. *(confidence 0.87)*

#### `vis-010` — MEDIUM · figure-purpose
*Location:* `concept_slug`=energy-diagrams-and-intermediates · `asset_id`=rc-two-step
*Anchor:* “Assuming a two-step profile always has a rate-limiting first step”

**Observation.** The concept names that assumption as a trouble spot, and the chapter's only two-step profile is authored with a rate-limiting first step with no counter-example.

**Learner impact.** A learner generalises from the one picture given, so the sole sample produces the very misconception the concept identified.

**Evidence.** concept trouble_spots[1]; rc-two-step is the only multi-step RC asset and its alt text states the first step is rate-limiting.

**Need.** Locating the rate-limiting step needs at least one case where it is not the first step. *(confidence 0.83)*

#### `vis-011` — MEDIUM · visual-opportunity
*Location:* `asset_id`=rc-two-step · `section_id`=nugget-intermediates
*Anchor:* “An intermediate occupies a local energy minimum; it is a real species, such as a carbocation”

**Observation.** The two-step diagram pins no structure to its intermediate minimum even though minima_molecules supports exactly that; the tert-butyl cation sits as a separate card below the diagram.

**Learner impact.** The distinction the section turns on becomes obvious the moment a structure sits in the valley and nothing sits on the peaks; split across two cards the learner must carry the cation back up and decide which minimum it belongs to.

**Evidence.** [internal source reference — not in this repo] documents minima_molecules as a map of minimum index to SMILES pinned to that minimum; rc-two-step's spec has no minima_molecules key; the cation is reader block blk-mepzjmph.

**Need.** The link between the intermediate valley and the actual carbocation needs to be visible in one place. *(confidence 0.86)*

#### `vis-012` — MEDIUM · visual-opportunity
*Location:* `concept_slug`=kinetics-and-transition-states · `question_slug`=ch6-match-terms
*Anchor:* “it lowers the barrier equally in both directions”

**Observation.** Catalysis is a stated objective graded in two questions, but no figure shows a catalysed and uncatalysed profile on shared axes.

**Learner impact.** The named trouble spot is believing a catalyst changes the equilibrium position, which two curves sharing endpoints but differing in peak height corrects instantly; as prose only, the learner must hold both claims and infer the picture.

**Evidence.** concept trouble_spots[0] and nugget-kinetics objective 3; graded by ch6-match-terms and its variant; the only kinetics figure is a single uncatalysed curve.

**Need.** The invariance of endpoints under catalysis alongside the change in barrier height needs to be visible in one comparison. *(confidence 0.84)*

#### `vis-013` — MEDIUM · figure-purpose
*Location:* `question_slug`=ch6-select-nucleophiles · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “Select every species below that can act as a nucleophile.”

**Observation.** The two multi_select questions are the only items authored with per-option structures and those structures never reach a student: SelectedResponseOption carries only id, text and imageUrl, and the renderer draws option text only.

**Learner impact.** The author's intent to let the learner judge electron-richness from the drawn species is silently discarded and the item degrades into a vocabulary check on four names.

**Evidence.** ch6-select-nucleophiles carries four structure_smiles and its variant three; [internal source reference — not in this repo] SelectedResponseOption has no structure field; SelectedResponseRenderer contains no molecule rendering.

**Need.** Either the structures must be visible to the student answering, or the items must be reworked so they do not depend on structures never seen. *(confidence 0.89)*

#### `vis-015` — MEDIUM · visual-redundancy
*Location:* `asset_id`=video-energy-diagram · `section_id`=nugget-kinetics
*Anchor:* “Walking a two-step energy diagram”

**Observation.** The only planned animation is unproduced, attached to the wrong section (its brief targets rc-two-step but the block sits in nugget-kinetics whose figure is rc-one-step), and its four storyboard beats are exactly the four annotations the static diagram is missing.

**Learner impact.** Nothing is broken on screen since the block is hidden, but the chapter carries a production commitment for motion that would not add information over a properly labelled still, while that labelling is switched off.

**Evidence.** video_briefs[0] visual_asset_ids [rc-two-step, mol-tert-butyl-cation], status needs_review; nugget-kinetics asset_ids [rc-one-step]; block blk-7577paa7 url empty, is_hidden true.

**Need.** The need is annotation on the static two-step profile, not motion, and it must sit with the two-step diagram. *(confidence 0.86)*

#### `vis-016` — MEDIUM · visual-opportunity
*Location:* `section_id`=nugget-bonds · `concept_slug`=bond-changes-radical-vs-polar
*Anchor:* “In homolytic cleavage the two bonding electrons separate evenly, one going to each fragment”

**Observation.** Neither kind of bond cleavage is pictured: an intact Cl2, a finished cation and a finished anion, with the split itself and the even-versus-uneven partition appearing in no figure.

**Learner impact.** The concept is a contrast between two ways one line comes apart, and both before- and after-states are shown while the coming-apart is not, so the learner must infer both processes.

**Evidence.** Section nugget-bonds blocks blk-5n4r9yyk, blk-7nq83b47, blk-6maxpx2g are all static molecules; trouble_spots[0] names the confusion; graded by ch6-sort-cleavage.

**Need.** The two ways a bonding pair can be divided need to be a visible contrast. *(confidence 0.85)*

#### `vis-017` — MEDIUM · alt-text-quality
*Location:* `asset_id`=rc-one-step · `concept_slug`=thermodynamics-of-reactions
*Anchor:* “A one-step free-energy profile: a single barrier (the transition state) separates reactants from lower-energy products”

**Observation.** No asset carries a long_description; every figure has a single-sentence alt text, and for the energy diagrams that sentence names the shape but never says how to read a quantity off it.

**Learner impact.** A learner who turns images off receives one sentence in place of the figure, omitting the two things the section asks them to extract; the same sentence is the permanent caption every learner reads.

**Evidence.** All ten assets have alt_text and none has long_description; the images-off path falls back to long || alt; ReaderBlockRenderer renders 'Described as:' under every diagram.

**Need.** Figure descriptions need to convey what a learner is supposed to read off the figure, not only what it is a picture of. *(confidence 0.82)*

#### `vis-014` — LOW · notation-consistency
*Location:* `question_slug`=ch6-select-nucleophiles-v2
*Anchor:* “Proton, H+”

**Observation.** Three of four options carry a structure and one does not, and the un-illustrated option is one of the two correct answers.

**Learner impact.** Currently moot because no option structure renders, but once they do, an option that looks different from its neighbours is a formatting cue independent of chemistry that points at a key.

**Evidence.** Options a [CH3+], b (no structure_smiles), c [Br-], d O; correct_option_ids [redacted].

**Need.** Options within one item need uniform treatment. *(confidence 0.78)*

**Strengths noted by this persona**

- Every authored asset reaches the compiled reader as a real block, with no figure stranded and no empty placeholder on screen.
- The unproduced video compiles with is_hidden true and the renderer returns null for hidden blocks, so no learner meets a dead card pointing at an empty url.
- No asset sets annotation_font_scale above 1.0, so no label glyph is enlarged onto the structure it annotates.
- rc-one-step's spec is fully valid and renders as its caption describes.
- Every asset carries a learning_goal naming a specific instructional point, and every figure has non-empty alt text.
- The images-off preference converts figure blocks into described callouts rather than deleting them.

**Open questions**

- All six Wikipedia further-reading blocks are concept titles mechanically converted into URLs and all six will 404; routing rather than filing since it sits outside my rubric's categories.
- Every concept authors trouble_spots and every nugget a practice_check, but the compiled reader contains no callout block, so none of that scaffolding reaches a student.
- ReactionCoordinateCard POSTs the spec at read time with a bearer token and the endpoint has an access-class gate; does an anonymous reader get the diagram or the alt-text fallback?
- Both reaction-classes and curved-arrow-notation declare preferred_representations ['molecule'], which correlates exactly with the two sections that have no transformation figure.
- No new category was coined; all seventeen findings use schema ids.


---

## Post-correction record

**Status:** applied-and-verified-without-second-persona-run 
**Post-correction estimate:** major revision — *Not a new persona verdict. All six blockers are cleared and the stranded scaffolding now reaches the reader, but the chapter still has no figure of any transformation, two questions assess untaught content, and neither energy profile has a long description.* 
**Baseline verdict above is preserved and unchanged (BLOCKED).** Only a separate four-persona regression run can issue a new verdict.

### Changes applied

1. Authored wikipedia_title on all six concepts (Organic_reaction, Homolysis_(chemistry), Arrow_pushing, Chemical_equilibrium, Activation_energy, Reaction_coordinate). All six verified HTTP 200. This restores the fix from commit [commit ref — not in this repo] durably: it had been applied to the compiled artifact only and reverted by two subsequent recompiles.
 - *Resolves:* `inst-008`, `sstud-006`, `access-011`
 - *Partially addresses:* —

2. rc-two-step barrier values high->large and low->small in the authored spec, so the renderer no longer coerces both to medium. The compiled figure now shows a large first barrier to an endergonic intermediate and a small second barrier. Also artifact-only since [commit ref — not in this repo] and reverted twice.
 - *Resolves:* `inst-001`, `vis-001`
 - *Partially addresses:* `sstud-008`, `access-005`

3. ch6-classify-reaction-type-v2 prompt and accessible description rewritten so a base-mediated elimination no longer claims HBr as a product; it now says the elements of HBr are lost from adjacent carbons.
 - *Resolves:* `inst-002`
 - *Partially addresses:* —

4. Rewrote five accessible descriptions to remove answer leaks: ch6-draw-substitution-product and its v2 no longer name the product, ch6-sort-cleavage no longer supplies the homolytic/heterolytic grading key as a gloss, and both multi_select items no longer gloss the term under test.
 - *Resolves:* `access-001`, `access-002`, `access-003`, `access-004`
 - *Partially addresses:* —

5. Reordered the authored cards of ch6-rank-bde and ch6-rank-bde-v2 so the presented order is no longer the answer. The renderer does not shuffle and seeds the presented order on mount, so both items previously submitted correct untouched.
 - *Resolves:* `access-007`
 - *Partially addresses:* `sstud-019`

6. Restored the precise catalyst wording in nugget-kinetics ('not consumed overall - it may be used up in one step and regenerated in a later one'). This was a tier-2 correction reverted by the same recompile, and it sits in the expanded tier, which is the tier the reader renders by default.
 - *Resolves:* `sstud-009`
 - *Partially addresses:* —

7. Set nugget order to 1..6. All six nuggets were authored order=1; the reader sorts nuggets by that key, so section sequence was resting on Python's stable sort preserving array order rather than on the authored value. Verified section order unchanged after recompile.
 - *Resolves:* —
 - *Partially addresses:* —

8. Recompiled with --write-runtime. The reader now carries 12 callout blocks, so all six practice checks and all twelve trouble spots reach a student for the first time.
 - *Resolves:* `inst-007`, `sstud-003`, `sstud-004`, `access-008`
 - *Partially addresses:* `sstud-016`

### Still open (not corrected)

- rec-007: the two bond-dissociation-energy questions still assess content the chapter never teaches, and the thermodynamics concept's own three objectives remain unassessed. Left uncorrected because the fix is a scope decision (add the prose, or move the items) that belongs to the author.
- rec-008: the chapter still contains no figure of any transformation - no reaction arrow, no curved arrow, no bond cleaving - in a chapter whose prose calls curved arrows the most transferable skill in the subject. All four personas raised this; it is new content authoring, not a correction.
- rec-009: neither energy profile has a long_description, so both still reduce to one sentence when images are off.
- rec-010: the prerequisite slugs functional-group-recognition and electronegativity still resolve to no concept in the corpus.
- rec-011: rc-one-step is still emitted twice in consecutive sections with identical content.

### Verification

- Topic-package compiler (proprietary toolchain, not in this repo) — clean
- Automated test suite — 144 passed, 4 failed (unrelated fixture drift noted in review)
- curl -L on all 14 compiled external links across both chapters - 14/14 HTTP 200
- python .[internal source reference — not in this repo] on all 8 persona envelopes - valid
- python .[internal source reference — not in this repo] --synthesized on both reports - valid

### Follow-up pass (same day)

Follow-up pass, same day, after the correction record above. Platform and figure work requested by the maintainer: transformation-figure support, the stereochemistry_conversion mapping, viewer colour preferences on reactions, and admin preview of unpublished chapters.

1. Added four `reaction` transformation figures - addition (but-2-ene + HBr -> 2-bromobutane), elimination (2-bromo-2-methylpropane -> 2-methylpropene + HBr), substitution (bromomethane + hydroxide -> methanol + bromide, with the leaving group drawn so the electron count is checkable), and rearrangement (secondary butyl cation -> tert-butyl cation by hydride shift). All four verified balanced atom-by-atom and charge-by-charge in RDKit. The substitution figure is reused in nugget-arrows, so the curved-arrow section finally shows the transformation its three paragraphs describe. Rearrangement had no depiction of any kind before this.
 - *Resolves:* `inst-005`, `sstud-005`, `sstud-007`, `vis-002`, `vis-006`, `vis-016`, `sstud-018`, `inst-011`
 - *Partially addresses:* `vis-003`

**Verification**

- Automated test suite — 167 passed
- Automated test suite — 104 passed
- npx tsc --noEmit - no errors in any changed file; project total unchanged at 729
- All four ch6 transformations verified balanced (atom counts and formal charge) and rendered for visual inspection
