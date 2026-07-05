# nhcx_communication (Communication)

app: nhcx | source: app/care_nhcx/nhcx/models/communication.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(100)
- `priority` string(100) NULL
- `category` jsonb NULL default=list
- `sent` datetime NULL
- `payload` jsonb NULL default=list
- `based_on` foreign_key -> nhcx_communicationrequest [col: based_on_id]
- `part_of` foreign_key -> nhcx_task [col: part_of_id] NULL
- `about` foreign_key -> nhcx_claim [col: about_id]

JSONB shapes (`history`, `meta`, `category`, `payload`): `jsonb/nhcx_communication.md`
