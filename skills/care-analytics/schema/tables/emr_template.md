# emr_template (Template)

app: emr | source: care/emr/models/report/template.py
bases: SlugBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `slug` string(255)
- `name` string(255)
- `status` string(255)
- `template_data` string
- `template_type` string(255)
- `default_format` string(255)
- `context` string(100) default=encounter_base
- `description` string
- `options` jsonb default=dict

JSONB shapes (`history`, `meta`, `options`): `jsonb/emr_template.md`
