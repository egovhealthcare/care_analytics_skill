---
mode: plan-review
task: |-
  /Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md
slug: improve-jsonb-schema-shards
generated: 2026-07-06T11:42:52.951Z
plugin-version: 1.3.1
codex-version: 0.142.4
template-version: 2
plan-path: "/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md"
cwd: "/Users/gigin/git/care_analytics_skill"
git-head: "fbaed1f349ff733ea5b1e27b8b754154dbd3b883"
codex-thread-id: "019f3728-aa35-7421-adb9-37af202bd3fc"
codex-resume-status: resumed
codex-resumed-from: ".hyperclaude/plan-reviews/20260706-1139-improve-jsonb-schema-shards.md"
codex-input-tokens: 4776433
codex-cached-input-tokens: 4478976
codex-output-tokens: 32836
codex-reasoning-output-tokens: 20625
---
# Plan review: 20260706-1621-improve-jsonb-schema-shards.md

### Issues

- **Major** — Task 4 restore/final gate omits `_base_models.md` and `_conventions.md` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:106)).
  New issue. The plan restores `_enums.md`, `_index.md`, `README.md`, and `PROVENANCE`, but current generated churn also modifies `_base_models.md` and `_conventions.md`. `_base_models.md` drops plug-derived base sections; `_conventions.md` has unrelated generated text churn. If this is a no-plug, core-JSONB-only commit, restore both too and include them in the final “no shared-catalog files” gate.

### Improvements

- Expand the shared-catalog restore list to include every generated top-level schema file not intentionally staged: `_base_models.md`, `_conventions.md`, `_enums.md`, `_index.md`, `README.md`, and `PROVENANCE`.
- Keep the quoted `noglob git restore -- '...*'` pathspec approach; it fixes the prior zsh/deleted-file blocker.

### Verdict

Ship after fixing the restore list. Prior findings about plug source assumptions, source pinning, `_enums.md` churn, Python version, count command, and unquoted restore globs are addressed. The remaining issue is another shared generated file leak: `_base_models.md` and `_conventions.md` need the same restore/gate treatment.