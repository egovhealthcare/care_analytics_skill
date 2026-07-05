# emr_deliveryorder (DeliveryOrder)

app: emr | source: care/emr/models/supply_delivery.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(255)
- `status` string(255)
- `note` string NULL
- `tags` array<integer> default=list
- `supplier` foreign_key -> emr_organization [col: supplier_id] NULL
- `origin` foreign_key -> emr_facilitylocation [col: origin_id] NULL
- `destination` foreign_key -> emr_facilitylocation [col: destination_id]
- `extensions` jsonb default=dict
- `patient` foreign_key -> emr_patient [col: patient_id] NULL
- `patient_invoice` foreign_key -> emr_invoice [col: patient_invoice_id] NULL

JSONB shapes (`history`, `meta`, `extensions`): `jsonb/emr_deliveryorder.md`
