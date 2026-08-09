# Coherence pass — amines-and-heterocycles
Date: 2026-07-30

Single pass, run after concepts, nuggets, assets, video briefs and question sets
were drafted and before the first compile. Every category answered; three prose
changes applied, no deletions.

## Questions → text/figures

**Three gaps found and closed by deepening the prose, not by softening the question.**

- `ch24-amide-nonbasic` grades three evidence statements about the amide nitrogen:
 the shortened C-N bond with restricted rotation, the coplanarity of the nitrogen
 with the carbonyl, and the fact that N,N-dimethylacetamide gains no basicity from
 its two alkyl groups. The basicity nugget asserted the conclusion ("the C-N bond
 has partial double-bond character") but never gave the experimental signatures the
 question asks the student to recognize as evidence, and never made the
 alkyl-groups-do-not-help point at all. Expanded tier of `nugget-amine-basicity`
 now states all three.
- `ch24-rank-aniline-substituents-v2` ranks benzylamine and diphenylamine, and
 `ch24-aniline-basicity-reasoning-v2` turns entirely on why a CH2 spacer rescues
 benzylamine's basicity. Neither compound appeared anywhere in the chapter: the
 arylamine nugget covered only the directly-attached case and its para
 substituents. Expanded tier of `nugget-arylamine-basicity` now adds the
 conjugation-path paragraph — benzylamine at pKaH 9.3 with the path broken by an
 sp3 carbon, diphenylamine at 0.8 with two rings in the path — which is also the
 generalization the substituent series was implicitly relying on.
- `ch24-choose-reducing-agent-v2` offers DIBAL-H at −78 °C as a distractor, and a
 distractor is only fair if the chapter has told the student what that reagent
 does. The reduction nugget said LiAlH4 goes "all the way to CH2 — not stopping at
 the aldehyde," which implies a reagent that does stop there but never names it.
 Expanded tier of `nugget-amine-synthesis-reduction` now names DIBAL-H and states
 the partial reduction explicitly.

Checked and confirmed adequate without change: the carbon-count bookkeeping that
`ch24-nitrile-carbon-count` and its Hofmann-rearrangement variant turn on is worked
in the reduction nugget with the same three cases; the methylation-equivalents rule
behind `ch24-hofmann-equivalents` is stated outright in the elimination nugget, and
the ring-nitrogen counting its variant needs is in the classification nugget; the
Chichibabin C2 amination and indole's C3 preference that the two pyridine variants
require are both stated in `nugget-pyridine-chemistry`; and the azobenzene trap in
`ch24-nitrile-route-v2` is called out by name in the reduction nugget.

No question was found to need a figure that does not exist. Every option set that
carries structures carries them on **all** options — the lone-illustrated-option
answer tell that the ch15 review surfaced was checked for mechanically and is absent.

## Questions → deck/reader

Every question type used has a worked treatment upstream. The two that most often
lack one were checked specifically: the `curved_arrow` attack is narrated
step-by-step in the expanded tier of `nugget-reductive-amination` and again in the
`video-reductive-amination` storyboard, and the single-step E2 that
`ch24-hofmann-profile` asks students to read off a curve is described in
`nugget-hofmann-elimination` as "one step, one transition state ... on a reaction
coordinate it is a single climb and descent — no intermediate — and exergonic
overall," which is exactly the geometry the profile shows. The
`bond_change_ledger` items are recoverable from the same sentence, which names all
four changes (proton removed, C-N broken, pi bond formed, O-H formed).

This is a full package with a freshly compiled deck, not a shim over a legacy deck,
so no frozen-deck escalation applies.

## Videos → text

Five briefs, all recorded as deferred (the chalk pipeline cannot animate electron
flow, orbital rehybridization, or pi-cloud electron counting). Because every brief
is deferred, the reader prose is the sole carrier of that content by design, so
there is no redundancy to trim — the overlap between `video-nitrogen-inversion` and
the inversion paragraph of `nugget-amine-structure-classification` is the intended
fallback, not duplication.

## Figures → text/questions

No orphans: all 26 molecule assets are cited by at least one nugget, checked
mechanically. Going the other way, one genuine gap was identified and **deferred
rather than papered over**: `nugget-pyrrole-imidazole` and `nugget-pyridine-chemistry`
both describe orbital geometry in words (a lone pair in a p orbital merged into the
pi cloud versus one in an in-plane sp2 orbital), which a figure would carry better
than prose. See Deferred.

## Concepts → whole package

All ten concepts have a nugget, at least one figure, and at least one question —
verified mechanically, not by inspection. No question or figure was found whose real
subject lacks a concept node: the fused-ring items (quinoline, indole) sit under
`pyridine-chemistry`, whose nugget covers the benzo-fused gallery explicitly, so no
eleventh node is warranted.

## Crosswalks

The concept list did not change during this pass, so the crosswalks authored against
it still cover it. All thirteen catalogued textbooks carry an explicit override
checked against `backend/app/data/textbook_catalog.json` rather than left to the term
matcher; two are honest partial matches with notes (Clayden, which splits the content
across chapters 29 and 43, and Bruice Essential, which has no dedicated amines
chapter).

## Deferred (not applied this pass)

- **Orbital overlay figures for pyrrole and pyridine.** The pyrrole-versus-pyridine
 lone-pair distinction is the load-bearing idea of the last two sections and is
 currently carried by prose plus the deferred `video-heterocycle-lone-pairs` brief.
 The `orbital-overlay-assets` skill needs a curated orbital-ready preset for each
 ring, which does not exist yet. Recorded here rather than authored, per the
 one-pass rule.

## Deletions (what + why)

None. Nothing in the package was found redundant or unreferenced.
