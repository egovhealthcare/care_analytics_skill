# emr_specimen JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseSpecimenSpec, SpecimenCreateSpec, SpecimenReadSpec, SpecimenRetrieveSpec +1

## specimen_type

- Coding (valueset-bound), required — BaseSpecimenSpec, SpecimenCreateSpec, SpecimenReadSpec, SpecimenRetrieveSpec
- Coding? (valueset-bound), optional — SpecimenUpdateSpec

## condition

- list[Coding], optional — BaseSpecimenSpec, SpecimenCreateSpec, SpecimenReadSpec, SpecimenRetrieveSpec +1

## processing

- list[ProcessingSpec], optional — BaseSpecimenSpec, SpecimenCreateSpec, SpecimenReadSpec, SpecimenRetrieveSpec +1

## collection

- CollectionSpec?, optional — BaseSpecimenSpec, SpecimenCreateSpec, SpecimenReadSpec, SpecimenRetrieveSpec +1

## definitions

- `CollectionSpec`: {collector: uuid?, collected_date_time: datetime?, quantity: QuantitySpec?, method: Coding?, procedure: uuid?, body_site: Coding?, fasting_status_codeable_concept: Coding?, fasting_status_duration: DurationSpec?}
- `DurationSpec`: {value: int, unit: Coding}
- `ProcessingSpec`: {description: str, method: Coding?, performer: uuid?, time_date_time: str}
- `QuantitySpec`: {value: decimal, unit: Coding}
- unresolved refs: Coding
