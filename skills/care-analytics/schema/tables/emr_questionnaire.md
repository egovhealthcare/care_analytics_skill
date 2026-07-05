# emr_questionnaire (Questionnaire)

app: emr | source: care/emr/models/questionnaire.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `version` string(255)
- `slug` string(255) UNIQUE default=uuid.uuid4
- `title` string(255)
- `description` string
- `subject_type` string(255)
- `status` string(255)
- `styling_metadata` jsonb default=dict
- `questions` jsonb default=dict
- `organization_cache` array<integer> default=list
- `internal_organization_cache` array<integer> default=list

JSONB shapes (`history`, `meta`, `styling_metadata`, `questions`): `jsonb/emr_questionnaire.md`
