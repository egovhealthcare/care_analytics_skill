# emr_metaartifact JSONB schemas

## history

```json
{
 "candidate_schemas": [],
 "default_shape": {
  "type": "object"
 },
 "inferred_schema": {
  "type": "object"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "default_shape_only"
}
```

## meta

```json
{
 "candidate_schemas": [
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/meta_artifact/spec.py",
   "spec": "care.emr.resources.meta_artifact.spec.MetaArtifactBaseSpec"
  },
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/meta_artifact/spec.py",
   "spec": "care.emr.resources.meta_artifact.spec.MetaArtifactCreateSpec"
  },
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/meta_artifact/spec.py",
   "spec": "care.emr.resources.meta_artifact.spec.MetaArtifactReadSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## object_value

```json
{
 "candidate_schemas": [
  {
   "annotation": "dict | list",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "any_of": [
     {
      "raw": "dict",
      "type": "object"
     },
     {
      "raw": "list",
      "type": "array"
     }
    ],
    "raw": "dict | list",
    "type": "union"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/meta_artifact/spec.py",
   "spec": "care.emr.resources.meta_artifact.spec.MetaArtifactBaseSpec"
  },
  {
   "annotation": "dict | list",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "any_of": [
     {
      "raw": "dict",
      "type": "object"
     },
     {
      "raw": "list",
      "type": "array"
     }
    ],
    "raw": "dict | list",
    "type": "union"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/meta_artifact/spec.py",
   "spec": "care.emr.resources.meta_artifact.spec.MetaArtifactCreateSpec"
  },
  {
   "annotation": "dict | list",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "any_of": [
     {
      "raw": "dict",
      "type": "object"
     },
     {
      "raw": "list",
      "type": "array"
     }
    ],
    "raw": "dict | list",
    "type": "union"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/meta_artifact/spec.py",
   "spec": "care.emr.resources.meta_artifact.spec.MetaArtifactReadSpec"
  }
 ],
 "default_shape": {
  "nullable": true,
  "type": "unknown"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
