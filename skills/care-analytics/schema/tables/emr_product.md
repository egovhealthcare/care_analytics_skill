# emr_product (Product)

app: emr | source: care/emr/models/product.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `product_knowledge` foreign_key -> emr_productknowledge [col: product_knowledge_id]
- `charge_item_definition` foreign_key -> emr_chargeitemdefinition [col: charge_item_definition_id] NULL
- `status` string(255)
- `product_type` string(255)
- `batch` jsonb NULL default=dict
- `expiration_date` datetime NULL
- `extensions` jsonb default=dict
- `standard_pack_size` integer NULL
- `purchase_price` decimal NULL

JSONB shapes (`history`, `meta`, `batch`, `extensions`): `jsonb/emr_product.md`
