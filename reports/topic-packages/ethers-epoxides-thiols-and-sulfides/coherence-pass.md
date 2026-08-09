# Coherence pass — ethers-epoxides-thiols-and-sulfides
Date: 2026-07-28

## Questions → text/figures
- Verified every answer key is taught at depth by a nugget: Williamson disconnection rules (nugget-williamson-synthesis), cleavage SN2-at-methyl vs SN1-at-tertiary and the aryl-bond survival rule (nugget-acidic-ether-cleavage), acid vs base regiochemistry with both product names spelled out (nuggets 6–7), the sulfur oxidation ladder with explicit stoichiometry (nugget-sulfides-oxidation), thiol pKa values 10.6/16 (nugget-thiols-disulfides), crown m-crown-n decoding (nugget-crown-ethers), halohydrin route naming (nugget-epoxide-preparation).
- `ts_character` (Hammond) asked by both reaction_coordinate_reasoning questions is taught in the ch16 EAS nugget, not re-taught here; hints carry the postulate locally. No change to prose — duplicating Hammond in this chapter would be redundant with the immediately preceding chapters.
- Change made: both RCR `accessible_description` texts rewritten answer-neutrally after the compile-time leak guard flagged "exergonic"/"early".

## Questions → deck/reader
- Each question type used has an upstream worked pattern: the boiling-point ranking mirrors the Et₂O/pentane/1-butanol comparison in the ether-properties prose; the bond ledger and curved arrow track the SN2 opening narrated step by step in nugget-base-epoxide-opening; error_repair misconceptions are the same two trouble_spots listed on acid-catalyzed-epoxide-opening. No missing-slide gap found.

## Videos → text
- One brief (two-branch regiochemistry animation), production deferred (chalk-pipeline curved-arrow class, same as ch16). The regiochemistry content is fully carried by prose + the two product molecule figures, so no learner-facing gap while deferred.

## Figures → text/questions
- No orphan assets: all 22 assets are cited by at least one nugget's asset_ids; mol-22-dimethyloxirane and the two regio product figures are additionally load-bearing for four question families.
- No change: reaction coordinate figure limited to the single-step base opening (one clean step — the reviewer-approved class); acid opening deliberately carries its energetics in prose only.

## Concepts → whole package
- Every concept has ≥1 nugget, ≥1 asset, and ≥1 surfaced question. Thinnest coverage: crown-ethers (1 numeric pair) and thiols-and-disulfides (1 structured_reasoning pair) — both depth-appropriate for enrichment/standard concepts.
- No concept is assessed ONLY by structure_scaffold (ch16 lesson): epoxide-preparation also carries short_answer.
- Concept slugs deliberately avoid collision with the pre-existing narrow `epoxides` package (epoxide-structure-strain, epoxide-synthesis, epoxide-basic-opening, epoxide-acid-opening…): this package uses epoxide-preparation-and-ring-strain / acid-catalyzed-epoxide-opening / base-promoted-epoxide-opening, since the compiler registers concept slugs first-wins across packages.

## Crosswalks
- mcmurry-6e / openstax = ch18, verified. loudon-6e = ch11, high confidence. FLAGGED for TOC verification in the override notes: mcmurry-fundamentals (8?), klein-4e (13/14?), wade-9e/5e (14?), smith-7e (9?), brown-foote-8e (11?), forsey-oer (10?), bruice-essential (10?). Clayden 1e/2e intentionally mapped to empty chapter lists with notes (material is distributed; no correct single target).

## Deferred (not applied this pass)
- The legacy `epoxides` topic package overlaps three concepts of this chapter; consolidating or retiring it is a separate decision for the maintainer (its deck `epoxides-structure-and-reactions` remains untouched).
- matching_pairs v2 items span thiol interconversions while carrying the parent's sulfides concept slug (compiler forces variants to keep the parent concept) — same accepted pattern as the two ch16 variants.
- Anisole/butyl-methyl-ether cleavage single_selects include a text-only "No reaction" option among illustrated options; it is a distractor, not the key, so it is not the ch15 lone-illustrated-key tell. Left as-is.

## Deletions (what + why)
- None. (One value edit: concept difficulty "enrichment" → "advanced" for crown ethers; the schema's depth vocabulary is core/standard/advanced.)
