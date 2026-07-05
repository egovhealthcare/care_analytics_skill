# emr_questionnairefacilityorganization (QuestionnaireFacilityOrganization)

app: emr | source: care/emr/models/questionnaire.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `questionnaire` foreign_key -> emr_questionnaire [col: questionnaire_id]
- `organization` foreign_key -> emr_facilityorganization [col: organization_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_questionnairefacilityorganization.md`
