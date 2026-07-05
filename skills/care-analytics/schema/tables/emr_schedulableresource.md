# emr_schedulableresource (SchedulableResource)

app: emr | source: care/emr/models/scheduling/schedule.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `resource_type` string(255) default=practitioner
- `user` foreign_key -> users_user [col: user_id] NULL
- `location` foreign_key -> emr_facilitylocation [col: location_id] NULL
- `healthcare_service` foreign_key -> emr_healthcareservice [col: healthcare_service_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_schedulableresource.md`

## Model meta

```json
{
 "constraints": "[models.UniqueConstraint(fields=['facility', 'resource_type', 'user'], name='unique_facility_resource_user'), models.UniqueConstraint(fields=['facility', 'resource_type', 'location'], name='unique_facility_resource_location'), models.UniqueConstraint(fields=['facility', 'resource_type', 'healthcare_service'], name='unique_facility_resource_healthcare_service')]"
}
```
