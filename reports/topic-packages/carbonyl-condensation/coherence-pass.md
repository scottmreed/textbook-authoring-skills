# Coherence pass — carbonyl-condensation
Date: 2026-07-29

Single pass, run after concepts, nuggets, assets, video briefs and question sets
were drafted and before the first compile. Every category answered; three prose
changes applied, no deletions.

## Questions → text/figures

**Three gaps found and closed by deepening the prose, not by softening the question.**

- `ch23-claisen-full-equivalent-v2` asks the student to name the side reaction by
 which a mismatched alkoxide alters an ester. The Claisen nugget described the
 exchange ("sodium methoxide added to an ethyl ester will attack it and exchange
 the alkoxy group") but never named **transesterification**, and never said why
 basicity is not the discriminator — which is exactly the distractor the question
 offers. Expanded tier of `nugget-claisen-condensation` now names the reaction,
 attributes it to the alkoxide's nucleophilicity, and states that methanol and
 ethanol both sit near pKa 16 so the two bases are equally basic.
- `ch23-addition-vs-dehydration-v2` grades a row on "passes through a carbocation
 at the beta carbon". The dehydration nugget covered E1cb fully but disposed of
 the acid route in one clause ("the familiar route of protonating the hydroxyl and
 losing water") without ever naming the cation. Expanded tier of
 `nugget-aldol-condensation-dehydration` now walks the E1 route explicitly and
 contrasts the two oppositely charged intermediates.
- `ch23-rank-michael-donors` (and its variant) requires ordering a ketone-activated
 position above an ester-activated one, at both the doubly and singly activated
 levels, and the v2 requires knowing where an alcohol's O-H falls relative to the
 donors. The Michael nugget listed the three donor pKa values but gave no reason
 for their order and no O-H anchor. Expanded tier of `nugget-michael-reaction` now
 explains why an ester is the weaker activator (its second oxygen already donates
 into the carbonyl) and sets the whole ladder against ethanol at 16, which is also
 the line that decides which compounds a catalytic alkoxide can deprotonate.

Checked and confirmed adequate without change: the ring-size counting rule
(`nugget-dieckmann-cyclization`, `nugget-intramolecular-aldol`) matches what
`ch23-dieckmann-ring-size` and `ch23-match-diketone-to-ring` ask; the mixed-aldol
product counts of four and two are both stated outright in
`nugget-mixed-aldol-selectivity`; the "at least two alpha hydrogens" requirement
that `ch23-flawed-claisen` turns on is stated in the Claisen nugget; and the
three-disconnection retrosynthesis that `ch23-robinson-retrosynthesis` grades is
written out step by step in `nugget-robinson-annulation`.

No question needed a figure that does not exist — every structural question either
carries its own option structures or names compounds the asset list already draws.

## Questions → deck/reader

Every question type used has a worked treatment upstream, with one recorded
exception. Both `curved_arrow` items ask only for the single bond-forming attack,
and both nuggets state that attack in words at the atom level ("the enolate's alpha
carbon attacks the carbonyl carbon of a second molecule"; "that enolate's central
carbon attacks the acceptor's beta carbon"). The `bond_change_ledger` item is
prepared by the atom-by-atom trace in `nugget-aldol-reaction`.

**Exception, recorded not fixed:** `reaction_coordinate_reasoning` requires the
skill of measuring each barrier from its own preceding valley rather than from the
diagram's left edge. This chapter does not teach profile-reading; it is prior-chapter
material (`overview-of-organic-reactions`), and the chapter's own contribution —
coupling an unfavorable addition to an irreversible dehydration — is fully carried
by `nugget-aldol-condensation-dehydration`. The hint ladder on both profile items
teaches the measurement rule directly. Same posture as ch22.

## Videos → text

No redundancy to trim: all five briefs are deferred (electron-flow and multi-stage
mechanism animations, which the chalk pipeline cannot produce), so nothing competes
with the prose for the same content. Each `production_note` names the nugget and
figures that carry the content in the reader today.

## Figures → text/questions

Zero orphans — the build script fails if any asset is unreferenced by a nugget, and
all 26 are cited. Conversely, every nugget that describes a spatial or structural
idea has figures attached: the four ring-size figures under
`nugget-intramolecular-aldol`, and the four-figure donor/adduct/product sequence
under `nugget-robinson-annulation`.

**Deliberate deviation from the ch22 asset mix, recorded here rather than as a
deletion:** no `synthesis_roadmap` assets were authored, although the Claisen,
Dieckmann, Stork and Robinson sections are exactly the multi-step sequences that
would normally get one. The ch22 review (rec-002) verified that roadmap assets
compile to empty-URL image blocks and render as nothing in the reader, and that the
`long_description` fallback is also dropped (rec-003) — so a roadmap would have been
an invisible figure with an unreachable description. Each sequence is instead carried
by a molecule asset per species, all of which render, plus the ordered prose. Revisit
if the roadmap renderer is fixed.

## Concepts → whole package

All ten concepts carry at least one nugget, at least one asset, and at least one
question; the build script enforces this and passes. No concept is assessed only by
`structure_scaffold` (the ch16 finding): the two scaffold items sit on
`aldol-reaction` and `dieckmann-cyclization`, which also carry four and two other
items respectively.

Reviewed for the reverse gap — a question or figure whose real subject has no concept
node — and found one borderline case: **mixed Claisen condensations** (ethyl formate,
diethyl carbonate, ethyl benzoate as non-enolizable ester partners) appear in
`nugget-claisen-condensation` and in the concept-1 sorter, without a node of their own.
Left as a sub-topic of `claisen-condensation` rather than promoted, because the
selectivity principle it illustrates is already a node
(`mixed-aldol-selectivity`) and duplicating it would give two nodes with one shared
evidence path. Recorded so a reviewer can overrule.

## Crosswalks

Concept list is unchanged since it was authored — nothing was added or removed by
this pass — so the crosswalks still cover it. All thirteen catalogued textbooks carry
an explicit override checked against the actual catalogued chapter titles, including
two honest empty mappings (Fundamentals 6e, Bruice Essential) where no corresponding
chapter exists, and two split mappings (Clayden 1e/2e, chapters 10 and 23). The
adjacent-topic notes are written from this chapter's side: where ch22's package said a
merged chapter's *earlier* sections belong to alpha-substitution, this package says its
*later* sections belong here.

## Deferred (not applied this pass)

- Mechanism step-through figure sequences for the Claisen and Robinson stages — no
 such asset kind is delivered to the reader today (ch22 rec-004).
- A pKa ladder figure for the donor ordering; the values are now all in prose
 (ch22 rec-013).
- Reader non-delivery of authored `practice_check` (10) and `long_description` (26)
 content — platform gap, identical in ch21 and ch22 (ch22 rec-003).
- `structure_scaffold` blank canvas has no non-visual or non-pointer alternative
 (standing platform ticket, ch22 rec-010).

## Deletions (what + why)

None. Nothing authored in steps 2–5 was removed; the three changes this pass made
were additions to existing prose. The one thing *not* authored — synthesis roadmap
figures — is recorded under "Figures" above with its reason, since it was a decision
taken during authoring rather than a deletion made here.
