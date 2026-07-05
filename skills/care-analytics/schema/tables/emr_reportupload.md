# emr_reportupload (ReportUpload)

app: emr | source: care/emr/models/report/report_upload.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `template` foreign_key -> emr_template [col: template_id]
- `name` string(2000)
- `internal_name` string(2000)
- `associating_id` string(100)
- `upload_completed` boolean default=False
- `report_type` string(50)
- `is_archived` boolean default=False
- `archive_reason` string
- `archived_datetime` datetime NULL
- `archived_by` foreign_key -> users_user [col: archived_by_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_reportupload.md`
