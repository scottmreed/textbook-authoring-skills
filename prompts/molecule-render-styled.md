# Prompt: styled / annotated molecule render

**Replaces:** `rdkit-advanced-rendering` (product-coupled RDKit service skill — not copied)

Use when a textbook figure needs highlights, atom numbering, rotation, or
limited color for pedagogy (not ACS monochrome).

---

## System / agent instructions

Render a teaching figure from SMILES with optional annotations.

Allowed customizations (use only what the lesson needs):

- Atom numbering or map indices for mechanism discussion
- Highlight atoms/bonds for the reactive site
- Limited brand-safe colors (prefer blue/gold/neutrals; avoid purple decorative themes)
- Explicit hydrogens when stereo or hybridization is the point
- Rotation / depiction choice so the scaffold reads left-to-right like the prose

Hard rules:

1. Validate SMILES before drawing.
2. Do not change connectivity to “look nicer.”
3. Keep labels chemically conventional (wedge/dash, E/Z, R/S only when defined).
4. Provide alt text that describes what is highlighted without revealing quiz answers.

## Input

```json
{
  "smiles": "CC(=O)Oc1ccccc1C(=O)O",
  "highlight_atoms": [1, 2, 3],
  "highlight_bonds": [],
  "number_atoms": false,
  "show_hydrogens": false,
  "caption": "Aspirin — ester and carboxylic acid highlighted"
}
```

## Output

- SVG/PNG asset
- `alt_text` and optional longer transcript for complex highlights
- Short note of any depiction caveats (e.g. aromatic Kekulé form)
