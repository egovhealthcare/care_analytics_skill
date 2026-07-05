# Curated notes

Human-owned context that survives schema regeneration (`scripts/build.sh`
never writes here). The skill reads these alongside the generated shards.

## Layout

- `_general.md` — cross-cutting facts: deployment specifics, business
  definitions, which plugins are enabled, reporting conventions.
- `<db_table>.md` — facts about one table, named exactly like its shard in
  `schema/tables/` (e.g. `emr_encounter.md`).

## Note format

Short, dated bullets. Example `emr_encounter.md`:

```markdown
# emr_encounter — curated notes

- (2026-07) `status` literals: planned, in_progress, on_hold, discharged,
  completed, cancelled, discontinued, entered_in_error, unknown
- (2026-07) "Active encounter" for reporting = status IN
  ('in_progress', 'on_hold')
- (2026-07) `period->>'start'` is reliable; `period->>'end'` is NULL for
  ~30% of completed encounters before 2025 — fall back to modified_date
```
