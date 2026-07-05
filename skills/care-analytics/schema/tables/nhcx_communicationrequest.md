# nhcx_communicationrequest (CommunicationRequest)

app: nhcx | source: app/care_nhcx/nhcx/models/communication.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `identifier` string(100)
- `status` string(100)
- `priority` string(100) NULL
- `category` jsonb NULL default=list
- `authored_on` datetime NULL
- `payload` jsonb NULL default=list
- `replaces` foreign_key -> nhcx_communicationrequest [col: replaces_id] NULL
- `based_on` foreign_key -> nhcx_task [col: based_on_id]
- `about` foreign_key -> nhcx_claim [col: about_id]

JSONB shapes (`history`, `meta`, `category`, `payload`): `jsonb/nhcx_communicationrequest.md`
