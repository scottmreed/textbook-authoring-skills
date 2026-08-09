# Chapter review — Acid-Base Concepts and Electron Flow (`acids-bases-and-curved-arrows`)

_Reviewed 2026-07-30 · chapter version 1 · personas: Instructor, Struggling
Student, Accessibility, Visual Preference_

**Publication readiness: major revision**

The chapter has a coherent conceptual sequence, varied and mostly sound
assessments, helpful feedback, and neutral accessible descriptions. It is not
ready to publish. Three chapter-local chemistry blockers misstate ammonium
acidity, reverse the period/group acidity rule in concept metadata, and call
the product-side ammonium ion an amine. The larger instructional defect is that
the core curved-arrow examples and four table-labeled assets compile as
unrelated single molecules, leaving the reader without the representations
their titles and descriptions promise.

### Top blockers

- **[BLOCKER] Amine/ammonium/oxonium acidity is conflated** — source detail
 levels put protonated amines near pKa 0 instead of about 9–11 and blur an
 amine with its conjugate acid. (`instr-001`, `struggling-007`;
 `nugget-functional-group-acidities`)
- **[BLOCKER] Periodic acidity metadata is reversed** — the trouble-spot text
 says size dominates across a period, contradicting the correct reader rule.
 (`instr-002`; concept `structure-and-acidity`)
- **[BLOCKER] The equilibrium example names the wrong acid** — ammonium, not
 the neutral amine, is the product-side acid with pKa about 10.
 (`instr-003`; `nugget-equilibrium-direction`)
- **[BLOCKER] The foundational arrow examples do not exist on screen** —
 diagram-titled assets compile as isolated ammonia or water molecules, with
 no acceptor, leaving group, product, or arrows. (`struggling-001`, also
 `instr-004`, `access-001`, `visual-001`)

### Top 5 recommended changes

1. **Correct the acid/base identities and pKa ranges** — align every detail
 tier around neutral amine N–H acidity, ammonium conjugate-acid pKa, and
 protonated-alcohol acidity. → **prose edit** (prose, blocker)
2. **Replace the curved-arrow placeholders** — provide chemically complete
 one-arrow and two-arrow examples whose visible and nonvisual content agree.
 → **new figure** (figure, blocker)
3. **Replace molecule placeholders posing as tables** — expose the actual pKa,
 structural-factor, and ΔG°/Keq comparisons. → **new figure** (figure, high)
4. **Assess the two-arrow objective** — require both coordinated electron-pair
 movements in a focused item. → **added practice** (assessment, high)
5. **Align instruction and assessment** — teach induction, phenol's pKa
 benchmark, resonance reasoning, and donor/acceptor recognition before they
 are graded. → **prose edit** (prose, high)

### Persona status cards

| Persona | Score | Blockers | Headline |
|---|---:|---:|---|
| Organic Chemistry Instructor | 4.1/10 | 3 | Three chemistry errors plus missing/misleading instructional figures |
| Struggling Student | 4.1/10 | 2 | No usable worked arrow example; contradictory amine pKa guidance |
| Accessibility Persona | 7.8/10 | 0 | Activities are operable, but visible and nonvisual figure content disagree |
| Learner with Visual Preference | 3.8/10 | 0 | The compiled visual layer does not deliver the authored relationships |

### Affected sections & assets

`electron-pair-donors-acceptors`, `curved-arrow-notation`,
`bronsted-lowry-framework`, `pka-and-acid-strength`,
`common-organic-acid-pkas`, `equilibrium-prediction`,
`structure-and-acidity`, `free-energy-and-equilibrium-constants`;
assets `asset-electron-pair-flow-diagram`,
`asset-curved-arrow-association`, `asset-curved-arrow-displacement`,
`asset-conjugate-pair-diagram`, `asset-pka-scale-table`,
`asset-functional-group-pka-table`, `asset-acidity-factors-table`,
`asset-delta-g-keq-table`; questions `ch2-lewis-arrow`,
`ch2-bronsted-acids-select`, `ch2-pka-match`,
`ch2-acidity-factors-matrix`.

---

## Full evidence

The exact schema-valid envelopes, including every verbatim evidence field and
open question, are embedded in
[`chapter-review.json`](chapter-review.json). The independent reports below are
kept separate so no persona's evidence is flattened into the synthesis.

### Independent persona report — Organic Chemistry Instructor

**Score:** 4.1/10 · **Verdict:** not ready for instructor use 
**Strengths:** coherent sequence; all inspected SMILES parse; reviewed answer
keys are sound; varied assessment types; generally explanatory feedback.

- **`instr-001` · blocker · chemical-accuracy** —
 `nugget-functional-group-acidities`: source standard/expanded prose assigns
 protonated amines the acidity of protonated alcohols and then calls primary
 amines weak acids using their conjugate-acid pKa. **Impact:** students confuse
 neutral amines, ammonium ions, and oxonium ions. **Need:** one correct
 distinction across all tiers. **Confidence:** 0.99.
- **`instr-002` · blocker · chemical-accuracy** — concept
 `structure-and-acidity`: metadata says “size dominates across a period,”
 reversing the correct across-period/down-group rule. **Impact:** adaptive or
 instructor guidance can teach wrong rankings. **Need:** electronegativity
 across a period; size/polarizability down a group. **Confidence:** 0.99.
- **`instr-003` · blocker · chemical-accuracy** —
 `nugget-equilibrium-direction`: the product-side acid is called “the amine”
 even though it is ammonium. **Impact:** students compare the wrong conjugate
 pair member. **Need:** name each actual acid species. **Confidence:** 0.99.
- **`instr-004` · high · figure-accuracy** —
 `asset-curved-arrow-displacement`: arrow assets contain only `N` or `O`
 SMILES while claiming complete reactions. **Impact:** no inspectable arrow
 source, sink, or bond change. **Need:** chemically faithful arrow examples.
 **Confidence:** 0.99.
- **`instr-005` · high · objective-alignment** — `ch2-lewis-arrow`: both
 curved-arrow items assess one-arrow association; neither assesses the stated
 two-arrow displacement objective. **Impact:** a student can pass without the
 chapter's main arrow skill. **Need:** a complete two-arrow task.
 **Confidence:** 0.99.
- **`instr-006` · high · objective-alignment** —
 `ch2-acidity-factors-matrix`: assessment uses induction before instruction
 and leaves size/across-period decisions unmeasured. **Impact:** students are
 graded on an untaught model. **Need:** align prose, objectives, and bank.
 **Confidence:** 0.98.
- **`instr-007` · high · sequencing** — `nugget-structure-acidity`: resonance
 is required by prose and a key but neither taught nor declared as a
 prerequisite. **Impact:** acetate stabilization becomes memorization.
 **Need:** establish equivalent contributors or a prerequisite.
 **Confidence:** 0.96.
- **`instr-008` · high · misconception** — `nugget-pka-scale`: stronger acid is
 said to generate lower pH without equal-concentration/media conditions.
 **Impact:** pKa becomes a mistaken direct predictor of any sample's pH.
 **Need:** qualify the comparison. **Confidence:** 0.95.
- **`instr-009` · high · figure-accuracy** — `asset-pka-scale-table`: four
 table-labeled assets compile as methane or acetic-acid cards. **Impact:** the
 promised numeric and structural comparisons are absent. **Need:** faithful
 visible values, labels, units, and trends. **Confidence:** 0.99.
- **`instr-010` · medium · assessment-readiness** —
 `ch2-bronsted-acids-select`: “can act as a Brønsted acid in water” supplies
 no threshold that cleanly selects ethanol but excludes propane. **Impact:** a
 careful interpretation can disagree with the key. **Need:** an explicit
 criterion. **Confidence:** 0.89.

### Independent persona report — Struggling Student

**Score:** 4.1/10 · **Blockers:** `struggling-001`, `struggling-007` 
**Strengths:** recognizable progression; repeated lower-pKa mnemonic; targeted
wrong-answer explanations; recurring familiar compounds; varied practice types.

- **`struggling-001` · blocker · worked-example-gap** —
 `asset-curved-arrow-displacement`: the lesson promises association and
 displacement drawings but renders isolated `N` and `O`. **Impact:** the
 learner rereads, cannot trace the moves, and guesses in the editor. **Need:**
 inspectable sources, destinations, bond changes, and products.
 **Confidence:** 0.99.
- **`struggling-002` · high · conceptual-support** —
 `nugget-electron-pair-flow`: lone pairs, pi systems, carbocations, incomplete
 octets, BF3, and AlCl3 arrive without recognition guidance. **Impact:** the
 learner sorts by familiarity or apparent charge. **Need:** a concrete
 electron-counting/recognition bridge. **Confidence:** 0.96.
- **`struggling-003` · high · misconception** — `nugget-pka-scale`: the
 unqualified pH sentence contradicts the standard tier's pH/pKa distinction.
 **Impact:** “lower pKa always means lower pH.” **Need:** conditions in every
 tier. **Confidence:** 0.98.
- **`struggling-004` · high · conceptual-support** —
 `nugget-equilibrium-direction`: the product-side ammonium is called an amine.
 **Impact:** the learner searches for and compares the wrong species.
 **Need:** consistent species names and pKa mapping. **Confidence:** 0.99.
- **`struggling-005` · high · assessment-readiness** — `ch2-pka-match`: phenol
 near pKa 10 is assessed before it appears in prose or the claimed table.
 **Impact:** the learner answers by elimination. **Need:** teach the benchmark
 and phenoxide stabilization first. **Confidence:** 0.99.
- **`struggling-006` · high · assessment-readiness** —
 `ch2-acidity-factors-matrix`: induction appears first in graded feedback.
 **Impact:** the learner pattern-matches fluorine without the through-sigma
 explanation. **Need:** connect withdrawal to conjugate-base stability before
 assessment. **Confidence:** 0.98.
- **`struggling-007` · blocker · misconception** —
 `nugget-functional-group-acidities`: source tiers assign ammonium pKa near 0,
 compiled prose says 10–11, and a question gives neutral ammonia N–H acidity
 near 38. **Impact:** the learner memorizes whichever number appeared last.
 **Need:** explicit chemical-species distinctions. **Confidence:** 1.0.
- **`struggling-008` · medium · cognitive-load** —
 `nugget-free-energy-equilibrium`: teacher-optional advanced metadata is lost
 in the reader. **Impact:** optional quantitative thermodynamics appears core.
 **Need:** preserve optional status. **Confidence:** 0.98.
- **`struggling-009` · medium · retrieval-practice** —
 `nugget-curved-arrow-rules`: all eight source `practice_check`s disappear
 from the reader. **Impact:** misunderstanding surfaces only after concepts
 accumulate. **Need:** deliver timely low-stakes checks. **Confidence:** 0.97.
- **`struggling-010` · high · cognitive-load** —
 `asset-pka-scale-table`: comparison summaries render unrelated molecules.
 **Impact:** the supposed support adds uncertainty and forces prose mining.
 **Need:** expose the promised relationships. **Confidence:** 0.99.
- **`struggling-011` · high · objective-alignment** — `ch2-lewis-arrow`: the
 two-arrow objective has no compiled item. **Impact:** one-arrow success looks
 like complete mastery. **Need:** perform and receive feedback on a coordinated
 two-arrow move. **Confidence:** 0.99.

### Independent persona report — Accessibility Persona

**Score:** 7.8/10 · **Blockers:** none 
**Strengths:** all 15 task descriptions are neutral; structure stimuli have
names/text; reviewed question controls are keyboard labeled; core prose is a
substantial text equivalent; empty videos are hidden.

- **`access-001` · high · alt-text-quality** —
 `asset-electron-pair-flow-diagram`: visible single-molecule renders and
 nonvisual descriptions refer to different chemical objects. **Impact:**
 magnified, speech-plus-visual, and screen-reader experiences have no shared
 reference. **Need:** equivalent visible and nonvisual content.
 **Confidence:** 0.99.
- **`access-002` · medium · alt-text-quality** —
 `asset-acidity-factors-table`: alt text names four row headings but omits
 every trend and example, with no extended description. **Impact:** direct
 figure navigation cannot recover the summary. **Need:** a complete ordered
 factor/trend/example readout. **Confidence:** 0.96.
- **`access-003` · medium · keyboard-operability** —
 `asset-electron-pair-flow-diagram`: section h2 headings are followed directly
 by molecule h4 headings. **Impact:** heading navigation implies missing
 structure. **Need:** contiguous semantic heading levels. **Confidence:** 0.98.

### Independent persona report — Learner with Visual Preference

**Score:** 3.8/10 · **Blockers:** none 
**Strengths:** coherent relationship order; useful scoped video storyboard;
structure-plus-name pKa matching; useful comparison-matrix organization.

- **`visual-001` · high · figure-accuracy** —
 `asset-curved-arrow-association`: all three electron-flow figures lack the
 reactions and arrows named by their titles. **Impact:** no visual inspection
 of source, sink, count, or bond change. **Need:** faithful complete content or
 removal/reframing. **Confidence:** 0.99.
- **`visual-002` · high · figure-accuracy** —
 `asset-conjugate-pair-diagram`: only acetic acid is rendered; water, acetate,
 hydronium, transfer, and four role labels are absent. **Impact:** the pair
 relationship is not made visible. **Need:** complete static scheme or honest
 reframing. **Confidence:** 0.99.
- **`visual-003` · high · figure-accuracy** — `asset-pka-scale-table`: all four
 quantitative/comparison “tables” are single molecule structures.
 **Impact:** learners meet unrelated structures instead of ordered values.
 **Need:** real visible rows/comparisons or remove the blocks.
 **Confidence:** 0.99.
- **`visual-004` · high · visual-opportunity** — `ch2-lewis-arrow`: learners
 enter the editor without a functioning worked arrow diagram. **Impact:** the
 item partly tests interface/notation interpretation. **Need:** an inspectable
 source-to-sink example mapped to editor sites. **Confidence:** 0.97.
- **`visual-005` · medium · visual-opportunity** —
 `nugget-equilibrium-direction`: two acids, two pKa values, favored side, and
 exponent calculation are paragraph-bound. **Impact:** working-memory load
 replaces visible alignment. **Need:** align side, acid, pKa, and direction.
 **Confidence:** 0.96.
- **`visual-006` · medium · visual-opportunity** —
 `nugget-structure-acidity`: parent acids, conjugate bases, charge
 distribution, and hybridization comparisons remain verbal. **Impact:**
 transfer to structure questions is difficult. **Need:** compact static or
 structured comparisons. **Confidence:** 0.96.
- **`visual-007` · medium · alt-text-quality** —
 `asset-functional-group-pka-table`: descriptions claim uncertain or
 nonexistent visuals, including “bar chart or table.” **Impact:** the
 description cannot be equivalent to a definite final visual. **Need:** exact
 correspondence with final content. **Confidence:** 0.99.

### Orchestrator decisions

The 18 ranked decisions are preserved in the machine report. The major
intervention calls are:

- Correct `instr-001/002/003`, `struggling-003/004/005/006/007`,
 `instr-006/008/010` with bounded prose/assessment edits.
- Use **new static figures**, not animation, for the conjugate-pair scheme and
 four table/comparison needs. The relationships are static.
- Use a complete arrow-pushing figure or static sequence for the one-arrow and
 two-arrow examples; prose and alt text alone cannot make the current isolated
 molecules faithful.
- Keep optional-status delivery, source `practice_check` delivery, and the h2→h4
 hierarchy as platform/compiler findings rather than chapter-local hacks.
- Leave broad question-bank expansion unapplied; only the focused two-arrow
 objective gap is recommended.

### Merged duplicates

- `instr-001` + `struggling-007` → one amine/ammonium/oxonium correction.
- `instr-003` + `struggling-004` → one equilibrium-species correction.
- `instr-004` + `struggling-001` + `access-001` + `visual-001` +
 `visual-004` → one curved-arrow representation cluster, retaining the
 strongest severity (`blocker`) and all learning/access impacts.
- `instr-009` + `struggling-010` + `access-001` + `visual-003` +
 `visual-007` → one placeholder-table cluster.
- `instr-005` + `struggling-011` → one two-arrow assessment gap.
- `instr-006` + `struggling-006` → one induction alignment gap.
- `instr-008` + `struggling-003` → one pH/pKa misconception correction.

### Retained disagreements

**Are the placeholder curved-arrow figures a publication blocker?**

- Struggling Student: yes—the learner cannot reconstruct the foundational move
 before assessment.
- Instructor and Visual Preference: high severity—the prose is chemically
 correct, but the figure layer is missing/misleading.
- Accessibility: high severity, but no required activity is demonstrably
 impossible without vision or fine-pointer input.

**Resolution:** retain the Struggling Student's blocker. It forces at least
`major revision`; because no required-access path is impossible, it does not
force `blocked`.

### Places where a description is sufficient (no new asset)

- All 15 question accessible descriptions are sufficient and leak no answers.
- Keyboard labels are sufficient for the reviewed ranking, matching,
 categorization, matrix, and curved-arrow controls.
- Hidden state is sufficient for the unfinished empty-URL video blocks.
- The two comparison-matrix questions already provide useful side-by-side
 organization; their immediate defect is missing prior explanation.
- A structured extended description is sufficient for a completed acidity
 table; animation is unnecessary.

### Regression targets for next run

Recheck `instr-001`, `instr-002`, `instr-003`, `instr-004`, `instr-005`,
`instr-006`, `instr-007`, `instr-008`, `instr-009`, `instr-010`,
`struggling-001`, `struggling-003`, `struggling-004`, `struggling-005`,
`struggling-006`, `struggling-007`, `struggling-011`, `access-001`,
`access-002`, `access-003`, `visual-001`, `visual-002`, `visual-003`,
`visual-004`, `visual-005`, `visual-006`, and `visual-007`.

### Orchestrator integrity check (pre-dispatch)

Clean. `topic_id`, `reader_slug`, concept/nugget/asset/question references,
reader section IDs, and all 15 compiled question slugs agree across surfaces.
All eight compiled external links resolve to intended Wikipedia pages. No
`orchestrator-*` finding was added.

---

## Post-correction record

**Estimated state: major revision (not a second persona verdict).**

### Changes applied

- Distinguished neutral amine N–H acidity (about 35–40), ammonium
 conjugate-acid pKa (about 9–11), and oxonium acidity (about −2) in every
 functional-group-acidity tier; added phenol near pKa 10 and the phenoxide
 rationale — resolves `instr-001`, `struggling-005`, `struggling-007`.
- Corrected the concept trouble-spot rule to electronegativity across a period
 and size/polarizability down a group — resolves `instr-002`.
- Named ammonium as the product-side acid in the worked equilibrium — resolves
 `instr-003`, `struggling-004`.
- Qualified the stronger-acid/lower-pH comparison by solvent, temperature, and
 analytical concentration — resolves `instr-008`, `struggling-003`.
- Added induction instruction using trifluoroethanol and chloroacetic acid,
 explained acetate's two equivalent resonance contributors, and aligned the
 learning objective — resolves `instr-007`, `struggling-006`; partially
 addresses `instr-006` because size/across-period assessment coverage is still
 absent.
- Added the exact donor/acceptor recognition logic needed for BF3, AlCl3,
 trimethylamine, and dimethyl ether — resolves `struggling-002`.
- Reframed the ambiguous Brønsted multi-select around an explicit O–H criterion
 and aligned its feedback, hint, and accessible description — resolves
 `instr-010`.

### Verification

- `jq empty content/organic/topic-packages/acids-bases-and-curved-arrows/topic.package.json`
 — valid JSON.
- Topic-package compiler (proprietary toolchain, not in this repo)
 — clean; 8 concepts, 8 nuggets, 8 assets, 15 questions.
- Automated test suite — passed —
 **143 passed**.
- Synthesized report validator — valid.
- Generated diff inspected; chapter-derived outputs retained and unrelated
 aggregate catalog/profile churn restored.

### Still recommended

- Replace the curved-arrow placeholders. `struggling-001` remains a live
 baseline blocker, so the estimate cannot rise above `major revision`.
- Replace the four molecule placeholders posing as tables and the acetic-acid
 placeholder posing as a conjugate-pair scheme.
- Add focused two-arrow displacement practice.
- Preserve teacher-optional metadata and source `practice_check`s through the
 reader compiler; add the missing extended descriptions; repair the shared
 h2→h4 figure-heading hierarchy.
