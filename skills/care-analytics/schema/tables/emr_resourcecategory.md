# emr_resourcecategory (ResourceCategory)

app: emr | source: care/emr/models/resource_category.py
bases: SlugBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `resource_type` string(255)
- `resource_sub_type` string(255)
- `title` string(255)
- `slug` string(255)
- `description` string NULL
- `parent` foreign_key -> emr_resourcecategory [col: parent_id] NULL
- `is_child` boolean default=False
- `cached_parent_json` jsonb default=dict
- `parent_cache` array<integer> default=list
- `level_cache` integer default=0
- `root_org` foreign_key -> emr_resourcecategory [col: root_org_id] NULL
- `has_children` boolean default=False
- `configured_monetary_components` jsonb default=list
- `calculated_monetary_components` jsonb default=list

JSONB shapes (`history`, `meta`, `cached_parent_json`, `configured_monetary_components`, `calculated_monetary_components`): `jsonb/emr_resourcecategory.md`

## Model meta

```json
{
 "indexes": "[models.Index(fields=['slug', 'facility'])]"
}
```
