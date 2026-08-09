---
name: organic-chapter-asset-auditor
description: Reviews chapter outlines, reader block lists, deck outlines, or syllabus-mapped units and recommends missing editable ChemIllusion figures with priorities. Use when auditing organic chemistry chapters for Newman, reaction coordinate, conformational, orbital, or stereochemistry figure gaps.
---

# Organic Chapter Asset Auditor

Audit **structured chapter input** and return prioritized replacement recommendations — not a generic figure wishlist.

## When to invoke

- After `syllabus-to-reader-outline` produces a draft plan
- Before Chapter 1–5 figure replacement passes
- When reviewing `ChemEdReaderChapterReviewPage` block lists
- When deck JSON still has `legacy_placeholder` or `static_image` figures

## Input schema

```ts
export type ChapterAssetAuditInput = {
 chapter_id: string;
 title: string;
 learning_objectives: string[];
 sections: Array<{
 id: string;
 title: string;
 current_assets: Array<{
 id: string;
 type: string;
 status: "legacy_placeholder" | "static_image" | "editable_asset" | "external_link";
 }>;
 concepts: string[];
 }>;
};
```

## Output schema

```ts
export type ChapterAssetAuditOutput = {
 chapter_id: string;
 required_replacements: Array<{
 section_id: string;
 placeholder_id?: string;
 proposed_asset_type:
 | "newman_projection"
 | "reaction_coordinate"
 | "conformational_energy_profile"
 | "orbital_overlay"
 | "molecule"
 | "stereochemistry_conversion"
 | "acid_base_energy_diagram";
 priority: "must_have" | "should_have" | "nice_to_have";
 rationale: string;
 editable_fields: string[];
 suggested_skill: string; // e.g. newman-projection-authoring
 }>;
 chapter_level_gaps: string[];
};
```

## Detection heuristics

| Concepts / section signals | Asset type | Priority |
| -------------------------- | ---------- | -------- |
| alkane conformation, staggered, eclipsed, Newman | `newman_projection` | must_have |
| butane anti, gauche, torsional strain | `newman_projection` + `conformational_energy_profile` | must_have |
| SN1, carbocation, unimolecular | `reaction_coordinate` | must_have |
| SN2, bimolecular, backside attack | `reaction_coordinate` (one-step) | should_have |
| acid/base, proton transfer, curved arrows intro | `reaction_coordinate` or `acid_base_energy_diagram` | should_have |
| pi bond, HOMO/LUMO, orbital overlap | `orbital_overlay` | should_have |
| R/S, enantiomers, Fischer/wedge conversion | `stereochemistry_conversion` | should_have |
| Generic "reaction happens" prose | **no** reaction coordinate | — |

## Rules

1. **Do not** suggest reaction coordinate diagrams for every reaction-like sentence.
2. Prefer **editable** replacements over new static images.
3. Flag `external_link` blocks that are fine as links — do not replace with bundled textbook content.
4. Return `priority`, not an unordered list.
5. Point each replacement to the authoring skill (`suggested_skill`).

## Examples

### Example 1 — Chapter 3 alkanes audit

**Input:** Section `3.2` concepts `["butane conformers", "anti", "gauche", "torsional strain"]`, `current_assets: [{ type: "image", status: "static_image" }]`.

**Output:** `must_have` `newman_projection` (anti + gauche pair) + `conformational_energy_profile`; rationale cites missing editable conformer comparison.

### Example 2 — Mechanism intro without over-flagging

**Input:** Section mentions "alkyl halides react with nucleophiles" only.

**Output:** `should_have` `reaction_coordinate` only if objectives include mechanism comparison; otherwise `nice_to_have` molecule figures — **not** mandatory multistep diagram.

## Test prompts

- "Audit a stereochemistry chapter and suggest missing figures."
- "Review Chapter 3 reader blocks for Newman gaps."
- "What editable assets are missing from this Wade Week 4 syllabus mapping?"

## Failure modes

- Generic "add more figures" without priorities → re-run with section-level concept mapping.
- Suggesting bundled textbook PDFs → violates reader rights; use `external_link` only.

## Manifest conventions & backlinks

Authored output lands as a per-chapter manifest (proprietary chapter-asset manifest,
not in this repo; schema `ChapterAssetManifest`). Draft manifests now exist for chapters
**01–05** (Phase 1) — see proprietary asset-audit documentation (not in this repo) for the
Phase 0/1 inventory. Chapter↔deck mapping uses the proprietary
`DECK_CHAPTER_TO_CONTENT_CHAPTER` crosswalk (not in this repo).

Downstream consumers of what this auditor produces:

- **Deck offers** resolve candidates against the manifest via
  `manifestAssetResolver.ts` (reviewed > draft > generate > coming-soon) and
  insert inline via proprietary deck-figure resolvers (not in this repo).
  Orbital overlays render from the bundled orbital library (`getAssetSvg`).
- **Reader** renders teaching assets on-site (e.g. the `reaction_coordinate`
  block via the proprietary reader block renderer (not in this repo).

Author assets as `science_review.status: "not_reviewed"`; **never auto-approve** (PRD §3, §13).
For chapters without a structured `ReaderBlock` fixture, do **not** fabricate
`legacy_placeholder_id`s — leave `replacements: []` until stable block IDs exist.

## Adding a NEW chapter (full package, not just a gap list)

When the task is **"add the next chapter"** — produce the whole package, not an audit list —
hand off to the **`produce-organic-chapter` (formerly `add-organic-chapter`)** skill. It composes this auditor's type choices into one
deterministic pass: manifest assets across the renderer-backed types, textbook sections, deck
offers (automatic from the manifest), and video segments where appropriate, all authored
`science_review.status: "not_reviewed"`.

New and existing chapters then surface in the **Science Review Queue** (`/admin/asset-review`) for
an admin or contractor to **View → Approve / Needs work / Pass** + leave a note (persisted in
`teaching_asset_reviews`; approved assets are offered first by the deck resolver). See
proprietary asset-review documentation (not in this repo) for the chapters 1–5 baseline that new chapters
should mirror.

## Related skills

- `produce-organic-chapter` (formerly `add-organic-chapter`) — orchestrates a full new-chapter package from this auditor's output
- `syllabus-to-reader-outline` — upstream plan input
- proprietary reader-block skill (not in this repo) — reader block types
- proprietary deck-figure resolvers (not in this repo) — deck placeholder replacement (out of scope for reader-only authoring)
