# Coherence pass — mass-spectrometry-and-infrared-spectroscopy
Date: 2026-07-25

## Questions → text/figures
- Verified every surfaced question tests prose the chapter teaches at the asked depth:
 neopentane/tert-butyl base peak, the M−15/18/29/43 neutral-loss table, the Br 1:1 and
 Cl 3:1 isotope ratios, the bond-order/atomic-mass frequency trends, the four-region
 map, alcohol vs ketone band contrast, and the butan-2-one worked unknown all appear
 explicitly in nugget text before any question asks them. No question was softened and
 no nugget needed deepening.
- Staged variant `ch12-rank-stretch-frequencies-v2` uses the aldehyde C–H (2720/2820 cm⁻¹)
 anomaly, which is taught in `nugget-ir-regions` (a different concept's nugget) rather
 than in `nugget-ir-basics`. No change: variants serve as remediation after the chapter
 is read in full, the feedback bundle itself teaches the anomaly, and duplicating the
 aldehyde discussion into the basics nugget would create redundant prose.

## Questions → deck/reader
- Every question type used has an upstream worked example or explicit teaching:
 numeric m/z ← propane practice_check; fragmentation single_select ← neopentane
 paragraph; matching ← neutral-loss list; categorize ← four-region map; rank ←
 stiffness/mass trends; spectrum_peaks ← hexan-1-ol vs cyclohexanone band contrast in
 `nugget-ir-regions`; evidence_board ← the butan-2-one worked example in
 `nugget-strategy`. No missing-slide gaps; this is a full package, so deck slides are
 compiled from the same nuggets.

## Videos → text
- One brief (`video-bond-vibrations`), production deferred (recorded on the brief).
 Its storyboard parallels `nugget-ir-basics` deliberately — the animation is the motion
 version of the spring-model prose, not a redundancy. No trim needed.

## Figures → text/questions
- No orphan assets: all 11 molecules are cited by at least one nugget, and
 `mol-2-hexanone` / `mol-hexan-1-ol` are shared into `nugget-strategy` so the capstone
 section has figures. Tiny-molecule rule applied (`show_hydrogens` on propane); larger
 chains render clearly without it.
- No energy diagrams authored (reviewer rule: none needed — no reaction energetics in
 this chapter).

## Concepts → whole package
- All six concepts have a nugget, at least one figure, and at least one surfaced
 question (counts: ms-basics 1, fragmentation 2, isotopes 1, ir-basics 2,
 characteristic-ir 3, strategy 2). No evidence-path gaps for mastery gating; no
 concept added or removed.

## Crosswalks
- All 13 catalogued books carry explicit overrides taken verbatim from
 `backend/app/data/textbook_catalog.json` chapter lists (verified numbers: McMurry 12,
 OpenStax 12, Klein 15, Wade 12, Smith 12A+12B, Loudon 14, Brown/Foote 12, Clayden 12,
 Forsey 13, Bruice 14). Combined chapters (Clayden ¹³C NMR, Forsey NMR, Bruice UV/Vis)
 carry notes scoping the match to the MS/IR portion.

## Deferred (not applied this pass)
- Video production for `video-bond-vibrations`: the spring-model scene is not producible
 by the molecule-video-creator chalk pipeline; needs a bespoke animated scene.
 Deferral recorded on the brief (`production_status: deferred`).
- Seeding (`concept-map seeder (proprietary toolchain, not in this repo)` / `question-bank seeder (proprietary toolchain, not in this repo)`) — deliberately not run:
 Supabase writes require maintainer approval.

## Deletions (what + why)
- None.
