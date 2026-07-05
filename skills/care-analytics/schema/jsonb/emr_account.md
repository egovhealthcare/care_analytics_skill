# emr_account JSONB schemas

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
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountCreateSpec"
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
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountMinimalReadSpec"
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
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountReadSpec"
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
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountRetrieveSpec"
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
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountSpec"
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
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountUpdateSpec"
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

## service_period

```json
{
 "candidate_schemas": [
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountCreateSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountMinimalReadSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountReadSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountRetrieveSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountSpec"
  },
  {
   "annotation": "PeriodSpec",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "PeriodSpec",
    "ref": "PeriodSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountUpdateSpec"
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

## cached_items

```json
{
 "candidate_schemas": [
  {
   "annotation": "list",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "raw": "list",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountRetrieveSpec"
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

## total_price_components

```json
{
 "candidate_schemas": [
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountRetrieveSpec"
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

## extensions

```json
{
 "candidate_schemas": [
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/account/spec.py",
   "spec": "care.emr.resources.account.spec.AccountRetrieveSpec"
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
