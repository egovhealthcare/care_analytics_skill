# emr_patientidentifierconfig (PatientIdentifierConfig)

app: emr | source: care/emr/models/patient.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(255)
- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `config` jsonb NULL default=dict

JSONB shapes (`history`, `meta`, `config`): `jsonb/emr_patientidentifierconfig.md`
