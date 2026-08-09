# Coherence pass — alkynes-organic-synthesis
Date: 2026-07-22

One pass, run after concepts/nuggets/figures/videos/questions were drafted and
before compiling. Three changes applied, three items deferred, no deletions.

## Questions → text/figures

- **Applied — `ch9-degrees-unsaturation` had no text behind it.** The question
 asks students to compute (2C + 2 - H) / 2 for C5H8, and its variant for C7H10,
 but `nugget-alkyne-structure` never introduced degrees of unsaturation at all;
 the prose went from orbital mixing straight to bond length. Rather than soften
 the question, the nugget gained the formula and the "a triple bond is worth
 two" point across all three text tiers, plus a third learning objective. The
 expanded tier also works the C5H8 and C7H10 cases the two questions use.
- **Applied — `ch9-acetylide-sn2-arrow` asked for arrow-pushing the prose never
 modeled.** `nugget-acetylide-alkylation` described the SN2 correctly in words
 ("approaches from the side opposite the halide") but never named an electron
 source or sink, which is the exact vocabulary the question grades. The
 expanded tier now walks both arrows explicitly, names which atom the
 bond-forming arrow points at (the carbon, never the halogen), and states why
 the reverse arrow is invalid — the two errors the question's distractors
 encode.
- **No change — the other twelve surfaced questions.** Each was checked against
 its nugget at the depth asked: the two hydration questions against the enol
 tautomerization paragraph, all three reduction questions against the
 three-conditions paragraph, both acidity questions against the pKa 25/44/60
 and ammonia-38 numbers, the energy-profile question against the "tall first
 barrier, shallow vinyl cation well" sentence, and `ch9-hbr-markovnikov`
 against the geminal-dihalide paragraph that its distractor draws on. No figure
 is missing for any of them; every structure a question needs is carried in its
 own `student_config`.

## Questions → deck/reader

- **No slide gap, and the frozen-deck rule did not bind.** Worth recording why:
 the legacy 41-slide `alkynes-structure-and-reactions` deck is untouched at its
 own slug, and this package compiles a *new* deck at `alkynes-organic-synthesis`
 (the same supersede-by-new-slug pattern used for ch7 and ch8). Because that
 deck is generated from the nuggets, the two text additions above become slides
 automatically — "add a slide" and "deepen a nugget" are the same action here,
 so nothing had to be escalated for permission.

## Videos → text

- **No change, no trims.** All four briefs were checked for redundancy against
 the prose that now exists. `video-alkyne-orbitals` overlaps
 `nugget-alkyne-structure` in content but not in medium: the prose asserts the
 two pi clouds superimpose into a cylinder, the video is the only place that
 shows it happening. Same verdict for `video-three-reductions` (the prose
 lists three outcomes, the video makes the one-substrate-three-arrows shape
 visible) and `video-chain-extension` (the only place the retrosynthetic
 direction is run backwards on screen). `video-hydration-fork` is the closest
 call — the hydration nugget already contrasts both routes thoroughly — but it
 is kept because it is the only asset that shows both enols tautomerizing.

## Figures → text/questions

- **No orphans.** Verified mechanically: every one of the 18 assets is cited by
 at least one nugget, and every concept has at least one figure. Nothing to
 delete.
- **Deferred — the cylindrical pi cloud has no figure.**
 `nugget-alkyne-structure` describes a spatial idea (two perpendicular pi
 bonds superimposing into a cylinder) that words carry badly and an
 `orbital_overlay` asset should carry. `orbital_overlay` is an allowed asset
 type, but no topic package in the repo has ever authored one, so there is no
 proven `spec` shape to copy and inventing one would ship an unrenderable
 figure. `video-alkyne-orbitals` covers the same ground in the interim.

## Concepts → whole package

- **No change.** All seven concepts have a nugget, at least one figure, and at
 least one surfaced question — no concept node without an evidence path, so
 mastery gating in the homework creator has something to key on for each.
 Question distribution is 1–3 per concept; `alkyne-nomenclature` has the single
 thinnest coverage (one `short_answer`), which is proportionate to its weight
 in the chapter.
- No question or figure turned out to have a subject with no concept node.
 Degrees of unsaturation is the one candidate — it is a tool rather than a
 chapter concept, and it now sits inside `alkyne-structure-and-bonding` where
 the numeric questions already point.

## Crosswalks

- **Applied — the auto-matcher was mapping five textbooks to the wrong
 chapter.** This row was supposed to be a re-check after concept churn, but
 running it exposed a pre-existing authoring error: the original `terms` list
 included generic words ("introduction", "synthesis", "reduction", "acidity"),
 and the deterministic title matcher scored those against unrelated chapter
 titles. It produced Wade → ch 1 ("Introduction and Review"), Loudon → ch 4
 ("Introduction to Alkenes"), Klein → ch 12 (should be 10), and both Clayden
 editions → ch 37 ("reduction"), each at high confidence and silently marked
 `matched`. Fix: `terms` narrowed to alkyne-specific tokens, and explicit
 `overrides` authored for all 13 catalogued textbooks against the real chapter
 titles in `backend/app/data/textbook_catalog.json`.
- Loudon 6e and both Clayden editions genuinely have **no** dedicated alkyne
 chapter. They are now overridden to an empty chapter list with a note saying
 the coverage is distributed and must be mapped at section level before
 publishing — an honest gap rather than a confident wrong number.
- All 13 books now resolve as `explicit`. mcmurry (ch 8) and openstax (ch 9)
 are both present, satisfying the Definition of Done. **Note for the skill:**
 the DoD line says "mcmurry + loudon5e crosswalks present", but the catalog
 ships `loudon-organic-chemistry-6e`, not 5e — and for this chapter the honest
 Loudon answer is "distributed, no chapter". That DoD wording is stale.

## Deferred (not applied this pass)

1. `orbital_overlay` figure for the cylindrical pi cloud — no established spec
 shape in the repo; needs the first authored example before this chapter can
 have one.
2. All four videos are briefs only; none has been rendered. Recorded as a
 deferral rather than dropped, per step 4.
3. Section-level Loudon and Clayden mapping, which needs a source neither the
 catalog nor this package carries.

## Deletions (what + why)

None. No asset, nugget, concept, or question was removed. The two candidates
considered were `video-hydration-fork` (kept: it is the only asset showing both
tautomerizations) and the `mol-propene` / `mol-propane` comparison molecules
(kept: authored for the acidity nugget, and the pass found `ch9-acidity-rank`
now uses the same two structures as ranking cards, so they earn their place
twice).
