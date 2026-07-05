# emr_supplydelivery (SupplyDelivery)

app: emr | source: care/emr/models/supply_delivery.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(255)
- `supplied_item_pack_quantity` integer NULL
- `supplied_item_pack_size` integer NULL
- `supplied_item_quantity` decimal NULL
- `supplied_item` foreign_key -> emr_product [col: supplied_item_id] NULL
- `supplied_inventory_item` foreign_key -> emr_inventoryitem [col: supplied_inventory_item_id] NULL
- `supplied_item_condition` string(255)
- `delivery_type` string(255)
- `supply_request` foreign_key -> emr_supplyrequest [col: supply_request_id] NULL
- `order` foreign_key -> emr_deliveryorder [col: order_id] NULL
- `extensions` jsonb default=dict
- `total_purchase_price` decimal NULL

JSONB shapes (`history`, `meta`, `extensions`): `jsonb/emr_supplydelivery.md`
