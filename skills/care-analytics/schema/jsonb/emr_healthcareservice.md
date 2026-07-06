# emr_healthcareservice JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseHealthcareServiceSpec, HealthcareServiceReadSpec, HealthcareServiceRetrieveSpec, HealthcareServiceWriteSpec

## styling_metadata

- dict, optional — BaseHealthcareServiceSpec, HealthcareServiceReadSpec, HealthcareServiceRetrieveSpec, HealthcareServiceWriteSpec

## service_type

- Coding? (valueset-bound), optional — BaseHealthcareServiceSpec, HealthcareServiceReadSpec, HealthcareServiceRetrieveSpec, HealthcareServiceWriteSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
