# emr_invoice (Invoice)

app: emr | source: care/emr/models/invoice.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `account` foreign_key -> emr_account [col: account_id]
- `title` string(1024) NULL
- `status` string(100)
- `cancelled_reason` string NULL
- `payment_terms` string NULL
- `note` string NULL
- `charge_items` array<integer> default=list
- `charge_items_copy` jsonb default=list
- `total_price_components` jsonb default=dict
- `total_net` decimal default=0
- `total_gross` decimal default=0
- `issue_date` datetime NULL
- `number` string(1000) NULL
- `locked` boolean default=False
- `lock_history` jsonb default=list
- `is_refund` boolean default=False

JSONB shapes (`history`, `meta`, `charge_items_copy`, `total_price_components`, `lock_history`): `jsonb/emr_invoice.md`
