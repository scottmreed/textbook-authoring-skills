# Coherence pass — epoxides
Date: 2026-07-31

Scope of this run: the package already had concepts, nuggets, assets and a video
brief; what was added is `question_sets[]` (8 surfaced + 8 staged variants). This
pass therefore focuses on what the new homework forces back onto the earlier
categories.

## Questions → text/figures

- **Changed.** `epox-acid-opening-order` and its variant ask the student to place
 the final proton loss in sequence, and `nugget-acid-opening` did not teach it.
 Both surfaces stopped after "a weak nucleophile then attacks", which leaves the
 product as an oxonium ion and never explains why the acid is a *catalyst*
 rather than a reagent. The question was kept and the **nugget was deepened** in
 both the `standard` and `expanded` tiers: activate, attack, then neutralize,
 with the regeneration of the catalyst stated explicitly. This is the intended
 direction of the rule — deepen the text rather than soften the question.
- **Changed.** `epox-basic-opening-true-v2` uses sodium azide, which the chapter
 never names. Rather than add a reagent list the chapter does not otherwise
 need, the *stem* now glosses it ("a strong nucleophile … with no acid
 present"), so the item tests the mechanism rather than reagent recall.
- **No change needed** for the other six parents: each maps onto a claim its
 nugget already makes. Ring strain as the source of reactivity
 (`nugget-epoxide-strain`), the two preparative routes
 (`nugget-epoxide-synthesis`), attack at the less hindered carbon with inversion
 (`nugget-basic-opening`), inversion at the attacked carbon only
 (`nugget-opening-stereochemistry`), and choosing conditions from the required
 regiochemistry (`nugget-epoxide-synthesis-planning`) are all stated in the text
 at or above the depth the questions ask.

## Questions → deck/reader

- **Deferred.** This is a supplement package over the frozen legacy deck
 `epoxides-structure-and-reactions` (18 slides). The two `structured_reasoning`
 items are the most demanding things in the set and there is no worked
 stereochemical example on a slide. Legacy decks are not edited by this
 pipeline, and the prose in `nugget-opening-stereochemistry` does carry the
 needed reasoning, so the gap is recorded rather than closed. Escalate only if a
 reviewer finds the items unanswerable from the text.

## Videos → text

- **No change.** One brief (`video-epoxide-synthesis-opening`) covers synthesis
 and opening and is referenced by three nuggets. It is unproduced, so it cannot
 yet duplicate or displace any prose. No redundancy to trim.

## Figures → text/questions

- **No change to the asset list.** All five assets remain cited by at least one
 nugget, so none is orphaned. No new figure was authored: every question in this
 set is answerable from text alone by construction (all eight types are verbal
 or tabular — no item depends on reading a rendered structure), which is why the
 set needs no stimulus figures.
- **Known platform limitation, recorded not fixed:** `asset-basic-opening-stereo`
 is a `stereochemistry_conversion`, a type the reader compiler has no block
 mapping for, so it is silently dropped and reaches no student. This is the same
 gap first recorded on ch25 and confirmed at root cause during the ch4 review
 (`_ASSET_TYPE_TO_BLOCK` in `[internal source reference — not in this repo]`).
 It is a compiler change, out of scope for adding a question set.

## Concepts → whole package

- **No change.** Every one of the six concepts now has a nugget, and — for the
 first time — at least one question: strain 1, synthesis 2, basic opening 1,
 acid opening 1, stereochemistry 2, synthesis planning 1. There is no concept
 without an evidence path, and no question or figure whose real subject lacks a
 concept node.

## Crosswalks

- **No change required.** The concept list is unchanged by this pass (nothing
 added or removed), so the existing `textbook_matching` block still covers it.
 The compile regenerated the per-textbook entries for this deck across all 13
 catalogued books; the diff was verified to be purely additive (195 insertions,
 0 deletions), so the known
 `topic-package-textbook-profiles.json` clobber did not occur.

## Deferred (not applied this pass)

- A worked stereochemical example on the legacy deck, motivated by the two
 `structured_reasoning` items (see Questions → deck/reader).
- Making `asset-basic-opening-stereo` render at all — blocked on a reader-compiler
 change.
- The chapter has no figure for the acid/base regiochemical *contrast* that
 `epox-choose-conditions` turns on; the prose carries it. Worth revisiting if a
 review finds the pair hard to follow.

## Deletions (what + why)

- None. Nothing was removed from the package in this pass.
