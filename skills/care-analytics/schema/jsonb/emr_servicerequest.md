# emr_servicerequest JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseServiceRequestSpec, ServiceRequestCreateSpec, ServiceRequestReadSpec, ServiceRequestRetrieveSpec +2

## code

- Coding (valueset-bound), required — BaseServiceRequestSpec, ServiceRequestCreateSpec, ServiceRequestReadSpec, ServiceRequestRetrieveSpec +1
- Coding? (valueset-bound), optional — ServiceRequestUpdateSpec

## body_site

- Coding? (valueset-bound), optional — BaseServiceRequestSpec, ServiceRequestCreateSpec, ServiceRequestReadSpec, ServiceRequestRetrieveSpec +2

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
