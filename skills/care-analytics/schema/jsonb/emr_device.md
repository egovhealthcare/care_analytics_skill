# emr_device JSONB schemas

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
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceCreateSpec"
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
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceListSpec"
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
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceRetrieveSpec"
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
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceSpecBase"
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
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceUpdateSpec"
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

## contact

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ContactPoint]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ContactPoint",
     "ref": "ContactPoint",
     "type": "ref"
    },
    "raw": "list[ContactPoint]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceCreateSpec"
  },
  {
   "annotation": "list[ContactPoint]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ContactPoint",
     "ref": "ContactPoint",
     "type": "ref"
    },
    "raw": "list[ContactPoint]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceListSpec"
  },
  {
   "annotation": "list[ContactPoint]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ContactPoint",
     "ref": "ContactPoint",
     "type": "ref"
    },
    "raw": "list[ContactPoint]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceRetrieveSpec"
  },
  {
   "annotation": "list[ContactPoint]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ContactPoint",
     "ref": "ContactPoint",
     "type": "ref"
    },
    "raw": "list[ContactPoint]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceSpecBase"
  },
  {
   "annotation": "list[ContactPoint]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ContactPoint",
     "ref": "ContactPoint",
     "type": "ref"
    },
    "raw": "list[ContactPoint]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/device/spec.py",
   "spec": "care.emr.resources.device.spec.DeviceUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "ContactPointSystemChoices",
     "name": "system",
     "required": true,
     "schema": {
      "raw": "ContactPointSystemChoices",
      "ref": "ContactPointSystemChoices",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "value",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "ContactPointUseChoices",
     "name": "use",
     "required": true,
     "schema": {
      "raw": "ContactPointUseChoices",
      "ref": "ContactPointUseChoices",
      "type": "ref"
     }
    }
   ],
   "name": "ContactPoint",
   "source_file": "care/emr/resources/common/contact_point.py",
   "spec": "care.emr.resources.common.contact_point.ContactPoint"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "ContactPointSystemChoices",
  "ContactPointUseChoices"
 ]
}
```

## metadata

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
