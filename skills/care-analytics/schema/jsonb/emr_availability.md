# emr_availability JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — AvailabilityBaseSpec, AvailabilityCreateSpec, AvailabilityForScheduleSpec

## availability

- list[AvailabilityDateTimeSpec], required — AvailabilityCreateSpec, AvailabilityForScheduleSpec

## definitions

- `AvailabilityDateTimeSpec`: {meta: dict, day_of_week: int, start_time: time, end_time: time}
