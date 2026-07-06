# emr_allergyintolerance JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — AllergyIntoleranceReadSpec, AllergyIntoleranceUpdateSpec, AllergyIntoleranceWriteSpec, BaseAllergyIntoleranceSpec

## code

- Coding, required — AllergyIntoleranceReadSpec
- Coding (valueset-bound), required — AllergyIntoleranceWriteSpec

## onset

- AllergyIntoleranceOnSetSpec, optional — AllergyIntoleranceReadSpec, AllergyIntoleranceWriteSpec

## definitions

- `AllergyIntoleranceOnSetSpec`: {meta: dict, onset_datetime: datetime, onset_age: int, onset_string: str, note: str}
- `Coding`: {system: str?, version: str?, code: str, display: str?}
