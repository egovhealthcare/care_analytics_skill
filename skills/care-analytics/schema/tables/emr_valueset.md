# emr_valueset (ValueSet)

app: emr | source: care/emr/models/valueset.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `slug` string(255) UNIQUE
- `name` string(255)
- `description` string
- `compose` jsonb default=dict
- `status` string(255)
- `is_system_defined` boolean default=False

JSONB shapes (`history`, `meta`, `compose`): `jsonb/emr_valueset.md`
