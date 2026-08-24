# facility_mobileotp (MobileOTP)

app: facility | source: care/facility/models/patient.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `is_used` boolean default=False
- `phone_number` string(14)
- `otp` string(10)
- `failed_attempts` integer default=0

## Model meta

```json
{
 "indexes": "[models.Index(fields=['phone_number', '-created_date'], name='pmo_phone_created_active_idx', condition=Q(deleted=False)), models.Index(fields=['phone_number', '-modified_date'], name='pmo_phone_modified_active_idx', condition=Q(deleted=False))]"
}
```
