# emr_facilitylocation (FacilityLocation)

app: emr | source: care/emr/models/location.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(255)
- `operational_status` string(255)
- `system_availability_status` string(255)
- `name` string(255)
- `description` string(255)
- `mode` string(255)
- `location_type` jsonb NULL default=dict
- `form` string(255)
- `facility_organization_cache` array<integer> default=list
- `facility` foreign_key -> facility_facility [col: facility_id]
- `parent` foreign_key -> emr_facilitylocation [col: parent_id] NULL
- `has_children` boolean default=False
- `level_cache` integer default=0
- `parent_cache` array<integer> default=list
- `metadata` jsonb default=dict
- `cached_parent_json` jsonb default=dict
- `root_location` foreign_key -> emr_facilitylocation [col: root_location_id] NULL
- `current_encounter` foreign_key -> emr_encounter [col: current_encounter_id] NULL
- `sort_index` integer default=0

JSONB shapes (`history`, `meta`, `location_type`, `metadata`, `cached_parent_json`): `jsonb/emr_facilitylocation.md`
