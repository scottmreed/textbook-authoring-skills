# Coherence pass — synthetic-polymers

Date: 2026-07-30

Run once, after concepts, nuggets, assets, video briefs and question sets were
drafted, and before the first compile. Categories walked later-authored →
earlier-authored so that what the question set revealed could propagate back
into the prose and the figures.

## Questions → text/figures

Every surfaced question was traced back to the prose that has to support it. To
be accurate about what this pass did and did not change: the nuggets and the
question set were drafted close together, so most of these dependencies were
already satisfied when the pass ran. What follows records what was **checked**,
and flags the one case where a figure was genuinely added as a result.

Verified as already carried, not changed:

- `ch31-carothers-degree-of-polymerization` asks the student to apply
 DPn = 1/(1 − p). The expanded tier of `nugget-chain-growth-versus-step-growth`
 derives it rather than asserting it (each reaction reduces the molecule count
 by one, so N = N₀(1 − p) and the units per molecule is N₀/N). Confirmed
 present.
- `ch31-weight-average-molar-mass` requires Σ(NᵢMᵢ²)/Σ(NᵢMᵢ), and its most
 instructive distractor is returning the number-average instead. Nugget 8's
 expanded tier states both definitions side by side and says in words that the
 extra factor of Mᵢ is the entire difference. Confirmed present.
- `ch31-tacticity-comparison-v2` turns on syndiotactic chains crystallising just
 as isotactic ones do — regularity, not one-sidedness, is what packing needs.
 Nugget 4's standard tier says exactly that. Confirmed present.
- `ch31-romp-driving-force` needs the strain values that separate norbornene and
 cyclooctene from cyclohexene. Nugget 9 gives ≈27 and ≈7 kcal/mol against
 essentially zero, so the answer is derivable rather than recalled. Confirmed
 present.
- `ch31-propagation-bond-ledger`'s hardest distractor — recording the C3–C4 bond
 as broken rather than reduced in order — depends on the sigma/pi split, which
 is carried by `mol-ethylene`'s long description. Confirmed present.

Changed as a result of this pass:

- **`fig-molecular-weight-distribution` was commissioned and added.** The
 molecular-weight concept was the only one whose central claim — that Mw and Mn
 are two weightings of one curve rather than two measurements — was carried in
 words alone, while a question had just been written that turns on it. The
 figure plots one distribution with both averages computed off the plotted
 table and marked on it, and asserts Mw > Mn before writing.

No question was softened to fit the prose, and no numerical claim in the prose
was left unchecked: the stoichiometric-imbalance ceilings quoted in nugget 6
(≈100 units at 2% excess, ≈40 at 5%) were recomputed from
DPn = (1 + r)/(1 − r) at complete conversion and match.

## Questions → deck/reader

This is a full package with no legacy deck, so the deck is compiled from these
nuggets and there is no frozen slide set to work around. Every question type used
has a worked precedent upstream:

- `rank_order` and `bond_change_ledger` are prepared by the four authored
 reaction assets (`rxn-aibn-homolysis`, `rxn-radical-initiation-styrene`,
 `rxn-radical-propagation-styrene`, `rxn-radical-termination-combination`),
 which walk the same sequence the questions ask students to reproduce.
- `comparison_matrix` is prepared by `fig-polymer-tacticity`, which lays the
 three cases out in the same shape the table asks for.
- `numeric_with_units` on Carothers is prepared by `fig-chain-vs-step-growth`,
 which prints the same computed values the question asks for at a different
 conversion.
- `structure_scaffold` is prepared by `rxn-pet-esterification` and
 `rxn-nylon-66-amidation`, which show one junction forming — exactly what the
 drawing questions ask for.

No gap found that would have required a slide.

## Videos → text

All six briefs are deferred, so no video currently duplicates prose. One overlap
was examined and deliberately kept: `video-chain-versus-step-growth` and
`fig-chain-vs-step-growth` argue the same point. They were kept as a pair because
the figure carries the *quantitative* claim (computed Carothers values against
conversion) and the video would carry the *temporal* one (two flasks evolving),
and the figure exists precisely because the video is deferred. The reasoning is
recorded in that brief's `production_note` so a later producer does not read the
figure as making the video redundant.

## Figures → text/questions

- **No orphans.** Checked mechanically: all 43 assets are cited by at least one
 nugget, and every concept has at least one asset.
- `fig-molecular-weight-distribution` was added during this pass; see the first
 section for why.
- Every figure is cited by the nugget whose argument it carries; none is
 decorative.

## Concepts → whole package

Every one of the ten concepts has a nugget, at least one asset, and at least one
surfaced question. Verified mechanically rather than by inspection.

Coverage counts (concept: nuggets / assets / surfaced questions):
`polymer-basics-and-repeat-units` 1/6/1 · `chain-growth-radical-polymerization`
1/10/2 · `cationic-and-anionic-chain-growth` 1/5/1 · `ziegler-natta-and-tacticity`
1/3/1 · `copolymers` 1/5/1 · `step-growth-polymerization` 1/11/2 ·
`chain-growth-versus-step-growth` 1/1/2 · `molecular-weight-and-dispersity`
1/3/1 · `olefin-metathesis-polymerization` 1/5/1 ·
`polymer-properties-and-degradation` 1/9/1.

`chain-growth-versus-step-growth` carries only one asset. This is deliberate:
the concept is a comparison rather than a body of structures, and its single
asset is the figure that *is* the comparison. It is supported by two surfaced
questions, so it is not thin on evidence.

No concept was added or removed during this pass, so the crosswalks did not need
revisiting; they were authored against the final ten-concept list.

## Crosswalks

Explicit `overrides` written for all thirteen catalogued books rather than the
usual six, per the standing rule from chapter 26. Six books have a genuine
Synthetic Polymers or Polymerization chapter and are mapped by number; five have
no such chapter in their catalogued list and are overridden to `chapters: []`
with a stated reason. Two entries are truncation artefacts rather than genuine
absences and say so.

## Deferred (not applied this pass)

- **All six video briefs are unrendered.** Five of them
 (`video-radical-chain-lifecycle`, `video-chain-versus-step-growth`,
 `video-tacticity-and-packing`, `video-metathesis-partner-swap`,
 `video-elastomer-stretch-and-recoil`) require multi-body motion over time,
 which the molecule-video-creator chalk pipeline structurally cannot express;
 each brief records that. The sixth, `video-repeat-unit-emerges`, *is* within
 the pipeline's ability — it asks only for a molecule to be drawn and extended —
 and is deferred only because rendering spends paid quota that was not
 authorised for this chapter. It is the one brief that could be produced today.
- **A glass-transition / melting-point figure for nugget 10.** A modulus-against-
 temperature plot marking Tg and Tm would strengthen the thermal-transition
 argument, which is currently carried in prose. Not authored this pass: no
 question depends on it, and the figure set was held to what the assessments
 actually require. Worth adding if this concept later gains a question.
- **`textbook_catalog.json` is truncated for two books.** The catalogued McMurry
 6e list stops at chapter 29 and the Klein 4e list has no polymers entry, so
 neither can be mapped by number even though the printed books very likely
 carry the chapter. Extending the catalogue is the correct fix and is outside
 this package.

## Deletions (what + why)

- **Three polypropylene tacticity molecule assets, cut before they shipped.**
 Verified stereo-SMILES for isotactic, syndiotactic and atactic pentads were
 built and dyad-checked (meso/racemo test: mmmm, rrrr, mrrm). They were then
 rendered and inspected, and RDKit's auto-depiction places the stereocentres at
 *alternating* zig-zag vertices, so an isotactic chain draws as alternating
 wedge/hash and a syndiotactic chain draws as all-wedges — the reverse of what a
 student reads off the page. Replaced by `fig-polymer-tacticity`, hand-built on a
 flat all-anti backbone with every substituted carbon asserted to sit on the
 same vertex parity. The chemistry was correct; the depiction was not, and the
 depiction is what a learner sees.
- **No `reaction_coordinate` asset anywhere in the chapter.** Every energetic
 argument here is either multistep (radical chain growth), an equilibrium
 balance rather than a barrier (metathesis), or not a reaction coordinate at all
 (Tg and Tm are thermal transitions). Per the standing science-review finding
 that diagrams authored for multistep processes are rejected with "rewrite text
 to avoid needing diagram", the energetics are carried in prose and the figure
 budget went to the four structure-property diagrams instead.
- **No `curved_arrow` question.** The chapter's two signature mechanisms are
 radical chain growth, which needs fishhooks rather than two-electron arrows,
 and metathesis, which has no polar arrow-pushing description at all — its own
 nugget says so explicitly. Combined with the renderer's inability to take a
 bond as an arrow endpoint, `bond_change_ledger` was used instead, which asks
 for the same electron bookkeeping in a form the platform can actually grade.
