# emr_token (Token)

app: emr | source: care/emr/models/scheduling/token.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `facility` foreign_key -> facility_facility [col: facility_id]
- `patient` foreign_key -> emr_patient [col: patient_id] NULL
- `queue` foreign_key -> emr_tokenqueue [col: queue_id]
- `category` foreign_key -> emr_tokencategory [col: category_id]
- `sub_queue` foreign_key -> emr_tokensubqueue [col: sub_queue_id] NULL
- `number` integer
- `status` string(255)
- `is_next` boolean default=False
- `note` string NULL
- `booking` foreign_key -> emr_tokenbooking [col: booking_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_token.md`
