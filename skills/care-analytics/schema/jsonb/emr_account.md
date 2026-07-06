# emr_account JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — AccountCreateSpec, AccountMinimalReadSpec, AccountReadSpec, AccountRetrieveSpec +2

## service_period

- PeriodSpec, required — AccountCreateSpec, AccountMinimalReadSpec, AccountReadSpec, AccountRetrieveSpec +2

## cached_items

- list[?], optional — AccountRetrieveSpec

## total_price_components

- dict, required — AccountRetrieveSpec

## extensions

- dict, required — AccountRetrieveSpec

## definitions

- `PeriodSpec`: {start: datetime?, end: datetime?}
