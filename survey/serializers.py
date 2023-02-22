from django.contrib.auth.models import User
from rest_framework import serializers

from survey.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    # answer_choices = serializers.SerializerMethodField()
    #
    # def get_answer_choices(self):

    class Meta:
        model = Question
        fields = ('name', 'question_type', 'written_answer', 'answer_choices')