# users_user (User)

app: users | source: care/users/models.py
bases: AbstractUser (inherited columns: `_base_models.md`)

## Columns

- `external_id` uuid UNIQUE default=uuid.uuid4
- `username` string(150) UNIQUE
- `user_type` string(100) NULL
- `created_by` foreign_key -> users_user [col: created_by_id] NULL
- `geo_organization` foreign_key -> emr_organization [col: geo_organization_id] NULL
- `phone_number` string(14)
- `alt_phone_number` string(14) NULL
- `video_connect_link` string NULL
- `old_gender` integer NULL choices=[1|2|3]
- `gender` string(100) NULL
- `date_of_birth` date NULL
- `profile_picture_url` string(500) NULL
- `skills` many_to_many -> users_skill (through UserSkill)
- `home_facility` foreign_key -> facility_facility [col: home_facility_id] NULL
- `weekly_working_hours` integer NULL
- `qualification` string NULL
- `doctor_experience_commenced_on` date NULL
- `doctor_medical_council_registration` string(255) NULL
- `prefix` string(10) NULL
- `suffix` string(50) NULL
- `is_service_account` boolean default=False
- `verified` boolean default=False
- `deleted` boolean default=False
- `pf_endpoint` string NULL
- `pf_p256dh` string NULL
- `pf_auth` string NULL
- `totp_secret` string NULL
- `mfa_settings` jsonb default=dict
- `preferences` jsonb default=dict
- `cached_role_orgs` jsonb NULL

JSONB shapes (`mfa_settings`, `preferences`, `cached_role_orgs`): `jsonb/users_user.md`
