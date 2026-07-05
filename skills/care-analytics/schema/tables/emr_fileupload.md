# emr_fileupload (FileUpload)

app: emr | source: care/emr/models/file_upload.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `name` string(2000)
- `internal_name` string(2000)
- `associating_id` string(100)
- `file_type` string(100)
- `file_category` string(100)
- `upload_completed` boolean default=False
- `is_archived` boolean default=False
- `archive_reason` string
- `archived_datetime` datetime NULL
- `archived_by` foreign_key -> users_user [col: archived_by_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_fileupload.md`
