# Chapter review — Structure Determination: Mass Spectrometry and Infrared Spectroscopy (`mass-spectrometry-and-infrared-spectroscopy`)

_Reviewed 2026-07-25 · chapter version 1 · personas: Instructor, Struggling Student, Accessibility, Visual Preference_

**Publication readiness: major revision**

The chemistry is verified sound — the Instructor checked every m/z value, isotope ratio, IR band position, SMILES, fragmentation outcome, and all 22 answer keys and found zero errors, and accessibility text-equivalence is unusually strong (structural alt text throughout, leak-free task descriptions on all 22 questions). No persona filed a publication blocker. The readiness verdict is nevertheless 'major revision' because three personas independently converged on one structural gap in the chapter's core skill: a spectrum-reading chapter whose reader never displays a single spectrum — no mass-spectrum bar graph, no IR trace, no four-region map — while its figure captions promise spectral signatures the plain structures cannot show. Secondary consensus items: all six background-reading links are fabricated Wikipedia URLs; authored per-section practice checks never compile into the reader; the capstone worked example uses 'degree of unsaturation' undefined and skips the mass-to-formula step; and the interactive question types' keyboard/screen-reader operability could not be verified from authoring artifacts. Bounded verified errors (links, captions, prose gaps, prerequisite metadata, a wavenumber inconsistency) are corrected in this run; the spectrum-figure need requires a new pipeline asset kind and remains the headline revision item.

### Top blockers

_(none — no persona filed a publication blocker and no blocker-severity finding exists)_

### Top 5 recommended changes

1. **Show actual spectra in the teaching sections** — The chapter teaches reading mass spectra and IR spectra, but the reader displays no spectrum, no fragment ladder, no isotope doublet, and no four-region map; band SHAPE and peak-pattern recognition are asserted in prose only, and the first spectrum a student meets is one they are graded on. → **new-figure** (figure, high)
2. **Replace fabricated Wikipedia background-reading links** — All six external links point to nonexistent articles auto-derived from concept titles; the only external scaffold is dead. → **prose-edit** (prose, high)
3. **Make figure captions state facts the figure can support** — Molecule captions are imperative authoring goals ('Anchor…', 'Tie the equal-intensity doublet…', 'Recognize the broad O–H band…') that promise spectral features the structure drawing does not display, sending students hunting for absent content. → **prose-edit** (figure, high)
4. **Verify interactive question-type operability (keyboard / screen reader / motion)** — spectrum_peaks band selection, the drag-family types (rank_order, matching_pairs, categorize_groups), and the evidence_board grid must be completable without a fine pointer and be announced with row/column context; the vibration animation should honor pause and reduced-motion. None of this is verifiable from authoring artifacts. → **instructor-note** (interactive, high)
5. **Surface per-section practice checks in the reader** — Every nugget has an authored practice_check, but the reader compiles none of them, so a student reads six dense sections with no inline checkpoint; the 22-item bank lives entirely outside the reading flow. → **alternate-activity** (practice, high)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 8.0/10 | 0 | Chemistry uniformly correct; go with minor revisions — but no spectrum is ever shown and two objectives go unassessed. |
| Struggling Student | 5.5/10 | 0 | Clear prose that names my traps, but no spectra, no inline checkpoints, and an undefined 'degree of unsaturation' would stall me. |
| Accessibility Persona | 7.2/10 | 0 | Excellent text equivalence and leak-free descriptions; interactive-type operability unverifiable from artifacts. |
| Learner with Visual Preference | 5.7/10 | 0 | A spectroscopy chapter with zero spectra in the reader; captions promise signatures the figures don't show. |

### Affected sections & assets

`nugget-ms-basics`, `nugget-fragmentation`, `nugget-isotopes`, `nugget-ir-basics`, `nugget-ir-regions`, `nugget-strategy`; assets `mol-propane`…`mol-benzaldehyde` (captions), `video-bond-vibrations`; questions `ch12-click-oh-band`, `ch12-rank-stretch-frequencies`, `ch12-neutral-loss-matching`, `ch12-ir-region-categorize`, `ch12-unknown-evidence-board`, `ch12-vibration-frequency-range`; all six compiled external-link blocks.

---
## Full evidence

### Independent persona reports

#### Organic Chemistry Instructor — 8.0/10

Go, with minor revisions. The chemistry is sound throughout: every m/z value (propane 44, hexan-2-one 100, neopentane M 72 / tert-butyl 57, isobutane 43, triethylamine 101, 1-bromopropane 122/124), isotope ratio (Cl 3:1, Br 1:1, 1.1% per C for M+1), IR band position (O-H 3350, X-H 2850-3600, Câ¡C 2120, Câ¡N 2250, C=O 1715, C=C 1650, fingerprint <1500), fragmentation outcome (alpha cleavage of butan-2-one to m/z 43 and 57, hexan-2-one McLafferty to m/z 58), SMILES, and answer key I checked is correct, and the compiled reader and question set are faithful to the source. The prose consistently builds mechanistic 'why' (the spring model, dipole-change intensity rule, carbocation-stability driver, and the negative-evidence discipline are genuine strengths), and 22 validated questions across nine types with variants give solid coverage. What holds it back from a clean go: the nitrogen rule and the M+1 carbon-count â both stated learning objectives and taught in prose â are never assessed; the structure-determination concept omits the isotopes concept from its prerequisites despite leaning on it; and a chapter whose entire purpose is reading spectra shows students no actual mass spectrum and no IR trace within the teaching sections, only molecule structures. None of these is a chemistry blocker; all are fixable before or during assignment.

**Strengths:**
- Chemical accuracy is uniformly high: verified m/z arithmetic (propane 44, hexan-2-one 100, neopentane loss-of-methyl to tert-butyl 57, isobutane 43, triethylamine 101), isotope ratios (Cl 3:1, Br 1:1, M+1 ~1.1% per carbon), and IR band positions across all regions are correct, and the fragmentation outcomes (butan-2-one acylium at 43/57, hexan-2-one McLafferty at 58) are right.
- The prose consistently teaches the 'why' rather than outcomes to memorize: the spring/mass model for vibrational frequency, the dipole-change rule for band intensity, carbocation stability as the driver of fragmentation, and the parity origin of the nitrogen rule are all reasoned, not asserted.
- The structure-determination section models genuine expert practice, including the discipline of negative evidence (absent O-H excludes alcohols/acids; empty carbonyl region excludes four families at once) that novices routinely neglect.
- Assessment is varied and validated: 22 questions across nine question types with paired variants, correct answer keys (compiled set matches source exactly), and feedback that diagnoses specific wrong answers (e.g., m/z 84 omits the oxygen; isopropyl appears at 43 not 57).
- The trouble_spots target real, well-known student errors (M+ treated as closed-shell cation, wavenumber vs wavelength, nitrogen rule applied backwards, trying to assign the fingerprint region peak by peak).

**Findings:**

- **`instr-001`** [medium / sequencing] (concept_slug=structure-determination-strategy, nugget_id=nugget-strategy, anchor_text=its parity applies the nitrogen rule, and any M+2 pattern reveals chlorine or bromine)
 - Observation: The concept structure-determination-strategy lists prerequisites ["fragmentation-patterns", "characteristic-ir-absorptions"] but omits isotopes-and-molecular-formulas, even though its own nugget prose depends heavily on that concept: it invokes the nitrogen rule ('the parity applies the nitrogen rule'), the halogen M+2 signatures ('a 1:1 doublet for bromine, a 3:1 pair for chlorine'), and the M+1 carbon count. Every worked-strategy step reuses material that only the isotopes concept establishes.
 - Learner impact: In any sequence honoring the declared prerequisite graph, a student could reach the capstone strategy section without having covered isotope patterns and the nitrogen rule, then be asked to apply exactly those tools. The dependency the prose actually assumes is not the dependency the metadata records.
 - Evidence: concepts[5].prerequisites = ["fragmentation-patterns", "characteristic-ir-absorptions"]; nugget-strategy expanded text: 'The parity of the mass invokes the nitrogen rule... The isotope envelope is scanned for the halogen signatures â a 1:1 doublet for bromine, a 3:1 pair for chlorine â and the M+1 intensity offers a rough carbon count.'
 - Recommended outcome: The prerequisite graph needs to reflect that the combined-evidence strategy depends on the isotopes-and-molecular-formulas concept, so the chapter's declared sequencing matches the reasoning the prose requires.
 - Confidence: 0.9
- **`instr-002`** [medium / objective-alignment] (concept_slug=isotopes-and-molecular-formulas, nugget_id=nugget-isotopes, anchor_text=Apply the nitrogen rule to decide whether a compound contains an odd number of nitrogen atoms.)
 - Observation: The isotopes concept declares three learning objectives â recognize Cl/Br from M+2, explain the M+1 peak, and apply the nitrogen rule â but only the first is assessed. Both questions for this concept (ch12-halogen-isotope-id and its v2) test halogen M+2 patterns; no question anywhere tests the nitrogen rule or the M+1 carbon count, despite the nitrogen rule being a headline objective and reused in the strategy section.
 - Learner impact: Students get no retrieval practice on the nitrogen rule or the M+1-to-carbon-count estimate, the two isotope ideas most likely to be tested on an exam and most easily applied backwards (an odd-mass ion implies an odd number of nitrogens, not the reverse â a trouble spot the concept itself flags). An instructor cannot check mastery of an objective the chapter never assesses.
 - Evidence: nugget-isotopes learning_objectives include 'Explain the origin of the small M+1 peak' and 'Apply the nitrogen rule'; the only isotope questions are answer_key [redacted] and {answer_text [redacted]}. trouble_spots: 'Applying the nitrogen rule backwards.'
 - Recommended outcome: Assessment coverage is needed for the nitrogen rule (e.g., inferring nitrogen count / parity from a molecular-ion mass) and for the M+1 carbon-count estimate, so all three stated objectives of this concept are actually tested.
 - Confidence: 0.88
- **`instr-003`** [medium / visual-opportunity] (concept_slug=mass-spectrometry-basics, nugget_id=nugget-fragmentation, anchor_text=the result is drawn as a bar graph of relative abundance versus m/z)
 - Observation: This is a spectrum-reading chapter, yet the teaching sections show no mass spectrum at all. The MS nuggets describe the base peak, the m/z axis, the fragment ladder (hexane at 57/43/29), the near-absent neopentane molecular ion, and the Cl/Br isotope doublets entirely in prose, and every MS asset is a bare molecule structure (propane, hexane, hexan-2-one, the halopropanes, triethylamine). No MS question renders a spectrum either â the MS items are numeric/select/matching. Students are asked to reason about peak heights and spacings they never see plotted.
 - Learner impact: The core skill of the chapter â reading a bar-graph mass spectrum â is taught without a single worked example of the object itself. Students who cannot mentally construct the plot from prose (a weak molecular ion beside a tall fragment, a 3:1 versus 1:1 satellite pair) miss the visual pattern recognition that MS interpretation actually is.
 - Evidence: assets[] are all type 'molecule'; nugget-ms-basics: 'the result is drawn as a bar graph of relative abundance versus m/z'; nugget-fragmentation: 'its molecular ion at m/z 72 is nearly absent'; no spectrum-type asset or MS spectrum_peaks question exists.
 - Recommended outcome: The MS sections need at least one annotated mass-spectrum representation (e.g., a labelled M+/base-peak/fragment-ladder plot and an isotope-doublet plot) so the peak-height and peak-spacing reasoning the prose describes is shown, not only asserted.
 - Confidence: 0.82
- **`instr-004`** [low / visual-opportunity] (concept_slug=characteristic-ir-absorptions, nugget_id=nugget-ir-regions, anchor_text=The spectrum is therefore read against a four-region map rather than band by band.)
 - Observation: The IR teaching sections describe the four-region map and characteristic band shapes (broad rounded O-H, sharp N-H doublet, â¡C-H spike, strong C=O) but no IR trace or region map appears in the reader prose; the only IR spectra reach students inside two spectrum_peaks questions, and the intended spring-model video (video-bond-vibrations) is deferred and hidden (is_hidden:true). Band shape is explicitly taught as diagnostic ('band shape matters as much as position'), yet shape can only be conveyed by a drawn band.
 - Learner impact: The distinction the chapter says is essential â a broad rounded O-H versus a sharp N-H versus a sharp â¡C-H at nearly the same wavenumber â cannot be learned from wavenumbers alone; without a shown band contour, students may reduce IR to a table of numbers and miss the shape cue the trouble_spots warn about.
 - Evidence: nugget-ir-regions: 'Band shape matters as much as position here'; reader video block blk-ifheb72h has url:'' and is_hidden:true; video_briefs[0].production_status 'deferred'. IR spectra appear only in ch12-click-oh-band and its v2.
 - Recommended outcome: The IR teaching section needs a shown four-region map and at least one annotated IR trace illustrating the contrasting band shapes, so the shape-based discrimination the prose relies on is visible during instruction and not only in two questions.
 - Confidence: 0.75
- **`instr-005`** [low / objective-alignment] (concept_slug=fragmentation-patterns, nugget_id=nugget-fragmentation, anchor_text=a process called alpha cleavage)
 - Observation: Alpha cleavage is a stated learning objective ('Recognize alpha cleavage as the characteristic fragmentation of carbonyl compounds') and the McLafferty rearrangement is taught in the expanded prose and referenced in the mol-2-hexanone learning goal, but no question directly tests either. The fragmentation questions (neopentane/isobutane cation ID, neutral-loss matching) cover only alkane C-C cleavage and mass differences; acylium/alpha-cleavage recognition surfaces only obliquely inside the evidence-board feedback.
 - Learner impact: Students taught that carbonyl compounds are diagnosed by alpha cleavage to acylium ions (m/z 43/57 for the butanone/hexanone examples) get no practice identifying or predicting that fragmentation, leaving a headline carbonyl-fragmentation objective unassessed.
 - Evidence: nugget-fragmentation learning_objectives: 'Recognize alpha cleavage as the characteristic fragmentation of carbonyl compounds'; expanded text teaches McLafferty (m/z 58) and acylium (m/z 43); no question_set has concept_slug fragmentation-patterns testing acylium/alpha cleavage â the four are neopentane-base-peak (x2) and neutral-loss-matching (x2).
 - Recommended outcome: Added practice is needed that tests recognition or prediction of alpha cleavage / acylium formation (and optionally the even-mass McLafferty clue) so the carbonyl-fragmentation objective is directly assessed.
 - Confidence: 0.78
- **`instr-006`** [low / conceptual-support] (section_id=nugget-fragmentation, anchor_text=Wikipedia â Fragmentation follows cation stability)
 - Observation: Every reader section carries an 'external_link' block whose URL is auto-generated by slugifying the concept title into a Wikipedia path â e.g. https://en.wikipedia.org/wiki/Fragmentation_follows_cation_stability, https://en.wikipedia.org/wiki/Isotope_peaks_and_the_nitrogen_rule, https://en.wikipedia.org/wiki/A_four-region_map_locates_functional_groups. These are not real Wikipedia articles; the titles are ChemIllusion nugget headings, not encyclopedia entries, so the links resolve to nonexistent pages.
 - Learner impact: An instructor who assigns the chapter, or a student who follows the 'Background reading' link, lands on a dead or wrong Wikipedia page, undermining trust in the chapter's supporting resources. This is a compile-pipeline artifact rather than a chemistry error, but it degrades instructor-facing polish.
 - Evidence: reader blocks blk-m3eiejvi, blk-acumv6bp, blk-y7pk52ni, blk-s0gxcw4y, blk-sqvckotu, blk-w3ej1nwe each point to en.wikipedia.org/wiki/<slugified nugget title>; none corresponds to an existing article.
 - Recommended outcome: The external background-reading links need to resolve to real, topic-appropriate resources (or be removed) so assigned reading does not point students at nonexistent pages.
 - Confidence: 0.7

**Open questions:**
- Finding instr-006 concerns broken auto-generated Wikipedia links; the schema's category list has no clean fit, so I filed it under conceptual-support. If these link blocks recur across chapters, a dedicated category such as 'external-resource-integrity' may be warranted for regression diffing.
- The video-bond-vibrations brief is deferred and its reader block is hidden (is_hidden:true), with a production_note saying the prose carries the same content. Is the chapter intended to publish without any dynamic IR/spring-model asset, relying on the two molecular_vibration questions to supply the animated equivalent?
- Is a rendered mass spectrum (bar graph) planned as a future asset type for this reader, or is the design decision to teach MS interpretation from prose plus molecule structures only?

#### Struggling Student — 5.5/10

The prose is clear, well-sequenced, and unusually good at naming the traps a shaky student falls into (Mâº as a radical cation, m/z vs mass, base peak â  molecular ion, absent bands as evidence), and the separate question bank is excellent â hints, wrong-answer explanations, and a variant for every item. But the chapter as a student actually reads it has two gaps that would stall someone like me. First, the entire chapter is about reading spectra, yet the reader shows only bare molecular structures â no mass-spectrum bar graph and no IR spectrum or four-region map appear anywhere in the six sections, so every sentence about 'the tallest peak' or the 'broad band near 3350 cmâ»Â¹' asks me to picture something I have never been shown. Second, the reader carries no inline retrieval practice or checkpoints: the authored practice_checks and the 22-question bank live outside the reading flow, so a low-confidence student reads six dense passages with nothing to test understanding against. Add an undefined 'degree of unsaturation' in the capstone worked example and a McLafferty rearrangement dropped in a single sentence, and there are several concrete places I would reread, guess, or quit.

**Strengths:**
- The prose explicitly names the exact misconceptions a shaky student holds and corrects them in place â Mâº as a radical cation not a closed-shell cation, m/z equalling mass only for singly charged ions, the base peak usually not being the molecular ion, and absent IR bands counting as evidence.
- The question bank is strong scaffolding where it exists: every item has a leveled hint ladder and most have specific wrong-answer explanations, and each question has a parallel variant for a second attempt.
- Concept prerequisites are stated and the six sections build in a sensible order (ionization â fragmentation â isotopes/formula â IR basics â IR regions â combined strategy), ending with a worked example that ties the two techniques together.
- Importance is signaled well in places â the C=O near 1715 cmâ»Â¹ is called 'the single most diagnostic band,' and recurring mass losses (Mâ15, Mâ18) are flagged as 'worth memorizing.'

**Findings:**

- **`struggle-001`** [high / conceptual-support] (section_id=nugget-ms-basics, nugget_id=nugget-ms-basics, anchor_text=The spectrum is presented as a bar graph of ion abundance against m/z, with the tallest peak, the base peak)
 - Observation: The whole chapter teaches how to READ spectra, but no mass spectrum is ever shown in the reader. The MS sections describe 'a bar graph of ion abundance against m/z,' the 'base peak,' the M+2 isotope doublet, and fragment 'peaks below the molecular ion,' yet the only figures in these sections are plain molecular structures (propane, hexane, hexan-2-one, the halides, triethylamine). A student never sees an actual peak, axis, or intensity ratio.
 - Learner impact: A low-confidence learner who has never seen a mass spectrum cannot form a mental picture from the prose alone. Reading 'an M+2 peak one-third the intensity of Mâº' or 'a 1:1 doublet at m/z 122 and 124' with no picture of what that looks like, I would reread the paragraph, still not visualize it, and fall back to memorizing words without understanding â then fail the spectrum-reading questions in the bank because I practiced only on prose.
 - Evidence: Reader sections nugget-ms-basics, nugget-fragmentation, and nugget-isotopes contain only block_type 'text' and 'molecule' (structures via SMILES) plus an external link; no spectrum figure exists. Contrast with the question bank, which does render spectra (ch12-click-oh-band peaks at 3350/2930/1055) â but those are not in the reader.
 - Recommended outcome: The reader needs a worked visual of at least one real mass spectrum (peaks on an m/z axis with base peak, Mâº, and an isotope/fragment example) so a student sees the object the prose describes before being asked to interpret it.
 - Confidence: 0.9
- **`struggle-002`** [high / conceptual-support] (section_id=nugget-ir-regions, nugget_id=nugget-ir-regions, anchor_text=The spectrum is therefore read against a four-region map rather than band by band.)
 - Observation: The IR sections repeatedly reference a 'four-region map' and specific band positions and shapes (broad OâH near 3350, sharp â¡CâH spike near 3300, strong C=O near 1715, the fingerprint region), but the reader shows no IR spectrum and no picture of the four-region map. The only IR figures are molecular structures (hex-1-yne, pent-1-ene, hexan-1-ol, cyclohexanone, benzaldehyde), and the planned spring-model video is hidden/deferred.
 - Learner impact: The core skill of this chapter is matching a band's position and SHAPE to a functional group, but shape ('broad, rounded' vs 'sharp spike') cannot be learned from words. Without an image of the four-region map or a real spectrum, I would memorize the number list (3350, 2120, 1715) without being able to recognize any band on an actual spectrum, and guess on the interpretation questions.
 - Evidence: nugget-ir-regions text describes the four regions and band shapes; the reader block for the animation (blk-ifheb72h, video 'Watching bonds vibrate') has "url": "" and "is_hidden": true, and video_brief video-bond-vibrations is production_status 'deferred'. No IR spectrum figure or region-map figure is present.
 - Recommended outcome: The reader needs a visual of the four-region IR map and at least one annotated real IR spectrum (showing band position AND shape) so band shape and region boundaries are something a student can see, not just read.
 - Confidence: 0.9
- **`struggle-003`** [high / retrieval-practice] (section_id=nugget-ms-basics, nugget_id=nugget-ms-basics, anchor_text=The peaks below the molecular ion â the fragmentation pattern â carry structural information of their own, taken up in the next section.)
 - Observation: The reader flow contains no inline checkpoints, self-check questions, or section summaries. Each nugget has an authored practice_check in the topic package (e.g., 'Propane... At what m/z does its molecular ion appear?'), but none of these are compiled into the reader; the 22-item question bank is also separate and none are demo_eligible (demo_eligible: 0). The student reads six dense passages back-to-back with nothing to check understanding.
 - Learner impact: A shaky student needs to test recall before moving on; without a checkpoint after each section, I don't discover I misunderstood 'base peak' or the nitrogen rule until much later (or never). I would finish the chapter with false confidence, or lose momentum from the sheer volume of uninterrupted prose and quit before the strategy section.
 - Evidence: Every nugget in topic.package.json has a populated 'practice_check' (e.g., nugget-ms-basics practice_check.prompt), but the compiled reader (frontend/public/reader/.../mass-spectrometry-and-infrared-spectroscopy.json) contains only text, molecule, video, and external_link blocks â no question or practice block in any section.
 - Recommended outcome: The reader needs an inline retrieval-practice checkpoint (the authored practice_check or a bank item) at the end of each section so a student can verify understanding before the next dense passage.
 - Confidence: 0.85
- **`struggle-004`** [medium / conceptual-support] (section_id=nugget-strategy, nugget_id=nugget-strategy, anchor_text=The mass fits CâHâO; the carbonyl band and one degree of unsaturation indicate a ketone or aldehyde)
 - Observation: The capstone worked example uses 'one degree of unsaturation' as if it were established, but the term is never defined anywhere in this chapter and is not listed as a prerequisite for the structure-determination-strategy concept (prerequisites are only fragmentation-patterns and characteristic-ir-absorptions).
 - Learner impact: The worked example is meant to be the payoff where everything comes together, but 'degree of unsaturation' is exactly the phrase where I would stall: I don't know what it means or how it follows from CâHâO, so the logical link from formula to 'ketone or aldehyde' breaks and I stop trusting that I can follow the method.
 - Evidence: nugget-strategy uses 'one degree of unsaturation' in both the standard and expanded text; no nugget or concept in the package defines degrees/index of unsaturation, and the concept's prerequisites list does not include it.
 - Recommended outcome: The worked example needs the 'degree of unsaturation' step either defined/computed in place or replaced with a plain-language explanation of how the carbonyl accounts for the formula, so the formula-to-functional-group link is followable.
 - Confidence: 0.85
- **`struggle-005`** [medium / worked-example-gap] (section_id=nugget-strategy, nugget_id=nugget-strategy, anchor_text=The molecular ion's m/z fixes the molecular mass, and with it the short list of molecular formulas of that nominal mass.)
 - Observation: The worked example jumps from 'Mâº at m/z 72' to 'suggest CâHâO' without showing how a nominal mass is turned into a candidate molecular formula. The intermediate reasoning (which the text calls 'the short list of molecular formulas of that nominal mass') is the exact step a struggling student cannot perform unaided, and it is skipped.
 - Learner impact: I can read that 72 'fits' CâHâO, but I cannot reproduce that step on a new problem because I was never shown how to generate or narrow the formula list from a mass. On the evidence-board and unknown questions I would guess the formula rather than derive it.
 - Evidence: nugget-strategy expanded text asserts 'The even mass and the absence of halogen patterns suggest CâHâO' with no shown computation; the question bank (ch12-unknown-evidence-board) similarly gives the candidates rather than teaching how to reach them.
 - Recommended outcome: The worked example needs the missing intermediate step made explicit â how to go from a nominal mass (with nitrogen-rule and isotope clues) to a small set of candidate formulas â so the strategy is reproducible, not just readable.
 - Confidence: 0.8
- **`struggle-006`** [medium / cognitive-load] (section_id=nugget-fragmentation, nugget_id=nugget-fragmentation, anchor_text=the McLafferty rearrangement, in which that hydrogen migrates to oxygen and a neutral alkene is expelled, leaving an even-mass fragment)
 - Observation: The final paragraph of the fragmentation section introduces alpha cleavage, the acylium ion, resonance stabilization, the McLafferty rearrangement, hydrogen migration, alkene expulsion, and the even-mass clue in rapid succession. The McLafferty rearrangement in particular is a genuinely hard, multi-step process compressed into a single sentence with no diagram and is not named in the section's learning objectives.
 - Learner impact: By the end of that paragraph I am tracking too many new ideas at once; the McLafferty sentence, with a hydrogen migrating and an alkene leaving all in one clause, is where I would give up trying to follow the mechanism and just try to memorize 'even-mass fragment = rearrangement' without understanding why.
 - Evidence: nugget-fragmentation expanded text final paragraph packs alpha cleavage, acylium resonance, McLafferty rearrangement, and the even-mass rule together; the learning_objectives for the nugget mention alpha cleavage but not McLafferty, signaling the reader is left to absorb it unscaffolded.
 - Recommended outcome: The McLafferty content needs either a step-by-step visual/scaffold or clear demotion as optional/enrichment, so the dense last paragraph does not overload a student right after the core fragmentation idea.
 - Confidence: 0.75
- **`struggle-007`** [low / figure-purpose] (section_id=nugget-ms-basics, asset_id=mol-propane, anchor_text=Anchor the molecular-ion concept: electron impact converts propane into the radical cation Mâº at m/z 44.)
 - Observation: The molecule figures' visible captions are authoring goals phrased as instructions ('Anchor the molecular-ion concept...', 'Recognize the broad OâH band near 3350 cmâ»Â¹...', 'Tie the equal-intensity Mâº/M+2 doublet...'), and they ask the student to 'recognize' or 'tie' spectral features that the structure figure does not actually display.
 - Learner impact: Under a plain structure of hexan-1-ol I am told to 'Recognize the broad OâH band near 3350 cmâ»Â¹,' but there is no band to recognize in the picture. The mismatch between caption and image makes me feel I am missing something on the page, so I reread looking for a band that was never there.
 - Evidence: Reader molecule blocks carry description = the asset learning_goal, e.g. blk-b2y2i00z (hexan-1-ol) 'Recognize the broad OâH band near 3350 cmâ»Â¹ and the CâO stretch near 1050 cmâ»Â¹', shown beneath a structure-only rendering.
 - Recommended outcome: The molecule captions need student-facing wording that matches what the figure actually shows (the structure and the bond responsible), rather than instructions to recognize spectral features absent from the image.
 - Confidence: 0.7
- **`struggle-008`** [medium / conceptual-support] (section_id=nugget-ms-basics, anchor_text=Background reading on Electron-impact ionization and the molecular ion. Opens on Wikipedia.)
 - Observation: Every section's only supplementary 'Background reading' link is a Wikipedia URL auto-generated from the nugget/concept title (e.g., en.wikipedia.org/wiki/Electron-impact_ionization_and_the_molecular_ion, .../Fragmentation_follows_cation_stability, .../A_four-region_map_locates_functional_groups). These are not real Wikipedia article titles and will almost certainly resolve to nonexistent pages.
 - Learner impact: When I am confused and click the one 'Background reading' lifeline offered, I would land on a missing/blank Wikipedia page. For a low-confidence student that is both a dead end and a small blow to trust in the whole chapter, and it removes the only external scaffold provided.
 - Evidence: external_link blocks in every reader section use url built from the concept title with underscores, e.g. blk-s0gxcw4y url 'https://en.wikipedia.org/wiki/Electron-impact_ionization_and_the_molecular_ion' and blk-y7pk52ni '.../A_four-region_map_locates_functional_groups' â phrasings that are section headings, not encyclopedia entries.
 - Recommended outcome: The supplementary links need to point at real, resolvable references on these standard topics (mass spectrometry, infrared spectroscopy) so the offered scaffold actually works when a stuck student uses it.
 - Confidence: 0.6
- **`struggle-009`** [low / notation-consistency] (section_id=nugget-ir-basics, nugget_id=nugget-ir-basics, anchor_text=Câ¡C near 2100 cmâ»Â¹, C=C near 1650 cmâ»Â¹, CâC near 1000 cmâ»Â¹)
 - Observation: The Câ¡C stretch is given as 'near 2100 cmâ»Â¹' in the body of nugget-ir-basics but as 'near 2120 cmâ»Â¹' in the same nugget's practice_check answer, in the mol-hex-1-yne learning goal, and in nugget-ir-regions. Similar small variation appears across carbonyl values, but the 2100/2120 clash sits inside a single section.
 - Learner impact: Seeing two different numbers for what I think is the same bond makes me unsure which to memorize, so I second-guess an answer I actually knew, or assume I misread and lose confidence in the number set.
 - Evidence: nugget-ir-basics standard/expanded: 'Câ¡C near 2100 cmâ»Â¹'; same nugget practice_check answer: 'The Câ¡C stretch (near 2120 cmâ»Â¹)'; nugget-ir-regions: 'the Câ¡C stretch of an alkyne near 2120 cmâ»Â¹'.
 - Recommended outcome: The Câ¡C stretch value needs to be stated consistently (a single number or an explicit range) across the section body, its practice check, and the figure captions.
 - Confidence: 0.7

**Open questions:**
- Are the authored per-nugget practice_checks intended to be surfaced in the reader, or is all retrieval practice meant to live only in the separate question bank? The reader currently shows neither.
- Is a mass-spectrum figure and/or an IR-spectrum figure planned for the reader but not yet compiled (the bank clearly can render spectra), or is the chapter intended to teach spectrum-reading using only structure figures?
- The spring-model vibration video is authored but hidden and deferred â is a static visual substitute planned for the reader, since the IR-basics prose leans heavily on the spring analogy?

#### Accessibility Persona — 7.2/10

On its text and metadata this chapter is unusually strong for accessibility: every molecule figure carries a structural (not merely naming) alt text, the spectral information the chapter teaches is carried in prose and in text form rather than trapped in images, the reader contains no visual-only spectrum that lacks a text equivalent, the deferred vibration video is hidden rather than left as a captionless placeholder, and every one of the 22 questions ships an accessible_description that states the task without leaking the answer, with all interactive options text-labelled (cations named alongside their structures, IR peaks labelled with their wavenumbers, evidence-board candidates given names and formulas). The open risks are all about the operability of the interactive question types, which cannot be confirmed from these authoring artifacts: the spectrum_peaks 'click the band' task is inherently spatial/pointer-driven, and matching_pairs, categorize_groups, rank_order, and the evidence_board grid are drag/grid patterns whose keyboard-and-screen-reader alternatives are not visible in the data. Because I cannot verify the reader UI's interaction behavior, I log these as high-priority needs plus open questions rather than asserting blockers. The molecular_vibration animation is well mitigated because the vibrating bond is named in the prompt and described in the accessible_description, so motion is not a sole carrier of meaning.

**Strengths:**
- Every molecule figure's alt_text describes the actual structure (chain length, substituent identity and position, e.g. 'Hexan-2-one: a six-carbon chain with a ketone carbonyl on the second carbon' and 'Triethylamine: a central nitrogen atom bonded to three ethyl groups') rather than merely naming the image.
- All spectral information the chapter teaches (m/z values, base peak, isotope ratios, wavenumbers, band shape) is carried in the prose and in text form; the reader contains no visual-only mass spectrum or IR trace that lacks a text equivalent.
- Every one of the 22 questions ships an accessibility_bundle.accessible_description that conveys the task without leaking the answer (e.g., the halogen-ID item says 'name the halogen responsible for this isotope pattern' without naming it).
- Interactive options are consistently text-labelled so no distinction rests on a visual alone: single_select cations are named beside their SMILES, spectrum_peaks bands carry visible wavenumber labels, and evidence_board candidates carry names and molecular formulas.
- The molecular_vibration questions name the vibrating bond in the prompt and describe its motion in the accessible_description, so the animation is redundant rather than the sole carrier of meaning.
- The deferred bond-vibration video is marked is_hidden in the reader with its content preserved in nugget-ir-basics prose, avoiding a captionless or narration-less video placeholder.
- Sections carry descriptive titles that give a coherent heading and reading order through the six nuggets.

**Findings:**

- **`access-001`** [high / keyboard-operability] (question_slug=ch12-click-oh-band, concept_slug=structure-determination-strategy, anchor_text=Click the band produced by the OâH stretch.)
 - Observation: The spectrum_peaks questions (ch12-click-oh-band and ch12-click-oh-band-v2) require the learner to click a band on a rendered IR spectrum. The task verb and interaction are inherently spatial/pointer-driven. The peak data does include text labels ('3350 cmâ»Â¹', '2930 cmâ»Â¹', '1055 cmâ»Â¹'), which could back a non-spatial selection, but nothing in these artifacts confirms the reader exposes the three bands as keyboard-focusable, screen-reader-labelled, selectable controls rather than click-only targets on an SVG/canvas.
 - Learner impact: A learner using a keyboard, switch device, or screen reader â or anyone who cannot use a fine pointer â may be unable to complete a required assessment of the structure-determination concept if selection is pointer-only. This is one of only two question types anchoring that concept.
 - Evidence: ch12-click-oh-band student_config.spectrum.peaks[] with ids peak_3350/peak_2930/peak_1055 and text labels; prompt_text 'Click the band produced by the OâH stretch.'; accessibility_bundle.accessible_description names the task ('select the band corresponding to the stretch named in the question') but does not establish an operable non-pointer path.
 - Recommended outcome: Every learner must be able to select the intended band without a fine pointer â the three labelled bands need to be reachable and choosable by keyboard and announced by a screen reader (a text-list equivalent of the labelled peaks would satisfy this), not clickable-only on a rendered plot.
 - Confidence: 0.6
- **`access-002`** [high / interactive-fallback] (question_slug=ch12-rank-stretch-frequencies, concept_slug=ir-spectroscopy-basics, anchor_text=Rank these stretching vibrations from highest to lowest wavenumber.)
 - Observation: The rank_order, matching_pairs, and categorize_groups questions are classic drag-arrangement patterns (rank_order cards to be ordered; matching_pairs left-to-right pairing; categorize_groups items dropped into region buckets). All of their content is text (no color/position-only meaning), but the authoring artifacts do not show any keyboard-operable, non-drag interaction path, and drag-and-drop without an alternative is a known barrier for keyboard, switch, and screen-reader users.
 - Learner impact: Learners who cannot perform drag gestures (keyboard-only, switch, tremor/motor-impairment, some screen-reader users) may be unable to complete these required practice items, which span three of the chapter's core IR/MS concepts (six of the eleven surfaced questions are drag-family).
 - Evidence: ch12-rank-stretch-frequencies (rank_order, cards c_oh/c_cc3/c_co2/c_co1); ch12-neutral-loss-matching (matching_pairs, left l_15â¦ / right r_ch3â¦); ch12-ir-region-categorize (categorize_groups, items i_ohâ¦ into groups g_xhâ¦), plus their v2 variants. None expose a documented keyboard alternative in student_config or grading_rules.
 - Recommended outcome: Each ordering/matching/categorizing activity needs a confirmed non-drag interaction path (e.g., keyboard move/select-and-assign) so a learner without fine-pointer or drag capability can complete the same required question.
 - Confidence: 0.55
- **`access-003`** [high / interactive-fallback] (question_slug=ch12-unknown-evidence-board, concept_slug=structure-determination-strategy, anchor_text=Mark how each observation bears on each candidate, eliminate the inconsistent structure, and choose the final answer.)
 - Observation: The evidence_board questions present a two-dimensional grid (candidates Ã evidence) in which each cell must be marked Supports/Contradicts/Neutral, followed by an elimination and a final selection. Content is fully text-labelled (candidates carry names and formulas alongside SMILES, evidence and statuses are text, and the accessible_description conveys the whole task without leaking marks), which is good; but the grid marking is a multi-step spatial interaction whose keyboard-and-screen-reader operability and cell-relationship semantics are not verifiable from these artifacts.
 - Learner impact: This grid is the capstone reasoning activity for the structure-determination concept. If the cell-by-cell marking is not keyboard-operable and does not announce its row/column context, a screen-reader or keyboard-only learner may be unable to complete or even parse the required activity.
 - Evidence: ch12-unknown-evidence-board student_config with candidates cand_ketone/cand_alcohol, evidence ev_mz/ev_co/ev_nooh, statuses support/contradict/neutral; answer_key.expected_marks is a candidateÃevidence matrix; same shape in -v2.
 - Recommended outcome: The evidence grid needs a confirmed keyboard-operable marking mechanism with programmatic row/column labelling so a non-visual or non-pointer learner can mark every cell, perform the elimination, and select the final answer.
 - Confidence: 0.55
- **`access-004`** [low / interactive-fallback] (question_slug=ch12-vibration-frequency-range, concept_slug=ir-spectroscopy-basics, asset_id=video-bond-vibrations, anchor_text=The animation shows the OâH stretching vibration of methanol.)
 - Observation: The molecular_vibration questions embed a 3D animation (asset_url /assets/vibrations/*.json) played in the reader. The barrier is well mitigated because the vibrating bond is named in the prompt ('the OâH stretching vibration of methanol') and fully described in the accessible_description, so motion is not the sole carrier of meaning and the four answer options are plain text. What is not verifiable is whether the animation can be paused/replayed/stepped and whether it honors reduced-motion preferences.
 - Learner impact: Learners sensitive to motion, or those who need to pause/replay, may be affected if the 3D animation auto-loops without controls; however, because the content is redundantly available in text, no learner is blocked from answering.
 - Evidence: ch12-vibration-frequency-range student_config.template 'choose_frequency_range', mode_id methanol_oh_stretch, asset_url /assets/vibrations/methanol_oh_stretch.json; accessible_description narrates the bond lengthening/shortening; options aâd are text ranges.
 - Recommended outcome: The vibration animation should offer pause/replay control and respect reduced-motion settings; no text-equivalent gap exists because the mode is already named and described.
 - Confidence: 0.6

**Open questions:**
- Does the reader's spectrum_peaks widget expose the three labelled IR bands as keyboard-focusable, screen-reader-announced selectable controls, or is band selection pointer-only on a rendered SVG/canvas? (Determines whether access-001 is a blocker.)
- Do the rank_order, matching_pairs, and categorize_groups question types provide a keyboard-operable, non-drag interaction path in the reader? (Determines whether access-002 is a blocker.)
- Is the evidence_board grid keyboard-operable, and does it programmatically expose each cell's candidate (column) and evidence (row) context to assistive technology? (Determines whether access-003 is a blocker.)
- Can the molecular_vibration 3D animation be paused, replayed, or stepped, and does it respect prefers-reduced-motion?

#### Learner with Visual Preference — 5.7/10

The prose is careful, accurate, and richly quantitative, and every molecule figure is chemically correct with clean alt text. But this is a chapter whose entire subject is reading spectra, and the compiled reader never shows a single spectrum. Both mass spectra (bar graphs of abundance vs m/z, base peaks, fragment ladders, isotope doublets) and IR spectra (transmittance vs wavenumber, band shapes, the four-region map) are described in dense text and illustrated only by plain 2D structures of the example molecules. Those structures do not depict the spectral feature each asset's stated learning goal promises to teach, so the visual that would most reduce explanation burden is absent throughout. Notably, the question bank already carries the missing visual infrastructure (clickable IR spectrum peak data, molecular-vibration animations, an evidence board), which a learner meets only inside graded items and never as a worked example in the reader. No figure is wrong, so there are no blockers; the gaps are opportunities, but for a spectroscopy chapter they are consequential.

**Strengths:**
- Every molecule figure is chemically correct (verified SMILES for propane, hexane, hexan-2-one, 1-bromopropane, 2-chloropropane, triethylamine, hex-1-yne, pent-1-ene, hexan-1-ol, cyclohexanone, benzaldehyde) and each carries clean, accurate structural alt text.
- The question bank is visually rich and varied â clickable IR spectrum peaks, molecular-vibration animations, an evidence-board comparison, and categorize/rank tasks â giving the assessment layer strong spatial and comparison affordances.
- The deferred spring-model video was correctly hidden (is_hidden, empty url) rather than shipped broken, and its production note honestly states the reader carries the same content in prose, so there is no distracting or dead visual in the reader.
- Figures are purposeful, not decorative: every molecule asset maps to a specific example the prose discusses, so there is nothing redundant to remove.

**Findings:**

- **`visual-001`** [high / visual-opportunity] (section_id=nugget-ms-basics, concept_slug=mass-spectrometry-basics, anchor_text=the result is drawn as a bar graph of relative abundance versus m/z)
 - Observation: The mass-spectrometry sections describe a bar-graph spectrum in detail â the m/z axis, the base peak scaled to 100%, the molecular ion, and the fragmentation pattern below it â but the reader never shows an example mass spectrum. The only figures in these three sections are plain 2D structures of the sample molecules (propane, hexane, hexan-2-one, the halides, triethylamine).
 - Learner impact: A learner who relies on seeing a relationship must build the entire mental picture of a mass spectrum â bar heights, base peak, molecular-ion position, spacing between peaks â from prose alone, on the first technique of the chapter. The abstraction the whole section turns on is never modeled visually.
 - Evidence: nugget-ms-basics prose: 'a bar graph of relative abundance versus m/z ... the tallest peak, called the base peak, is assigned a relative abundance of 100%.' Section blocks contain only text, a molecule (blk-bs7icvzp, propane), and a Wikipedia link â no spectrum.
 - Recommended outcome: The reader needs at least one worked example mass spectrum shown as an annotated bar graph (m/z axis, base peak, molecular ion) so the core object the section describes is visible, not only narrated.
 - Confidence: 0.9
- **`visual-002`** [high / visual-opportunity] (section_id=nugget-ir-regions, concept_slug=characteristic-ir-absorptions, anchor_text=The spectrum is therefore read against a four-region map rather than band by band.)
 - Observation: The IR content is built around an explicitly named 'four-region map' of the wavenumber axis and repeatedly leans on band shape (broad rounded OâH vs sharp NâH vs sharp â¡CâH spike) and relative intensity, yet the reader shows no IR spectrum and no labeled four-region diagram. The IR sections again show only plain molecule structures (hex-1-yne, pent-1-ene, hexan-1-ol, cyclohexanone, benzaldehyde).
 - Learner impact: The map metaphor and the shape cues (broad vs sharp, strong vs weak) are inherently spatial and cannot be conveyed by a structure drawing or by prose as efficiently as by a single annotated axis. A visual learner has to reconstruct the whole spectral landscape mentally while also learning the chemistry.
 - Evidence: nugget-ir-regions and nugget-ir-basics prose describe the 4000â2500 / 2500â2000 / 2000â1500 / <1500 cmâ»Â¹ regions and band shapes; the deferred video brief (video-bond-vibrations) storyboard itself ends 'Close on the four-region map with each region labeled by its bond type,' confirming the authors see the map as a figure â but that video is production_status 'deferred' and its reader block (blk-ifheb72h) is is_hidden with an empty url.
 - Recommended outcome: The reader needs a persistent, static, labeled visual of the wavenumber axis divided into its four regions with a representative band in each (and at least one real annotated IR trace showing broad OâH vs sharp spike vs strong C=O), independent of whether the deferred spring-model animation is ever produced.
 - Confidence: 0.9
- **`visual-003`** [high / figure-purpose] (asset_id=mol-1-bromopropane, section_id=nugget-isotopes, anchor_text=Tie the equal-intensity Mâº/M+2 doublet at m/z 122 and 124)
 - Observation: The molecule assets state spectral learning goals but render only the bare structure, so the figure does not teach the point it claims. mol-1-bromopropane's goal is to 'Tie the equal-intensity Mâº/M+2 doublet ... to the near-equal abundances of â·â¹Br and â¸Â¹Br,' yet the figure (and its alt text) shows only a three-carbon chain with a bromine â no doublet. The same mismatch runs through mol-propane ('Mâº at m/z 44'), mol-hexane ('m/z 57, 43, 29 fragment series'), mol-2-hexanone ('alpha cleavage m/z 43 and McLafferty m/z 58'), and mol-cyclohexanone ('carbonyl absorption near 1715 cmâ»Â¹').
 - Learner impact: The figure's instructional purpose and its actual content diverge: a learner sees a generic structure while the caption asserts a spectral signature that is nowhere depicted. The structure is necessary but not sufficient, and the promised relationship stays invisible.
 - Evidence: Asset learning_goal fields vs. accessibility.alt_text fields, e.g. mol-1-bromopropane learning_goal 'equal-intensity Mâº/M+2 doublet at m/z 122 and 124' but alt_text 'a three-carbon chain with a bromine atom on the terminal carbon'; mol-hexane goal 'm/z 57, 43, and 29 fragment series' but alt_text 'an unbranched six-carbon chain drawn as a zigzag skeleton.'
 - Recommended outcome: Each asset that promises a spectral signature needs its figure to actually show that signature (e.g., the isotope doublet, the fragment ladder, the diagnostic band) alongside the structure, or the learning goal should be scoped to what the structure alone can teach.
 - Confidence: 0.85
- **`visual-004`** [medium / visual-opportunity] (section_id=nugget-isotopes, concept_slug=isotopes-and-molecular-formulas, asset_id=mol-2-chloropropane, anchor_text=An equal doublet or a 3:1 pair separated by two mass units is therefore read at a glance)
 - Observation: The chlorine 3:1 vs bromine 1:1 isotope patterns are pure relative-height comparisons that the prose itself says are 'read at a glance,' but the reader presents them only as text next to plain structures.
 - Learner impact: A side-by-side of a 3:1 pair and a 1:1 doublet makes the discrimination instant and durable; without it, the learner memorizes ratios verbally rather than recognizing shapes, which is exactly the skill the exam-style questions (ch12-halogen-isotope-id) later require.
 - Evidence: nugget-isotopes prose contrasts 'Â³âµCl and Â³â·Cl in very nearly a 3:1 ratio' with 'â·â¹Br and â¸Â¹Br ... an unmistakable 1:1 doublet ... at m/z 122 and 124'; the section's figures are only mol-2-chloropropane and mol-1-bromopropane structures.
 - Recommended outcome: The section needs a small visual comparison of the two isotope-cluster shapes (3:1 vs 1:1, two mass units apart) so the 'at a glance' recognition the prose promises is actually available on the page.
 - Confidence: 0.82
- **`visual-005`** [medium / visual-opportunity] (section_id=nugget-fragmentation, concept_slug=fragmentation-patterns, asset_id=mol-2-hexanone, anchor_text=Carbonyl compounds break the bond between the carbonyl carbon and the adjacent alpha carbon)
 - Observation: Fragmentation, alpha cleavage, and the McLafferty rearrangement are transformations â a specific bond breaks and the charge lands on a specific carbon â but the figures are undecorated structures with no indication of the cleavage site, the fragment produced, or where the charge goes.
 - Learner impact: The spatial logic ('the bond that breaks is the one that produces the more stable carbocation') is what a visual learner most needs to see. An annotated structure showing the cleaved bond, the departing neutral, and the charged fragment would replace a dense paragraph; the plain structure forces the learner to hold the whole transformation in their head.
 - Evidence: nugget-fragmentation expanded text describes hexane giving m/z 57/43/29, neopentane losing methyl to a tert-butyl cation, and hexan-2-one alpha cleavage (m/z 43) and McLafferty (m/z 58); assets mol-hexane and mol-2-hexanone are shown without any cleavage annotation.
 - Recommended outcome: The fragmentation section needs an annotated structure (or short static sequence) that marks the cleaved bond and the resulting charged fragment for at least one worked example, making the 'charge rests on the more substituted carbon' rule visible.
 - Confidence: 0.8
- **`visual-006`** [medium / visual-opportunity] (concept_slug=structure-determination-strategy, question_slug=ch12-click-oh-band, anchor_text=Click the band produced by the OâH stretch)
 - Observation: The visual infrastructure the reader lacks already exists in the question bank: spectrum_peaks items carry real IR peak coordinates and an invert-x/invert-y trace, and molecular_vibration items reference vibration animation JSON. But a learner encounters these spectra and animations only inside graded questions, and none are demo_eligible (demo_eligible count is 0), so no spectrum is ever shown as a worked or annotated example first.
 - Learner impact: Learners are asked to click the OâH or C=O band on a spectrum they have never been shown how to read in the reader. The first spectrum a visual learner sees is one they are being graded on, which raises anxiety and load rather than building recognition.
 - Evidence: question-set.json includes ch12-click-oh-band / ch12-click-oh-band-v2 (full IR peak data) and ch12-vibration-frequency-range / -v2 (asset_url /assets/vibrations/*.json); counts.demo_eligible = 0; the compiled reader sections contain no spectrum or vibration block (blk-ifheb72h video is is_hidden).
 - Recommended outcome: The same spectrum and vibration visuals used in assessment should also appear in the reader as an annotated worked example before students are tested on reading them.
 - Confidence: 0.78
- **`visual-007`** [low / alt-text-quality] (asset_id=mol-hexane, section_id=nugget-fragmentation, anchor_text=Hexane: an unbranched six-carbon chain drawn as a zigzag skeleton.)
 - Observation: Molecule alt texts accurately describe the structure drawn but omit the spectral feature that is the figure's stated teaching point, so a learner who depends on the description gets the connectivity but not the concept the asset was placed to convey. This overlaps the Accessibility persona.
 - Learner impact: For anyone relying on the text description in place of the image, the pedagogical payload (why this molecule is here â its fragment ladder, isotope pattern, or diagnostic band) is missing.
 - Evidence: mol-hexane alt_text 'an unbranched six-carbon chain drawn as a zigzag skeleton' vs learning_goal about the 'm/z 57, 43, and 29 fragment series'; parallel gap in mol-propane, mol-cyclohexanone, mol-1-bromopropane.
 - Recommended outcome: If these figures are upgraded to show spectral signatures (see visual-003), the descriptions must convey that signature; if they remain structures, the caption/description should still state the spectral point in words so the figure earns its placement.
 - Confidence: 0.7

**Open questions:**
- Are the molecule blocks in the reader intended to later be replaced or augmented by actual spectrum figures (bar-graph MS, IR trace, four-region map), given that the assets' learning goals are all spectral? Clarifying this determines whether visual-001/002/003 are one intervention or several.
- Is the four-region-map visual meant to be delivered by the deferred video-bond-vibrations, and if that video stays deferred, is a static map figure planned as its replacement in the reader?

### Orchestrator integrity findings

- **`orch-001`** [high / conceptual-support] (section_id=nugget-ms-basics, anchor_text=https://en.wikipedia.org/wiki/Electron-impact_ionization_and_the_molecular_ion) — All six compiled 'Background reading' external links are auto-derived from concept titles and point to nonexistent Wikipedia articles (e.g. A_four-region_map_locates_functional_groups). The package sets no wikipedia_title on any concept; structure-and-bonding demonstrates the working pattern (explicit wikipedia_title per concept). → Each concept needs a real, resolvable reference target for its background-reading link.
- **`orch-002`** [low / conceptual-support] (anchor_text=mcmurry-organic-openstax) — The reader builder emits an OpenStax/McMurry further-reading block only when textbook mappings contain id 'mcmurry-organic-openstax'; no package's mappings ever contain that id, so the block compiles for no chapter (verified against structure-and-bonding and overview-of-organic-reactions). Systemic compiler dead code, not specific to this chapter. → The compiler's OpenStax link lookup needs to key on an id the mapping pipeline actually produces (repo-level fix, out of chapter scope).
- **`orch-003`** [low / media-equivalence] (asset_id=video-bond-vibrations, anchor_text=Watching bonds vibrate: from spring model to IR spectrum) — The deferred video compiles into the reader as a video block with an empty url but is_hidden: true, so nothing broken renders; the deferral is recorded on the brief and the prose carries the content. → No change needed now; unhide only when a produced, described video exists.

### Orchestrator decisions (ranked recommendations)

- **`rec-001` Show actual spectra in the teaching sections** [high, figure] → **new-figure**
 - Need: The chapter teaches reading mass spectra and IR spectra, but the reader displays no spectrum, no fragment ladder, no isotope doublet, and no four-region map; band SHAPE and peak-pattern recognition are asserted in prose only, and the first spectrum a student meets is one they are graded on.
 - Rationale: A small set of STATIC annotated figures (one MS bar graph with M+, base peak and fragment ladder; one 3:1-vs-1:1 isotope doublet comparison; one annotated IR trace plus four-region map) fully addresses the need — animation or new interactives would be over-build. Not applied this pass: the topic-package pipeline's ALLOWED_ASSET_TYPES has no spectrum figure kind, so this requires registering one (teaching-asset-kind-registration; nmr_spectrum ChemTeachingAsset is precedent) — a product-level change outside chapter-content scope.
 - Consolidates: `struggle-001`, `struggle-002`, `visual-001`, `visual-002`, `visual-004`, `visual-005`, `visual-006`, `instr-003`, `instr-004`
- **`rec-002` Replace fabricated Wikipedia background-reading links** [high, prose] → **prose-edit**
 - Need: All six external links point to nonexistent articles auto-derived from concept titles; the only external scaffold is dead.
 - Rationale: Setting an explicit wikipedia_title per concept (the structure-and-bonding pattern) is a six-line metadata fix; every replacement target verified HTTP 200 before applying.
 - Consolidates: `orch-001`, `struggle-008`, `instr-006`
- **`rec-003` Make figure captions state facts the figure can support** [high, figure] → **prose-edit**
 - Need: Molecule captions are imperative authoring goals ('Anchor…', 'Tie the equal-intensity doublet…', 'Recognize the broad O–H band…') that promise spectral features the structure drawing does not display, sending students hunting for absent content.
 - Rationale: Rewriting each learning_goal as a declarative caption linking the shown structure to its spectral consequence fixes the mismatch without new assets; structural alt text stays untouched (it is an accessibility strength). If rec-001 later adds true spectrum figures, captions can point at them.
 - Consolidates: `visual-003`, `struggle-007`, `visual-007`
- **`rec-004` Verify interactive question-type operability (keyboard / screen reader / motion)** [high, interactive] → **instructor-note**
 - Need: spectrum_peaks band selection, the drag-family types (rank_order, matching_pairs, categorize_groups), and the evidence_board grid must be completable without a fine pointer and be announced with row/column context; the vibration animation should honor pause and reduced-motion. None of this is verifiable from authoring artifacts.
 - Rationale: These are properties of the RELEASED platform question-type components used product-wide, not of this chapter's content; the correct action is a targeted UI verification pass against the live components (Accessibility persona confidence was 0.55–0.6 for exactly this reason), not chapter edits. Logged as verification tasks; if verification fails, it becomes a platform fix benefiting every chapter.
 - Consolidates: `access-001`, `access-002`, `access-003`, `access-004`
- **`rec-005` Surface per-section practice checks in the reader** [high, practice] → **alternate-activity**
 - Need: Every nugget has an authored practice_check, but the reader compiles none of them, so a student reads six dense sections with no inline checkpoint; the 22-item bank lives entirely outside the reading flow.
 - Rationale: The content already exists — the fix is the reader builder emitting the authored practice_check as an end-of-section checkpoint block. That is a compiler change benefiting all chapters (out of chapter-content scope this pass); authoring new inline questions per-chapter would duplicate existing content.
 - Consolidates: `struggle-003`
- **`rec-006` Complete the capstone worked example's skipped steps** [medium, prose] → **prose-edit**
 - Need: The strategy worked example uses 'degree of unsaturation' without defining it and jumps from m/z 72 to C₄H₈O without showing how a nominal mass becomes a candidate formula — the two steps a struggling student cannot reproduce.
 - Rationale: Two short in-place additions (a parenthetical definition; one subtraction sentence deriving C₄H₈O) close the gap without restructuring; applied this pass.
 - Consolidates: `struggle-004`, `struggle-005`
- **`rec-007` Record the strategy concept's real prerequisite** [medium, prose] → **prose-edit**
 - Need: structure-determination-strategy leans on the nitrogen rule, halogen M+2 signatures, and the M+1 carbon count but does not list isotopes-and-molecular-formulas as a prerequisite, so declared sequencing diverges from what the prose assumes.
 - Rationale: One-line metadata fix to the prerequisite list; applied this pass.
 - Consolidates: `instr-001`
- **`rec-008` Assess the untested stated objectives (nitrogen rule, M+1 count, alpha cleavage)** [medium, assessment] → **added-practice**
 - Need: Three headline objectives are taught but never assessed: applying the nitrogen rule, estimating carbon count from M+1, and recognizing alpha cleavage/acylium formation.
 - Rationale: Needs 2–3 new bank items plus variants — a deliberate question-authoring pass, not a silent scope expansion during corrections; deferred to a follow-up authoring session against the same concepts.
 - Consolidates: `instr-002`, `instr-005`
- **`rec-009` Signpost McLafferty as recognition-level enrichment** [medium, prose] → **prose-edit**
 - Need: The fragmentation section's final paragraph stacks alpha cleavage, acylium resonance, and the full McLafferty mechanism in rapid succession; McLafferty is not in the learning objectives yet is presented at mechanism depth.
 - Rationale: A one-sentence signpost demoting the mechanism to recognition level (its even-mass calling card) relieves the overload without deleting correct chemistry; applied this pass.
 - Consolidates: `struggle-006`
- **`rec-010` State the C≡C stretch value consistently** [low, prose] → **prose-edit**
 - Need: nugget-ir-basics body says 'near 2100 cm⁻¹' while its own practice check, the asset captions, and nugget-ir-regions say 'near 2120 cm⁻¹'.
 - Rationale: Standardize on 2120 cm⁻¹ (matches hex-1-yne and every other occurrence); applied this pass.
 - Consolidates: `struggle-009`
- **`rec-011` Fix the never-firing OpenStax further-reading block** [low, instructor-support] → **instructor-note**
 - Need: The reader builder's McMurry/OpenStax link block keys on textbook id 'mcmurry-organic-openstax', which no package's mappings produce, so the block compiles for no chapter.
 - Rationale: Repo-level compiler fix affecting all chapters; out of scope for a chapter correction pass, recorded for the pipeline backlog.
 - Consolidates: `orch-002`

### Merged duplicates

- Missing spectra in the reader: `struggle-001`/`struggle-002` (Struggling Student, high), `visual-001`/`visual-002`/`visual-004`/`visual-005`/`visual-006` (Visual Preference, high/medium), `instr-003`/`instr-004` (Instructor, medium/low) → `rec-001`, kept at **high**; all three learner impacts retained (mental-model failure, spatial-recognition failure, shape-cue loss).
- Fabricated Wikipedia links: `orch-001` (orchestrator, high), `struggle-008` (medium), `instr-006` (low) → `rec-002`, kept at **high** (a dead scaffold on every section).
- Caption/figure mismatch: `visual-003` (high), `struggle-007` (low), `visual-007` (low) → `rec-003`, kept at **high**; alt-text left structural by design.

### Retained disagreements

- **Is the absence of spectra an accessibility strength or a pedagogy gap?**
 - Accessibility Persona: "Strength: 'the reader contains no visual-only mass spectrum or IR trace that lacks a text equivalent' — all spectral information is carried in prose and text form."
 - Learner with Visual Preference: "High-severity gap: 'this is a chapter whose entire subject is reading spectra, and the compiled reader never shows a single spectrum.'"
 - **Resolution:** Both are true and compatible: text-first parity is genuinely strong and must be preserved, and the missing visual modeling is still a real instructional gap. rec-001 therefore requires any added spectrum figure to ship with a structured description of equal information content, keeping the accessibility property while closing the visual one.
- **Overall readiness impression**
 - Organic Chemistry Instructor: "'Go, with minor revisions' at 8.0 — chemistry uniformly correct."
 - Struggling Student: "5.5 — 'several concrete places I would reread, guess, or quit.'"
 - **Resolution:** Chemical accuracy is necessary but not sufficient. Readiness is computed from the consensus high-severity findings (three personas independently flagged the missing-spectrum gap), so the verdict is 'major revision' despite zero chemistry errors and zero blockers.

### Places where a description is sufficient (no new asset)

- Deferred bond-vibration video: hidden block + prose coverage + molecular_vibration questions already carry the animated equivalent; no placeholder or transcript work needed until production (orch-003).
- Molecule alt texts: structural descriptions are correct and should NOT be rewritten to include spectral claims — captions (rec-003) carry the spectral point instead.
- molecular_vibration questions: prompt names the bond and the accessible description narrates the motion, so the animation is redundant rather than sole carrier of meaning; only pause/reduced-motion verification remains (folded into rec-004).
- All 22 question accessible_descriptions: task-conveying and leak-free; no changes needed.

### Regression targets for next run

`struggle-001`, `struggle-002`, `struggle-003`, `visual-001`, `visual-002`, `visual-003`, `instr-002`, `instr-005`, `access-001`, `access-002`, `access-003`, `orch-001`, `orch-002` — plus confirmation that applied corrections (rec-002/003/006/007/009/010) hold after recompile.

---
## Post-correction record

**Estimated state: major revision (not a second persona verdict).** All bounded verified errors are corrected; the headline item — no spectrum shown in a spectrum-reading chapter (`rec-001`) — needs a new pipeline figure kind and remains open.

### Changes applied
- Explicit `wikipedia_title` on all six concepts; all six replacement articles verified HTTP 200; compiled links now resolve — resolves `orch-001`, `struggle-008`, `instr-006`
- `isotopes-and-molecular-formulas` added to the strategy concept's prerequisites — resolves `instr-001`
- C≡C stretch standardized to 2120 cm⁻¹ in all three inconsistent spots — resolves `struggle-009`
- Degree of unsaturation defined in place (both tiers) and the mass→formula subtraction step (72 − 16 = 56 → C₄H₈) shown in the worked example — resolves `struggle-004`, `struggle-005`
- McLafferty signposted as recognition-level in the expanded tier — resolves `struggle-006`
- All eleven figure captions rewritten as declarative structure-to-spectrum statements; structural alt text intentionally unchanged — resolves `visual-003`, `struggle-007`; partially addresses `visual-007`
- Compile side-effect repaired: restored `alkynes-organic-synthesis` and `overview-of-organic-reactions` entries the compiler clobbered from `topic-package-textbook-profiles.json` (runtime `textbook_profiles.json` verified addition-only)

### Verification
- `compile_topic_package … --write-runtime` — clean, zero validation errors, 22 questions (11 surfaced + 11 staged variants)
- `pytest tools/topic_packages/tests/ -q` — 50 passed
- backend `pytest` (accessibility leaks, wrong-answer explanations, numeric grading) — 142 passed
- curl on all six replacement Wikipedia URLs — 200 each

### Still recommended
- `rec-001` spectrum figures (needs a spectrum asset kind in the topic-package pipeline; static annotated figures suffice)
- `rec-004` operability verification of the interactive question types against live components
- `rec-005` compile `practice_check` into the reader as end-of-section checkpoints (compiler change)
- `rec-008` assessment for the nitrogen rule, M+1 carbon count, and alpha cleavage
- `rec-011` fix the never-firing OpenStax further-reading block (compiler dead code, all chapters)

---
## Follow-up session record (2026-07-25, same day)

- **rec-004 resolved by verification**: all flagged interactive types are keyboard/SR-operable at the component level — spectrum_peaks peaks are native buttons (aria-pressed, focus-visible); matching/categorize use native selects (no drag); rank_order card sort has per-card up/down buttons + aria-live (drag is optional); evidence_board is a labeled table of per-cell selects with row+column context in each aria-label; VibrationViewer honors prefers-reduced-motion with explicit play/pause. Renderer tests 10/10.
- **rec-011 fixed**: builder now matches real mapping ids + the chapters[] shape; OpenStax link emits once (first section); ch12 verified. (The previously working links were catalog bridge-prose links — a different surface.)
- **rec-008 partially applied**: nitrogen-rule and M+1 carbon-count questions added (+staged variants) → 26 questions; alpha cleavage still unassessed.
- **Seeded to prod** (owner 52): concept maps upserted (with a new first-wins dedupe fixing the pre-existing curved-arrow-notation collision between the acids-bases and overview packages); question sets created 13 + 13 staged; rerun idempotent (all unchanged).
