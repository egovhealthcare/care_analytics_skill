# emr_specimen JSONB schemas

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
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.BaseSpecimenSpec"
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
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenCreateSpec"
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
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenReadSpec"
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
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenRetrieveSpec"
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
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenUpdateSpec"
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

## specimen_type

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.BaseSpecimenSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenCreateSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenReadSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenRetrieveSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[SPECIMEN_TYPE_CODE_VALUESET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenUpdateSpec"
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

## condition

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.BaseSpecimenSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenCreateSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenReadSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenRetrieveSpec"
  },
  {
   "annotation": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]",
     "type": "valueset_coding"
    },
    "raw": "list[ValueSetBoundCoding[SPECIMEN_CONDITION_VALUESET.slug]]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenUpdateSpec"
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

## processing

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[ProcessingSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProcessingSpec",
     "ref": "ProcessingSpec",
     "type": "ref"
    },
    "raw": "list[ProcessingSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.BaseSpecimenSpec"
  },
  {
   "annotation": "list[ProcessingSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProcessingSpec",
     "ref": "ProcessingSpec",
     "type": "ref"
    },
    "raw": "list[ProcessingSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenCreateSpec"
  },
  {
   "annotation": "list[ProcessingSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProcessingSpec",
     "ref": "ProcessingSpec",
     "type": "ref"
    },
    "raw": "list[ProcessingSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenReadSpec"
  },
  {
   "annotation": "list[ProcessingSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProcessingSpec",
     "ref": "ProcessingSpec",
     "type": "ref"
    },
    "raw": "list[ProcessingSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenRetrieveSpec"
  },
  {
   "annotation": "list[ProcessingSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "ProcessingSpec",
     "ref": "ProcessingSpec",
     "type": "ref"
    },
    "raw": "list[ProcessingSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenUpdateSpec"
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
     "name": "description",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[SPECIMEN_PROCESSING_METHOD_VALUESET.slug] | None",
     "name": "method",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[SPECIMEN_PROCESSING_METHOD_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "performer",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "str",
     "name": "time_date_time",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    }
   ],
   "name": "ProcessingSpec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.ProcessingSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## collection

```json
{
 "candidate_schemas": [
  {
   "annotation": "CollectionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CollectionSpec | None",
    "ref": "CollectionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.BaseSpecimenSpec"
  },
  {
   "annotation": "CollectionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CollectionSpec | None",
    "ref": "CollectionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenCreateSpec"
  },
  {
   "annotation": "CollectionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CollectionSpec | None",
    "ref": "CollectionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenReadSpec"
  },
  {
   "annotation": "CollectionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CollectionSpec | None",
    "ref": "CollectionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenRetrieveSpec"
  },
  {
   "annotation": "CollectionSpec | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "CollectionSpec | None",
    "ref": "CollectionSpec",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.SpecimenUpdateSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "UUID4 | None",
     "name": "collector",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "datetime.datetime | None",
     "name": "collected_date_time",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "datetime.datetime | None",
      "type": "datetime"
     }
    },
    {
     "annotation": "QuantitySpec | None",
     "name": "quantity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "QuantitySpec | None",
      "ref": "QuantitySpec",
      "type": "ref"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[COLLECTION_METHOD_VALUESET.slug] | None",
     "name": "method",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[COLLECTION_METHOD_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "procedure",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
     "name": "body_site",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[FASTING_STATUS_VALUESET.slug] | None",
     "name": "fasting_status_codeable_concept",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[FASTING_STATUS_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "DurationSpec | None",
     "name": "fasting_status_duration",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DurationSpec | None",
      "ref": "DurationSpec",
      "type": "ref"
     }
    }
   ],
   "name": "CollectionSpec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.CollectionSpec"
  },
  {
   "fields": [
    {
     "annotation": "Decimal",
     "name": "value",
     "required": false,
     "schema": {
      "raw": "Decimal",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "Coding",
     "name": "unit",
     "required": true,
     "schema": {
      "raw": "Coding",
      "ref": "Coding",
      "type": "ref"
     }
    }
   ],
   "name": "QuantitySpec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.QuantitySpec"
  },
  {
   "fields": [
    {
     "annotation": "int",
     "name": "value",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "Coding",
     "name": "unit",
     "required": true,
     "schema": {
      "raw": "Coding",
      "ref": "Coding",
      "type": "ref"
     }
    }
   ],
   "name": "DurationSpec",
   "source_file": "care/emr/resources/specimen/spec.py",
   "spec": "care.emr.resources.specimen.spec.DurationSpec"
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
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "Decimal"
 ]
}
```
