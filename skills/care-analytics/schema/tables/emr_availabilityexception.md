# emr_availabilityexception (AvailabilityException)

app: emr | source: care/emr/models/scheduling/schedule.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `resource` foreign_key -> emr_schedulableresource [col: resource_id]
- `name` string(255)
- `reason` string NULL
- `valid_from` date
- `valid_to` date
- `start_time` time
- `end_time` time

JSONB shapes (`history`, `meta`): `jsonb/emr_availabilityexception.md`
