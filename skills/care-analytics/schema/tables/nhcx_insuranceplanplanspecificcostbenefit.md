# nhcx_insuranceplanplanspecificcostbenefit (InsurancePlanPlanSpecificCostBenefit)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `specific_cost` foreign_key -> nhcx_insuranceplanplanspecificcost [col: specific_cost_id]
- `fhir_element_id` string(64) NULL
- `type` jsonb default=dict
- `type_code` string(64) NULL idx
- `type_display` string(255) idx

JSONB shapes (`history`, `meta`, `type`): `jsonb/nhcx_insuranceplanplanspecificcostbenefit.md`
