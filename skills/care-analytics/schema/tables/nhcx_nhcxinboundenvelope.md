# nhcx_nhcxinboundenvelope (NHCXInboundEnvelope)

app: nhcx | source: app/care_nhcx/nhcx/models/inbound_envelope.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `correlation_id` string(128) NULL idx
- `api_call_id` string(128) NULL idx
- `callback_type` string(64) idx choices=[coverageeligibility_on_check|predetermination_on_submit|preauth_on_submit|claim_on_submit|communication_request|paymentnotice_request|insuranceplan_on_request|task_on_submit|error_response]
- `recipient_code` string(128) NULL
- `raw_payload` string
- `headers` jsonb default=dict
- `status` string(16) idx choices=[pending|processing|completed|failed] default=EnvelopeStatusChoices.PENDING
- `attempts` integer default=0
- `error_message` string
- `processed_at` datetime NULL

JSONB shapes (`history`, `meta`, `headers`): `jsonb/nhcx_nhcxinboundenvelope.md`

## Model meta

```json
{
 "indexes": "[models.Index(fields=['callback_type', 'correlation_id']), models.Index(fields=['status', 'callback_type'])]"
}
```
