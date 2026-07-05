# nhcx_paymentreconciliation JSONB schemas

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
   "source_file": "app/care_nhcx/nhcx/specs/payment.py",
   "spec": "nhcx.specs.payment.PaymentReconciliationRetrieveSpec"
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
   "annotation": "dict | None",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "nullable": true,
    "raw": "dict | None",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/payment.py",
   "spec": "nhcx.specs.payment.PaymentReconciliationRetrieveSpec"
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

## payment_amount

```json
{
 "candidate_schemas": [
  {
   "annotation": "float",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "float",
    "type": "number"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/payment.py",
   "spec": "nhcx.specs.payment.PaymentReconciliationRetrieveSpec"
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

## payment_identifier

```json
{
 "candidate_schemas": [
  {
   "annotation": "str | None",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "nullable": true,
    "raw": "str | None",
    "type": "string"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/payment.py",
   "spec": "nhcx.specs.payment.PaymentReconciliationRetrieveSpec"
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

## detail

```json
{
 "candidate_schemas": [
  {
   "annotation": "list | None",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "nullable": true,
    "raw": "list | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/payment.py",
   "spec": "nhcx.specs.payment.PaymentReconciliationRetrieveSpec"
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

## process_note

```json
{
 "candidate_schemas": [
  {
   "annotation": "list | None",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "nullable": true,
    "raw": "list | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/payment.py",
   "spec": "nhcx.specs.payment.PaymentReconciliationRetrieveSpec"
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
