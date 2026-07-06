# emr_product JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseProductSpec, ProductReadSpec, ProductUpdateSpec, ProductWriteSpec

## batch

- ProductBatch?, optional — BaseProductSpec, ProductReadSpec, ProductUpdateSpec, ProductWriteSpec

## extensions

- dict, required — BaseProductSpec, ProductReadSpec, ProductUpdateSpec, ProductWriteSpec

## definitions

- `ProductBatch`: {lot_number: str?}
