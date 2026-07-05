# emr_encounter (Encounter)

app: emr | source: care/emr/models/encounter.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(100) NULL
- `status_history` jsonb default=dict
- `encounter_class` string(100) NULL
- `encounter_class_history` jsonb default=dict
- `patient` foreign_key -> emr_patient [col: patient_id]
- `period` jsonb default=dict
- `facility` foreign_key -> facility_facility [col: facility_id]
- `appointment` foreign_key -> emr_tokenbooking [col: appointment_id] NULL
- `hospitalization` jsonb default=dict
- `priority` string(100) NULL
- `external_identifier` string(100) NULL
- `care_team` jsonb default=dict
- `care_team_users` array<integer> default=list
- `facility_organization_cache` array<integer> default=list
- `current_location` foreign_key -> emr_facilitylocation [col: current_location_id] NULL
- `discharge_summary_advice` string NULL
- `tags` array<integer> default=list
- `extensions` jsonb default=dict

JSONB shapes (`history`, `meta`, `status_history`, `encounter_class_history`, `period`, `hospitalization`, `care_team`, `extensions`): `jsonb/emr_encounter.md`
