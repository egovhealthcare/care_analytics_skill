# emr_consent JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — ConsentBaseSpec, ConsentCreateSpec, ConsentListSpec, ConsentRetrieveSpec +1

## period

- PeriodSpec, optional — ConsentBaseSpec, ConsentCreateSpec, ConsentListSpec, ConsentRetrieveSpec
- PeriodSpec?, optional — ConsentUpdateSpec

## verification_details

- list[dict], optional — ConsentListSpec, ConsentRetrieveSpec

## definitions

- `PeriodSpec`: {start: datetime?, end: datetime?}
