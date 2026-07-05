# emr_paymentreconciliation (PaymentReconciliation)

app: emr | source: care/emr/models/payment_reconciliation.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `target_invoice` foreign_key -> emr_invoice [col: target_invoice_id] NULL
- `account` foreign_key -> emr_account [col: account_id]
- `reconciliation_type` string(100)
- `status` string(100)
- `kind` string(100)
- `issuer_type` string(100)
- `outcome` string(100)
- `disposition` string NULL
- `payment_datetime` datetime NULL
- `method` string(100)
- `reference_number` string(1024) NULL
- `authorization` string(1024) NULL
- `tendered_amount` decimal
- `returned_amount` decimal
- `amount` decimal
- `note` string NULL
- `is_credit_note` boolean default=False
- `location` foreign_key -> emr_facilitylocation [col: location_id] NULL
- `extensions` jsonb default=dict

JSONB shapes (`history`, `meta`, `extensions`): `jsonb/emr_paymentreconciliation.md`
