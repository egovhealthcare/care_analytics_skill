# nhcx_insuranceplanbenefit (InsurancePlanBenefit)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `insurance_plan` foreign_key -> nhcx_insuranceplan [col: insurance_plan_id]
- `plan` foreign_key -> nhcx_insuranceplanplan [col: plan_id]
- `coverage` foreign_key -> nhcx_insuranceplancoverage [col: coverage_id]
- `coverage_type_code` string(64) idx
- `coverage_type_display` string(255)
- `type_code` string(64) idx
- `type_display` string(255) idx
- `plan_type_code` string(64) NULL idx
- `plan_type_display` string(255)
- `specialty_category_code` string(64) NULL idx
- `specialty_category_display` string(255)
- `specific_cost_benefit` foreign_key -> nhcx_insuranceplanplanspecificcostbenefit [col: specific_cost_benefit_id] NULL
- `coverage_benefit_fhir_ids` jsonb default=list
- `min_cost` decimal NULL idx
- `max_cost` decimal NULL idx
- `max_limit_amount` decimal NULL idx
- `cost_count` integer default=0
- `qualifier_count` integer default=0
- `authorization_required` boolean idx default=True
- `is_day_care` boolean NULL idx
- `implant_applicable` boolean NULL idx
- `stratification_allowed` boolean NULL idx
- `procedure_type` string(64) NULL idx
- `has_copayment` boolean idx default=False
- `has_deductible` boolean idx default=False
- `has_waiting_period` boolean idx default=False
- `has_stratification_qualifier` boolean idx default=False
- `has_implant_qualifier` boolean idx default=False
- `has_consumable_qualifier` boolean idx default=False
- `has_questionnaire` boolean idx default=False
- `questionnaire_fhir_ids` jsonb default=list
- `requires_supporting_info` boolean idx default=False
- `supporting_info_count` integer default=0
- `condition_count` integer default=0
- `exclusion_count` integer default=0

JSONB shapes (`history`, `meta`, `coverage_benefit_fhir_ids`, `questionnaire_fhir_ids`): `jsonb/nhcx_insuranceplanbenefit.md`

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['insurance_plan', 'plan', 'coverage_type_code', 'type_code'], name='uniq_ipb_per_plan')]",
 "indexes": "[models.Index(fields=['insurance_plan', 'plan', 'type_display']), models.Index(fields=['insurance_plan', 'plan_type_code']), models.Index(fields=['insurance_plan', 'coverage_type_code', 'type_code'])]"
}
```
