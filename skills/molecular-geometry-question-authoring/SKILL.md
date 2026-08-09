---
name: molecular-geometry-question-authoring
description: Author molecular_geometry (VSEPR angle-diagram) questions from the curated 11-geometry catalog. Use when asked to create a molecular-geometry or VSEPR question, quiz common bond angles, or add a geometry example to a question bank, tutorial, or chapter.
---

# Molecular Geometry Question Authoring

Creates valid `molecular_geometry` question items (see proprietary molecular-geometry PRD,
not in this repo). The type is a **curated
teaching-image + selected-response** MVP: one reviewed, committed SVG per
geometry with the important bond angles labeled, graded by the existing
deterministic selected-response grader.

## Use when asked to

- create a molecular-geometry question
- create a VSEPR question
- show or quiz common bond angles
- add a geometry example to a tutorial, question bank, or chapter
- create questions using the 11 supported geometry shapes

## The curated catalog (the ONLY allowed examples)

Source of truth: the proprietary molecular-geometry catalog (not in this repo);
the frontend mirror is `MOLECULAR_GEOMETRY_ASSETS` in the proprietary catalog
module (not in this repo). Assets are committed under proprietary SVG assets
(not in this repo).

| geometry_id | Example | Formula | Angle labels |
|---|---|---|---|
| `linear` | Carbon dioxide | CO2 | 180° |
| `trigonal_planar` | Boron trifluoride | BF3 | 120° |
| `tetrahedral` | Methane | CH4 | 109.5° |
| `bent` | Water | H2O | 104.5° |
| `trigonal_pyramidal` | Ammonia | NH3 | 107° |
| `trigonal_bipyramidal` | Phosphorus pentachloride | PCl5 | 90°, 120°, 180° |
| `seesaw` | Sulfur tetrafluoride | SF4 | ≈90°, ≈120°, 180° |
| `t_shaped` | Chlorine trifluoride | ClF3 | ≈90°, 180° |
| `octahedral` | Sulfur hexafluoride | SF6 | 90°, 180° |
| `square_pyramidal` | Bromine pentafluoride | BrF5 | ≈90°, 180° |
| `square_planar` | Xenon tetrafluoride | XeF4 | 90°, 180° |

## Rules

1. Select only from the curated catalog. **Do not invent a molecule or
 geometry** — if the requested molecule isn't in the table, use the catalog
 example for its geometry (or flag for teacher review in exam conversion).
2. Use the catalog angle labels **exactly**, including the `≈` prefix for
 seesaw, T-shaped, and square-pyramidal non-180° labels.
3. Do not introduce conformational analysis, coordinate optimization, or new
 3D rendering — the committed SVG is the stimulus; the runtime never calls
 RDKit/CineMol/xyzrender.
4. Selected-response questions only in the MVP (`answer_key.correct_option_ids`
 with exactly one correct id).
5. Include an answer-safe `accessible_description` in `response_config` that
 describes the arrangement **without naming the geometry** for
 `identify_geometry` / `match_example` questions (the renderer strips the
 asset's own title/desc precisely because they name the geometry).
6. `show_geometry_name` must be `false` whenever the geometry name is the
 answer (`identify_geometry`, `match_example`); it may be `true` for
 `identify_angle`.
7. Use `angle_label_mode: "one_missing"` + `hidden_angle` (the exact label
 string, e.g. `"120°"`) for angle-identification questions; the base asset is
 reused with a `?` mask — never generate a second SVG.
8. Validate before emitting: the `geometry_id` must be in the catalog, the
 `asset_url` must equal the catalog `asset_url`, and the referenced SVG must
 exist on disk in the proprietary molecular-geometry asset tree (not in this repo).
 `validate_question_spec` enforces the config checks server-side.
9. Question modes: `identify_geometry` ("What is the molecular geometry of
 X?"), `identify_angle` ("What is the A–B–C bond angle?"), `match_example`
 ("Which molecule has <geometry> geometry?").
10. Distractors: pick 3 plausible geometry names (or angle values) from the
 catalog — e.g. shapes with the same electron-domain count or the same
 steric number with different lone-pair counts.

## Output shape (question-bank item)

```json
{
 "question_type_slug": "molecular_geometry",
 "prompt_text": "What is the molecular geometry of BF3?",
 "author_state": {
 "response_config": {
 "mode": "identify_geometry",
 "geometry_id": "trigonal_planar",
 "asset_url": "/assets/molecular-geometry/trigonal-planar-boron-trifluoride.svg",
 "example_name": "Boron trifluoride",
 "formula": "BF3",
 "show_example_name": true,
 "show_formula": true,
 "show_geometry_name": false,
 "angle_label_mode": "all",
 "accessible_description": "A flat triangle of three fluorine atoms around a central boron, with one F–B–F angle labeled 120 degrees.",
 "options": [
 {"id": "a", "text": "Linear"},
 {"id": "b", "text": "Trigonal planar"},
 {"id": "c", "text": "Tetrahedral"},
 {"id": "d", "text": "Trigonal pyramidal"}
 ]
 }
 },
 "answer_key": {"correct_option_ids": ["b"]},
 "grading_rules": {"mode": "deterministic"}
}
```

For `identify_angle`, add `"hidden_angle": "120°"`, set
`"angle_label_mode": "one_missing"`, `"show_geometry_name": true`, and make the
options angle values (90°, 107°, 109.5°, 120°).

## Regenerating assets

Only when the catalog changes:

```bash
# proprietary toolchain (not in this repo)
# proprietary function (not in this repo)
python -m pytest tests/unit/test_services/test_molecular_geometry_catalog.py -q
```

Review each regenerated SVG visually before committing.

## Related

- [question-hint-authoring](../question-hint-authoring/SKILL.md) — hint ladders
 (`molecular_geometry` profile: text hints only)
- [question-explanation-authoring](../question-explanation-authoring/SKILL.md) —
 wrong-answer explanations for the demo/bank fixtures
- [question-figure-authoring](../question-figure-authoring/SKILL.md) — the
 committed asset counts as the question figure (`asset_url`)
