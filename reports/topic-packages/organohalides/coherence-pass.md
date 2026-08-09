# Coherence pass — organohalides
Date: 2026-07-23

One pass, run after concepts, nuggets, assets, videos, and question sets were drafted
and before compiling. Walked later-authored categories back to earlier ones.

## Questions -> text/figures
- **Change made:** The rank_order variant (`ch10-radical-stability-rank-v2`) asks students to
 order C-H bonds by bond dissociation energy, using approximate kcal/mol values. The radical
 nugget originally taught only the *radical-stability* order, not the equivalent *bond-strength*
 order or any numbers. Deepened `nugget-radical-halogenation` (standard and expanded tiers) to
 state that the weakest C-H yields the most stable radical and to give the approximate BDEs
 (methane ~105, primary ~101, secondary ~98, allylic ~88 kcal/mol). The question is now fully
 supported by the prose rather than only by its own feedback.
- **No change (confident):** Every other question tests something a nugget teaches at the depth
 asked — classification (single_select, categorize_groups, matching_pairs), naming (short_answer),
 chlorination selectivity/product count (numeric, error_repair), radical stability (rank_order),
 allylic products (multi_select), allylic site (hotspot), alcohol-to-halide reagents
 (structure_scaffold), Grignard reduction (synthesis_route), and Grignard/cuprate contrast
 plus coupling sterics (comparison_matrix).

## Questions -> deck/reader
- **No change:** The deck/reader slides are generated from the nuggets, and each question type
 has an upstream nugget that prepares it. No mechanism type was authored that lacks a worked
 example: deliberately no `curved_arrow` (the chapter's signature mechanism is a radical chain,
 which uses single-electron fishhook arrows the two-electron arrow tool does not model), and no
 `reaction_coordinate_reasoning` (per the science-review lesson that multistep ionic profiles
 get rejected — the energetics here are carried in prose). Structure is covered by
 `structure_scaffold`; the mechanism/electron-flow family is represented by `error_repair`.

## Videos -> text
- **No change:** The three video briefs (radical chain, allylic resonance, Grignard polarity
 reversal) visualize processes the prose describes rather than duplicating a paragraph. Each
 is the better medium for its content (stepwise electron flow, delocalization, charge inversion).

## Figures -> text/questions
- **No change:** All 17 molecule assets are cited by at least one nugget or video (verified: zero
 orphans). No figure is unreferenced, and no nugget describes a structure that lacks a figure.
 Benzyl bromide, bromobenzene, and the radical species appear only inside question options as
 SMILES/text, which is appropriate — they do not need standalone chapter figures.

## Concepts -> whole package
- **No change:** All 7 concepts have a nugget (1:1), supporting figures, and at least one question
 (verified: zero concepts without a question). No question or figure has a subject lacking a
 concept node.

## Crosswalks
- **No change needed beyond authoring:** The final concept list (7) was fixed before crosswalks
 were written. Explicit overrides are supplied for all 13 catalogued books. McMurry 6e,
 Fundamentals 6e, and OpenStax map 1:1 to their ch10 "Organohalides"; texts that fold halide
 structure into a combined substitution chapter (Wade ch6, Smith ch7, the Loudon and Forsey
 alkyl-halide chapters) or into radical/organometallic chapters (Klein ch11, Clayden ch9,
 Brown ch8) are mapped to the closest single chapter with a note; the condensed Essential text
 is overridden to an empty chapter list with a note, since it has no standalone match. Verified
 the compiled mapping resolves McMurry to ch10 at confidence 1.0 (not a generic term match).

## Deferred (not applied this pass)
- None.

## Deletions (what + why)
- None. (During drafting, before this pass, the initial `comparison_matrix` chlorination-vs-
 bromination question and a Gilman-coupling `synthesis_route` were reassigned so that every
 variant keeps its parent's concept_slug and all 7 concepts carry a question; that was a
 pre-pass authoring decision, not a coherence-pass deletion.)
