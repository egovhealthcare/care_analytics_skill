# emr_notethread (NoteThread)

app: emr | source: care/emr/models/notes.py
bases: EMRBaseModel (inherited columns: `_base_models.md`)

## Columns

- `title` string(255) NULL
- `patient` foreign_key -> emr_patient [col: patient_id]
- `encounter` foreign_key -> emr_encounter [col: encounter_id] NULL

JSONB shapes (`history`, `meta`): `jsonb/emr_notethread.md`
