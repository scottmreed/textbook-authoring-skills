# Coherence pass — nuclear-magnetic-resonance-spectroscopy
Date: 2026-07-25

## Questions → text/figures
- **Change:** `ch13-decoupling-propyl` (+v2) tests selective irradiation, which no
 nugget taught. Deepened `nugget-splitting` (expanded tier) with a sentence on
 selective decoupling — irradiating a group collapses the splittings it causes —
 rather than softening the question.
- **Change:** harmonized the "C–H on oxygen/halogen-bearing carbon" ¹H region to
 δ 2.5–4.5 (the value `nugget-shifts-integration` teaches) in
 `ch13-shift-region-matching-v2`, `ch13-downfield-ranking-v2`,
 `ch13-aldehyde-peak-select-v2`, and `ch13-isomer-reasoning-v2`, which had used
 a narrower 3.3–4.5.
- No change otherwise: every question's target fact is taught at the asked depth —
 δ = Hz/MHz with a worked example (Q1), p-xylene/cyclohexane/neopentane signal
 counts (Q2/Q3), full region map including acid and aldehyde windows (Q4/Q5/Q14),
 9:3 integration on methyl pivalate (Q6), J facts and the n + 1 rule (Q7/Q8),
 2-bromopropane equivalence (Q9), 1,1-dichloroethane doublet/quartet (Q10, Q12-v2
 — it is the splitting nugget's practice check), butan-2-one and ester ¹³C values
 (Q13/Q15), TMS (Q16), and both isomer discriminations worked in the strategy
 nugget (Q17).

## Questions → deck/reader
- No change: the deck compiles from the same nuggets, so each question type has an
 upstream worked example (ethyl quartet-triplet, isopropyl doublet-septet, region
 maps, the four-question inventory). The decoupling gap was the one exception and
 was closed in the text (above).

## Videos → text
- No change: the single brief (`video-nuclear-spin-states`) is deferred with a
 production note (spin-state energy-shelf animation is not chalk-producible —
 same category as ch12's spring-model deferral); its content is fully carried by
 `nugget-nmr-theory` prose, so no duplication exists to trim.

## Figures → text/questions
- No change: all 12 molecule assets are referenced by at least one nugget, and
 five also back questions (cyclohexane → Q3; 2-bromopropane → Q9; bromoethane →
 Q8/Q12; 1,1-dichloroethane → Q10/Q12-v2; propanal → Q14). No orphans. Tiny
 molecules carry `show_hydrogens: true` per the review-lessons rule.

## Concepts → whole package
- No change: each of the 7 concepts has a nugget, at least one figure (via its
 nugget), and at least one published question — theory (Q18), chemical shift
 (Q1, Q16), equivalence (Q2, Q3, Q9), shifts+integration (Q4, Q5, Q6, Q12, Q14),
 splitting (Q7, Q8, Q10, Q11), ¹³C/DEPT (Q13, Q15), structure determination (Q17).
 No concept lacks an evidence path; no question targets a missing concept.

## Crosswalks
- No change: concepts were not added or removed during the pass; the 13 explicit
 overrides (mcmurry ×2, openstax, klein, wade ×2, smith 12C, loudon 13,
 brown-foote, clayden ×2, forsey, bruice-essential) still cover the final list.
 Clayden 1e (ch. 11) and Smith 12C are the two lens numbers most worth a human
 spot-check at review time.

## Deferred (not applied this pass)
- `nmr_dynamic_explorer` question type left unused: variable-temperature/exchange
 NMR is not taught in this chapter's prose (and not in the McMurry-level ch13
 scope), so a coalescence question would test untaught content. The existing
 `two-site-exchange-v1` asset remains demo-only.
- Spectrum-trace figures in the reader (rec-001 from the ch12 review): the
 topic-package pipeline still has no spectrum asset kind in
 `ALLOWED_ASSET_TYPES`; spectra ship inside the interactive question types
 (trace assets + peak-diagram configs) instead. Cross-chapter pipeline gap, not
 a ch13 content fix.
- Video brief production (see Videos section).

## Deletions (what + why)
- None.
