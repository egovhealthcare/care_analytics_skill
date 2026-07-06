---
mode: plan-review
task: |-
  /Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md
slug: improve-jsonb-schema-shards
generated: 2026-07-06T11:34:17.610Z
plugin-version: 1.3.1
codex-version: 0.142.4
template-version: 2
plan-path: "/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md"
cwd: "/Users/gigin/git/care_analytics_skill"
git-head: "fbaed1f349ff733ea5b1e27b8b754154dbd3b883"
codex-thread-id: "019f3728-aa35-7421-adb9-37af202bd3fc"
codex-resume-status: resumed
codex-resumed-from: ".hyperclaude/plan-reviews/20260706-1128-improve-jsonb-schema-shards.md"
codex-input-tokens: 2507288
codex-cached-input-tokens: 2265344
codex-output-tokens: 23831
codex-reasoning-output-tokens: 16093
---
# Plan review: 20260706-1621-improve-jsonb-schema-shards.md

### Issues

- **Major** — Task 4: stage `_enums.md` after a no-plug build ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:104)).
  Prior plug-scope finding is only partly addressed. The plan now restores plug shard deletions under `jsonb/` and `tables/`, but `_enums.md` is also regenerated from the no-plug source scope. Current diff shows it drops plug enum sections for `care_abdm`, `care_nhcx`, `care_scribe`, and `encounter_identifiers`. Do not stage `_enums.md` from a no-plug build unless that loss is intended; either restore `_enums.md` too, or run a full-plug build before staging shared catalogs.

- **Major** — Task 4: `PYTHON=python3.13 scripts/build.sh` with default `CARE_REF=develop` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:102)).
  New issue. This updates/generates from whatever `develop` is today, and current diff already shows the generated `care_sha` changed. If the plan stages regenerated JSONB shards but omits `PROVENANCE`/coverage/index files, the committed shards can reflect a newer CARE source while metadata still describes the old one. Pin `CARE_REF` to the currently committed `PROVENANCE` SHA for a generator-only change, or explicitly treat this as a source refresh and stage the corresponding metadata/index changes after review.

### Improvements

- Use one source scope for the whole artifact set. The simplest safe path is: pin `CARE_REF` to the existing provenance SHA, run the no-plug build, restore all plug-scope/shared churn, and stage only generator plus affected non-plug JSONB shards.
- Add `_enums.md`, `_index.md`, `README.md`, and `PROVENANCE` to the “restore or intentionally stage” decision, not just `jsonb/` and `tables/`.

### Verdict

Ship after fixes. The previous Python command, table deletion, count command, and threading-summary issues are addressed. The remaining risk is still scope control: no-plug regeneration leaks through shared catalogs, and unpinned `develop` can mix source drift into a generator-only change.