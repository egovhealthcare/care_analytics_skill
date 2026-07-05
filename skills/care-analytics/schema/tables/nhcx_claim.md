# nhcx_claim (Claim)

app: nhcx | source: app/care_nhcx/nhcx/models/claim.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `use` string(100)
- `status` string(100)
- `priority` string(100)
- `type` jsonb
- `provider` foreign_key -> nhcx_provider [col: provider_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `insurer` jsonb default=dict
- `billable_period` jsonb NULL
- `related` jsonb NULL default=list
- `care_team` jsonb NULL default=list
- `supporting_info` jsonb NULL default=list
- `procedure` jsonb NULL default=list
- `diagnosis` jsonb default=list
- `insurance` jsonb default=list
- `item` jsonb default=list
- `accident` jsonb NULL
- `payee` jsonb NULL
- `questionnaire_responses` jsonb NULL default=list
- `dispatched_at` datetime NULL
- `dispatch_error` string
- `dispatch_status` string(16) idx choices=DispatchStatusChoices.choices default=DispatchStatusChoices.PENDING

JSONB shapes (`history`, `meta`, `type`, `insurer`, `billable_period`, `related`, `care_team`, `supporting_info`, `procedure`, `diagnosis`, `insurance`, `item`, `accident`, `payee`, `questionnaire_responses`): `jsonb/nhcx_claim.md`
