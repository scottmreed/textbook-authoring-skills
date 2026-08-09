# Chapter review — Structure and Bonding (`structure-and-bonding`)

_Reviewed 2026-07-24 · chapter version 1 · personas: Organic Chemistry Instructor, Struggling Student, Accessibility, Learner with Visual Preference · baseline before corrections_

**Publication readiness: blocked**

The chapter is coherently sequenced and its introductory bonding explanations are mostly sound, but it is not ready to publish unchanged. One assessment explanation teaches the false rule that sp hybridization occurs only in triple bonds, and one accessibility description reproduces a grading-accepted answer. The four reviewers also converge on thin assessment coverage, missing reader-visible practice checks, and inadequate support for the spatial reasoning required by hybridization, polarity, and skeletal notation. Orchestrator verification additionally found that all six compiled Wikipedia links are fabricated from internal concept titles.

## Top blockers

- **[BLOCKER · chemical accuracy] Triple-bond-only sp rule** — feedback says sp hybridization occurs only at a carbon of a triple bond, excluding valid sp carbons such as the central carbon of an allene (`instructor-001`, `ch1-sp-hybridized-carbon`).
- **[BLOCKER · answer leak] Accepted answer repeated in accessibility text** — the ethanol description supplies `-OH`, which the answer key accepts verbatim (`access-001`, `ch1-ethanol-functional-group`).

## Top recommended changes

- **Replace the false triple-bond-only rule for sp carbon** — Assessment feedback must define sp hybridization by two electron domains and linear geometry without excluding allenic or other valid sp carbons. → **prose-edit** (assessment, blocker).
- **Make question descriptions answer-neutral and structurally equivalent** — The ethanol prompt must not reproduce an accepted answer, and structure-based options must expose bond order without revealing the inference. → **text-equivalent** (assessment, blocker).
- **Assess every core objective** — Students and instructors need direct evidence for sp3 geometry, shape/polarity reasoning, and actual line-angle decoding. → **added-practice** (assessment, high).
- **Expose the authored practice checks in the reader** — The six source practice checks need a visible formative path rather than being dropped from the compiled reader. → **added-practice** (practice, high).
- **Make hybridization and orbital overlap inspectable** — Learners need an available representation of sp3/sp2/sp geometry, retained p orbitals, and sigma-versus-pi overlap. → **static-image-sequence** (figure, high).

## Persona status cards

| Persona | Score | Blockers | Headline |
|---|---:|---:|---|
| Organic Chemistry Instructor | 6.1/10 | 1 | Not ready for instructor assignment. The chapter has a coherent introductory sequence and mostly accurate core explanations, but the assessment feedback contains a false rule about sp-hybridized carbon that would create a durable misconception. Assessment coverage is also too narrow for the stated objectives, the reader omits the package's practice checks, and the hybridization objectives lack a visible representation or worked application that lets students reason beyond memorized alkane/alkene/alkyne patterns. |
| Struggling Student | 5.4/10 | 0 | The chapter has a sensible broad progression, but a learner with weak prerequisites is asked to absorb foundational vocabulary, orbital models, three-dimensional geometry, polarity, and drawing conventions with almost no visible step-by-step practice. The source package contains useful practice checks, yet they are absent from the compiled reader, and the four-question bank leaves major objectives unrehearsed. I could often repeat the stated rule, but I would not feel able to apply it to a new molecule without guessing. |
| Accessibility Persona | 6.3/10 | 1 | The chapter provides concise, chemically specific alt text for every molecule and repeats most spatial chemistry in prose, giving learners a substantially usable text path. However, one short-answer accessibility description reproduces a grading-accepted answer, two structure-based questions do not communicate the bond-order information shown in their molecular options, several figure descriptions omit their stated teaching point, and the planned hybridization video lacks a documented equivalent for its visual transformations. Runtime keyboard, heading, notation-pronunciation, and media-control behavior cannot be established from these files. |
| Learner with Visual Preference | 6.2/10 | 0 | The chapter has a clear conceptual progression and attaches small, purposeful molecule examples to every section, but the compiled reader relies heavily on prose and basic molecular structures for ideas that are intrinsically spatial. Lewis electron pairs, orbital overlap, the sp3/sp2/sp comparison, dipole-vector cancellation, and the translation into line-angle notation are not made visibly inspectable in the available blocks. The hidden hybridization video indicates awareness of the largest spatial burden, but its current reader entries are unavailable and locally misdescribed. No visual issue is a publication blocker, though the chapter would benefit materially from tighter alignment between each visual, its stated learning goal, and the relationship the learner is meant to see. |

## Correction status

The two baseline blockers and the local access/accuracy defects were corrected
and verified. The four personas were not rerun, so the post-correction state is
an evidence-backed estimate, not a new publication-readiness verdict. Remaining
high-priority assessment and worked-example gaps keep the estimate at **major
revision**.

---

## Full evidence

The four persona reviews were independent. Three ran concurrently; the fourth was queued only because this environment provides three reviewer slots in addition to the orchestrator. Each reviewer saw only its own rubric.

### Organic Chemistry Instructor

**Score:** 6.1/10 · **publication blockers:** instructor-001

Not ready for instructor assignment. The chapter has a coherent introductory sequence and mostly accurate core explanations, but the assessment feedback contains a false rule about sp-hybridized carbon that would create a durable misconception. Assessment coverage is also too narrow for the stated objectives, the reader omits the package's practice checks, and the hybridization objectives lack a visible representation or worked application that lets students reason beyond memorized alkane/alkene/alkyne patterns.

**Strengths**

- The six concepts are sequenced coherently from covalent bonding through sp3, sp2, and sp hybridization before shape, polarity, and structure notation.
- The core decompositions of a carbon-carbon double bond as one sigma plus one pi bond and a triple bond as one sigma plus two pi bonds are correct and consistently reinforced.
- The supplied SMILES, answer keys, and named molecular examples are chemically valid for the intended introductory examples.
- Most question hints and incorrect-answer explanations teach the relevant valence or bonding rationale rather than merely revealing an answer.

**Findings**

- **instructor-001 · blocker · chemical-accuracy** — The generic incorrect-answer feedback states a false exclusivity rule. A carbon can be sp-hybridized without participating in a triple bond, including the central carbon of an allene or another appropriate cumulated system.
 - Location: question_slug=ch1-sp-hybridized-carbon; concept_slug=sp-hybridization; anchor_text=sp hybridization occurs only at a carbon of a triple bond
 - Learner impact: Students may memorize triple bond as a necessary condition for sp hybridization and later misassign valid linear, two-domain carbons.
 - Evidence: Both the topic package and compiled question set give the feedback: "sp hybridization occurs only at a carbon of a triple bond." The answer Acetylene is correct for the listed choices, but the explanatory rule is not generally correct.
 - Needed outcome: The feedback needs to define sp hybridization through two electron domains and linear orbital geometry without excluding valid sp-hybridized carbons that lack a triple bond.
 - Confidence: 0.99
- **instructor-002 · high · objective-alignment** — The question bank has no item for molecular shape or polarity and no item for the sp3 objective. Its four questions cover only oxygen valence, recognition of an sp carbon, recognition of molecules containing pi bonds, and naming ethanol's functional group.
 - Location: section_id=molecular-shape-polarity; concept_slug=molecular-shape-polarity; nugget_id=nugget-shape-polarity; anchor_text=Predict molecular shape from electron-pair arrangement and relate electronegativity to bond and molecular polarity.
 - Learner impact: An instructor cannot determine whether students can predict geometry, distinguish bond polarity from molecular polarity, reason about dipole cancellation, or explain tetrahedral carbon—the central outcomes of two sections.
 - Evidence: The package declares six learning objectives, including the quoted shape/polarity objective and an sp3 geometry objective. The compiled question set contains concept slugs only for atoms-electrons-covalent-bonds, sp-hybridization, drawing-organic-structures, and sp2-hybridization-pi-bonds.
 - Needed outcome: The assessment needs direct evidence that students can apply electron-domain reasoning to shape and molecular polarity and can explain or identify tetrahedral sp3 geometry.
 - Confidence: 0.99
- **instructor-003 · high · assessment-readiness** — The only question mapped to the drawing objective asks students to name the group in the explicit condensed formula CH3CH2OH. It does not require reading a line-angle structure, recovering implied carbon hydrogens, translating between representations, or identifying an unfamiliar functional group from a structure.
 - Location: section_id=drawing-organic-structures; concept_slug=drawing-organic-structures; nugget_id=nugget-drawing; question_slug=ch1-ethanol-functional-group; anchor_text=Read condensed and line-angle structures and identify common functional groups.
 - Learner impact: Students can pass the available item by recognizing OH while remaining unable to read the skeletal notation required throughout organic chemistry.
 - Evidence: The learning objective requires reading both condensed and line-angle structures, while ch1-ethanol-functional-group supplies the formula and accepts hydroxyl, alcohol, -OH, or OH. No compiled question requires interpretation of an unlabeled skeletal structure.
 - Needed outcome: Assessment needs to demonstrate actual interpretation of condensed and line-angle notation, including implied atoms or hydrogens and functional-group recognition from structure rather than from a named molecule.
 - Confidence: 0.98
- **instructor-004 · high · visual-opportunity** — The package identifies orbital overlays as a preferred representation for sp3 and sp2 hybridization, but the compiled reader exposes only ordinary molecule blocks. The sole hybridization video has an empty URL and is hidden, so the spatial relationship among hybrid orbitals, the unhybridized p orbital, and sigma/pi overlap is conveyed only in prose.
 - Location: section_id=sp2-hybridization-pi-bonds; concept_slug=sp2-hybridization-pi-bonds; nugget_id=nugget-sp2; asset_id=video-hybridization; anchor_text=One 2p orbital remains unhybridized and stands perpendicular to that plane.
 - Learner impact: Students are asked to explain three-dimensional orbital geometry and side-on overlap without being able to inspect the spatial model on which the explanation depends.
 - Evidence: The sp3 and sp2 concepts list orbital_overlay among preferred representations. The reader's video blocks for Hybridization: from sp3 to sp2 to sp have url "" and is_hidden true; visible assets are methane, ethane, ethylene, and acetylene molecule blocks.
 - Needed outcome: Learners need a visible, instructionally equivalent representation that makes orbital orientation, retained unhybridized p orbitals, and sigma-versus-pi overlap inspectable across sp3, sp2, and sp carbon.
 - Confidence: 0.98
- **instructor-005 · medium · misconception** — The octet rule is stated for main-group elements generally, and the characteristic valences of carbon, nitrogen, and oxygen are presented without explicitly limiting them to common neutral second-row patterns. Charged structures and familiar octet exceptions are not acknowledged.
 - Location: section_id=atoms-electrons-covalent-bonds; concept_slug=atoms-electrons-covalent-bonds; nugget_id=nugget-atoms-bonds; anchor_text=Main-group elements are most stable when surrounded by eight valence electrons
 - Learner impact: Students may treat formal-charge patterns such as ammonium, oxonium, or carbanions as invalid and may overextend the octet heuristic to elements for which expanded or incomplete octets occur.
 - Evidence: The prose says main-group elements are most stable with eight valence electrons and then states carbon forms four bonds, nitrogen three with one lone pair, and oxygen two with two lone pairs. Only the oxygen assessment prompt adds the qualifier "neutral."
 - Needed outcome: The chapter needs to frame these valence counts as common neutral patterns for the principal second-row organic elements and establish that charge and defined octet exceptions alter the pattern.
 - Confidence: 0.96
- **instructor-006 · medium · misconception** — The bond-length trend is attached to the comparison of ethane, ethylene, and acetylene without separating the effect of increasing sigma-bond s character from the simultaneous increase in carbon-carbon bond order and number of pi bonds.
 - Location: section_id=sp-hybridization; concept_slug=sp-hybridization; nugget_id=nugget-sp; anchor_text=as the s character of the hybrid orbital increases from sp3 to sp2 to sp, bonds shorten
 - Learner impact: Students may incorrectly attribute the entire single-to-double-to-triple carbon-carbon bond shortening trend to hybridization and fail to distinguish bond-order effects from hybrid-orbital effects.
 - Evidence: The sp section introduces acetylene's short, strong triple bond and immediately explains the series by increasing s character from sp3 to sp2 to sp.
 - Needed outcome: The explanation needs to distinguish the contribution of hybrid-orbital s character from the independent effect of carbon-carbon bond order when interpreting bond lengths and strengths.
 - Confidence: 0.94
- **instructor-007 · medium · retrieval-practice** — Each source nugget defines a practice_check, but none of those checks appears in the compiled reader sections. The reader contains text, molecule blocks, hidden video blocks, and external links only.
 - Location: section_id=nugget-sp3; concept_slug=sp3-hybridization; nugget_id=nugget-sp3; anchor_text=What bond angle is expected at an sp3-hybridized carbon, and why?
 - Learner impact: Students reading the chapter cannot pause to retrieve and apply each section's central idea, and instructors lose the intended formative checkpoints unless another runtime surface injects them.
 - Evidence: The topic package includes the quoted sp3 practice check and analogous checks for all six nuggets. The compiled reader section nugget-sp3 has no practice or question block, and the same omission occurs in every compiled section.
 - Needed outcome: The assigned reader experience needs to expose section-level retrieval opportunities or an equivalent clearly connected formative path for all six concepts.
 - Confidence: 0.93
- **instructor-008 · medium · misconception** — The storyboard phrase "Remove one p orbital" is chemically ambiguous and may imply that the orbital disappears. In the sp2 model, one p orbital is excluded from the hybridization combination and remains on carbon precisely so it can form the pi bond.
 - Location: asset_id=video-hybridization; concept_slug=sp2-hybridization-pi-bonds; anchor_text=Remove one p orbital to form three sp2 orbitals and a pi bond in ethylene.
 - Learner impact: If visualized literally, the sequence would undermine the chapter's explanation of how an unhybridized p orbital produces the pi bond.
 - Evidence: The video-hybridization storyboard first says to build four sp3 orbitals and then says to remove one p orbital to form three sp2 orbitals and a pi bond.
 - Needed outcome: The hybridization sequence needs to preserve and explicitly distinguish the unhybridized p orbital from the orbitals combined into the sp2 set.
 - Confidence: 0.95

**Open questions**

- Does the reader runtime inject the compiled question set or source practice checks outside the chapter JSON, or are these activities currently inaccessible from the assigned reading flow?
- Does the molecule renderer expand implicit hydrogens and provide a three-dimensional or electron-pair view for the SMILES C, O, and N? Without that behavior, the methane, water, and ammonia blocks cannot visibly demonstrate their stated geometry and lone-pair goals.
- Are formal charge, resonance, and octet exceptions intentionally assigned to a neighboring topic package? They are not present here despite the chapter's foundational Structure and Bonding scope.

### Struggling Student

**Score:** 5.4/10 · **publication blockers:** none

The chapter has a sensible broad progression, but a learner with weak prerequisites is asked to absorb foundational vocabulary, orbital models, three-dimensional geometry, polarity, and drawing conventions with almost no visible step-by-step practice. The source package contains useful practice checks, yet they are absent from the compiled reader, and the four-question bank leaves major objectives unrehearsed. I could often repeat the stated rule, but I would not feel able to apply it to a new molecule without guessing.

**Strengths**

- The six concepts follow a coherent macro-sequence from covalent bonding through sp3, sp2, and sp hybridization before moving to polarity and drawing conventions.
- The hybridization sections consistently state characteristic geometry and sigma/pi bond counts, giving the learner useful summary rules once the underlying model is understood.
- The source package includes a focused practice_check for every nugget, and the compiled questions generally provide concise corrective feedback and hints.

**Findings**

- **student-001 · high · cognitive-load** — The opening three paragraphs introduce orbitals, energy levels, valence electrons, the octet rule, ions, covalent bonds, Lewis structures, bonding pairs, lone pairs, and four characteristic valences without walking through the electron count for even one complete Lewis structure.
 - Location: section_id=atoms-electrons-covalent-bonds; concept_slug=atoms-electrons-covalent-bonds; nugget_id=nugget-atoms-bonds; anchor_text=An atom consists of a small, dense nucleus of protons and neutrons surrounded by electrons that occupy orbitals of increasing energy.
 - Learner impact: A weak-prerequisite student is likely to reread the paragraph, memorize that carbon has four bonds and oxygen has two, and move on without knowing how the octet rule produces those numbers.
 - Evidence: The reader moves directly from "electrons that occupy orbitals of increasing energy" to "the octet rule" and then to "Counting to an octet gives the characteristic valences"; the molecule blocks for Water and Methane show final structures but no intermediate electron counting.
 - Needed outcome: The opening needs an incremental bridge that lets the learner use valence-electron counts to construct and check at least one bond-and-lone-pair arrangement before relying on the summary valence rules.
 - Confidence: 0.97
- **student-002 · high · conceptual-support** — The first hybridization section assumes that the learner understands ground-state 2s and 2p orbitals, orbital equivalence, and what it means for orbitals to be "combined" even though the preceding section only names orbitals generally.
 - Location: section_id=sp3-hybridization; concept_slug=sp3-hybridization; nugget_id=nugget-sp3; anchor_text=Carbon has four valence electrons and forms four bonds, but its ground-state 2s and 2p orbitals are not equivalent.
 - Learner impact: A low-confidence student is likely to treat sp3 as a label to memorize or form the mistaken picture that physical orbitals simply merge because carbon needs four bonds, without understanding the purpose or limits of the model.
 - Evidence: The transition is from the first section's general statement that electrons "occupy orbitals of increasing energy" to "one 2s and three 2p orbitals are combined into four equivalent sp3 hybrid orbitals," with no intervening explanation of orbital occupancy or hybridization as a model.
 - Needed outcome: The transition into hybridization needs enough prerequisite support to explain what problem the model solves, what is being combined, and how the result connects to four equivalent carbon bonds.
 - Confidence: 0.95
- **student-003 · high · cognitive-load** — The sp2 and sp sections ask the learner to mentally coordinate planes, perpendicular p orbitals, end-on versus side-on overlap, sigma and pi bonds, restricted rotation, and an s-character trend. The only compiled hybridization video has an empty URL and is_hidden true, while the visible molecule blocks show connectivity rather than the orbital relationships described.
 - Location: concept_slug=sp2-hybridization-pi-bonds; nugget_id=nugget-sp2; asset_id=video-hybridization; anchor_text=Side-on overlap of this p orbital with the corresponding p orbital on the adjacent carbon produces a π bond
 - Learner impact: A student who struggles to integrate prose and spatial models will guess at which orbital makes which bond and may memorize "double equals one pi" and "triple equals two pi" without understanding geometry or rotation.
 - Evidence: The reader states that a p orbital "stands perpendicular to that plane" and that pi density lies "above and below the sigma framework"; the following section adds two mutually perpendicular p orbitals and the sp3-to-sp2-to-sp s-character trend. Blocks blk-2d6fh9oy and blk-ycu3thq7 compile the relevant video with url "" and is_hidden true.
 - Needed outcome: These sections need a concrete, available representation or explanation that lets the learner map each orbital orientation to the corresponding sigma or pi bond and check that mapping before the text adds rotation and bond-length trends.
 - Confidence: 0.98
- **student-004 · high · worked-example-gap** — The section introduces electron-pair geometry, lone-pair effects, electronegativity, partial charges, bond polarity, molecular shape, dipole cancellation, and net dipole in three paragraphs, but it never works through the intermediate decisions for a molecule.
 - Location: section_id=molecular-shape-polarity; concept_slug=molecular-shape-polarity; nugget_id=nugget-shape-polarity; anchor_text=Whether a molecule as a whole is polar depends on both its bond polarities and its shape.
 - Learner impact: The student can repeat that water is bent and polar but will stall on a new molecule because they do not know the order in which to count electron pairs, identify bond dipoles, judge symmetry, and decide whether cancellation occurs.
 - Evidence: The text moves from "four pairs give a tetrahedral arrangement" to δ− and δ+ and then to "Symmetric arrangements can cancel the individual bond dipoles" without showing how those claims are applied step by step. The only question set contains no question for concept_slug molecular-shape-polarity.
 - Needed outcome: The learner needs a fully reasoned example that makes the decision sequence from electron-pair arrangement through molecular shape and bond dipoles to net molecular polarity explicit and transferable.
 - Confidence: 0.98
- **student-005 · high · worked-example-gap** — The line-angle convention is stated once and followed by finished ethanol and acetic-acid structures, but the chapter never demonstrates how to count vertices, restore implied hydrogens, or convert among Lewis, condensed, and line-angle forms.
 - Location: section_id=drawing-organic-structures; concept_slug=drawing-organic-structures; nugget_id=nugget-drawing; anchor_text=carbon atoms are represented by the ends and vertices of a zig-zag of lines, hydrogen atoms on carbon are not drawn
 - Learner impact: A shaky student will count visible labels rather than carbon vertices, omit or add hydrogens incorrectly, and then guess at later structures even though implied hydrogens are the concept's named trouble spot.
 - Evidence: The topic package explicitly names "Missing the implied hydrogens on carbon in a line-angle drawing" as the trouble spot. The compiled assessment only asks "Name the functional group that characterizes ethanol (CH3CH2OH)," which tests recognition from a condensed formula rather than decoding a line-angle structure.
 - Needed outcome: The chapter needs guided reasoning and feedback that let the learner reconstruct carbon and hydrogen counts from a line-angle structure and recognize the common vertex/end-point mistakes.
 - Confidence: 0.99
- **student-006 · high · retrieval-practice** — The source package gives every nugget a practice_check, but none of those checks appears in the compiled reader, and the compiled question set covers only four of the six concepts. It omits sp3 hybridization and molecular shape/polarity and does not directly test line-angle decoding.
 - Location: concept_slug=sp3-hybridization; anchor_text="questions": 4
 - Learner impact: A student who mistakes familiarity for mastery can read all six sections without an immediate checkpoint, then finish the bank without discovering that they cannot explain tetrahedral hybridization, predict polarity, or recover implied hydrogens.
 - Evidence: Each of nugget-atoms-bonds, nugget-sp3, nugget-sp2, nugget-sp, nugget-shape-polarity, and nugget-drawing has a practice_check in topic.package.json. The reader sections contain text, molecule/video, and external-link blocks but no practice blocks. question-set.json reports "questions": 4 and its concept slugs exclude sp3-hybridization and molecular-shape-polarity.
 - Needed outcome: Students need timely retrieval opportunities for every stated chapter objective, especially the unrehearsed sp3, polarity, and line-angle reasoning, with feedback that exposes rather than conceals weak understanding.
 - Confidence: 0.99
- **student-007 · medium · misconception** — The hint introduces "groups" as a counting unit that the chapter never defines, and it does not warn that a multiple bond counts as one electron group rather than multiple bond lines.
 - Location: concept_slug=sp-hybridization; question_slug=ch1-sp-hybridized-carbon; anchor_text=Count the groups on each carbon; sp carbons bear only two.
 - Learner impact: A weak student may look at acetylene's triple bond, count three bond lines plus the C–H bond, reject the correct answer, and conclude that the earlier linear-geometry rule is inconsistent.
 - Evidence: The question hint says "Count the groups on each carbon; sp carbons bear only two," while the chapter text describes two sigma bonds and two pi bonds but never teaches electron-group counting terminology.
 - Needed outcome: The assessment cue needs to use a counting rule already defined in the chapter and explicitly prevent the common mistake of counting the lines in a multiple bond as separate groups.
 - Confidence: 0.96

**Open questions**

- Are the six source practice_check objects rendered through another student-facing surface, or are they unintentionally lost from the compiled reader?
- Is video-hybridization intentionally unavailable while its status is needs_review, and what student-facing support is expected until its URL is populated?

### Accessibility Persona

**Score:** 6.3/10 · **publication blockers:** access-001

The chapter provides concise, chemically specific alt text for every molecule and repeats most spatial chemistry in prose, giving learners a substantially usable text path. However, one short-answer accessibility description reproduces a grading-accepted answer, two structure-based questions do not communicate the bond-order information shown in their molecular options, several figure descriptions omit their stated teaching point, and the planned hybridization video lacks a documented equivalent for its visual transformations. Runtime keyboard, heading, notation-pronunciation, and media-control behavior cannot be established from these files.

**Strengths**

- All eight molecule assets have concise, molecule-specific alt text rather than generic labels.
- The prose explicitly states most spatially important chemistry, including tetrahedral, planar, linear, bent, and pyramidal geometry, reducing reliance on figures alone.
- All four compiled questions include accessible descriptions, and three avoid stating a correct option or chemical verdict directly.
- The ethanol and acetic-acid descriptions communicate their functional-group connectivity clearly enough for these simple static figures.

**Findings**

- **access-001 · blocker · alt-text-quality** — The accessible description supplies “-OH,” which is itself listed as an accepted answer in the question's answer_key.
 - Location: concept_slug=drawing-organic-structures; question_slug=ch1-ethanol-functional-group; anchor_text=Type the name of the functional group in ethanol (the -OH group).
 - Learner impact: A learner receiving the accessible description can submit text already supplied by the question and receive credit without performing the functional-group identification required of other learners.
 - Evidence: The compiled question pairs accessible_description “Type the name of the functional group in ethanol (the -OH group).” with accepted answers including “-OH” and “OH.”
 - Needed outcome: The nonvisual wording needs to preserve the ethanol stimulus and naming task without reproducing any grading-accepted response or otherwise identifying the requested group for the learner.
 - Confidence: 0.99
- **access-002 · high · media-equivalence** — Each option includes a molecular structure through structure_smiles, but the accessible description supplies only the molecule names and does not communicate the single-, double-, or triple-bond structures shown to a sighted learner.
 - Location: concept_slug=sp-hybridization; question_slug=ch1-sp-hybridized-carbon; anchor_text=Choose the molecule whose carbons are sp-hybridized from ethane, ethene, and acetylene.
 - Learner impact: A learner unable to inspect the rendered structures must infer structural information from nomenclature alone and does not receive an equivalent stimulus for determining hybridization.
 - Evidence: The options pair Ethane with “CC,” Ethene with “C=C,” and Acetylene with “C#C,” while accessible_description lists only “ethane, ethene, and acetylene.”
 - Needed outcome: The nonvisual stimulus needs to communicate the chemically relevant connectivity and bond order of every option while leaving the hybridization inference to the learner.
 - Confidence: 0.9
- **access-003 · high · media-equivalence** — The multi-select options include molecular structures through structure_smiles, but the accessible description lists names without conveying the bond orders visible in those structures.
 - Location: concept_slug=sp2-hybridization-pi-bonds; question_slug=ch1-pi-bond-molecules; anchor_text=Select all molecules containing a pi bond from ethene, acetylene, and ethane.
 - Learner impact: A nonvisual learner receives less structural evidence than a sighted learner and may be forced to rely on memorized compound names rather than apply the requested multiple-bond reasoning.
 - Evidence: The student_config includes “C=C,” “C#C,” and “CC” for the three options, whereas accessible_description provides only their names.
 - Needed outcome: The accessible stimulus needs to expose each option's relevant structural features without stating which options contain pi bonds.
 - Confidence: 0.9
- **access-004 · medium · alt-text-quality** — The water asset's stated learning goal includes oxygen's two lone pairs, but its alt text mentions only two O-H bonds and bent geometry.
 - Location: concept_slug=atoms-electrons-covalent-bonds; nugget_id=nugget-atoms-bonds; asset_id=mol-water; anchor_text=Show a simple molecule with two bonds and two lone pairs on oxygen.
 - Learner impact: The figure description omits the electron-pair information the asset is intended to reinforce. Nearby prose supplies that fact, so the chapter remains learnable, but the figure is not independently equivalent.
 - Evidence: The learning_goal is “Show a simple molecule with two bonds and two lone pairs on oxygen,” while alt_text is “Structure of water: an oxygen atom bonded to two hydrogen atoms in a bent geometry.”
 - Needed outcome: The figure's accessible description needs to include the lone-pair information that is load-bearing for its stated instructional purpose.
 - Confidence: 0.97
- **access-005 · medium · alt-text-quality** — The methane asset is intended to demonstrate tetrahedral geometry, but its alt text reports only a central carbon bonded to four hydrogens.
 - Location: concept_slug=sp3-hybridization; nugget_id=nugget-sp3; asset_id=mol-methane; anchor_text=Show the tetrahedral geometry of an sp3-hybridized carbon.
 - Learner impact: A learner relying on the figure description does not receive the three-dimensional relationship that gives the figure its instructional purpose, although the adjacent prose mitigates the omission.
 - Evidence: The learning_goal specifies “tetrahedral geometry of an sp3-hybridized carbon,” while alt_text is “Structure of methane: a central carbon bonded to four hydrogen atoms.”
 - Needed outcome: The figure description needs to communicate the tetrahedral arrangement central to the asset's learning goal.
 - Confidence: 0.96
- **access-006 · medium · alt-text-quality** — The ethylene asset's learning goal is planarity at sp2 carbons, but its alt text describes only atom and bond counts.
 - Location: concept_slug=sp2-hybridization-pi-bonds; nugget_id=nugget-sp2; asset_id=mol-ethylene; anchor_text=Show a planar carbon–carbon double bond from sp2 carbons.
 - Learner impact: The accessible figure description omits the spatial property the figure is meant to teach. Adjacent prose states that ethylene is planar, reducing but not eliminating the mismatch.
 - Evidence: The learning_goal is “Show a planar carbon–carbon double bond from sp2 carbons,” while alt_text is “Structure of ethylene: two carbons joined by a double bond, each bearing two hydrogens.”
 - Needed outcome: The accessible description needs to include the planar arrangement that is chemically relevant to the figure's purpose.
 - Confidence: 0.95
- **access-007 · medium · media-equivalence** — The video brief relies on animated construction and transformation of orbital models, but it contains no accessibility transcript or description of the meaningful visual changes. Its narration outline states concepts without narrating those transformations, and the compiled reader blocks are currently hidden with empty URLs.
 - Location: concept_slug=sp3-hybridization; asset_id=video-hybridization; anchor_text=Hybridization: from sp3 to sp2 to sp
 - Learner impact: If the media is activated as authored, learners unable to perceive the animation—especially GIF-only presentation—may miss how the orbital arrangement changes from sp3 to sp2 to sp.
 - Evidence: The storyboard says “Build four sp3 orbitals,” “Remove one p orbital,” and “Reduce to two sp orbitals,” while narration_outline only directs the narrator to state hybridization principles and trends. No accessibility or transcript field is present.
 - Needed outcome: Before activation, the media needs an equivalent account of its changing orbital arrangements and a way for learners who cannot perceive or follow motion to access the same sequence and relationships.
 - Confidence: 0.94

**Open questions**

- Does the question renderer expose each structure_smiles value through an accessible chemical label in addition to the compiled accessible_description?
- Are the question controls, molecule links, and any editor launched through /generator fully keyboard-operable with visible focus and programmatic labels?
- When video-hybridization receives a URL and becomes visible, will the player provide captions, meaningful visual narration, pause/replay or step controls, and a non-motion equivalent?
- How do supported screen-reader and browser combinations announce strings such as sp3, 2p, H₂C=CH₂, σ, π, δ−, and δ+ in the rendered reader?
- What semantic heading levels and landmarks does the reader UI assign to chapter and section titles? The compiled JSON establishes order but not rendered heading semantics.
- Are the compiled questions required for chapter completion? That determines whether the unresolved structure-equivalence barriers in access-002 and access-003 are publication-blocking.

### Learner with Visual Preference

**Score:** 6.2/10 · **publication blockers:** none

The chapter has a clear conceptual progression and attaches small, purposeful molecule examples to every section, but the compiled reader relies heavily on prose and basic molecular structures for ideas that are intrinsically spatial. Lewis electron pairs, orbital overlap, the sp3/sp2/sp comparison, dipole-vector cancellation, and the translation into line-angle notation are not made visibly inspectable in the available blocks. The hidden hybridization video indicates awareness of the largest spatial burden, but its current reader entries are unavailable and locally misdescribed. No visual issue is a publication blocker, though the chapter would benefit materially from tighter alignment between each visual, its stated learning goal, and the relationship the learner is meant to see.

**Strengths**

- Every molecule asset has a stated learning goal, concept and nugget linkage, editable SMILES, and a learner-facing text alternative, giving the visuals clearer instructional intent than decorative imagery.
- The chapter's sp3-to-sp2-to-sp sequence is logically ordered, and the recurring methane, ethylene, and acetylene examples provide stable molecular anchors for the changing bonding models.
- The compiled questions pair structure_smiles with molecule names such as Ethane, Ethene, and Acetylene, so the assessed choices are not dependent on recognizing an unlabeled structure image.
- The hybridization video remains hidden while its status is needs_review and its URL is empty, avoiding a broken visible control in the current reader.

**Findings**

- **visual-001 · medium · figure-purpose** — The section introduces Lewis structures by contrasting bonding pairs with lone pairs, and the water asset's learning goal is to show "two bonds and two lone pairs on oxygen." In the compiled reader, however, the available block is a generic molecule configured from SMILES "O"; its alt text says only that oxygen is bonded to two hydrogens in a bent geometry and does not identify the two lone pairs. No available block is explicitly configured as a Lewis electron-pair representation.
 - Location: section_id=atoms-electrons-covalent-bonds; concept_slug=atoms-electrons-covalent-bonds; nugget_id=nugget-atoms-bonds; asset_id=mol-water; anchor_text=each bonding pair is drawn as a line between two atoms and each nonbonding pair as a lone pair
 - Learner impact: A learner cannot readily connect the prose convention of lines and lone pairs to a visible, labeled example at the exact point where that convention is introduced, increasing the burden of mentally constructing the representation.
 - Evidence: Topic asset mol-water states the learning goal "Show a simple molecule with two bonds and two lone pairs on oxygen." Reader block blk-4odxiyrb contains smiles "O" and alt text "Structure of water: an oxygen atom bonded to two hydrogen atoms in a bent geometry."
 - Needed outcome: The first Lewis-structure example needs to make bonding pairs and nonbonding pairs distinguishable, with the visual purpose and description both covering the electron-pair information the prose asks learners to read.
 - Confidence: 0.95
- **visual-002 · medium · visual-opportunity** — The core explanation depends on the perpendicular orientation of an unhybridized p orbital, side-on overlap, and electron density above and below the sigma framework. The topic package names "orbital_overlay" as a preferred representation for this concept, but the compiled section contains only the ethylene molecule block plus a hidden video with an empty URL; the available molecule's description addresses planarity but not the orbital relationship.
 - Location: section_id=sp2-hybridization-pi-bonds; concept_slug=sp2-hybridization-pi-bonds; nugget_id=nugget-sp2; asset_id=mol-ethylene; anchor_text=Side-on overlap of this p orbital with the corresponding p orbital on the adjacent carbon produces a π bond
 - Learner impact: The learner must infer a three-dimensional orbital-overlap model from dense spatial prose while the visible example primarily confirms that ethylene has a double bond.
 - Evidence: Concept sp2-hybridization-pi-bonds lists preferred_representations ["molecule", "orbital_overlay"]. Reader section nugget-sp2 includes molecule blk-bmg4sfph and hidden video blk-2d6fh9oy with url ""; the molecule description is "Show a planar carbon–carbon double bond from sp2 carbons."
 - Needed outcome: The section needs an inspectable representation or description that makes the p-orbital orientation, side-on overlap, and resulting above/below-plane electron-density relationship concrete rather than leaving all three relationships in prose.
 - Confidence: 0.97
- **visual-003 · medium · visual-opportunity** — The sp3, sp2, and sp cases are presented in three separate sections and the culminating trend sentence asks the learner to compare orbital count, angle, geometry, pi-bond count, and bond length across them. The visible assets are separate molecule blocks, while the only cross-series treatment is video-hybridization, which is status "needs_review" in the topic package and hidden with an empty URL in all three compiled sections.
 - Location: section_id=sp-hybridization; concept_slug=sp-hybridization; nugget_id=nugget-sp; anchor_text=as the s character of the hybrid orbital increases from sp3 to sp2 to sp, bonds shorten and the geometry changes from tetrahedral to trigonal planar to linear
 - Learner impact: The learner must retain details from earlier sections and mentally align several changing attributes, making the most important comparative pattern harder to scan and self-check.
 - Evidence: Nuggets nugget-sp3, nugget-sp2, and nugget-sp each reference video-hybridization. The video brief's title is "Hybridization: from sp3 to sp2 to sp" and its storyboard covers all three cases, but reader blocks blk-j44zuyoh, blk-2d6fh9oy, and blk-ycu3thq7 are is_hidden true with url "".
 - Needed outcome: The chapter needs a readily comparable summary of the sp3-to-sp2-to-sp relationships so geometry, angle, remaining p orbitals, and sigma/pi composition can be inspected together without depending on an unavailable video.
 - Confidence: 0.96
- **visual-004 · medium · visual-opportunity** — The prose distinguishes polar bonds from a net molecular dipole through vector cancellation, but the reader provides only molecule blocks for water and ammonia. Their descriptions establish bent and pyramidal shape; neither block's content identifies bond-dipole directions, partial charges, a net dipole, or a symmetric cancellation case.
 - Location: section_id=molecular-shape-polarity; concept_slug=molecular-shape-polarity; nugget_id=nugget-shape-polarity; asset_id=mol-water; anchor_text=Symmetric arrangements can cancel the individual bond dipoles
 - Learner impact: A learner can see the example shapes but cannot directly inspect why bond dipoles add in those shapes or what cancellation would look like, leaving the key bond-polarity-versus-molecular-polarity distinction abstract.
 - Evidence: Reader section nugget-shape-polarity states that symmetric arrangements can cancel bond dipoles and that water and ammonia retain a net dipole. Blocks blk-jep4lhff and blk-v949zhr9 contain ammonia and water with shape-oriented descriptions but no dipole or partial-charge information.
 - Needed outcome: The section needs the directional relationship between individual bond polarities, molecular shape, cancellation, and the net molecular dipole to be explicitly inspectable for both a noncancelling and a cancelling arrangement.
 - Confidence: 0.96
- **visual-005 · medium · visual-opportunity** — The section explains the translation from a condensed formula to line-angle notation and the inference of omitted carbon-bound hydrogens, but the compiled reader shows ethanol and acetic acid only as separate molecule blocks. The ethanol text supplies CH3CH2OH, while its block description and alt text name the chain and hydroxyl group without exposing the end/vertex-to-carbon mapping or the implied-hydrogen count.
 - Location: section_id=drawing-organic-structures; concept_slug=drawing-organic-structures; nugget_id=nugget-drawing; asset_id=mol-ethanol; anchor_text=carbon atoms are represented by the ends and vertices of a zig-zag of lines
 - Learner impact: A learner who is new to skeletal notation must perform the representational translation mentally and gets no visible check of how explicit atoms disappear while carbon valence is preserved.
 - Evidence: Reader text in nugget-drawing gives condensed CH3CH2OH and explains ends, vertices, and implied hydrogens. Block blk-3ta5odpm has alt text "Line structure of ethanol: a two-carbon chain ending in a hydroxyl (OH) group" and description "Show the hydroxyl functional group in a line-angle structure."
 - Needed outcome: The introduction to skeletal notation needs the correspondence among condensed atoms, line ends or vertices, and implied hydrogens to be traceable in the example rather than only asserted in prose.
 - Confidence: 0.94
- **visual-006 · low · figure-purpose** — Each hidden hybridization video block in the sp3, sp2, and sp sections repeats only the first storyboard step, "Build four sp3 orbitals on carbon and show tetrahedral methane." In the sp2 and sp sections this local description does not state the section-specific role of ethylene or acetylene even though the topic-level brief contains later storyboard steps for them.
 - Location: section_id=sp2-hybridization-pi-bonds; concept_slug=sp2-hybridization-pi-bonds; nugget_id=nugget-sp2; anchor_text=Build four sp3 orbitals on carbon and show tetrahedral methane.
 - Learner impact: If the currently hidden media is activated as configured, its surrounding description will make its purpose ambiguous and may direct attention back to methane instead of the orbital change taught in the current section.
 - Evidence: Reader blocks blk-j44zuyoh, blk-2d6fh9oy, and blk-ycu3thq7 all use the same description. Topic video brief video-hybridization separately lists storyboard steps for sp3 methane, sp2 ethylene, and sp acetylene.
 - Needed outcome: Before this media becomes available, each placement needs a section-aligned purpose and description that identifies the relevant stage of the sp3-to-sp2-to-sp comparison.
 - Confidence: 0.99
- **visual-007 · medium · alt-text-quality** — The methane asset's explicit learning goal is tetrahedral geometry, but its compiled alt text says only "a central carbon bonded to four hydrogen atoms." Unlike the acetylene, water, and ammonia alternatives, it omits the geometry that gives the figure its instructional purpose.
 - Location: section_id=sp3-hybridization; concept_slug=sp3-hybridization; nugget_id=nugget-sp3; asset_id=mol-methane; anchor_text=The four sp3 orbitals point toward the corners of a regular tetrahedron
 - Learner impact: A learner relying on the description receives atom connectivity but not the spatial relationship the section is using methane to establish.
 - Evidence: Topic asset mol-methane has learning_goal "Show the tetrahedral geometry of an sp3-hybridized carbon." Reader block blk-ffdkw4x2 uses alt_text "Structure of methane: a central carbon bonded to four hydrogen atoms."
 - Needed outcome: The methane figure's text equivalent needs to convey the tetrahedral arrangement and its connection to the approximately 109.5-degree bond angle, not connectivity alone.
 - Confidence: 0.98

**Open questions**

- Do molecule blocks render an inspectable 3D geometry or only a conventional 2D structure from SMILES? The compiled artifact does not specify the rendering mode.
- Is video-hybridization intended for this chapter version, and will its three placements receive section-specific descriptions before it is unhidden?
- Does the molecule renderer display implicit hydrogens and lone pairs for SMILES such as "C" and "O"? The reader JSON does not state these display settings.

### Orchestrator verification

- **orchestrator-001 · high · conceptual-support** — The compiler derives Wikipedia paths directly from internal concept titles. All six Chapter 1 URLs therefore point to non-existent article slugs such as Atoms,_electrons,_and_covalent_bonding and sp3_hybridization_and_the_tetrahedral_carbon. A learner following the provided background-reading help reaches missing pages and loses a support path.

### Orchestrator decisions

| rec | need | chosen intervention | rationale | target | severity | sources |
|---|---|---|---|---|---|---|
| rec-001 | Assessment feedback must define sp hybridization by two electron domains and linear geometry without excluding allenic or other valid sp carbons. | prose-edit | One sentence in the existing feedback causes the error; a precise local rewrite fully corrects it. | assessment | blocker | instructor-001 |
| rec-002 | The ethanol prompt must not reproduce an accepted answer, and structure-based options must expose bond order without revealing the inference. | text-equivalent | Neutral, chemically descriptive wording corrects the access gap without changing question interaction. | assessment | blocker | access-001, access-002, access-003 |
| rec-003 | Students and instructors need direct evidence for sp3 geometry, shape/polarity reasoning, and actual line-angle decoding. | added-practice | New questions are required because the current four-item bank cannot measure the omitted objectives. | assessment | high | instructor-002, instructor-003, student-004, student-005, student-006 |
| rec-004 | The six source practice checks need a visible formative path rather than being dropped from the compiled reader. | added-practice | The content already exists; the reader/compiler integration, not new question authoring, is the missing piece. | practice | high | instructor-007, student-006 |
| rec-005 | Learners need an available representation of sp3/sp2/sp geometry, retained p orbitals, and sigma-versus-pi overlap. | static-image-sequence | A labeled static comparison can carry the spatial relationships without waiting for a produced video. | figure | high | instructor-004, student-002, student-003, visual-002, visual-003 |
| rec-006 | The chapter needs stepwise examples for Lewis counting, polarity decisions, and condensed-to-skeletal translation. | prose-edit | Worked examples can extend the existing sections without requiring a new interaction type. | prose | high | student-001, student-004, student-005 |
| rec-007 | Water, methane, and ethylene descriptions need the lone-pair, tetrahedral, and planar information their figures are intended to reinforce. | structured-chemical-description | The adjacent prose already carries the chemistry, so improving the existing descriptions is sufficient. | figure | medium | access-004, access-005, access-006, visual-001, visual-007 |
| rec-008 | The octet/valence statements, bond-length trend, electron-group hint, and hybridization storyboard need wording that does not seed later misconceptions. | prose-edit | Each issue is a local explanatory overstatement rather than missing infrastructure. | prose | medium | instructor-005, instructor-006, instructor-008, student-007, visual-006 |
| rec-009 | All six compiled Wikipedia links must resolve to real, relevant articles. | prose-edit | Explicit Wikipedia article slugs in concept metadata let the existing compiler emit valid links. | prose | high | orchestrator-001 |
| rec-010 | Any activated animation needs a section-aligned description, meaningful visual narration, and a non-motion equivalent. | transcript | The video is currently hidden; documenting the equivalent before activation prevents a new barrier without forcing immediate production. | figure | medium | access-007, visual-006 |

### Retained disagreements

- **Whether missing structure details in question descriptions are publication blockers.** Accessibility Persona: High-severity equivalence gaps, with blocker status contingent on whether the activities are required. Organic Chemistry Instructor: The named choices make the chemistry answerable, but assessment coverage is not sufficient. **Resolution:** Treat the answer leak as the live access blocker and the missing structural descriptions as high-priority corrections; do not claim formal activity incompletability without runtime evidence.
- **Media required for hybridization.** Learner with Visual Preference: A visible comparison would materially reduce the explanation burden. Accessibility Persona: Any activated motion needs an equivalent account and controls. **Resolution:** Prefer a labeled static comparison plus structured description; keep the unproduced video hidden until it has an equivalent.

### Places where a description is sufficient (no new asset)

- The ethanol and acetic-acid molecule alt text already communicates the relevant functional-group connectivity.
- The oxygen-valence question description is task-focused and answer-neutral.
- The visible molecule examples are purposeful; they do not need animation merely because hybridization is spatial.

### Regression targets for next run

instructor-001, instructor-002, instructor-003, instructor-004, instructor-005, instructor-006, instructor-007, instructor-008, student-001, student-002, student-003, student-004, student-005, student-006, student-007, access-001, access-002, access-003, access-004, access-005, access-006, access-007, visual-001, visual-002, visual-003, visual-004, visual-005, visual-006, visual-007, orchestrator-001

---

## Post-correction record

**Estimated state: major revision (not a second persona verdict).**

### Changes applied

- Corrected `ch1-sp-hybridized-carbon` feedback: sp carbon is defined by two
 electron groups and linear geometry; a triple bond is a common example, not
 an exclusive requirement.
- Rewrote its hint to explain that single, double, and triple bonds each count
 as one electron group.
- Removed `-OH` and `OH` from the ethanol question’s accepted answer names and
 rewrote its accessibility description without naming the answer.
- Added answer-neutral bond-order descriptions to the sp-hybridization and
 pi-bond question options.
- Expanded water, methane, and ethylene alternatives to include the
 load-bearing lone-pair, tetrahedral/109.5°, and planar information.
- Qualified the octet/valence prose as common neutral second-row patterns and
 noted formal-charge changes and defined exceptions.
- Separated the influence of hybrid-orbital s character from the simultaneous
 increase in carbon–carbon bond order.
- Corrected the video storyboard so unhybridized p orbitals remain present, and
 added a structured transcript plus static-equivalent requirement before the
 video can be made visible.
- Replaced all six fabricated Wikipedia targets with verified real article
 slugs and added a compiler override so internal concept titles no longer have
 to double as external article names.
- Restored curated chemistry display notation across the canonical package and
 generated Chapter 1 surfaces, including σ/π symbols and formula subscripts in
 H₂C=CH₂, CH₃CH₂OH, and –CO₂H.

### Verification

- Chapter compilation completed with 6 concepts, 6 nuggets, 8 assets, and 4
 questions.
- Topic-package suite: **50 passed**.
- The synthesized report passes its schema and cross-reference validator.
- All six corrected Wikipedia targets resolve.
- Compiled descriptions, answer keys, prose, and figure alternatives were
 spot-checked.

### Still recommended

- Add direct assessment for sp3 geometry and shape/polarity reasoning.
- Test actual line-angle decoding, not just functional-group naming from a
 condensed formula.
- Surface the six existing `practice_check` items in the reader.
- Add a static, inspectable sp3/sp2/sp orbital comparison.
- Add transferable worked examples for Lewis counting, polarity decisions, and
 skeletal translation.

The next four-persona regression run should confirm `instructor-001`,
`access-001`–`access-006`, `instructor-005`, `instructor-006`,
`instructor-008`, `student-007`, `visual-001`, `visual-007`, and
`orchestrator-001` as resolved.
