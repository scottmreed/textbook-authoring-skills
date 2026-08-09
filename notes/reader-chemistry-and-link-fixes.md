# Reader chemistry & dead-link fixes

Notes from cover-to-cover agent audits that landed as two data-only fix batches in the
private ChemIllusion monorepo:

| Batch | Merged | Commit |
|-------|--------|--------|
| Tier-1 reader fixes (private monorepo PR #2747) | 2026-07-30 | `[commit ref — not in this repo]` |
| Tier-2 reader fixes (private monorepo PR #2750) | 2026-07-30 | `[commit ref — not in this repo]` |

Both PRs were **data-only** edits to compiled OER reader chapter JSON
(proprietary reader chapter artifacts, not in this repo): prose fields and diagram/link
payloads — **no application code**. They are independent and merged cleanly in
either order.

> **Lesson for textbook authoring:** these fixes lived in **build outputs**. A
> later recompile from `topic.package.json` can wipe them unless the same
> corrections are back-ported into the package (or the compiler gap is fixed).
> See `skills/produce-organic-chapter` and `skills/review-organic-chapter`
> (“compiled reader is a BUILD OUTPUT — never hand-edit it”).

---

## How these findings were obtained

1. **Full cover-to-cover read** of the live organic reader corpus (~25 chapters,
   **957 blocks**, ~**199,500 words**), performed by an automated cover-to-cover pass —
   not by sampling or persona-review alone.
2. Defects were classified into severity bands:
   - **Tier-1** — chemistry that would mis-teach a core idea if left standing
     (wrong energetics, wrong stereo SMILES, wrong pKa band, contradictory
     strain numbers), plus **invalid diagram barrier tokens** and **dead
     external links**.
   - **Tier-2** — subtler chemical misstatements, incomplete scopes, and
     length-variant drift (`terse` / `standard` / `expanded` disagreeing).
3. Each proposed edit was applied to **all affected length variants** so a
   student switching detail level would not see two answers.
4. **Verification before merge** (both PRs):
   - Chapter JSON parse: 50/50
   - SMILES parse regression guard: 460/460
   - Targeted chemistry checks (CIP labels, barrier enums, HTTP 200 on links)
5. Persona-based chapter reviews (`reports/topic-packages/*/chapter-review.*` in
   this repo) are a **separate** QA track (`review-organic-chapter`). They later
   rediscovered the artifact-vs-package drift problem when recompiles erased
   curated reader fixes — which is why the orchestration skills now require a
   pre-compile artifact diff.

---

## Tier-1 batch — chemistry, barriers, and dead links

**Title:** fix(reader): tier-1 chemistry errors, invalid energy-diagram barriers, and all 77 dead links  
**Batch:** tier-1 reader fixes (private ChemIllusion monorepo)

### Tier-1 chemistry errors (summary)

1. **ch7** — all four two-step energy diagrams drew the carbocation/bromonium
   *below* the reactants (`exergonic` first step). Corrected to endergonic first
   step (matches house convention elsewhere + SN1 demo spec).
2. **ch5** — `(R)`- and `(S)`-2-bromobutane shared flat SMILES `CCC(C)Br`; fixed
   to stereo SMILES, RDKit CIP-confirmed.
3. **ch2** — protonated amines given pKa ~10 units too low; amines vs alcohols
   separated.
4. **Epoxide ring strain** — ch18 vs ch18.5 disagreed by ~2×; both set to
   ~114 kJ/mol aligned with cyclopropane (~115).

### Invalid energy-diagram barriers

`reaction_coordinate_service.py` only accepts `small|medium|large`. Other tokens
are **silently coerced to `medium`**, flattening intended profiles.

| Chapter | Block | Was | Now |
|---|---|---|---|
| ch6 | `blk-9lduopna` | endergonic/**high** → exergonic/**low** | endergonic/large → exergonic/small |
| ch7 | `blk-x3lpbuuq`, `blk-yn2l9dl9`, `blk-54zbeqik`, `blk-ur483tha` | exergonic/**large** → exergonic/**small** (and wrong first-step sign) | endergonic/large → exergonic/small |
| ch9 | `blk-i1unmt96` | endergonic/**high** → exergonic/**low** | endergonic/large → exergonic/small |
| ch21 | `blk-n8mt41fm` | endergonic/**low** → exergonic/**low** | endergonic/small → exergonic/small |

All 12 non-empty diagrams ended on valid barrier values.

### Dead external links: 77 → 0

Reader resolved **214/214** after the pass.

- **69 genuine 404s** — section headings auto-minted into Wikipedia titles that
  never existed (heavy in ch2–ch11 / ch18.5). Each remapped to a real article and
  HTTP-verified at 200.
- **8 non-ASCII title issues** (Brønsted, Diels–Alder, Hückel, …) — retitled /
  percent-encoded as needed.

`provenance.source_url` updated with each `content.url`.

### Deliberately deferred in #2747

- Availability / preview gating (separate product work)
- Tier-2 chemistry (~26 items → became #2750)
- Missing tables / figure assets
- Nine visibly broken empty `reaction_coordinate` / empty `image` blocks (need
  assets, not prose edits)

---

## Tier-2 batch — chemistry corrections

**Title:** fix(reader): 33 tier-2 chemistry corrections across 18 chapters  
**Batch:** tier-2 reader fixes (private ChemIllusion monorepo)

Second pass from the same cover-to-cover read. **33 corrections across 18
chapters.** Prose fields only (`markdown` / `description` / `alt_text` and
detail variants). Independent of #2747.

### Chemical corrections table

| Ch | Block | Was | Now |
|---|---|---|---|
| 4 | `blk-t2w4o9go` | cyclobutane lumped with cyclopentane as "moderate net strain" | ~110 kJ/mol (nearly cyclopropane's 115) vs cyclopentane's ~26, numbers given |
| 5 | `blk-y8rh3kw8` | "exchanging **any two** groups produces the mirror image" | scoped to one stereocenter; notes that inverting one of two gives a diastereomer |
| 6 | `blk-qcea7897` | "a catalyst… **is consumed** and regenerated" | "is **not** consumed overall — used up in one step and regenerated in a later one" |
| 8 | `blk-aci0uyvs` | "**Because boron is electron-deficient**, it becomes bonded to the less hindered carbon" | sterics + charge development in the four-centre TS |
| 9 | `blk-yw6csmek` | vinyl cation's "empty orbital sits in an sp framework with **high s character**" | the σ bonds carry the s character; the vacancy is a pure p orbital |
| 11 | `blk-rohm8q5l` | "a strong base with little steric bulk favors **elimination**" (unscoped) | restricted to 2°/3°, with the 1° behaviour stated |
| 12 | `blk-ydmjq1pv` | "Only butan-2-one and butanal remain" | adds **2-methylpropanal**; cyclobutanol and cyclic ethers excluded correctly |
| 13 | `blk-7qlmod7a` | n+1 "with a single neighboring proton **on each side**" | methyl sees one (doublet), CHCl₂ sees three (quartet) |
| 14 | `blk-1uqkzovn` | "the **mere presence** of a 200–400 nm band indicates conjugation" | requires an *intense* band; acetone (279 nm, ε ≈ 15, n→π*) given as the counterexample |
| 15 | `blk-twya61gw` | benzene's 4 DoU "a figure that a **chain** triene would also satisfy" | **cyclic** triene (an acyclic triene has 3) |
| 15 | `blk-bwcsz2v3` | adenine NH₂ "on the carbon **between its two nitrogens**" | that carbon (C2) bears H; NH₂ is at C6 |
| 15 | `blk-wlzjl4vz` | pyrrole "would be **antiaromatic**" | **nonaromatic** — an sp³ N breaks conjugation, which §4 of the same chapter insists on |
| 16 | `blk-mwk48fb7` | acylium "RC≡O⁺, in which the **positive carbon**…" | both resonance forms given; in RC≡O⁺ the formal charge is on **oxygen** |
| 16 | `blk-26yi1320` | "**doubly** bonded to something more electronegative… –C≡N" | **multiply** bonded |
| 18 | `blk-ljljvglo` | "**the exclusive product**", drawn as one enantiomer | racemic; diastereospecific, not enantioselective |
| 18 | `blk-46ym9os5` | single enantiomer from achiral cyclohexene | notes the racemic trans pair; one enantiomer drawn |
| 19 | `blk-odfc65hw` | carbinolamine "with OH and **NR₂**" | NHR from a 1° amine, NR₂ from a 2° amine |
| 20 | `blk-6cy7imuk` | charge "over two oxygens **and the carbon between them**" | shared by the two oxygens through a π system spanning O–C–O |
| 20 | `blk-6cy7imuk` | induction via "the carbonyl group… the **negatively charged oxygen**" | the sp² carbon withdrawing σ density from both oxygens |
| 21 | `blk-tz5r45b6` | "**-ic acid** → **-oyl chloride**" (gives "acetoyl chloride") | -ic → **-yl**; systematic -oic → -oyl, with both examples |
| 21 | `blk-qhxcm53z` | amide hydrolysis "expels the amine as its **ammonium salt**" | expels the **neutral** amine, protonated after |
| 22 | `blk-zi0w0kbt` | ester α-H "the **least acidic** of the common carbonyl families" (pKa 25) | "markedly less acidic than a ketone's" — amides are 30 |
| 23 | `blk-pfybrl19` | enone π system "spread over **three atoms**" | **four** — β-C, α-C, carbonyl C, O |
| 23 | `blk-smr2vme2` | benzaldehyde's ring carbon "**whose hydrogen cannot be removed**" | carries **no hydrogen at all** |
| 24 | `blk-8ho9ll50` | diazonium hydrolysis "the **chief industrial phenol synthesis**" | never was; cumene oxidation named instead |
| 24 | `blk-dwxjp4rp` | glutamate dehydrogenase presented as a **PLP** enzyme | GDH is NAD(P)H-dependent; PLP transaminases run no reduction — split into two claims |
| 24 | `blk-gwkfku4c` | "**Three** reducing systems appear on exams" followed by two | "Two" |

### Self-contradictions resolved (same audit)

Three were length-variant drift (detail levels disagreed):

- **ch21 `blk-tz5r45b6`** — `standard`/`terse` propagated naming error to anhydrides
- **ch23 `blk-pfybrl19`** — `standard` said acid-catalyzed dehydration is ordinary **E1**; main text argues it is not
- **ch23 `blk-uilw2br2`** — Grignard **or hydride** stays at carbonyl vs ch19 NaBH₄ conjugate reduction of enones
- **ch21 `blk-qhxcm53z`** — primary/tertiary amide-reduction series skipped **secondary** (tested elsewhere)
- **ch24 `blk-2qp5o5tn`** — "two rings, twice the discount" refuted by chapter pKaH values

### Judgement calls called out in the PR

- **ch15 pyrrole** — kept the “four electrons” rhetorical hook; only the
  *antiaromatic* label was wrong → *nonaromatic*.
- **ch18 captions** — drawings unchanged (one enantiomer for relative config);
  exclusivity claims qualified; RDKit confirmed (S,S) products from achiral
  substrates → racemate statement correct.

### Deliberately not included in #2750

- ch16 AlCl₃ stoichiometry ambiguity (would add new content)
- Missing tables/figures and ch18.5 delete/merge
- Nine text-only / empty figures (assets, not edits)

### Verification (#2750)

| Check | Result |
|---|---|
| Chapter JSON parses | 50/50 |
| SMILES parse (regression guard) | 460/460 |
| ch18 stereochemistry claims | confirmed via `rdCIPLabeler` — (S,S), chiral, from achiral substrates |
| Every edit landed in all variants | 33/33 asserted |
| Merge with #2747 | clean, no conflicts |

---

## Relation to persona reviews in this repo

| Artifact | Role |
|----------|------|
| `reports/topic-packages/*/chapter-review.md` (+ `.json`) | Multi-persona orchestrated reviews (`instructor`, `struggling-student`, `accessibility`, `visual-preference`) |
| `coherence-pass.md` | Post-persona coherence notes where present |
| `persona-*` / `persona-returns/` / `persona-envelopes/` | Raw persona envelopes for some chapters |
| This file | Corpus-wide chemistry/link audit that shipped as #2747 + #2750 |

Use them together in the textbook-authoring story: personas catch chapter-local
pedagogy and access issues; the cover-to-cover pass caught systematic link minting,
barrier-token silent failure, and cross-chapter chemical drift.
