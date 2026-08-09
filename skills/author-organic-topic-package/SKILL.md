---
name: author-organic-topic-package
description: Author and compile textbook-agnostic organic chemistry topics as canonical concept nodes and teaching nuggets. Use when asked to add a topic such as epoxides to teacher tools, Deck Creator, assets, videos, review queues, concept maps, readers, LMS outputs, or textbook sequences.
---

# Author Organic Topic Package

Create one canonical package, then compile every teacher-facing representation from it. Do not hand-author a new deck chapter, asset manifest, review file, or textbook profile independently.

Read [references/topic-package-contract.md](references/topic-package-contract.md) before authoring.

## Terminology

- **Canonical concept node:** stable textbook-independent idea in the concept graph.
- **Teaching nugget:** reusable instructional unit with one purpose, objectives, three text variants, practice, and linked media.
- **Removable optional topic:** teacher-optional subset compiled to the proprietary optional-topic registry (not in this repo). This is not a synonym for canonical concept node.
- **Textbook lens:** labels, chapter locators, and sequence alignment over canonical concepts. It never owns canonical prose.

## Workflow

1. Inspect:
 - the proprietary topic-package corpus (not in this repo)
 - nearby compiled chapters and textbook lenses
 - the proprietary package validator and schema (not in this repo)
 - legacy deck references, if any.
2. Search the two private proprietary deck corpora (not in this repo) only when useful for coverage comparison. If extracting source evidence, invoke `ingest-deck-json-to-nuggets`. Never copy source prose, titles, slide order, or images.
3. Create the topic-package JSON (proprietary assets, not in this repo).
4. Model the topic:
 - stable concept slugs, prerequisites, order, difficulty, trouble spots, representations;
 - one nugget per reusable teaching purpose;
 - complete `terse`, `standard`, and `expanded` text;
 - renderer-backed editable assets with required alt text;
 - video briefs for concepts that materially benefit from motion;
 - neutral textbook matching terms and private evidence provenance.
5. Validate in isolation:

 ```bash
 # proprietary function (not in this repo)
 ```

6. Inspect the compile report and all textbook mappings. Fix weak or incorrect mappings with explicit package overrides; do not change canonical content to fit a book.
7. Compile into runtime files:

 ```bash
 # proprietary function (not in this repo)
 ```

7a. Verify reader chapter + LMS module were compiled:
 ```bash
 # proprietary assets (not in this repo)
 ```
 If the files are missing, run compile with `--write-runtime` again.

8. Verify:
 - Deck Creator manifest and topic registry contain the topic.
 - all listed textbooks have a profile mapping;
 - review manifest contains `deck_text`, `deck_figure`, and applicable `deck_video_brief` tasks;
 - assets begin `science_review.status: not_reviewed`;
 - videos begin `needs_review`;
 - concept-map seed discovery includes the package;
 - public outputs contain no source branding or source media paths.

## Prose tone (required)

Write in the register of a published textbook, not a blog post or a chat reply. Reviewers reject prose that "reads like AI."

- **Formal and impersonal.** Third person, declarative sentences. Do not address the reader as "you," and avoid imperative openers and conversational hooks: no "Start with…", "Here is the master mechanism…", "The interesting part is…", "The classic trap is…", "is almost free", "worth reading slowly." State the chemistry directly.
- **No personification of molecules or electrons.** Molecules do not "want," "grab," "reach out," "look for," "drop onto," or "commit to a carbocation at the top of a hill." Use neutral verbs: *attacks, forms, adds, is protonated, donates a lone pair, predominates*.
- **Distinct, genuinely rescaled tiers.** `terse` = one sentence; `standard` = one compact paragraph; `expanded` = 2–3 paragraphs of connected explanation. Do not pad the expanded tier with narration about the diagram or with meta-commentary.
- **Formulas.** Prefer Unicode subscripts/superscripts and symbols in prose and titles (Br₂, H₂O, H₃O⁺, sp², sp³, π, σ, °). The reader also normalizes ASCII formulas ("Br2" → "Br₂") via a formatting guard applied to body text **and** headings/figure titles (`renderChemFormula`), so nugget/section/asset **titles** subscript correctly too — but author them cleanly regardless.

## Figures

- Give every reader section at least one renderable figure. `molecule` (needs `smiles`) and `reaction_coordinate` (needs a `spec`) render in the reader; `orbital_overlay`/`newman`/`synthesis` compile as image blocks that render only when a file exists.
- `reaction_coordinate` specs use the `ReactionCoordinateSpec` shape — `title`, `energy_axis`, `steps[]` (`{type, barrier}`), `minima_labels[]` (steps.length + 1), and optional `minima_molecules` (index → SMILES). Do **not** use an ad-hoc `{points}` shape; the reader cannot render it.
- **Reaction coordinate diagrams only for clear, simple reactions** (reviewer rule, 2026-07-23): one clean step, or two steps whose profile shape is the lesson (SN1). Multistep ionic additions (HBr, hydration, Br₂/bromonium, alkyne hydration, proton transfer) get prose + molecule figures, never an energy diagram — every such diagram was rejected in review.
- **Canonical spec shapes are mandatory or the figure renders blank** in the Science Review Queue and reader: `newman_projection` takes an `object` (NewmanProjectionObject) — never `{front_substituents, back_substituents}`; `synthesis_roadmap` is linear `nodes` + `steps` — no `edges`, no branching (alternate branch goes in `scientific_caveats`); `stereochemistry_conversion` needs `spec.molecules: [{label, smiles}]`, not just `labels`.
- Small structures are rendered with explicit hydrogens automatically: the reader/deck default is `hydrogens: "auto"` with a heavy-atom threshold of 6 (now a **user-tunable** display preference — see the proprietary reader preferences module, not in this repo, and the backend `_resolve_show_hydrogens` in `deck_creator.py`), so author SMILES normally. To force it regardless of the viewer's preference, set `rdkit_options: {"show_hydrogens": true}` on a chapter-manifest `molecule` asset (an explicit authored boolean always wins over the tri-state) for tiny molecules (ethane/ethene/ethyne).
- **Never author `annotation_font_scale` to enlarge a stereo label.** R/S, E/Z and cis/trans annotations already render at ~1.0× a default atom label: `render_molecule_png` applies the house default `annotation_font_scale: 0.75` and clamps authored values to `[0.5, 1.0]` (`ANNOTATION_FONT_SCALE_MIN/MAX` in `deck_creator.py`), warning on anything out of band. The pipeline used to author `1.8`, which RDKit honors unbounded — annotations bypass `maxFontSize` — putting the glyph at 2.5× the atom labels and ~23% of the figure height, on top of the structure. Same rule for `base_font_scale` (clamped to `[1.0, 2.0]`): use it only for a genuinely unreadable formal charge, never as a general "make it bigger" knob.
- Run all display text through `ensure_chemistry_display_text` (chemistry-text-normalizer): H₂/Br₂/X₂ subscripts, σ/π; plain "pKa" is the house convention.
- Never emit a `deck-figure:<id>` review task when `<id>` is already a chapter-manifest asset — it double-lists the same figure for review (the queue hides such duplicates).

## Figure provenance (required)

Every asset carrying a hosted `image_url` needs a `generation` block naming the tool that drew it. Validation rejects the asset without one (proprietary generation validator, not in this repo).

```jsonc
"generation": {
 "method": "svg_builder", // ai_image | rdkit | svg_builder | matplotlib |
 // external_render | licensed_clipart | animation_pipeline
 "tool": "proprietary builder entry point (not in this repo)",
 "provider": "chemillusion", // google | openai | bria | chemillusion | external
 "generated_on": "2026-07-30", // optional, ISO-8601
 "ai_regeneration_allowed": false
}
```

- **`tool` must name something that exists.** Point at the committed builder entry point, or at the model slug. If the figure's builder was never committed, say so (`"RDKit MolDraw2DSVG (builder script not committed)"`) — naming a script that does not exist is a worse record than naming the gap, and `report_asset_provenance.py` lists these under "attributed but not reproducible".
- **`ai_regeneration_allowed` is false unless the figure is pure schematic illustration.** It is the gate on whether a generative model may ever redraw the figure, and it is false for anything whose teaching content lives in the geometry of the drawing: structures, mechanisms, monomer sequences, and quantitative plots. A generative render can be confidently wrong in all four ways, and neither alt text nor a formula check catches it.
- **`method: "ai_image"` additionally requires `prompt`** (the full prompt, verbatim), a generative `provider`, and `ai_regeneration_allowed: true`. Record any reference images or SMILES fed alongside the prompt in `input_assets[]`. Without the stored prompt the figure cannot be reproduced or audited.
- After adding or changing figures, regenerate the inventory with the proprietary asset-report script (not in this repo). `--check` fails when the committed report is stale.

## Authoring rules

- Canonical prose must be newly authored and textbook-agnostic.
- Exact full-content equality across terse/standard/expanded is valid for intrinsically non-rescalable text and may auto-approve. Otherwise write genuinely distinct levels.
- Figures, teaching assets, and video briefs never auto-approve.
- Use only asset types in `ChemTeachingAssetType`; do not disguise screenshots as editable assets.
- Keep `publishing.available` false until required review is complete.
- A package is incomplete if it only builds slides. Assets, review tasks, video decisions, concept-map inclusion, and every textbook lens are part of the completion gate.
- Every topic package generates four output classes: (1) deck slides, (2) an OER reader chapter at `/reader/organic/<reader_slug>`, (3) an LMS module JSON, and (4) the Deck Creator Teaching-Package Textbook tab, which renders the same compiled reader chapter (no separate authoring — the reader chapter IS the deck textbook). A package is incomplete if any of these is absent after compilation.
- OER reader chapter blocks must satisfy: molecule/reaction/image/video blocks have `provenance.rights_status = "generated"`; all external link blocks (McMurry, Wikipedia) have `rights_status = "linked_only"`.
- LMS module items use nugget `text.expanded` for body content. The `text.terse` and `text.standard` variants are embedded in the reader chapter JSON and rendered client-side by the personalization slider.

## Required handoff

Report the canonical package path, generated outputs, counts, mappings needing verification, tests run, and review items still pending. Do not commit unless explicitly asked.

- Reader chapter JSON path and section count
- LMS module JSON path and item count
- Whether `available: true` or still draft
- Direct URL to preview the chapter: `http://localhost:3000/reader/organic/<reader_slug>`
