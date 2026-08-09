# Coherence pass — alcohols-and-phenols
Date: 2026-07-28
Author: agent (produce-organic-chapter pipeline, step 6)

One pass, walked later-authored → earlier-authored.

## Questions → text/figures
- No change (confident). Every surfaced question tests a concept the prose teaches at the depth asked:
 reagent selection and NaBH₄ vs LiAlH₄ (nugget-reduction); Grignard product class + equivalents
 (nugget-grignard); alcohol/phenol acidity and substituent effects (nugget-acidity,
 nugget-phenol-acidity-substituents); classification and alcohol-vs-phenol (nugget-structure-naming);
 oxidation level vs class and mild-vs-strong oxidant (nugget-oxidation); halide/dehydration reagents
 (nugget-dehydration-halides); phenol EAS activation and quinone formation (nugget-phenol-reactions).
 No question needs a figure that does not exist — the two structure_scaffold items are answered from the
 named substrate (cyclohexanone→cyclohexanol; propanal→1-propanol), and every option-bearing question
 that benefits from a structure carries an inline `structure_smiles`.

## Questions → deck/reader
- No change (confident). Every question type used has an upstream worked example in a nugget. Deliberately
 used NO mechanism-drawing types (curved_arrow, bond_change_ledger): per the 2026-07-23 science-review
 lessons, the ionic mechanisms of this chapter (acid dehydration, HX substitution, Grignard/hydride
 addition) are multistep and are carried in prose + molecule figures rather than reaction-coordinate or
 arrow-drawing assets. structure_scaffold is the structure/mechanism-adjacent type that the chemistry
 supports cleanly (draw a reduction product), satisfying the DoD "at least one structure type."

## Videos → text
- No change. The 3 video briefs (Grignard addition, oxidation levels, phenol-acidity resonance) each
 reinforce a nugget that also carries the content in prose; this is intended redundancy for a motion
 concept, not duplication to trim. All three are production_status: deferred (curved-arrow/electron-flow
 animations outside the molecule-video-creator chalk pipeline), with the accessibility caption/transcript
 requirement recorded on each brief.

## Figures → text/questions
- No change. All 7 molecule assets are cited by ≥1 nugget (no orphans): ethanol (structure, H-bonding),
 phenol (structure, acidity), p-nitrophenol (substituent acidity), cyclohexanol (reduction, oxidation),
 2-methyl-2-butanol (oxidation, dehydration), p-benzoquinone (phenol reactions), TBS ether (protection).
 Small molecules (ethanol) carry `rdkit_options.show_hydrogens: true` per the tiny-molecule render lesson.
 No RC/energy-profile assets were authored (see Questions → deck/reader).

## Concepts → whole package
- No change to the concept list. All 9 concepts have ≥1 nugget; concept 3 (acidity) has 2. Every concept
 has a nugget and a figure. Two concepts intentionally have no dedicated question — hydrogen-bonding-and-
 properties (concept 2) and protection-as-silyl-ethers (concept 9, advanced/optional). This is consistent
 with the [internal PRD reference — not in this repo] rule "1–2 questions per *suitable* type spread across concepts," not one question per
 concept; both concepts still carry a nugget with a practice_check and a figure, so mastery-gating has an
 evidence path. No question or figure has a subject lacking a concept node.

## Crosswalks
- No change needed. The final 9-concept list is unchanged from authoring, so the crosswalks stand. All 13
 catalogued textbooks map with status=explicit, confidence 1.0, to the correct chapter(s): McMurry 6e /
 Fundamentals 6e / OpenStax → ch 17 "Alcohols and Phenols"; Klein → 13; Wade 5e/9e → 10+11; Smith → 9;
 Loudon → 12 (Alcohols and Ethers; phenol specifics live with aromatic chemistry, noted); Brown/Foote →
 10+22; Forsey OER → 10; Bruice Essential → 11; Clayden 1e/2e → empty (mechanism-first organization, no
 dedicated chapter), each with an explanatory note per the DoD guidance to override rather than leave a
 wrong number.

## Deferred (not applied this pass)
- Videos: production of all 3 briefs deferred (motion-mechanism animations; chalk pipeline cannot render).
- Seeding to the DB and flipping `available: true`: deferred pending maintainer approval (per skill).

## Deletions (what + why)
- None this pass. (During authoring, four variant questions were re-scoped so each keeps its parent's
 concept_slug per the variant contract; nothing was removed from the package.)
