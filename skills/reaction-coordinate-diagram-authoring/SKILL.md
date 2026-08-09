---
name: reaction-coordinate-diagram-authoring
description: Creates static and animated reaction coordinate diagrams for education and slide decks. Use for mechanism energy profiles (SN1, SN2, E1, E2, multistep), thermodynamic vs kinetic comparisons, transition states and intermediates — not for conformational dihedral scans.
---

# Reaction Coordinate Diagram Authoring

Reaction coordinate diagrams are **approximate, unitless teaching figures** showing progress along a reaction path vs relative energy. They are distinct from conformational energy profiles.

## When to use

- **Clear, simple reactions only** — one step (SN2, concerted epoxidation,
 hydrogenation drop) or a clean two-step profile whose shape IS the lesson
 (SN1's slow-then-fast, Hammond on a single barrier)
- Intermediates (e.g. carbocation), transition states, rate-determining steps
- Thermodynamic vs kinetic product comparisons (side-by-side specs)
- Deck GIF/MP4/poster, reader static/interactive embed, LMS link

## When NOT to use

**Reviewer-established rule (science review, 2026-07-23): in complicated
reactions an energy diagram misleads more than it teaches.** Multistep ionic
additions (HBr/Markovnikov, acid-catalyzed hydration, Br₂/bromonium,
alkyne hydration via enol, proton-transfer equilibria) had every authored
diagram rejected with "rewrite text to avoid needing diagram — remove diagram".
For those, write prose that names the slow step and what it selects; add
molecule figures, not a profile. Default to NO diagram unless the profile's
shape is itself the learning goal.

| Request | Redirect to |
| ------- | ----------- |
| Multistep ionic addition (HBr, hydration, Br₂), proton transfer, anything ≥2 barriers where the shape isn't the lesson | Prose + molecule figures — no diagram |
| Ethane/butane torsion vs dihedral angle | `conformational-energy-profile-authoring` |
| Ring flip energy sketch | `conformational-energy-profile-authoring` |
| Newman anti/gauche only (no reaction) | `newman-projection-authoring` |
| Quantitative ΔG° from literature | Note unitless caveat; do not invent numeric barriers |

## Scientific checks (required)

1. Count steps = number of transition states; minima = reactants + intermediates + products.
2. **SN2:** one step, no carbocation intermediate.
3. **SN1:** two steps, carbocation intermediate; RDS often first step (large first barrier).
4. Label rate-determining step when pedagogy requires it.
5. Add `scientific_caveats`: diagram is schematic, unitless, not from computation.
6. Optional molecule thumbnails at minima — SMILES must validate ([`rdkit-agent` → prompts/molecule-validation.md](../../prompts/molecule-validation.md)).

## Core types (repo)

Proprietary reaction-coordinate types and renderers (not in this repo): `ReactionCoordinateSpec`,
`RCStep`, `BarrierSize`; SVG/PNG render; animation planning; Remotion integration.

## Output schema

```ts
export type ReactionCoordinateTeachingAsset = {
 type: "reaction_coordinate";
 id: string;
 title: string;
 spec: ReactionCoordinateSpec;
 render_targets: Array<"svg" | "png" | "gif" | "mp4" | "pptx_poster">;
 embed_policy: {
 reader: "interactive" | "static";
 deck: "gif_with_poster" | "poster_only";
 lms: "link_to_site" | "embedded_gif";
 pdf: "static_with_link";
 };
 scientific_caveats: string[];
 accessibility_text: string;
};
```

## Spec building guide

```ts
// SN1 two-step (exergonic steps, large first barrier = RDS)
{
 title: "SN1 hydrolysis of tert-butyl chloride",
 energy_axis: "free_energy",
 steps: [
 { type: "exergonic", barrier: "large" },
 { type: "exergonic", barrier: "small" }
 ],
 minima_labels: ["Reactants", "Carbocation", "Products"],
 minima_molecules: { "0": "CC(C)(C)Cl", "1": "CC(C)(C)+", "2": "CC(C)(C)O" }
}
```

Barrier sizes: `small` | `medium` | `large` — qualitative only.

## Reader embed (`/reader/organic`)

When a `reaction_coordinate` block is compiled into topic-package reader JSON, the on-site card badge is **`blue` subtle** (`ReaderBlockRenderer`) — never purple. Diagram SVG itself stays black/gray teaching ink per house style; do not add purple curve or label styling for reader exports.

## Animation & export

- Remotion plans energy-curve reveal; GIF/MP4 for deck (proprietary deck export toolchain, not in this repo)
- PPTX: animated GIF + poster fallback + speaker notes with transcript
- Teacher review warning in `scientific_caveats` for all exports

## Examples

### Example 1 — SN1 two-step

**Prompt:** Make an SN1 reaction coordinate diagram with a carbocation intermediate and rate-determining first step.

**Emit:** `ReactionCoordinateTeachingAsset` with 2 steps, 3 minima, `scientific_caveats` including unitless schematic note, `render_targets` including `gif` + `pptx_poster` for deck use.

### Example 2 — SN2 redirect

**Prompt:** SN2 hydrolysis energy diagram.

**Emit:** One-step spec (reactants → products), **no** intermediate minimum; refuse carbocation if user insists.

## Test prompts

- "Make an SN1 reaction coordinate diagram with a carbocation intermediate."
- "Compare SN1 vs SN2 energy diagrams for the same substrate."
- "Animate this two-step elimination for a deck slide."

## Failure modes

- Conformational scan misrouted here → redirect to `conformational-energy-profile-authoring`.
- Missing `accessibility_text` → invoke `chem-representation-accessibility`.
- Invented numeric kcal/mol on unitless diagram → strip numbers; add caveat.
