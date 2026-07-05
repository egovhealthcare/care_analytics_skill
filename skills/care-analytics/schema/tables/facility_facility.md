# facility_facility (Facility)

app: facility | source: care/facility/models/facility.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(1000)
- `description` string
- `is_active` boolean default=True
- `verified` boolean default=False
- `facility_type` integer choices=[1|2|3|4|5|6|7|9|10|800|802|803|830|840|860|870|900|910|1010|1100|+9 more]
- `features` array<integer> NULL
- `longitude` decimal NULL
- `latitude` decimal NULL
- `pincode` integer NULL
- `address` string
- `geo_organization` foreign_key -> emr_organization [col: geo_organization_id] NULL
- `geo_organization_cache` array<integer> default=list
- `default_internal_organization` foreign_key -> emr_facilityorganization [col: default_internal_organization_id] NULL
- `internal_organization_cache` array<integer> default=list
- `phone_number` string(14)
- `created_by` foreign_key -> users_user [col: created_by_id] NULL
- `cover_image_url` string(500) NULL
- `middleware_address` string(200) NULL
- `is_public` boolean default=False
- `print_templates` jsonb default=list

JSONB shapes (`print_templates`): `jsonb/facility_facility.md`

## Model meta

```json
{
 "verbose_name_plural": "Facilities"
}
```
