# emr_medicationadministration (MedicationAdministration)

app: emr | source: care/emr/models/medication_administration.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(100)
- `status_reason` jsonb NULL
- `category` string(100) NULL
- `medication` jsonb default=dict
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `request` foreign_key -> emr_medicationrequest [col: request_id] NULL
- `authored_on` datetime NULL
- `occurrence_period_start` datetime default=datetime.now
- `occurrence_period_end` datetime NULL
- `recorded` datetime NULL
- `performer` jsonb default=list
- `dosage` jsonb NULL
- `note` string NULL
- `administered_product` foreign_key -> emr_productknowledge [col: administered_product_id] NULL

JSONB shapes (`history`, `meta`, `status_reason`, `medication`, `performer`, `dosage`): `jsonb/emr_medicationadministration.md`
