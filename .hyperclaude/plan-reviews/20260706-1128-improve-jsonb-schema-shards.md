---
mode: plan-review
task: |-
  /Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md
slug: improve-jsonb-schema-shards
generated: 2026-07-06T11:30:32.388Z
plugin-version: 1.3.1
codex-version: 0.142.4
template-version: 2
plan-path: "/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md"
cwd: "/Users/gigin/git/care_analytics_skill"
git-head: "fbaed1f349ff733ea5b1e27b8b754154dbd3b883"
codex-thread-id: "019f3728-aa35-7421-adb9-37af202bd3fc"
codex-resume-status: resumed
codex-resumed-from: ".hyperclaude/plan-reviews/20260706-1120-improve-jsonb-schema-shards.md"
codex-input-tokens: 2014022
codex-cached-input-tokens: 1794816
codex-output-tokens: 18496
codex-reasoning-output-tokens: 11948
---
# Plan review: 20260706-1621-improve-jsonb-schema-shards.md

### Issues

- **Major** — Task 4: `Run the self-check + rebuild: scripts/build.sh ... needs Python 3.13` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:101)).
  Prior finding remains. The plan notes the 3.13 requirement but still runs the wrapper without setting `PYTHON`; `scripts/build.sh` defaults to `python3` ([build.sh](/Users/gigin/git/care_analytics_skill/scripts/build.sh:17)). In this checkout, `python3` is 3.11.15 and `python3.13` exists. Use `PYTHON=python3.13 scripts/build.sh`, or change the wrapper default.

- **Major** — Task 4: `git restore skills/care-analytics/schema/jsonb/...` then stage `tables/` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:103)).
  Prior scope-aware commit finding is only partially addressed. The restore command covers deleted plug `jsonb/` shards, but the no-plug build also deletes plug `tables/` shards. Staging `tables/` after that can still commit unrelated `abdm_`, `care_scribe_`, `nhcx_`, and `encounter_identifiers_` table deletions. Restore both `schema/jsonb/` and `schema/tables/` plug deletions, or do not stage `tables/` wholesale.

- **Minor** — Task 4: unresolved-ref count command ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:102)).
  New issue. `sed 's/, /\n/g'` splits the line but leaves `unresolved refs:` attached to the first ref, so it is not a clean unique-ref count. Strip the prefix first: `grep -rhoE 'unresolved refs: .*' ... | sed 's/^.*unresolved refs: //' | tr ',' '\n' | sed 's/^ *//' | sort -u | wc -l`.

- **Minor** — Threading summary: ``enum_index` ... is passed to `build_column_jsonb_schema`` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:11)).
  New issue. Current source does not pass it yet; the task step later correctly says to update the caller. Fix the summary wording so it says `enum_index` exists in `build_physical_table_catalog` and must be passed down.

### Improvements

- Do not stage `tables/` unless `git diff -- skills/care-analytics/schema/tables/` shows an intentional non-deletion change. This task is about JSONB definitions; broad table staging is avoidable risk.
- Drop the sorted ambiguous-spec fallback after import-map lookup. If an ambiguous ref has no import evidence, leaving it unresolved is less code and avoids documenting a guessed shape.

### Verdict

Ship after fixes. Prior blockers around `PatientIdentifierListSpec`, divergent `DurationSpec`, standalone import-triggering tests, enum-definition dedupe, and scalar grep verification are addressed in the revised plan. Remaining risk is operational: the build command still uses the wrong default Python, and the scope-aware commit instructions still miss deleted plug table shards.