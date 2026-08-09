# Coherence pass — carboxylic-acids-and-nitriles
Date: 2026-07-29

Run once, after concepts/nuggets/figures/videos/questions were drafted and before
the runtime compile. Categories walked later-authored → earlier-authored.

## Questions → text/figures

Two questions were asked at a depth the prose only implied. Both were fixed by
deepening the nugget, not by softening the question:

- **`ch20-deprotonation-ledger` (bond_change_ledger)** asks for the proton
 transfer bond by bond and charge by charge. `nugget-carboxylic-acid-acidity`
 argued the *thermodynamics* of the carboxylate but never enumerated what
 actually changes in the step. Added a sentence to `text.expanded` stating that
 one bond breaks (O–H), one forms (H–base), the two heteroatom formal charges
 exchange, and the carbon skeleton and C=O are spectators.
- **`ch20-nitrile-sn2-arrow` (curved_arrow)** requires knowing that the
 nucleophilic lone pair of cyanide is on **carbon**, not nitrogen.
 `nugget-nitrile-structure-and-preparation` named the SN2 mechanism but did not
 state the electron flow. Added a sentence to `text.expanded` giving the flow
 explicitly (carbon lone pair → backside attack on the halogen-bearing carbon,
 C–X electrons leave with halide).

No question needed a figure that does not exist. Every question whose stimulus is
a structure either carries `structure_smiles` on its options (`single_select`,
`multi_select`, `matching_pairs`, `comparison_matrix`, `synthesis_route`) or
names the compound in the prompt as a condensed formula (`short_answer`,
`rank_order`, `structure_scaffold`).

## Questions → deck/reader

The deck is compiled from the same nuggets, so slide coverage tracks nugget
coverage. After the two prose additions above, every question type used has a
worked treatment upstream:

- `curved_arrow` → nugget 8 electron-flow sentence (SN2 arrows themselves are a
 chapter-11 prerequisite, declared on the concept).
- `bond_change_ledger` → nugget 3 bond-accounting sentence.
- `rank_order` / `multi_select` / `comparison_matrix` → nugget 5 carries the full
 pKa series and the substituted-benzoic-acid ordering.
- `synthesis_route` → nugget 6 plus the `roadmap-nitrile-homologation` figure.
- `numeric_with_units` → nugget 10 gives both wavenumbers asked for.

## Videos → text

No redundancy to trim. All three briefs are electron-flow or atom-tracking
animations that the prose covers in words rather than duplicating:

- `video-carboxylate-delocalization` ↔ nugget 3 (bond-length argument).
- `video-nitrile-hydrolysis` ↔ nugget 9 (addition then amide hydrolysis).
- `video-nitrile-homologation-route` ↔ nugget 6 + the static roadmap figure.
 Static and animated forms are complementary here (the video's contribution is
 the coloured-carbon tracking), so the roadmap was **not** deleted.

All three are recorded as `production_status: deferred` with reasons — none is a
molecule drawn stroke by stroke, so the molecule-video-creator chalk pipeline
cannot produce them (same deferral class as chapters 12–19).

## Figures → text/questions

- **No orphans.** All 20 assets are cited by at least one nugget's `asset_ids`,
 and 12 of them additionally back a question. Nothing was deleted.
- **One gap that current asset types cannot close:** nugget 2 describes the
 cyclic hydrogen-bonded dimer, which is a spatial idea that a figure ought to
 carry, but no `ChemTeachingAssetType` renders an intermolecular hydrogen bond
 (a dot-separated SMILES would draw two unassociated molecules and mislead).
 Covered in prose plus the butanoic acid / butan-1-ol pair for the boiling-point
 comparison. Recorded under Deferred.

## Concepts → whole package

Every concept has a nugget, a figure, and a question — verified mechanically.
Two concepts were thin at one surfaced question each and were brought to two:

- `reactions-of-carboxylic-acids` → added `ch20-acid-reduction-reagent`
 (LiAlH₄ vs NaBH₄ vs oxidant vs proton transfer) + variant on selective
 reduction in the presence of a ketone.
- `reactions-of-nitriles` → added `ch20-nitrile-hydrolysis-product` (acid
 hydrolysis) + variant on DIBAH partial reduction.

Surfaced questions went 19 → 21; staged variants 19 → 21. No question or figure
was found whose real subject lacked a concept node, so no node was added.

## Crosswalks

The final concept list is unchanged by this pass (no concept added or removed),
so the mappings authored in step 2 still cover it. McMurry 6e ch 20 and OpenStax
ch 20 are exact one-to-one matches and are set as explicit overrides; all 13
catalogued books carry an explicit override rather than relying on term scoring.

## Deferred (not applied this pass)

- **Hydrogen-bonded dimer figure.** Needs an asset type that can draw an
 intermolecular hydrogen bond. Worth raising as a `teaching-asset-kind-registration`
 request; not invented here as a mislabelled `molecule` asset.
- **Videos.** All three briefs remain unproduced pending a mechanism-animation
 pipeline; deferral reasons and caption/transcript requirements are recorded in
 each brief's `production_note`.
- **`bruice-essential-organic-chemistry` crosswalk.** The catalogued chapter list
 for that title stops at chapter 16 and contains no carbonyl chapters, so the
 override is an empty chapter list with a FLAG note. Fixing it means extending
 `backend/app/data/textbook_catalog.json`, which is outside this chapter's scope.

## Deletions (what + why)

None. Nothing in the package was found redundant or unreferenced, so no concept,
nugget, figure, video brief, or question was removed in this pass.
