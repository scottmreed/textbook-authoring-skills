---
name: chem-representation-accessibility
description: Generates accessibility text (alt text and longer transcripts) for chemistry-native teaching figures — Newman projections, reaction coordinate diagrams, orbital overlays, stereochemistry, chair conformations, and molecules. Use for reader, deck, LMS, and PDF exports requiring WCAG-aligned figure descriptions.
---

# Chem Representation Accessibility

Every `ChemTeachingAsset` **must** include `accessibility_text`. This skill produces concise alt text plus optional longer transcripts consumable by reader export, deck speaker notes, and LMS alt-text fields.

**Pair with:** proprietary skill (not in this repo) for conformance documentation.

## Output bundle

```ts
export type AccessibilityBundle = {
 alt_text: string; // ≤ ~150 chars for slide/LMS alt fields
 transcript: string; // 2–5 sentences for notes/captions
 figure_type: ChemTeachingAsset["type"];
 locale?: string; // default "en"
};
```

Attach to parent asset as `accessibility_text` (alt) and `accessibility_transcript` (optional extended field in export metadata).

## Readout patterns

### Newman projection

Include: viewing axis (which bond), front/back substituents by position (top, left, right), conformer relationship (staggered/eclipsed/anti/gauche), dihedral if known.

**Alt:** `Newman projection along C2–C3: front top methyl, front left hydrogen; back top methyl; staggered gauche conformer.`

**Transcript:** `The diagram views down the carbon 2 to carbon 3 bond. On the front carbon, a methyl group points up and hydrogen points left. On the back carbon, a methyl points up, giving a gauche relationship between the two methyl groups.`

### Reaction coordinate diagram

Include: number of steps, labeled minima (reactants, intermediates, products), which step has the largest barrier if RDS is pedagogical, unitless/schematic caveat.

**Alt:** `Reaction coordinate: two-step profile with carbocation intermediate; first step has the higher barrier.`

### Conformational energy profile

Include: x-axis quantity (dihedral or flip progress), named minima and relative ordering.

### Orbital overlay

Include: overlay type (pi bond, lone pair, pi*), **not computed MO** disclaimer, phase color meaning if shown.

### Stereochemistry / chair

Include: R/S or E/Z when known; axial/equatorial positions for chair; wedge/dash orientation in transcript.

### Molecule figure

Include: IUPAC or common name, key functional groups, stereochemistry notation if present.

## Rules

1. **Alt text** — one or two sentences; no "image of" prefix.
2. **Transcript** — teach the figure; do not repeat alt text verbatim.
3. **Never** claim computed energies or MOs unless asset metadata says so.
4. Same bundle feeds reader (`accessibility` block), deck notes, IMSCC alt fields.
5. For animated GIF/MP4, describe **start and end states** and what motion conveys.

## Question accessibility text never reveals the answer

The readout patterns above are for **reader / deck / PDF** figures, where stating
the pedagogical point ("first transition state is highest", "anti conformer")
is exactly right. When the **same figure backs a question** — a
`ChemTeachingAsset` inside a question's `accessibility_bundle.accessible_description`,
or a demo fixture's `accessible_description` — the description is the non-visual
equivalent of the stimulus and must convey the **task, not the solution**. A
screen-reader user must have to reason to the answer just like a sighted student.

Describe what is shown and what to do; never the verdict, the values, or the
grouping the student is being asked to produce.

| Context | Answer-stating OK? | Example |
|---|---|---|
| Reader / deck figure | Yes | "…the first transition state is highest, so ionization is rate-determining." |
| Same figure in a question | **No** | "A two-step energy profile; identify the rate-determining step and the overall direction." |

Before/after (IR peak-selection question):
- **Leaks:** "…select the strong band near 1715 — the carbonyl stretch."
- **Neutral:** "An IR spectrum with three labelled absorptions at 2950, 1715,
 and 1100 cm⁻¹; select the band for the functional group named in the question."

**Guard:** the proprietary accessibility-leak checker (not in this repo) flags
answer ids, classification verdicts (anti, beta, exergonic, singlet…),
and computed answer numbers not visible in the stimulus. It runs over every demo
fixture in `test_accessibility_answer_leaks.py` and at chapter-compile time via
the proprietary question-set validator (not in this repo), so an answer-stating
question description fails the build. Numbers/words that also
appear in the prompt or student_config are stimulus-visible and allowed.

## Examples

### Example 1 — Butane anti Newman

**Input:** `NewmanProjectionTeachingAsset` preset `butane_anti`.

**Output:**
- alt: `Newman projection, butane anti conformer: methyl groups 180 degrees apart on front and back carbons.`
- transcript: `Looking down the central C–C bond of butane in the anti conformation, the two methyl substituents are on opposite sides (top front and bottom back), minimizing steric clash.`

### Example 2 — SN1 diagram

**Input:** Two-step reaction coordinate with carbocation.

**Output:**
- alt: `Energy diagram: reactants, carbocation intermediate, products; first transition state is highest.`
- transcript: `The reaction proceeds in two steps with a carbocation intermediate between reactants and products. The first activation barrier is larger, indicating the leaving group departure is rate-determining. Diagram is schematic and not drawn to quantitative scale.`

## Test prompts

- "Write accessible text for a butane gauche Newman projection."
- "Generate alt text and transcript for an SN2 one-step energy diagram."
- "Add LMS-ready descriptions for these three deck figures."

## Failure modes

- Empty `accessibility_text` on any teaching asset → blocking error for authoring skills.
- Alt text > 250 chars → trim for alt; keep detail in transcript.
- Claiming "computed orbital" for curated overlay → add qualitative disclaimer.

## Shared schema reference

All figure skills emit into:

```ts
export type ChemTeachingAsset =
 | { type: "molecule"; id: string; title: string; smiles: string; accessibility_text: string }
 | { type: "newman_projection"; id: string; title: string; object: NewmanProjectionObject; accessibility_text: string }
 | { type: "reaction_coordinate"; id: string; title: string; spec: ReactionCoordinateSpec; video?: SlideVideoSpec; accessibility_text: string }
 | { type: "conformational_energy_profile"; id: string; title: string; spec: ConformationalEnergyProfileAsset; accessibility_text: string }
 | { type: "orbital_overlay"; id: string; title: string; manifest_id: string; accessibility_text: string }
 | { type: "stereochemistry_conversion"; id: string; title: string; spec: unknown; accessibility_text: string };
```

Future code home: proprietary accessibility bundle module (not in this repo;
docs-only for now).
