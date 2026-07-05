# abdm_abhanumber (AbhaNumber)

app: abdm | source: app/care_abdm/abdm/models/abha_number.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `abha_number` string NULL UNIQUE
- `health_id` string NULL UNIQUE
- `patient` one_to_one -> emr_patient [col: patient_id] NULL
- `name` string NULL
- `first_name` string NULL
- `middle_name` string NULL
- `last_name` string NULL
- `gender` string NULL
- `date_of_birth` string NULL
- `address` string NULL
- `district` string NULL
- `state` string NULL
- `pincode` string NULL
- `mobile` string NULL
- `email` string NULL
- `profile_photo` string NULL
- `new` boolean default=False
- `access_token` string NULL
- `refresh_token` string NULL
