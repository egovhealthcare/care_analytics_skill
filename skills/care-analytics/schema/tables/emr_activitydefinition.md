# emr_activitydefinition (ActivityDefinition)

app: emr | source: care/emr/models/activity_definition.py
bases: SlugBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `version` integer default=1
- `slug` string(255)
- `title` string(1024)
- `classification` string(100)
- `derived_from_uri` string NULL
- `status` string(255)
- `description` string
- `usage` string
- `kind` string(100)
- `code` jsonb NULL
- `body_site` jsonb NULL
- `specimen_requirements` array<integer> default=list
- `observation_result_requirements` array<integer> default=list
- `locations` array<integer> default=list
- `latest` boolean default=True
- `charge_item_definitions` array<integer> default=list
- `diagnostic_report_codes` jsonb NULL
- `healthcare_service` foreign_key -> emr_healthcareservice [col: healthcare_service_id] NULL
- `tags` array<integer> default=list
- `category` foreign_key -> emr_resourcecategory [col: category_id] NULL

JSONB shapes (`history`, `meta`, `code`, `body_site`, `diagnostic_report_codes`): `jsonb/emr_activitydefinition.md`
