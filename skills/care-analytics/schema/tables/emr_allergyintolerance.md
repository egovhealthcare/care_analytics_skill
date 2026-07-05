# emr_allergyintolerance (AllergyIntolerance)

app: emr | source: care/emr/models/allergy_intolerance.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `clinical_status` string(100) NULL
- `verification_status` string(100) NULL
- `category` string(100) NULL
- `criticality` string(100) NULL
- `code` jsonb default=dict
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `onset` jsonb default=dict
- `recorded_date` datetime NULL
- `last_occurrence` datetime NULL
- `note` string NULL
- `copied_from` integer NULL
- `allergy_intolerance_type` string(20) default=allergy

JSONB shapes (`history`, `meta`, `code`, `onset`): `jsonb/emr_allergyintolerance.md`
