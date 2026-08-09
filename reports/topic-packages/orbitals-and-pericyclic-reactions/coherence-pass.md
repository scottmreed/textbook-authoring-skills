# Coherence pass — orbitals-and-pericyclic-reactions
Date: 2026-07-30

Run once, after concepts, nuggets, assets, video briefs and question sets were all
drafted, and before the final compile. Every category below was answered; where
nothing changed, the reason is recorded rather than left blank.

## Questions → text/figures

Three gaps where a question demanded something the prose did not actually teach.
In each case the prose was deepened rather than the question softened.

- **`ch30-dienophile-reactivity-rank` outran the text.** The question ranks
 ethylene < methyl acrylate < maleic anhydride < tetracyanoethylene, but the
 cycloaddition nugget named only "a carbonyl, nitrile, or nitro group" and
 maleic anhydride — a student could not have placed TCNE, and had no basis for
 treating the effect as cumulative. **Added** a sentence to
 `nuggets[5].text.standard` making the effect explicitly additive and naming all
 four dienophiles in order.
- **`ch30-endo-adduct-statements` option (d) tests a fact the text never stated.**
 The distractor claims the adduct forms as a single enantiomer; it is in fact
 racemic. The chapter discussed racemic products for conrotatory electrocyclic
 closure but never for cycloaddition, so the item was unanswerable from the
 chapter. **Added** a paragraph to `nuggets[6].text.standard` separating relative
 from absolute configuration: the Diels-Alder fixes the former completely and
 leaves the latter undetermined, giving one diastereomer as a racemate.
- **`ch30-electrocyclic-ring-size-sort` uses hexa-1,5-diene as a
 "not conjugated" distractor.** The electrocyclic nugget said spectator π bonds
 "are not counted" but never said that a non-conjugated diene cannot undergo an
 electrocyclic reaction at all. **Added** a paragraph to
 `nuggets[3].text.standard` stating the continuity requirement, naming
 hexa-1,5-diene explicitly (and noting it belongs to the Cope family instead),
 and stating the ring-size rule the question sorts on.

No question needed a figure that did not exist: the two `structure_scaffold`
items are answered by drawing, and every other item's stimulus is carried in its
`prompt_text` or its options.

## Questions → deck/reader

Every question type used has a worked example upstream. Specifically checked the
two that most often lack one: `comparison_matrix`
(`ch30-selection-rules-matrix`) is prepared by the four canonical results set out
in `nuggets[4].text.expanded`, and `rank_order`
(`ch30-dienophile-reactivity-rank`) is prepared by the HOMO–LUMO energy-gap
argument in `nuggets[2].text.expanded` plus the substituent discussion in
`nuggets[5]`. This is a full package, not a shim over a legacy deck, so the deck
recompiles from the nuggets and no frozen slide problem arises.

## Videos → text

Reduced from ten planned briefs to **five**. Ten briefs, every one of them
deferred, would have been noise in the review queue rather than a production
plan. The five retained are the ones whose teaching value cannot be recovered
from a static figure: the rotation animation, the frontier-orbital approach, the
endo/exo stack, the [3,3] chair fold, and the two-step vitamin D sequence. No
brief duplicates prose that the text already carries well; the deleted five were
all cases where the static molecule and reaction assets say the same thing.

## Figures → text/questions

- **No orphans.** The assembler enforces this mechanically: every asset id must
 be cited by at least one nugget or the build fails. All 35 pass.
- **Two figures added because a nugget described something no figure showed.**
 `mol-5-methylcyclopentadiene` — the sigmatropic nugget leans on substituent
 scrambling as its evidence that a [1,5] shift is easy, and had no picture of
 the compound. `rxn-previtamin-to-vitamin-d` — the biology nugget claims two
 consecutive pericyclic steps but only the ring opening had a reaction figure,
 so the [1,7] shift was asserted and not shown.
- **Deliberate absence, recorded so it is not read as an oversight.** There is no
 figure of the butadiene ψ1–ψ4 or hexatriene ψ1–ψ6 orbital sets. The committed
 orbital library holds no polyene MO asset, and inventing one is prohibited —
 new orbital SVGs are authored in a reviewed sandbox, not in-app. The chapter
 therefore carries those systems as the node-counting rule and the terminal-lobe
 rule, which is exactly the information the selection rules consume, and
 `nuggets[1].text.expanded` says so in as many words so the omission reads as a
 choice. The Additional Reading panel links OpenStax §30.1 specifically for
 readers who want to see the orbitals drawn.

## Concepts → whole package

All ten concepts carry a nugget, between two and eight assets, and at least one
surfaced question. No concept is evidence-free, and no question or figure has a
subject without a concept node. `orbital-symmetry-selection-rules` carries two
parent questions rather than one because it is the chapter's load-bearing idea
and is tested both as a rule (the matrix) and as an application (the drawing).

## Crosswalks

The concept list did not change during this pass — the three edits above deepened
existing nuggets and added no concept — so the crosswalks authored against it
still hold. All thirteen catalogued textbooks carry an explicit override.

## Deferred (not applied this pass)

- **McMurry 6e maps to nothing.** The catalogued chapter list for
 `mcmurry-organic-chemistry-6e` stops at chapter 29, so there is no pericyclic
 entry to read a number off, and the crosswalk asserts `chapters: []` with an
 explanation rather than an unverified 30. The fix is to extend
 `backend/app/data/textbook_catalog.json`; that is a catalog change with
 consequences beyond this chapter (the same truncation will block the future
 Synthetic Polymers package) and is left for a separate, deliberate edit.
- **Orbital library assets are not `verified`.** All four MO overlays used here
 are `reviewStatus: scientific_review`. Promotion is a chemistry-reviewer action,
 not an authoring one.

## Deletions (what + why)

- **Five video briefs** (building π orbitals, what a photon does, what makes a
 reaction pericyclic, sigmatropic numbering, and the standalone electrocyclic
 closure brief). Replaced by the five retained briefs plus static assets; each
 deleted brief covered material the surviving figures and prose already carry.
- **`rxn-cope-hexadiene`** — the degenerate Cope of hexa-1,5-diene. Replaced by
 **`rxn-cope-divinylcyclobutane`**. A degenerate rearrangement renders as a
 figure whose left and right sides are identical, which teaches nothing and
 reads as a rendering bug; the divinylcyclobutane ring expansion gives a visibly
 different product and is strain-driven to completion. The degenerate case is
 still discussed in prose, where it belongs, as the reason the parent Cope is
 invisible.

## Independent chemistry review (run after the coherence pass, before publication)

A separate skeptical-reviewer pass was run over the whole package against RDKit and
PubChem. It confirmed every SMILES, every InChIKey for the five biological
structures, all four selection-rule statements, the [i,j] and electron-count rules,
the endo assignment (by 3D geometry), the meso/chiral claims, and all 22 answer
keys. It found four real errors, all now corrected:

1. **`rxn-cope-divinylcyclobutane` carried the *trans* SMILES** while every word of
 the asset described *cis*. `C(=C)[C@H]1CC[C@@H]1C=C` is (R,R) — chiral, vinyls on
 opposite faces. This mattered: *trans*-1,2-divinylcyclobutane cannot reach the
 [3,3] geometry at all and goes by a diradical to 4-vinylcyclohexene, so the asset
 and its linked question would both have been wrong. Corrected to the meso (R,S)
 isomer `C=C[C@H]1CC[C@H]1C=C`.
2. **The sigmatropic `practice_check` said the methyl migrates.** The room-temperature
 scrambling of 5-methylcyclopentadiene is a [1,5]-*hydrogen* shift; the methyl only
 appears to move because the sp3 carbon does. Every other place in the package said
 hydrogen — the prompt was the sole contradiction. Reworded.
3. **The four-electron thermal case was written as a ring closure**, contradicting this
 chapter's own earlier statement that cyclobutene strain makes *opening* the
 accessible direction. Heating (2E,4E)-hexa-2,4-diene does not give
 trans-3,4-dimethylcyclobutene; the equilibrium sits on the diene side. Restated
 throughout as the ring opening it actually is — `rxn-electrocyclic-4pi-thermal`
 reversed, the trans and cis cyclobutene descriptions rewritten, and the
 "four canonical results" paragraph rebuilt so the thermal four-electron entry is an
 opening while the photochemical one stays a closure (light can drive it uphill).
 The selection rule is unchanged, because forward and reverse share one transition
 state — which the corrected text now says explicitly. **Added**
 `mol-2e4z-hexadiene`, since the cis cyclobutene's conrotatory opening gives the E,Z
 diene and that result was newly named in prose with no figure behind it. The
 `video-conrotatory-vs-disrotatory` storyboard, which labelled the conrotatory
 closure "thermal", was corrected the same way.
4. **"Mirror-image stereochemical outcome"** described the thermal-versus-photochemical
 pair. Those are *diastereomers* (cis vs trans), never enantiomers. Reworded.

Five smaller points from the same pass were also taken: a carbon-count slip in the
pentadiene alt text, a two-versus-three-carbon slip in the prephenate side chain, a
parenthetical noting that the literature writes the 1,3-dipolar cycloaddition as
[3+2] rather than this chapter's electron-count [4+2], a softening of the
chorismate-mutase claim (the entropy-versus-electrostatics split is still argued),
and a fix to a storyboard beat that said to freeze four carbons when only the central
two are stationary.

## Corrections made during this pass (not category-driven, but recorded)

- `nuggets[8]` and `assets` (`rxn-cope-divinylcyclobutane`) claimed a chair-like
 transition state for the divinylcyclobutane Cope. The four-membered ring tethers
 the two arms too closely to reach a chair; that rearrangement goes through a
 **boat-like** transition state. Corrected in both places, and the general
 statement now reads as a preference that a ring can override.
- `nuggets[4].text.expanded` contained a self-contradicting sentence ("opposite
 motions" followed by naming disrotatory twice). Rewritten to state what is
 actually constant across the four canonical results: cis always comes from
 disrotatory closure *for these substrates*, while the pairing between conditions
 and product label is not constant — the rule predicts a motion, never a label.
