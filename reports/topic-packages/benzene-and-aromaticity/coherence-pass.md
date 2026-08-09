# Coherence pass — benzene-and-aromaticity
Date: 2026-07-27

Single bounded pass run after concepts, nuggets, figures, video briefs, and
question sets were drafted, and before the runtime compile. Every category is
answered; changes actually applied are marked **applied**.

## Questions → text/figures

- **Applied — added a figure.** `mol-cyclopropenyl-cation` (`[cH+]1cc1`) was
 added to `nugget-aromatic-ions`. The cyclopropenyl cation is argued about in
 the aromatic-ions prose and is used by three questions
 (`ch15-aromaticity-requirements` wrong-answer explanation,
 `ch15-classify-rings-v2`, `ch15-pi-electron-matching-v2`), but the chapter
 had no figure of it. Asset count 20 → 21.
- **Applied — prose wording.** `nugget-naming-benzenes` `practice_check.answer`
 had a comma splice; rewritten as one correctly punctuated sentence.
- No change: every other question tests something the prose teaches at the
 depth asked. Spot checks that motivated this conclusion —
 `ch15-fused-ring-stabilization-v2` (anthracene central-ring reactivity) is
 stated in `nugget-polycyclic-aromatics`; `ch15-ring-current-shift-v2`
 (interior hydrogens upfield) is stated in `nugget-aromatic-spectroscopy`;
 `ch15-aromatic-ir-band-v2` (para out-of-plane band at 812 cm⁻¹) sits inside
 the 810–840 cm⁻¹ range the same nugget gives; `ch15-classify-rings-v2`
 (cycloheptatrienyl anion antiaromatic) is stated in `nugget-aromatic-ions`;
 `ch15-acidity-ranking-v2` relies on the alkylamine-versus-pyridinium pKa
 comparison in `nugget-aromatic-heterocycles`.
- No change: two counts asked numerically (anthracene's 14 π electrons,
 cyclooctatetraene's 8 π molecular orbitals) are not stated verbatim in the
 prose, but the counting rule that produces them is stated explicitly in both
 `nugget-benzene-mos` and `nugget-polycyclic-aromatics`. Asking a student to
 apply a stated rule is the intended depth; the prose was not softened to
 pre-answer them.

## Questions → deck/reader

- No change. This is a full package, so the deck is compiled from the same
 nuggets and assets — every question type used has upstream prose in the same
 chapter. The two types most at risk of having no worked example upstream were
 checked individually: `hotspot` (locate the sp³ ring carbon) is set up by the
 explicit sp³-carbon discussion in `nugget-aromatic-ions`, and
 `spectrum_peaks` (read an IR band) is set up by the band table in
 `nugget-aromatic-spectroscopy`.

## Videos → text

- No change. The one brief, `video-benzene-mo-filling`, restates
 `nugget-benzene-mos` in animated form rather than adding content, which is
 the intended relationship; since the brief is recorded as deferred, no
 duplication reaches a learner. No prose was trimmed against a video that
 does not exist yet.

## Figures → text/questions

- No orphans. All 21 assets are cited by at least one nugget, and 13 of them
 additionally appear as question stimuli. Assets cited only by prose
 (`mol-phenol`, `mol-aniline`, `mol-imidazole`, `mol-phenanthrene`,
 `mol-adenine`) each carry a distinct teaching point in their section and
 were kept.
- No change: no nugget was found describing a spatial or energetic idea in
 words that an available figure kind could carry better. The one place that
 argument does apply — the π molecular-orbital ladder — has no renderable
 asset type (see Deferred).

## Concepts → whole package

- No change. All eight concepts have at least one nugget, at least one figure,
 and at least two questions, so every concept has an evidence path for
 mastery gating. Distribution of the 46 authored questions:
 `aromatic-ions` 10, `huckel-rule-and-antiaromaticity` 8,
 `naming-substituted-benzenes` 6, `spectroscopy-of-aromatic-compounds` 6,
 `benzene-structure-and-stability` 4, `molecular-orbitals-of-benzene` 4,
 `aromatic-heterocycles` 4, `polycyclic-aromatic-compounds` 4.
- No question or figure was found whose real subject lacked a concept node.

## Crosswalks

- No change needed. No concept was added or removed by this pass (the one
 addition was an asset), so the final concept list is the list the crosswalks
 were authored against. All 13 catalogued textbooks carry explicit
 `overrides`; the compile report's `verification_required` list is empty, so
 no mapping fell back to title-token matching.

## Deferred (not applied this pass)

- **No mechanism / curved-arrow question.** The chapter teaches structure and
 stability and contains no mechanism. The one arrow-pushing step it does teach
 — deprotonation of cyclopentadiene — needs a hydrogen atom as an arrow
 endpoint, and the `curved_arrow` workspace builds arrows by clicking heavy
 atoms rendered from `molecule_smiles`, where hydrogens are implicit. The
 resonance-arrow alternative needs a `bond` endpoint, which the click-based
 renderer also cannot produce (`[internal source reference — not in this repo]target: {kind: "atom"}`). Structure coverage is instead carried by four
 `structure_scaffold` questions and two `hotspot` questions.
- **No `peak_assignment` question.** Its grader (`CATEGORIZE_GRADER`) compares
 peak → atom id strings exactly, with no equivalence normalization. Every
 level-appropriate aromatic compound has symmetry-equivalent ring carbons, so
 a correct assignment would be ambiguous between two valid atom indices.
 Spectroscopy is covered by `spectrum_peaks`, `numeric_with_units`, and
 `single_select` instead. Making aromatic peak assignment authorable needs
 symmetry-aware grading — a platform change, not a chapter change.
- **No orbital-diagram figure for the π molecular-orbital ladder or the
 inscribed-polygon construction.** `orbital_overlay` is an allowed asset type
 but compiles to an image block with an empty URL
 (`reader_chapter_builder._asset_block`), so it renders blank until a file
 exists. The content is carried in `nugget-benzene-mos` prose. This is the
 same open visual-scaffolding item recorded for ch14's MO ladder.
- **Video not produced.** `video-benzene-mo-filling` carries
 `production_status: "deferred"` with its reason in `production_note`: it is
 an animated energy-level diagram, not a molecule drawn stroke by stroke, so
 the chalk pipeline cannot produce it.

## Deletions (what + why)

- None. Nothing authored in steps 2–5 was found redundant or unreferenced, so
 no concept, nugget, figure, video brief, or question was removed.
