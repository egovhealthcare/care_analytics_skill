# nhcx_insuranceplancoveragebenefitlimit (InsurancePlanCoverageBenefitLimit)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `benefit` foreign_key -> nhcx_insuranceplancoveragebenefit [col: benefit_id]
- `fhir_element_id` string(64) NULL
- `value_amount` decimal NULL
- `value_unit` string(32) NULL
- `value_system` string(255) NULL
- `value_code` string(64) NULL
- `code` jsonb NULL

JSONB shapes (`history`, `meta`, `code`): `jsonb/nhcx_insuranceplancoveragebenefitlimit.md`
