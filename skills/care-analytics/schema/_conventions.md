# CARE Analytics SQL Conventions

Target: PostgreSQL 16. Django `JSONField` columns are JSONB.

## Core rules

- Soft delete: `BaseModel` descendants have `deleted`; always filter `deleted = false` unless auditing deletions.
- IDs: `id` is the internal integer PK used by FK joins. `external_id` is the public UUID — expose this in results, never `id`.
- FKs are stored as `<name>_id` integer columns. Join `child.<name>_id = parent.id` unless the shard shows a `to_field`.
- Timestamps: `created_date` / `modified_date` (auto-managed, nullable, indexed).
- `EMRBaseModel` descendants add `history`, `meta` (JSONB), `created_by_id`, `updated_by_id` -> `users_user`.

## JSONB

- Shapes are documented in `jsonb/<db_table>.md`, distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape. Named object types are expanded once per file under `## definitions`.
- Access patterns: `col->>'field'` (text), `col->'nested'` (jsonb), `jsonb_array_elements(col)` for arrays.
- Fields on a `stores (when __store_metadata__)` line live in the `meta` column only for resources that enable it.

## Enum values

- Resolved choices appear inline in table shards as `choices=[a|b|c]` — these are the stored values, use them directly.
- Unresolved symbols (`choices=Status.choices (see _enums.md)`) and columns with no `choices=` at all (common on EMR status/category columns, validated at the API layer): look up `_enums.md` by class name, preferring the definition whose file matches the column's model or resource module. Never guess enum values.

## Caveats

- Plugin tables (sources under `app/`) exist in the catalog but may not be enabled in a given deployment.
- The catalog is source-derived, not introspected from a live database; verify unusual constructs against migrations if in doubt.
