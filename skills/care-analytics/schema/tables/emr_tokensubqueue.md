# emr_tokensubqueue (TokenSubQueue)

app: emr | source: care/emr/models/scheduling/token.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `resource` foreign_key -> emr_schedulableresource [col: resource_id]
- `name` string(255)
- `status` string(255)
- `current_token` foreign_key -> emr_token [col: current_token_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_tokensubqueue.md`
