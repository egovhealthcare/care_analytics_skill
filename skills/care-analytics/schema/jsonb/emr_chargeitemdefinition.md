# emr_chargeitemdefinition JSONB schemas

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
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionReadSpec"
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
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionSpec"
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
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionWriteSpec"
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

## price_components

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[MonetaryComponent]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "MonetaryComponent",
     "ref": "MonetaryComponent",
     "type": "ref"
    },
    "raw": "list[MonetaryComponent]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionReadSpec"
  },
  {
   "annotation": "list[MonetaryComponent]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "MonetaryComponent",
     "ref": "MonetaryComponent",
     "type": "ref"
    },
    "raw": "list[MonetaryComponent]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionSpec"
  },
  {
   "annotation": "list[MonetaryComponent]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "MonetaryComponent",
     "ref": "MonetaryComponent",
     "type": "ref"
    },
    "raw": "list[MonetaryComponent]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionWriteSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "MonetaryComponentType",
     "name": "monetary_component_type",
     "required": true,
     "schema": {
      "raw": "MonetaryComponentType",
      "ref": "MonetaryComponentType",
      "type": "ref"
     }
    },
    {
     "annotation": "Coding | None",
     "name": "code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Coding | None",
      "ref": "Coding",
      "type": "ref"
     }
    },
    {
     "annotation": "Decimal | None",
     "name": "factor",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Decimal | None",
     "name": "amount",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Decimal | None",
     "name": "tax_included_amount",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "bool",
     "name": "global_component",
     "required": false,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "list[EvaluatorConditionSpec]",
     "name": "conditions",
     "required": false,
     "schema": {
      "items": {
       "raw": "EvaluatorConditionSpec",
       "ref": "EvaluatorConditionSpec",
       "type": "ref"
      },
      "raw": "list[EvaluatorConditionSpec]",
      "type": "array"
     }
    }
   ],
   "name": "MonetaryComponent",
   "source_file": "care/emr/resources/common/monetary_component.py",
   "spec": "care.emr.resources.common.monetary_component.MonetaryComponent"
  },
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
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "metric",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "operation",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "dict | str",
     "name": "value",
     "required": true,
     "schema": {
      "any_of": [
       {
        "raw": "dict",
        "type": "object"
       },
       {
        "raw": "str",
        "type": "string"
       }
      ],
      "raw": "dict | str",
      "type": "union"
     }
    }
   ],
   "name": "EvaluatorConditionSpec",
   "source_file": "care/emr/resources/common/condition_evaluator.py",
   "spec": "care.emr.resources.common.condition_evaluator.EvaluatorConditionSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "Decimal",
  "MonetaryComponentType"
 ]
}
```

## discount_configuration

```json
{
 "candidate_schemas": [
  {
   "annotation": "DiscountConfiguration | None",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "nullable": true,
    "raw": "DiscountConfiguration | None",
    "ref": "DiscountConfiguration",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionReadSpec"
  },
  {
   "annotation": "DiscountConfiguration | None",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "nullable": true,
    "raw": "DiscountConfiguration | None",
    "ref": "DiscountConfiguration",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionSpec"
  },
  {
   "annotation": "DiscountConfiguration | None",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "nullable": true,
    "raw": "DiscountConfiguration | None",
    "ref": "DiscountConfiguration",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/charge_item_definition/spec.py",
   "spec": "care.emr.resources.charge_item_definition.spec.ChargeItemDefinitionWriteSpec"
  }
 ],
 "default_shape": {
  "nullable": true,
  "type": "unknown"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "max_applicable",
     "required": false,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "DiscountApplicability",
     "name": "applicability_order",
     "required": true,
     "schema": {
      "raw": "DiscountApplicability",
      "ref": "DiscountApplicability",
      "type": "ref"
     }
    }
   ],
   "name": "DiscountConfiguration",
   "source_file": "care/emr/resources/common/monetary_component.py",
   "spec": "care.emr.resources.common.monetary_component.DiscountConfiguration"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "DiscountApplicability"
 ]
}
```
