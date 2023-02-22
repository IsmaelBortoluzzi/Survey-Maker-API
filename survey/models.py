from djongo import models
from survey.managers import SurveyManager


class QuestionChoices(models.Model):
    text = models.TextField()

    class Meta:
        abstract = True


class Question(models.Model):
    QUESTION_TYPE = (
        ('descriptive', 'descriptive'),
        ('multiple_choice', 'multiple_choice'),
        ('mutually_exclusive', 'mutually_exclusive')
    )
    name = models.CharField(max_length=128)
    question_type = models.CharField(max_length=64, choices=QUESTION_TYPE)

    written_answer = models.TextField(default=None)  # if it's a descriptive question
    answer_choices = models.ArrayField(model_container=QuestionChoices)  # if it's NOT a descriptive question
    
    class Meta:
        abstract = True


class SurveyToRespond(models.Model):
    date_responded = models.DateTimeField()
    respondent = models.IntegerField()
    questions = models.ArrayField(model_container=Question)

    class Meta:
        abstract = True


class Survey(models.Model):
    objects = SurveyManager()
    _id = models.ObjectIdField()
    date_created = models.DateField()
    responded_surveys = models.ArrayField(model_container=SurveyToRespond)
    author = models.IntegerField()
    title = models.CharField(max_length=64)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        return super().save(force_insert=force_insert, force_update=force_update, using='mongodb', update_fields=update_fields)

    def delete(self, using=None, keep_parents=False):
        return super().delete(using='mongodb', keep_parents=keep_parents)
