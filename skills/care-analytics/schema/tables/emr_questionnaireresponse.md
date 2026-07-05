# emr_questionnaireresponse (QuestionnaireResponse)

app: emr | source: care/emr/models/questionnaire.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `questionnaire` foreign_key -> emr_questionnaire [col: questionnaire_id] NULL
- `subject_id` uuid
- `responses` jsonb default=list
- `structured_responses` jsonb default=dict
- `structured_response_type` string NULL
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `form_submission` foreign_key -> emr_formsubmission [col: form_submission_id] NULL
- `status` string(255) default=completed

JSONB shapes (`history`, `meta`, `responses`, `structured_responses`): `jsonb/emr_questionnaireresponse.md`
