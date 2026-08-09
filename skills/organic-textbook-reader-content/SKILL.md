---
name: organic-textbook-reader-content
description: Authoring workflow for the installable organic PWA reader at /reader/organic — chapter catalog, bridge/study-guide prose, McMurry/OpenStax links, reader manifests, and LTI redirects. Use when fleshing out organicTextbookCatalog.ts, seeding textbook bridges, or extending /reader/organic chapter pages. Former skill folder textbook-chapter-development.
---

# Organic Textbook Reader Content

## Overview

Each pilot chapter has two content layers:

1. **Static catalog** — the proprietary frontend catalog module (not in this repo): article lists, bridge text, and coreNote. Ships with the frontend; no DB needed.
2. **DB-backed bridges** — the proprietary bridge seeder (not in this repo): CC BY-SA authored prose that the reader API serves and that goes into exports. Requires `alembic upgrade head` and `--apply` run against the live DB.

For day-to-day chapter fleshing-out, the catalog is the right place to start. Backend bridge seeding is for content that needs to flow into generated exports or be served dynamically.

---

## McMurry Chapter Map (OpenStax edition)

| ChemIllusion Ch | McMurry Ch | Topic |
|-----------------|------------|-------|
| 1 | 1 | Structure and Bonding |
| 2 | 2 | Polar Covalent Bonds; Acids and Bases |
| 3 | 3 | Alkanes and Their Stereochemistry |
| 4 | 4 | Cycloalkanes and Their Stereochemistry |
| 5 | 5 | Stereochemistry at Tetrahedral Centers |
| 6 | 6 | An Overview of Organic Reactions |
| 7 | 7 | Alkenes: Structure and Reactivity |
| 8 | 8 | Alkenes: Reactions and Synthesis |
| 9 | 9 | Alkynes: An Introduction to Organic Synthesis |
| 10 | 10 | Organohalides |
| 11 | 11 | SN1/SN2/E1/E2 Reactions |
| 12 | 12 | Mass Spec and IR Spectroscopy |
| 13 | 13 | NMR Spectroscopy |
| 14 | 14 | Conjugated Compounds and UV |
| 15 | 15 | Benzene and Aromaticity |
| 16 | 16 | Electrophilic Aromatic Substitution |
| 17 | 17 | Alcohols and Phenols |
| 18 | 18 | Ethers and Epoxides |
| 19 | 19 | Aldehydes and Ketones |
| 20 | 20 | Carboxylic Acids and Nitriles |
| 21 | 21 | Carboxylic Acid Derivatives |
| 22 | 22 | Carbonyl Alpha-Substitution |
| 23 | 23 | Carbonyl Condensation |
| 24 | 24 | Amines and Heterocycles |
| 25 | 25 | Carbohydrates |
| 26 | 26 | Amino Acids, Peptides, Proteins |

## URL conventions

**Always use** `https://openstax.org/details/books/organic-chemistry` as the McMurry link target.
Chapter-specific page URLs (`/books/organic-chemistry/pages/N-introduction`) return 404.
Include the section reference in the link text instead:

```
[McMurry §3.7–3.8](https://openstax.org/details/books/organic-chemistry)
[McMurry Table 2.3](https://openstax.org/details/books/organic-chemistry)
```

NC State Pressbooks is a stable secondary:
`https://ncstate.pressbooks.pub/ncstateorgchem/`

---

## Files to update per chapter

### 1. Static catalog module (not in this repo)

The `chapter()` helper signature:

```typescript
chapter(
 number, // integer
 slug, // kebab-case, matches the route
 title, // Full chapter title as in McMurry
 bridge, // Study guide prose — shown ABOVE the article list.
 // Supports [text](url) and **bold**. Two \n\n = paragraph break.
 // Frame as: "why these articles, what to do with them, what to do when stuck."
 core, // string[] of Wikipedia article titles (exact title, no URL).
 // Format: "Article title" or "Article title - Section anchor"
 review, // string[] — optional prerequisite refreshers, shown collapsed
 deeperLook, // string[] — optional enrichment, shown collapsed
 coreNote, // Optional. Appears BELOW the article list.
 // Use for: gap analysis ("these articles don't cover X"), McMurry supplements,
 // specific problem sets to try after reading.
)
```

`mcmurrySections` is set separately, in the `MCMURRY_SECTIONS` map lower in the
same file (keyed by reader slug), so the positional `chapter(...)` calls stay
untouched. It holds **1–6 links to specific OpenStax sections**, each with a
one-sentence context note, rendered in the Additional Reading list beside the
Wikipedia targets:

```ts
"cycloalkanes-and-stereochemistry": [
 os(
 "4-2-cis-trans-isomerism-in-cycloalkanes",
 "§4.2 — Cis–trans isomerism in cycloalkanes",
 "One sentence naming what this section adds that the chapter text does not.",
 ),
],
```

A wrong slug returns HTTP 404, so every link is verifiable — the bulk check and
the selection/wording rules live in
[produce-organic-chapter](../produce-organic-chapter/SKILL.md) step 7. The proprietary
catalog module (not in this repo) enforces the shape.

#### Writing the bridge (study guide)

- Lead with WHY this chapter matters in the arc of organic chemistry.
- Name 2–3 articles the student should read first and in what order.
- Include at least one specific "if you are unclear about X, do Y" pointer.
- End with a conformational/practice prompt for mechanism-heavy chapters.
- Paragraph 1: context and sequencing. Paragraph 2: the hard part + what to do about it.
- Length: 3–6 sentences total. Do not repeat the chapter title.

#### Writing the coreNote

- Gap analysis: what the Wikipedia articles cover well vs. where they're thin.
- Specific McMurry supplement: "for X, see [McMurry §N.N](url)".
- A single concrete fact or quantity worth remembering (e.g., gauche/anti energy difference).
- 2–4 sentences. No fluff.

#### Article title format

For whole-article links: `"Alkane"`, `"Lewis structure"`, `"Conformational isomerism"`
For section anchors: `"Periodic table - Periodic trends"`, `"Butane - Conformation"`
The `toWikipediaUrl()` function in the catalog handles URL encoding.

### 2. DB bridge seeder (optional — proprietary function, not in this repo)

Add entries to the `BRIDGES` list. Each entry:

```python
{
 "chapter_number": 3,
 "chapter_slug": "alkanes-and-stereochemistry",
 "layer": None, # None = chapter intro; "core" | "review" | "deeper_look" = section intro
 "body_markdown": "...", # CC BY-SA authored prose; [text](url) inline links; \n\n paragraphs
},
```

After adding: run the proprietary bridge seeder with `--apply` (not in this repo;
requires live DB + permission).

The static catalog bridge takes precedence in the reader when the DB row is absent, so the static text is the right place to develop the content before seeding.

---

## Step-by-step workflow for a new chapter

1. **Identify the McMurry chapter number** from the map above.
2. **Open the McMurry chapter** at `https://openstax.org/details/books/organic-chemistry` and note the key sections and problems.
3. **Select core Wikipedia articles**: 5–10 articles that together cover the chapter's core concepts. Prefer articles with solid chemistry content; avoid disambiguation pages.
4. **Select review articles**: 2–6 prerequisite topics from prior courses. These appear collapsed — err on the side of fewer.
5. **Select deeper-look articles**: 2–6 application/context topics. Industrial, biological, or historical connections. Also collapsed.
6. **Write the bridge** (study guide): context + sequencing + "if stuck" pointer.
7. **Write the coreNote**: gap analysis + specific McMurry supplement + one memorable quantity.
8. **Update `organicTextbookCatalog.ts`**: replace the stub `chapter(N, slug, title)` with the full `chapter(N, slug, title, bridge, core, review, deeperLook, coreNote)` call.
9. **Build and verify**: `cd frontend && npm run build` — no TypeScript errors.
10. **Preview at**: `http://localhost:3000/lti/textbook/organic/CHAPTER-SLUG?lti_session=13&embed=1`
11. **DB bridge (optional)**: add to `seed_textbook_bridges.py` for content that needs to flow into exports.

---

## Quality checklist per chapter

- [ ] `bridge` opens with WHY, not "In this chapter..."
- [ ] At least one McMurry section reference in the bridge, linked to the specific section page
- [ ] `coreNote` identifies at least one gap in the Wikipedia coverage
- [ ] `review` articles are genuinely prerequisite (not just adjacent topics)
- [ ] `deeperLook` articles connect to biology, industry, or history (not more chemistry fundamentals)
- [ ] `mcmurrySections` has 1–6 specific section links with a context sentence each
- [ ] No broken URLs — McMurry targets are specific section pages
 (`.../pages/4-2-cis-trans-isomerism-in-cycloalkanes`), never a chapter landing
 page or the book details page; verify each returns 200
- [ ] Wikipedia article titles match exactly (check by visiting `https://en.wikipedia.org/wiki/TITLE`)
- [ ] Build passes in the proprietary frontend workspace (not in this repo)

---

## Chapters with full content (as of 2026-06-02)

| Ch | Status |
|----|--------|
| 1 | ✅ Full — core, review, deeperLook, bridge, coreNote |
| 2 | ✅ Full — core, review, deeperLook, bridge, coreNote |
| 3 | ✅ Full — core, review, deeperLook, bridge, coreNote |
| 4 | 🔶 Bridge only — no article lists yet |
| 5 | 🔶 Bridge only — no article lists yet |
| 6–29 | ⬜ Stub — title only |

**Next priority**: Chapters 4 (Cycloalkanes) and 5 (Stereochemistry at Tetrahedral Centers).
Both need core/review/deeperLook article lists and a gap-analysis coreNote.

---

## Relationship to the snapshot pipeline

The article lists in the catalog drive the DOCX crosswalk import. When you add articles to `core`, `review`, or `deeperLook` they should also be reflected in the crosswalk DOCX (proprietary crosswalk
document, not in this repo) when that document is next updated, so that `wiki_import_docx.py --apply` seeds the corresponding `WikiCrosswalkTarget` and `WikiArticleSource` rows.

For the fetch pipeline (Phase 1), the sources table is the authoritative driver — the catalog is the student-facing shell. Keep them in sync when adding articles.

---

## Topic-Package Chapters (new pipeline — 2026-06-24)

Topic-package chapters are compiled by the proprietary topic-package compiler
(not in this repo) and live at:

- **Reader JSON**: proprietary reader chapter artifact (not in this repo)
- **LMS module JSON**: proprietary LMS module artifact (not in this repo)
- **Catalog**: proprietary reader catalog index (not in this repo; updated automatically)

### Route
`/reader/organic/<reader_slug>` — same URL pattern as the Wikipedia chapters. The page detects topic-package chapters by looking up the slug in the catalog.

### Second consumer: Deck Creator Textbook tab (2026-07-24)
The compiled reader JSON is **canonical for two surfaces**: the reader route above AND the
Deck Creator Teaching-Package **Textbook tab** (`CanonicalTextbookView` →
`TopicPackageChapterRenderer`, resolved from the deck chapter id via the catalog +
`organicChapterCrosswalk`). Both share the reader personalization prefs
(Concise/Standard/Detailed via `_detail_texts`). Book numbering stays a link-time lens
(`mcmurry_link` blocks, crosswalk ordering) — never embed it in canonical prose.

### Reader UI palette (`/reader/organic`)

**No purple** anywhere on the organic reader surface — badges, buttons, links, or generated figure chrome.

Block badges in `ReaderBlockRenderer` / `ExternalReadingLinkCard` (do not override in JSON):

| Block / surface | Chakra badge | Notes |
| --------------- | ------------ | ----- |
| `reaction_coordinate` | `blue` `subtle` | Matches `ChapterAssetGallery` teaching-asset labels |
| `external_link` / `mcmurry_link` | `gray` `subtle` | Outbound link card only |
| `video` | `pink` | External vs on-site copy in label text |
| `tutorial` | `teal` | Launch button also `teal` |
| `chat_tool` | `teal` | Chapter coach scaffolds |
| Asset gallery type chip | `blue` `subtle` | `ChapterAssetGallery` |

Agents authoring topic-package JSON or teaching assets should **not** embed purple styling; reader chrome is owned by these components.

### Personalization
Topic-package chapters show a `ReaderPersonalizationPanel` with:
- Detail level slider: Concise / Standard / Detailed (maps to nugget `text.terse / standard / expanded`)
- Toggles (all default on): McMurry links, Wikipedia links, Structures & diagrams, Videos

Preferences persist in `localStorage` key `chemillusion.readerPrefs`.

### Chapter homework preview panel

Every topic-package chapter ends with a **"Chapter homework preview"** panel
(`ChapterHomeworkPanel` → `PublicQuestionSetPanel`, mounted in
`TopicPackageChapterRenderer` after the last section), visible only to admins
and approved teacher-preview users. Facts that matter when authoring:

- **Content comes from the seeded question bank** (proprietary API, not in this repo),
 *not* from the static homework-tab JSON (proprietary assets, not in this repo).
 Compiling alone changes nothing on
 this surface — `seed_question_sets.py` must run.
- The panel shows **all published items in `display_order`**; staged `-v2`
 variants (drafts) never appear. There is no per-chapter curation field.
- Placement is **end-of-chapter only** — `ReaderBlockType` has no question
 block, so "distributed" coverage means ordering questions to follow the
 chapter's concept sequence (see produce-organic-chapter step 5f: 6–10
 questions, ≥5 types, every major concept).

### Canonical marketing version
The canonical "show as demo" version is the compiled chapter at `standard` detail, all toggles on. To make a chapter publicly discoverable, set `publishing.available = true` in the topic package and recompile.

### Asset curation note
The compiler includes assets per nugget's `asset_ids` list. If an asset is not suitable for the textbook (e.g. a detailed intermediate structure not helpful without context), remove it from the nugget's `asset_ids` before compiling — do NOT remove it from `assets[]`, as that breaks the deck and review queue.

### Pre-recorded pronunciation audio (2026-07-25)
Molecule-name pronunciation on `/reader/organic/*` is served **static-first**: `useInlineChemLingo` checks the proprietary pronunciation manifest (not in this repo) before calling `/api/chemlingo/pronounce`, so pre-recorded molecules play instantly with no TTS spend or quota. After compiling a chapter with molecule blocks (or retitling one), pre-record it:

```bash
# proprietary toolchain (not in this repo)
# proprietary function (not in this repo) <reader-slug> # incremental
# proprietary function (not in this repo) --all --force # re-record everything
```

Records every eligible molecule × name mode (iupac/common/as_shown) × voice `echo` through the live `ChemlingoService` pipeline (PubChem name resolution + pronunciation guide). MP3s + manifest are **committed to git** and bundle with the frontend deploy (same policy as other proprietary reader assets, not in this repo). Manifest keys must match `readerChemlingoStaticKey` in the proprietary catalog module (not in this repo); unrecorded molecules gracefully fall back to the live API. Molecule titles follow **"IUPAC (common)"** format — e.g. `Prop-1-ene (propene)` — so the printed name matches the default-iupac audio.

### Relationship to Wikipedia catalog
The 31-chapter Wikipedia catalog (`organicTextbookCatalog.ts`) and the topic-package chapters are separate systems that coexist. Do not add topic-package chapters to the static TypeScript catalog. When the same subject appears in both (e.g. alkenes is chapter 7 in the Wikipedia catalog AND could be a topic package), they serve different purposes: the Wikipedia chapters link to broad background reading; the topic-package chapters provide ChemIllusion-native assets and structured exercises.

## PWA Reader (added 2026-06-02)

The chapter catalog now renders through the **installable PWA reader** at `/reader/*`, not just the LMS-embedded LTI route.

### Routes
- `/reader/organic` — public chapter list (`ReaderHomePage`)
- `/reader/organic/:chapterSlug` — chapter reader (`ReaderChapterPage`), accepts `?lti_session=X` for LMS launches
- `/reader/:readerId` — personalized reader from a saved manifest (`PersonalizedReaderPage`)
- `/lti/textbook/organic` and `/lti/textbook/organic/:chapterSlug` — 301-redirect into `/reader/*` (query string preserved)

The reader is installable (vite-plugin-pwa). The service worker caches the first-party shell only; OpenStax/Wikipedia are `NetworkOnly` and never cached.

### OpenStax URL format (CONFIRMED WORKING — use these)
- Chapter intro: `https://openstax.org/books/organic-chemistry/pages/{N}-why-this-chapter`
- Specific section: `https://openstax.org/books/organic-chemistry/pages/{N}-{M}-{section-slug}`
 - e.g. `https://openstax.org/books/organic-chemistry/pages/2-1-polar-covalent-bonds-and-electronegativity`
- **Never use** `https://openstax.org/details/books/organic-chemistry` (landing page, no content)
- **Never use** `.../pages/{N}-introduction` (404s)

Put the section number in the link *text* (e.g. `[McMurry §3.7–3.8](url)`), and the page URL in the link target.

### Personalized readers + external content
A teacher/student saves a `reader_manifest` (DB-backed) with ordered sections. Section types:
- `chemillusion_content` — `content_id` = a chapter slug; rendered via `OrganicChapterLayout`
- `external_source` — `source_url` + `source_license` + `attribution_metadata` (`article_title`, `history_url`); rendered via `ExternalContentSection`, fetched client-side after consent, with attribution card fallback when CORS blocks
- `user_note` — free-text `user_notes`
- `activity` — `activity_id` (Ketcher activity wiring is deferred)

Manifests get a share URL + QR (`ReaderShareModal`) and visibility (private/unlisted/class_link/public). Create/load via the reader-manifest API (not in this repo).

### Chapter license registry (guardrail — read before adding a new source)
The proprietary reader license registry (not in this repo) is the single source of truth for the license
statement students see. The chapter-page footer (`ReaderChapterLicenseFooter`, which replaces
the site-wide "All rights reserved" line on `/reader/organic/:slug`), the chapter-list banner
(`TextbookLicenseBanner`), and `/reader/organic/attributions` (`ReaderAttributionsPage`) all
derive their text from `READER_CONTENT_SOURCES` — never hand-write a license line.

When a chapter starts showing material from a new source, add it to that array:
- `usage: "link-only"` — linked, never reproduced; its terms do NOT flow into our license.
 This is why OpenStax/McMurry (CC BY-NC-SA 4.0) does not force an NC clause today.
- `usage: "embedded"` — rendered inside our pages; its terms DO flow in. An embedded NC source
 auto-escalates the displayed license to CC BY-NC-SA 4.0 everywhere; an embedded ND /
 all-rights-reserved source throws (it must stay link-only).

The proprietary license-registry tests (not in this repo) lock this behavior in; the current
registry must derive to CC BY-SA 4.0.

### External content attribution rules (CC compliance)
- OpenStax sections: CC BY-NC-SA 4.0, noncommercial + ShareAlike + "not endorsed by OpenStax" notices, "Read on OpenStax →" link always present.
- Wikipedia sections: CC BY-SA 4.0, contributor history link, ShareAlike notice.
- A one-time consent banner (localStorage `chemillusion.externalContentConsent`) gates all external fetches.
- Third-party HTML is sanitized with **DOMPurify** before render (`externalContentService.ts`); never stored server-side.

### Cron health check
A cron-gated internal job (not in this repo) HEAD-checks `external_source` URLs not verified in 7+ days and writes `url_health_status` back to `reader_sections`.

### Updating chapter status
When you flesh out chapters 4+, they automatically appear in the reader chapter list (`ORGANIC_TEXTBOOK_CHAPTERS`). No reader-side change needed — just update the catalog entry per the checklist above.
