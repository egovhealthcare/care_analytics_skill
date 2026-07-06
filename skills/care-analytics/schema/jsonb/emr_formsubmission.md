# emr_formsubmission JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — BaseFormSubmissionSpec, FormSubmissionReadSpec, FormSubmissionUpdateSpec, FormSubmissionWriteSpec

## response_dump

- dict, required — FormSubmissionReadSpec, FormSubmissionUpdateSpec, FormSubmissionWriteSpec
