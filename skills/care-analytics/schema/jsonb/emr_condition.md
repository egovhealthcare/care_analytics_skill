# emr_condition JSONB schemas

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
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.BaseConditionSpec"
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
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ChronicConditionUpdateSpec"
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
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionReadSpec"
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
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionSpec"
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
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionUpdateSpec"
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

## code

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ChronicConditionUpdateSpec"
  },
  {
   "annotation": "Coding",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "Coding",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_CODITION_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "system",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "version",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "code",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "display",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "Coding",
   "source_file": "care/emr/resources/common/coding.py",
   "spec": "care.emr.resources.common.coding.Coding"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## body_site

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

## onset

```json
{
 "candidate_schemas": [
  {
   "annotation": "ConditionOnSetSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionOnSetSpec",
    "ref": "ConditionOnSetSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ChronicConditionUpdateSpec"
  },
  {
   "annotation": "ConditionOnSetSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionOnSetSpec",
    "ref": "ConditionOnSetSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionReadSpec"
  },
  {
   "annotation": "ConditionOnSetSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionOnSetSpec",
    "ref": "ConditionOnSetSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionSpec"
  },
  {
   "annotation": "ConditionOnSetSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionOnSetSpec",
    "ref": "ConditionOnSetSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionUpdateSpec"
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
     "annotation": "datetime.datetime | None",
     "name": "onset_datetime",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    },
    {
     "annotation": "int | None",
     "name": "onset_age",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "int | None",
      "type": "integer"
     }
    },
    {
     "annotation": "str | None",
     "name": "onset_string",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "note",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ConditionOnSetSpec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionOnSetSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## abatement

```json
{
 "candidate_schemas": [
  {
   "annotation": "ConditionAbatementSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionAbatementSpec",
    "ref": "ConditionAbatementSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ChronicConditionUpdateSpec"
  },
  {
   "annotation": "ConditionAbatementSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionAbatementSpec",
    "ref": "ConditionAbatementSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionReadSpec"
  },
  {
   "annotation": "ConditionAbatementSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionAbatementSpec",
    "ref": "ConditionAbatementSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionSpec"
  },
  {
   "annotation": "ConditionAbatementSpec",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "ConditionAbatementSpec",
    "ref": "ConditionAbatementSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionUpdateSpec"
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
     "annotation": "datetime.datetime | None",
     "name": "abatement_datetime",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    },
    {
     "annotation": "int | None",
     "name": "abatement_age",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "int | None",
      "type": "integer"
     }
    },
    {
     "annotation": "str | None",
     "name": "abatement_string",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "note",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ConditionAbatementSpec",
   "source_file": "care/emr/resources/condition/spec.py",
   "spec": "care.emr.resources.condition.spec.ConditionAbatementSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
