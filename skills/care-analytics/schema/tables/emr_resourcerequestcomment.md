# emr_resourcerequestcomment (ResourceRequestComment)

app: emr | source: care/emr/models/resource_request.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `request` foreign_key -> emr_resourcerequest [col: request_id]
- `comment` string

JSONB shapes (`history`, `meta`): `jsonb/emr_resourcerequestcomment.md`
