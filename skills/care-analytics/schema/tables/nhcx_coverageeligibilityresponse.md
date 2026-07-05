# nhcx_coverageeligibilityresponse (CoverageEligibilityResponse)

app: nhcx | source: app/care_nhcx/nhcx/models/coverage_eligibility.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `request` foreign_key -> nhcx_coverageeligibilityrequest [col: request_id]
- `outcome` string(100)
- `disposition` string NULL
- `insurance` jsonb NULL
- `error` jsonb NULL

JSONB shapes (`history`, `meta`, `insurance`, `error`): `jsonb/nhcx_coverageeligibilityresponse.md`
