# nhcx_coverageeligibilityrequest JSONB schemas

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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestBaseSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestCreateSpec"
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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestListSpec"
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

## purpose

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[CoverageEligibilityRequestPurposeChoices]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "CoverageEligibilityRequestPurposeChoices",
     "ref": "CoverageEligibilityRequestPurposeChoices",
     "type": "ref"
    },
    "raw": "list[CoverageEligibilityRequestPurposeChoices]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestCreateSpec"
  },
  {
   "annotation": "list[str]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "items": {
     "raw": "str",
     "type": "string"
    },
    "raw": "list[str]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec",
 "unresolved_refs": [
  "CoverageEligibilityRequestPurposeChoices"
 ]
}
```

## insurer

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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestListSpec"
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

## supporting_info

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[CoverageEligibilityRequestSupportingInfoSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "CoverageEligibilityRequestSupportingInfoSpec",
     "ref": "CoverageEligibilityRequestSupportingInfoSpec",
     "type": "ref"
    },
    "raw": "list[CoverageEligibilityRequestSupportingInfoSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestCreateSpec"
  },
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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "str | None",
     "name": "value_string",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "UUID4 | None",
     "name": "value_attachment",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    }
   ],
   "name": "CoverageEligibilityRequestSupportingInfoSpec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestSupportingInfoSpec"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## insurance

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[CoverageEligibilityRequestInsuranceSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "CoverageEligibilityRequestInsuranceSpec",
     "ref": "CoverageEligibilityRequestInsuranceSpec",
     "type": "ref"
    },
    "raw": "list[CoverageEligibilityRequestInsuranceSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestCreateSpec"
  },
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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "bool",
     "name": "focal",
     "required": true,
     "schema": {
      "raw": "bool",
      "type": "boolean"
     }
    },
    {
     "annotation": "Policy",
     "name": "policy",
     "required": true,
     "schema": {
      "raw": "Policy",
      "ref": "Policy",
      "type": "ref"
     }
    }
   ],
   "name": "CoverageEligibilityRequestInsuranceSpec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestInsuranceSpec"
  },
  {
   "fields": [
    {
     "annotation": "str",
     "name": "sno",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "abhanumber",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "mobilenumber",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "memberid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "payerid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "productid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "productname",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "str",
     "name": "processingid",
     "required": true,
     "schema": {
      "raw": "str",
      "type": "string"
     }
    },
    {
     "annotation": "PolicyPeriod | None",
     "name": "policy_period",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "PolicyPeriod | None",
      "ref": "PolicyPeriod",
      "type": "ref"
     }
    }
   ],
   "name": "Policy",
   "source_file": "app/care_nhcx/nhcx/services/types/participant.py",
   "spec": "nhcx.services.types.participant.Policy"
  },
  {
   "fields": [
    {
     "annotation": "str | None",
     "name": "start",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    },
    {
     "annotation": "str | None",
     "name": "end",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "str | None",
      "type": "string"
     }
    }
   ],
   "name": "PolicyPeriod",
   "source_file": "app/care_nhcx/nhcx/services/types/participant.py",
   "spec": "nhcx.services.types.participant.PolicyPeriod"
  }
 ],
 "json_schema_validators": [],
 "meta_stored_fields": [],
 "status": "from_pydantic_spec"
}
```

## item

```json
{
 "candidate_schemas": [
  {
   "annotation": "list[CoverageEligibilityRequestItemSpec]",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "items": {
     "raw": "CoverageEligibilityRequestItemSpec",
     "ref": "CoverageEligibilityRequestItemSpec",
     "type": "ref"
    },
    "raw": "list[CoverageEligibilityRequestItemSpec]",
    "type": "array"
   },
   "source": "pydantic_spec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestCreateSpec"
  },
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
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestListSpec"
  }
 ],
 "default_shape": {
  "type": "array"
 },
 "definitions": [
  {
   "fields": [
    {
     "annotation": "int",
     "name": "sequence",
     "required": true,
     "schema": {
      "raw": "int",
      "type": "integer"
     }
    },
    {
     "annotation": "list[int]",
     "name": "supporting_info_sequence",
     "required": false,
     "schema": {
      "items": {
       "raw": "int",
       "type": "integer"
      },
      "raw": "list[int]",
      "type": "array"
     }
    },
    {
     "annotation": "dict | None",
     "name": "category",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    },
    {
     "annotation": "dict | None",
     "name": "product_or_service",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "dict | None",
      "type": "object"
     }
    },
    {
     "annotation": "list[dict]",
     "name": "modifier",
     "required": false,
     "schema": {
      "items": {
       "raw": "dict",
       "type": "object"
      },
      "raw": "list[dict]",
      "type": "array"
     }
    },
    {
     "annotation": "list[UUID4]",
     "name": "charge_items",
     "required": false,
     "schema": {
      "items": {
       "raw": "UUID4",
       "type": "uuid"
      },
      "raw": "list[UUID4]",
      "type": "array"
     }
    },
    {
     "annotation": "Quantity | None",
     "name": "quantity",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "Quantity | None",
      "ref": "Quantity",
      "type": "ref"
     }
    },
    {
     "annotation": "float | None",
     "name": "unit_price",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "float | None",
      "type": "number"
     }
    },
    {
     "annotation": "list[CoverageEligibilityRequestItemDiagnosisSpec]",
     "name": "diagnosis",
     "required": false,
     "schema": {
      "items": {
       "raw": "CoverageEligibilityRequestItemDiagnosisSpec",
       "ref": "CoverageEligibilityRequestItemDiagnosisSpec",
       "type": "ref"
      },
      "raw": "list[CoverageEligibilityRequestItemDiagnosisSpec]",
      "type": "array"
     }
    }
   ],
   "name": "CoverageEligibilityRequestItemSpec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestItemSpec"
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
  },
  {
   "fields": [
    {
     "annotation": "UUID4 | None",
     "name": "diagnosis_reference",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "UUID4 | None",
      "type": "uuid"
     }
    },
    {
     "annotation": "ValueSetBoundCoding[NHCX_COVERAGE_ELIGIBILITY_REQUEST_ITEM_DIAGNOSIS_CODE_VALUESET.slug] | None",
     "name": "diagnosis_code",
     "required": false,
     "schema": {
      "nullable": true,
      "raw": "ValueSetBoundCoding[NHCX_COVERAGE_ELIGIBILITY_REQUEST_ITEM_DIAGNOSIS_CODE_VALUESET.slug] | None",
      "type": "valueset_coding"
     }
    }
   ],
   "name": "CoverageEligibilityRequestItemDiagnosisSpec",
   "source_file": "app/care_nhcx/nhcx/specs/coverage_eligibility.py",
   "spec": "nhcx.specs.coverage_eligibility.CoverageEligibilityRequestItemDiagnosisSpec"
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
