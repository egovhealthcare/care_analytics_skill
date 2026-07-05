# emr_servicerequest (ServiceRequest)

app: emr | source: care/emr/models/service_request.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `title` string(1024)
- `category` string(255)
- `status` string(255)
- `intent` string(255)
- `priority` string(255)
- `do_not_perform` boolean default=False
- `note` string NULL
- `occurance` datetime NULL
- `patient_instruction` string NULL
- `code` jsonb NULL
- `body_site` jsonb NULL
- `locations` array<integer> default=list
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `healthcare_service` foreign_key -> emr_healthcareservice [col: healthcare_service_id] NULL
- `activity_definition` foreign_key -> emr_activitydefinition [col: activity_definition_id] NULL
- `requester` foreign_key -> users_user [col: requester_id] NULL
- `tags` array<integer> default=list

JSONB shapes (`history`, `meta`, `code`, `body_site`): `jsonb/emr_servicerequest.md`
