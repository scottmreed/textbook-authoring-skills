---
name: chemistry-text-normalizer
description: Heuristic recovery of chemistry subscripts, superscripts, arrows, and Greek letters from OCR-mangled text. Use when normalizing chemistry notation in review UIs or extending glyph recovery patterns.
---

# Chemistry Text Normalizer

**Type:** Development skill
**Last verified against main:** 2026-06-22
**Implementation:** proprietary normalization service and chemistry-text UI module (not in this repo). Stage 2 normalization runs after segment cleanup in the proprietary ingestion pipeline (not in this repo).

## Purpose

Heuristic recovery of chemistry subscripts, superscripts, arrows, and Greek letters from OCR-mangled text.

## When to use

- Processing OCR-mangled chemistry strings that have broken formulas or notation
- Rendering chemistry text in the tutorial review UI with proper subscripts and superscripts
- Debugging cases where LLM verification rewrites a normalized prompt
- Extending glyph recovery patterns for new chemistry symbols or abbreviations

## Key files

- proprietary normalization service (not in this repo) — normalization logic
 - Export: `normalize_chemistry_text(raw_text) -> NormalisationResult`
 - Contains: `_SUBSCRIPT_MAP`, `_SUPERSCRIPT_MAP`, glyph patterns
- proprietary chemistry-text UI module (not in this repo) — UI rendering
 - Export: `renderChemText(text) -> React.ReactNode`
 - Export: `ChemText` component for JSX use

## Pipeline context

**Stage 2 (Text Normalization)** — Applied after `clean_segment_text` on each question's prompt text.

Produces `NormalisationResult` with:
- `normalized_text: str` — recovered chemistry notation
- `changes: List[str]` — list of glyphs corrected
- `missed_glyph_patterns: List[str]` — patterns that could not be recovered
- `confidence: float` — confidence in the normalization

## Self-update triggers

- **LLM verification call rewrites a normalized prompt** in a way that touches a glyph not in `_SUBSCRIPT_MAP` or `_SUPERSCRIPT_MAP` → add new glyph mapping
- **`missed_glyph_patterns` is non-empty** for a question in a review queue → prioritize adding those patterns
- **`changes` list is empty but the LLM's `teacher_intent_summary` suggests formula errors** → review regex patterns for false negatives

## Usage notes

- Operates post-OCR on question text only; does not modify answer text
- Maps common OCR artifacts (e.g., "H2O" → "H₂O", "H+" → "H⁺", "arrow" → "→")
- Proprietary `ChemText` UI component (not in this repo) auto-renders normalized text for display in modals and review UI
- Glyph mappings are conservative: only patterns with high confidence are normalized
