# emr_formsubmission (FormSubmission)

app: emr | source: care/emr/models/questionnaire.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `questionnaire` foreign_key -> emr_questionnaire [col: questionnaire_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `status` string(255)
- `response_dump` jsonb default=dict

JSONB shapes (`history`, `meta`, `response_dump`): `jsonb/emr_formsubmission.md`
