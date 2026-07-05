# facility_mobileotp (MobileOTP)

app: facility | source: care/facility/models/patient.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `is_used` boolean default=False
- `phone_number` string(14)
- `otp` string(10)
