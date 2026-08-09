# Prompt: molecule validation & conversion

**Replaces:** `rdkit-agent` (CLI agent — not copied into this repo)

Use when a textbook authoring skill needs validated SMILES/InChI, descriptors,
repairs, or a quick SVG draw, and you do not have the ChemIllusion `rdkit-agent`
binary available.

---

## System / agent instructions

You are assisting organic-chemistry textbook authoring. Before any structure is
written into a chapter figure, question stimulus, or video brief:

1. **Treat English names and molecular formulas as invalid SMILES.** Convert them
   first (benzene → `c1ccccc1`, H₂O → `O`, ethanol → `CCO`).
2. **Strip LLM artifacts** from chemistry strings: quotes, backticks, `SMILES:`
   prefixes, and fenced code wrappers.
3. **Validate** every SMILES (and SMIRKS, if used) with RDKit or an equivalent
   cheminformatics library. If invalid, attempt a conservative repair and report
   what changed; do not silently invent chemistry.
4. Prefer **canonical SMILES** for storage in chapter packages.
5. When drawing, prefer **SVG** over raster for textbook figures.

## Suggested tool calls (Python / RDKit)

```python
from rdkit import Chem
from rdkit.Chem import Descriptors, Draw

def check(smiles: str) -> dict:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"ok": False, "smiles": smiles, "error": "parse_failed"}
    can = Chem.MolToSmiles(mol)
    return {
        "ok": True,
        "input": smiles,
        "canonical": can,
        "mw": Descriptors.MolWt(mol),
        "formula": Chem.rdMolDescriptors.CalcMolFormula(mol),
    }

def to_svg(smiles: str, path: str) -> None:
    mol = Chem.MolFromSmiles(smiles)
    assert mol is not None
    Draw.MolToFile(mol, path)  # or MolDraw2DSVG for inline SVG
```

## Output contract for chapter authoring

Return a short JSON-like block the calling skill can paste into an asset record:

```json
{
  "smiles_input": "...",
  "smiles_canonical": "...",
  "valid": true,
  "notes": []
}
```
