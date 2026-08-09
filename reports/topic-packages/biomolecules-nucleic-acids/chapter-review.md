# Chapter review — Biomolecules: Nucleic Acids (`biomolecules-nucleic-acids`)

_Reviewed 2026-07-30 · chapter version 1 · personas: Instructor, Struggling Student,
Accessibility, Visual Preference_

**Publication readiness: blocked**

Chemically this is the strongest chapter reviewed to date. The instructor persona
independently re-parsed all 20 SMILES with RDKit and confirmed every InChIKey, every
beta-anomeric assignment, the dinucleotide's 3'-to-5' connectivity and free-end identity,
and both hotspot answer keys. All 46 answer keys pass referential integrity, no
`accessible_description` leaks an answer, and no hint contains its own answer. One chemical
blocker exists and it is chapter-authored and bounded: two strand-directionality questions
name DNA residues with ribonucleoside names ("the adenosine residue" in a strand containing
thymine), and one distractor describes a 2'-oxygen that a DNA residue does not have — which
contradicts the chapter's own practice check. The verdict is nonetheless **blocked** rather
than major revision, because two required-access blockers are unresolved and are
platform-level: the hotspot items expose atom targets whose only accessible name is an
element-plus-index string with no disclosed mapping to the chemical position the prompt
names, and the structure_scaffold items offer no answer channel except a pointer-driven
drawing canvas. Both recur from chapters 1, 11, and 15 through 19. The dominant
non-blocking theme is unanimous across all four personas: the chapter teaches two mechanisms
and a hydrogen-bonded pair entirely in prose, and no figure anywhere shows two bases facing
each other, either mechanism's electron flow, or the in-line geometry at phosphorus — while
the one genuinely sequential figure that was authored, the phosphoramidite roadmap, reaches
the reader as an empty image container.

### Top blockers

- **[BLOCKER] DNA residues named as ribonucleosides in both strand-directionality questions**
 — the keyed-correct option misnames a DNA residue with a ribonucleoside term, and
 a distractor places a 2'-oxygen on a DNA residue that cannot have one
 (Instructor, `ch28-strand-directionality`, `ch28-strand-directionality-v2`). **Corrected below.**
- **[BLOCKER] Hotspot atom targets carry no chemical identity** — targets announce as
 "P atom 16", with nothing mapping the prompt's "alpha phosphorus" onto a target
 (Accessibility, `ch28-alpha-phosphorus-hotspot`). Platform ticket.
- **[BLOCKER] structure_scaffold has no non-pointer, non-visual answer channel** — the only
 answer surface is an embedded Ketcher canvas (Accessibility, `ch28-draw-thymine`).
 Platform ticket.

### Top 5 recommended changes

1. **Name every DNA residue as the 2'-deoxy compound** — assessment must stop contradicting
 the chapter's own ribose/deoxyribose rule → **prose-edit** (assessment, blocker)
2. **Show two bases hydrogen bonded as a pair** — the chapter's headline derivable skill is
 currently performable only in the head → **new-figure** (figure, high)
3. **Draw both mechanisms** — two objectives begin "Draw the mechanism…" and the chapter
 models neither → **static-image-sequence** (figure, high)
4. **Make the phosphoramidite roadmap render** — the authored five-node spec reaches nobody
 → **new-figure** (figure, high)
5. **Stop captions asking for positions the render does not label** — RDKit indices are
 traversal order, not locants, so labelling would mislead → **prose-edit** (figure, high)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---|---|---|
| Organic Chemistry Instructor | 7.8/10 | 1 | Chemistry verified correct throughout; one naming blocker in the assessment |
| Struggling Student | 6.4/10 | 1 | "I would finish this chapter feeling like I had read something very clear and still be unable to draw a base pair" |
| Accessibility | 6.4/10 | 2 | Authored metadata is the best in the corpus; two required activities are unanswerable |
| Learner with Visual Preference | 5.4/10 | 2 (1 rejected) | Figure-dense by count, figure-poor where it matters |

### Affected sections & assets

Concepts `phosphodiester-backbone`, `base-pairing-and-hydrogen-bonding`,
`rna-versus-dna-hydrolytic-stability`, `chain-extension-at-phosphorus`,
`n-glycosidic-bond`, `reading-and-writing-dna`, `nucleoside-analogue-drugs`,
`dna-double-helix-and-base-stacking`; assets `roadmap-phosphoramidite-cycle`, `mol-atp`,
`mol-adenine`, `mol-uridine`, `mol-damp`, `mol-dinucleotide-dapdt`,
`mol-beta-d-ribofuranose`, `clip-dna-double-helix`, `pdb-b-dna-dodecamer`; questions
`ch28-strand-directionality(-v2)`, `ch28-alpha-phosphorus-hotspot(-v2)`,
`ch28-draw-thymine(-v2)`, `ch28-pairing-donors-acceptors`, `ch28-mismatch-failure-mode`,
`ch28-phosphoramidite-step-order`, `ch28-capping-purpose`, `ch28-pyrophosphate-driving-force`.

---

## Full evidence

The four independent persona envelopes are stored verbatim in
[`chapter-review.json`](chapter-review.json) under `personas[]`, each with its own summary,
score, strengths, findings and open questions. They were produced without sight of one
another's rubrics or findings. The orchestrator's own pre-dispatch integrity finding is
recorded separately under `orchestrator_findings[]`.

**Finding counts:** Instructor 15, Struggling Student 13, Accessibility 10, Visual
Preference 14, orchestrator 1 — 53 findings in total, consolidated into 21 ranked
recommendations.

### Orchestrator decisions

The full set of 21 recommendations, each with its need, chosen intervention, rationale,
target surface and `source_findings`, is in `chapter-review.json` under
`ranked_recommendations[]`. The interventions chosen were: **prose-edit** for 9
recommendations, **new-figure** for 3, **added-practice** for 2, **static-image-sequence**,
**keyboard-alternative**, **alternate-activity**, **text-equivalent**,
**structured-chemical-description** and **instructor-note** for 1 each.

Two decisions are worth stating explicitly because the obvious intervention was rejected:

- **Atom numbering on figures (rec-007).** The natural fix for "the caption says locate N9
 and the drawing has no labels" is to enable atom indices. That would make things worse:
 RDKit indices are 0-based traversal order, so N9 would display as "8" and the alpha
 phosphorus as "15". Every asset's `long_description` already maps the named positions
 correctly, and the compiler now emits `long_description` into the reader, so rewriting the
 six offending captions is both cheaper and more correct than any rendering change.
- **Attaching structures to the two "read off the structures" items (rec-008).** Both items'
 options are prose statements about donor/acceptor patterns, not structures to compare, so
 attaching structures would not change what the student evaluates. The stems were reworded
 instead; the underlying skill gap is addressed by rec-004.

### Merged duplicates

| Topic | Findings merged | Kept severity |
|---|---|---|
| No paired-base figure | `vis-003`, `stu-001`, `instr-002` | high |
| Neither mechanism drawn | `vis-006`, `stu-002`, `instr-003` | high |
| Roadmap does not render | `vis-002`, `stu-004`, `instr-004`, `access-008` | high (see disagreement 2) |
| Captions demand unlabelled positions | `vis-004`, `stu-003` | high |
| Stems promise absent structures | `vis-007`, `instr-005` | medium |
| Beta configuration has no checkable depiction | `stu-009`, `instr-006` | medium |
| Ribo ATP in a DNA-framed section | `vis-014`, `stu-012` | low |
| Metadata inconsistency | `instr-007`, `instr-008` | medium |
| Assessment coverage gaps | `stu-007`, `instr-011` | medium |

Each merge keeps the strongest severity offered by any persona and preserves every distinct
learner impact; nothing was dropped in consolidation.

### Retained disagreements

**1. Do the four deferred video blocks present dead media affordances?**

- *Learner with Visual Preference* (`vis-001`, **blocker**): "A reader sees four apparently-playable
 media affordances… clicks them, and nothing happens", citing that the video case builds a
 link to `c.url` with no empty-url guard and that `applyPrefs` filters nothing on url.
- *Accessibility Persona* (`access-010`, **low**): "None today — I confirmed no surface renders
 them", citing `[internal source reference — not in this repo]vis-001` is rejected as a blocker.** I verified
independently that all four compiled blocks carry `is_hidden: true`, that the guard at
`[internal source reference — not in this repo]TopicPackageChapterRenderer` delegates to that same renderer — so both
surfaces suppress them. The visual persona inspected the video case and the compiled JSON but
missed the guard. The residual risk it identifies is real and is retained at low severity:
suppression depends on a single flag, and removing it would expose four links to nowhere. The
minority position is preserved verbatim in `chapter-review.json`.

**2. How severe is the non-rendering phosphoramidite roadmap?**

- *Visual Preference* (`vis-002`, **blocker**): the authored spec "never reaches a student".
- *Struggling Student* (`stu-004`, **high**): "I hit a caption with nothing above it, which reads
 as the page being broken."
- *Accessibility* (`access-008`, **low**): "everyone receives the 60-word alt string", and the
 prose states all four reagents.

**Resolution: high.** Accessibility is right that nobody is blocked — `ReaderProviderImage`
falls back to rendering `alt_text`, and that alt text names all four operations in the correct
order. But the other two are right that an authored figure reaching nobody, in the densest
section, beside an orphan caption, is a real defect. High preserves both readings.

**3. Which text tier is the default — and was the briefing wrong?**

- *Struggling Student*: filed `stu-011` on the premise that lowering the tier removes assessed
 material, while noting in its open questions that `useReaderPersonalization` defaults to
 `expanded`, not `standard` as the briefing stated.
- *Orchestrator*: **the briefing I gave all four personas was wrong.**

**Resolution: the student persona is right and I was wrong.**
`[internal source reference — not in this repo]detailLevel: "expanded"`. This lowers
`stu-011` from a live gap to a risk borne only by students who deliberately shorten the text —
which is precisely the coping move a struggling reader makes, so the finding stands at medium
rather than being dismissed. It also means the four tier-deepening edits made during the
production coherence pass were prudence rather than repair. Recorded because it is a
correction to my own instrumentation, not to the chapter.

### Places where a description is sufficient (no new asset)

- The 20 molecule assets' `alt_text` and `long_description` need **no enrichment**. They name
 ring sizes, numbered positions, stereocentre counts and donor/acceptor patterns, and are
 honest about what the drawing omits. Only the `learning_goal` captions needed repair.
- The two clipart figures' descriptions are **sufficient**; both explicitly disclose what the
 stylised drawing does not show, which is the correct treatment for orienting art.
- `pdb-b-dna-dodecamer`'s description is **sufficient for the figure as supplied**. The gap in
 that section is the absent geometry figure (`vis-005`), not the description.
- All 46 `accessible_description` strings are **well-formed, non-leaking and task-accurate**.
 They need a delivery path (rec-019), not rewriting.
- The four deferred video briefs' production notes are **sufficient** — they pre-commit to
 captions, transcripts and a no-colour-alone rule.
- **No reaction-coordinate diagram is needed.** The visual persona called the omission
 "correct restraint, not a gap", and the chapter makes no energy-profile argument.

### Regression targets for next run

`instr-001` (must be resolved), `access-001`, `access-002` (platform tickets — expect
unchanged), `vis-002`/`stu-004`/`instr-004` (roadmap), `vis-003`/`stu-001`/`instr-002`
(paired-base figure), `vis-006`/`stu-002`/`instr-003` (mechanism figures), `access-004`
(expect resolved by the `long_description` compiler change), `access-006`, `orchestrator-001`,
`instr-009`, `instr-012`, `instr-013`, `instr-014`, `instr-015`, `stu-008`, `stu-010`,
`stu-011`, `instr-007`, `instr-008`, `instr-010`.

---

## Post-correction record

**Estimated state: blocked (not a second persona verdict).**

The two required-access blockers (`access-001`, `access-002`) are platform tickets that no
chapter edit can clear, so the baseline verdict stands. Every chapter-authored verified error
was corrected.

### Changes applied

- Renamed every DNA residue in both strand-directionality questions to its 2'-deoxy compound,
 and re-anchored the impossible 2'-oxygen distractor onto a possible structure — resolves
 `instr-001` (**the chemical blocker**).
- Underscored seven `wikipedia_title` values so the generated links resolve — resolves
 `orchestrator-001`.
- Converted three markdown headings and four ordered-list markers in
 `nugget-reading-and-writing-dna` to bold lead-ins that `RichText` actually renders —
 resolves `access-006`.
- Rewrote six `learning_goal` captions so they no longer instruct the reader to find a
 position the render does not label — resolves `vis-004` / `stu-003`.
- Reworded the two stems that promised a structure-reading task and showed no structure —
 resolves `vis-007` / `instr-005` (the stem defect; the skill gap remains under rec-004).
- Defined melting temperature at first substantive use, named pyrophosphorolysis in the
 standard tier, and named dichloroacetic acid where detritylation is taught — resolves
 `stu-008`, `stu-011` (partially), `stu-010` (partially).
- Removed N-methylimidazole from a rank_order card, since it appears nowhere in the chapter —
 resolves the rest of `stu-010`.
- Stated the thymidine naming exception in the prose where the naming rule is given —
 resolves `instr-009`.
- Corrected the beta-attack feedback to say a **diphosphate** is delivered to the chain end —
 resolves `instr-012`.
- Softened the depurination-over-depyrimidination ratio from "two orders of magnitude" to the
 qualitative claim the questions actually rely on — resolves `instr-013`.
- Replaced `S_N2` with `SN2` so one rendering is used throughout — resolves `instr-014`.
- Widened `ch28-capping-purpose` to accept the answer the prompt literally asks for —
 resolves `instr-015`.
- Corrected `why_optional` on `nucleoside-analogue-drugs` to declare the two optional concepts
 a single removable unit, and added the two missing prerequisite edges — resolves
 `instr-007`, `instr-008`.
- Corrected the textbook-matching note to name PCR and translation as out of scope instead of
 claiming a one-to-one mapping — resolves `instr-010`.
- Added a sentence reconciling the ribo ATP figure with the DNA framing of its section —
 resolves `vis-014` / `stu-012`.
- Recompiled, which also picked up the compiler's new `long_description` emission — resolves
 `access-004`.
- **Drew the three base-pair figures** (A·T, G·C, and the failed A·C) with RDKit, each in pairing
 orientation with every hydrogen bond dashed and every donor/acceptor role written in words —
 resolves `vis-003` / `stu-001` / `instr-002`.
- **Drew both mechanisms** as arrow-pushing schemes with curved arrows anchored to real atoms —
 resolves `vis-006` / `stu-002` / `instr-003`.
- **Rendered the authored roadmap spec** and set its `image_url`, so the phosphoramidite cycle
 draws instead of compiling to an empty container. Every image block now resolves, 9 of 9 —
 resolves `vis-002` / `stu-004` / `instr-004` / `access-008`.
- Added a `diagram` asset type for generated static figures: requires an `image_url`, maps to an
 image block, and carries generated provenance rather than the third-party credit `clipart` needs.

### Verification

All results below are actual command output, not expectations.

- Automated test suite — passed — **75 passed**
- pytest over the backend question suites (proprietary toolchain, not in this repo): question_bank,
 public_question_demos, deep_linking_question_sets, accessibility_answer_leaks,
 question_wrong_answer_explanations, numeric_grading) — **177 passed**
- `npx vitest run [internal source reference — not in this repo] [internal source reference — not in this repo][internal source reference — not in this repo] --write-runtime` — **46 questions validated against the live
 registry, 0 errors**; 23 surfaced, 23 staged variants, 12 types
- HEAD check of all 12 compiled external URLs — **12/12 returned 200** (was 5/12 before
 correction)
- grep of the compiled reader for literal `###` — **0 occurrences** (was 3)
- grep of the compiled reader for `S_N2` — **0** (was 2); `SN2` — 2
- grep of the compiled question set for "the adenosine residue" / "the cytidine residue" —
 **0 occurrences each** (was 3 combined)
- grep of the compiled reader for `long_description` — **38 fields present** (was 0)
- accessibility leak guard over all 46 questions — **0 leaking**
- answer-key referential integrity over all 46 questions — **0 problems**
- textbook profiles restored after the known compiler clobber — **13 textbooks, 299 chapter
 entries** (the compile had reduced the file to 13)
- `pytest tools/topic_packages/tests/ -q` after the figure work — **143 passed** (new
 diagram-asset cases included)
- every image block in the compiled reader resolves — **9 of 9, zero empty urls** (was 1 empty)
- each figure was **visually inspected as a raster before wiring in**, which is how three defects
 were caught: mojibake from RDKit's ISO-8859-1 header, captions colliding with the rings, and an
 `atomLabel` that had overwritten adenine's exocyclic amino group

### Still recommended

The figure cluster (rec-004, rec-005, rec-006) has since been **drawn and wired in** — see the
figure entries in the changes list above. The one figure recommendation still open is the Haworth
alpha/beta pair (rec-015), which needs a depiction style the package does not yet use. Platform tickets remain for hotspot target naming
(rec-002), structure_scaffold input (rec-003), `accessible_description` delivery (rec-019),
question-stimulus alt text (rec-018), and reader delivery of practice checks and section
metadata (rec-016). Assessment coverage gaps (rec-017, rec-011's objective items) are
recorded for a future bank expansion.
