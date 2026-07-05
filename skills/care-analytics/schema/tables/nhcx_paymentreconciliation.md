# nhcx_paymentreconciliation (PaymentReconciliation)

app: nhcx | source: app/care_nhcx/nhcx/models/payment.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `identifier` string(100)
- `status` string(100)
- `period` jsonb NULL default=dict
- `outcome` string(100) NULL
- `disposition` string NULL
- `payment_date` datetime
- `payment_amount` jsonb default=dict
- `payment_identifier` jsonb NULL
- `detail` jsonb NULL default=list
- `process_note` jsonb NULL default=list
- `request` foreign_key -> nhcx_task [col: request_id]
- `claim` foreign_key -> nhcx_claim [col: claim_id]

JSONB shapes (`history`, `meta`, `period`, `payment_amount`, `payment_identifier`, `detail`, `process_note`): `jsonb/nhcx_paymentreconciliation.md`
