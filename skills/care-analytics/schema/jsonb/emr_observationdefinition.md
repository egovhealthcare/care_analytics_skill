# emr_observationdefinition JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseObservationDefinitionSpec, ObservationDefinitionCreateSpec, ObservationDefinitionReadSpec, ObservationDefinitionUpdateSpec

## code

- Coding (valueset-bound), required — BaseObservationDefinitionSpec, ObservationDefinitionCreateSpec, ObservationDefinitionReadSpec, ObservationDefinitionUpdateSpec

## body_site

- Coding? (valueset-bound), optional — BaseObservationDefinitionSpec, ObservationDefinitionCreateSpec, ObservationDefinitionReadSpec, ObservationDefinitionUpdateSpec

## method

- Coding? (valueset-bound), optional — BaseObservationDefinitionSpec, ObservationDefinitionCreateSpec, ObservationDefinitionReadSpec, ObservationDefinitionUpdateSpec

## permitted_unit

- Coding? (valueset-bound), optional — BaseObservationDefinitionSpec, ObservationDefinitionCreateSpec, ObservationDefinitionReadSpec, ObservationDefinitionUpdateSpec

## component

- list[ObservationDefinitionComponentSpec]?, optional — BaseObservationDefinitionSpec, ObservationDefinitionCreateSpec, ObservationDefinitionReadSpec, ObservationDefinitionUpdateSpec

## qualified_ranges

- list[QualifiedRangeSpec], required — BaseObservationDefinitionSpec, ObservationDefinitionCreateSpec, ObservationDefinitionReadSpec, ObservationDefinitionUpdateSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `EvaluatorConditionSpec`: {metric: str, operation: str, value: dict | str}
- `InterpretationSpec`: {display: str, icon: str?, color: str?, highlight: bool?, code: Coding?}
- `NumericRangeSpec`: {interpretation: InterpretationSpec, min: decimal?, max: decimal?}
- `ObservationDefinitionComponentSpec`: {code: Coding, permitted_data_type: QuestionType, permitted_unit: Coding?, qualified_ranges: list[QualifiedRangeSpec]}
- `QualifiedRangeSpec`: {title: str?, conditions: list[EvaluatorConditionSpec], ranges: list[NumericRangeSpec], default_interpretation: InterpretationSpec?, normal_coded_value_set: str?, critical_coded_value_set: str?, abnormal_coded_value_set: str?, valueset_interpretation: list[ValueSetInterpretationSpec]}
- `ValueSetInterpretationSpec`: {interpretation: InterpretationSpec, valuset: str}
- `QuestionType`: 'group' | 'boolean' | 'decimal' | 'integer' | 'string' | 'text' | 'display' | 'date' | 'dateTime' | 'time' | 'choice' | 'url' | 'quantity' | 'structured'
