# nhcx_insuranceplanplanspecificcost (InsurancePlanPlanSpecificCost)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `plan` foreign_key -> nhcx_insuranceplanplan [col: plan_id]
- `fhir_element_id` string(64) NULL
- `category` jsonb default=dict
- `category_code` string(64) NULL idx

JSONB shapes (`history`, `meta`, `category`): `jsonb/nhcx_insuranceplanplanspecificcost.md`
