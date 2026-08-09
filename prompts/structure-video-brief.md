# Prompt: structure video brief (portable)

**Companion to:** `skills/molecule-video-creator/` (copied, but ChemIllusion-API coupled)

Use this prompt when you want a **portable teaching-video brief** for a textbook
chapter without calling ChemIllusion’s `configure_video_parameters` tool.

---

## System / agent instructions

Author one video brief per concept that benefits from motion (bond formation,
conformation change, drawing a scaffold). Do not invent product APIs.

### Brief schema

```json
{
  "id": "alkene-e-z-draw",
  "concept_slug": "alkene-stereochemistry",
  "purpose": "Show drawing of (E)-2-butene with priority labels",
  "smiles": "C/C=C/C",
  "style": "chalk",
  "duration_seconds": 8,
  "narration_beats": [
    "Draw the carbon backbone",
    "Add the double bond",
    "Mark higher-priority substituents on each end"
  ],
  "accessibility": {
    "transcript": "...",
    "alt_poster": "..."
  },
  "defer_if": "No motion advantage over a static figure"
}
```

### Rules

1. Validate `smiles` first (see `prompts/molecule-validation.md`).
2. Prefer chalk/line-draw styles for textbooks; skip decorative AI styles unless requested.
3. If motion does not teach anything new, **defer** and keep a static figure.
4. Always include a poster alt text + short transcript.
