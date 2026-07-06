# emr_metaartifact JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — MetaArtifactBaseSpec, MetaArtifactCreateSpec, MetaArtifactReadSpec, MetaArtifactUpdateSpec

## object_value

- dict | list[?], required — MetaArtifactBaseSpec, MetaArtifactCreateSpec, MetaArtifactReadSpec, MetaArtifactUpdateSpec
