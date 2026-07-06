---
mode: plan-review
task: |-
  /Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md
slug: improve-jsonb-schema-shards
generated: 2026-07-06T11:23:47.730Z
plugin-version: 1.3.1
codex-version: 0.142.4
template-version: 2
plan-path: "/Users/gigin/git/care_analytics_skill/.hyperclaude/plans/20260706-1621-improve-jsonb-schema-shards.md"
cwd: "/Users/gigin/git/care_analytics_skill"
git-head: "fbaed1f349ff733ea5b1e27b8b754154dbd3b883"
codex-thread-id: "019f3728-aa35-7421-adb9-37af202bd3fc"
codex-resume-status: fresh
codex-input-tokens: 1060831
codex-cached-input-tokens: 869248
codex-output-tokens: 11737
codex-reasoning-output-tokens: 7543
---
# Plan review: 20260706-1621-improve-jsonb-schema-shards.md

### Issues

- **Blocker** — Task 3: `fetch candidates = spec_name_index.get(simple_name(ref), [])` for `PatientIdentifierListSpec`.
  This will not resolve as written. `PatientIdentifierListSpec` has no declared fields of its own and inherits from `BasePatientIdentifierSpec`, while the parser only includes spec classes with fields, model markers, or direct spec bases ([generator](/Users/gigin/git/care_analytics_skill/scripts/generate_ai_analytics_schema.py:745), [source](/Users/gigin/git/care_analytics_skill/.care/care/emr/resources/patient_identifier/spec.py:79)). It will not be in `spec_name_index`, so the fallback has no candidate. Resolve the imported FQN from `source_spec["imports"]` and ensure inherited-only imported specs can be collected.

- **Major** — Task 3: `These are duplicate specs across modules with the same field shape`.
  False for `DurationSpec`: specimen has `value: int`; specimen definition has `value: Decimal` ([specimen](/Users/gigin/git/care_analytics_skill/.care/care/emr/resources/specimen/spec.py:41), [specimen_definition](/Users/gigin/git/care_analytics_skill/.care/care/emr/resources/specimen_definition/spec.py:73)). A sorted/package fallback can silently document the wrong shape. Use the parsed import map first; `ProductKnowledge` explicitly imports `DurationSpec` from `care.emr.resources.specimen.spec` ([source](/Users/gigin/git/care_analytics_skill/.care/care/emr/resources/inventory/product_knowledge/spec.py:17)).

- **Major** — Task 4: `python3 scripts/test_jsonb_enum_resolution.py`.
  Importing `collect_embedded_definitions` imports the whole generator, and the generator resolves/clones/updates the CARE checkout at module import time ([generator](/Users/gigin/git/care_analytics_skill/scripts/generate_ai_analytics_schema.py:117)). That makes the “~25 lines, no framework” check non-isolated and environment-dependent. Either make the generator import-safe first, or drop the script and verify through the real rebuild.

- **Major** — Task 4: `scripts/build.sh` plus `skills/care-analytics/schema/** (regenerated output — commit as-is)`.
  The build deletes all existing table/jsonb shard files before rewriting ([generator](/Users/gigin/git/care_analytics_skill/scripts/generate_ai_analytics_schema.py:1898)). Source scope depends on the local CARE checkout and plugs; in this checkout the current rebuild state shows many plugin shard deletions. Do not commit regenerated output “as-is” unless the same plug/source scope is pinned and deleted shards are explicitly expected.

- **Minor** — Task 2: `Dedupe key ... defn["name"], which is unique per enum class — fine`.
  Not true. The enum catalog already has duplicate enum class names such as `StatusChoices` and `CategoryChoices`. If synthetic keys are needed to avoid collisions in collection, carry that key through rendering instead of collapsing back to `name`.

- **Minor** — Task 1 verification: `grep -rn 'Decimal\|UUID5\|datetime.time' ... returns no unresolved refs hits`.
  That command is not scoped to unresolved refs, so it can fail for harmless occurrences or pass without proving scalar rendering. Grep `unresolved refs:` lines directly, then spot-check the affected field definitions.

### Improvements

- Do not add `enum_index` to `resolve_schema_ref` if enum resolution happens only after it returns `None`; pass it only to `collect_embedded_definitions`.
- Drop `resolve_enum_ref` as a separate helper unless it has more than one caller; inline the simple enum lookup in the collector.
- Drop `scripts/test_jsonb_enum_resolution.py` unless the generator is made import-safe; the rebuild plus targeted grep checks cover this change with less code.

### Verdict

Send back to design. The enum/scalar direction is mostly reasonable, but the ambiguous-spec plan is wrong for the current source, and the rebuild/test steps can produce environment-driven schema churn rather than a controlled fix.

