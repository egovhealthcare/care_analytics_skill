---
mode: plan-review
task: |-
  /Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md
slug: improve-jsonb-schema-shards
generated: 2026-07-06T11:40:52.211Z
plugin-version: 1.3.1
codex-version: 0.142.4
template-version: 2
plan-path: "/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md"
cwd: "/Users/gigin/git/care_analytics_skill"
git-head: "fbaed1f349ff733ea5b1e27b8b754154dbd3b883"
codex-thread-id: "019f3728-aa35-7421-adb9-37af202bd3fc"
codex-resume-status: resumed
codex-resumed-from: ".hyperclaude/plan-reviews/20260706-1136-improve-jsonb-schema-shards.md"
codex-input-tokens: 4052779
codex-cached-input-tokens: 3768832
codex-output-tokens: 30632
codex-reasoning-output-tokens: 19463
---
# Plan review: 20260706-1621-improve-jsonb-schema-shards.md

### Issues

- **Blocker** — Task 4 restore command: `git restore skills/care-analytics/schema/jsonb/{abdm_,care_scribe_,nhcx_,encounter_identifiers_}* ...` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:106)).
  New issue. After the no-plug build, those files are deleted from the working tree, so zsh expands the unquoted globs before `git restore` runs and fails with `zsh: no matches found`. Use Git pathspecs, not shell globs: quote each wildcard or prefix with `noglob`, e.g. `noglob git restore -- 'skills/care-analytics/schema/jsonb/abdm_*' ...`.

### Improvements

- Replace the long restore glob command with quoted Git pathspecs, one per prefix and directory. It is less clever and actually works for deleted tracked files in zsh.
- Keep the final gate as written: staged set must be exactly the generator plus core JSONB shards.

### Verdict

Ship after fixing the restore command. Prior findings about plug source assumptions, source pinning, `_enums.md`/shared catalog churn, Python version, table deletions, and count command are addressed. The only current blocker is the unquoted restore globs failing after the files are deleted.