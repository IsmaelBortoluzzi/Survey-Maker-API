from djongo import models


class QuestionManager(models.DjongoManager):
    def mdb(self):
        return self.using('mongodb')


class ChoiceContent(models.Model):
    text = models.TextField()

    class Meta:
        abstract = True


class Question(models.Model):
    objects = QuestionManager()

    QUESTION_TYPE = (
        ('descriptive', 'descriptive'),
        ('multiple_choice', 'multiple_choice'),
        ('mutually_exclusive', 'mutually_exclusive')
    )
    _id = models.ObjectIdField()
    name = models.CharField(max_length=128)
    question_type = models.CharField(max_length=64, choices=QUESTION_TYPE)

    written_answer = models.TextField(default=None)  # if it's a descriptive question
    answer_choices = models.ArrayField(model_container=ChoiceContent)  # if it's NOT a descriptive question
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        return super().save(force_insert=force_insert, force_update=force_update, using='mongodb', update_fields=update_fields)

    def delete(self, using=None, keep_parents=False):
        return super().delete(using='mongodb', keep_parents=keep_parents)
