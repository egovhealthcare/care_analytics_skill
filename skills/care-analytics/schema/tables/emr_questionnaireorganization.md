# emr_questionnaireorganization (QuestionnaireOrganization)

app: emr | source: care/emr/models/questionnaire.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `questionnaire` foreign_key -> emr_questionnaire [col: questionnaire_id]
- `organization` foreign_key -> emr_organization [col: organization_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_questionnaireorganization.md`
