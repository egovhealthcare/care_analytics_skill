# nhcx_insuranceplanplan (InsurancePlanPlan)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `insurance_plan` foreign_key -> nhcx_insuranceplan [col: insurance_plan_id]
- `fhir_element_id` string(64) NULL
- `identifiers` jsonb NULL default=list
- `type` jsonb NULL default=dict
- `type_code` string(64) NULL idx

JSONB shapes (`history`, `meta`, `identifiers`, `type`): `jsonb/nhcx_insuranceplanplan.md`
