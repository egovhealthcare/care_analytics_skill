# emr_supplyrequest (SupplyRequest)

app: emr | source: care/emr/models/supply_request.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(255)
- `quantity` decimal NULL
- `supplied_item_condition` string(255)
- `item` foreign_key -> emr_productknowledge [col: item_id]
- `order` foreign_key -> emr_requestorder [col: order_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_supplyrequest.md`
