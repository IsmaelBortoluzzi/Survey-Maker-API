import mongoengine
from survey.managers import SurveyManager


class QuestionChoices(mongoengine.Document):
    text = mongoengine.StringField(default='', required=True)
    chosen = mongoengine.BooleanField(default=False, required=True)

    class Meta:
        abstract = True


class Question(mongoengine.Document):
    QUESTION_TYPE = (
        ('descriptive', 'descriptive'),
        ('multiple_choice', 'multiple_choice'),
        ('mutually_exclusive', 'mutually_exclusive')
    )
    name = models.CharField(max_length=512)
    question_type = models.CharField(max_length=64, choices=QUESTION_TYPE)

    written_answer = models.TextField(default=None)  # if it's a descriptive question
    answer_choices = models.ArrayField(model_container=QuestionChoices)  # if it's NOT a descriptive question
    
    class Meta:
        abstract = True


class SurveyToRespond(mongoengine.Document):
    date_responded = models.DateTimeField()
    respondent = models.IntegerField()
    questions = models.ArrayField(model_container=Question)

    class Meta:
        abstract = True


class Survey(mongoengine.Document):
    objects = SurveyManager()
    _id = models.ObjectIdField()
    date_created = models.DateField()
    responded_surveys = models.ArrayField(model_container=SurveyToRespond)
    author = models.IntegerField()
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'survey_survey'
