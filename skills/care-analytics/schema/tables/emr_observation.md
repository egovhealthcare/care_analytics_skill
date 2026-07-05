# emr_observation (Observation)

app: emr | source: care/emr/models/observation.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(255)
- `is_group` boolean default=False
- `category` jsonb default=dict
- `main_code` jsonb default=dict
- `alternate_coding` jsonb default=list
- `subject_type` string(255)
- `subject_id` uuid
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `effective_datetime` datetime NULL
- `data_entered_by` foreign_key -> users_user [col: data_entered_by_id] NULL
- `performer` jsonb default=dict
- `value_type` string(255)
- `value` jsonb
- `note` string
- `body_site` jsonb default=dict
- `method` jsonb default=dict
- `reference_range` jsonb default=list
- `interpretation_old` string(255) NULL
- `interpretation` jsonb default=dict
- `parent` uuid NULL
- `questionnaire_response` foreign_key -> emr_questionnaireresponse [col: questionnaire_response_id] NULL
- `component` jsonb default=list
- `diagnostic_report` foreign_key -> emr_diagnosticreport [col: diagnostic_report_id] NULL
- `observation_definition` foreign_key -> emr_observationdefinition [col: observation_definition_id] NULL

JSONB shapes (`history`, `meta`, `category`, `main_code`, `alternate_coding`, `performer`, `value`, `body_site`, `method`, `reference_range`, `interpretation`, `component`): `jsonb/emr_observation.md`
