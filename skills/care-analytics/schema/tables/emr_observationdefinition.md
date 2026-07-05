# emr_observationdefinition (ObservationDefinition)

app: emr | source: care/emr/models/observation_definition.py
bases: SlugBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `version` integer default=1
- `slug` string(255)
- `title` string(1024)
- `status` string(255)
- `description` string
- `derived_from_uri` string
- `category` string(255) NULL
- `code` jsonb
- `permitted_data_type` string(100)
- `body_site` jsonb NULL
- `method` jsonb NULL
- `permitted_unit` jsonb NULL
- `component` jsonb NULL
- `qualified_ranges` jsonb NULL default=list

JSONB shapes (`history`, `meta`, `code`, `body_site`, `method`, `permitted_unit`, `component`, `qualified_ranges`): `jsonb/emr_observationdefinition.md`
