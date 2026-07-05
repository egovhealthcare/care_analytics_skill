# emr_tokenslot (TokenSlot)

app: emr | source: care/emr/models/scheduling/booking.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `resource` foreign_key -> emr_schedulableresource [col: resource_id]
- `availability` foreign_key -> emr_availability [col: availability_id] NULL
- `start_datetime` datetime
- `end_datetime` datetime
- `allocated` integer default=0

JSONB shapes (`history`, `meta`): `jsonb/emr_tokenslot.md`
