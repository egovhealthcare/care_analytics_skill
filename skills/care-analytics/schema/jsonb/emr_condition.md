# emr_condition JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseConditionSpec, ChronicConditionUpdateSpec, ConditionReadSpec, ConditionSpec +1

## code

- Coding (valueset-bound), required — ChronicConditionUpdateSpec, ConditionSpec, ConditionUpdateSpec
- Coding, required — ConditionReadSpec

## body_site

- shape unknown — no spec declares this field (check serializers; default is dict)

## onset

- ConditionOnSetSpec, optional — ChronicConditionUpdateSpec, ConditionReadSpec, ConditionSpec, ConditionUpdateSpec

## abatement

- ConditionAbatementSpec, optional — ChronicConditionUpdateSpec, ConditionReadSpec, ConditionSpec, ConditionUpdateSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `ConditionAbatementSpec`: {meta: dict, abatement_datetime: datetime?, abatement_age: int?, abatement_string: str?, note: str?}
- `ConditionOnSetSpec`: {meta: dict, onset_datetime: datetime?, onset_age: int?, onset_string: str?, note: str?}
