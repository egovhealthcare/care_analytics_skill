# emr_notemessage (NoteMessage)

app: emr | source: care/emr/models/notes.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `thread` foreign_key -> emr_notethread [col: thread_id]
- `message` string
- `message_history` jsonb default=dict

JSONB shapes (`history`, `meta`, `message_history`): `jsonb/emr_notemessage.md`
