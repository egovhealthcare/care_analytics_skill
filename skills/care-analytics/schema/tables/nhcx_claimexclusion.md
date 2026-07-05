# nhcx_claimexclusion (ClaimExclusion)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: ClaimExtensionBase (inherited columns: `_base_models.md`)

## Columns

- `category` jsonb NULL
- `category_code` string(64) NULL idx
- `statements` jsonb NULL default=list
- `items` jsonb NULL
- `items_codes` jsonb NULL default=list

JSONB shapes (`history`, `meta`, `category`, `statements`, `items`, `items_codes`): `jsonb/nhcx_claimexclusion.md`

## Model meta

```json
{
 "abstract": false,
 "indexes": "[*ClaimExtensionBase.Meta.indexes, models.Index(fields=['level', 'category_code'])]"
}
```
