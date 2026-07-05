# emr_medicationstatement (MedicationStatement)

app: emr | source: care/emr/models/medication_statement.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(100)
- `reason` string(100) NULL
- `medication` jsonb default=dict
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `effective_period` jsonb default=dict
- `information_source` string(100)
- `dosage_text` string NULL
- `note` string NULL

JSONB shapes (`history`, `meta`, `medication`, `effective_period`): `jsonb/emr_medicationstatement.md`
