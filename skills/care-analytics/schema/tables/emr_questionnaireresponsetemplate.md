# emr_questionnaireresponsetemplate (QuestionnaireResponseTemplate)

app: emr | source: care/emr/models/questionnaire.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `name` string(255)
- `description` string
- `template_data` jsonb default=dict
- `questionnaire` foreign_key -> emr_questionnaire [col: questionnaire_id] NULL
- `facility_organizations` array<integer> default=list
- `users` array<integer> default=list
- `available_keys` array<string> default=list

JSONB shapes (`history`, `meta`, `template_data`): `jsonb/emr_questionnaireresponsetemplate.md`
