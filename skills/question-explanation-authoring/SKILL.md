---
name: question-explanation-authoring
description: Author specific, chemistry-accurate wrong-answer explanations for ChemIllusion question-type demo fixtures. Use when adding, reviewing, or debugging post-answer feedback, when a demo question only shows a generic "Not quite" message, or when adding a new question type demo fixture.
---

# Question Explanation Authoring

> Distinct from hints ([question-hint-authoring](../question-hint-authoring/SKILL.md)):
> hints are shown *before* an answer, gated, and must never name what's
> right or wrong. Explanations are shown *after* grading, only for a wrong
> or partial submission, and their entire purpose is to say specifically
> what's wrong with **what the student actually entered**.

One small pattern-matching engine for every question type — a fixture
authors a short list of anticipated wrong submissions with a targeted
explanation each, plus one generic fallback. Canonical code: the proprietary
wrong-answer explanation matcher (not in this repo). Wired into
`question_demo_service.grade_demo_attempt`, which appends the matched
explanation to the grader's `feedback_text` when the grading result status is
`"incorrect"` or `"partially_correct"`.

## Fixture shape

```python
"wrong_answer_explanations": [
 {"match": {"selected_option_ids": {"$contains": "b"}},
 "explanation": "Propane (CCC) is a plain alkane — no -OH."},
 {"match": {"selected_option_ids": {"$missing": "a"}},
 "explanation": "Ethanol does have the hydroxyl group — don't leave it out."},
],
"generic_incorrect_explanation": "An alcohol needs a hydroxyl (-OH) bonded to a saturated carbon.",
```

- `match` is a **partial (subset) match** against the student's submission
 dict — every key you list must be present with a matching value,
 recursively. You don't need to specify the whole submission shape, only
 the part that discriminates this particular mistake.
- Two operators work on list-valued submission fields: `{"$contains": id}`
 (the list has this id in it — usually "this wrong thing was picked") and
 `{"$missing": id}` (the list is missing this id — usually "this right
 thing was left out"). Without an operator, a list pattern requires exact
 equality including order — use that for order-sensitive types
 (`rank_order`'s `ordered_ids`). `$contains`/`$missing` also accept a dict
 value (e.g. matching one row of `bond_change_ledger`'s `rows`), but that
 dict is checked by full equality against a list element, not a partial
 match — if the target schema grows a field later, a dict `$contains`
 pattern silently stops matching (falls through to the generic fallback,
 no error) rather than partially matching.
- String leaves compare case-insensitively (`short_answer`'s typed text
 shouldn't need to match your casing).
- Patterns are checked **in order, first match wins** — put the most
 specific/important mistake first.
- Every fixture with a real (non-`"unsupported"`) answer key must set
 `generic_incorrect_explanation` — the fallback for any wrong submission
 none of your patterns anticipated. `walkthrough` (teacher-review only, no
 deterministic key) is the one fixture exempt from this.
- **Few-option rule (≤2 options/categories)**: an explanation is shown after a
 wrong submission, so it may say what's wrong — but when the option space is
 only 2 (a binary categorize, a two-option select), stating the *correct*
 group/option for a missed item hands over the only remaining answer on the
 first miss. Teach the discriminating **criterion** instead ("hydroxide
 carries a full negative charge and lone pairs it can donate — which role fits
 an electron-rich donor?"), never naming the right category. Guarded by
 `test_question_wrong_answer_explanations.py::TestFewOptionFeedbackDoesNotNameTheAnswer`,
 which fails if a ≤2-group categorize explanation names the correct category
 or the generic fallback names any category. (With 3+ options, naming one is
 fine — it doesn't collapse the space.)
- **Chemistry display text**: write formulas as normalized Unicode
 (`R₃C⁺`, `OH⁻`, `H₂O`), the `ensure_chemistry_display_text` canonical form —
 explanation prose renders as plain text with no markup.

## Workflow

1. Start from the fixture's existing `incorrect_response` — write one
 pattern that matches it exactly (or with `$contains`/`$missing`, more
 generally). This is guaranteed reachable and cheap to verify.
2. Think about 1-3 more plausible wrong answers a student might actually
 submit (not just the canned one) and add a pattern per one, each keyed
 to the specific field/value that reveals the misconception — not the
 whole submission. Nested dicts work: `{"cells": {"basicity": {"case_acetate": "yes"}}}`
 matches on just that one cell regardless of what else is in `cells`.
3. Write `generic_incorrect_explanation` — a chemistry-specific fallback
 for this exact question, not a generic "try again."
4. Validate:
 ```bash
 # proprietary toolchain (not in this repo)
 python -m pytest tests/unit/test_services/test_question_wrong_answer_explanations.py -v
 ```
 `TestExplanationCoverage` fails if you forgot the generic fallback, or
 if your `incorrect_response` pattern only reaches the generic message
 (meaning you didn't actually write a targeted pattern for it).
5. Preview: submit the fixture's `incorrect_response` shape through
 `/question-types/{slug}` in the demo gallery (public and anonymous-accessible
 when the question-type-gallery feature flag (not in this repo) is on) and confirm the
 feedback alert shows your specific sentence appended after "Not quite —
 review the prompt." (or the family's equivalent generic prefix).

## Relationship to hints and figures

- [question-hint-authoring](../question-hint-authoring/SKILL.md) — pre-answer
 progressive hints, server-gated, never name the answer.
- [question-figure-authoring](../question-figure-authoring/SKILL.md) — ensures
 the question itself has the figures a student needs to answer it.
- proprietary demo fixture catalogs (not in this repo) — the fixture catalog all three
skills author into.
