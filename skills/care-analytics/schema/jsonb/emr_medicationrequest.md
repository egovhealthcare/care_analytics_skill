# emr_medicationrequest JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseMedicationRequestSpec, MedicationRequestReadSpec, MedicationRequestReadWithoutPrescriptionSpec, MedicationRequestResource +2

## method

- shape unknown — no spec declares this field (check serializers; default is dict)

## medication

- Coding? (valueset-bound), optional — BaseMedicationRequestSpec, MedicationRequestReadSpec, MedicationRequestReadWithoutPrescriptionSpec, MedicationRequestSpec

## dosage_instruction

- list[DosageInstruction], required — BaseMedicationRequestSpec, MedicationRequestReadSpec, MedicationRequestReadWithoutPrescriptionSpec, MedicationRequestSpec

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `DosageInstruction`: {sequence: int?, text: str?, additional_instruction: list[Coding]?, patient_instruction: str?, timing: Timing?, as_needed_boolean: bool, as_needed_for: Coding?, site: Coding?, route: Coding?, method: Coding?, dose_and_rate: DoseAndRate?, max_dose_per_period: DoseRange?}
- `DosageQuantity`: {value: decimal, unit: Coding}
- `DoseAndRate`: {type: DoseType, dose_range: DoseRange?, dose_quantity: DosageQuantity?}
- `DoseRange`: {low: DosageQuantity, high: DosageQuantity}
- `PeriodSpec`: {start: datetime?, end: datetime?}
- `Timing`: {repeat: TimingRepeat, code: Coding?}
- `TimingQuantity`: {value: decimal, unit: TimingUnit}
- `TimingRange`: {low: TimingQuantity, high: TimingQuantity}
- `TimingRepeat`: {frequency: int, period: decimal, period_unit: TimingUnit, bounds_duration: TimingQuantity?, bounds_range: TimingRange?, bounds_period: PeriodSpec?}
- `DoseType`: 'ordered' | 'calculated'
- `TimingUnit`: 's' | 'min' | 'h' | 'd' | 'wk' | 'mo' | 'a'
