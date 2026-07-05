# emr_product JSONB schemas

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
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.BaseProductSpec"
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
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductReadSpec"
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
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductUpdateSpec"
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
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductWriteSpec"
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

## batch

```json
{
 "candidate_schemas": [
  {
   "annotation": "ProductBatch | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductBatch | None",
    "ref": "ProductBatch",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.BaseProductSpec"
  },
  {
   "annotation": "ProductBatch | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductBatch | None",
    "ref": "ProductBatch",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductReadSpec"
  },
  {
   "annotation": "ProductBatch | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductBatch | None",
    "ref": "ProductBatch",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductUpdateSpec"
  },
  {
   "annotation": "ProductBatch | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductBatch | None",
    "ref": "ProductBatch",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductWriteSpec"
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
     "name": "lot_number",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "ProductBatch",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductBatch"
  }
 ],
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
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.BaseProductSpec"
  },
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductReadSpec"
  },
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductUpdateSpec"
  },
  {
   "annotation": "dict",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "dict",
    "type": "object"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product/spec.py",
   "spec": "care.emr.resources.inventory.product.spec.ProductWriteSpec"
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
