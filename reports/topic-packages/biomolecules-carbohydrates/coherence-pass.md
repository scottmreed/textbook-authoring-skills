# Coherence pass — biomolecules-carbohydrates

Date: 2026-07-30

Run once, after concepts, nuggets, assets, video briefs, and question sets were
drafted, and before compiling. Categories are walked later-authored →
earlier-authored so the newest information propagates first.

## Questions → text/figures

**Change applied — Kiliani–Fischer chain lengthening added to the prose.** The
`synthesis_route` question (`ch25-kiliani-fischer-route`, plus its `-v2`) asks a
student to lengthen D-arabinose to D-glucose through a cyanohydrin. Nothing in
the drafted nuggets taught chain extension at all: the question demanded a
reaction the chapter never introduced. Per the skill's rule, the fix was to
deepen the text rather than soften the question. Added:

- a full Kiliani–Fischer paragraph to the `expanded` tier of
 `nugget-sugar-oxidation-and-reduction`, covering HCN addition, the controlled
 nitrile reduction that stops at the aldehyde, the fact that addition to a
 planar carbonyl produces **two C2 epimers**, and the Wohl degradation as the
 reverse operation;
- a two-sentence version in the `standard` tier;
- a fifth learning objective naming the sequence and the epimer pair.

**Change applied — the question was retagged to the concept the text now
teaches.** Both route questions were authored under `glycoside-formation`, which
was simply wrong: chain lengthening is monosaccharide reagent chemistry, not
acetal chemistry. Retagged parent and variant to
`sugar-oxidation-and-reduction`, where the new prose lives.

**Change applied — new figure.** Adding the reaction to the prose left the
intermediate undrawn, so `mol-gluco-cyanohydrin` was authored (verified SMILES,
alt text plus long description) and cited from
`nugget-sugar-oxidation-and-reduction`. Asset count 30 → 31.

**Change applied — acylation of the non-anomeric hydroxyls added to the prose.**
`ch25-glycoside-error-repair-v2` turns on the fact that acetic anhydride and
pyridine acylate a glycoside's free secondary hydroxyls and leave the acetal
untouched. The drafted `nugget-glycoside-formation` said glycosides are stable
to base but never said what the *rest* of the ring does. Added a paragraph to
its `expanded` tier: once C1 is an acetal, C2/C3/C4/C6 are ordinary alcohols that
acylate and alkylate normally, which is exactly why the glycoside is the standard
anomeric protecting group.

**Change applied — a second question added so a major concept is not assessed by
one item.** Retagging the route questions left `glycoside-formation` with a single
surfaced question. Added `ch25-glycosylation-outcome` (single_select on the
planar-oxocarbenium origin of the anomeric mixture) and its `-v2` on the
N-glycosidic linkage of adenosine, which the `expanded` tier of
`nugget-glycoside-formation` already covered but nothing assessed. Surfaced
questions 27 → 28.

**No change, checked:** the mutarotation arithmetic question needs
+112 / +18.7 / +52.6 — all three are in `nugget-anomers-and-mutarotation`. The
`chair` question needs the all-equatorial result and the β-D-xylopyranose case —
both in `nugget-pyranose-chair-conformation`. `ch25-reducing-sugar-criterion-v2`
needs the enediol by name — present in `nugget-sugar-oxidation-and-reduction`
along with the Lobry de Bruyn–van Ekenstein rearrangement. The galactose rotation
values in `ch25-mutarotation-percent-v2` are supplied in the prompt itself and
need no prose support.

## Questions → deck/reader slides

The deck is compiled from the nuggets (one section per concept), so "is there a
slide that prepares students for each question type" reduces to whether the prose
works the relevant example.

**No change needed.** The two types most often unsupported were checked directly:
`curved_arrow` (ring closure) is worked arrow-by-arrow in the `expanded` tier of
`nugget-cyclic-hemiacetal-formation`, including the C6 alternative the question
uses as a distractor; `rank_order` (stereocenter counting) is derived in
`nugget-carbohydrate-classification` and applied in
`nugget-d-l-configuration-and-families`. `reaction_coordinate_reasoning` is
supported by the `rc-mutarotation` asset in the same section.

## Videos → text

**No change.** All four briefs are deferred (the chalk pipeline cannot animate
bond formation, ring puckering, or polymer assembly), so no video currently
displaces prose. Each brief's `production_note` records that the reader carries
the same content in the named nugget, and the overlap is deliberate
reinforcement rather than duplication — if the videos are ever produced, the
prose still has to stand alone for the deferral case.

## Figures → text/questions

**No change beyond the addition above.** Verified mechanically that no asset is
orphaned: all 31 assets are cited by at least one nugget's `asset_ids`, and all
four video briefs are cited by a nugget's `video_brief_ids`.

Also checked the reverse direction — nuggets describing something spatial in
words that a figure should carry. The chair discussion in
`nugget-pyranose-chair-conformation` is the candidate, and it is deliberately
carried by five molecule figures plus the `chair` question workspace rather than
by a `conformational_energy_profile` asset: that asset type maps to a
`reaction_coordinate` reader block whose dihedral-scan spec the reader cannot
render, so it would ship as alt text only. The energetics stay in prose.

## Concepts → whole package

**No change.** Every concept has a nugget, at least two figures, and at least two
surfaced questions after the changes above (range 2–4). No question or figure
was found whose real subject lacked a concept node.

## Crosswalks

**No change needed.** The concept list did not gain or lose a concept in this
pass — only one concept's question allocation changed. The `textbook_matching`
terms already cover the Kiliani–Fischer material implicitly through
"monosaccharides"; all thirteen catalogued textbooks carry explicit `overrides`,
so no term-scored match can drift.

## Deferred (not applied this pass)

- **Wohl degradation is named but not worked.** The new prose mentions it in one
 clause as the reverse of Kiliani–Fischer. No question tests it and no figure
 shows it. Worth a worked example if the chapter is ever expanded, but adding
 one now would trigger another round of question authoring.
- **No figure for the oxocarbenium ion.** `nugget-glycoside-formation` describes
 it in words and `ch25-mutarotation-profile-v2` puts it on an energy profile,
 but there is no drawn structure. The `orbital_overlay` asset type would suit
 it and has never been used by any package in this repo; leaving it alone rather
 than debugging an unexercised renderer inside a content pass.
- **The `chair` workspace draws a plain carbocycle.** The renderer has no ring
 heteroatom, so both chair questions state in the prompt and the accessible
 description that the unsubstituted vertex is the ring oxygen. This is honest
 and answerable, but a pyranose-aware chair workspace would be better. Platform
 work, not content work.

## Deletions (what + why)

None. Nothing authored in steps 2–5 was found redundant or unsupported.

---

# Post-compile verification (separate from the coherence pass)

Run after compiling, 2026-07-30. Recorded here rather than in a new file because
it is the evidence behind this chapter's Definition-of-Done claims.

- **Every authored question was graded with its own correct answer** through the
 live registry graders (a submission built mechanically from each `answer_key`).
 56 / 56 graded; 52 returned `correct`. The four `structured_reasoning` items
 returned `manual_review` with `objective_score: 1.0` — every selected-response
 field graded correct and only the free-text field escalated.
- **Platform observation:** `structured_reasoning` never autogrades its
 `short_text` fields. Submitting the authored answer and submitting the string
 `"banana"` produce byte-identical results. The `answer_key.fields.*.answer_text`
 lists authored for those fields are therefore inert at grading time and serve
 only as documentation for the reviewing teacher. Chapter 24 has the same
 pattern. Not a chapter defect; worth raising if the review pass wants those
 fields to gate.
- **Both `fischer` answer keys were re-derived independently** rather than
 trusted from memory: `sugar_form_service.render_fischer_svg` was run on the
 D-glucose and D-galactose SMILES and the left/right side of each stereocenter
 hydroxyl read off the generated projection. D-glucose came out right / left /
 right / right and D-galactose right / left / left / right, matching the
 authored `expected_state` rows exactly.
- **Every SMILES in the package was verified with RDKit** (formula, CIP labels at
 every stereocenter, InChIKey). The four disaccharides were checked more
 strongly still: each was fragmented at its glycosidic bond and the pieces
 capped, and each regenerated exactly the expected monosaccharide pair —
 maltose → β-D-Glcp + α-D-Glcp, cellobiose → β-D-Glcp + β-D-Glcp, lactose →
 β-D-Glcp + β-D-Galp, sucrose → β-D-Fruf + α-D-Glcp. Sucrose's InChIKey
 (CZMRCDWAGMRECN-UGDNZRGBSA-N) matches the literature value.
- **Review manifest:** 86 tasks, no duplicate `asset_id`. All 31 figures and all
 4 video briefs are `needs_review`; nothing was auto-approved.
- **Reader homework preview** (from the compiled public summary): 28 surfaced
 questions across 19 types, all 10 concepts represented, ordered by concept and
 then core → standard → advanced within each concept. No
 `molecular_geometry` / `molecular_vibration` items, which `PublicQuestionSetPanel`
 cannot render answerably.
