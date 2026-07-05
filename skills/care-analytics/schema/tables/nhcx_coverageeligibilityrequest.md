# nhcx_coverageeligibilityrequest (CoverageEligibilityRequest)

app: nhcx | source: app/care_nhcx/nhcx/models/coverage_eligibility.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `status` string(100)
- `priority` string(100)
- `purpose` jsonb default=list
- `provider` foreign_key -> nhcx_provider [col: provider_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL
- `insurer` jsonb default=dict
- `supporting_info` jsonb NULL default=list
- `insurance` jsonb default=list
- `item` jsonb NULL default=list
- `dispatched_at` datetime NULL
- `dispatch_error` string
- `dispatch_status` string(16) idx choices=DispatchStatusChoices.choices default=DispatchStatusChoices.PENDING

JSONB shapes (`history`, `meta`, `purpose`, `insurer`, `supporting_info`, `insurance`, `item`): `jsonb/nhcx_coverageeligibilityrequest.md`
