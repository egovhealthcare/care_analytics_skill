# emr_requestorder (RequestOrder)

app: emr | source: care/emr/models/supply_request.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(255)
- `status` string(255)
- `note` string NULL
- `tags` array<integer> default=list
- `supplier` foreign_key -> emr_organization [col: supplier_id] NULL
- `priority` string(255)
- `intent` string(255)
- `reason` string(255)
- `category` string(255)
- `origin` foreign_key -> emr_facilitylocation [col: origin_id] NULL
- `destination` foreign_key -> emr_facilitylocation [col: destination_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_requestorder.md`
