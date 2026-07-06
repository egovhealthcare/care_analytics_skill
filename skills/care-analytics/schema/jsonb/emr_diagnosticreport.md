# emr_diagnosticreport JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — DiagnosticReportCreateSpec, DiagnosticReportListSpec, DiagnosticReportRetrieveSpec, DiagnosticReportSpecBase +1

## category

- Coding (valueset-bound), required — DiagnosticReportCreateSpec, DiagnosticReportListSpec, DiagnosticReportRetrieveSpec, DiagnosticReportSpecBase +1

## code

- Coding? (valueset-bound), optional — DiagnosticReportCreateSpec, DiagnosticReportListSpec, DiagnosticReportRetrieveSpec, DiagnosticReportSpecBase +1

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
