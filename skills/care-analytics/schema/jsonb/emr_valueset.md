# emr_valueset JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — ValueSetBaseSpec, ValueSetReadSpec, ValueSetSpec

## compose

- ValueSetCompose, required — ValueSetBaseSpec, ValueSetReadSpec, ValueSetSpec

## definitions

- `ValueSetCompose`: {id: str?, include: list[ValueSetInclude], exclude: list[ValueSetInclude]?, property: list[str]?}
- `ValueSetConcept`: {id: str?, code: str?, display: str?}
- `ValueSetFilter`: {id: str?, property: str?, op: str?, value: str?}
- `ValueSetInclude`: {id: str?, system: str?, version: str?, concept: list[ValueSetConcept]?, filter: list[ValueSetFilter]?}
