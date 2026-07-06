# emr_medicationdispense JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseMedicationDispenseSpec, MedicationDispenseReadSpec, MedicationDispenseRetrieveSpec, MedicationDispenseUpdateSpec +1

## dosage_instruction

- list[DosageInstruction], optional — BaseMedicationDispenseSpec, MedicationDispenseReadSpec, MedicationDispenseRetrieveSpec, MedicationDispenseUpdateSpec +1

## substitution

- MedicationDispenseSubstitution?, optional — BaseMedicationDispenseSpec, MedicationDispenseReadSpec, MedicationDispenseRetrieveSpec, MedicationDispenseUpdateSpec +1

## definitions

- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `DosageInstruction`: {sequence: int?, text: str?, additional_instruction: list[Coding]?, patient_instruction: str?, timing: Timing?, as_needed_boolean: bool, as_needed_for: Coding?, site: Coding?, route: Coding?, method: Coding?, dose_and_rate: DoseAndRate?, max_dose_per_period: DoseRange?}
- `DosageQuantity`: {value: decimal, unit: Coding}
- `DoseAndRate`: {type: DoseType, dose_range: DoseRange?, dose_quantity: DosageQuantity?}
- `DoseRange`: {low: DosageQuantity, high: DosageQuantity}
- `MedicationDispenseSubstitution`: {was_substituted: bool, substitution_type: SubstitutionType, reason: SubstitutionReason}
- `PeriodSpec`: {start: datetime?, end: datetime?}
- `Timing`: {repeat: TimingRepeat, code: Coding?}
- `TimingQuantity`: {value: decimal, unit: TimingUnit}
- `TimingRange`: {low: TimingQuantity, high: TimingQuantity}
- `TimingRepeat`: {frequency: int, period: decimal, period_unit: TimingUnit, bounds_duration: TimingQuantity?, bounds_range: TimingRange?, bounds_period: PeriodSpec?}
- `SubstitutionReason`: 'CT' | 'FP' | 'OS' | 'RR'
- `SubstitutionType`: 'E' | 'EC' | 'BC' | 'G' | 'TE' | 'TB' | 'TG' | 'F' | 'N'
- `DoseType`: 'ordered' | 'calculated'
- `TimingUnit`: 's' | 'min' | 'h' | 'd' | 'wk' | 'mo' | 'a'
