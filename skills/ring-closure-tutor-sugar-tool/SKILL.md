---
name: ring-closure-tutor-sugar-tool
description: Calls the deterministic Ring Closure Tutor / sugar-forms tool and renders sugar representations (Fischer projection, ring forms, educational diagrams, canvas identify) to ChemIllusion conventions. Use when a chem-assistant chat, deck/reader authoring flow, or the Generator modal builds, converts, previews, or identifies curated monosaccharides (pentoses/hexoses, D/L, alpha/beta anomers, pyranose/furanose).
---

# Ring Closure Tutor — Sugar Tool

The sugar tool is a **deterministic, RDKit-first** service (no AI quota, no DB). A chat
or authoring flow calls the HTTP endpoints below; it must **never** hand-render sugars
or invent SMILES. Curated data lives in proprietary assets (not in this repo).

**PRD:** internal tracker issue, not in this repo (Ring Closure Tutor / Sugar Representation Builder Modal).

**Backend / Frontend:** proprietary functions (not in this repo). For textbook authoring without the product API, use `molecule-svg-drawing` conventions or static figures with alt text — do not hand-draw Fischer/Haworth projections.

## Endpoints (`/api/sugar-forms/*`)

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/catalog` | curated sugars, representations, `coming_soon` |
| POST | `/identify` | graded/fuzzy classify a structure (see below) |
| POST | `/convert` | resolve a curated target form (or hold back) |
| POST | `/validate` | RDKit validation + warnings |
| POST | `/preview` | deterministic 2D SVG (skeletal / ring) |
| POST | `/fischer` | **textbook Fischer projection SVG** (generated, not editable) |
| POST | `/haworth` | **textbook Haworth projection SVG** (generated, not editable) |
| POST | `/diagram` | labeled educational diagram SVG |

**Fischer and Haworth are their own endpoints.** For "Open-chain Fischer" call
`/fischer` (pass `sugar_id` or `smiles`); for the "Haworth projection" call `/haworth`
(pass `form_id`, or `sugar_id` + `ring_size` + `anomer`, or a ring `smiles`). Do **not**
send these to `/preview`, which only produces a skeletal drawing. Both are generated
teaching diagrams, not editable Ketcher structures — say so. `haworth_like` (editable)
stays available for a canvas-compatible ring; `haworth` is the textbook projection.

## Display conventions (MUST follow — these are graded expectations)

1. **Anomers use Greek letters (alpha, beta) rendered as their Greek glyphs** in every
 user-facing label, note, caption, and chat sentence. Never "a/b", never the spelled
 words in output text. (Backend note map: `_DIAGRAM_ROLE_NOTES["anomeric"]` is the
 Greek pair.)
2. **D and L are always capital** (`D`, `L`, `D/L`) — never lowercase `d`/`l`, in
 display names, notes, captions, or prose.
3. **Fischer projections:** vertical spine, most-oxidised carbon on top; the terminal
 groups (`CHO`, `CH2OH`) draw the **carbon on the spine** so the bond connects to the
 **C**, not the middle of the text. Each -OH is placed left/right from RDKit
 stereochemistry (D-glucose = right, left, right, right). It is a generated teaching
 diagram, not an editable Ketcher structure — say so.
4. **Haworth projections (drawing rules — codified):** draw the ring **edge-on** — a
 hexagon for pyranoses, a pentagon for furanoses — with the ring **O at the back**
 and a **horizontal, bold BOTTOM edge as the anchor** line. Substituents (**-H, -OH,
 -CH2OH**) point **strictly straight up or straight down** (vertical bonds only). The
 vertical bond must terminate **on the attaching atom**: the **O of an -OH** (and the
 **C of -CH2OH**) sits **on the bond axis**, with the rest of the group offset beside
 it — never bond to the middle of the label text. In the D-series the CH2OH is up; β
 places the anomeric -OH on that same (up) side, α on the opposite side. The up/down
 face is derived deterministically from the ring stereochemistry via a **pucker-immune
 local frame** (cross of the two ring bonds), anchored to the reference CH2OH and
 **majority-voted across conformers** — never hard-coded per sugar. The Greek anomer
 letter is drawn as real SVG text. This is a generated teaching diagram, not editable.
 The same **heteroatom-centred attachment** rule applies to Fischer termini and any
 RDKit/Ketcher-derived sugar depiction: bonds connect to the actual atom (C or O),
 not the centre of a multi-character label.
5. **Contrast (WCAG 2.2 SC 1.4.11, at least 3:1):** highlight colours are deep and
 saturated (teal-green = anomeric, burnt orange-red = carbonyl, strong blue = D/L
 reference), **never purple**. Do **not** enlarge the R/S stereo annotations or role
 notes — keep RDKit's default annotation scale so labels don't collide with the
 structure. Colour is never the only cue: always keep the text note (`D/L`, the Greek
 anomer pair, `C=O`) and the legend.
6. **Chair is not a real conformation yet.** `/convert` with `representation: "chair"`
 returns `advisory` — surface it verbatim ("shows the ring connectivity, not a true
 chair"). Never present a flat ring as a chair.
7. **Canvas auto-detect is graded — never guess stereochemistry.** `/identify` returns
 `confidence`: `exact` | `constitutional` | `ambiguous` | `low` | `none`, plus
 `suggestions` (curated sugar ids). Offer suggestions as "did you mean ..."; only treat
 `exact` as a firm match. For `constitutional`, tell the user the connectivity matched
 but the drawn D/L and anomer should be double-checked. For unmatched drawings, explain
 what is recognisable (one connected pentose/hexose, open-chain or a single
 pyranose/furanose ring, explicit stereochemistry).

## Guardrails

- Deterministic only — no new deps, no DB migration, no Ketcher fork.
- Adding/moving items out of `coming_soon` (true chair renderer, textbook Haworth SVG,
 broader arbitrary-structure perception) is a real feature — implement + test, don't
 fake the output.
- When adding examples to chat, prefer curated `sugar_id`s from `/catalog`.
- Haworth 3D-embedding is slow; SVGs for all curated forms are **pre-rendered** in
 the proprietary sugar SVG cache (not in this repo; built via a proprietary script).
 Regenerate the cache whenever the catalog's ring SMILES change.
