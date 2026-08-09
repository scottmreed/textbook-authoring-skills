# Coherence pass — carbonyl-alpha-substitution
Date: 2026-07-29

## Questions → text/figures
- `ch22-enol-attack-site` (and v2) lean on the oxocarbenium stabilization argument; verified `nugget-enols-as-nucleophiles` teaches it explicitly in the standard tier, not just expanded. No change.
- `ch22-halogenation-profile` (reaction_coordinate_reasoning) embeds its own two-step profile; the chapter deliberately ships **no standalone reaction-coordinate figure** per the 2026-07-23 science-review lesson (RC diagrams only for clean, simple reactions). The rate-law reasoning the question needs is carried in `nugget-alpha-halogenation` prose. No change.
- `ch22-kinetic-enolate` shows both regioisomeric enolate structures in its options; `nugget-enolate-formation-bases` describes both in prose and `mol-2-methylcyclohexanone` shows the substrate. A dedicated two-enolate comparison figure was considered and deferred (see Deferred). No question softened.
- `ch22-pka-estimate`/v2 and `ch22-rank-alpha-acidity`/v2 use exactly the pKa anchors the acidity nugget states (9/11/13/17/19/25/30, alkane ~50). Checked value-by-value for consistency between hints and nugget prose. No change.
- RDKit validation: all 60 SMILES in assets/questions parse; every keto/enol pair confirmed as same-formula constitutional isomers; distractor formulas (cyclohexanol, gem-diol, propan-1-ol) differ exactly as their wrong-answer explanations claim; both curved-arrow site indices verified against RDKit atom ordering.

## Questions → deck/reader
- Every question type used has upstream preparation: curved_arrow is rehearsed by the enolate-alkylation nugget + (deferred) video storyboard; rank_order by the pKa ladder; synthesis_route by the two roadmap figures with step notes; error_repair by the halide-scope trouble spots. No gap requiring a new slide.
- Two nugget `practice_check`s intentionally parallel *staged v2 variants* (nugget-malonic's 3-phenylpropanoic plan ↔ `ch22-malonic-route-v2`; nugget-acetoacetic's 2-hexanone ↔ `ch22-acetoacetic-outcomes-v2`). Variants are drafts that never appear in the default HW set, so this is reinforcement rather than an answer leak; parents use different chemistry (pentanoic acid; origin-of-atoms statements). Accepted deliberately.

## Videos → text
- All three briefs are deferred (electron-flow/resonance/cyclic-TS animations the chalk pipeline cannot draw — same deferral class as ch12–21). Each brief's content is deliberately duplicated in its nugget so the reader is complete without the video; production_note on each records the deferral and the accessibility requirements for eventual production. No trimming.

## Figures → text/questions
- No orphans: all 21 assets are cited by at least one nugget (checked programmatically at build time); roadmaps additionally back the two synthesis_route questions.
- `mol-ethyl-acetate` was added during authoring specifically so the acidity nugget's ester rung has a visible structure — the pKa ladder was otherwise the only prose-only comparison. (Additive change made in this pass's spirit before compile.)

## Concepts → whole package
- All 10 concepts have: a nugget, ≥1 figure path, and ≥1 question; no concept is assessed only by structure_scaffold (build-time check). `enols-as-nucleophiles` carries a single question pair by design — its mechanism content is also exercised indirectly by the halogenation and ledger questions.
- Prerequisite chain forms a DAG rooted at keto-enol-tautomerism; verified all prereq slugs are in-package.

## Crosswalks
- All 13 catalogued textbooks mapped against `backend/app/data/textbook_catalog.json` chapter titles copied verbatim (including Smith's "α-Carbon" with the Greek letter). Two honest empty overrides with notes: mcmurry-fundamentals-6e (no dedicated alpha-substitution chapter in the catalogued list) and bruice-essential (catalogued list ends at ch16). Merged-chapter notes added for Klein, Wade 5e/9e, Loudon, Brown/Foote, Forsey; Clayden mapped to both ch19 and ch23 with the acylation-half caveat.

## Deferred (not applied this pass)
- A dedicated side-by-side figure of the kinetic vs thermodynamic enolates of 2-methylcyclohexanone (the question options already render both structures; add as a teaching figure if the science review asks).
- All three video briefs (production_status: deferred, recorded per-brief).
- QM9S/IR-style spectroscopy content: this chapter has no spectroscopy section by design (McMurry ch22 has none either).

## Deletions (what + why)
- None. No orphan assets or unreachable concepts were produced, so nothing needed removal.
