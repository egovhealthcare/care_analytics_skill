# Inherited Base Columns

Every table's `bases:` line names its ancestry; those columns are defined once here instead of repeated per table. JSONB shapes for inherited columns (`meta`, `history`) are table-specific — see `jsonb/<db_table>.md`.

## django.db.models.Model

- `id` integer PK

## care.utils.models.base.BaseModel

- `external_id` uuid UNIQUE default=uuid4
- `created_date` datetime NULL idx
- `modified_date` datetime NULL idx
- `deleted` boolean idx default=False

## abdm.models.consent.Consent

- `consent_id` uuid NULL UNIQUE
- `patient_abha` foreign_key -> abdm_abhanumber.health_id [col: patient_abha_id]
- `encounter` foreign_key -> emr_encounter.external_id [col: encounter_id] NULL
- `care_contexts` jsonb default=list
- `status` string(20) choices=Status.choices (see _enums.md) default=Status.REQUESTED.value
- `purpose` string(20) choices=[CAREMGT|BTG|PUBHLTH|HPAYMT|DSRCH|PATRQT] default=Purpose.CARE_MANAGEMENT.value
- `hi_types` array<string> default=list
- `hip` string(50) NULL
- `hiu` string(50) NULL
- `requester` foreign_key -> users_user [col: requester_id] NULL
- `access_mode` string(20) choices=[VIEW|STORE|QUERY|STREAM] default=AccessMode.VIEW.value
- `from_time` datetime NULL default=default_from_time
- `to_time` datetime NULL default=default_to_time
- `expiry` datetime NULL default=default_expiry
- `frequency_unit` string(20) choices=[HOUR|DAY|WEEK|MONTH|YEAR] default=FrequencyUnit.HOUR.value
- `frequency_value` integer default=1
- `frequency_repeats` integer default=0

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

## nhcx.models.insurance_plan.ClaimExtensionBase

- `parent_content_type` foreign_key -> ContentType [col: parent_content_type_id]
- `parent_object_id` integer idx
- `parent` generic_foreign_key -> ?
- `level` string(32) NULL idx choices=[insurance_plan|coverage|coverage_benefit|plan|plan_specific_cost_benefit]
