# emr_diagnosticreport JSONB schemas

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
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportCreateSpec"
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
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportListSpec"
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
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportRetrieveSpec"
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
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportSpecBase"
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
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportUpdateSpec"
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

## category

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportCreateSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportListSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportRetrieveSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportSpecBase"
  },
  {
   "annotation": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
   "excluded_by_spec": false,
   "required": true,
   "schema": {
    "raw": "ValueSetBoundCoding[DIAGNOSTIC_SERVICE_SECTIONS_CODE_VALUESET.slug]",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportUpdateSpec"
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

## code

```json
{
 "candidate_schemas": [
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportCreateSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportListSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportRetrieveSpec"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportSpecBase"
  },
  {
   "annotation": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
   "excluded_by_spec": false,
   "required": false,
   "schema": {
    "nullable": true,
    "raw": "ValueSetBoundCoding[CARE_OBSERVATION_VALUSET.slug] | None",
    "type": "valueset_coding"
   },
   "source": "pydantic_spec",
   "source_file": "care/emr/resources/diagnostic_report/spec.py",
   "spec": "care.emr.resources.diagnostic_report.spec.DiagnosticReportUpdateSpec"
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
