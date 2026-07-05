# emr_valueset JSONB schemas

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
   "source_file": "care/emr/resources/valueset/spec.py",
   "spec": "care.emr.resources.valueset.spec.ValueSetBaseSpec"
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
   "source_file": "care/emr/resources/valueset/spec.py",
   "spec": "care.emr.resources.valueset.spec.ValueSetReadSpec"
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

## compose

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetCompose",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetCompose",
    "ref": "ValueSetCompose",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/valueset/spec.py",
   "spec": "care.emr.resources.valueset.spec.ValueSetBaseSpec"
  },
  {
   "annotation": "ValueSetCompose",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetCompose",
    "ref": "ValueSetCompose",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/valueset/spec.py",
   "spec": "care.emr.resources.valueset.spec.ValueSetReadSpec"
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
     "name": "id",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[ValueSetInclude]",
     "name": "include",
     "required": true,
     "schema": {
      "items": {
       "raw": "ValueSetInclude",
       "ref": "ValueSetInclude",
       "type": "ref"
      },
      "raw": "list[ValueSetInclude]",
      "type": "array"
     }
    },
    {
     "annotation": "list[ValueSetInclude] | None",
     "name": "exclude",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetInclude",
       "ref": "ValueSetInclude",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[ValueSetInclude] | None",
      "type": "array"
     }
    },
    {
     "annotation": "list[str] | None",
     "name": "property",
     "required": false,
     "schema": {
      "items": {
       "raw": "str",
       "type": "string"
      },
      "nullable": true,
      "raw": "list[str] | None",
      "type": "array"
     }
    }
   ],
   "name": "ValueSetCompose",
   "source_file": "care/emr/resources/common/valueset.py",
   "spec": "care.emr.resources.common.valueset.ValueSetCompose"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "id",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
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
     "annotation": "list[ValueSetConcept] | None",
     "name": "concept",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetConcept",
       "ref": "ValueSetConcept",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[ValueSetConcept] | None",
      "type": "array"
     }
    },
    {
     "annotation": "list[ValueSetFilter] | None",
     "name": "filter",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetFilter",
       "ref": "ValueSetFilter",
       "type": "ref"
      },
      "nullable": true,
      "raw": "list[ValueSetFilter] | None",
      "type": "array"
     }
    }
   ],
   "name": "ValueSetInclude",
   "source_file": "care/emr/resources/common/valueset.py",
   "spec": "care.emr.resources.common.valueset.ValueSetInclude"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "id",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
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
   "name": "ValueSetConcept",
   "source_file": "care/emr/resources/common/valueset.py",
   "spec": "care.emr.resources.common.valueset.ValueSetConcept"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "id",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "property",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "op",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ValueSetFilter",
   "source_file": "care/emr/resources/common/valueset.py",
   "spec": "care.emr.resources.common.valueset.ValueSetFilter"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```
