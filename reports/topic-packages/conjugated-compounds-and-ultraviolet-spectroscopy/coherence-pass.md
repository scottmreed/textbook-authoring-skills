# Coherence pass — conjugated-compounds-and-ultraviolet-spectroscopy
Date: 2026-07-27

## Questions → text/figures
- **Change made:** `ch14-diene-stability-ranking` breaks the tie between two conjugated
 dienes by double-bond substitution, but nugget-diene-classes originally taught only the
 conjugated > isolated > cumulated ordering. Added one sentence to the expanded tier
 stating the alkyl-substitution increment (internal vs terminal conjugated dienes),
 so the question tests something the prose teaches at the asked depth.
- No change otherwise: every fact quizzed is taught — MO counts and bonding/antibonding
 split (nugget-butadiene-mos), λmax values 171/217/258/455 nm and the
 E = 1.196 × 10⁵/λ conversion with the 551 kJ/mol worked value (nugget-uv-spectroscopy),
 the −80 °C/40 °C ratios (nugget-kinetic-thermodynamic), s-cis/s-trans naming and the
 s-trans preference (nuggets 1 and 6), stereospecific syn addition (nugget-diels-alder),
 and the capture-step mechanism for the curved-arrow and error-repair items
 (nugget-allylic-cation-addition).

## Questions → deck/reader
- No change: each question type used has an upstream worked treatment — 1,2-/1,4-product
 construction is walked through carbon by carbon in nugget 3 (prepares the two
 structure_scaffold items and the curved_arrow/error_repair pair), MO filling is worked
 in nugget 2 (prepares the HOMO/LUMO selects and MO counts), the two-step
 protonation-then-capture sequence with relative barrier heights is described in
 nuggets 3–4 (prepares reaction_coordinate_reasoning), and the λ→E conversion is worked
 numerically in nugget 7 (prepares numeric_with_units).

## Videos → text
- No change: the single brief (Diels–Alder in motion) is deferred with a recorded
 production_note (concerted transition-state morph is outside the chalk pipeline, same
 category as ch12's spring-model and ch13's spin-state deferrals). Its content is fully
 carried by nugget-diels-alder prose; no redundant prose was found to trim because the
 video does not exist yet.

## Figures → text/questions
- No change: all 12 molecule assets are cited by at least one nugget (checked
 asset.nugget_ids against nugget.asset_ids) and several also appear as question
 stimuli via structure_smiles. No orphan assets.

## Concepts → whole package
- No change: all 7 concepts have exactly one nugget, at least one figure, and 2–4
 surfaced questions each (3/2/3/3/2/3/3). No concept lacks an evidence path; no
 question or figure lacks a concept node.

## Crosswalks
- No change: explicit overrides cover all 13 catalogued books (chapter numbers taken
 from backend/app/data/textbook_catalog.json titles, not term-matching); compile
 reports 13 mappings and an empty verification_required list. mcmurry-6e, fundamentals,
 and openstax all point at ch 14 "Conjugated Compounds and Ultraviolet Spectroscopy".

## Deferred (not applied this pass)
- A `conformational_energy_profile` figure for the butadiene s-trans ↔ s-cis torsion
 (~12 kJ/mol difference) would carry the conformational idea nuggets 1 and 6 describe
 in words. Deferred: ch12/ch13 review precedent is molecule-only asset sets, and
 authoring a new asset type at the end of the pass risks the blank-render spec-shape
 failure mode (science-review lesson 5). The prose plus practice_check carries the
 content; motivated by questions ch14-scis-conformation / ch14-unreactive-diene.
- An endo/exo question (endo rule is taught in nugget 6's expanded tier) — no released
 question type renders a bicyclic endo/exo choice cleanly without a bespoke figure;
 revisit if a suitable figure kind lands.

## Deletions (what + why)
- None.
