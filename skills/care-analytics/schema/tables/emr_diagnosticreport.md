# emr_diagnosticreport (DiagnosticReport)

app: emr | source: care/emr/models/diagnostic_report.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `status` string(255)
- `category` jsonb NULL
- `code` jsonb NULL
- `note` string NULL
- `conclusion` string NULL
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `service_request` foreign_key -> emr_servicerequest [col: service_request_id]

JSONB shapes (`history`, `meta`, `category`, `code`): `jsonb/emr_diagnosticreport.md`
