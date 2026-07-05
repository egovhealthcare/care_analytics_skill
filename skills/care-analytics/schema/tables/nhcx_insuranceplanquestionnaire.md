# nhcx_insuranceplanquestionnaire (InsurancePlanQuestionnaire)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `insurance_plan` foreign_key -> nhcx_insuranceplan [col: insurance_plan_id]
- `fhir_id` string(64) NULL
- `full_url` string(512) NULL idx
- `url` string(512) NULL
- `title` string(512)
- `status` string(16) choices=PublicationStatus.choices default=PublicationStatus.ACTIVE
- `subject_type` jsonb NULL default=list
- `purpose` string(64) NULL idx
- `items` jsonb NULL default=list

JSONB shapes (`history`, `meta`, `subject_type`, `items`): `jsonb/nhcx_insuranceplanquestionnaire.md`

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['insurance_plan', 'fhir_id'], name='uniq_ip_questionnaire_fhir_id')]"
}
```
