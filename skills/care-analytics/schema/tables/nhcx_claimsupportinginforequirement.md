# nhcx_claimsupportinginforequirement (ClaimSupportingInfoRequirement)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: ClaimExtensionBase (inherited columns: `_base_models.md`)

## Columns

- `category` jsonb NULL
- `category_code` string(64) NULL idx
- `code` jsonb NULL
- `code_code` string(64) NULL idx
- `documentation_url` string(512) NULL

JSONB shapes (`history`, `meta`, `category`, `code`): `jsonb/nhcx_claimsupportinginforequirement.md`

## Model meta

```json
{
 "abstract": false,
 "indexes": "[*ClaimExtensionBase.Meta.indexes, models.Index(fields=['code_code', 'level'])]"
}
```
