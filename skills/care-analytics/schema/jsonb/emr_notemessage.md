# emr_notemessage JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — NoteMessageCreateSpec, NoteMessageReadSpec, NoteMessageSpec, NoteMessageUpdateSpec

## message_history

- dict, required — NoteMessageReadSpec
