# emr_productknowledge JSONB schemas

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
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.BaseProductKnowledgeSpec"
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
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeReadSpec"
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
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeUpdateSpec"
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
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeWriteSpec"
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
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.BaseProductKnowledgeSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeReadSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeUpdateSpec"
  },
  {
   "annotation": "Coding | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "Coding | None",
    "ref": "Coding",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeWriteSpec"
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

## names

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ProductName] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProductName",
     "ref": "ProductName",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ProductName] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.BaseProductKnowledgeSpec"
  },
  {
   "annotation": "list[ProductName] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProductName",
     "ref": "ProductName",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ProductName] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeReadSpec"
  },
  {
   "annotation": "list[ProductName] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProductName",
     "ref": "ProductName",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ProductName] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeUpdateSpec"
  },
  {
   "annotation": "list[ProductName] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProductName",
     "ref": "ProductName",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[ProductName] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeWriteSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "ProductNameTypes",
     "name": "name_type",
     "required": true,
     "schema": {
      "raw": "ProductNameTypes",
      "ref": "ProductNameTypes",
      "type": "ref"
     }
    },
    {
     "annotation": "str",
     "name": "name",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "ProductName",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductName"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "ProductNameTypes"
 ]
}
```

## storage_guidelines

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[StorageGuideline] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "StorageGuideline",
     "ref": "StorageGuideline",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[StorageGuideline] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.BaseProductKnowledgeSpec"
  },
  {
   "annotation": "list[StorageGuideline] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "StorageGuideline",
     "ref": "StorageGuideline",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[StorageGuideline] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeReadSpec"
  },
  {
   "annotation": "list[StorageGuideline] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "StorageGuideline",
     "ref": "StorageGuideline",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[StorageGuideline] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeUpdateSpec"
  },
  {
   "annotation": "list[StorageGuideline] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "StorageGuideline",
     "ref": "StorageGuideline",
     "type": "ref"
    },
    "nullable": true,
    "raw": "list[StorageGuideline] | None",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeWriteSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "str",
     "name": "note",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "DurationSpec",
     "name": "stability_duration",
     "required": true,
     "schema": {
      "raw": "DurationSpec",
      "ref": "DurationSpec",
      "type": "ref"
     }
    }
   ],
   "name": "StorageGuideline",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.StorageGuideline"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "DurationSpec"
 ]
}
```

## definitional

```json
{
 "candidate_schemas": [
  {
   "annotation": "ProductDefinitionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductDefinitionSpec | None",
    "ref": "ProductDefinitionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.BaseProductKnowledgeSpec"
  },
  {
   "annotation": "ProductDefinitionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductDefinitionSpec | None",
    "ref": "ProductDefinitionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeReadSpec"
  },
  {
   "annotation": "ProductDefinitionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductDefinitionSpec | None",
    "ref": "ProductDefinitionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeUpdateSpec"
  },
  {
   "annotation": "ProductDefinitionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ProductDefinitionSpec | None",
    "ref": "ProductDefinitionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeWriteSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "ValueSetBoundCoding[MEDICATION_FORM_CODES.slug] | None",
     "name": "dosage_form",
     "required": true,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[MEDICATION_FORM_CODES.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "list[Coding]",
     "name": "intended_routes",
     "required": false,
     "schema": {
      "items": {
       "raw": "Coding",
       "ref": "Coding",
       "type": "ref"
      },
      "raw": "list[Coding]",
      "type": "array"
     }
    },
    {
     "annotation": "list[ProductIngredient]",
     "name": "ingredients",
     "required": false,
     "schema": {
      "items": {
       "raw": "ProductIngredient",
       "ref": "ProductIngredient",
       "type": "ref"
      },
      "raw": "list[ProductIngredient]",
      "type": "array"
     }
    },
    {
     "annotation": "list[ProductNutrient]",
     "name": "nutrients",
     "required": false,
     "schema": {
      "items": {
       "raw": "ProductNutrient",
       "ref": "ProductNutrient",
       "type": "ref"
      },
      "raw": "list[ProductNutrient]",
      "type": "array"
     }
    },
    {
     "annotation": "list[DrugCharacteristic]",
     "name": "drug_characteristic",
     "required": false,
     "schema": {
      "items": {
       "raw": "DrugCharacteristic",
       "ref": "DrugCharacteristic",
       "type": "ref"
      },
      "raw": "list[DrugCharacteristic]",
      "type": "array"
     }
    }
   ],
   "name": "ProductDefinitionSpec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductDefinitionSpec"
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
     "annotation": "bool",
     "name": "is_active",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_SUBSTANCE_VALUSET.slug]",
     "name": "substance",
     "required": true,
     "schema": {
      "raw": "ValueSetBoundCoding[CARE_SUBSTANCE_VALUSET.slug]",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ProductStrength",
     "name": "strength",
     "required": true,
     "schema": {
      "raw": "ProductStrength",
      "ref": "ProductStrength",
      "type": "ref"
     }
    }
   ],
   "name": "ProductIngredient",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductIngredient"
  },
  {
   "fields": [
    {
     "annotation": "ValueSetBoundCoding[CARE_NUTRIENTS_VALUESET.slug]",
     "name": "item",
     "required": true,
     "schema": {
      "raw": "ValueSetBoundCoding[CARE_NUTRIENTS_VALUESET.slug]",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ProductStrength",
     "name": "amount",
     "required": true,
     "schema": {
      "raw": "ProductStrength",
      "ref": "ProductStrength",
      "type": "ref"
     }
    }
   ],
   "name": "ProductNutrient",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductNutrient"
  },
  {
   "fields": [
    {
     "annotation": "DrugCharacteristicCode",
     "name": "code",
     "required": true,
     "schema": {
      "raw": "DrugCharacteristicCode",
      "ref": "DrugCharacteristicCode",
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
    }
   ],
   "name": "DrugCharacteristic",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.DrugCharacteristic"
  },
  {
   "fields": [
    {
     "annotation": "Ratio",
     "name": "ratio",
     "required": true,
     "schema": {
      "raw": "Ratio",
      "ref": "Ratio",
      "type": "ref"
     }
    },
    {
     "annotation": "Quantity",
     "name": "quantity",
     "required": true,
     "schema": {
      "raw": "Quantity",
      "ref": "Quantity",
      "type": "ref"
     }
    }
   ],
   "name": "ProductStrength",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductStrength"
  },
  {
   "fields": [
    {
     "annotation": "Quantity",
     "name": "numerator",
     "required": true,
     "schema": {
      "raw": "Quantity",
      "ref": "Quantity",
      "type": "ref"
     }
    },
    {
     "annotation": "Quantity",
     "name": "denominator",
     "required": true,
     "schema": {
      "raw": "Quantity",
      "ref": "Quantity",
      "type": "ref"
     }
    }
   ],
   "name": "Ratio",
   "source_file": "care/emr/resources/common/quantity.py",
   "spec": "care.emr.resources.common.quantity.Ratio"
  },
  {
   "fields": [
    {
     "annotation": "Decimal | None",
     "name": "value",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Decimal | None",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Coding | None",
     "name": "unit",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Coding | None",
      "ref": "Coding",
      "type": "ref"
     }
    },
    {
     "annotation": "dict | None",
     "name": "meta",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
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
    }
   ],
   "name": "Quantity",
   "source_file": "care/emr/resources/common/quantity.py",
   "spec": "care.emr.resources.common.quantity.Quantity"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "Decimal",
  "DrugCharacteristicCode"
 ]
}
```

## base_unit

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.BaseProductKnowledgeSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeUpdateSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[CARE_UCUM_UNITS.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/inventory/product_knowledge/spec.py",
   "spec": "care.emr.resources.inventory.product_knowledge.spec.ProductKnowledgeWriteSpec"
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
