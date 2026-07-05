# nhcx_insuranceplanplanspecificcostbenefitcost (InsurancePlanPlanSpecificCostBenefitCost)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `benefit` foreign_key -> nhcx_insuranceplanplanspecificcostbenefit [col: benefit_id]
- `fhir_element_id` string(64) NULL
- `type` jsonb default=dict
- `type_code` string(64) NULL idx
- `applicability` jsonb NULL
- `value_amount` decimal NULL
- `value_unit` string(32) NULL

JSONB shapes (`history`, `meta`, `type`, `applicability`): `jsonb/nhcx_insuranceplanplanspecificcostbenefitcost.md`
