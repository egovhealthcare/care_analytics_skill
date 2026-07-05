# emr_patientuser (PatientUser)

app: emr | source: care/emr/models/patient.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `user` foreign_key -> users_user [col: user_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `role` foreign_key -> security_rolemodel [col: role_id]

JSONB shapes (`history`, `meta`): `jsonb/emr_patientuser.md`
