# emr_availability (Availability)

app: emr | source: care/emr/models/scheduling/schedule.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `schedule` foreign_key -> emr_schedule [col: schedule_id]
- `name` string(255)
- `slot_type` string
- `slot_size_in_minutes` integer NULL
- `tokens_per_slot` integer NULL
- `create_tokens` boolean default=False
- `reason` string NULL
- `availability` jsonb default=dict

JSONB shapes (`history`, `meta`, `availability`): `jsonb/emr_availability.md`
