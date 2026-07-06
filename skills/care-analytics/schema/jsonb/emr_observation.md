# emr_observation JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## category

- Coding?, optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## main_code

- Coding?, optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## alternate_coding

- CodeableConcept?, optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## performer

- Performer?, optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## value

- QuestionnaireSubmitResultValue, required — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec
- QuestionnaireSubmitResultValue?, optional — ObservationUpdateSpec

## body_site

- Coding? (valueset-bound), optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## method

- Coding? (valueset-bound), optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## reference_range

- list[ReferenceRange], optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## interpretation

- dict, optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## component

- list[Component], optional — BaseObservationSpec, ObservationReadSpec, ObservationRetrieveSpec, ObservationSpec +1

## definitions

- `CodeableConcept`: {id: str?, coding: list[Coding]?, text: str?}
- `Component`: {value: QuestionnaireSubmitResultValue, interpretation: str | dict, reference_range: list[ReferenceRange], code: Coding?, note: str}
- `Performer`: {type: PerformerType, id: str}
- `QuestionnaireSubmitResultValue`: {value: str?, unit: Coding?, coding: Coding?}
- `ReferenceRange`: {min: float?, max: float?, unit: str?, interpretation: str, value: str?}
- `PerformerType`: 'related_person' | 'user'
- unresolved refs: Coding
