# textbook-authoring-skills

> **Scope:** This repository publishes agent skills and dated QA artifacts that
> document how we authored an organic chemistry OER textbook. It does not
> contain the live product codebase, deployment configuration, or a complete
> standalone textbook platform.

This is a curated, MIT-licensed snapshot of the organic chemistry authoring
workflow: chapter planning, reader prose, teaching figures, accessibility,
videos, question authoring, and review. It is a parallel historical copy of the
skills used for the textbook-authoring story, not a live product mirror.

## What’s inside

| Path | Purpose |
|------|---------|
| [`skills/`](skills/) | Authoring and review skill folders, with references/scripts where present |
| [`prompts/`](prompts/) | Stand-in prompts for omitted molecule-rendering helpers |
| [`reports/topic-packages/`](reports/topic-packages/) | Dated multi-persona chapter-review snapshots |
| [`reports/comparison/`](reports/comparison/) | Curated full-book comparison release artifacts |
| [`notes/`](notes/) | Dated reader-chemistry and link-fix notes |
| [`scripts/`](scripts/) | Comparison and repository-maintenance scripts |
| [`config/`](config/) | Chapter map and molecule-alias curation |
| [`CONTENTS.md`](CONTENTS.md) | Generated-checked inventory, skill map, and exclusions |

## Use these skills to build a new textbook

Treat the collection as composable methods, not as a drop-in textbook product.
Bring your own subject-matter expertise, source documents and licenses, content
schema, publishing tools, and evaluation process. A practical sequence is:

1. Use `syllabus-to-reader-outline` to establish scope and learning goals.
2. Use `author-organic-topic-package` and `organic-textbook-reader-content` to
   author your chapters in your own content model.
3. Run `organic-chapter-asset-auditor`, then apply the relevant figure and
   accessibility skills to fill teaching-asset gaps.
4. Use the question-authoring skills to create assessments aligned to what the
   chapter actually teaches.
5. Use `review-organic-chapter` and your own subject experts, learner testing,
   and automated checks before publishing.

[`produce-organic-chapter`](skills/produce-organic-chapter/SKILL.md) is a useful
working example of how we chained those skills inside our original framework.
It deliberately retains historical references to proprietary registries,
runtime behavior, services, and evaluation expectations. A new textbook needs
its own framework, documentation, data contracts, and evaluations in their
place.

## Optional local tooling

The checked snapshot was tested with Python 3.14.6. To run the optional
comparison tooling and regression checks from a clean checkout:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
MPLCONFIGDIR=/tmp/textbook-authoring-mpl python -m unittest discover -s tests -v
```

## OpenStax–ChemIllusion comparison

`scripts/compare_openstax_chemillusion.py` compares OpenStax Organic Chemistry
with compiled reader chapters on phrase overlap, identical-molecule counts, and
figure taxonomy. It supports a local source tree or a compiled snapshot for
testing. Write scratch runs under ignored `outputs/`; reviewed, curated releases
belong in dated folders under [`reports/comparison/`](reports/comparison/).

Public comparison manifests deliberately record only the source commit, whether
the selected inputs were dirty, and content hashes. They never record local
paths, source-repository identity, branches, or repository-wide status output.

## Intentionally not copied

- Molecule-rendering helpers and agents: use the portable prompts in `prompts/`
  instead.
- Deck, slide, PPTX, and ZoomDeck companion workflows.
- Product catalog and infrastructure workflows that are not required to author
  reader prose, figures, and questions.
- The deprecated `add-organic-chapter` redirect stub.

## Provenance and historical context

The authoring skills have been substantially decoupled from the original
product, but they are not uniformly portable. Some retain selected
product-coupled terminology or `(not in this repo)` placeholders so the original
workflow remains intelligible. The QA artifacts under `reports/topic-packages/`
are dated historical evidence; they retain selected identifiers and
implementation details for context and are not statements about the current
released textbook. See [`CONTENTS.md`](CONTENTS.md#provenance-and-history) and
[`reports/topic-packages/README.md`](reports/topic-packages/README.md) before
interpreting them.

## License

MIT — see [LICENSE](LICENSE).
