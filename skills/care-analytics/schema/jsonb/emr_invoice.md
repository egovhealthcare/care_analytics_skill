# emr_invoice JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseInvoiceSpec, InvoiceReadSpec, InvoiceRetrieveSpec, InvoiceWriteSpec

## charge_items_copy

- shape unknown — no spec declares this field (check serializers; default is list[?])

## total_price_components

- list[dict], required — InvoiceRetrieveSpec

## lock_history

- list[dict], required — InvoiceRetrieveSpec
