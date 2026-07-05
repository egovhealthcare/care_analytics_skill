# nhcx_insuranceplan (InsurancePlan)

app: nhcx | source: app/care_nhcx/nhcx/models/insurance_plan.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `request` foreign_key -> nhcx_task [col: request_id]
- `fhir_id` string(64) NULL UNIQUE
- `identifier_system` string(255)
- `identifier_value` string(128) idx
- `additional_identifiers` jsonb NULL default=list
- `status` string(16) idx choices=PublicationStatus.choices default=PublicationStatus.ACTIVE
- `type` jsonb default=dict
- `type_code` string(64) NULL idx
- `name` string(512) idx
- `alias` jsonb NULL default=list
- `period_start` date NULL
- `period_end` date NULL
- `owned_by` jsonb default=dict
- `administered_by` jsonb NULL default=dict
- `contact` jsonb NULL default=list
- `source_system` string(128) NULL idx
- `raw_bundle_id` string(128) NULL

JSONB shapes (`history`, `meta`, `additional_identifiers`, `type`, `alias`, `owned_by`, `administered_by`, `contact`): `jsonb/nhcx_insuranceplan.md`

## Model meta

```json
{
 "indexes": "[models.Index(fields=['identifier_value', 'source_system']), models.Index(fields=['status', 'period_start', 'period_end'])]"
}
```
