from django.contrib.auth.models import User
from rest_framework import serializers

from survey.models import Survey


class QuestionSerializer(serializers.ModelSerializer):
    # responded_surveys = serializers.SerializerMethodField()
    #
    # def get_responded_surveys(self):

    class Meta:
        model = Survey
        fields = ('_id', 'date_created', 'author', 'title', 'responded_surveys')
