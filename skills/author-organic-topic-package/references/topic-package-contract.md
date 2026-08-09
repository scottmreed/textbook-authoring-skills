# Topic package contract

Canonical path: proprietary topic-package JSON (not in this repo)

Authoritative implementation:

- validator: proprietary package validator (not in this repo)
- schema: proprietary package schema (not in this repo)
- compiler: proprietary topic-package compiler (not in this repo)
- template: proprietary package template (not in this repo)

Compiler outputs (proprietary assets, not in this repo):

- deck manifest
- reader chapter JSON
- LMS module JSON
- review manifest
- textbook profile lenses
- question-set artifact (when `question_sets[]` is present)
- chapter asset manifest
- `reports/topic-packages/<topic-id>/textbook-mappings.json`
- `reports/topic-packages/<topic-id>/compile-report.json`

`--write-runtime` also merges the chapter into the proprietary reader catalog and all generated textbook lenses.

Validation rejects duplicate IDs, broken references, missing text levels, unsupported/non-editable assets, missing alt text, videos not queued for review, and source-branded public text.

Source evidence belongs only in `evidence[]`. Public slides/assets/videos are compiled without it.
