# emr_device (Device)

app: emr | source: care/emr/models/device.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `identifier` string(1024) NULL
- `status` string(16)
- `availability_status` string(14)
- `manufacturer` string(1024)
- `manufacture_date` datetime NULL
- `expiration_date` datetime NULL
- `lot_number` string(1024) NULL
- `serial_number` string(1024) NULL
- `registered_name` string(1024) NULL
- `user_friendly_name` string(1024) NULL
- `model_number` string(1024) NULL
- `part_number` string(1024) NULL
- `contact` jsonb default=dict
- `care_type` string(1024) NULL
- `metadata` jsonb default=dict
- `facility` foreign_key -> facility_facility [col: facility_id]
- `managing_organization` foreign_key -> emr_facilityorganization [col: managing_organization_id] NULL
- `current_location` foreign_key -> emr_facilitylocation [col: current_location_id] NULL
- `current_encounter` foreign_key -> emr_encounter [col: current_encounter_id] NULL
- `facility_organization_cache` array<integer> default=list

JSONB shapes (`history`, `meta`, `contact`, `metadata`): `jsonb/emr_device.md`
