# emr_patientidentifier (PatientIdentifier)

app: emr | source: care/emr/models/patient.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `patient` foreign_key -> emr_patient [col: patient_id]
- `config` foreign_key -> emr_patientidentifierconfig [col: config_id]
- `value` string(1024) idx

JSONB shapes (`history`, `meta`): `jsonb/emr_patientidentifier.md`
