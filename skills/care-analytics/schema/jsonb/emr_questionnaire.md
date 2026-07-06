# emr_questionnaire JSONB shapes

Distilled from Pydantic API specs — strong hints, not guarantees; custom serializers can change the stored shape.

## history

- shape unknown — no spec declares this field (check serializers; default is dict)

## meta

- dict, optional — AnswerOption, EnableWhen, Performer, Question +5
- dict?, optional — TemplateConfig

## styling_metadata

- dict, optional — Question, QuestionnaireSpec, QuestionnaireUpdateSpec, QuestionnaireWriteSpec
- dict, required — QuestionnaireReadSpec

## questions

- list[?], optional — Question
- list[?], required — QuestionnaireReadSpec
- list[Question], required — QuestionnaireSpec, QuestionnaireUpdateSpec, QuestionnaireWriteSpec

## definitions

- `AnswerOption`: {meta: dict, value: any, initial_selected: bool}
- `Coding`: {system: str?, version: str?, code: str, display: str?}
- `EnableWhen`: {meta: dict, question: str, operator: EnableOperator, answer: any}
- `Question`: {meta: dict, link_id: str, id: uuid | uuid, code: Coding?, collect_time: bool, collect_performer: bool, text: str, description: str?, type: QuestionType, structured_type: str?, enable_when: list[EnableWhen]?, enable_behavior: EnableBehavior?, disabled_display: DisabledDisplay?, collect_body_site: bool?, collect_method: bool?, required: bool?, repeats: bool?, read_only: bool?, max_length: int?, answer_constraint: AnswerConstraint?, answer_option: list[AnswerOption]?, answer_value_set: str?, is_observation: bool?, unit: Coding?, questions: list[?], formula: str?, styling_metadata: dict, templates: list[TemplateConfig], is_component: bool}
- `TemplateConfig`: {meta: dict?, name: str, content: str, structured_content: dict?}
- `AnswerConstraint`: 'required' | 'optional'
- `DisabledDisplay`: 'hidden' | 'protected'
- `EnableBehavior`: 'all' | 'any'
- `EnableOperator`: 'exists' | 'equals' | 'not_equals' | 'greater' | 'less' | 'greater_or_equals' | 'less_or_equals'
- `QuestionType`: 'group' | 'boolean' | 'decimal' | 'integer' | 'string' | 'text' | 'display' | 'date' | 'dateTime' | 'time' | 'choice' | 'url' | 'quantity' | 'structured'
