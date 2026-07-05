# emr_dispenseorder (DispenseOrder)

app: emr | source: care/emr/models/medication_dispense.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(255) NULL
- `status` string(255)
- `note` string NULL
- `location` foreign_key -> emr_facilitylocation [col: location_id]
- `tags` array<integer> default=list
- `patient` foreign_key -> emr_patient [col: patient_id]
- `facility` foreign_key -> facility_facility [col: facility_id]
- `alternate_identifier` string(100) NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_dispenseorder.md`

## Model meta

```json
{
 "constraints": "[UniqueConstraint(fields=['alternate_identifier', 'patient', 'location'], name='unique_alternate_identifier_encounter_location')]"
}
```
