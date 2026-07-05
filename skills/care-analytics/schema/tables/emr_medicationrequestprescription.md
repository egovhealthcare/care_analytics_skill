# emr_medicationrequestprescription (MedicationRequestPrescription)

app: emr | source: care/emr/models/medication_request.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `name` string(100) NULL
- `note` string NULL
- `prescribed_by` foreign_key -> users_user [col: prescribed_by_id] NULL
- `status` string(100) NULL
- `approval_status` string(100) NULL
- `alternate_identifier` string(100) NULL
- `tags` array<integer> default=list

JSONB shapes (`history`, `meta`): `jsonb/emr_medicationrequestprescription.md`

## Model meta

```json
{
 "constraints": "[UniqueConstraint(fields=['alternate_identifier', 'encounter'], name='unique_alternate_identifier_encounter')]"
}
```
