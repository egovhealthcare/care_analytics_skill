# emr_questionnaireresponse JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — EMRQuestionnaireResponseBase, QuestionnaireResponseReadSpec, QuestionnaireResponseUpdate

## responses

- list[?], required — QuestionnaireResponseReadSpec

## structured_responses

- dict, required — QuestionnaireResponseReadSpec
