---
name: nmr-spectrum-figure-authoring
description: Author NMR spectrum-trace teaching figures (1H/13C shifts, first-order splitting/multiplets, integration bands, variable-temperature coalescence) as the editable `nmr_spectrum` ChemTeachingAsset. Use when adding a spectrum figure to a reader chapter, slide deck, or chapter asset manifest — distinct from the proprietary nmr-unique-signals skill (not in this repo; a signal-COUNT reveal, not a spectrum).
---

# NMR Spectrum Figure Authoring

Author the `nmr_spectrum` teaching asset — the actual chemical-shift / splitting /
integration spectrum trace — so it renders **live** in the reader and exports as a
**static SVG** in decks/PDF from the *same* spec.

## When this vs. the signal-count reveal

- **`nmr_spectrum` (this skill)** — shows the spectrum: peaks at ppm, first-order
  multiplets, shaded integration bands, or a dynamic coalescence figure.
- **`nmr_unique_signals`** — a count-and-reveal of how many *inequivalent* nuclei a
  molecule has. Different asset, different renderer. Don't conflate them.
  (Authoring skill is proprietary, not in this repo.)

## Data model

Canonical types: `NmrSpectrumFigureAsset` / `NmrSpectrumFigureSpec` (and backend
mirror `NmrSpectrumAsset`) — proprietary schemas (not in this repo). Spec kept as
a loose mapping — authored/validated on the TypeScript side.

The spec is a **compact peak list**, not a raw trace:

```ts
{
  nucleus: "1H",              // or "13C"
  spectrometerMHz: 300,       // converts Hz couplings → ppm; default 300
  peaks: [
    { ppm: 1.25, protons: 3, label: "–CH₃", couplings: [{ neighborCount: 2, jHz: 7 }] },
    { ppm: 3.65, protons: 2, label: "–CH₂–", couplings: [{ neighborCount: 3, jHz: 7 }] },
  ],
  regions: [{ startPpm: 1.1, endPpm: 1.4, label: "3H" }],  // shaded integration bands
  markersPpm: [7.26],                                        // vertical guides
}
```

Variable-temperature / coalescence figure (use in conformational chapters — amide
rotation, ring flip — **not** only the NMR chapter):

```ts
{ dynamic: { siteAPpm: 2.9, siteBPpm: 3.1, regime: "coalescence", caption: "…" } }
```

## Single source of truth for the trace

Both surfaces build the displayed curve from the peak list with
`buildNmrSpectrumTrace` (proprietary function, not in this repo), which reuses the
first-order simulator shared with the grader (also proprietary, not in this repo).
Never hand-author (xPpm, y) arrays — author `peaks` and let the builder produce the
trace so the live reader render and the static deck SVG agree.

- Live reader: `TeachingAssetLiveRenderer` → `NmrSpectrumCanvas`.
- Deck/PDF export: `buildNmrSpectrumFigureSvg(spec)` → `svgToDataUrl` (inverted ppm
  axis, single `<path>`, integer-ppm ticks).

## Rules

- **ppm axis is inverted** (high ppm on the left). The builder handles it; don't
  fight it.
- First-order (spin-½) splitting only — `couplings` are `{ neighborCount, jHz }`
  levels. This matches the grader; higher-order patterns are out of scope.
- Keep `protons` as the *relative* integration; it drives band weighting.
- Every asset needs `accessibility.alt_text`. For a spoken transcript of peaks and
  splitting, see [`chem-representation-accessibility`](../chem-representation-accessibility/SKILL.md).
- No backend simulation on the deploy platform — all trace math is browser-side. The
  live-simulation feature flag (not in this repo) must stay **False**.

## Where it appears

- Reader: a `teaching_asset` block whose `content.asset` is the `nmr_spectrum` asset.
- Deck: surfaced by the per-slide offer panel (candidate keyed on shift/splitting/
  integration language) and inserted as inline SVG; or from a reviewed chapter
  manifest asset.
- Registration checklist for the asset kind itself: proprietary skill (not in this
  repo).
