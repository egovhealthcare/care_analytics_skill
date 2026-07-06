# emr_chargeitem JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — ChargeItemReadSpec, ChargeItemSpec, ChargeItemUpdateSpec, ChargeItemWriteSpec

## code

- Coding?, optional — ChargeItemReadSpec, ChargeItemSpec, ChargeItemUpdateSpec, ChargeItemWriteSpec

## unit_price_components

- list[MonetaryComponent], required — ChargeItemReadSpec, ChargeItemSpec, ChargeItemUpdateSpec, ChargeItemWriteSpec

## total_price_components

- list[dict], required — ChargeItemReadSpec

## override_reason

- ChargeItemOverrideReason?, optional — ChargeItemReadSpec, ChargeItemSpec, ChargeItemUpdateSpec, ChargeItemWriteSpec

## discount_configuration

- dict?, optional — ChargeItemReadSpec

## definitions

- `ChargeItemOverrideReason`: {text: str, code: Coding?}
- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `EvaluatorConditionSpec`: {metric: str, operation: str, value: dict | str}
- `MonetaryComponent`: {monetary_component_type: MonetaryComponentType, code: Coding?, factor: decimal?, amount: decimal?, tax_included_amount: decimal?, global_component: bool, conditions: list[EvaluatorConditionSpec]}
- `MonetaryComponentType`: 'base' | 'surcharge' | 'discount' | 'tax' | 'informational'
