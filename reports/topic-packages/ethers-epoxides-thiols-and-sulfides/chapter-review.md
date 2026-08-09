# Chapter review — Ethers and Epoxides; Thiols and Sulfides (v1)

Run: 2026-07-28 · Four personas (Instructor 7.9 / Student 6.8 / Accessibility 6.8 / Visual 6.4)

## Baseline verdict: **BLOCKED**

Three blockers force this (computed, not averaged):

1. **instr-001 (chemical-accuracy)** — the asset titled *cis*-2,3-dimethyloxirane encodes `C[C@H]1O[C@@H]1C`, RDKit-verified as the chiral (2R,3R)-**trans** epoxide; the cis isomer is the meso (2R,3S) compound. The figure teaches the opposite of the syn-epoxidation lesson it carries. *(Orchestrator independently re-verified with RDKit: authored SMILES is R,R and not meso; `C[C@H]1O[C@H]1C` is meso.)*
2. **access-001 (media-equivalence)** — both reaction_coordinate_reasoning questions ask for conclusions read off a plotted curve whose `accessible_description` omits the relative energies; unanswerable non-visually.
3. **access-002 (interactive-fallback)** — both blank-canvas structure_scaffold items have no vision/pointer-independent input path (standing platform ticket; mitigated: no concept is assessed drawing-only).

Zero wrong answer keys: the Instructor verified all 38 keys, including curved-arrow site maps and hotspot atom indices against RDKit numbering.

## Compact editorial view (ranked)

| Rec | Sev | What | Decision |
|---|---|---|---|
| rec-001 | blocker | cis-epoxide SMILES is trans | Fix SMILES to meso (applied) |
| rec-002 | blocker | RCR questions withhold curve data from AT users | Neutral data readout in accessible_description (applied) |
| rec-003 | blocker | Drawing items have no non-pointer path | Platform ticket; content mitigation already in place (open) |
| rec-004 | high | No keyboard path for arrows/hotspots | Platform ticket (open) |
| rec-005 | high | Central acid/base contrast has no delivered visual (3 personas converged) | Co-locate both product figures in both opening sections (applied); video remains deferred |
| rec-006 | high | Hammond graded but not taught | Anchor paragraph in base-opening nugget (applied) |
| rec-007 | high | Bromohydrin figure can't show "anti" | Swap to stereodefined trans-2-bromocyclohexanol (applied) |
| rec-008 | medium | BP rankings contradict literature (pentane 36 °C > Et₂O 34.6 °C) | Replace alkane cards with butane / pentane-vs-C5-ether triples; rewrite feedback (applied) |
| rec-009 | medium | Distractor name has impossible locants | Rename to 3-methoxy-2-methyl-2-butanol (applied) |
| rec-010 | medium | Williamson disconnection prose-only; jargon unglossed | Prose gloss applied; two-branch visual → figure backlog |
| rec-011 | medium | Claisen = unglossed jargon | Enrichment framing + plain-language clause (applied) |
| rec-012 | medium | Crown host–guest unassessed/unshown | Recommendation (scope) |
| rec-013 | medium | SN1-like TS prose-only | Recommendation (figure backlog) |
| rec-014 | medium | No in-reader checkpoints (practice_checks not compiled) | Platform ticket (pre-existing) |
| rec-015 | medium | cis-butene "before" never shown | Add cis-2-butene figure (applied) |
| rec-016 | low | "elision", HSAB "harder" | Reworded (applied) |
| rec-017 | low | Video storyboard color-only mid-video | Requirement appended to production_note (applied) |
| rec-018 | low | No sulfur mechanism-level item; SAM unassessed | Recommendation (scope) |
| rec-019 | low | Anisole caption reused across sections | Compiler limitation; caption already dual-purpose (noted) |
| rec-020 | low | Thiol-vs-alcohol table opportunity | Sufficient as is |

## Disagreements retained
- **Text tiers**: Accessibility counts three tiers a strength; Instructor saw only expanded. Resolution: terse/standard ship as `_detail_texts` for the personalization slider; expanded is the default body.
- **Hidden video blocks**: Student = central missing support; Accessibility = cleanly hidden, no silent-media debt. Both true; handled via rec-005 co-location, video stays deferred. Triple placement is compiler-per-linked-nugget behavior, not an authoring error.

## Full evidence view
The complete, schema-valid persona envelopes (33 findings, strengths, open questions) are embedded in [chapter-review.json](chapter-review.json) and preserved verbatim in [persona-envelopes.json](persona-envelopes.json). Notable open platform questions carried forward: whether `accessibility_bundle.accessible_description` is delivered to AT at runtime (ch16 found it was not), keyboard operability of hotspot/arrow/rank/categorize widgets, and hotspot renderer atom-index mapping (orchestrator note: keys were authored against RDKit SMILES-order indices, the mapping proven correct in the ch16 review).

---

## Post-correction record (2026-07-28, same run — not a new persona verdict)

Baseline verdict above is preserved. 12 correction groups applied (full detail in `chapter-review.json → corrections`):

1. **instr-001 (blocker)** — cis-epoxide SMILES → `C[C@H]1O[C@H]1C`; RDKit-verified meso. **Resolved.**
2. **access-001 (blocker)** — both RCR `accessible_description`s now carry a neutral plotted-data readout; pushed directly to the two seeded rows (the seeder hash ignores bundle-only changes — see gotcha below). **Resolved.**
3. instr-004 — ranking triples now unambiguous (butane / pentane as the alkanes); feedback rewritten. **Resolved.**
4. instr-002 — distractor renamed 3-methoxy-2-methyl-2-butanol. **Resolved.**
5. stud-004 (+instr-005) — Hammond postulate taught in the base-opening nugget, both tiers. **Resolved.**
6. visual-005 (+stud-003, instr-006) — bromohydrin figure now stereodefined trans-2-bromocyclohexan-1-ol (CIP-verified trans). **Resolved / partially addresses the step-sequence need.**
7. stud-001/visual-001 — both regio products co-located in both opening sections. **Partially addressed** (full fix = deferred video).
8. visual-004 — cis-2-butene figure added beside the cis-epoxide. **Resolved.**
9. stud-006, stud-005, stud-008 — prose glosses (disconnection, Claisen enrichment framing, elision/HSAB wording). **Resolved.**
10. access-006 — non-color-carrier requirement appended to the video brief's production note. **Resolved.**

**Still open:** access-002 (structure_scaffold input path — platform ticket, mitigated), access-003/004 (widget keyboard paths — platform ticket), deferred regiochemistry video, crown/sulfur assessment-coverage recommendations (rec-012, rec-018).

**Verification:** recompile with `--write-runtime` clean (leak guard passed); profiles snapshot deep-merged (additive, 1937 leaf keys); `tools/topic_packages/tests` 54/54; reseed `updated 1 / unchanged 18 / staged_variants 19` + targeted DB update of the two RCR rows verified by readback; corrected variant configs verified in DB.

**Post-correction estimate: ready with minor revisions** *(not a new persona verdict; assumes access-002 remains tracked platform-side as in prior chapters).*

### Seeder gotcha discovered this run
`question-bank seeder (proprietary toolchain, not in this repo)` change detection hashes slug/prompt/author_state(student_config)/answer_key/grading_rules only — `feedback_bundle` and `accessibility_bundle` changes are invisible, and hash-equal items are skipped entirely. Bundle-only corrections must be pushed to existing rows manually (or a hashed field must change).
