# emr_consent JSONB schemas

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
   "source_file": "care/emr/resources/consent/spec.py",
   "spec": "care.emr.resources.consent.spec.ConsentBaseSpec"
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
   "source_file": "care/emr/resources/consent/spec.py",
   "spec": "care.emr.resources.consent.spec.ConsentListSpec"
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
   "source_file": "care/emr/resources/consent/spec.py",
   "spec": "care.emr.resources.consent.spec.ConsentUpdateSpec"
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

## period

```json
{
 "candidate_schemas": [
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/consent/spec.py",
   "spec": "care.emr.resources.consent.spec.ConsentBaseSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/consent/spec.py",
   "spec": "care.emr.resources.consent.spec.ConsentListSpec"
  },
  {
   "annotation": "PeriodSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "PeriodSpec | None",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/consent/spec.py",
   "spec": "care.emr.resources.consent.spec.ConsentUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "datetime.datetime | None",
     "name": "start",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    },
    {
     "annotation": "datetime.datetime | None",
     "name": "end",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    }
   ],
   "name": "PeriodSpec",
   "source_file": "care/emr/resources/base.py",
   "spec": "care.emr.resources.base.PeriodSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## verification_details

```json
{
 "candidate_schemas": [
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
   "source_file": "care/emr/resources/consent/spec.py",
   "spec": "care.emr.resources.consent.spec.ConsentListSpec"
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
