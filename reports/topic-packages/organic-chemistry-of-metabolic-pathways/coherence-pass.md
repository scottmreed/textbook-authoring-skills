# Coherence pass — organic-chemistry-of-metabolic-pathways
Date: 2026-07-30

One pass, run after concepts, nuggets, figures, videos and question sets were all
drafted and before compiling.

## Questions → text/figures

Two questions were found to probe a detail the prose only carried in a figure
caption, and in both cases the nugget was deepened rather than the question
softened.

- **`ch29-schiff-base-arrow-v2`** asks for the arrow in which an active-site
 cysteine thiolate adds to the aldehyde of glyceraldehyde 3-phosphate. The
 covalent thiohemiacetal appeared only in a step note on
 `roadmap-glycolysis`, which is too thin a basis for a mechanism question.
 Added a passage to the `glycolysis-mechanisms` expanded text walking the three
 stages of that step — thiohemiacetal, hydride removal to a thioester, then
 phosphate displacing the cysteine — and stating why trapping the oxidised
 carbon as a thioester is what makes the acyl phosphate reachable.
- **`ch29-acyl-donor-ranking`** asks students to rank an acyl phosphate above a
 thioester, above an ester, above an amide. The `thioester-activation` nugget
 explained why a thioester beats an ester but never placed it on a scale, and
 acyl phosphates were introduced two concepts later. Added a paragraph to that
 nugget giving the full ordering, tying it to the stability of the group
 released, and saying which two metabolism actually uses and why.

Every other surfaced question was traced to prose that teaches its content at the
depth asked. No question needed a figure that does not exist.

## Questions → deck/reader

The deck is compiled from the concept list, so each concept becomes a section and
no question sits on a concept with no slide. Checked that each of the four
non-select question types has a worked example upstream: `curved_arrow` is
prepared by `site-aldolase`, which draws the identical lysine-to-carbonyl arrow;
`bond_change_ledger` by `site-citrate-synthase`, which draws the enol-to-ketone
arrow the ledger records; `hotspot` by `rxn-enoyl-coa-hydratase` and
`rxn-thiolase-retro-claisen`, which show the atoms being asked about; and
`structure_scaffold` by `rxn-aldolase-retro-aldol` and `rxn-enolase-dehydration`,
which show the products students are asked to draw. No change needed.

## Videos → text

Five briefs, checked against the prose for duplication. `video-citric-acid-cycle-carbons`
overlaps the claim in the `citric-acid-cycle-mechanisms` nugget that the carbon
dioxide released in a turn comes from the acceptor rather than from the acetyl
group — but the prose can only assert it while the video tracks labelled carbons
through nine steps, which is the medium that can actually show it. Kept both; no
duplicate trimmed. No brief was found to restate a paragraph redundantly.

## Figures → text/questions

No orphan assets: all 44 are referenced by a nugget, and the subset used in video
storyboards is referenced there too (verified mechanically — zero orphans, zero
dangling references). No nugget was found describing a spatial or energetic idea
in words that a figure should carry instead; the four active-site diagrams and
two protein structures exist precisely because the prose named catalytic residues
and an induced-fit closure that no molecule figure can show.

Deliberately **not** added: a reaction coordinate diagram. Every reaction in this
chapter is multistep and enzyme-mediated, which is exactly the case the 2026-07-23
review pass rejected. Energetics are carried in prose instead.

## Concepts → whole package

All ten concepts carry a nugget, at least three figures, and at least one
surfaced question; no concept is evidence-free and none had to be removed. No
question or figure was found whose real subject lacked a concept node. Concept
count unchanged at ten.

## Crosswalks

The concept list did not change during this pass, so the mcmurry and openstax
overrides written against it still hold. Both point at chapter 29. Separately,
the OpenStax entry in `backend/app/data/textbook_catalog.json` stopped at chapter
28 although the book has 31; chapters 29 to 31 were added after verifying the
section URLs return 200 and 32 does not. Nine of the thirteen catalogued books
have no metabolism chapter at all and are overridden to an empty chapter list
with a note, rather than being left to term-scoring, which would have matched
them confidently and wrongly.

## Deferred (not applied this pass)

- Gluconeogenesis (OpenStax 29.8) is out of scope and appears only as a caveat on
 `roadmap-glycolysis`. `ch29-catabolic-anabolic` lists it as an item to sort,
 which the caveat supports but does not develop. Covered instead by an
 Additional Reading link to §29.8; a dedicated concept would be the right fix if
 the chapter is ever expanded.
- The electron-transport chain and oxidative phosphorylation appear as the final,
 explicitly out-of-scope stage of `roadmap-glucose-to-carbon-dioxide`. They are
 not organic chemistry and no nugget develops them.

## Deletions (what + why)

None. Nothing authored in steps 2 through 5 was found redundant or unreferenced,
so no figure, nugget, brief or question was removed.
