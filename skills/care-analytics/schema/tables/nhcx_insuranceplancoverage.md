# nhcx_insuranceplancoverage (InsurancePlanCoverage)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `insurance_plan` foreign_key -> nhcx_insuranceplan [col: insurance_plan_id]
- `fhir_element_id` string(64) NULL
- `type` jsonb default=dict
- `type_code` string(64) NULL idx
- `type_display` string(255)

JSONB shapes (`history`, `meta`, `type`): `jsonb/nhcx_insuranceplancoverage.md`
