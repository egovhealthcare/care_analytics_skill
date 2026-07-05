# nhcx_insuranceplancoveragebenefit (InsurancePlanCoverageBenefit)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `coverage` foreign_key -> nhcx_insuranceplancoverage [col: coverage_id]
- `fhir_element_id` string(64) NULL
- `type` jsonb default=dict
- `type_code` string(64) NULL idx
- `type_display` string(255) idx
- `requirement` string NULL

JSONB shapes (`history`, `meta`, `type`): `jsonb/nhcx_insuranceplancoveragebenefit.md`
