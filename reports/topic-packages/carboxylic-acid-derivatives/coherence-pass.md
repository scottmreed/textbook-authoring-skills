# Coherence pass — carboxylic-acid-derivatives
Date: 2026-07-29

One pass, run after concepts, nuggets, figures, video briefs and question sets were
drafted and before the runtime compile. Chapter 21 (McMurry/OpenStax numbering),
reader slug and deck slug `carboxylic-acid-derivatives`.

## Questions → text/figures

- **Changed — `nugget-spectroscopy-acyl-derivatives`.** `ch21-ir-identify-derivative-v2`
 asks the student to use *two* bands between 3200 and 3400 cm⁻¹ to pick a primary
 amide over a tertiary one, but the prose only said that primary and secondary
 amides absorb in that region at all. The expanded tier now states the band count
 for each of the three amide classes, so the discrimination the question requires is
 taught rather than assumed.
- **Changed — `nugget-addition-elimination`.** `ch21-addition-elimination-arrow` and its
 variant ask for the arrow of the addition step, and the deferred video brief was the
 only place the arrows were described concretely. The expanded tier now names the
 origin and destination of each arrow in both steps, so the drawn answer has a worked
 precedent in the chapter text.
- **No change, and the reason:** every other question's chemistry is developed at the
 depth asked. Spot-checked the ones that reach furthest — `ch21-anhydride-acetylation-v2`
 (cyclic anhydride, covered in `nugget-anhydride-reactions` third paragraph),
 `ch21-amide-hydrolysis-conditions-v2` (the N,N-dimethylformamide coalescence
 experiment, covered in `nugget-amide-reactions` first paragraph),
 `ch21-thioester-vs-ester-v2` (acyl adenylates, covered in
 `nugget-biological-acyl-transfer` third paragraph), and
 `ch21-grignard-equivalents-v2` (three equivalents of base for a triester, which
 follows from the stoichiometry argument already made in `nugget-ester-hydrolysis`).
- No question requires a figure that does not exist. See "Deferred" for the one
 figure that would improve a question rather than enable it.

## Questions → deck/reader

- The compile emits 46 slides from the eleven nuggets, and every question type used
 has a worked precedent upstream: `curved_arrow` now has the arrow-level description
 added above plus `mol-tetrahedral-intermediate`; `rank_order` has the whole of
 `nugget-reactivity-ladder`; `synthesis_route` has `roadmap-acid-to-amide`, which is
 the same activation-then-acylation sequence the question asks the student to
 assemble; `reaction_coordinate_reasoning` has `rc-addition-elimination`;
 `bond_change_ledger` has the elimination-step description in the mechanism nugget.
- This is a full package, not a shim over a legacy deck, so no frozen-deck escalation
 was needed.

## Videos → text

- All three briefs (`video-addition-elimination`, `video-reactivity-ladder`,
 `video-saponification`) are recorded as `production_status: deferred` — each is an
 electron-flow or electron-density animation that the molecule-video-creator chalk
 pipeline cannot produce, the same deferral class as the mechanism briefs in
 chapters 12–20. Because nothing was produced, no prose was trimmed as redundant:
 the reader still has to carry this content, and each deferral note names the nugget
 and figures that do so.

## Figures → text/questions

- No orphans: all 23 assets are cited by at least one nugget or video brief, checked
 mechanically against `asset_ids` and `visual_asset_ids`.
- No nugget describes a spatial or energetic idea in words that a missing figure
 should carry. The two candidates were checked: the tetrahedral intermediate has
 `mol-tetrahedral-intermediate`, and the two-step energy story has
 `rc-addition-elimination`.
- `rc-addition-elimination` is the only reaction coordinate diagram in the chapter and
 is retained deliberately under the 2026-07-23 reviewer rule: it is a two-step profile
 whose *shape* is the lesson (a shallow intermediate well between two low barriers),
 the same exemption the rule grants SN1. No energy diagram was authored for any of the
 multistep interconversions, which are carried in prose and molecule figures instead.

## Concepts → whole package

- All ten concepts have a nugget, at least one asset, and at least one surfaced
 question; verified mechanically. Nothing was added or removed.
- No question or figure has a subject without a concept node. The closest case is
 step-growth polymerization, which is a section of McMurry chapter 21 rather than a
 reaction of a single derivative; it has its own concept node
 (`step-growth-polymers`) with two questions and four figures.

## Crosswalks

- The concept list did not change during this pass, so the mappings authored against
 it still stand. Re-checked the two that the pass could have invalidated: the
 polymer concept is why Wade, Smith, Loudon, Brown/Foote/Iverson/Anslyn and Clayden
 each carry a **second** mapped chapter (their synthetic-polymer chapters), which
 would have been wrong to omit had that concept been dropped.
- All 13 catalogued books have an explicit override. `bruice-essential-organic-chemistry`
 is mapped to an empty chapter list with a FLAG note, because the catalogued list for
 that title stops at chapter 16 and contains no carbonyl chapters.

## Deferred (not applied this pass)

- An `ir_spectrum` figure for `ch21-ir-identify-derivative` would let the student read
 the anhydride's two carbonyl bands off a trace instead of from a prose summary. The
 question is answerable as written (all four options carry structures and the band
 positions are given in the prompt), so this is an improvement rather than a gap.
- A `mechanism_path` question for the addition–elimination sequence would exercise the
 whole mechanism rather than one arrow, but the chapter already covers that ground
 with `curved_arrow`, `bond_change_ledger`, and `reaction_coordinate_reasoning`.
- Producing the three deferred video briefs requires an animation pipeline that does
 not exist yet; the briefs stay in the package rather than being dropped.

## Deletions (what + why)

- None. Nothing authored in steps 2–5 turned out to be redundant or unreferenced.
