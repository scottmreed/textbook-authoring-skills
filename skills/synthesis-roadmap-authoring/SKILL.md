---
name: synthesis-roadmap-authoring
description: Creates multistep synthesis roadmap teaching assets ("an introduction to organic synthesis") — a left→right map of a route with structure nodes joined by reagent-labeled arrows, rendered as a slide SVG and (optionally) a stepwise-reveal GIF. Use for forward syntheses, retrosynthetic analyses, acetylide/alkylation chain-building, and "build the target molecule" problems. Not for single-step mechanisms (use reaction-coordinate-diagram-authoring) or one molecule (use a molecule figure).
---

# Synthesis Roadmap Authoring

A synthesis roadmap is a **route map**, not a mechanism: an ordered series of structure
nodes (starting material → … → target) joined by arrows, each arrow labeled with the
reagents/conditions for that step. It is the canonical figure for the alkynes chapter's
"introduction to organic synthesis" and for any "design a synthesis of X" content.

Renders as a static SVG slide by default; the same pure builder can emit a stepwise
sequence (step 1, steps 1–2, …) for an animated "gif" reveal.

## When to use

- Multistep **forward synthesis** (≥ 2 steps) building a target molecule
- **Retrosynthetic** analysis (set `spec.retrosynthetic = true` → open ⇒ arrows)
- Acetylide alkylation chain-building, protect/deprotect routes, functional-group interconversions
- Deck slide (inline SVG) or stepwise-reveal GIF

## When NOT to use

| Request | Redirect to |
| ------- | ----------- |
| Single mechanism energy profile (SN1/SN2/E1/E2) | `reaction-coordinate-diagram-authoring` |
| One structure / product only | `molecule` figure |
| cis/trans or R/S comparison of one transformation | `stereochemistry-conversion` asset |
| Torsional/conformational energy | `conformational-energy-profile-authoring` |

## Scientific checks (required)

1. **Every node `smiles` must validate** (use [`rdkit-agent` → prompts/molecule-validation.md](../../prompts/molecule-validation.md)). A node may be text-only
 (omit `smiles`) but prefer real structures.
2. **`steps.length === nodes.length - 1`** — each step is the arrow from `nodes[i]` to `nodes[i+1]`.
3. **Reagents must be chemically correct and complete** for the drawn transformation
 (number the operations when order matters, e.g. `1. NaNH₂ 2. CH₃Br`).
4. **Acetylide alkylation:** Sₙ2 — methyl / primary alkyl halides only; secondary/tertiary
 halides eliminate. Each alkylation forms one new C–C bond.
5. **Alkyne reduction stereochemistry:** H₂/Lindlar → **cis (Z)** (syn); Na/NH₃ → **trans (E)**;
 H₂/Pd → full reduction to the alkane. Set the target SMILES geometry to match.
6. **Markovnikov vs anti-Markovnikov:** hydration (H₂O/H⁺,Hg²⁺) → methyl ketone;
 hydroboration–oxidation → aldehyde. Pick the reagent that actually gives the drawn node.
7. **Retrosynthetic direction:** when `retrosynthetic`, arrows read target → precursors
 ("comes from"); label disconnections, not reagents-as-forward.
8. Add `scientific_caveats` (schematic; stoichiometry/work-up not shown; halide constraints).
9. `accessibility.alt_text` is REQUIRED; add a `long_description` narrating each step.

## Core types / files (repo)

Proprietary synthesis-roadmap types and renderers (not in this repo):

- `SynthesisRoadmapSpec`, `SynthesisRoadmapAsset` (union member `type: "synthesis_roadmap"`)
- `buildSynthesisRoadmapSvg` (pure; `revealUpTo` for animation frames), `resolveRoadmapNodes`, `renderSynthesisRoadmap`
- `renderManifestAssetToDataUrl` case + generate-new default render
- `synthesis_roadmap` detector (synthesis keywords; `owningSkill: "synthesis-roadmap-authoring"`)
- `CANDIDATE_TO_ASSET_TYPES`, `INLINE_SVG_TYPES`

Structure node images reuse the shared RDKit endpoint and proprietary structure assets (not in this repo).

## Output schema (manifest asset)

```jsonc
{
 "id": "roadmap-<topic>",
 "type": "synthesis_roadmap",
 "title": "Introduction to organic synthesis: building <target> from <start>",
 "learning_goal": "...",
 "editable": true,
 "spec": {
 "nodes": [
 { "smiles": "C#C", "label": "acetylene" },
 { "smiles": "CC#C", "label": "propyne" },
 { "smiles": "CC#CCC", "label": "pent-2-yne" },
 { "smiles": "C/C=C\\CC", "label": "(Z)-pent-2-ene", "is_target": true }
 ],
 "steps": [
 { "reagents": "1. NaNH₂ 2. CH₃Br", "note": "acetylide alkylation — 1st C–C bond" },
 { "reagents": "1. NaNH₂ 2. CH₃CH₂Br", "note": "acetylide alkylation — 2nd C–C bond" },
 { "reagents": "H₂, Lindlar catalyst", "note": "syn addition → cis (Z) alkene" }
 ],
 "retrosynthetic": false,
 "scientific_caveats": ["Acetylide Sₙ2 alkylation works with methyl/1° halides only."]
 },
 "accessibility": { "alt_text": "...", "long_description": "..." },
 "source_context": {
 "chapter_id": "chapter-06",
 "section_id": "alkyne-synthesis",
 "concept_tags": ["multistep synthesis", "acetylide alkylation", "stereoselective reduction"],
 "representation_tags": ["synthesis_roadmap", "reaction_map"]
 },
 "science_review": { "status": "not_reviewed" }
}
```

> JSON note: a SMILES backslash (cis double bond `C/C=C\C`) must be escaped as `\\` in JSON.

## House style (WCAG)

- Target node highlighted with a **green** border + "(target)" caption. Forward arrows are
 blue with an arrowhead; retrosynthetic uses open ⇒ double-lines. **Never use purple**
 (ChemIllusion brand rule). Dark text on white nodes for AA contrast.
- Reagents bold above the arrow; mechanism-class/role note muted below.

## Animation (stepwise reveal → GIF)

`buildSynthesisRoadmapSvg(resolvedNodes, spec, { revealUpTo: k })` dims nodes/arrows beyond
`k`. Render frames `k = 1..nodes.length`, then encode to GIF/MP4 via the
`molecule-video-creator` export path (proprietary toolchain, not in this repo) and attach as the
asset's `video` ref (`gif_url` / `mp4_url` / `poster_url`).

## Examples

### Example 1 — alkyne intro-to-synthesis (forward)
**Prompt:** "Build (Z)-pent-2-ene from acetylene." → 4 nodes (acetylene → propyne → pent-2-yne →
(Z)-pent-2-ene), 3 steps (two acetylide alkylations + Lindlar). Target flagged; caveat on the
primary-halide constraint. (Shipped as `roadmap-alkyne-intro-synthesis` in chapter-06.)

### Example 2 — retrosynthesis
**Prompt:** "Show the retrosynthesis of 2-hexanone." → `retrosynthetic: true`, arrows target →
precursors, notes describe disconnections (e.g. "C–C disconnection → acetylide + 1° halide").

## Test prompts

- "Make a synthesis roadmap building (Z)-pent-2-ene from acetylene."
- "Draw a retrosynthetic map for this internal alkyne."
- "Animate the route one step at a time for a deck slide."

## Failure modes

- `steps.length !== nodes.length - 1` → arrows/nodes misalign; fix counts.
- Secondary/tertiary halide on an acetylide alkylation → wrong; switch to a 1° halide or note elimination.
- Wrong reduction stereochemistry (Lindlar drawn as trans) → fix the target geometry/reagent.
- Missing `accessibility.alt_text` → invoke `chem-representation-accessibility`.
- Invalid node SMILES → renderer degrades the node to text-only; validate with [`rdkit-agent` → prompts/molecule-validation.md](../../prompts/molecule-validation.md).
