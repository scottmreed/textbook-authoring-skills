---
name: orbital-overlay-assets
description: How agents add scientifically-constrained, teacher-gated orbital overlays (p orbitals, sigma/pi overlap, carbonyl pi*, benzene pi cloud, lone pairs) onto curated orbital-ready molecule presets in ChemIllusion. Use for Graphical Abstract, ChemEd authoring, slide decks, and ChemTutor playback.
when_to_use: A user asks to show/teach an orbital, pi bond, lone pair, empty p orbital, carbonyl electrophilicity, aromatic pi cloud, or orbital overlap on a molecule; or to add an orbital diagram to a graphical abstract, lesson, slide, or tutorial.
---

# Orbital Overlay Assets

ChemIllusion ships a **verified static library** of qualitative orbital cartoons. The app
consumes finished assets only; the SVG-generation tooling is **not** in this repo.

> These overlays are **qualitative teaching diagrams** of canonical orbital shape and
> overlap. They are **NOT computed molecular orbitals**. Never claim otherwise.

## Hard rules for agents

1. **Use curated molecule presets first.** Do not invent freeform overlays on arbitrary
 molecules. Start from a verified `*_orbital_ready_v1` preset.
2. **Only place overlays a preset allows.** Each preset lists `allowedOverlays`. If the
 requested molecule/overlay pair is not allowed, ask the user to pick a verified
 preset+overlay — do not improvise.
3. **Never generate new orbital SVGs in-app.** Call the deterministic tool/endpoints below.
 New assets are authored in the sandbox, reviewed, and committed — not produced at runtime.
4. **Preserve phase convention.** Phase colors mean **wavefunction phase, not charge**.
 Keep the phase warning whenever `phaseConvention.usesPhaseColors` is true.
5. **Avoid skeletal-only drawings.** Overlays require `orbital_ready_explicit_2d` molecules
 with explicit atoms — that is why presets exist.
6. **Authoring is teacher-gated.** Only admins, contractors (`lti_sandbox_allowed`), LMS
 teachers (`is_teacher`), and paid tiers (premium/professional) can author. Students and
 Free/Basic users get **read-only** rendering of teacher-approved figures.
7. **Respect review status.** Only `verified` assets are public to students. Assets in
 `scientific_review` are usable by authoring roles but carry a "pending review" warning.

## Deterministic agent action

```jsonc
{
 "tool": "add_orbital_overlay",
 "surface": "graphical_abstract", // | chemed_authoring | slide_deck_creator | chemtutor
 "moleculePresetId": "ethene_orbital_ready_v1",
 "overlayAssetId": "pi_bond_alkene",
 "placement": "default_verified", // or "teacher_adjusted" with a transform
 "purpose": "Show side-by-side p-orbital overlap in an alkene pi bond"
}
```

The action validates: user role, asset review status, preset review status, asset/preset
compatibility, transform constraints, export compatibility. On failure it steers the user to
a verified preset rather than improvising.

## Backend endpoints (mounted under `/api`)

| Method | Path | Purpose |
|---|---|---|
| GET | `/orbitals/assets` | list overlay assets (verified; +pending for authors) |
| GET | proprietary orbital manifest (not in this repo) | full asset manifest |
| GET | `/orbitals/presets` | list molecule presets |
| GET | `/orbitals/presets/{id}` | full molecule preset (atom roles/positions, allowed overlays) |
| POST | `/orbitals/validate-placement` | role + compatibility + transform validation; returns `safeTransform` |
| POST | `/orbitals/compose-preview` | composed preset+overlay SVG with not-a-computed-orbital metadata |

## Placement & node alignment

Overlays are authored so the scientifically meaningful **node sits at coordinate (0,0)**.
Bond-anchored overlays (alkene/alkyne/carbonyl) place their two p-orbital nodes at
`(±50, 0)`; the default transform scales by `bondLength / 100` and rotates to the bond
vector, so **the nodes land exactly on the two bonded atoms**. Single-atom overlays
(p, empty-p, lone pair) anchor their node on the atom center.

## Allowed edits (constrained)

Uniform scale (single slider — never corner handles, aspect ratio is locked), rotation
within the manifest's allowed modes, x/y nudge, **opacity/transparency**, accessible phase
palette, show/hide phase labels, reset to reviewed placement, delete. **Blocked:**
non-uniform scale, arbitrary path edits, phase-erasing recolor, disallowed flips, anchoring
to invalid substructures.

## Asset locations

Proprietary orbital asset tree (not in this repo): manifest schemas, overlay library,
preset manifests, and versioned SVG folders per asset and preset.

## Adding / promoting assets (owner workflow)

1. Generate new SVG + manifest + thumbnail in the sandbox tooling (kept out of this repo).
2. Run the scientific-review checklist in proprietary orbital documentation (not in this repo).
3. Commit the asset folder and register it in the proprietary orbital manifest (not in this repo).
4. Promote `review.status` to `verified` only after a chemistry reviewer signs off — that is
 what exposes it to students.

Code: proprietary orbital overlay service (not in this repo).
