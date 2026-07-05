# emr_facilitymonetoryconfig (FacilityMonetoryConfig)

app: emr | source: care/emr/models/facility_config.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` one_to_one -> facility_facility [col: facility_id] UNIQUE
- `discount_codes` jsonb default=list
- `discount_monetary_components` jsonb default=list
- `discount_configuration` jsonb NULL default=dict
- `invoice_number_expression` string(1000) NULL

JSONB shapes (`history`, `meta`, `discount_codes`, `discount_monetary_components`, `discount_configuration`): `jsonb/emr_facilitymonetoryconfig.md`
