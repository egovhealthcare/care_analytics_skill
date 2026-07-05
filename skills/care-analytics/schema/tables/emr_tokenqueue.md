# emr_tokenqueue (TokenQueue)

app: emr | source: care/emr/models/scheduling/token.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `resource` foreign_key -> emr_schedulableresource [col: resource_id]
- `name` string(255)
- `is_primary` boolean default=True
- `date` date
- `system_generated` boolean default=False

JSONB shapes (`history`, `meta`): `jsonb/emr_tokenqueue.md`
