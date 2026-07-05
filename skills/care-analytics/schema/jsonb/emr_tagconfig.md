# emr_tagconfig JSONB schemas

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
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigBaseSpec"
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
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigReadSpec"
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
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigRetrieveSpec"
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
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigUpdateSpec"
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
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigWriteSpec"
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

## cached_parent_json

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

## metadata

```json
{
 "candidate_schemas": [
  {
   "annotation": "TagConfigMetadata | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TagConfigMetadata | None",
    "ref": "TagConfigMetadata",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigBaseSpec"
  },
  {
   "annotation": "TagConfigMetadata | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TagConfigMetadata | None",
    "ref": "TagConfigMetadata",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigReadSpec"
  },
  {
   "annotation": "TagConfigMetadata | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TagConfigMetadata | None",
    "ref": "TagConfigMetadata",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigRetrieveSpec"
  },
  {
   "annotation": "TagConfigMetadata | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TagConfigMetadata | None",
    "ref": "TagConfigMetadata",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigUpdateSpec"
  },
  {
   "annotation": "TagConfigMetadata | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "TagConfigMetadata | None",
    "ref": "TagConfigMetadata",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigWriteSpec"
  }
 ],
 "default_shape": {
  "nullable": true,
  "type": "unknown"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "color",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "icon",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "TagConfigMetadata",
   "source_file": "care/emr/resources/tag/config_spec.py",
   "spec": "care.emr.resources.tag.config_spec.TagConfigMetadata"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
