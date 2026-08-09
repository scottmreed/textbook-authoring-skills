# Coherence pass — biomolecules-amino-acids-peptides-and-proteins
Date: 2026-07-30

Run once, after concepts, nuggets, figures, videos and question sets were
drafted, and before compiling. Categories are walked later-authored →
earlier-authored so the newest information propagates backwards.

## Questions → text/figures

**No change needed, and here is why I am confident.** Every surfaced question
was checked against the prose that has to prepare it, by searching the nugget
text for the specific idea the question grades rather than for the topic:

- `ch26-build-l-alanine-fischer` needs the Fischer convention, not just the word
 "Fischer". `nugget-amino-acid-stereochemistry` uses the term four times and
 states the horizontal-toward-the-viewer rule twice, and anchors the L series
 to glyceraldehyde. Adequate.
- `ch26-histidine-isoelectric-point` grades pI = 7.59 from the two highest pKa
 values. `nugget-isoelectric-point` derives histidine's pI at that value by
 walking the charge ladder rather than quoting a recipe. Adequate.
- `ch26-amide-resonance-arrow` grades a lone-pair-to-atom arrow.
 `nugget-peptide-bond-structure` gives the nitrogen-into-carbonyl
 delocalisation with bond lengths and the 15–20 kcal/mol barrier. Adequate.
- `ch26-amidomalonate-leucine-route` and `ch26-racemic-amino-acid-synthesis`
 both grade the racemic outcome. `nugget-amino-acid-synthesis` states it for
 all four routes and names the planar or symmetric intermediate in each.
 Adequate.
- `ch26-draw-boc-glycine` and `ch26-boc-vs-fmoc-matrix` need the orthogonality
 of acid- and base-labile protection. `nugget-peptide-synthesis` carries both
 removal conditions explicitly. Adequate.
- `ch26-enzyme-catalysis-select` grades the ΔG‡-not-ΔG° distinction, which
 `nugget-enzymes-and-catalysis` states in four separate tiers. Adequate.

No question required a step the text hand-waves, so no nugget was deepened and
no question was softened.

## Questions → deck/reader

The chapter has no legacy deck; the deck is compiled from this package, so
every question type is prepared by the nugget that compiles into the slide
section covering its concept. The two types that most often lack an upstream
worked example — `curved_arrow` and `rank_order` — both land on concepts whose
nuggets carry the worked reasoning (amide delocalisation; the pI charge ladder
walked residue by residue). No slide gap found, nothing deferred here.

## Videos → text

**No change.** All three briefs animate a change over time that the prose can
only assert: proton order in a titration, the amide flattening as the lone pair
delocalises, and one Edman cycle leaving the rest of the chain intact. None
duplicates a paragraph — each brief's `production_note` records that the reader
carries the same content in the matching nugget, which is the intended
redundancy for a deferred video, not a duplication to trim.

## Figures → text/questions

**Five changes applied.** The mechanical orphan check found five figures cited
by no nugget and no video, which would have rendered nowhere. In every case the
prose does teach the chemistry, so the fix was to cite rather than delete:

| Figure | Cited into | Because the prose already |
|---|---|---|
| `mol-l-threonine` | `nugget-amino-acid-stereochemistry` | names threonine 6× and gives 2S,3R |
| `mol-l-isoleucine` | `nugget-amino-acid-stereochemistry` | names isoleucine 6× and gives 2S,3S |
| `mol-l-glutamic-acid` | `nugget-isoelectric-point` | works glutamic acid as an acidic-side-chain case 4× |
| `mol-l-tryptophan` | `nugget-peptide-sequencing` | discusses tryptophan's destruction by 6 M HCl 9× |
| `clip-antibody-schematic` | `nugget-protein-structure-levels` | uses an antibody as the multi-chain, disulfide-tied example |

Going the other way, no nugget was found describing a spatial or energetic idea
in words that a figure should carry: the four structure levels, the disulfide
cross-link, and the two enzyme folds are all figure-backed.

## Concepts → whole package

**No change.** All ten concepts carry a nugget, at least three figures, and at
least one surfaced question, so no concept has a broken evidence path for
mastery gating. Coverage counts after the citation fixes:

| # | concept | nuggets | figures | surfaced questions |
|---|---|---|---|---|
| 1 | amino-acid-structure-and-classification | 1 | 13 | 3 |
| 2 | amino-acid-stereochemistry | 1 | 5 | 1 |
| 3 | zwitterions-and-acid-base-behaviour | 1 | 4 | 1 |
| 4 | isoelectric-point | 1 | 9 | 3 |
| 5 | amino-acid-synthesis | 1 | 3 | 2 |
| 6 | peptide-bond-structure | 1 | 3 | 3 |
| 7 | peptide-sequencing | 1 | 7 | 2 |
| 8 | peptide-synthesis | 1 | 5 | 2 |
| 9 | protein-structure-levels | 1 | 7 | 2 |
| 10 | enzymes-and-catalysis | 1 | 3 | 1 |

No question or figure was found whose real subject lacked a concept node.

## Crosswalks

**No change.** No concepts were added or removed by this pass, so the six
explicit `textbook_matching.overrides` (McMurry 6e, McMurry Fundamentals 6e,
OpenStax current, Klein 4e, Wade 9e, Wade 5e) still cover the final list. Every
book in the catalogue has an explicit override rather than relying on term
scoring, because this chapter's terms ("synthesis", "structure") are exactly the
generic ones that produce confident wrong matches.

## Deferred (not applied this pass)

- **All three video briefs remain unproduced.** Each animates bond formation,
 electron flow or a reagent change, which the chalk-drawing
 `molecule-video-creator` pipeline cannot render. Recorded as
 `production_status: "deferred"` with the accessibility requirements the
 eventual production must meet, matching the deferral class used in chapters
 12–25.
- ~~**A titration-curve figure for `nugget-isoelectric-point`.**~~ **RESOLVED
 2026-07-30, after the four-persona review raised it independently three times
 (`instr-005`, `stud-003`, `visual-006`).** A `titration_curve` asset kind was
 added to the pipeline and two figures now lead the section: L-alanine and
 L-lysine, computed exactly from the charge balance rather than sketched, with
 pKa values confirmed against PubChem's curated Dissociation Constants. See
 `[internal source reference — not in this repo]nugget-peptide-bond-structure` names phi and psi and
 says a Ramachandran plot maps them, but nothing plots them. Same blocker as
 above.

## Deletions (what + why)

None. The five orphan figures were candidates for deletion under the
"cite it or delete it" rule, but each turned out to back chemistry the prose
genuinely teaches, so all five were cited instead. No reaction coordinate
diagram was authored at all — this chapter has no clean one- or two-step
profile whose shape is the lesson, and the science-review guidance is to carry
energetics in prose rather than force a diagram.
