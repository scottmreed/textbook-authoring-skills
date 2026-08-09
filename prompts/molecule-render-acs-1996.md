# Prompt: ACS 1996–style molecule render

**Replaces:** `rdkit-acs-1996-rendering` (product-coupled RDKit service skill — not copied)

Use when a textbook figure should look like a formal ACS line drawing:
monochrome, journal-style bond lengths/weights, transparent background preferred.

---

## System / agent instructions

Produce a publication-style 2D structure drawing for inclusion in an organic
chemistry textbook chapter.

Constraints:

- **Monochrome** black bonds and atom labels on transparent or white background.
- **No rainbow / decorative color schemes.**
- Prefer **SVG** (vector). If only PNG is available, use high DPI (≥300).
- Use ACS-like proportions: consistent bond length, modest line width, readable
  heteroatom labels, wedge/dash stereo only when stereochemistry is the lesson.
- Explicit hydrogens: show only when the pedagogy needs them (tiny molecules,
  stereo centers under discussion); otherwise use skeletal notation.
- Never invent atoms or bonds that are not in the provided SMILES.

## Input you will receive

- `smiles` (required, already validated if possible)
- optional `caption` / `alt_text` draft
- optional `show_hydrogens`: `auto` | `true` | `false`

## Output

1. An SVG (or PNG) file path / bytes for the figure.
2. A one-line **alt text** that describes the structure without giving away a
   quiz answer (name the molecule class or connectivity, not “the correct choice”).
3. Confirmation that the drawing matches the SMILES (atom count / key FG check).

## Minimal RDKit sketch

```python
from rdkit import Chem
from rdkit.Chem.Draw import rdMolDraw2D

mol = Chem.MolFromSmiles(smiles)
drawer = rdMolDraw2D.MolDraw2DSVG(400, 300)
# Prefer black/white ACS-like options available in your RDKit version
opts = drawer.drawOptions()
opts.bondLineWidth = 1.5
drawer.DrawMolecule(mol)
drawer.FinishDrawing()
svg = drawer.GetDrawingText()
```
