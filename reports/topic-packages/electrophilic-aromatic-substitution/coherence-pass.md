# Coherence pass — electrophilic-aromatic-substitution
Date: 2026-07-28

## Questions → text/figures
- **Change:** `ch16-eas-profile-reading` (and its variant) asks for transition-state
 character (early/late), which the prose never taught. Added a Hammond-postulate
 sentence to `nugget-eas-mechanism` (expanded tier) rather than dropping the ask.
- **Change:** `ch16-xylene-nitration-isomers` (and variant) rely on
 symmetry-equivalence counting that `nugget-polysubstituted-synthesis` implied but
 never stated. Added an explicit sentence (expanded tier) covering the p-xylene = 1
 / o-xylene = 2 counting logic.
- No change otherwise: every remaining question maps to prose that teaches it at the
 asked depth (checked question-by-question against the eight nuggets), and every
 question that needs a structure carries `structure_smiles` / `molecule_smiles` /
 a profile inline.

## Questions → deck/reader
- No change: each question type used has an upstream worked example — the mechanism
 nuggets carry the arenium/rearomatization walkthrough (prepares `bond_change_ledger`,
 `hotspot`, `reaction_coordinate_reasoning`), nugget 4's practice check is itself a
 reactivity ranking (prepares `rank_order`), nugget 6's practice check is an
 order-of-steps synthesis (prepares `synthesis_route`), and nugget 5 walks the
 resonance-form comparison (prepares `structured_reasoning` and `error_repair`).
- `curved_arrow` was deliberately not used: the EAS attack step requires a bond-source
 arrow (frontend emits single-site endpoints; backend requires two sites for bond
 arrows) and the rearomatization step requires an implicit-H target — both are the
 recorded ch15 dead-ends. `bond_change_ledger` + `hotspot` carry the mechanism
 interaction instead.

## Videos → text
- No change: the single brief (`video-eas-two-step-mechanism`) intentionally overlaps
 `nugget-eas-mechanism` because production is deferred (chalk pipeline cannot draw a
 curved-arrow mechanism animation); the deferral note records that the reader prose
 and the `rc-eas-bromination-profile` figure carry the content meanwhile.

## Figures → text/questions
- No change: all 20 assets are cited by at least one nugget's `asset_ids` (verified
 exhaustively); no orphans. The lone reaction-coordinate figure is the two-step
 EAS profile whose shape is the lesson (the reviewer-approved class), not a
 multistep-addition diagram.

## Concepts → whole package
- No change: every concept has a nugget, at least one figure, and at least one
 surfaced question. Thinnest coverage: `nucleophilic-aromatic-substitution-and-benzyne`
 and `aromatic-side-chain-oxidation-and-reduction` each have one surfaced question
 (plus staged variants) — acceptable under the 1–2-per-suitable-type target, noted
 for the review pass.

## Crosswalks
- No change to concepts during this pass, so the 13 authored overrides stand.
 mcmurry-6e / openstax map to chapter 16 (verified). Flagged as needing TOC
 verification in their override notes: smith-7e (number/title), brown-foote-8e
 (number), forsey-oer (number/title), bruice-essential (number).

## Deferred (not applied this pass)
- Two staged variants test chemistry that pedagogically belongs to the NAS concept
 (`ch16-intermediate-name-v2` = benzyne; `ch16-arenium-pi-electrons-v2` =
 Meisenheimer π count) but carry the parent's `concept_slug`
 (`eas-mechanism-and-arenium-ion`) because the compiler requires variants to keep
 the parent concept. They are draft-only remediation items, so mastery mapping is
 unaffected; revisit only if variants are ever promoted to surfaced.
- Video production for `video-eas-two-step-mechanism` (bespoke animated scene;
 recorded in the brief's production_note).

## Deletions (what + why)
- None.
