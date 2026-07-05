# nhcx_communication JSONB schemas

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
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationBaseSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationCreateSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationListSpec"
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

## category

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ValueSetBoundCoding[NHCX_COMMUNICATION_CATEGORY_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[NHCX_COMMUNICATION_CATEGORY_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[NHCX_COMMUNICATION_CATEGORY_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "dict",
     "type": "object"
    },
    "raw": "list[dict]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## payload

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[CommunicationPayloadSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "CommunicationPayloadSpec",
     "ref": "CommunicationPayloadSpec",
     "type": "ref"
    },
    "raw": "list[CommunicationPayloadSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationCreateSpec"
  },
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "dict",
     "type": "object"
    },
    "raw": "list[dict]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "content_string",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "content_attachment",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    }
   ],
   "name": "CommunicationPayloadSpec",
   "source_file": "app/care_nhcx/nhcx/specs/communication.py",
   "spec": "nhcx.specs.communication.CommunicationPayloadSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
