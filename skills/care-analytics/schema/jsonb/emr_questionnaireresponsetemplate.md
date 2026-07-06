# emr_questionnaireresponsetemplate JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — QuestionnaireResponseTemplateBaseSpec, QuestionnaireResponseTemplateCreateSpec, QuestionnaireResponseTemplateReadSpec, QuestionnaireResponseTemplateRetrieveSpec +1

## template_data

- TemplateData, required — QuestionnaireResponseTemplateBaseSpec, QuestionnaireResponseTemplateCreateSpec, QuestionnaireResponseTemplateReadSpec, QuestionnaireResponseTemplateRetrieveSpec +1

## definitions

- `ActivityDefinitionTemplateSpec`: {slug: str, service_request: ServiceRequestUpdateSpec}
- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `DosageInstruction`: {sequence: int?, text: str?, additional_instruction: list[Coding]?, patient_instruction: str?, timing: Timing?, as_needed_boolean: bool, as_needed_for: Coding?, site: Coding?, route: Coding?, method: Coding?, dose_and_rate: DoseAndRate?, max_dose_per_period: DoseRange?}
- `DosageQuantity`: {value: decimal, unit: Coding}
- `DoseAndRate`: {type: DoseType, dose_range: DoseRange?, dose_quantity: DosageQuantity?}
- `DoseRange`: {low: DosageQuantity, high: DosageQuantity}
- `MedicationRequestTemplateSpec`: {status: MedicationRequestStatus, status_reason: StatusReason?, intent: MedicationRequestIntent, category: MedicationRequestCategory, priority: MedicationRequestPriority, do_not_perform: bool, medication: Coding?, dosage_instruction: list[DosageInstruction], authored_on: datetime, note: str?, dispense_status: MedicationRequestDispenseStatus?, requested_product: str?}
- `PeriodSpec`: {start: datetime?, end: datetime?}
- `QuestionnaireAnswer`: {question_id: str, answer: dict, meta: dict}
- `ServiceRequestUpdateSpec`: {meta: dict, id: str?, title: str?, status: ServiceRequestStatusChoices?, intent: ServiceRequestIntentChoices?, priority: ServiceRequestPriorityChoices?, category: ActivityDefinitionCategoryOptions?, do_not_perform: bool?, note: str?, body_site: Coding?, code: Coding?, occurance: datetime?, patient_instruction: str?, healthcare_service: uuid?, locations: list[uuid], requester: uuid?}
- `TemplateData`: {medication_request: list[MedicationRequestTemplateSpec]?, questionnaire: list[QuestionnaireAnswer]?, activity_definition: list[ActivityDefinitionTemplateSpec]?, meta: dict?}
- `Timing`: {repeat: TimingRepeat, code: Coding?}
- `TimingQuantity`: {value: decimal, unit: TimingUnit}
- `TimingRange`: {low: TimingQuantity, high: TimingQuantity}
- `TimingRepeat`: {frequency: int, period: decimal, period_unit: TimingUnit, bounds_duration: TimingQuantity?, bounds_range: TimingRange?, bounds_period: PeriodSpec?}
- `ActivityDefinitionCategoryOptions`: 'laboratory' | 'imaging' | 'counselling' | 'surgical_procedure' | 'education'
- `DoseType`: 'ordered' | 'calculated'
- `MedicationRequestCategory`: 'inpatient' | 'outpatient' | 'community' | 'discharge'
- `MedicationRequestDispenseStatus`: 'complete' | 'partial' | 'incomplete' | 'declined'
- `MedicationRequestIntent`: 'proposal' | 'plan' | 'order' | 'original_order' | 'reflex_order' | 'filler_order' | 'instance_order'
- `MedicationRequestPriority`: 'routine' | 'urgent' | 'asap' | 'stat'
- `MedicationRequestStatus`: 'active' | 'on_hold' | 'ended' | 'stopped' | 'completed' | 'cancelled' | 'entered_in_error' | 'draft' | 'unknown'
- `StatusReason`: 'altchoice' | 'clarif' | 'drughigh' | 'hospadm' | 'labint' | 'non_avail' | 'preg' | 'salg' | 'sddi' | 'sdupther' | 'sintol' | 'surg' | 'washout'
- `TimingUnit`: 's' | 'min' | 'h' | 'd' | 'wk' | 'mo' | 'a'
- `ServiceRequestIntentChoices`: 'proposal' | 'plan' | 'directive' | 'order'
- `ServiceRequestPriorityChoices`: 'routine' | 'urgent' | 'asap' | 'stat'
- `ServiceRequestStatusChoices`: 'draft' | 'active' | 'on_hold' | 'entered_in_error' | 'ended' | 'completed' | 'revoked'
