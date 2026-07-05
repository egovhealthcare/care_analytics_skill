# emr_tokenbooking (TokenBooking)

app: emr | source: care/emr/models/scheduling/booking.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `token_slot` foreign_key -> emr_tokenslot [col: token_slot_id]
- `patient` foreign_key -> emr_patient [col: patient_id]
- `booked_on` datetime
- `booked_by` foreign_key -> users_user [col: booked_by_id] NULL
- `status` string
- `note` string NULL
- `tags` array<integer> default=list
- `associated_encounter` foreign_key -> emr_encounter [col: associated_encounter_id] NULL
- `token` foreign_key -> emr_token [col: token_id] NULL
- `charge_item` foreign_key -> emr_chargeitem [col: charge_item_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_tokenbooking.md`
