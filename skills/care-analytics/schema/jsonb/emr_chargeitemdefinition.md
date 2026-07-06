# emr_chargeitemdefinition JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — ChargeItemDefinitionReadSpec, ChargeItemDefinitionSpec, ChargeItemDefinitionWriteSpec

## price_components

- list[MonetaryComponent], required — ChargeItemDefinitionReadSpec, ChargeItemDefinitionSpec, ChargeItemDefinitionWriteSpec

## discount_configuration

- DiscountConfiguration?, required — ChargeItemDefinitionReadSpec, ChargeItemDefinitionSpec, ChargeItemDefinitionWriteSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `DiscountConfiguration`: {max_applicable: int, applicability_order: DiscountApplicability}
- `EvaluatorConditionSpec`: {metric: str, operation: str, value: dict | str}
- `MonetaryComponent`: {monetary_component_type: MonetaryComponentType, code: Coding?, factor: decimal?, amount: decimal?, tax_included_amount: decimal?, global_component: bool, conditions: list[EvaluatorConditionSpec]}
- `DiscountApplicability`: 'total_asc' | 'total_desc'
- `MonetaryComponentType`: 'base' | 'surcharge' | 'discount' | 'tax' | 'informational'
