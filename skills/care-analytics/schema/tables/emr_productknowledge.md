# emr_productknowledge (ProductKnowledge)

app: emr | source: care/emr/models/product_knowledge.py
bases: SlugBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `slug` string(255)
- `alternate_identifier` string(255) NULL
- `status` string(255)
- `product_type` string(255)
- `code` jsonb NULL default=dict
- `name` string(255)
- `names` jsonb NULL default=list
- `names_cache` string(2048) NULL
- `storage_guidelines` jsonb NULL default=list
- `definitional` jsonb NULL default=dict
- `base_unit` jsonb NULL default=dict
- `category` foreign_key -> emr_resourcecategory [col: category_id] NULL

JSONB shapes (`history`, `meta`, `code`, `names`, `storage_guidelines`, `definitional`, `base_unit`): `jsonb/emr_productknowledge.md`
