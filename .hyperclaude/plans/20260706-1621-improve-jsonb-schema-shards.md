---
plugin-version: 1.3.1
---

# Improve JSONB schema shards — resolve enums, scalars, ambiguous specs

Goal: the 3 unresolved-ref buckets (33 enums, 3 scalars, 2 ambiguous specs) collapse to near-zero
so `jsonb/*.md` readers get real enum literals, scalar types, and nested field shapes. All fixes land
in the single generator `scripts/generate_ai_analytics_schema.py`; shards are regenerated, never hand-edited.

Threading summary (verified against source): `enum_index` already exists in
`build_physical_table_catalog` (param, line ~1365) but is NOT yet passed onward — it must be threaded
DOWN into `build_column_jsonb_schema` (call at line ~1386, which needs a new param) and then into
`collect_embedded_definitions`. Pass `enum_index` ONLY into `build_column_jsonb_schema` (line ~1312) and forward
to `collect_embedded_definitions` (line ~1269, call at ~1340) — do NOT thread it into
`resolve_schema_ref` (enum lookup happens in the collector only after spec resolution misses).
Enum dict shape (`parse_enum_classes`, line ~1456): `{"class_name", "source_file", "line", "values"}`;
`enum_index` maps `class_name -> [enum, ...]` and names are NOT unique (StatusChoices/CategoryChoices
recur across files) — dedupe by `source_file + class_name`, never by name alone.

Confirmed source facts driving the spec fixes:
- `PatientIdentifierListSpec` (`.care/care/emr/resources/patient_identifier/spec.py:79`) has NO own
  `AnnAssign` fields and its base `BasePatientIdentifierSpec` is not in `SPEC_BASE_NAMES`, so the parser
  filter at line ~745 (`fields or model_expr or base_names & SPEC_BASE_NAMES`) EXCLUDES it — it is absent
  from `spec_name_index` AND `specs_by_fqn`. A name-index fallback cannot resolve it.
- `DurationSpec` shapes DIVERGE by module: specimen `value: int` (`specimen/spec.py:41`) vs
  specimen_definition `value: Decimal` (`specimen_definition/spec.py:73`). A sorted/same-package pick can
  document the WRONG shape; the referring spec's import map (e.g. ProductKnowledge imports it from
  `care.emr.resources.specimen.spec`, `inventory/product_knowledge/spec.py:17`) is the only reliable
  disambiguator.
- Final spec dicts from `build_specs_catalog` (line ~1139) currently DROP `imports`; it must be added so
  the resolver can read the referring spec's import map.
- `.care/care` local checkout has NO plugs and no `plugs.json`; a plain build DELETES all committed
  abdm_/care_scribe_/nhcx_/encounter_identifiers_ plug shards. The commit step must be scope-aware.

---

## Task 1: Map leaking scalar types (Decimal / UUID5 / time) to scalar names

**Files to create / modify**
- `scripts/generate_ai_analytics_schema.py`

**Steps**
- [ ] In `schema_from_annotation` `ast.Name` mapping (line ~312), add `"Decimal": "decimal"`, `"UUID5": "uuid"`, `"time": "time"` (`UUID`/`UUID4`/`date`/`datetime` already mapped).
- [ ] In the same function's `ast.Attribute` branch (line ~329, alongside `.datetime` / `.date`), add: `dotted.endswith(".time")` → `{"type": "time", "raw": raw}`; `dotted.endswith(".Decimal")` → `{"type": "decimal", "raw": raw}`; `dotted.endswith((".UUID", ".UUID4", ".UUID5"))` → `{"type": "uuid", "raw": raw}`.
- [ ] Add `"decimal": "decimal"` to `SIMPLE_TYPE_NAMES` (dict ending line ~1769; `time`/`uuid` already present) so `type_str` renders it instead of `"?"`.

**Verification**
- After Task 4 rebuild, grep ONLY the unresolved-refs lines: `grep -rh 'unresolved refs:' skills/care-analytics/schema/jsonb/*.md | grep -E 'Decimal|UUID5|datetime.time'` returns nothing. Then spot-check an affected field renders as `decimal`/`uuid`/`time`, e.g. `grep -rn 'decimal\|: time' skills/care-analytics/schema/jsonb/emr_chargeitem.md` shows a real type.

**Commit message**
`fix(schema-gen): map Decimal/UUID5/time annotations to scalar types`

---

## Task 2: Resolve enum-typed refs to inline stored DB values

**Files to create / modify**
- `scripts/generate_ai_analytics_schema.py`

**Steps**
- [ ] Add `enum_index` param to `collect_embedded_definitions` (line ~1269). In the ref loop (line ~1283), when spec resolution yields a usable FQN handle it as today (see Task 3 for the membership guard). When it does NOT, inline the enum lookup (no separate helper — single caller): `candidates = enum_index.get(simple_name(ref), [])`; if candidates, pick the enum whose `source_file == source_spec["source_file"]`, else one whose `source_file` shares the spec's module path, else `sorted(candidates, key=lambda e: (e["source_file"], e["line"]))[0]`. On a hit, add a definition keyed by the synthetic unique key `f"enum::{enum['source_file']}::{enum['class_name']}"` (never collides with spec FQNs), shaped `{"name": enum["class_name"], "key": <synthetic key>, "kind": "enum", "values": enum["values"]}`; do NOT queue children; do NOT add to `unresolved_refs`. Only fall through to `unresolved_refs.add(ref)` when spec AND enum lookups both miss.
- [ ] Add `enum_index` param to `build_column_jsonb_schema` (line ~1312); forward it into the `collect_embedded_definitions` call (line ~1340). Update the caller in `build_physical_table_catalog` (line ~1386) to pass the in-scope `enum_index`.
- [ ] Dedupe enum defs by synthetic key, not name: in `write_jsonb_shards` (line ~1856-1861), change `definitions.setdefault(defn["name"], defn)` to `definitions.setdefault(defn.get("key", defn["name"]), defn)` so distinct same-named enums (StatusChoices etc.) don't collapse to one wrong value list.
- [ ] Render enum defs: in the definition-render loop (line ~1865), branch — if `defn.get("kind") == "enum"` emit `` - `Name`: `'v1' | 'v2' | ...` `` (values `repr`-joined with ` | `, matching `type_str` literal style); else keep `fields_str(defn)`.

**Verification**
- After Task 4 rebuild: `grep -n 'AdmitSourcesChoices\|DietPreferenceChoices\|DischargeDispositionChoices' skills/care-analytics/schema/jsonb/emr_encounter.md` shows each with a `'value' | 'value'` list, not a bare `unresolved refs:` line; the shard's `unresolved refs:` line (if any) no longer lists those three.

**Commit message**
`fix(schema-gen): resolve enum-typed JSONB refs to inline stored values`

---

## Task 3: Resolve ambiguous + inherited-only nested specs via the import map

**Files to create / modify**
- `scripts/generate_ai_analytics_schema.py`

**Steps**
- [ ] Include inherited-only specs: in `parse_spec_classes` (line ~745), broaden the filter to `bool(fields or model_expr or set(base_names) & SPEC_BASE_NAMES or any(name.endswith("Spec") for name in base_names))` so subclasses of specs (e.g. `PatientIdentifierListSpec(BasePatientIdentifierSpec)`) enter `spec_classes`; their fields are then filled by the existing `collect_spec_fields` base-walk. Add a `# ponytail: CARE spec classes all end in "Spec"; include subclasses so inherited-only specs resolve` comment. Ceiling: over-includes any stray `*Spec`-based class — harmless, only surfaces when referenced.
- [ ] Carry the import map: in `build_specs_catalog` (line ~1139), add `"imports": info["imports"]` to the emitted spec dict so `specs_by_fqn[...]["imports"]` is available in the collector.
- [ ] Import-map-first resolution: in `resolve_schema_ref` (line ~1260), before the `resolve_class_name` call, try `imported = source_spec.get("imports", {}).get(simple_name(ref))`; if `imported` is a real spec FQN (caller will verify membership), return it. Else fall back to `resolve_class_name(...)` and return its result (None on ambiguity). No sorted last-resort pick — an ambiguous ref with no import evidence stays in `unresolved_refs` rather than documenting a guessed shape. `# ponytail: import map disambiguates; no-import ambiguity stays unresolved, not guessed`.
- [ ] Guard membership in the collector: in `collect_embedded_definitions` (line ~1288-1290), replace the hard `target_spec = specs_by_fqn[target_fqn]` with a guarded lookup — if `resolve_schema_ref` returns an FQN that is NOT in `specs_by_fqn`, skip the spec branch and fall through to the enum lookup / `unresolved_refs` (prevents a KeyError from an import FQN that was still filtered out).

**Verification**
- After Task 4 rebuild: `grep -rn 'DurationSpec\|PatientIdentifierListSpec' skills/care-analytics/schema/jsonb/` shows both under `## definitions` with a `{field: type, ...}` body and absent from `unresolved refs:` lines. Confirm DurationSpec renders the shape matching the referring column's import (int vs decimal `value`), not a blanket pick — spot-check the specimen vs specimen_definition consumer shards.

**Commit message**
`fix(schema-gen): resolve ambiguous/inherited nested specs via import map`

---

## Task 4: In-build self-check, scoped rebuild, scope-aware commit

**Files to create / modify**
- `scripts/generate_ai_analytics_schema.py` (self-check only — no separate test script)
- `skills/care-analytics/schema/**` (regenerated output — staged selectively, see steps)

**Steps**
- [ ] Add an assert-based self-check called at the TOP of `main()` (line ~1913): `_selfcheck_enum_resolution()` builds stub inputs — a `source_spec` dict with `module`, `source_file`, `imports`, `fields`; a `specs_by_fqn` containing it; an `enum_index` with one enum (`{"class_name":"AdmitSourcesChoices","source_file":"x.py","line":1,"values":["hosp-trans","emd"]}`); a root schema `{"type":"ref","ref":"AdmitSourcesChoices"}` — calls `collect_embedded_definitions([...], specs_by_fqn, {}, enum_index)` and asserts the returned definitions include one with `kind=="enum"` and `values==["hosp-trans","emd"]` and `unresolved_refs == []`. Running it inside `main()` means every `scripts/build.sh` exercises it; no separate module import (which would trigger the import-time clone) is needed. Skipped: import-safety refactor of the module-level clone (line ~117) — YAGNI, the in-`main` check needs no isolation. `# ponytail: self-check runs in main(); no standalone importer to keep isolated`.
- [ ] This is deliberately a NO-PLUG, generator-only change. Plug sources (abdm/care_scribe/nhcx/encounter_identifiers) are absent from the local checkout, so a no-plug rebuild ALWAYS drops their shards + regenerates shared catalogs without plug sections — that churn is restored, not committed (step below). Full plug parity is out of scope; it would require supplying `plugs.json`/`ADDITIONAL_PLUGS` so plug sources clone — call that the explicit prerequisite if ever wanted.
- [ ] PIN the CARE source to the committed baseline SHA before rebuilding, so the CORE (non-plug) shards differ ONLY due to the generator fix, not CARE source drift. Committed `PROVENANCE` records `care_sha: fd2300fee1beb87cfdee299e28264c7bd1cf221d`; `.care/care` has drifted to `c6ca8ef`. Checkout the baseline explicitly (an existing `.care/care` is NOT auto-re-checked-out): `git -C .care/care checkout fd2300fee1beb87cfdee299e28264c7bd1cf221d`.
- [ ] Run the self-check + rebuild pinned: `CARE_REF=fd2300fee1beb87cfdee299e28264c7bd1cf221d PYTHON=python3.13 scripts/build.sh`. `PYTHON=python3.13` is required (`build.sh` defaults to `python3` = 3.11 here; build needs 3.13). A failing self-check aborts the build loudly.
- [ ] Count unresolved refs after: `grep -rhoE 'unresolved refs: .*' skills/care-analytics/schema/jsonb/ | sed 's/^.*unresolved refs: //' | tr ',' '\n' | sed 's/^ *//' | sort -u | wc -l` — expect a drop from ~38 toward 0 (a few genuinely-opaque refs acceptable).
- [ ] RESTORE everything the generator fix didn't intentionally change = every generated file DIRECTLY under `schema/` (the SIX top-level files) PLUS all plug shards under `jsonb/` and `tables/` — i.e. everything except the core (non-plug) jsonb shards. Plug files are DELETED from the working tree, so pass QUOTED git pathspecs (git expands against the index) with `noglob` so zsh doesn't error on no-match. List the six top-level files LITERALLY (never a `schema/*.md` pathspec — it would also match `jsonb/*.md` and clobber the core shards we intend to keep): `noglob git restore -- 'skills/care-analytics/schema/jsonb/abdm_*' 'skills/care-analytics/schema/jsonb/care_scribe_*' 'skills/care-analytics/schema/jsonb/nhcx_*' 'skills/care-analytics/schema/jsonb/encounter_identifiers_*' 'skills/care-analytics/schema/tables/abdm_*' 'skills/care-analytics/schema/tables/care_scribe_*' 'skills/care-analytics/schema/tables/nhcx_*' 'skills/care-analytics/schema/tables/encounter_identifiers_*' skills/care-analytics/schema/PROVENANCE skills/care-analytics/schema/README.md skills/care-analytics/schema/_base_models.md skills/care-analytics/schema/_conventions.md skills/care-analytics/schema/_enums.md skills/care-analytics/schema/_index.md`.
- [ ] SCOPE-AWARE COMMIT (do NOT `git add -A`): `git add` ONLY `scripts/generate_ai_analytics_schema.py` and the CORE (non-plug) `skills/care-analytics/schema/jsonb/*.md` shards that changed. Final gate (backstop): `git status` + `git diff --cached --stat` must show the staged set is EXACTLY the generator file + core jsonb shards — no `tables/` files, no top-level `schema/` files (PROVENANCE, README.md, _base_models.md, _conventions.md, _enums.md, _index.md), no plug shards. If any shared-catalog or plug file is still staged/modified, restore it before committing.

**Verification**
- Pinned `scripts/build.sh` completes (self-check passed, else it aborts); regenerated `emr_encounter.md` shows the three encounter enums with values; unique unresolved-ref count is near 0; after restore + selective add, `git diff --cached --stat` lists ONLY the generator and core jsonb shards — no `tables/` files, no top-level `schema/` files, no plug shards.

**Commit message**
`chore(schema): regenerate jsonb shards with resolved enums/scalars/specs + self-check`
