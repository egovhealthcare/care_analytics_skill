# emr_medicationdispense JSONB schemas

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
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.BaseMedicationDispenseSpec"
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
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseReadSpec"
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
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseRetrieveSpec"
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
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseUpdateSpec"
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
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseWriteSpec"
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

## dosage_instruction

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[DosageInstruction]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "DosageInstruction",
     "ref": "DosageInstruction",
     "type": "ref"
    },
    "raw": "list[DosageInstruction]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.BaseMedicationDispenseSpec"
  },
  {
   "annotation": "list[DosageInstruction]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "DosageInstruction",
     "ref": "DosageInstruction",
     "type": "ref"
    },
    "raw": "list[DosageInstruction]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseReadSpec"
  },
  {
   "annotation": "list[DosageInstruction]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "DosageInstruction",
     "ref": "DosageInstruction",
     "type": "ref"
    },
    "raw": "list[DosageInstruction]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseRetrieveSpec"
  },
  {
   "annotation": "list[DosageInstruction]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "DosageInstruction",
     "ref": "DosageInstruction",
     "type": "ref"
    },
    "raw": "list[DosageInstruction]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseUpdateSpec"
  },
  {
   "annotation": "list[DosageInstruction]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "DosageInstruction",
     "ref": "DosageInstruction",
     "type": "ref"
    },
    "raw": "list[DosageInstruction]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseWriteSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int | None",
     "name": "sequence",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "int | None",
      "type": "integer"
     }
    },
    {
     "annotation": "str | None",
     "name": "text",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "list[ValueSetBoundCoding[CARE_ADDITIONAL_INSTRUCTION_VALUESET.slug]] | None",
     "name": "additional_instruction",
     "required": false,
     "schema": {
      "items": {
       "raw": "ValueSetBoundCoding[CARE_ADDITIONAL_INSTRUCTION_VALUESET.slug]",
       "type": "valueset_coding"
      },
      "nullable": true,
      "raw": "list[ValueSetBoundCoding[CARE_ADDITIONAL_INSTRUCTION_VALUESET.slug]] | None",
      "type": "array"
     }
    },
    {
     "annotation": "str | None",
     "name": "patient_instruction",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "Timing | None",
     "name": "timing",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Timing | None",
      "ref": "Timing",
      "type": "ref"
     }
    },
    {
     "annotation": "bool",
     "name": "as_needed_boolean",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_AS_NEEDED_REASON_VALUESET.slug] | None",
     "name": "as_needed_for",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_AS_NEEDED_REASON_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
     "name": "site",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_BODY_SITE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_ROUTE_VALUESET.slug] | None",
     "name": "route",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_ROUTE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[CARE_ADMINISTRATION_METHOD_VALUESET.slug] | None",
     "name": "method",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[CARE_ADMINISTRATION_METHOD_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    },
    {
     "annotation": "DoseAndRate | None",
     "name": "dose_and_rate",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DoseAndRate | None",
      "ref": "DoseAndRate",
      "type": "ref"
     }
    },
    {
     "annotation": "DoseRange | None",
     "name": "max_dose_per_period",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DoseRange | None",
      "ref": "DoseRange",
      "type": "ref"
     }
    }
   ],
   "name": "DosageInstruction",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DosageInstruction"
  },
  {
   "fields": [
    {
     "annotation": "TimingRepeat",
     "name": "repeat",
     "required": true,
     "schema": {
      "raw": "TimingRepeat",
      "ref": "TimingRepeat",
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
    }
   ],
   "name": "Timing",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.Timing"
  },
  {
   "fields": [
    {
     "annotation": "DoseType",
     "name": "type",
     "required": true,
     "schema": {
      "raw": "DoseType",
      "ref": "DoseType",
      "type": "ref"
     }
    },
    {
     "annotation": "DoseRange | None",
     "name": "dose_range",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DoseRange | None",
      "ref": "DoseRange",
      "type": "ref"
     }
    },
    {
     "annotation": "DosageQuantity | None",
     "name": "dose_quantity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "DosageQuantity | None",
      "ref": "DosageQuantity",
      "type": "ref"
     }
    }
   ],
   "name": "DoseAndRate",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DoseAndRate"
  },
  {
   "fields": [
    {
     "annotation": "DosageQuantity",
     "name": "low",
     "required": true,
     "schema": {
      "raw": "DosageQuantity",
      "ref": "DosageQuantity",
      "type": "ref"
     }
    },
    {
     "annotation": "DosageQuantity",
     "name": "high",
     "required": true,
     "schema": {
      "raw": "DosageQuantity",
      "ref": "DosageQuantity",
      "type": "ref"
     }
    }
   ],
   "name": "DoseRange",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DoseRange"
  },
  {
   "fields": [
    {
     "annotation": "int",
     "name": "frequency",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "Decimal",
     "name": "period",
     "required": false,
     "schema": {
      "raw": "Decimal",
      "ref": "Decimal",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingUnit",
     "name": "period_unit",
     "required": true,
     "schema": {
      "raw": "TimingUnit",
      "ref": "TimingUnit",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingQuantity | None",
     "name": "bounds_duration",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "TimingQuantity | None",
      "ref": "TimingQuantity",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingRange | None",
     "name": "bounds_range",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "TimingRange | None",
      "ref": "TimingRange",
      "type": "ref"
     }
    },
    {
     "annotation": "PeriodSpec | None",
     "name": "bounds_period",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PeriodSpec | None",
      "ref": "PeriodSpec",
      "type": "ref"
     }
    }
   ],
   "name": "TimingRepeat",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.TimingRepeat"
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
   "name": "DosageQuantity",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.DosageQuantity"
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
     "annotation": "TimingUnit",
     "name": "unit",
     "required": true,
     "schema": {
      "raw": "TimingUnit",
      "ref": "TimingUnit",
      "type": "ref"
     }
    }
   ],
   "name": "TimingQuantity",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.TimingQuantity"
  },
  {
   "fields": [
    {
     "annotation": "TimingQuantity",
     "name": "low",
     "required": true,
     "schema": {
      "raw": "TimingQuantity",
      "ref": "TimingQuantity",
      "type": "ref"
     }
    },
    {
     "annotation": "TimingQuantity",
     "name": "high",
     "required": true,
     "schema": {
      "raw": "TimingQuantity",
      "ref": "TimingQuantity",
      "type": "ref"
     }
    }
   ],
   "name": "TimingRange",
   "source_file": "care/emr/resources/medication/request/spec.py",
   "spec": "care.emr.resources.medication.request.spec.TimingRange"
  },
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
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "Decimal",
  "DoseType",
  "TimingUnit"
 ]
}
```

## substitution

```json
{
 "candidate_schemas": [
  {
   "annotation": "MedicationDispenseSubstitution | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "MedicationDispenseSubstitution | None",
    "ref": "MedicationDispenseSubstitution",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.BaseMedicationDispenseSpec"
  },
  {
   "annotation": "MedicationDispenseSubstitution | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "MedicationDispenseSubstitution | None",
    "ref": "MedicationDispenseSubstitution",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseReadSpec"
  },
  {
   "annotation": "MedicationDispenseSubstitution | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "MedicationDispenseSubstitution | None",
    "ref": "MedicationDispenseSubstitution",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseRetrieveSpec"
  },
  {
   "annotation": "MedicationDispenseSubstitution | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "MedicationDispenseSubstitution | None",
    "ref": "MedicationDispenseSubstitution",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseUpdateSpec"
  },
  {
   "annotation": "MedicationDispenseSubstitution | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "MedicationDispenseSubstitution | None",
    "ref": "MedicationDispenseSubstitution",
    "type": "ref"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseWriteSpec"
  }
 ],
 "default_shape": {
  "type": "object"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "bool",
     "name": "was_substituted",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "SubstitutionType",
     "name": "substitution_type",
     "required": true,
     "schema": {
      "raw": "SubstitutionType",
      "ref": "SubstitutionType",
      "type": "ref"
     }
    },
    {
     "annotation": "SubstitutionReason",
     "name": "reason",
     "required": true,
     "schema": {
      "raw": "SubstitutionReason",
      "ref": "SubstitutionReason",
      "type": "ref"
     }
    }
   ],
   "name": "MedicationDispenseSubstitution",
   "source_file": "care/emr/resources/medication/dispense/spec.py",
   "spec": "care.emr.resources.medication.dispense.spec.MedicationDispenseSubstitution"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "SubstitutionReason",
  "SubstitutionType"
 ]
}
```
