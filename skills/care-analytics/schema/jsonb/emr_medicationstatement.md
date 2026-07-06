# emr_medicationstatement JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseMedicationStatementSpec, MedicationStatementReadSpec, MedicationStatementSpec, MedicationStatementUpdateSpec

## medication

- Coding (valueset-bound), required — BaseMedicationStatementSpec, MedicationStatementReadSpec, MedicationStatementSpec

## effective_period

- PeriodSpec?, optional — BaseMedicationStatementSpec, MedicationStatementReadSpec, MedicationStatementSpec, MedicationStatementUpdateSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `PeriodSpec`: {start: datetime?, end: datetime?}
