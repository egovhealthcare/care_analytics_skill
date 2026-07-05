# abdm_transaction (Transaction)

app: abdm | source: app/care_abdm/abdm/models/transaction.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `reference_id` string(100)
- `type` integer choices=[1|2|3|4|5|6]
- `status` integer choices=[1|2|3|4] default=TransactionStatus.COMPLETED
- `meta_data` jsonb NULL
- `created_by` foreign_key -> users_user [col: created_by_id] NULL

JSONB shapes (`meta_data`): `jsonb/abdm_transaction.md`
