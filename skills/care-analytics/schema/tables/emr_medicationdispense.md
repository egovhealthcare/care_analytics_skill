# emr_medicationdispense (MedicationDispense)

app: emr | source: care/emr/models/medication_dispense.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(100)
- `not_performed_reason` string(100) NULL
- `category` string(100) NULL
- `when_prepared` datetime NULL
- `when_handed_over` datetime NULL
- `note` string NULL
- `dosage_instruction` jsonb NULL default=list
- `substitution` jsonb NULL default=dict
- `encounter` foreign_key -> emr_encounter [col: encounter_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `location` foreign_key -> emr_facilitylocation [col: location_id]
- `authorizing_request` foreign_key -> emr_medicationrequest [col: authorizing_request_id] NULL
- `item` foreign_key -> emr_inventoryitem [col: item_id]
- `charge_item` foreign_key -> emr_chargeitem [col: charge_item_id] NULL
- `quantity` decimal
- `days_supply` decimal NULL
- `order` foreign_key -> emr_dispenseorder [col: order_id] NULL

JSONB shapes (`history`, `meta`, `dosage_instruction`, `substitution`): `jsonb/emr_medicationdispense.md`
