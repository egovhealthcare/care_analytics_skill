# emr_healthcareservice (HealthcareService)

app: emr | source: care/emr/models/healthcare_service.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `styling_metadata` jsonb NULL
- `name` string(1024)
- `service_type` jsonb default=dict
- `internal_type` string(255) NULL
- `locations` array<integer> default=list
- `extra_details` string
- `managing_organization` foreign_key -> emr_facilityorganization [col: managing_organization_id] NULL

JSONB shapes (`history`, `meta`, `styling_metadata`, `service_type`): `jsonb/emr_healthcareservice.md`
