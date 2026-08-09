# Coherence pass — biomolecules-nucleic-acids
Date: 2026-07-30

One pass, run after concepts, nuggets, assets, videos and question sets were drafted and
before compiling. Every category is answered. Changes were applied to the package; nothing
below is a proposal.

## Questions → text/figures

Four gaps surfaced, all of the same shape: the question set was authored against the
**expanded** text tier, but the reader's default tier is **standard**, so a student on the
default setting would have been asked something the visible prose did not teach. In every
case the fix was to deepen the nugget rather than soften the question.

- **`ch28-backbone-charge-count` (and its variant) → `nugget-phosphodiester-backbone`.**
 The question asks for an exact charge count on a 12-residue strand (answer 11). The
 standard tier said a strand of n residues carries "roughly n" negative charges, which is
 the wrong precision for a question graded with zero tolerance. **Changed:** the standard
 tier now states explicitly that n residues give n − 1 internal phosphodiesters, so a
 strand with free hydroxyls at both ends carries n − 1 charges.
- **`ch28-melting-temperature-rank` (and its variant) → `nugget-dna-double-helix-and-base-stacking`.**
 Both rank questions turn on counterion screening of backbone repulsion; the salt effect
 appeared only in the expanded tier. **Changed:** added the salt-screening paragraph to the
 standard tier, including the point that a melting temperature is meaningless without the
 buffer.
- **`ch28-mismatch-failure-mode` (and its variant) → `nugget-base-pairing-and-hydrogen-bonding`.**
 The questions require working a *rejected* pair (A·C donor-against-donor, G·T
 acceptor-against-acceptor) and distinguishing that electronic failure from a size
 argument. The standard tier worked only the two successful pairs. **Changed:** the
 standard tier now works both rejected combinations and states that neither fails on size.
- **`ch28-base-weak-basicity-v2` → `nugget-purine-and-pyrimidine-bases`.**
 The variant asks about the weak *acidity* of the lactam N–H (pKa 9–10), which was in the
 expanded tier only. **Changed:** added that sentence to the standard tier. Lower urgency
 than the three above because a `-v2` seeds as a draft and is never surfaced by default,
 but the pre-authored variant runtime can serve it, so the text has to support it.

No question needed a figure that did not exist. No question was softened or dropped.

## Questions → deck/reader

Each question type used has a worked example upstream in the same chapter:

- `rank_order` on the phosphoramidite cycle ← `roadmap-phosphoramidite-cycle`, which lays
 out the same four operations in order with reagents and notes.
- `hotspot` on the alpha phosphorus ← `mol-atp`, whose accessibility text names the alpha,
 beta and gamma phosphorus atoms and states which one is attacked.
- `structure_scaffold` (draw thymine / uracil) ← `mol-thymine` and `mol-uracil`.
- `comparison_matrix` and `multi_select` on donor/acceptor patterns ← the four base figures,
 each of whose `long_description` reads its own pairing edge as donors and acceptors.
- `error_repair` on RNA cleavage ← `mol-uridine-23-cyclic-phosphate` plus the mechanism in
 the nugget.

This package compiles its own deck (45 slides) from the nuggets, so there is no frozen
legacy deck to work around and no deferral was needed in this category.

## Videos → text

Four briefs (`video-nucleotide-assembly`, `video-base-pairing`, `video-rna-cleavage`,
`video-chain-extension`). No trim needed: each brief animates a change over time — bond
formation, arrow pushing, a strand being cut — which the prose can only assert. All four
are recorded as `production_status: deferred` with the reason (the chalk pipeline draws a
single molecule stroke by stroke and cannot render intermolecular bond changes) and with
the accessibility requirements production must meet. The reader carries the same content in
the matching nugget, so no learner is blocked by the deferral.

Two briefs authored earlier were **deleted** rather than deferred — see Deletions.

## Figures → text/questions

- Checked mechanically: every one of the 24 assets is referenced by at least one nugget's
 `asset_ids`, so there are no orphans inflating the review queue.
- No nugget was found describing a spatial or energetic idea in words that a figure should
 carry. The one candidate — the unequal grooves of the double helix — is carried by
 `pdb-b-dna-dodecamer`, a real crystal structure, precisely because a stylised drawing
 cannot show groove widths honestly.
- **No reaction coordinate diagram was authored for this chapter, deliberately.** The two
 candidates (acid-catalysed depurination, and the base-mediated RNA cleavage) are both
 multistep ionic processes, which is exactly the class that was rejected across chapters
 12–25 with "rewrite text to avoid needing diagram". The energetics are carried in prose
 instead.

## Concepts → whole package

All ten concepts have a nugget, at least one figure, and at least one surfaced question —
verified mechanically rather than by eye. No concept is left with no evidence path, so
mastery gating in the homework creator has something to key on for every node.

No question or figure was found whose real subject lacked a concept node.

## Crosswalks

No concepts were added or removed during this pass, so the crosswalk authored against the
final list still stands. All 13 catalogued textbooks are covered by explicit overrides
rather than by term matching, including the deliberate empty mapping for the sixteen-chapter
Essential edition, which has no nucleic acid chapter at all. Chapter numbers were read from
`backend/app/data/textbook_catalog.json` rather than recalled.

## Deferred (not applied this pass)

- **Videos remain unproduced.** Four briefs, each with a recorded deferral note. Producing
 them needs a pipeline that can animate intermolecular bond changes, which does not exist.
- **`clip-dna-double-helix` and `clip-rna-single-strand` are stylised, not molecular.** They
 orient the reader and are honest about it in their alt text ("shows overall shape only —
 it does not depict individual atoms"). A future pass could commission a labelled
 nucleotide-anatomy figure that names base, sugar and phosphate on one structure; the
 chapter currently splits that job across four separate molecule figures plus the prose.
- **No question exercises the `curved_arrow` type.** The RNA-cleavage and chain-extension
 mechanisms are both good candidates, but both are substitutions at phosphorus, and the
 curved-arrow renderer's bond-source handling has been unusable in previous chapters. The
 mechanisms are assessed by `error_repair` and `hotspot` instead.

## Deletions (what + why)

- **`video-glycosidic-bond-formation` (brief) — deleted.** It animated the same bond-forming
 event as `video-nucleotide-assembly`, which already forms the N9-to-C1' bond on screen and
 labels the beta configuration. Two briefs for one event is duplicated production cost for
 no teaching gain.
- **`video-helix-stacking` (brief) — deleted.** Replaced by `pdb-b-dna-dodecamer`. A real
 crystal structure shows stacking, antiparallel backbones and the two groove widths at once
 and more honestly than an animation of a schematic could, and it costs nothing to produce.
- **`clip-dna-strand-schematic` and `clip-base-pair-schematic` (planned clipart) — deleted
 before authoring.** The curated library has no clipart that actually depicts a single
 strand's backbone connectivity or a hydrogen-bonded base pair; the nearest candidates were
 decorative. Both jobs are done better by real structures: the dinucleotide figure
 (`mol-dinucleotide-dapdt`) for backbone connectivity, and the four base figures for the
 pairing edges.
- **`clip-dna-double-helix` removed from `nugget-dna-double-helix-and-base-stacking`.** It
 was placed in both nugget 1 and nugget 6, so the same stylised drawing rendered twice in
 one chapter. It is kept at the chapter opening, where orienting the reader is its job, and
 section 6 now leads with the crystal structure. The asset's own `concept_slugs` and
 `nugget_ids` were narrowed to match.
