# CARE Analytics SQL Conventions

Target: PostgreSQL 16. Django `JSONField` columns are JSONB.

## Core rules

- Soft delete: `BaseModel` descendants have `deleted`; always filter `deleted = false` unless auditing deletions.
- IDs: `id` is the internal integer PK used by FK joins. `external_id` is the public UUID — expose this in results, never `id`.
- FKs are stored as `<name>_id` integer columns. Join `child.<name>_id = parent.id` unless the shard shows a `to_field`.
- Timestamps: `created_date` / `modified_date` (auto-managed, nullable, indexed).
- `EMRBaseModel` descendants add `history`, `meta` (JSONB), `created_by_id`, `updated_by_id` -> `users_user`.

## JSONB

- Shapes are documented in `jsonb/<db_table>.md`. `candidate_schemas` come from Pydantic API specs — strong hints, not guarantees; custom serializers can change stored shape.
- Access patterns: `col->>'field'` (text), `col->'nested'` (jsonb), `jsonb_array_elements(col)` for arrays.
- Fields under `meta_stored_fields` live in the `meta` column only when the resource sets `__store_metadata__ = True`.

## Enum values

- `choices=Status.choices` refers to a Django choices class. Grep the table's `source:` file (and its imports) for the class to learn the literal stored values before filtering on them.

## Caveats

- Plugin tables (sources under `app/`) exist in the catalog but may not be enabled in a given deployment.
- The catalog is source-derived, not introspected from a live database; verify unusual constructs against migrations if in doubt.
