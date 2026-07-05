# emr_patientorganization (PatientOrganization)

app: emr | source: care/emr/models/patient.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `patient` foreign_key -> emr_patient [col: patient_id]
- `organization` foreign_key -> emr_organization [col: organization_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_patientorganization.md`
