# Contents map — textbook-authoring-skills

Snapshot of agent skills used to author organic textbook **content and assets**
(reader chapters, topic packages, teaching figures, videos, questions). Sourced
from ChemIllusion’s skill tree for a publishable textbook-authoring story.

---

## Layout

```
textbook-authoring-skills/
├── LICENSE                 # MIT
├── README.md
├── CONTENTS.md             # this file
├── .gitignore
├── skills/                 # duplicated skill folders (SKILL.md + refs)
├── prompts/                # stand-in prompts for agents / RDKit helpers not copied
├── reports/topic-packages/ # persona-based chapter reviews (32 topics)
└── notes/                  # corpus-wide reader fix writeups
```

---

## Included skills (`skills/`)

### Orchestration & QA

| Skill | Role |
|-------|------|
| `produce-organic-chapter` | End-to-end chapter pipeline (canonical entry) |
| `review-organic-chapter` | Multi-persona QA + finding schema / scripts |

*Omitted:* `add-organic-chapter` (deprecated redirect only).

### Content & prose

| Skill | Role |
|-------|------|
| `author-organic-topic-package` | Concepts, nuggets, assets, question sets (+ contract ref) |
| `organic-textbook-reader-content` | PWA reader catalog / bridges / McMurry links |
| `ingest-deck-json-to-nuggets` | Private source decks → nugget proposals |
| `chemistry-text-normalizer` | Subscripts / Greek / OCR cleanup conventions |

### Planning & audit

| Skill | Role |
|-------|------|
| `syllabus-to-reader-outline` | Syllabus → reader/deck plan + figure needs |
| `organic-chapter-asset-auditor` | Missing-figure audit |

### Figure / teaching-asset authoring

| Skill | Role |
|-------|------|
| `newman-projection-authoring` | Newman projections |
| `reaction-coordinate-diagram-authoring` | Mechanism energy diagrams |
| `conformational-energy-profile-authoring` | Torsional / ring-flip profiles |
| `orbital-overlay-assets` | Orbital overlays |
| `synthesis-roadmap-authoring` | Multistep synthesis maps |
| `ir-vibration-asset-authoring` | IR vibration figures |
| `nmr-spectrum-figure-authoring` | NMR traces |
| `molecule-svg-drawing` | Hand/SVG skeletal conventions |
| `ring-closure-tutor-sugar-tool` | Sugar Fischer/ring forms (product-coupled) |
| `chem-representation-accessibility` | Alt text / transcripts |

### Video

| Skill | Role |
|-------|------|
| `molecule-video-creator` | Structure video (ChemIllusion-coupled; see portable prompt) |

### Questions

| Skill | Role |
|-------|------|
| `question-figure-authoring` | Stimulus figures |
| `question-explanation-authoring` | Wrong-answer explanations |
| `question-hint-authoring` | Hint ladders |
| `molecular-geometry-question-authoring` | VSEPR / geometry items |
| `qm9s-ir-question-updater` | Attach calculated IR to vibration questions |

---

## Prompts instead of molecule-rendering agents (`prompts/`)

These were **not** copied (CLI agent or heavy product RDKit service skills).
Use the prompts when a chapter skill would have invoked them:

| Prompt | Replaces |
|--------|----------|
| `molecule-validation.md` | `rdkit-agent` |
| `molecule-render-acs-1996.md` | `rdkit-acs-1996-rendering` |
| `molecule-render-styled.md` | `rdkit-advanced-rendering` |
| `molecule-structure-build.md` | `rdkit-structure-builder` |
| `structure-video-brief.md` | Portable alternative to `molecule-video-creator` API |

---

## Out of scope (not copied)

### Deck / slide companions

Intentionally excluded from the story repo:

- `deck-creator-content`
- `deck-creator-concept-authoring`
- `deck-creator-dynamic-chem-assets`
- `deck-video-integration`
- `deck-harness-intent`
- `pptx-deck-creator`
- `zoomdeck-creator`

**During textbook writing:** `produce-organic-chapter` / the auditor may *mention*
Deck Creator for verification or placeholder replacement. That is product
packaging, not required for reader chapter prose + figures.

### Graphical abstract / journal club

**Double-check result:** not called by the textbook chapter skills listed above.
Do not copy `graphical-abstract-pipeline` or journal-club workflows.

### Infrastructure (skipped)

Not part of day-to-day textbook writing:

- `teaching-asset-kind-registration`
- `visual-capability-registry`
- `course-reader-builder` (teacher course reader at `/chemed/readers`, not the organic PWA)
- `textbook-ingestion` (add a textbook *lens* / mapping — product catalog work, not chapter prose)

### Optional polish (skipped)

- `kling-character-overlays` (mascot overlays on videos)

---

## Persona-based reviews (`reports/topic-packages/`)

Copied from ChemIllusion `reports/topic-packages/` for the textbook-authoring story.

| Artifact | Description |
|----------|-------------|
| `CHAPTER_REVIEW_STATUS.md` | Corpus status tally |
| `<topic>/chapter-review.md` | Human-readable multi-persona review report |
| `<topic>/chapter-review.json` | Structured findings + corrections |
| `<topic>/coherence-pass.md` | Coherence notes (where present) |
| `<topic>/persona-*` / `persona-returns/` / `persona-envelopes/` | Raw persona envelopes (subset of chapters) |
| `<topic>/review-submission.json` | Submission payload (where present) |

**32 topic folders** with `chapter-review.md` + `.json` (acids/bases through synthetic polymers, plus biomolecules, spectroscopy, etc.).

Personas (from `review-organic-chapter`): instructor, struggling student, accessibility, visual preference.

## Reader fix notes (`notes/`)

| File | Description |
|------|-------------|
| `reader-chemistry-and-link-fixes.md` | How cover-to-cover audits produced tier-1 and tier-2 reader fix batches in the private ChemIllusion monorepo, including the tier-2 chemistry table and tier-1 barrier/dead-link summary |

## Suggested story reading order

1. `produce-organic-chapter` — how a chapter is built  
2. `author-organic-topic-package` + `references/topic-package-contract.md`  
3. `organic-chapter-asset-auditor` → figure skills → `chem-representation-accessibility`  
4. Question trio (`question-figure` / `explanation` / `hint`)  
5. `review-organic-chapter` personas + sample `reports/topic-packages/*/chapter-review.md`  
6. `notes/reader-chemistry-and-link-fixes.md` — corpus-wide chemistry/link pass  
7. `prompts/*` when structures need validate/render without RDKit agents  

---

## Provenance note

Skills are **duplicates** for storytelling and review. Product monorepo paths
(`frontend/…`, `backend/…`, `docs/…`, `content/organic/…`), internal API routes,
feature-flag names, hosting/database vendor names, private-repo commit and issue
references, and AI-generation cost figures have been removed from skill text and
replaced with `(not in this repo)` statements. Omitted helpers point at `prompts/`
where a portable stand-in exists.

Persona reviews and reader fix notes are historical QA artifacts from the ChemIllusion
reader corpus; they may name internal slugs, block IDs, and product URLs. A second
redaction pass over `reports/topic-packages/` has removed literal answer-key data
(`answer_key`, `correct_option_ids`, `expected_*`, graded SMILES/atom-id values),
whole-bank grading-positional-bias disclosures, backend/frontend source file and
line citations, pricing-tier constants, and private-repo commit references. A small
number of narrative sentences describing specific graded questions may still name
an option/atom id in free prose rather than a structured field — treat any such
mention you find as informational QA history, not as current live assessment data.
