# textbook-authoring-skills

> **Scope:** This repository publishes **agent skills and QA artifacts** that
> document how we authored an organic chemistry OER textbook. It is **not** the
> live ChemIllusion product codebase, deployment config, or private monorepo.

A curated, MIT-licensed snapshot of **agent skills for organic chemistry textbook
authoring** — chapter orchestration, reader prose, teaching figures, accessibility,
videos, and question authoring.

This repo was extracted from the ChemIllusion skill tree for a **story on textbook
authoring**. It is a parallel copy, not a live mirror of the product monorepo.

## What’s inside

| Path | Purpose |
|------|---------|
| [`skills/`](skills/) | Duplicated skill folders (`SKILL.md` + references/scripts where present) |
| [`prompts/`](prompts/) | Stand-in prompts for RDKit/agent helpers that were **not** copied |
| [`reports/topic-packages/`](reports/topic-packages/) | Saved multi-persona chapter reviews (md/json + persona envelopes) |
| [`notes/`](notes/) | Cover-to-cover reader chemistry and link-fix notes |
| [`scripts/`](scripts/) | OpenStax–ChemIllusion comparison script (local use only) |
| [`config/`](config/) | Chapter map and molecule alias curation |
| [`CONTENTS.md`](CONTENTS.md) | Full map: included, omitted, and replacements |
| [`LICENSE`](LICENSE) | MIT |

## Quick start

1. Read [`CONTENTS.md`](CONTENTS.md) for the inventory and omissions.
2. Start at `skills/produce-organic-chapter/SKILL.md` (chapter pipeline).
3. When a skill would call molecule validation/rendering agents, use `prompts/` instead.
4. Deck Creator / PPTX / ZoomDeck are out of scope for this repo — focus on reader chapters, figures, and questions.
5. For QA narrative: persona reviews under `reports/topic-packages/`, plus
   [`notes/reader-chemistry-and-link-fixes.md`](notes/reader-chemistry-and-link-fixes.md).

## OpenStax–ChemIllusion comparison (local only)

`scripts/compare_openstax_chemillusion.py` compares OpenStax Organic Chemistry with
ChemIllusion reader chapters on phrase overlap, identical-molecule counts, and figure
taxonomy. It requires a **local checkout of the private ChemIllusion monorepo** and
writes scratch results to ignored `outputs/` directories. Reviewed full-book releases
belong in dated, source-control-visible folders under `reports/comparison/`; cached
PDFs and temporary compiled reader chapters remain local. Set `CHEMILLUSION_ROOT` in
`.env` if the private checkout is not a sibling directory.

The default comparison covers all 31 chapters of John McMurry's OpenStax
*Organic Chemistry: A Tenth Edition* using exact 5-, 8-, 12-, 16-, and 20-word
phrases. Use `--chemillusion-provenance-root` when scoring an isolated compiled
mirror so the run manifest fingerprints the original authored checkout.

## Intentionally not copied

- **Molecule rendering helpers / agents:** `rdkit-agent`, `rdkit-acs-1996-rendering`,
  `rdkit-advanced-rendering`, `rdkit-structure-builder` → see `prompts/`
- **Deck / slide companions:** all `deck-creator-*`, `pptx-deck-creator`,
  `zoomdeck-creator`, `deck-video-integration`, `deck-harness-intent`
- **Graphical abstract / journal club:** not invoked by the textbook pipeline
- **Textbook lens ingestion:** `textbook-ingestion` (product catalog mapping, not chapter prose)
- **Deprecated stub:** `add-organic-chapter` (redirect only)

## License

MIT — see [LICENSE](LICENSE).

## Provenance

Skill text no longer points at ChemIllusion monorepo file paths, internal API
routes, feature-flag names, hosting/database vendor names, or private-repo
commit/issue references. Missing product code is marked with `(not in this
repo)` statements; RDKit stand-ins live under `prompts/`.
The QA artifacts under `reports/topic-packages/` have likewise had literal
answer-key data, grading-exploit disclosures, and backend/frontend source
citations redacted — see [`CONTENTS.md`](CONTENTS.md#provenance-note) for detail.
