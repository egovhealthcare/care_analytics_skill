# care_scribe_scribe (Scribe)

app: care_scribe | source: app/care_scribe/care_scribe/models/scribe.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `requested_by` foreign_key -> users_user [col: requested_by_id] NULL
- `requested_in_facility` foreign_key -> facility_facility [col: requested_in_facility_id] NULL
- `requested_in_encounter` foreign_key -> emr_encounter [col: requested_in_encounter_id] NULL
- `form_data` jsonb NULL
- `transcript` string NULL
- `text` string NULL
- `ai_response` jsonb NULL default=dict
- `status` string(50) choices=[CREATED|READY|GENERATING_TRANSCRIPT|GENERATING_AI_RESPONSE|COMPLETED|REFUSED|FAILED] default=Status.CREATED
- `prompt` string NULL
- `meta` jsonb NULL default=dict
- `chat_model` string(100) NULL
- `audio_model` string(100) NULL
- `chat_model_temperature` number NULL
- `is_feedback_positive` boolean NULL
- `feedback_comments` string NULL
- `chat_input_tokens` integer NULL
- `chat_output_tokens` integer NULL

JSONB shapes (`form_data`, `ai_response`, `meta`): `jsonb/care_scribe_scribe.md`
