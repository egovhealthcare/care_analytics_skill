# emr_condition (Condition)

app: emr | source: care/emr/models/condition.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `clinical_status` string(100) NULL
- `verification_status` string(100) NULL
- `category` string(100) NULL
- `severity` string(100) NULL
- `code` jsonb default=dict
- `body_site` jsonb default=dict
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `onset` jsonb default=dict
- `abatement` jsonb default=dict
- `recorded_date` datetime NULL
- `note` string NULL

JSONB shapes (`history`, `meta`, `code`, `body_site`, `onset`, `abatement`): `jsonb/emr_condition.md`
