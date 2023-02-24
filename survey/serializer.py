from django.contrib.auth.models import User
from rest_framework.fields import empty
from rest_framework.serializers import SerializerMethodField

from survey.models import Survey, SurveyToRespond, Question,  QuestionChoices
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer


class QuestionChoicesSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = QuestionChoices
        fields = ('text', 'chosen')


class QuestionSerializer(EmbeddedDocumentSerializer):
    answer_choices = QuestionChoicesSerializer(many=True)

    class Meta:
        model = Question
        fields = ('name', 'question_type', 'written_answer', 'answer_choices')


class SurveyToRespondSerializer(EmbeddedDocumentSerializer):
    questions = QuestionSerializer(many=True)
    date_responded = SerializerMethodField()

    def get_date_responded(self, obj):
        return obj.date_responded.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = SurveyToRespond
        fields = ('date_responded', 'respondent', 'questions')


class SurveySerializer(DocumentSerializer):
    responded_surveys = SurveyToRespondSerializer(many=True)
    date_created = SerializerMethodField()
    _id = SerializerMethodField(method_name='get_id')

    def get_id(self, obj):
        return str(obj.id)

    def get_date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Survey
        fields = ('_id', 'date_created', 'responded_surveys', 'author', 'title')
        depth = 3

    def update(self, instance, validated_data):
        responded_surveys = validated_data.pop('responded_surveys')
        updated_instance = super(SurveySerializer, self).update(instance, validated_data)

        for responded_survey in responded_surveys:
            updated_instance.responded_surveys.append(SurveyToRespond(**responded_survey))

        updated_instance.save()
        return updated_instance

    def create(self, validated_data):
        responded_surveys = validated_data.pop('responded_surveys')
        created_instance = super(SurveySerializer, self).create(validated_data)

        for responded_survey in responded_surveys:
            created_instance.responded_surveys.append(SurveyToRespond(**responded_survey))

        created_instance.save()
        return created_instance

    def validate(self, attrs):
        return super().validate(attrs)