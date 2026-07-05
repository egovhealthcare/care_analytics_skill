# emr_patient (Patient)

app: emr | source: care/emr/models/patient.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(200)
- `gender` string(35)
- `phone_number` string(14)
- `emergency_phone_number` string(14)
- `address` string
- `permanent_address` string
- `pincode` integer NULL default=0
- `date_of_birth` date NULL
- `year_of_birth` integer NULL
- `deceased_datetime` datetime NULL
- `blood_group` string(16)
- `geo_organization` foreign_key -> emr_organization [col: geo_organization_id] NULL
- `organization_cache` array<integer> default=list
- `users_cache` array<integer> default=list
- `instance_identifiers` jsonb NULL default=list
- `facility_identifiers` jsonb NULL default=dict
- `instance_tags` array<integer> default=list
- `facility_tags` jsonb NULL default=dict
- `extensions` jsonb default=dict

JSONB shapes (`history`, `meta`, `instance_identifiers`, `facility_identifiers`, `facility_tags`, `extensions`): `jsonb/emr_patient.md`
