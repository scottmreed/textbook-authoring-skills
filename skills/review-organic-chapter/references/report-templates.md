# Synthesized report templates

The orchestrator writes both views into one markdown file
`reports/topic-packages/<chapter_id>/chapter-review.md` (plus the machine
`chapter-review.json` from the schema). Do **not** flatten everything into one
generic list — the two views serve different readers.

---

## Compact editorial view (top of the file)

```markdown
# Chapter review — <Chapter Title> (`<chapter_id>`)

_Reviewed <ISO date> · chapter version <v> · personas: Instructor, Struggling
Student, Accessibility, Visual Preference_

**Publication readiness: <ready | ready with minor revisions | major revision | blocked>**

<one-paragraph executive summary>

### Top blockers
- **[BLOCKER] <title>** — <one line> (<persona(s)>, <location>)
 _(none — omit the section if empty)_

### Top 5 recommended changes
1. **<title>** — <need> → **<chosen intervention>** (<target surface>, <severity>)
...

### Persona status cards
| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 8.1/10 | 0 | ... |
| Struggling Student | 6.4/10 | 1 | ... |
| Accessibility | 5.9/10 | 2 | ... |
| Learner with Visual Preference | 7.7/10 | 0 | ... |

### Affected sections & assets
`11.3`, `11.7`, asset `mol-12`, question `ch11-sn1-energy-profile`, ...
```

## Full evidence view (below a `---` divider)

```markdown
---
## Full evidence

### Independent persona reports
For each persona: summary, overall_score, strengths, then every finding with
`finding_id`, severity, category, location, observation, learner_impact,
evidence, recommended_outcome, confidence. Present the four reports separately —
never merged.

### Orchestrator decisions
For each ranked recommendation: the `rec_id`, the need, the **chosen
intervention and why it is the least-complex option that fully addresses the
need**, target surface, and the `source_findings` it consolidates.

### Merged duplicates
Findings from different personas about the same location, and how they were
consolidated (keep the strongest severity; keep both learner impacts).

### Retained disagreements
Where personas conflicted (e.g. Accessibility wants a text equivalent while
Visual Preference wants an animation), both positions verbatim + the
orchestrator's resolution and rationale. Never delete the minority view.

### Places where a description is sufficient (no new asset)
List figures/sections where existing or slightly-improved description fully
covers the need — explicitly, so no one over-builds.

### Regression targets for next run
Stable `finding_id`s to recheck after revision.
```

## Post-correction record (default mode)

Append after the full evidence view:

```markdown
---
## Post-correction record

**Estimated state: <state> (not a second persona verdict).**

### Changes applied
- <exact change> — resolves `<finding_id>`

### Verification
- `<exact command>` — <result>

### Still recommended
- <unresolved enhancement or broader change>
```

Do not rewrite the baseline verdict at the top. The correction record describes
what changed; a new verdict requires a new four-persona regression run.

## Regression section (when a prior `chapter-review.json` exists)

```markdown
### Regression vs <prior run date>
- **Resolved (N):** <finding_id>: <title>
- **Unchanged (N):** <finding_id>: <title> ← still open
- **Worsened (N):** <finding_id>: <what got worse>
- **New (N):** <finding_id>: <title>

> A rising average score does not clear an unchanged blocker — unchanged
> blockers keep the readiness at `major revision`/`blocked`.
```
