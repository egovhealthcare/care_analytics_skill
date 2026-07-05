# nhcx_provider (Provider)

app: nhcx | source: app/care_nhcx/nhcx/models/provider.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `participant_code` string(50) NULL UNIQUE
- `encryption_private_key` string NULL
- `facility` one_to_one -> facility_facility.external_id [col: facility_id]
