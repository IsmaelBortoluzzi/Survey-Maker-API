import datetime

from django.contrib.auth.models import User
from django.core.exceptions import BadRequest
from rest_framework.serializers import SerializerMethodField

from survey.models import Survey, SurveyToRespond, Question, QuestionChoices, SurveyToRespondModel
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

from survey.serializer_fields import DocumentPrimaryKeyRelatedField


class QuestionChoicesSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = QuestionChoices
        fields = ('text', 'chosen')


class QuestionSerializer(EmbeddedDocumentSerializer):
    answer_choices = QuestionChoicesSerializer(many=True)

    class Meta:
        model = Question
        fields = ('name', 'question_type', 'written_answer', 'answer_choices')


class SurveyToRespondSerializer(DocumentSerializer):
    questions = QuestionSerializer(many=True)
    _id = SerializerMethodField(method_name='get_id')
    date_responded = SerializerMethodField()
    survey = DocumentPrimaryKeyRelatedField(queryset=Survey.objects.all())

    def get_id(self, obj):
        return str(obj.id)

    def get_date_responded(self, obj):
        return obj.date_responded.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = SurveyToRespond
        fields = ('_id', 'date_responded', 'respondent', 'questions', 'survey')

    def update(self, instance, validated_data):
        questions = validated_data.pop('questions')
        updated_instance = super(SurveyToRespondSerializer, self).update(instance, validated_data)

        for question in questions:
            updated_instance.questions.append(Question(**question))

        updated_instance.save()
        return updated_instance

    def create(self, validated_data):
        questions = validated_data.pop('questions')
        created_instance = super(SurveyToRespondSerializer, self).create(validated_data)

        for question in questions:
            created_instance.questions.append(Question(**question))

        created_instance.save()
        return created_instance

    def validate(self, attrs):
        date_responded = attrs.get('date_responded', datetime.datetime.now())
        respondent = attrs.get('respondent')
        questions = attrs.get('questions')
        survey = attrs.get('survey')

        if all((respondent, questions, survey)) is not True:
            raise BadRequest('You must pass the fields: "respondent", "questions" and "survey"')

        return attrs


class SurveyToRespondModelSerializer(EmbeddedDocumentSerializer):
    questions = QuestionSerializer(many=True)
    date_responded = SerializerMethodField()

    def get_date_responded(self, obj):
        return obj.date_responded.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = SurveyToRespondModel
        fields = ('date_responded', 'respondent', 'questions')


class SurveySerializer(DocumentSerializer):
    survey_model = SurveyToRespondModelSerializer(many=False)
    date_created = SerializerMethodField()
    _id = SerializerMethodField(method_name='get_id')

    def get_id(self, obj):
        return str(obj.id)

    def get_date_created(self, obj):
        return obj.date_created.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Survey
        fields = ('_id', 'date_created', 'survey_model', 'author', 'title')
        depth = 3

    def validate(self, attrs):
        return super().validate(attrs)