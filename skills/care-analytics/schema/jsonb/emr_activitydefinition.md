# emr_activitydefinition JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — ActivityDefinitionReadSpec, ActivityDefinitionRetrieveSpec, ActivityDefinitionWriteSpec, BaseActivityDefinitionSpec

## code

- Coding (valueset-bound), required — ActivityDefinitionReadSpec, ActivityDefinitionRetrieveSpec, ActivityDefinitionWriteSpec, BaseActivityDefinitionSpec

## body_site

- Coding? (valueset-bound), optional — ActivityDefinitionReadSpec, ActivityDefinitionRetrieveSpec, ActivityDefinitionWriteSpec, BaseActivityDefinitionSpec

## diagnostic_report_codes

- list[Coding], optional — ActivityDefinitionReadSpec, ActivityDefinitionRetrieveSpec, ActivityDefinitionWriteSpec, BaseActivityDefinitionSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
