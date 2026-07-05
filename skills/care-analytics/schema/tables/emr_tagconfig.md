# emr_tagconfig (TagConfig)

app: emr | source: care/emr/models/tag_config.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `facility_organization` foreign_key -> emr_facilityorganization [col: facility_organization_id] NULL
- `organization` foreign_key -> emr_organization [col: organization_id] NULL
- `status` string(255)
- `display` string(255)
- `description` string NULL
- `category` string(255)
- `priority` integer default=100
- `level_cache` integer default=0
- `parent_cache` array<integer> default=list
- `cached_parent_json` jsonb default=dict
- `parent` foreign_key -> emr_tagconfig [col: parent_id] NULL
- `has_children` boolean default=False
- `root_tag_config` foreign_key -> emr_tagconfig [col: root_tag_config_id] NULL
- `resource` string(255)
- `metadata` jsonb NULL

JSONB shapes (`history`, `meta`, `cached_parent_json`, `metadata`): `jsonb/emr_tagconfig.md`
