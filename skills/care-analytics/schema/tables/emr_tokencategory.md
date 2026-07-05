# emr_tokencategory (TokenCategory)

app: emr | source: care/emr/models/scheduling/token.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `resource_type` string(255)
- `name` string(255)
- `shorthand` string(255)
- `metadata` jsonb default=dict
- `default` boolean default=False

JSONB shapes (`history`, `meta`, `metadata`): `jsonb/emr_tokencategory.md`
