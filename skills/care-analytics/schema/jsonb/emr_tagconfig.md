# emr_tagconfig JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — TagConfigBaseSpec, TagConfigReadSpec, TagConfigRetrieveSpec, TagConfigUpdateSpec +1

## cached_parent_json

- shape unknown — no spec declares this field (check serializers; default is dict)

## metadata

- TagConfigMetadata?, optional — TagConfigBaseSpec, TagConfigReadSpec, TagConfigRetrieveSpec, TagConfigUpdateSpec +1

## definitions

- `TagConfigMetadata`: {color: str?, icon: str?}
