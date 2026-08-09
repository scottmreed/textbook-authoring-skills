---
name: syllabus-to-reader-outline
description: Converts syllabus extraction results into a reader, deck, and tutorial plan with topic prerequisites, textbook mapping, and explicit ChemTeachingAsset figure needs. Use when mapping Wade, McMurry, LibreTexts, or custom Organic I/II sequences to ChemIllusion reader sections without bundling third-party textbook content.
---

# Syllabus to Reader Outline

Convert parsed syllabus data into a **mapping plan** — not a reproduced textbook.

## The one rule

**Map to sequences. Link external readings. Never bundle or replace third-party textbooks.** Same policy as the proprietary course-reader skill and its ingestion documentation (not in this repo).

## When to invoke

- Syllabus upload / `document_parser_service` extraction complete
- Teacher names Wade 9e, McMurry, LibreTexts, or custom week order
- Need reader sections + figure generation queue before `organic-chapter-asset-auditor`

## Inputs

Typical sources:
- proprietary syllabus-parser output (not in this repo)
- proprietary catalog assets and ingestion documentation (not in this repo)
- Teacher overrides (reorder, merge, split, hide, lock)

## Output structure

```ts
export type SyllabusReaderPlan = {
 reader_id: string;
 textbook_mapping: {
 primary_text?: "wade" | "mcmurry" | "libretexts" | "openstax" | "custom";
 chapter_alignment_notes: string; // flag numbering mismatches
 external_links_only: true; // always true
 };
 topic_graph: Array<{
 topic_id: string;
 title: string;
 prerequisites: string[];
 reader_section_ids: string[];
 syllabus_weeks: number[];
 }>;
 chapter_operations: Array<
 | { op: "reorder"; chapter_ids: string[] }
 | { op: "merge"; from: string[]; into: string }
 | { op: "split"; chapter_id: string; at_section: string }
 | { op: "hide"; chapter_id: string; reason: string }
 | { op: "lock"; chapter_id: string; reason: string }
 >;
 asset_generation_queue: Array<{
 topic_id: string;
 section_id: string;
 requested_asset_type: ChemTeachingAsset["type"];
 priority: "must_have" | "should_have" | "nice_to_have";
 authoring_skill: string;
 }>;
};
```

## Mapping workflow

1. **Parse** syllabus weeks/topics and learning objectives.
2. **Align** to catalog chapter IDs — emit `chapter_alignment_notes` when reader chapter number ≠ textbook chapter number.
3. **Build** prerequisite DAG (e.g. conformations before SN1/SN2).
4. **Map** each topic → `reader_section_ids` (create stubs if missing).
5. **Queue** `ChemTeachingAsset` requests by concept:
 - alkanes/conformations → Newman + conformational profile
 - mechanisms → reaction coordinate
 - orbitals → orbital overlay
6. **Hand off** queue to `organic-chapter-asset-auditor` for refinement.

## Textbook sequence handling

| Syllabus says | Agent behavior |
| ------------- | -------------- |
| Wade Ch 3 before Ch 4 | Emit reorder plan; do not assume fixed reader order |
| Skips spectroscopy week | `hide` or defer sections; note in plan |
| Custom "functional groups first" | `reorder` with prerequisite warnings |
| LibreTexts module URLs | `external_link` blocks only |

## Examples

### Example 1 — Wade 9e Organic I

**Prompt:** Convert a Wade 9e Organic I syllabus (weeks 1–8) into reader sections and figure needs.

**Output:** `SyllabusReaderPlan` with `textbook_mapping.primary_text: "wade"`, week→section map, queue entries for Week 3 Newman/conformation assets, Week 5 mechanism diagrams — all `external_links_only: true`.

### Example 2 — Chapter number mismatch

**Prompt:** Syllabus "Chapter 5: Alkenes" but reader catalog lists alkenes as Chapter 4.

**Output:** `chapter_alignment_notes` explaining offset; sections still mapped by **topic**, not assumed numbers.

## Test prompts

- "Convert a syllabus week on alkanes into reader sections and figure needs."
- "Map McMurry Chapter 6 content to ChemIllusion reader stubs."
- "Build a prerequisite graph for conformations → mechanisms."

## Failure modes

- Emitting copied textbook prose → forbidden; links only.
- Fixed chapter order regardless of syllabus → must honor teacher sequence.
- Asset queue without priorities → add must/should/nice tiers.

## Related skills

- proprietary reader-block skill (not in this repo) — reader block implementation
- `organic-chapter-asset-auditor` — downstream gap refinement
- `organic-textbook-reader-content` — `/reader/organic` PWA catalog (distinct from teacher course reader)
