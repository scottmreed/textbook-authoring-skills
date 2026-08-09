# Coherence pass — stereochemistry-at-tetrahedral-centers
Date: 2026-07-24

One pass, run after concepts, nuggets, assets, the video brief, and question sets were
drafted and before compiling. Walked later-authored categories back to earlier ones.

## Questions -> text/figures
- **Change made:** After drafting the question set, the `racemates-and-resolution` concept had a
 nugget and a figure but no question, while every other standard-depth concept carried one. Added
 a `single_select` (`ch5-resolve-racemate-method`) and its variant on the chiral-stationary-phase
 rationale, both fully supported by `nugget-racemates`, which already teaches diastereomeric-salt
 resolution and the transient-diastereomer basis of chiral chromatography. No prose change was
 needed; the nugget already carried the depth the question asks.
- **No change (confident):** Every other question tests something a nugget teaches at the depth
 asked — chirality identification (single_select, multi_select, categorize_groups), CIP priority
 and R/S reading (rank_order, short_answer), stereoisomer relationships and the 2^n/meso count
 (matching_pairs, numeric_with_units), enantiomer-vs-diastereomer physical properties
 (comparison_matrix), and configuration drawing (structure_scaffold, fischer). All stereo SMILES
 and R/S labels used in prompts, options, and answer keys were verified with RDKit
 (FindMolChiralCenters) before authoring.

## Questions -> deck/reader
- **No change:** Deck/reader slides are generated from the nuggets, and each question type has an
 upstream nugget that prepares it. Deliberately no `curved_arrow` or `reaction_coordinate_reasoning`
 type: this chapter has no mechanism and no energy profile (per the science-review lesson that
 multistep ionic profiles and diagram-dependent prompts are rejected). Structure/spatial reasoning
 is carried by `structure_scaffold` and `fischer`, both of which have worked support in
 `nugget-rs`.

## Videos -> text
- **No change:** The single video brief (`video-rs-assignment`) visualizes the R/S assignment
 procedure — ranking by CIP priority and reading the clockwise/counterclockwise sense with the
 lowest priority group pointed away — which is the one process in the chapter that materially
 benefits from motion. It complements rather than duplicates the prose. Video *production* is
 deferred (the brief compiles as a `needs_review` task in the video manifest); no brief was
 dropped silently.

## Figures -> text/questions
- **No change:** All 11 molecule assets are cited by at least one nugget or the video brief
 (verified: zero orphans). The achiral contrast (propan-2-ol), the R/S worked example
 (2-bromobutane), the enantiomer pair (2-butanol), the meso/diastereomer set (tartaric acid,
 3-bromobutan-2-ol), and the biological stereocenters (glyceraldehyde, alanine) each anchor a
 specific teaching point. Molecules that appear only inside question options (e.g. lactic acid,
 branched alkanes) are text/SMILES within the item and correctly do not need standalone figures.

## Concepts -> whole package
- **No change to structure; one gap accepted with reason:** All 6 concepts have a nugget (1:1) and
 at least one supporting figure (verified: zero concepts without a nugget or figure). Five of six
 also carry a question. `prochirality-and-chirality-in-nature` (the advanced concept) is carried by
 its nugget plus two figures without a dedicated question: prochirality/pro-R/pro-S and biological
 discrimination of enantiomers are treated as advanced reading rather than assessed items in an
 Organic I core set. It is not orphaned (nugget + figures present), so this is an accepted scoping
 decision, not a broken evidence path.

## Crosswalks
- **No change needed beyond authoring:** The final concept list (6) was fixed before crosswalks were
 written. Explicit overrides are supplied for all 13 catalogued books. McMurry 6e and OpenStax map
 1:1 to ch5 "Stereochemistry at Tetrahedral Centers"; Klein (ch5), Wade (ch5), Smith (ch5), and
 Forsey (ch5) map to their dedicated stereochemistry chapters; texts that place stereochemistry
 earlier or later (Brown ch3, Clayden ch14/16, the Fundamentals ch6, the sixth-edition Loudon ch6,
 Bruice ch4) are mapped to the closest single chapter with a note. Verified the compiled mapping
 resolves McMurry and OpenStax to ch5 at confidence 1.0 (explicit, not a generic term match). The
 three manifest books without a `catalog_id` (the default McMurry alias, the fifth-edition Loudon
 alias, and Soderberg OCBE) are not catalog-driven and receive no compiled lens, consistent with
 every other topic package.

## Deferred (not applied this pass)
- Video production for `video-rs-assignment` (brief authored and queued needs_review; the MP4/GIF
 render is a separate paid step).

## Deletions (what + why)
- None.

## Addendum (2026-07-24) — R/S priority-rotation arrow section
Added a second nugget to `r-s-configuration` ("The priority-rotation arrow: reading R and S
at a glance") with two figures (`mol-rs-arrow-r`, `mol-rs-arrow-s`) that overlay a curved arrow
tracing CIP priorities 1 -> 2 -> 3 on a flat 2-bromobutane skeleton. A new backend render knob
(`rdkit_options.priority_arrow`, in `[internal source reference — not in this repo]reader_chapter_builder`) and the deck/review
figure (`compiler._figure`), and the reader (`ReaderBlockRenderer`) forwards it to the shared
`/deck-creator/render/preview` renderer. Coherence: the new nugget deepens the R/S concept the
questions already assess (`rank_order`, `short_answer`, `structure_scaffold`, `fischer`); no
question or figure was orphaned. Both new figures are submitted needs_review with the rest.
