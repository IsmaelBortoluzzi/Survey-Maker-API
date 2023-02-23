import datetime
from enum import Enum

import mongoengine
from survey.managers import SurveyManager


class QuestionChoices(mongoengine.EmbeddedDocument):
    text = mongoengine.StringField(max_length=4096, default='')
    chosen = mongoengine.BooleanField(default=False, required=True)


class Question(mongoengine.EmbeddedDocument):
    class QuestionType(Enum):
        DESCRIPTIVE = 'descriptive'
        MULTIPLE_CHOICE = 'multiple_choice'
        MUTUALLY_EXCLUSIVE = 'mutually_exclusive'

    name = mongoengine.StringField(max_length=512, required=True)
    question_type = mongoengine.EnumField(QuestionType, default=QuestionType.DESCRIPTIVE, required=True)

    written_answer = mongoengine.StringField(max_length=4096, default='')  # if it's a descriptive question
    answer_choices = mongoengine.EmbeddedDocumentListField(document_type=QuestionChoices)  # if it's NOT a descriptive question


class SurveyToRespond(mongoengine.EmbeddedDocument):
    date_responded = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    respondent = mongoengine.IntField(required=True)
    questions = mongoengine.EmbeddedDocumentListField(document_type=Question)


class Survey(mongoengine.Document):
    _id = mongoengine.ObjectIdField(primary_key=True)
    date_created = mongoengine.DateTimeField(default=datetime.datetime.utcnow)
    responded_surveys = mongoengine.EmbeddedDocumentListField(document_type=SurveyToRespond)
    author = mongoengine.IntField(required=True)
    title = mongoengine.StringField(max_length=64, default='')

    meta = {'collection': 'survey_survey'}
