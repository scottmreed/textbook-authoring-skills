# Chapter review — Organic Compounds: Alkanes and Their Stereochemistry (`alkanes-and-stereochemistry`)

_Reviewed 2026-07-30 · chapter version 1 · personas: Instructor, Struggling
Student, Accessibility, Visual Preference_

**Publication readiness: blocked**

The source has a coherent progression, accurate ordinary molecule structures,
and varied assessments. The baseline is blocked because two required questions
are not equivalent across visual and nonvisual use: the functional-group
identification options omit structural descriptions, while the IUPAC item's
accessible description gives away the parent, substituent, and locant.

Chemistry and assessment corrections are also required. The chapter attributes
chemical inertness to intermolecular forces, mischaracterizes ethane's 12 kJ/mol
barrier relative to room-temperature thermal energy, and accepts incomplete or
common names for an IUPAC prompt. Its two conformational profiles and only
Newman teaching asset also fail the inspected reader rendering contracts.

## Top blockers

- **Required functional-group activities are not media-equivalent**
 (`access-001`).
- **The IUPAC accessible description reveals the answer-producing analysis**
 (`access-002`).
- **Physical properties and alkane chemical reactivity are causally conflated**
 (`instructor-001`).
- **The ethane thermal-barrier explanation is quantitatively false**
 (`instructor-002`).
- **The systematic-name key accepts missing locants and a common name**
 (`instructor-003`, `struggle-008`).
- **The core conformation visuals do not meet reader renderer contracts**
 (`visual-001`, `visual-002`).

## Persona status

| Persona | Score | Declared blockers | Headline |
|---|---:|---:|---|
| Organic Chemistry Instructor | 5.2/10 | 3 | Three correctness defects plus alignment gaps |
| Struggling Student | 5.4/10 | 0 | Missing intermediate steps for naming and conformations |
| Accessibility Persona | 7.0/10 | 2 | Two inequivalent required assessments |
| Learner with Visual Preference | 4.2/10 | 2 | Profiles and Newman teaching asset do not render as authored |

## Top recommended changes

1. Provide neutral connectivity descriptions for structure-backed answer
 options.
2. Replace the IUPAC answer-leaking description with a speech-friendly
 rendering of the condensed formula.
3. Correct the reactivity explanation, thermal-barrier explanation, and
 systematic-name key.
4. Preserve the authored conformation profile specs and normalize the Newman
 spec into the reader's renderer contract.
5. Add a worked line-to-Newman sequence and an annotated nomenclature example.
6. Teach ester before assessing it and add an ethane retrieval check.
7. Replace the five dead Wikipedia background links.

## Full evidence

The four independent, schema-valid persona envelopes—including every finding,
evidence anchor, confidence value, strength, and open question—are preserved in
[`chapter-review.json`](chapter-review.json). The synthesized recommendations
deduplicate overlap without altering any persona verdict.

## Preflight and integrity checks

- Source, compiled reader, and compiled question-set identifiers agree.
- Source count: 6 concepts, 6 nuggets, 12 assets, 20 questions.
- Asset/nugget/question cross-references are internally consistent.
- The OpenStax link and `Functional_groups` page resolve; five generated
 Wikipedia section links return 404.

## Correction record

The baseline above was schema-validated before any content edits. Verified
corrections were then applied and recompiled without running the personas a
second time, so the original verdict remains the official baseline.

**Post-correction estimate: major revision** _(not a new persona verdict)_

Applied and verified:

- separated dispersion-force physical properties from covalent-bond/reactivity
 reasoning;
- corrected the room-temperature interpretation of ethane's 12 kJ/mol barrier;
- removed incomplete/common-name answers from the IUPAC item;
- removed the invalid ethane torsion tuple so automatic H–C–C–H selection is
 used;
- qualified functional-group behavior and taught the ester pattern before its
 assessment;
- supplied neutral condensed connectivity for the two structure-backed
 functional-group questions;
- removed the IUPAC accessibility answer leak and aligned Newman activity
 descriptions with their real controls;
- disambiguated both comparison matrices; and
- replaced five dead section links with verified live article mappings.

Still open:

- preserve conformational-profile specs through the reader compiler;
- normalize the authored Newman spec into the renderer's required object;
- add a worked ethane line-to-Newman sequence and a retrieval item;
- add an annotated nomenclature example; and
- show gauche and eclipsed butane before those states are assessed.

Verification: package compile clean (6 concepts, 6 nuggets, 12 assets,
20 questions); topic-package suite **144 passed**; synthesized report schema
valid.
