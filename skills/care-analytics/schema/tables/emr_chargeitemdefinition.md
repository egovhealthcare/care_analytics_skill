# emr_chargeitemdefinition (ChargeItemDefinition)

app: emr | source: care/emr/models/charge_item_definition.py
bases: SlugBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `version` integer default=1
- `status` string(255)
- `title` string(255)
- `slug` string(255)
- `derived_from_uri` string NULL
- `description` string NULL
- `purpose` string NULL
- `price_components` jsonb default=list
- `tags` array<integer> default=list
- `can_edit_charge_item` boolean default=True
- `category` foreign_key -> emr_resourcecategory [col: category_id] NULL
- `discount_configuration` jsonb NULL

JSONB shapes (`history`, `meta`, `price_components`, `discount_configuration`): `jsonb/emr_chargeitemdefinition.md`
