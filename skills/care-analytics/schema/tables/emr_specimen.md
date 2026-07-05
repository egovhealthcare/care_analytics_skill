# emr_specimen (Specimen)

app: emr | source: care/emr/models/specimen.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `accession_identifier` string(255) idx
- `status` string(20)
- `specimen_type` jsonb
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `received_time` datetime NULL
- `note` string NULL
- `condition` jsonb default=list
- `processing` jsonb default=list
- `collection` jsonb default=dict
- `service_request` foreign_key -> emr_servicerequest [col: service_request_id] NULL
- `specimen_definition` foreign_key -> emr_specimendefinition [col: specimen_definition_id] NULL

JSONB shapes (`history`, `meta`, `specimen_type`, `condition`, `processing`, `collection`): `jsonb/emr_specimen.md`
