# emr_resourcecategory JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — ResourceCategoryBaseSpec, ResourceCategoryReadSpec, ResourceCategoryUpdateSpec, ResourceCategoryWriteSpec

## cached_parent_json

- shape unknown — no spec declares this field (check serializers; default is dict)

## configured_monetary_components

- list[MonetaryComponent]?, optional — ResourceCategoryReadSpec

## calculated_monetary_components

- list[MonetaryComponent]?, optional — ResourceCategoryReadSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `EvaluatorConditionSpec`: {metric: str, operation: str, value: dict | str}
- `MonetaryComponent`: {monetary_component_type: MonetaryComponentType, code: Coding?, factor: decimal?, amount: decimal?, tax_included_amount: decimal?, global_component: bool, conditions: list[EvaluatorConditionSpec]}
- `MonetaryComponentType`: 'base' | 'surcharge' | 'discount' | 'tax' | 'informational'
