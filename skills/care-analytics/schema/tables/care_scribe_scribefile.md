# care_scribe_scribefile (ScribeFile)

app: care_scribe | source: app/care_scribe/care_scribe/models/scribe_file.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(2000)
- `internal_name` string(2000)
- `associating_id` string(100)
- `file_type` integer choices=FileType.choices default=FileType.SCRIBE_AUDIO
- `mime_type` string(200) NULL
- `signed_url` string(2000) NULL
- `upload_completed` boolean default=False
- `uploaded_by` foreign_key -> users_user [col: uploaded_by_id] NULL
- `meta` jsonb default=dict

JSONB shapes (`meta`): `jsonb/care_scribe_scribefile.md`
