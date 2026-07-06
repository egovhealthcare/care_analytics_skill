---
mode: plan-review
task: |-
  /Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md
slug: improve-jsonb-schema-shards
generated: 2026-07-06T11:37:49.924Z
plugin-version: 1.3.1
codex-version: 0.142.4
template-version: 2
plan-path: "/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md"
cwd: "/Users/gigin/git/care_analytics_skill"
git-head: "fbaed1f349ff733ea5b1e27b8b754154dbd3b883"
codex-thread-id: "019f3728-aa35-7421-adb9-37af202bd3fc"
codex-resume-status: resumed
codex-resumed-from: ".hyperclaude/plan-reviews/20260706-1132-improve-jsonb-schema-shards.md"
codex-input-tokens: 3236232
codex-cached-input-tokens: 2973312
codex-output-tokens: 27535
codex-reasoning-output-tokens: 18124
---
# Plan review: 20260706-1621-improve-jsonb-schema-shards.md

### Issues

- **Blocker** — Task 4: `git status must show NO plug-shard deletions ... If ... any plug shard is deleted, the checkout was not pinned correctly — re-pin and rebuild` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:105)).
  New issue. Pinning the CARE SHA does not recreate the external plug source directories that produced the committed `abdm_`, `care_scribe_`, `nhcx_`, and `encounter_identifiers_` shards. The baseline CARE tree at `fd2300f` has no `app/` directory, and the current `.care` checkout has no plug source dirs. So the gate can still fail after a correct pin, and “re-pin and rebuild” will not fix it. Do either a full-plug build with the needed `ADDITIONAL_PLUGS`/`plugs.json`, or keep the no-plug build and explicitly restore/exclude plug-shard and shared-catalog churn before staging.

- **Major** — Task 4: `with the source correctly pinned there is nothing unrelated to restore` ([plan](/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md:106)).
  This is the same faulty assumption in operational form. Core SHA pinning only controls `.care` tracked source; it does not control absent plug checkouts or shared generated files affected by their absence. Keep the restore/exclude step for plug shards and shared catalogs unless the plan also supplies the plug sources.

### Improvements

- Use the simpler no-plug path: pin `CARE_REF`, rebuild, then restore/exclude `abdm_`, `care_scribe_`, `nhcx_`, `encounter_identifiers_`, `_enums.md`, `_index.md`, README, and PROVENANCE unless intentionally staged. Stage only the generator and affected core JSONB shards.
- If full plug parity is required, make `plugs.json`/`ADDITIONAL_PLUGS` an explicit prerequisite instead of relying on the CARE SHA.

### Verdict

Send back for one more fix. Prior findings about Python version, source drift, `_enums.md` staging, count command, table deletion staging, and ambiguous spec guessing are addressed. The remaining blocker is that the new pin gate assumes plug sources come back from the CARE SHA; they do not.