# nhcx_claimcondition (ClaimCondition)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: ClaimExtensionBase (inherited columns: `_base_models.md`)

## Columns

- `properties` jsonb NULL default=dict
- `procedure_type` string(64) NULL idx
- `govt_reserved` boolean NULL
- `approval_not_required` boolean NULL idx
- `scheduled_tat_approval` boolean NULL
- `enhancement_allowed` boolean NULL
- `quantity_allowed` integer NULL
- `is_day_care` boolean NULL idx
- `implant_applicable` boolean NULL idx
- `multiple_implants_allowed` boolean NULL
- `maximum_implants_allowed` integer NULL
- `stratification_allowed` boolean NULL idx
- `multiple_stratification_allowed` boolean NULL
- `maximum_stratification_allowed` integer NULL
- `cyclic_procedure` boolean NULL
- `maximum_cycles_allowed` integer NULL
- `condition_type` jsonb NULL
- `code` jsonb NULL
- `description` string NULL
- `value` jsonb NULL

JSONB shapes (`history`, `meta`, `properties`, `condition_type`, `code`, `value`): `jsonb/nhcx_claimcondition.md`

## Model meta

```json
{
 "abstract": false,
 "indexes": "[*ClaimExtensionBase.Meta.indexes, models.Index(fields=['level', 'procedure_type'])]"
}
```
