# Chapter-review finding schema

The four persona subagents return the **same** JSON envelope so their findings
merge and diff cleanly. Validate every return with the proprietary findings
validator (not in this repo) before synthesis; re-request a malformed return once, then record it as an
`open_question` if it still fails.

## Persona output envelope

```json
{
 "persona": "Accessibility Persona",
 "persona_version": "1.0.0",
 "chapter_id": "alkyl-halide-substitution-and-elimination",
 "chapter_version": "1",
 "model": "<model id the subagent ran on>",
 "summary": "One paragraph: the chapter's state through this persona's lens.",
 "overall_score": 7.4,
 "publication_blockers": ["access-003"],
 "findings": [ /* Finding[] — see below */ ],
 "strengths": ["Concept prerequisites are explicit and correctly ordered."],
 "open_questions": ["Is asset mol-12 meant to be interactive in the reader?"]
}
```

- `persona` — exactly one of: `Organic Chemistry Instructor`,
 `Struggling Student`, `Accessibility Persona`, `Learner with Visual Preference`.
- `overall_score` — 0–10, this persona's holistic read. **Advisory only** — it
 must never be used to average away a blocker (see synthesis rules).
- `publication_blockers` — the `finding_id`s (subset of `findings`) this persona
 considers hard blocks. Empty list is valid and common.

## Finding

```json
{
 "finding_id": "access-003",
 "location": {
 "section_id": "11.3",
 "concept_slug": "sn1-mechanism-and-stereochemistry",
 "asset_id": "mechanism-animation-12",
 "question_slug": "ch11-sn1-energy-profile",
 "nugget_id": "nug-...",
 "anchor_text": "verbatim phrase from the chapter to locate the spot"
 },
 "severity": "high",
 "category": "media-equivalence",
 "observation": "What is wrong or missing, factually.",
 "learner_impact": "Who is affected and how their learning/access degrades.",
 "evidence": "The specific chapter content that grounds this (quote/ids).",
 "recommended_outcome": "What should change — described as a NEED, not a fixed asset.",
 "confidence": 0.91
}
```

### `location` (at least one resolvable anchor required)
Populate whichever of these resolve for the finding; **at least one is
mandatory** so every finding is location-anchored:
`section_id`, `concept_slug`, `nugget_id`, `asset_id`, `question_slug`,
`anchor_text` (a short verbatim quote). A finding with an empty `location`
fails validation.

### `severity` (constrained scale — used for ranking and regression)
- `blocker` — chapter must not publish until fixed (wrong chemistry; a required
 activity is impossible for some learners; an answer is leaked).
- `high` — materially harms learning/access; fix before instructor use.
- `medium` — real improvement; schedule but not blocking.
- `low` — polish.

### `category` (stable identifiers — keep spelling exact for regression diffing)
`chemical-accuracy`, `notation-consistency`, `sequencing`,
`conceptual-support`, `objective-alignment`, `misconception`, `missing-example`,
`assessment-readiness`, `cognitive-load`, `worked-example-gap`,
`retrieval-practice`, `media-equivalence`, `alt-text-quality`,
`keyboard-operability`, `color-motion-only`, `interactive-fallback`,
`figure-accuracy`, `figure-purpose`, `visual-opportunity`, `visual-redundancy`.
Add a new id only when none fit; document it in the persona rubric so the next
run reuses it.

### `recommended_outcome` states a NEED, not a solution
Write "the SN1 stereochemistry is only conveyed by the animation; a
non-animated learner has no equivalent" — **not** "add a GIF." The orchestrator,
not the persona, decides the least-complex intervention that fully addresses the
need (see synthesis rules). Personas may suggest, but must frame as a need.

## Synthesized report schema (orchestrator output)

Written to `reports/topic-packages/<chapter_id>/chapter-review.json` (machine)
and `chapter-review.md` (human, both views). Shape:

```json
{
 "chapter_id": "...",
 "chapter_version": "1",
 "run_at": "ISO-8601",
 "personas": [{ "persona": "...", "persona_version": "...", "model": "...", "overall_score": 7.4 }],
 "publication_readiness": "ready | ready with minor revisions | major revision | blocked",
 "executive_summary": "...",
 "consensus_strengths": ["..."],
 "ranked_recommendations": [
 {
 "rec_id": "rec-001",
 "title": "...",
 "need": "...",
 "chosen_intervention": "sufficient-alt-text | longer-description | structured-chemical-description | static-image-sequence | animation-or-interactive | transcript | keyboard-alternative | text-equivalent | alternate-activity | prose-edit | new-figure | added-practice | instructor-note",
 "rationale": "why this is the least-complex intervention that fully addresses the need",
 "target_surface": "prose | figure | interactive | practice | assessment | instructor-support",
 "severity": "blocker|high|medium|low",
 "source_findings": ["access-003", "visual-007"]
 }
 ],
 "accessibility_blockers": ["..."],
 "visual_opportunities": ["..."],
 "sufficient_as_is": ["places a description is enough — no new asset needed"],
 "disagreements": [
 { "topic": "...", "positions": {"Accessibility Persona": "...", "Learner with Visual Preference": "..."}, "resolution": "orchestrator's call + why" }
 ],
 "regression": { "resolved": [], "unchanged": [], "worsened": [], "new": [] }
}
```

`publication_readiness` is computed, not averaged: **any** persona
`publication_blocker` (or any `blocker`-severity finding) forces at least
`major revision`, and an unresolved required-access blocker forces `blocked`. A
high aggregate `overall_score` can never downgrade this.

## Post-correction extension

When verified errors are corrected in the same workflow, preserve the baseline
fields above and add:

```json
{
 "corrections": {
 "status": "applied-and-verified-without-second-persona-run",
 "post_correction_readiness_estimate": "major revision",
 "estimate_note": "Not a new persona verdict.",
 "applied": [
 {
 "change": "Exact edit made.",
 "resolves": ["access-003"],
 "partially_addresses": []
 }
 ],
 "remaining_high_priority": ["..."],
 "verification": ["exact command — result"]
 }
}
```

Never overwrite the baseline `publication_readiness` after a targeted correction
pass. Only a separate four-persona regression run can issue a new verdict.
