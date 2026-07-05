# emr_medicationrequest (MedicationRequest)

app: emr | source: care/emr/models/medication_request.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(100) NULL
- `status_reason` string(100) NULL
- `intent` string(100) NULL
- `category` string(100) NULL
- `priority` string(100) NULL
- `do_not_perform` boolean
- `method` jsonb NULL default=dict
- `medication` jsonb NULL default=dict
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `dosage_instruction` jsonb NULL default=list
- `note` string NULL
- `authored_on` datetime NULL default=timezone.now
- `requester` foreign_key -> users_user [col: requester_id] NULL
- `requested_product` foreign_key -> emr_productknowledge [col: requested_product_id] NULL
- `dispense_status` string(100) NULL
- `prescription` foreign_key -> emr_medicationrequestprescription [col: prescription_id] NULL

JSONB shapes (`history`, `meta`, `method`, `medication`, `dosage_instruction`): `jsonb/emr_medicationrequest.md`
