---
name: qm9s-ir-question-updater
description: Verify exact QM9S calculated IR spectra, attach them to existing ChemIllusion `molecular_vibration` questions, add reviewed band annotations, and reformat spectrum-linked questions without leaking answers. Use when asked to add QM9S spectra, upgrade IR questions, annotate vibration bands, or audit existing vibration questions for verified spectrum coverage.
---

# QM9S IR Question Updater

Safely upgrade existing `molecular_vibration` questions with **calculated** IR
spectra from the **QM9S** dataset (Figshare v3, CC BY 4.0, B3LYP/def-TZVP). This
skill is **dry-run first**: it inspects, verifies exact molecular identity, and
reports a plan before any record changes. It never substitutes a similar molecule
and never leaks an answer.

Read the QM9S IR spectra PRD before acting (proprietary documentation, not in
this repo). This skill operationalizes that PRD; it builds **on top of** the
shipped curated 3Dmol.js vibration system (see
[`ir-vibration-asset-authoring`](../ir-vibration-asset-authoring/SKILL.md)) and
the Interactive Vibrations / IR question PRD (proprietary documentation, not in
this repo).

## What it touches

- **Questions:** the `molecular_vibration` type only — proprietary type
  definition, validation (`_validate_molecular_vibration_config`), and
  question-bank editor UI (not in this repo).
- **Approved spectra:** proprietary IR spectrum assets (not in this repo) —
  runtime index plus per-spectrum JSON (produced offline; never fetched from
  Figshare at runtime).
- **Spectrum ↔ mode links:** proprietary `IrSpectrumModeLink` data (not in this
  repo; confidence `verified` / `reviewed` / `illustrative`).
- **Apply path:** only the proprietary updater script (not in this repo) —
  never hand-edit question JSON to force a change.

## Expected repository components

Slice A shipped these as the real components this skill operates on and through
(replacing any earlier "suggested pipeline files" language in the PRD). All are
proprietary (not in this repo):

- Identity service — offline exact-identity resolution (InChIKey → canonical
  isomeric SMILES).
- Spectrum processing service — spectrum normalization, resampling, and
  validation.
- Spectrum catalog — versioned catalog (`get_spectrum_by_inchikey`).
- Offline ingestion CLI — the only script that reads the local QM9S source
  files (see localhost data-source note below).
- Dry-run-first apply/rollback updater (see "Apply path" above).
- Runtime spectrum index — produced by the ingestion CLI; empty/absent until a
  spectrum has been ingested.
- `VibrationSpectrumViewer` — combined animation + spectrum viewer (see "Where
  it appears" below).
- `IrSpectrumCanvas` — IR-specific spectrum trace, extracted alongside the NMR
  canvas.
- `GenericSpectrumCanvas` — shared base canvas reused by both
  `NmrSpectrumCanvas` and `IrSpectrumCanvas` (PRD §7 refactor).

## Localhost-only data sources

The two raw QM9S source files (`ir_boraden.csv` and the `qm9s_csv/` directory of
per-molecule CSVs) live only in the proprietary codebase (localhost data; not in
this repo). They are **~18 GB** combined, are `.gitignore`d, and must **never**
be committed. The **only** code that reads them is the proprietary ingestion CLI
(not in this repo) — no other script, service, or runtime path touches these raw
files.

**Join rule:** for molecule index *n*, `qm9s_csv/{n:06d}.csv` (zero-padded to 6
digits) joins to row `n-1` (0-indexed) of `ir_boraden.csv`.

Interactive band selection (`select_spectrum_band` question template and the
`IrSpectrumModeLink` record described in the PRD) is **Slice B, not yet built** —
it requires human-reviewed band assignments and is out of scope for this skill's
current dry-run/passive-attach behavior.

## Behavior

1. Resolve the requested scope: bank, course, chapter, question IDs, or mode scope.
2. Inspect **only** `molecular_vibration` questions.
3. Resolve exact molecule identity using the approved catalog (InChIKey → canonical
   isomeric SMILES → canonical nonisomeric SMILES only when neither record has
   unresolved stereochemistry). Identity uses the existing RDKit tooling
   ([`rdkit-agent` → prompts/molecule-validation.md](../../prompts/molecule-validation.md)).
4. Find an approved QM9S spectrum in the proprietary IR spectrum index (not in
   this repo).
5. Verify dataset, version (`figshare_v3`), license (CC BY 4.0), checksum, exact
   identity, and runtime schema.
6. Find an approved `IrSpectrumModeLink` when annotation is required.
7. Decide: add a **passive** spectrum, or migrate to an **interactive** band
   question — only when an exact spectrum **and** a `reviewed`/`verified`
   assignment exist.
8. Prevent answer leakage (pre-submit display never reveals the target band/range).
9. Preserve attribution in the record and in every export.
10. Produce a **dry-run report** before changing any record.
11. Apply changes **only** through the supported updater script.
12. Run validation, tests, and previews; report the rollback identifiers.

## Hard constraints

- **Default to dry-run.** No writes until explicitly confirmed.
- Never substitute a similar molecule.
- Never match by formula or name alone.
- Never attach a different tautomer, charge state, isotope, stereoisomer, or
  constitutional isomer.
- Never describe QM9S spectra as experimental — they are **calculated**.
- Never omit CC BY 4.0 attribution.
- Never call an assignment `verified` without explicit **source-level** evidence.
- Never reveal the target frequency or band before submission when that would
  answer the question.
- Never alter the 3D structure to force a match.
- Never fetch the full QM9S dataset during runtime.
- Never use NIST, SDBS, or any other restricted source as a silent fallback.
- Preserve rollback data for **every** applied update.

## Required dry-run outcomes

Each inspected question ends in exactly one of:

```text
updated_passive_spectrum
updated_interactive_band
no_exact_qm9s_match
no_reviewed_band_assignment
already_current
blocked_validation_error
requires_human_review
```

## Required report columns

```text
question_id
mode_id
molecule
identity_match_method
spectrum_id
spectrum_checksum
assignment_link_id
assignment_confidence
current_template
proposed_template
answer_key_changed
warnings
proposed_action
```

## Stop conditions (do not apply)

- no exact match exists;
- source version is not pinned;
- checksum or license metadata is missing;
- spectrum arrays fail validation;
- an interactive question lacks a `reviewed`/`verified` assignment;
- the proposed display leaks the answer;
- the answer key cannot be migrated deterministically;
- rollback data cannot be stored;
- tests fail.

## Where it appears

- Live reader / preview: the combined `VibrationSpectrumViewer` (existing
  `VibrationViewer` animation + `IrSpectrumCanvas`), reused by reader live
  rendering and asset preview — proprietary UI (not in this repo).
- Accessibility transcript patterns for the animated mode + spectrum:
  [`chem-representation-accessibility`](../chem-representation-accessibility/SKILL.md)
  and a proprietary WCAG audit skill (not in this repo).
- Authoring the vibration mode itself (upstream of this skill):
  [`ir-vibration-asset-authoring`](../ir-vibration-asset-authoring/SKILL.md).
