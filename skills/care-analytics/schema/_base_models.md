# Inherited Base Columns

Every table's `bases:` line names its ancestry; those columns are defined once here instead of repeated per table. JSONB shapes for inherited columns (`meta`, `history`) are table-specific — see `jsonb/<db_table>.md`.

## django.db.models.Model

- `id` integer PK

## care.utils.models.base.BaseModel

- `external_id` uuid UNIQUE default=uuid4
- `created_date` datetime NULL idx
- `modified_date` datetime NULL idx
- `deleted` boolean idx default=False

## care.emr.models.base.EMRBaseModel

- `history` jsonb default=dict
- `meta` jsonb default=dict
- `created_by` foreign_key -> users_user [col: created_by_id] NULL
- `updated_by` foreign_key -> users_user [col: updated_by_id] NULL

## care.emr.models.organization.OrganizationCommonBase

- `active` boolean default=True
- `root_org` foreign_key -> care.emr.models.organization.OrganizationCommonBase [col: root_org_id] NULL
- `org_type` string(255)
- `name` string(255)
- `has_children` boolean default=False
- `description` string NULL
- `system_generated` boolean default=False
- `parent` foreign_key -> care.emr.models.organization.OrganizationCommonBase [col: parent_id] NULL
- `level_cache` integer default=0
- `parent_cache` array<integer> default=list
- `metadata` jsonb default=dict
- `cached_parent_json` jsonb default=dict

## care.utils.models.base.BaseFlag

- `flag` string(1024)
