# nhcx_task (Task)

app: nhcx | source: app/care_nhcx/nhcx/models/task.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `identifier` string(100) NULL
- `status` string(100)
- `intent` string(100)
- `priority` string(100) NULL
- `code` jsonb NULL
- `authored_on` datetime NULL
- `description` string NULL
- `reason_code` jsonb NULL
- `input` jsonb NULL default=list
- `output` jsonb NULL default=list
- `part_of` foreign_key -> nhcx_task [col: part_of_id] NULL
- `claim` foreign_key -> nhcx_claim [col: claim_id] NULL
- `use_case` string(32) choices=[communication_request|communication_response|payment_notice_request|payment_notice_response|reprocess_request|reprocess_response|cancel_request|cancel_response|search_request|search_response|insurance_plan_request]
- `focus_type` foreign_key -> ContentType [col: focus_type_id] NULL
- `focus_id` integer NULL
- `focus` generic_foreign_key -> ?
- `dispatched_at` datetime NULL
- `dispatch_error` string
- `dispatch_status` string(16) idx choices=[pending|awaiting|partial|complete|error] default=DispatchStatusChoices.PENDING

JSONB shapes (`history`, `meta`, `code`, `reason_code`, `input`, `output`): `jsonb/nhcx_task.md`
