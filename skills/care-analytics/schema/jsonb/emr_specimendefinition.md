# emr_specimendefinition JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseSpecimenDefinitionSpec, SpecimenDefinitionReadSpec, SpecimenDefinitionWriteSpec

## type_collected

- Coding (valueset-bound), required — BaseSpecimenDefinitionSpec, SpecimenDefinitionReadSpec, SpecimenDefinitionWriteSpec

## patient_preparation

- list[Coding], optional — BaseSpecimenDefinitionSpec, SpecimenDefinitionReadSpec, SpecimenDefinitionWriteSpec

## collection

- Coding? (valueset-bound), optional — BaseSpecimenDefinitionSpec, SpecimenDefinitionReadSpec, SpecimenDefinitionWriteSpec

## type_tested

- TypeTestedSpec?, optional — BaseSpecimenDefinitionSpec, SpecimenDefinitionReadSpec, SpecimenDefinitionWriteSpec

## definitions

- `ContainerSpec`: {description: str?, capacity: QuantitySpec?, minimum_volume: MinimumVolumeSpec?, cap: Coding?, preparation: str?}
- `DurationSpec`: {value: decimal, unit: Coding}
- `HandlingSpec`: {temperature_qualifier: HandlingConditionOptions?, temperature_range: RangeSpec?, max_duration: DurationSpec?, instruction: str?}
- `MinimumVolumeSpec`: {quantity: QuantitySpec?, string: str?}
- `QuantitySpec`: {value: decimal, unit: Coding}
- `RangeSpec`: {low: QuantitySpec?, high: QuantitySpec?}
- `TypeTestedSpec`: {is_derived: bool, preference: PreferenceOptions, container: ContainerSpec?, requirement: str?, retention_time: DurationSpec?, single_use: bool?, handling: HandlingSpec?}
- `HandlingConditionOptions`: 'room' | 'refrigerated' | 'frozen'
- `PreferenceOptions`: 'preferred' | 'alternate'
- unresolved refs: Coding
