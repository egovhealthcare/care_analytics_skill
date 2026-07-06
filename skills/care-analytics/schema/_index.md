# CARE Physical Table Index

One line per table: `db_table` (ClassName) `<N>c` declared columns, `<N>j` JSONB columns, `->` foreign-key target tables. Details: `tables/<db_table>.md`. JSONB shapes: `jsonb/<db_table>.md`. Inherited columns: `_base_models.md`. Enum values: `_enums.md`. SQL rules: `_conventions.md`.

## emr

- `emr_account` (Account) 18c 6j -> emr_encounter emr_patient facility_facility
- `emr_activitydefinition` (ActivityDefinition) 21c 5j -> emr_healthcareservice emr_resourcecategory facility_facility
- `emr_allergyintolerance` (AllergyIntolerance) 13c 4j -> emr_encounter emr_patient
- `emr_availability` (Availability) 8c 3j -> emr_schedule
- `emr_availabilityexception` (AvailabilityException) 7c 2j -> emr_schedulableresource
- `emr_chargeitem` (ChargeItem) 22c 7j -> emr_account emr_chargeitemdefinition emr_encounter emr_invoice emr_patient facility_facility users_user
- `emr_chargeitemdefinition` (ChargeItemDefinition) 13c 4j -> emr_resourcecategory facility_facility
- `emr_condition` (Condition) 12c 6j -> emr_encounter emr_patient
- `emr_consent` (Consent) 8c 4j -> emr_encounter
- `emr_deliveryorder` (DeliveryOrder) 10c 3j -> emr_facilitylocation emr_invoice emr_organization emr_patient
- `emr_device` (Device) 20c 4j -> emr_encounter emr_facilitylocation emr_facilityorganization facility_facility
- `emr_deviceencounterhistory` (DeviceEncounterHistory) 4c 2j -> emr_device emr_encounter
- `emr_devicelocationhistory` (DeviceLocationHistory) 4c 2j -> emr_device emr_facilitylocation
- `emr_deviceservicehistory` (DeviceServiceHistory) 4c 3j -> emr_device
- `emr_diagnosticreport` (DiagnosticReport) 9c 4j -> emr_encounter emr_patient emr_servicerequest facility_facility
- `emr_dispenseorder` (DispenseOrder) 8c 2j -> emr_facilitylocation emr_patient facility_facility
- `emr_encounter` (Encounter) 18c 8j -> emr_facilitylocation emr_patient emr_tokenbooking facility_facility
- `emr_encounterorganization` (EncounterOrganization) 2c 2j -> emr_encounter emr_facilityorganization
- `emr_facilitylocation` (FacilityLocation) 19c 5j -> emr_encounter emr_facilitylocation facility_facility
- `emr_facilitylocationencounter` (FacilityLocationEncounter) 5c 2j -> emr_encounter emr_facilitylocation
- `emr_facilitylocationorganization` (FacilityLocationOrganization) 2c 2j -> emr_facilitylocation emr_facilityorganization
- `emr_facilitymonetoryconfig` (FacilityMonetoryConfig) 5c 5j -> facility_facility
- `emr_facilityorganization` (FacilityOrganization) 1c 4j -> facility_facility
- `emr_facilityorganizationuser` (FacilityOrganizationUser) 3c 2j -> emr_facilityorganization security_rolemodel users_user
- `emr_fileupload` (FileUpload) 10c 2j -> users_user
- `emr_formsubmission` (FormSubmission) 5c 3j -> emr_encounter emr_patient emr_questionnaire
- `emr_healthcareservice` (HealthcareService) 8c 4j -> emr_facilityorganization facility_facility
- `emr_inventoryitem` (InventoryItem) 4c 2j -> emr_facilitylocation emr_product
- `emr_invoice` (Invoice) 18c 5j -> emr_account emr_patient facility_facility
- `emr_medicationadministration` (MedicationAdministration) 15c 6j -> emr_encounter emr_medicationrequest emr_patient emr_productknowledge
- `emr_medicationdispense` (MedicationDispense) 17c 4j -> emr_chargeitem emr_dispenseorder emr_encounter emr_facilitylocation emr_inventoryitem emr_medicationrequest emr_patient
- `emr_medicationrequest` (MedicationRequest) 17c 5j -> emr_encounter emr_medicationrequestprescription emr_patient emr_productknowledge users_user
- `emr_medicationrequestprescription` (MedicationRequestPrescription) 9c 2j -> emr_encounter emr_patient users_user
- `emr_medicationstatement` (MedicationStatement) 9c 4j -> emr_encounter emr_patient
- `emr_metaartifact` (MetaArtifact) 6c 3j
- `emr_notemessage` (NoteMessage) 3c 3j -> emr_notethread
- `emr_notethread` (NoteThread) 3c 2j -> emr_encounter emr_patient
- `emr_observation` (Observation) 25c 12j -> emr_diagnosticreport emr_encounter emr_observationdefinition emr_patient emr_questionnaireresponse users_user
- `emr_observationdefinition` (ObservationDefinition) 15c 8j -> facility_facility
- `emr_organization` (Organization) 1c 4j
- `emr_organizationuser` (OrganizationUser) 3c 2j -> emr_organization security_rolemodel users_user
- `emr_patient` (Patient) 19c 6j -> emr_organization
- `emr_patientidentifier` (PatientIdentifier) 4c 2j -> emr_patient emr_patientidentifierconfig facility_facility
- `emr_patientidentifierconfig` (PatientIdentifierConfig) 3c 3j -> facility_facility
- `emr_patientorganization` (PatientOrganization) 2c 2j -> emr_organization emr_patient
- `emr_patientuser` (PatientUser) 3c 2j -> emr_patient security_rolemodel users_user
- `emr_paymentreconciliation` (PaymentReconciliation) 20c 3j -> emr_account emr_facilitylocation emr_invoice facility_facility
- `emr_product` (Product) 10c 4j -> emr_chargeitemdefinition emr_productknowledge facility_facility
- `emr_productknowledge` (ProductKnowledge) 13c 7j -> emr_resourcecategory facility_facility
- `emr_questionnaire` (Questionnaire) 10c 4j
- `emr_questionnairefacilityorganization` (QuestionnaireFacilityOrganization) 2c 2j -> emr_facilityorganization emr_questionnaire
- `emr_questionnaireorganization` (QuestionnaireOrganization) 2c 2j -> emr_organization emr_questionnaire
- `emr_questionnaireresponse` (QuestionnaireResponse) 9c 4j -> emr_encounter emr_formsubmission emr_patient emr_questionnaire
- `emr_questionnaireresponsetemplate` (QuestionnaireResponseTemplate) 8c 3j -> emr_questionnaire facility_facility
- `emr_reportupload` (ReportUpload) 10c 2j -> emr_template users_user
- `emr_requestorder` (RequestOrder) 11c 2j -> emr_facilitylocation emr_organization
- `emr_resourcecategory` (ResourceCategory) 15c 5j -> emr_resourcecategory facility_facility
- `emr_resourcerequest` (ResourceRequest) 15c 3j -> emr_patient facility_facility users_user
- `emr_resourcerequestcomment` (ResourceRequestComment) 2c 2j -> emr_resourcerequest
- `emr_schedulableresource` (SchedulableResource) 5c 2j -> emr_facilitylocation emr_healthcareservice facility_facility users_user
- `emr_schedule` (Schedule) 8c 2j -> emr_chargeitemdefinition emr_schedulableresource
- `emr_servicerequest` (ServiceRequest) 19c 4j -> emr_activitydefinition emr_encounter emr_healthcareservice emr_patient facility_facility users_user
- `emr_specimen` (Specimen) 13c 6j -> emr_encounter emr_patient emr_servicerequest emr_specimendefinition facility_facility
- `emr_specimendefinition` (SpecimenDefinition) 11c 6j -> facility_facility
- `emr_supplydelivery` (SupplyDelivery) 12c 3j -> emr_deliveryorder emr_inventoryitem emr_product emr_supplyrequest
- `emr_supplyrequest` (SupplyRequest) 5c 2j -> emr_productknowledge emr_requestorder
- `emr_tagconfig` (TagConfig) 16c 4j -> emr_facilityorganization emr_organization emr_tagconfig facility_facility
- `emr_template` (Template) 10c 3j -> facility_facility
- `emr_token` (Token) 10c 2j -> emr_patient emr_tokenbooking emr_tokencategory emr_tokenqueue emr_tokensubqueue facility_facility
- `emr_tokenbooking` (TokenBooking) 10c 2j -> emr_chargeitem emr_encounter emr_patient emr_token emr_tokenslot users_user
- `emr_tokencategory` (TokenCategory) 6c 3j -> facility_facility
- `emr_tokenqueue` (TokenQueue) 6c 2j -> emr_schedulableresource facility_facility
- `emr_tokenslot` (TokenSlot) 5c 2j -> emr_availability emr_schedulableresource
- `emr_tokensubqueue` (TokenSubQueue) 5c 2j -> emr_schedulableresource emr_token facility_facility
- `emr_userresourcefavorites` (UserResourceFavorites) 5c 2j -> facility_facility users_user
- `emr_uservaluesetpreference` (UserValueSetPreference) 3c 3j -> emr_valueset users_user
- `emr_valueset` (ValueSet) 6c 3j

## facility

- `facility_facility` (Facility) 20c 1j -> emr_facilityorganization emr_organization users_user
- `facility_facilityflag` (FacilityFlag) 1c -> facility_facility
- `facility_mobileotp` (MobileOTP) 3c

## security

- `security_permissionmodel` (PermissionModel) 5c
- `security_roleassociation` (RoleAssociation) 5c -> security_rolemodel users_user
- `security_rolemodel` (RoleModel) 6c
- `security_rolepermission` (RolePermission) 3c -> security_permissionmodel security_rolemodel

## users

- `users_plugconfig` (PlugConfig) 2c 1j
- `users_skill` (Skill) 2c
- `users_user` (User) 30c 3j -> emr_organization facility_facility users_skill users_user
- `users_userflag` (UserFlag) 1c -> users_user
- `users_userskill` (UserSkill) 2c -> users_skill users_user
