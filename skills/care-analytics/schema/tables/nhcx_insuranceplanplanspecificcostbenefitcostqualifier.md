# nhcx_insuranceplanplanspecificcostbenefitcostqualifier (InsurancePlanPlanSpecificCostBenefitCostQualifier)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `cost` foreign_key -> nhcx_insuranceplanplanspecificcostbenefitcost [col: cost_id]
- `qualifier` jsonb default=dict
- `qualifier_code` string(64) NULL idx
- `qualifier_type` string(32) idx choices=CostQualifierType.choices default=CostQualifierType.OTHER

JSONB shapes (`history`, `meta`, `qualifier`): `jsonb/nhcx_insuranceplanplanspecificcostbenefitcostqualifier.md`

## Model meta

```json
{
 "indexes": "[models.Index(fields=['qualifier_type', 'qualifier_code'])]"
}
```
