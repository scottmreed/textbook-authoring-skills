# Coherence pass — alkyl-halide-substitution-and-elimination
Date: 2026-07-24

Single pass, run after concepts, nuggets, assets, video briefs, and question
sets were drafted and after a clean dry compile (0 validation errors,
`verification_required: []`). Walked later-authored → earlier-authored.

## Questions → text/figures
- Every one of the 14 surfaced questions tests something the prose teaches at
 the depth asked. The SN2-kinetics `numeric` question is grounded by the
 explicit second-order rate law in `nugget-sn2-mechanism`; the SN1
 `reaction_coordinate_reasoning` question maps directly onto the two-step,
 ionization-rate-determining picture in `nugget-sn1-mechanism`; the E2
 `hotspot` (Zaitsev vs Hofmann β-hydrogen) is fully prepared by the Zaitsev/
 Hofmann discussion in `nugget-e2`. No question required a step the text
 hand-waved, so no nugget was softened to fit a question.
- No new figure was needed: every question that shows structures uses inline
 option/stimulus SMILES (single_select, structure_scaffold, synthesis_route,
 hotspot, curved_arrow) rather than a chapter figure, so the molecule assets
 were not stretched to cover them.

## Questions → deck/reader
- Each question type has upstream preparation. The `curved_arrow` SN2 question
 is preceded by the backside-attack mechanism nugget; the `comparison_matrix`
 SN2-vs-SN1 and E2-vs-E1 grids are the tabular form of the overview nugget and
 the four mechanism nuggets; the `predicting` questions are the worked form of
 `nugget-predicting`. No question type is orphaned from the prose.

## Videos → text
- The three briefs (SN2 inversion, SN1 racemization, E2 anti-periplanar/Zaitsev)
 each dramatize a spatial/temporal idea the prose can only state — umbrella
 inversion, capture from both faces of a planar cation, and the anti coplanar
 alignment. None duplicates a paragraph that already stands alone; they are
 complementary, not redundant. Video *generation* is deferred (see Deferred);
 the briefs are authored and queued `needs_review`.

## Figures → text/questions
- All 15 molecule assets are cited by a nugget (checked: every asset id appears
 in some `nugget.asset_ids`). No orphan assets. The inversion pair
 (`mol-S-2-bromobutane` → `mol-R-2-butanol`) carries the one spatial idea a
 line drawing must show; the substrate series (methyl/1°/2°/3° bromides) carries
 the steric-access argument that words alone rank poorly.
- No nugget describes a spatial idea that lacks a figure: the SN1 planar cation
 has `mol-tert-butyl-cation`; the two elimination regiochemical products have
 `mol-but-2-ene` and `mol-but-1-ene`.

## Concepts → whole package
- All 8 concepts have a nugget, at least one figure, and at least one question
 (coverage: overview→comparison_matrix; sn2-mechanism→short_answer/numeric/
 curved_arrow; sn2-reactivity→rank_order/structure_scaffold; sn1-mechanism→
 reaction_coordinate_reasoning; sn1-reactivity→single_select; e2→hotspot;
 e1→error_repair; predicting→multi_select/categorize/matching/synthesis). No
 concept node is left without an evidence path.
- No question or figure has a subject without a concept node; the four
 mechanisms, their reactivity factors, and the prediction grid each map to a node.

## Crosswalks
- Concept list did not change during this pass, so the crosswalks stand. All 13
 catalogued books carry an explicit override; the compiled
 `textbook-mappings.json` was checked book-by-book and every entry points at the
 correct substitution/elimination chapter(s) (spans flagged for Klein, Smith,
 Loudon, Clayden, Bruice; one-to-one for the McMurry family, OpenStax, Wade,
 Brown/Foote, Forsey). No generic-term mis-match was left in place.

## Deferred (not applied this pass)
- Video generation: three briefs authored and queued `needs_review`; actual
 mp4/gif rendering via `molecule-video-creator` is deferred to conserve
 generation budget. Recorded here rather than dropping the briefs.
- Seeding (`concept-map seeder (proprietary toolchain, not in this repo)` / `question-bank seeder (proprietary toolchain, not in this repo)`): not run — requires
 a live production database, and the skill forbids production seeding
 without explicit permission.
- Science-review sign-off: assets/videos begin `not_reviewed`/`needs_review`;
 human sign-off in the Science Review Queue is pending.

## Deletions (what + why)
- None. Nothing was removed in this pass; every drafted concept, nugget, asset,
 brief, and question survived with a live reference.
