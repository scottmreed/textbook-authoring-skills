# Coherence pass — biomolecules-lipids
Date: 2026-07-30

Run once, after concepts/nuggets/assets/videos/question_sets were drafted and
before compiling. Package state at pass time: 10 concepts, 10 nuggets, 36
molecule assets, 4 video briefs, 26 surfaced questions across 18 types plus 26
staged `-v2` variants.

## Questions → text/figures

**Change applied — `chain-packing-and-melting-points` nugget deepened (standard
and expanded tiers).** The `newman` variant
`ch27-saturated-chain-conformation-v2` asks for the *highest*-energy
conformation about an interior chain bond (syn-eclipsed), but the nugget only
taught the anti minimum — it never mentioned the eclipsed maximum or the
rotational barrier. Per the rule, the nugget was deepened rather than the
question softened: both tiers now name the syn-eclipsed arrangement explicitly
as the barrier between staggered forms, and the expanded tier makes the
butane-C2–C3 analogy explicit so the projection the question shows is the one
the prose describes.

**Change applied — `steroids-structure-and-conformation` nugget deepened
(expanded tier).** The `chair` variant `ch27-cholesterol-a-ring-chair-v2` moves
to a freely flipping methylcyclohexane and asks which conformer dominates at
equilibrium, and the parent question's feedback appeals to 1,3-diaxial
crowding. The nugget distinguished axial from equatorial as labels but never
named the steric penalty that makes equatorial preferred in an unconstrained
ring. Added a clause naming the 1,3-diaxial interaction and stating the
methylcyclohexane equilibrium result.

**No change — melting-point numbers.** Both `rank_order` questions and the two
`structured_reasoning` questions grade against specific melting points. Checked
that every value used appears in the `chain-packing-and-melting-points` expanded
tier: lauric 44, myristic 54, palmitic 63, stearic 70, oleic 13, elaidic 45,
linoleic −5, linolenic −11, arachidonic −49 °C. All present.

**No change — hydrogenation stoichiometry.** `ch27-hydrogen-equivalents-arachidonic-v2`
requires summing double bonds across three different acyl chains. The
`hydrogenation-and-trans-fats` expanded tier already works exactly this case
(1 + 2 + 3 = 6), so the question is answerable from the prose as written.

**No change — no question needed a figure that did not exist.** Every question
carrying structures draws them from the verified asset SMILES set. The two
`rank_order` questions are deliberately text-only because that type drops
structures at render; their card text carries the shorthand and the
double-bond count so each card is self-sufficient without a figure.

**Accepted cross-chapter dependency (recorded, not changed).**
`ch27-identify-steroid-from-evidence-v2` uses the ester C=O infrared absorption
near 1740 cm⁻¹ as evidence. That number is taught in the spectroscopy chapter,
not this one. Judged a legitimate prerequisite callback for an Organic 2
chapter rather than a gap; the question remains answerable from the structures
alone via the saponification and rigidity evidence.

## Questions → deck/reader

This is a full package with no legacy deck, so deck slides are compiled from the
nuggets — there is no separate slide surface that could fall out of step, and the
two nugget deepenings above propagate into the deck automatically.

Checked that each question type used has a worked example upstream. The
mechanism types are the ones at risk: `curved_arrow`, `bond_change_ledger`, and
their variants all sit on the saponification mechanism, which the
`saponification-and-soap-action` expanded tier develops step by step with the
electron flow named at each stage, and which `video-saponification-mechanism`
storyboards arrow by arrow. `error_repair` and `evidence_board` need no separate
worked example — they test claims the prose asserts directly.

## Videos → text

Four briefs, each mapped to one nugget. Checked each for redundancy against the
prose and found none worth trimming: every brief animates something the text can
only assert. `video-cis-kink-packing` shows chains failing to stack,
`video-saponification-mechanism` shows electron flow, `video-bilayer-assembly`
shows self-assembly, `video-steroid-rigidity` shows a ring flip being attempted
and failing. Each is a motion or assembly the static figures cannot carry, so
both media are kept.

All four are recorded as `production_status: deferred` with an explicit note:
each animates motion, assembly, or arrow-pushing rather than a single structure
drawn stroke by stroke, which is outside what the molecule-video-creator chalk
pipeline produces. This matches the deferral class used in chapters 12–25. Each
note records the accessibility requirement (captions, narration naming every
visual change, transcript, no distinction resting on colour or motion alone) and
names the nugget carrying the same content in the reader.

## Figures → text/questions

**No orphans.** Verified mechanically: all 36 assets are referenced by at least
one nugget's `asset_ids` or one video brief's `visual_asset_ids`, and no nugget
references a missing asset. Nothing was added speculatively and nothing needed
deleting.

**No change — spatial ideas already carried by figures rather than words.** The
three arguments in this chapter that are genuinely geometric each have a figure
pair doing the work: cis-versus-trans packing has oleic/elaidic/stearic acid,
the stereocenter argument has tristearin against the mixed triacylglycerol, and
the rigidity argument has cis- against trans-decalin.

## Concepts → whole package

Every concept has a nugget, at least four figures, and at least two surfaced
questions — verified mechanically, lowest coverage is 4 figures and 2 questions.
No concept lacks an evidence path, so mastery gating in the homework creator has
something to work with everywhere.

No question or figure was found whose real subject had no concept node. The one
that came closest was the saponification *mechanism*, which could arguably be
its own node; it is left inside `saponification-and-soap-action` because the
mechanism and the soap behaviour are taught as one argument (the irreversible
proton transfer is what makes the carboxylate, and the carboxylate is what
cleans), and splitting them would separate a cause from its consequence.

## Crosswalks

Concept list unchanged by this pass — the two changes were deepenings of existing
nuggets, adding no concepts and removing none — so the crosswalks did not need
re-derivation. They were nonetheless verified against
`backend/app/data/textbook_catalog.json` rather than assumed, since the matcher
scores generic terms and can produce a confident wrong match. Explicit overrides
are supplied for **all 13 catalogued textbooks**, so no chapter number in this
package comes from the scorer.

Two are deliberately non-obvious and are annotated in the package:

- **clayden-organic-chemistry-1e / 2e** → ch 47 *Natural Products*. Clayden has
 no lipids chapter; the terpenoid and steroid half of this package lives in
 Natural Products, while fats, soaps, and phospholipids are treated with ester
 chemistry earlier. The note records that no single chapter covers the package.
- **bruice-essential-organic-chemistry** → **empty chapter list**. The catalogued
 chapter list for this text ends at chapter 16 (aromatic substitution) and
 contains no biomolecule chapters at all, so there is genuinely nothing to map
 to. Left empty with a note rather than pointing at an unrelated chapter.

Two more carry a combined-chapter caveat: `mcmurry-fundamentals-organic-chemistry-6e`
ch 24 and `forsey-organic-chemistry-2e-oer` ch 20 each bundle lipids with nucleic
acids, so the note states that only the lipid half maps here.

## Deferred (not applied this pass)

- **Lanosterol figure.** The squalene → squalene oxide → lanosterol → cholesterol
 sequence is told in prose in the `steroids-structure-and-conformation` expanded
 tier, but lanosterol itself is not rendered. Hand-built SMILES for it failed
 verification twice (wrong formula — the Δ8,9 ring double bond and the 14α-methyl
 are easy to drop), and shipping an unverified structure would violate the rule
 against submitting a figure that has not been confirmed to render correctly.
 Squalene and cholesterol, both verified, carry the endpoints. Revisit with an
 authoritative structure source.
- **Myristic acid figure.** Used as a card in `ch27-rank-unsaturation-melting-points-v2`
 and quoted in the melting-point series, but not rendered as an asset. Harmless
 because `rank_order` drops structures anyway, so the card would show text
 regardless. Add if the melting-point series is ever given a figure of its own.
- **Cortisol figure.** Verified to the correct formula (C21H30O5) with full
 stereochemistry, but dropped from the asset set to keep the steroid figures to
 the three that carry the argument (cholesterol, testosterone, estradiol).
 Cortisol is named in prose as the glucocorticoid that shuts off eicosanoid
 synthesis upstream, which is the only role it plays in this chapter.

## Deletions (what + why)

- **Reaction coordinate diagram for saponification — never authored, deliberately.**
 The obvious energy figure for this chapter would profile the addition–elimination
 sequence, but the science-review rule restricts reaction coordinate diagrams to
 single clean steps or to two-step profiles whose shape *is* the lesson.
 Saponification is a multistep ionic mechanism whose lesson is the irreversibility
 of a *proton transfer*, which a coordinate diagram obscures rather than shows.
 Replaced by: prose in the `saponification-and-soap-action` expanded tier plus the
 `video-saponification-mechanism` storyboard, and the energetics stated in words.
- **All non-`molecule` asset types — none authored.** `newman_projection`,
 `conformational_energy_profile`, and similar render as empty graphic
 placeholders unless the package also ships a hosted `image_url`, and
 `stereochemistry_conversion` does not render in the reader at all. The
 conformational content is instead carried by the `newman` *question* type,
 which does render, and by prose. Recorded here so a later pass does not
 re-add them without also producing hosted renders.
