# emr_account (Account)

app: emr | source: care/emr/models/account.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `status` string(255)
- `billing_status` string(255)
- `name` string(255)
- `service_period` jsonb default=dict
- `description` string NULL
- `patient` foreign_key -> emr_patient [col: patient_id]
- `cached_items` jsonb default=dict
- `total_net` decimal default=0
- `total_gross` decimal default=0
- `total_paid` decimal default=0
- `total_balance` decimal default=0
- `total_price_components` jsonb default=dict
- `calculated_at` datetime NULL
- `total_billable_charge_items` decimal default=0
- `tags` array<integer> default=list
- `extensions` jsonb default=dict
- `primary_encounter` foreign_key -> emr_encounter [col: primary_encounter_id] NULL

JSONB shapes (`history`, `meta`, `service_period`, `cached_items`, `total_price_components`, `extensions`): `jsonb/emr_account.md`
