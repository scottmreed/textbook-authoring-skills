# Chapter review — Alkenes: Reactions and Synthesis (`alkenes-reactions-and-synthesis`)

**Run:** 2026-07-31 · chapter version 1 · four persona subagents (claude-opus-5[1m]) + orchestrator integrity check
**Publication readiness (baseline): `blocked`** — computed, not averaged. Persona scores: Instructor 5.4 · Struggling Student 4.3 · Accessibility 4.5 · Visual Preference 5.0.

---

## Compact editorial view

### Verdict

**Blocked.** Two graded items are chemically wrong as depicted, one blocker-level teach-before-grade
gap spans five facts the chapter never contains, nine `accessible_description`s hand
screen-reader users the graded answer (all invisible to the compile-time guard), and the
hotspot items lose their only non-visual path the moment those leaks are removed
(`access-005` is the unresolved required-access blocker that forces `blocked`).
Both `rank_order` items ship pre-solved (the ch6 class) and the whole bank is positionally
predictable (all ten single_selects key `a`).

The chemistry underneath is structurally sound: the instructor persona machine-verified
**all 13 asset SMILES and every structure in all 32 questions** by formula and InChIKey,
and re-derived every answer key's intended outcome — zero misidentified compounds, zero
wrong intended outcomes. The two blockers are depiction/keying errors, not reagent-table errors.

### The recompile-revert class hit this chapter (4th confirmed instance)

- `[commit ref — not in this repo]` fixed all four fabricated Wikipedia links **in the compiled artifact only**
 (to the real Prilezhaev reaction, Dihydroxylation, Ozonolysis, Organic synthesis).
 A later recompile reverted them. **The live reader 404s on 4 of 6 links today.**
 No concept in the package authors a `wikipedia_title`.
- `[commit ref — not in this repo]`-era artifact carried the correct two-reason hydroboration regiochemistry
 explanation (steric bulk + developing δ+ on the more substituted carbon in the
 four-centre TS). Reverted by recompile; the package still holds the weaker
 "boron is electron-deficient" non-sequitur (instr-010).
- Both fixes are back-ported to `topic.package.json` in the correction pass (rec-007, rec-008).

### Blockers (all persona-declared, reconciled)

| # | What | Source |
|---|---|---|
| B1 | `ch8-epox-product-v2` keys a single enantiomer ((2R,3R), InChIKey PQXKWPLDPFFDJP-QWWZWVQMSA-N) as THE product of epoxidizing achiral (E)-2-butene with achiral mCPBA — must be racemic; the (2S,3S) answer is unofferable; racemate principle taught nowhere | instr-001 |
| B2 | `ch8-diol-syn` labels ethylene glycol (OCCO, zero stereocenters) "A syn (cis) 1,2-diol"; v2 renders a structure on ONLY the correct option; v2's drawn "cis" diol carries no stereochemistry | instr-002, instr-003, visual-004/005, access-008 |
| B3 | Graded content never taught: anti epoxide ring-opening, "bromonium", 9-BBN, hot-vs-cold KMnO₄, alkyne hydrogenation — each 0 occurrences in every prose tier | stud-002, instr-007 |
| B4 | Nine `accessible_description`s state the graded answer (draw items name the product to draw; hotspots name the atom to select; 3 short answers list accepted strings; both route items give the full mapping; one numeric performs the counting). Compile guard clean on all — the leaks are semantic | access-001..004, access-009 |
| B5 | Hotspot items have no neutral non-visual orientation once de-leaked — renderer says only "C atom 1..4" (platform ticket, ch25/26/28 class); chapter-side connectivity readout required so a valid attempt exists | access-005 |
| B6 | Both `rank_order` items authored cards in exactly the key order; renderer submits presented order untouched (ch6 class). Plus whole-bank positional bias: 10/10 single_selects key `a`, multi_selects `a,b`, matching/categorize keys in listed order | stud-004 (+ orchestrator check) |

### The unanimous instructional finding

**A reactions chapter in which no reaction is drawn.** All 13 figures are flat, isolated
structures; no arrow, reagent, intermediate, or mechanism is depicted anywhere despite five
of six nuggets being typed `mechanism`; and all three syn-stereochemistry claims are
illustrated on substrates where stereochemistry is invisible (butane; one-stereocenter
propene products). The osmate ester and peroxyacid O–O bond — the chapter's two causal
arguments — are named and never shown. All four personas found this independently
(instr-004/005/006, stud-001/008, visual-001/002, access none — carried in prose, so it is
a learnability failure, not an access failure).

### Also found

- All 6 practice_checks and 6 trouble_spots reach no student (artifact predates the ch30
 callout emitter; recompile closes this for free).
- Hint ladders bottom out by stating the complete answer key on ≥8 items.
- 8 open-response items have `wrong_answer_explanations: []`.
- Two short-answer stems contain their own answers.
- Prerequisite graph wrong on two concepts; "these two chapters" resolves to nothing.
- Notation drift (but-2-ene vs 2-Butene; cis/trans vs E/Z unexplained; mixed subscripts).
- `ch8-ozon-products-v2` option says "Two molecules of propanal", draws one.
- Hotspot `select_count: one_or_more` vs single-atom keys.
- OpenStax ch8 link promises ~2× the coverage this chapter delivers (instructor note).
- Heading hierarchy h1→h2→h4 (platform).

### Sufficient as is (do not over-build)

- The twelve simple molecule alt texts (3–5 heavy atoms) are genuine equivalents — **no
 long_descriptions added**; only differentiate the two byte-identical propene alts and give
 the one complex figure (rc-epoxidation) a full text equivalent.
- Keyboard operability: nothing to fix — all 11 renderers in use are keyboard-complete and
 both draw items already allow typed entry (the ch5 blocker does not recur).
- The two hidden video blocks render as nothing, not as dead affordances (`is_hidden`
 honoured; same evidence as ch28/ch31).

### Disagreements (retained)

1. **Alt-text sufficiency** — Accessibility: one-line alts suffice for simple molecules;
 Visual: alts should carry the teaching point. *Resolution:* both honoured — simple alts
 kept, propene pair differentiated, rc-epoxidation gets the full equivalent.
2. **Hidden videos** — Visual scored the vanishing comparisons high; Accessibility noted
 nothing is broken today. *Resolution:* renderer verified; content gap addressed
 structurally (rec-023 removes the objective's dependency on the deferred video).
3. **Picture-only-on-key severity** — Visual asked for a standing policy; Instructor
 reached blocker via chemical accuracy. *Resolution:* blockers via rec-002; cueing folded
 into the same uniform-treatment fix (ch6/ch7 precedent).

### Ranked recommendations (chosen interventions)

Blockers: rec-001 racemate reframe (prose-edit) · rec-002 diol item re-base on
stereo-expressible substrate (alternate-activity) · rec-003 teach-before-grade
(prose-edit + item re-scope) · rec-004 de-leak nine descriptions (text-equivalent) ·
rec-005 hotspot neutral connectivity readout (structured-chemical-description) ·
rec-006 de-pre-solve rank_order + de-bias keys (alternate-activity).
High: rec-007 wikipedia_titles (verified) · rec-008 back-port hydroboration paragraph ·
rec-009 face-distinguishable syn case (new-figure) · rec-010 reaction schemes (new-figure;
platform `reaction` block already renders) · rec-011 osmate ester + peroxyacid figures ·
rec-012 recompile for callouts (added-practice) · rec-013 hint ladders stay procedural.
Medium/low: rec-014 wrong-answer explanations · rec-015 stems · rec-016 prerequisites +
companion pointer · rec-017 notation · rec-018 rc-epoxidation text equivalent ·
rec-019 heat-of-hydrogenation into standard tier · rec-020 opener/summary frame ·
rec-021 propanal SMILES ×2 · rec-022 select_count · rec-023 reverse-ozonolysis + syn
product items (needs sign-off) · rec-024 video accessibility plans (instructor-note) ·
rec-025 OpenStax scope note · rec-026 heading hierarchy (platform).

---

## Full evidence view

The four validated persona envelopes are embedded verbatim in
[`chapter-review.json`](chapter-review.json) (`personas[]`), including every finding with
location anchors, evidence, learner impact, and confidence. Orchestrator integrity findings
and their classification:

### Orchestrator integrity check

1. **Artifact-vs-package drift (classified per skill step 6a before any recompile):**
 - Links: live artifact and package both carry the four fabricated 404s
 (`Epoxidation_with_a_peroxyacid`, `Syn_dihydroxylation`,
 `Oxidative_cleavage_(ozonolysis)`, `Choosing_reactions_in_synthesis`). The
 `[commit ref — not in this repo]` artifact carried the fixed targets → **correction the package lacks;
 back-port as authored `wikipedia_title`s** (folded into instr-015 → rec-007).
 - Hydroboration paragraph: curated artifact text ("for two reasons… four-centre
 transition state… developing positive charge sits on the more substituted carbon")
 vs live/package "Because boron is electron-deficient…" → **correction the package
 lacks; back-port** (folded into instr-010 → rec-008).
 - Everything else: 173→c8c text diff is zero lines; live differs from curated only in
 that one paragraph + the link set + the later OpenStax link addition (a package change
 the curated artifact predates — keep).
2. **Referential integrity:** all concept refs resolve; all 4 external prerequisite slugs
 resolve to `alkenes-structure-and-reactivity`; nugget `order` is globally sequential
 (1–6, the ch5 trap does not recur).
3. **Cross-surface:** deck `assets.manifest.json` matches the package 13/13 — no SMILES or
 RC-spec drift (the ch7 deck-manifest failure does not recur). RC barrier vocabulary
 valid (`medium`).
4. **Mechanical assessment checks:** both rank_order card orders equal their keys
 (pre-solved); `ch8-diol-syn-v2` illustrates only the key; both hotspot keys are
 `atom_0` with `select_count: one_or_more` (folded into stud-004, visual-005, instr-018).
5. **Link verification:** 7 outbound URLs fetched — OpenStax 200, Catalytic_hydrogenation
 200, Hydroboration-oxidation 200, four 404s as above.

### Category substitution (for regression diffing)

- instr-015 was originally coined `broken-resource-link`; on validator rejection it was
 remapped to `media-equivalence`. If dead-link defects recur across chapters, the schema
 may warrant a dedicated id.

### Open questions carried out of the persona envelopes

- Does any delivery surface shuffle options/cards? (If so, stud-004's positional pattern is
 partially mitigated; the authored keys remain fully predictable and were corrected anyway.)
- Which surface consumes `accessibility_bundle`? The reader questions manifest strips it
 (standing platform gap, first proved on ch16).
- Hotspot atom indexing: keys assume input-SMILES atom order (atom_0 = terminal CH₂ under
 RDKit input-order indexing) — verified correct for these two SMILES during corrections.
- Are the 16 `-v2` staged variants student-visible? Several findings sit in variants;
 severity assumes they can surface.

---

## Post-correction record (2026-07-31, same day — not a new persona verdict)

**Baseline verdict preserved: `blocked`. Post-correction estimate: `major revision`.**
All corrections were made in `topic.package.json` (never the compiled artifact) and then
recompiled, per step 6a — including back-porting the two artifact-only fixes so the
recompile-revert cycle is closed for this chapter.

### 18 correction groups applied

1. **wikipedia_title authored on all 6 concepts**, each HTTP-verified 200
 (Prilezhaev reaction, Dihydroxylation, Ozonolysis, Retrosynthetic analysis restored/added;
 the two working ones made explicit). 7/7 outbound links now 200 (was 3/7).
2. **Hydroboration regiochemistry back-ported** from the [commit ref — not in this repo] artifact into both prose
 tiers, extended with the four-centre-TS developing-charge argument bridged to Markovnikov
 logic, plus 9-BBN.
3. **Racemate blocker (B1)**: ch8-epox-product-v2 now presents the trans epoxide as racemic;
 the achiral+achiral principle is taught in the epoxidation nugget.
4. **Diol blocker (B2)**: ch8-diol-syn rebuilt on cyclopentene with verified stereo structures
 on ALL options (cis = meso S,R; trans = S,S, noted racemic); v2's key-only illustration
 removed. The "syn (cis)" label no longer sits on ethylene glycol.
5. **Teach-before-grade (B3)**: anti back-side ring-opening, bromonium-defined anti addition,
 and hot-vs-cold KMnO₄ now taught in prose; 9-BBN taught; the alkyne variant rebased to
 isoprene (in-chapter chemistry).
6. **Answer leaks (B4)**: nine accessible_descriptions rewritten answer-free.
7. **Hotspot access (B5)**: both items carry a neutral per-atom connectivity readout keyed to
 the renderer's "C atom N" names (input-order indexing verified in [internal source reference — not in this repo]);
 platform atom-naming gap remains a ticket.
8. **Pre-solve + positional bias (B6)**: rank_order cards reordered off the key; single_select
 key display positions now 2,3,2,2,3,2,3,3,2,1 (were 1,1,1,1,1,1,1,1,1,1); matching /
 categorize / route listings shuffled.
9. 16 answer-stating hint rungs across 14 items rewritten to stay procedural.
10. All 8 open-response items gained error-diagnosing feedback (enriched always-firing generic
 explanations — pattern matching on these submission shapes risks the ch27 dead-pattern class).
11. Two self-answering stems rewritten.
12. Prerequisites corrected (ozonolysis → `functional-groups-overview`; synthesis concept
 declares all six upstream reactions); "these two chapters" now names the companion chapter.
13. Notation normalized across 116 student-facing fields (current IUPAC + Unicode subscripts;
 graded fields verified untouched).
14. rc-epoxidation given a full long_description carrying the concerted-TS argument.
15. Heat of hydrogenation taught in the standard tier with real kJ/mol values; hyperconjugation
 glossed; cis/trans = Z/E equivalence stated.
16. Organizing frame at the chapter opening + reagent consolidation in the synthesis section.
17. **Six `reaction` assets added** — first drawn transformations in the chapter; three carry
 verified stereochemistry (1,2-dimethylcyclohexene → cis-1,2-dimethylcyclohexane;
 (E)-but-2-ene → trans epoxide (racemic); cyclopentene → cis-diol) so syn delivery and
 stereospecificity are visible for the first time.
18. Mechanical: propanal option draws two molecules; hotspot `select_count: one`; propene alt
 texts differentiated.

**Recompile bonus:** the artifact predated the ch30 callout emitter — the recompile emitted
**12 callout blocks** (6 practice checks + 6 trouble spots), reaching a student for the first time.

### Verification

- Compile clean (`--write-runtime`), compile-time leak guard passed; `pytest tools/topic_packages/tests/` → **172 passed**.
- All 7 outbound links curl-verified 200.
- Every new/changed stereo SMILES RDKit-verified by CIP + mirror-image (meso) test + InChIKey.
- Compiled-bank audit: 0 pre-solved rank_order items, 0 partial-illustration items, varied key positions.
- Reader block census: 6 text, **12 callout**, 13 molecule, **6 reaction**, 1 reaction_coordinate, 6 external_link, 1 mcmurry_link, 2 video (hidden).
- Aggregate churn inspected: all chapter-derived (deck slide_count 26→32, catalog sha) — no unrelated restores needed. Concurrent uncommitted `nmr_spectrum` platform work (tools/, NMR package) observed in the tree and left untouched.

### Still open (high priority)

- Intermediate figures (osmate ester, peroxyacid O–O, organoborane, ozonide) — rec-011, needs built `diagram` assets.
- Platform: accessible_description reaches no reader surface; hotspot renderer atom naming; h2→h4 heading skip.
- rec-023 bank additions (reverse-inference ozonolysis on a fresh substrate; stereochemical hydrogenation product item) — needs sign-off.
- rec-024 video accessibility plans; rec-025 OpenStax scope statement.

---

## Second correction pass (2026-07-31, same day) — intermediate figures + gated questions

**Post-correction estimate moves to `ready with minor revisions`.** Baseline verdict
(`blocked`) is unchanged and still stands; only a four-persona regression run can issue a
new verdict.

### The four intermediate figures (closes rec-011)

Built by `[internal source reference — not in this repo]chemfig`
canvas; provenance recorded on every asset, `ai_regeneration_allowed: false`). Every claim
printed on a figure is derived in the script, not typed:

| Figure | The argument it makes visible | The invariant asserted |
|---|---|---|
| `osmate-ester.svg` | Why dihydroxylation is syn: a 5-membered ring cannot reach the far face | Osmium is deleted in software and the released diol is asserted **equal** to the chapter's cis (meso) diol and **unequal** to the trans one |
| `peroxyacid-oxygen-transfer.svg` | Why epoxidation is one step: the weak O–O bond and the butterfly TS | Formula subtraction — peracid loses exactly one O, alkene gains exactly one O |
| `hydroboration-four-centre-ts.svg` | Where boron lands and why (δ+ on the more substituted carbon) | The carbon labelled "more substituted" is read off the molecule, not asserted |
| `ozonide-cleavage.svg` | Which former alkene carbon becomes which carbonyl | Ketone vs aldehyde decided by H count; molozonide/ozonide asserted isomeric; carbon count conserved (5 = 5) |

**All four were rasterised and visually inspected before wiring in** — which caught text
overrunning the canvas on all four figures and two label collisions that no schema check
would have seen. A bottom-bound assertion now fails the build rather than shipping clipped
captions. Reader image blocks went 0 → 4, all resolving.

One shared-infra fix was needed: `[internal source reference — not in this repo]#00FF00 # F, Cl`
whitelist entry, but RDKit emits `#00CC00` for chlorine. Chapter 8 is the first to draw a
chlorine (mCPBA), so the guard had never fired; the entry was split rather than the figure
recoloured, since its intent already covered Cl.

### The two questions that needed sign-off — authored, gated to preview

Both are **admin/teacher/contractor preview only** and reach no student:

- **`ch8-ozon-reverse-infer-v2`** — reverse inference on a fresh substrate: cyclohexanone +
 propanal back to propylidenecyclohexane, with a formula-identical C₉H₁₆ in-ring-alkene
 trap (that isomer would open the ring to one molecule, not two).
- **`ch8-hydrog-stereo-product-v2`** — the stereochemical hydrogenation outcome:
 1,2-dimethylcyclopentene + H₂ gives the **cis** (meso) product, verified S,R with an
 InChIKey distinct from the trans (S,S).

**How the gate works:** both are authored as `variant_of` a same-type parent. The seeder
keeps variants at `review_status: draft` and never publishes them, and
`build_public_question_summary` drops them from the student-facing projection. Both are
`demo_eligible: false` and tagged `needs-maintainer-review` + `admin-preview-only`.
Verified: absent from the compiled student projection (16 surfaced, unchanged), present in
the compiled bank. They surface to students only if promoted off `variant_of`.

### Verification

- `[internal source reference — not in this repo]pytest tools/topic_packages/tests/ scripts/figures/tests/ -q` — **213 passed**.
- Reader census: 6 text, 12 callout, 13 molecule, 6 reaction, **4 image**, 1 reaction_coordinate, 6 external_link, 1 mcmurry_link, 2 video (hidden).
- Nothing committed. The working tree also carries another session's in-progress `nmr_spectrum` work (`tools/topic_packages/*`, NMR package, frontend NMR refactor) — observed and left untouched.

---

## Third pass (2026-07-31) — manual review of the figures and the practice checks

### One figure withdrawn

`peroxyacid-oxygen-transfer.svg` (the epoxidation butterfly transition state) was
**reviewed manually and found to depict the transition state incorrectly.** The asset, the
SVG, and its builder function were all removed rather than left in place to be regenerated;
the builder's module docstring records why, so the next author does not rebuild the same
error. The concerted argument it was meant to carry is still made in the prose and in
`rc-epoxidation`'s long_description. Re-authoring needs the butterfly geometry settled
first — in particular the orientation of the peroxyacid O–H relative to the breaking O–O
bond and the carbonyl oxygen that accepts it, which the schematic did not show.

Three figures retained and confirmed good: `osmate-ester.svg`,
`hydroboration-four-centre-ts.svg`, `ozonide-cleavage.svg`. Reader image blocks: 3, all resolving.

### Practice checks now reveal on click (PLATFORM — affects every chapter)

Manual reader review found that ch8's compiled reader printed its own answer directly under the prompt:

> **Check yourself before moving on** — Try it. What is the stereochemical relationship of
> the two hydroxyl groups after OsO₄ dihydroxylation? **Answer.** The two hydroxyl groups
> are syn (cis) — added to the same face of the double bond.

A self-check that answers itself before it is attempted is not a self-check. Fixed at the
platform level:

- `_practice_check_block` now emits the worked answer as `content.reveal` with a
 `reveal_label`, instead of appending `**Answer.** …` to the visible markdown.
- The reader gained a `CalloutBlock` component that renders `reveal` behind a labelled
 control. The answer is **not placed in the DOM until opened**, so it cannot be read ahead
 from the accessibility tree either.
- The builder test now asserts the inverse of what it asserted before — the answer must be
 in `reveal` and must **not** appear in `markdown` — plus two new renderer tests.

This was a standing defect: it was recorded on the epoxides supplement review
("practice_check callouts print their own answers") and never fixed. **33 packages author
practice checks**, and each picks up the reveal on its next recompile.

### Verification

- `pytest tools/topic_packages/tests/ scripts/figures/tests/ -q` — **213 passed**.
- `vitest run src/components/textbook/__tests__ src/components/readers` — **84 passed**, including 2 new reveal tests.
- ch8 recompiled: 6 practice-check callouts carry click-to-reveal answers, **0 print inline**; 3 image blocks resolve.
- Nothing committed.
