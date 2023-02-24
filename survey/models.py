import datetime
import mongoengine
from mongoengine import CASCADE


class QuestionChoices(mongoengine.EmbeddedDocument):
    text = mongoengine.StringField(max_length=4096, default='', null=True)
    chosen = mongoengine.BooleanField(default=False, required=True)


class Question(mongoengine.EmbeddedDocument):
    QUESTION_TYPES = ('descriptive', 'multiple_choice', 'mutually_exclusive')

    name = mongoengine.StringField(max_length=512, required=True)
    question_type = mongoengine.StringField(choices=QUESTION_TYPES, default=QUESTION_TYPES[0], required=True)

    written_answer = mongoengine.StringField(max_length=4096, required=True, default='', null=True)   # if it's a descriptive question
    answer_choices = mongoengine.EmbeddedDocumentListField(document_type=QuestionChoices)  # if it's NOT a descriptive question


class SurveyToRespondModel(mongoengine.EmbeddedDocument):
    date_responded = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    respondent = mongoengine.IntField(required=True)
    questions = mongoengine.EmbeddedDocumentListField(document_type=Question)


class Survey(mongoengine.Document):
    date_created = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    survey_model = mongoengine.EmbeddedDocumentField(document_type=SurveyToRespondModel)
    author = mongoengine.IntField(required=True)
    title = mongoengine.StringField(max_length=64, null=True, default='')

    meta = {'collection': 'survey_survey'}


class SurveyToRespond(mongoengine.Document):
    date_responded = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    respondent = mongoengine.IntField(required=True)
    questions = mongoengine.EmbeddedDocumentListField(document_type=Question)
    survey = mongoengine.LazyReferenceField(Survey, reverse_delete_rule=CASCADE)

    meta = {'collection': 'survey_survey_to_respond'}
