# Contents map — textbook-authoring-skills

This is the authoritative map of the tracked public snapshot. The inventory
below is generated from the Git index; run `python scripts/check_contents.py
--check` to verify it and `--write` to refresh it after a tracked top-level
path changes.

<!-- BEGIN GENERATED REPOSITORY INVENTORY -->

## Generated repository inventory

```text
textbook-authoring-skills/
├── .gitignore               # ignored local tooling, caches, and scratch outputs
├── CONTENTS.md              # this repository map
├── LICENSE                  # MIT license
├── README.md                # project overview and clean-checkout workflow
├── config/                  # chapter map and molecule-alias curation
├── data/                    # tracked placeholders for local cache data
├── notes/                   # dated reader chemistry and link-fix notes
├── outputs/                 # tracked placeholders for ignored local analysis outputs
├── prompts/                 # portable stand-ins for omitted helper agents
├── reports/                 # dated QA snapshots and curated comparison releases
├── requirements.txt         # optional Python tooling dependencies
├── scripts/                 # reproducible repository helper scripts
├── skills/                  # authoring and review skill packages
└── tests/                   # automated regression checks
```

<!-- END GENERATED REPOSITORY INVENTORY -->

## How to read this collection

The repository combines reusable authoring methods with evidence from one
historical product framework. To build a new textbook, adapt the portable
methods to your own subject expertise, source documents, content model,
publishing tools, and evaluation suite. The recommended composition is:

1. `syllabus-to-reader-outline` for scope and learning goals.
2. `author-organic-topic-package` and `organic-textbook-reader-content` for
   authored material in your own schema.
3. `organic-chapter-asset-auditor`, the relevant figure skills, and
   `chem-representation-accessibility` for teaching assets.
4. The question-authoring skills for assessments that match the prose and
   figures.
5. `review-organic-chapter`, subject-matter review, learner testing, and your
   own automated evaluations before publication.

`produce-organic-chapter` is the historical working example of how we chained
those methods in the original framework. It is intentionally product-coupled:
its registries, seed process, runtime variants, paid behavior, and services are
examples to replace, not infrastructure supplied by this repository.

## Included skills (`skills/`)

### Orchestration and review

| Skill | Role | Portability |
|---|---|---|
| `produce-organic-chapter` | Historical end-to-end chapter-production example | Product-coupled reference |
| `review-organic-chapter` | Multi-persona QA, finding schema, and validation script | Adaptable review method |
| `syllabus-to-reader-outline` | Syllabus-to-reader and figure plan | Adaptable planning method |
| `organic-chapter-asset-auditor` | Missing-figure audit | Adaptable audit method |

*Omitted:* `add-organic-chapter` (deprecated redirect only).

### Content and prose

| Skill | Role |
|---|---|
| `author-organic-topic-package` | Concepts, nuggets, assets, and question sets, with contract reference |
| `organic-textbook-reader-content` | Reader content and textbook bridges |
| `ingest-deck-json-to-nuggets` | Private source-deck evidence to nugget proposals |
| `chemistry-text-normalizer` | Subscript, Greek, and OCR-cleanup conventions |

### Figure, accessibility, and video assets

| Skill | Role |
|---|---|
| `newman-projection-authoring` | Newman projections |
| `reaction-coordinate-diagram-authoring` | Mechanism energy diagrams |
| `conformational-energy-profile-authoring` | Torsional and ring-flip profiles |
| `orbital-overlay-assets` | Orbital overlays |
| `synthesis-roadmap-authoring` | Multistep synthesis maps |
| `ir-vibration-asset-authoring` | IR vibration figures |
| `nmr-spectrum-figure-authoring` | NMR traces |
| `molecule-svg-drawing` | Skeletal drawing conventions |
| `ring-closure-tutor-sugar-tool` | Sugar Fischer/ring forms |
| `chem-representation-accessibility` | Alt text and transcripts |
| `molecule-video-creator` | Structure video; product-coupled, with a portable prompt alternative |

### Questions

| Skill | Role |
|---|---|
| `question-figure-authoring` | Stimulus figures |
| `question-explanation-authoring` | Wrong-answer explanations |
| `question-hint-authoring` | Hint ladders |
| `molecular-geometry-question-authoring` | VSEPR and geometry items |
| `qm9s-ir-question-updater` | Calculated IR for vibration questions |

## Prompts instead of molecule-rendering agents (`prompts/`)

These helpers were not copied because they require unavailable CLI agents or
product services. Use the stand-in prompts when a chapter skill calls for their
capability:

| Prompt | Replaces |
|---|---|
| `molecule-validation.md` | `rdkit-agent` |
| `molecule-render-acs-1996.md` | `rdkit-acs-1996-rendering` |
| `molecule-render-styled.md` | `rdkit-advanced-rendering` |
| `molecule-structure-build.md` | `rdkit-structure-builder` |
| `structure-video-brief.md` | Portable alternative to the structure-video API |

## Out of scope

- Deck, slide, PPTX, ZoomDeck, graphical-abstract, and journal-club workflows.
- Product catalog, runtime, database, and deployment work.
- The product-specific implementations behind `(not in this repo)` references.

## Dated QA snapshots (`reports/topic-packages/`)

See [`reports/topic-packages/README.md`](reports/topic-packages/README.md)
before opening individual reviews. They are point-in-time QA evidence, not
claims about the current released textbook.

| Artifact | Description |
|---|---|
| `CHAPTER_REVIEW_STATUS.md` | Concise dated index of the saved review snapshots |
| `<topic>/chapter-review.md` | Human-readable multi-persona report |
| `<topic>/chapter-review.json` | Structured findings and corrections |
| `<topic>/coherence-pass.md` | Coherence notes, where present |
| `<topic>/persona-*`, `persona-returns/`, `persona-envelopes/` | Raw persona envelopes, where present |
| `<topic>/review-submission.json` | Submission payload, where present |

## Curated comparisons (`reports/comparison/`)

Dated comparison releases are intentionally version-controlled. They contain
the published results, figures, and public-safe provenance manifests for a
specific run; they are not ignored scratch output. Run manifests contain input
hashes and source commit state, never local paths, source-repository identity,
branches, or repository-wide dirty-file lists.

## Provenance and history

The skills are substantially decoupled from the original product, not fully
product-neutral. They retain selected terminology and `(not in this repo)`
markers where that preserves the workflow’s meaning. The reports and notes are
historical QA material and retain selected implementation details, identifiers,
and product context. Read their dates and the surrounding historical wrapper;
do not interpret a snapshot finding, test count, deployment reference, or
publication assessment as a statement about the current textbook.
