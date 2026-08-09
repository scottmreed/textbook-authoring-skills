---
name: conformational-energy-profile-authoring
description: Authors conformational energy profiles (torsional scans, ring flips, axial/equatorial preference) and prevents misusing reaction coordinate diagrams for conformational analysis. Use for ethane/butane dihedral plots, anti/gauche energy comparisons, and Newman-linked conformer pedagogy.
---

# Conformational Energy Profile Authoring

**Purpose:** Keep conformational analysis figures scientifically distinct from **reaction mechanism** coordinate diagrams.

## When to use

- Ethane 0°/60°/120° torsional profile (qualitative or relative kcal/mol)
- Butane anti / gauche / eclipsed relative energies
- Cyclohexane ring-flip progress coordinate
- Axial vs equatorial preference sketches (e.g. methylcyclohexane)
- Pairing with Newman projections (`linked_newman_asset_id`)

## When NOT to use

| Request | Redirect to |
| ------- | ----------- |
| SN1/SN2/E1/E2 mechanism | `reaction-coordinate-diagram-authoring` |
| Activation barrier along reaction path | `reaction-coordinate-diagram-authoring` |
| Carbocation intermediate on energy axis | `reaction-coordinate-diagram-authoring` |

## Coordinate kinds

| `coordinate` value | X-axis meaning |
| ------------------ | -------------- |
| `dihedral_angle` | H–C–C–H or substituent dihedral (0–360°) |
| `ring_flip_progress` | Chair ↔ chair via twist-boat (schematic 0–100%) |
| `relative_conformer_energy` | Ordinal ranking without angle axis |

## Output schema

```ts
export type ConformationalEnergyProfileAsset = {
 type: "conformational_energy_profile";
 id: string;
 title: string;
 coordinate: "dihedral_angle" | "ring_flip_progress" | "relative_conformer_energy";
 conformers: Array<{
 label: string;
 angle_deg?: number;
 relative_energy?: number | "low" | "medium" | "high";
 linked_newman_asset_id?: string;
 }>;
 scientific_caveats?: string[]; // e.g. "qualitative only"
 accessibility_text: string;
};
```

## Scientific checks

1. X-axis must be **conformational** (dihedral, flip progress), not reaction progress.
2. When quantitative values appear, label source or mark as illustrative.
3. Link Newman assets for each named conformer when the chapter teaches both views.
4. **Prefer numeric `relative_energy` (kcal/mol) over "low/medium/high"**
 (reviewer rule, 2026-07-23). Compute with an RDKit constrained MMFF94
 dihedral scan (ethane eclipsed ≈ +3.2 by MMFF94; experimental ≈ 2.9 — cite
 both in `scientific_caveats`) or use canonical literature values. Cyclohexane
 ring flip: chair 0 → half-chair +10 → twist-boat +5.5 → boat +6.5 →
 twist-boat +5.5 → half-chair +10 → flipped chair 0; the boat is a maximum
 between twist-boats (flagpole H–H contact), never a resting minimum.
4. Anti/gauche pairs: anti lower than gauche for butane (qualitative default).

## Examples

### Example 1 — Butane profile + Newman pair

**Prompt:** Build butane anti/gauche teaching assets with an energy profile.

**Emit:**
1. `ConformationalEnergyProfileAsset` with conformers at 60° (gauche), 180° (anti)
2. Two `newman-projection-authoring` assets with cross-linked IDs
3. Shared `accessibility_text` bundle via `chem-representation-accessibility`

### Example 2 — Reject mechanism misuse

**Prompt:** Energy diagram for rotating ethane from staggered to eclipsed during SN2.

**Response:** Separate concerns — conformational scan is `conformational-energy-profile-authoring`; SN2 barrier is `reaction-coordinate-diagram-authoring`. Do not combine on one reaction-coordinate spec.

## Test prompts

- "Plot butane conformer energies vs dihedral angle."
- "Sketch axial vs equatorial methyl preference on cyclohexane."
- "Link Newman projections to each minimum on the profile."

## Failure modes

- Agent emits `ReactionCoordinateSpec` for torsion → wrong skill; rewrite as conformational profile.
- Newman comparison without profile when section title implies energy ranking → add profile or flag gap in `organic-chapter-asset-auditor`.

## Related skills

- `newman-projection-authoring` — paired conformer views
- `reaction-coordinate-diagram-authoring` — mechanisms only
- `organic-chapter-asset-auditor` — Chapter 3 conformation gaps
