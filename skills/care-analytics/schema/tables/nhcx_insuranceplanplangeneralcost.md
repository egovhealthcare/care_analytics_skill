# nhcx_insuranceplanplangeneralcost (InsurancePlanPlanGeneralCost)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `plan` foreign_key -> nhcx_insuranceplanplan [col: plan_id]
- `fhir_element_id` string(64) NULL
- `type` jsonb NULL
- `group_size` integer NULL
- `cost_value` decimal NULL
- `cost_currency` string(8) default=INR
- `comment` string NULL

JSONB shapes (`history`, `meta`, `type`): `jsonb/nhcx_insuranceplanplangeneralcost.md`
