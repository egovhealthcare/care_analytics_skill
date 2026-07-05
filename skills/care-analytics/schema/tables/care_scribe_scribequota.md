# care_scribe_scribequota (ScribeQuota)

app: care_scribe | source: app/care_scribe/care_scribe/models/scribe_quota.py
bases: BaseModel (inherited columns: `_base_models.md`)

## Columns

- `created_by` foreign_key -> users_user [col: created_by_id] NULL
- `user` foreign_key -> users_user [col: user_id] NULL
- `facility` foreign_key -> facility_facility [col: facility_id] NULL
- `tokens` integer default=0
- `tokens_per_user` integer default=0
- `used` integer default=0
- `allow_ocr` boolean default=False
- `tnc_hash` string(255) NULL
- `tnc_accepted_date` datetime NULL

## Model meta

```json
{
 "verbose_name": "Scribe Quota",
 "verbose_name_plural": "Scribe Quotas"
}
```
