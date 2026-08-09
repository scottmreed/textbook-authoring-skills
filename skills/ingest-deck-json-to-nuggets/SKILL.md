---
name: ingest-deck-json-to-nuggets
description: Analyze extracted textbook deck.json files as private evidence and produce canonical concept and teaching-nugget proposals. Use for Loudon-, Bruice-, or similar source decks when checking topic coverage, examples, misconceptions, assets, or sequence without publishing source-derived prose.
---

# Ingest Deck JSON to Nuggets

Use a source deck as evidence, not as the public content model. Read [references/source-unit-contract.md](references/source-unit-contract.md) before extraction.

## Inputs

Expected shape: `chapters[]`, each with source chapter identity and `slides[]` containing titles, body text, and asset metadata. The known Loudon and Bruice files are examples, not privileged schemas.

## Workflow

1. Parse and inventory source chapters, slides, text blocks, image references, and source locators.
2. Select source units relevant to the requested topic using titles, body terms, and neighboring context.
3. Produce a private evidence report with:
 - source locator;
 - short factual coverage summary in new words;
 - proposed canonical concept slug;
 - proposed nugget purpose/type;
 - misconception or trouble-spot signal;
 - useful representation/asset signal;
 - similarity risk and required human verification.
4. Compare multiple source decks by concept coverage, not chapter number or slide order.
5. Identify consensus coverage, source-specific emphasis, omissions, and conflicting sequences.
6. Hand the report to `author-organic-topic-package`, which makes the canonical authoring decisions.

## Hard boundaries

- Do not write public Deck Creator JSON, asset manifests, reader prose, LMS content, or textbook profiles.
- Do not copy source sentences, source titles, image files, speaker notes, or source slide IDs into public fields.
- Do not promote source sequence into canonical concept order without independent pedagogical justification.
- Do not use one textbook's terminology as the canonical concept slug when a neutral term exists.
- Keep all source locators under private/admin provenance.

## Output

Write a coverage report under `reports/topic-packages/<topic-id>/source-evidence/` or provide an equivalent structured draft. Use the fields in the reference contract. The report may propose nuggets, but it is not itself a canonical package.
