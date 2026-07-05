# emr_availability JSONB schemas

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
   "source_file": "care/emr/resources/scheduling/schedule/spec.py",
   "spec": "care.emr.resources.scheduling.schedule.spec.AvailabilityBaseSpec"
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
   "source_file": "care/emr/resources/scheduling/schedule/spec.py",
   "spec": "care.emr.resources.scheduling.schedule.spec.AvailabilityCreateSpec"
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
   "source_file": "care/emr/resources/scheduling/schedule/spec.py",
   "spec": "care.emr.resources.scheduling.schedule.spec.AvailabilityForScheduleSpec"
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

## availability

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[AvailabilityDateTimeSpec]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "AvailabilityDateTimeSpec",
     "ref": "AvailabilityDateTimeSpec",
     "type": "ref"
    },
    "raw": "list[AvailabilityDateTimeSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/scheduling/schedule/spec.py",
   "spec": "care.emr.resources.scheduling.schedule.spec.AvailabilityCreateSpec"
  },
  {
   "annotation": "list[AvailabilityDateTimeSpec]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "AvailabilityDateTimeSpec",
     "ref": "AvailabilityDateTimeSpec",
     "type": "ref"
    },
    "raw": "list[AvailabilityDateTimeSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/scheduling/schedule/spec.py",
   "spec": "care.emr.resources.scheduling.schedule.spec.AvailabilityForScheduleSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "dict",
     "name": "meta",
     "required": false,
     "schema": {
      "raw": "dict",
      "type": "object"
     }
    },
    {
     "annotation": "int",
     "name": "day_of_week",
     "required": false,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "datetime.time",
     "name": "start_time",
     "required": true,
     "schema": {
      "raw": "datetime.time",
      "ref": "datetime.time",
      "type": "ref"
     }
    },
    {
     "annotation": "datetime.time",
     "name": "end_time",
     "required": true,
     "schema": {
      "raw": "datetime.time",
      "ref": "datetime.time",
      "type": "ref"
     }
    }
   ],
   "name": "AvailabilityDateTimeSpec",
   "source_file": "care/emr/resources/scheduling/schedule/spec.py",
   "spec": "care.emr.resources.scheduling.schedule.spec.AvailabilityDateTimeSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "datetime.time"
 ]
}
```
