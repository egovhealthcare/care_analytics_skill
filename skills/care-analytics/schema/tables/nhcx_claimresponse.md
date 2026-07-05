# nhcx_claimresponse (ClaimResponse)

app: nhcx | source: app/care_nhcx/nhcx/models/claim.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `request` foreign_key -> nhcx_claim [col: request_id]
- `use` string(100) NULL
- `status` string(100) NULL
- `outcome` string(100)
- `disposition` string NULL
- `pre_auth_ref` string(255) NULL
- `adjudication` jsonb NULL
- `identifier` jsonb NULL
- `type` jsonb NULL
- `item` jsonb NULL
- `add_item` jsonb NULL
- `total` jsonb NULL
- `error` jsonb NULL

JSONB shapes (`history`, `meta`, `adjudication`, `identifier`, `type`, `item`, `add_item`, `total`, `error`): `jsonb/nhcx_claimresponse.md`
