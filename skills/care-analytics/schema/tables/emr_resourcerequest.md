# emr_resourcerequest (ResourceRequest)

app: emr | source: care/emr/models/resource_request.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `origin_facility` foreign_key -> facility_facility [col: origin_facility_id]
- `approving_facility` foreign_key -> facility_facility [col: approving_facility_id] NULL
- `assigned_facility` foreign_key -> facility_facility [col: assigned_facility_id] NULL
- `emergency` boolean default=False
- `title` string(255)
- `reason` string
- `referring_facility_contact_name` string
- `referring_facility_contact_number` string(14)
- `status` string(100)
- `category` string(100)
- `priority` integer NULL
- `is_assigned_to_user` boolean default=False
- `assigned_to` foreign_key -> users_user [col: assigned_to_id] NULL
- `related_patient` foreign_key -> emr_patient [col: related_patient_id] NULL
- `extensions` jsonb default=dict

JSONB shapes (`history`, `meta`, `extensions`): `jsonb/emr_resourcerequest.md`
