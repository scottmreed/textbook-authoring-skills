---
name: ir-vibration-asset-authoring
description: Author animated IR vibrational-mode teaching figures as the `molecular_vibration` ChemTeachingAsset from the curated 28-mode catalog. Use when adding a vibration/IR figure to a reader chapter or slide deck — a stretch, bend, or characteristic-absorption mode that plays live (3Dmol) in the reader and exports as a poster/GIF in decks.
---

# IR Vibration Asset Authoring

Author the `molecular_vibration` teaching asset — an animated vibrational mode that
plays **live in the reader** (3Dmol) and exports as a **poster/GIF in decks**.

## Data model

Canonical types: `MolecularVibrationFigureAsset` / `MolecularVibrationFigureSpec`
(and backend mirror `MolecularVibrationAsset`) — proprietary schemas (not in this
repo).

The spec just **references a committed mode id**; the displacement vectors are baked
into the catalog asset, never computed at runtime:

```ts
{ mode_id: "carbonyl_stretch", autoplay: true, show_vectors: true, show_frequency: true }
```

Pick `mode_id` from the proprietary vibration catalog index (not in this repo;
28 curated modes). Each entry names the molecule, functional group,
`mode_category` (stretch/bend), and characteristic frequency range.

## Renderers

- Live reader / preview: `VibrationViewer` — proprietary UI (not in this repo);
  consumes `/assets/vibrations/<mode_id>.json`. Reused by
  `TeachingAssetLiveRenderer` (reader) and `AssetPreview` (review queue).
- Deck: **not** rendered inline (no per-slide WebGL). The deck video pipeline
  renders a poster PNG + frame-capture GIF into the asset's `video` ref; the offer
  panel then inserts that poster/GIF. Until a `video` ref exists, the deck offer
  points the author here rather than falsely rendering a still.

## Hard constraints

- **3Dmol is loaded from a pinned CDN** via a proprietary loader (not in this
  repo) — it is deliberately **not** an npm dependency (keeps `package-lock.json`/
  Vercel untouched). Do not `npm install 3dmol`.
- `VibrationViewer` respects `prefers-reduced-motion` (no autoplay; manual frame
  scrubber) and falls back to the text `accessibility_description` when WebGL is
  unavailable. Preserve both.
- Motion arrows use the blue accent; highlight spheres use the orange accent —
  color is never the only cue (label the mode).
- Frequency labels honor the approximate/range convention via
  `formatFrequencyLabel` — don't hard-code a single wavenumber for a range mode.

## Where it appears

- Reader: a `teaching_asset` block whose `content.asset` is the vibration asset —
  useful beyond IR chapters (bond-strength/functional-group slides, greenhouse-gas
  asides).
- Deck: per-slide offer keyed on IR/vibration language; inserted as poster/GIF.
- Accessibility transcript patterns for an animated 3D mode:
  [`chem-representation-accessibility`](../chem-representation-accessibility/SKILL.md).
- Registering the asset kind end-to-end: proprietary skill (not in this repo).
