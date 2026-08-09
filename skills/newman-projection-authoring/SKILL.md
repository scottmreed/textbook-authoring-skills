---
name: newman-projection-authoring
description: Creates, edits, tests, and exports Newman projections as editable ChemIllusion teaching objects. Use when authoring conformational analysis figures (ethane, butane anti/gauche, staggered/eclipsed), reader/deck/LMS assets, or when a user asks for Newman projections, dihedral conformers, or alkane conformation teaching figures.
---

# Newman Projection Authoring

Guide agents to treat Newman projections as **first-class editable teaching objects**, not decorative clipart or generic SVG images.

**PRD:** proprietary documentation (not in this repo)
**Surface:** `/generator` canvas overlay (ChemIllusion-owned; **not** a Ketcher fork)

## When to use

- Conformational analysis: staggered, eclipsed, gauche, anti, partially rotated views
- Alkane / substituted-ethane / haloalkane conformer pairs
- Cyclohexane-adjacent pedagogy where a Newman view clarifies a bond rotation
- Reader blocks, deck slides, ChemTutor questions, LMS/PDF export

## When NOT to use

| Request | Redirect to |
| ------- | ----------- |
| Absolute stereochemistry at a chiral center (wedge/dash) | `molecule-svg-drawing`, Ketcher skeletal |
| Reaction mechanism energy landscape | `reaction-coordinate-diagram-authoring` |
| Torsional energy vs dihedral angle plot | `conformational-energy-profile-authoring` |
| Fischer projection or chair flip alone | Chair/skeletal tools; Newman only if comparing bond rotation |
| Arbitrary 3D conformer from SMILES | RDKit 3D — Newman is a **2D pedagogical projection** |

## Scientific checks (required before emit)

1. Confirm the pedagogical goal is **viewing down a C–C (or C–X) bond** for conformation comparison.
2. Name front/back carbons and substituents explicitly in metadata.
3. Set `scientific_status` honestly: `visual_only` | `substituent_tokens` | `graph_backed`.
4. Pair anti/gauche or staggered/eclipsed as **two assets** when comparing conformers.
5. Never claim quantitative strain energies from the diagram alone.

## Canonical presets (≥8)

| Preset ID | Description |
| --------- | ----------- |
| `ethane_staggered` | H/H staggered 60° |
| `ethane_eclipsed` | H/H eclipsed 0° |
| `propane_staggered` | Me/H staggered template |
| `butane_anti` | Me–Me 180° anti |
| `butane_gauche` | Me–Me ~60° gauche |
| `substituted_ethane_template` | Custom front/back substituent tokens |
| `haloalkane_staggered` | e.g. Cl front / H back pedagogy |
| `cyclohexane_bond_view` | Newman along a ring bond (conceptual link to chair) |

## Output schema

```ts
export type NewmanProjectionTeachingAsset = {
 type: "newman_projection";
 id: string;
 title: string;
 learning_goal: string;
 object: NewmanProjectionObject; // front_rotation_deg, back_rotation_deg, substituents, labels
 editable_fields: Array<
 | "front_rotation_deg"
 | "back_rotation_deg"
 | "front_substituents"
 | "back_substituents"
 | "labels"
 >;
 scientific_status: "visual_only" | "substituent_tokens" | "graph_backed";
 accessibility_text: string;
 source_context?: {
 chapter_id?: string;
 section_id?: string;
 syllabus_topic?: string;
 };
};
```

Emit as part of shared `ChemTeachingAsset` (see `chem-representation-accessibility`).

## Label & token rules

- Display labels: `H`, `Me`, `Et`, `Cl`, `Br`, `OH`, etc.
- Token maps tie labels to substituent slots (`front_top`, `front_left`, `front_right`, `back_*`).
- Continuation bonds may link to drawn structures via object-sketch / canvas attachment — preserve in export metadata.
- Formula display is optional; do not infer IUPAC names from unvalidated free text.

## Export policy

| Surface | Behavior |
| ------- | -------- |
| Reader | Editable block or static SVG + link to interactive site |
| Deck | Static SVG default; site link if interactivity required |
| LMS (IMSCC) | Link-to-site or embedded static + alt text |
| PDF | Static SVG/PNG + accessibility transcript in figure caption |

## Implementation pointers

- Renderer/tests: follow the proprietary Newman implementation guide (not in this repo); object-sketch canvas path
- Accessibility: invoke **`chem-representation-accessibility`** for every asset
- Audit queue: **`organic-chapter-asset-auditor`** flags Newman gaps in alkane/conformation sections

## Examples

### Example 1 — Butane anti/gauche pair (Chapter 3)

**Prompt:** Create a butane anti/gauche Newman figure pair for a conformational analysis section.

**Emit:** Two `NewmanProjectionTeachingAsset` records (`butane_anti`, `butane_gauche`), `scientific_status: "substituent_tokens"`, linked `source_context.section_id`, plus `accessibility_text` for each.

### Example 2 — Reject wedge/dash misuse

**Prompt:** Draw the R configuration of 2-bromobutane as a Newman projection.

**Response:** Explain Newman is for **bond-axis conformation**, not absolute R/S at a stereocenter; offer wedge/dash skeletal via Ketcher instead.

## Test prompts

- "Create a butane anti/gauche Newman figure for Chapter 3."
- "Add a staggered ethane Newman for an intro alkanes deck slide."
- "Why shouldn't I use a Newman for Fischer projection content?"

## Failure modes

- **Generic image request** — emit structured `NewmanProjectionTeachingAsset`, not a PNG prompt.
- **Missing alt text** — block completion; call `chem-representation-accessibility`.
- **Single conformer when comparison intended** — emit both conformers or ask which comparison is needed.
