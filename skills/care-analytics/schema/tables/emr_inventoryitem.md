# emr_inventoryitem (InventoryItem)

app: emr | source: care/emr/models/inventory_item.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `location` foreign_key -> emr_facilitylocation [col: location_id]
- `product` foreign_key -> emr_product [col: product_id]
- `status` string(255)
- `net_content` decimal default=Decimal(0)

JSONB shapes (`history`, `meta`): `jsonb/emr_inventoryitem.md`
