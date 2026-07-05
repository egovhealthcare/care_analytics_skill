# emr_consent (Consent)

app: emr | source: care/emr/models/consent.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(50)
- `category` string(50)
- `date` datetime
- `period` jsonb default=dict
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `decision` string(10)
- `verification_details` jsonb default=list
- `note` string NULL

JSONB shapes (`history`, `meta`, `period`, `verification_details`): `jsonb/emr_consent.md`
