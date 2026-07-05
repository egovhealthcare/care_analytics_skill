# emr_invoice JSONB schemas

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
   "source_file": "care/emr/resources/invoice/spec.py",
   "spec": "care.emr.resources.invoice.spec.BaseInvoiceSpec"
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
   "source_file": "care/emr/resources/invoice/spec.py",
   "spec": "care.emr.resources.invoice.spec.InvoiceReadSpec"
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
   "source_file": "care/emr/resources/invoice/spec.py",
   "spec": "care.emr.resources.invoice.spec.InvoiceRetrieveSpec"
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
   "source_file": "care/emr/resources/invoice/spec.py",
   "spec": "care.emr.resources.invoice.spec.InvoiceWriteSpec"
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

## charge_items_copy

```json
{
 "candidate_schemas": [],
 "default_shape": {
  "type": "array"
 },
 "inferred_schema": {
  "type": "array"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "default_shape_only"
}
```

## total_price_components

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "dict",
     "type": "object"
    },
    "raw": "list[dict]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/invoice/spec.py",
   "spec": "care.emr.resources.invoice.spec.InvoiceRetrieveSpec"
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

## lock_history

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[dict]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "dict",
     "type": "object"
    },
    "raw": "list[dict]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/invoice/spec.py",
   "spec": "care.emr.resources.invoice.spec.InvoiceRetrieveSpec"
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
