from django.contrib.auth.models import User
from rest_framework.fields import empty
from rest_framework.serializers import SerializerMethodField

from survey.models import Survey, SurveyToRespond, Question, QuestionChoices, SurveyToRespondModel
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


class SurveyToRespondSerializer(DocumentSerializer):
    questions = QuestionSerializer(many=True)
    _id = SerializerMethodField(method_name='get_id')
    date_responded = SerializerMethodField()
    survey_id = SerializerMethodField()

    def get_id(self, obj):
        return str(obj.id)

    def get_date_responded(self, obj):
        return obj.date_responded.strftime('%Y-%m-%d %H:%M:%S')

    def get_survey_id(self, obj):
        return str(obj.survey.pk)

    class Meta:
        model = SurveyToRespond
        fields = ('date_responded', 'respondent', 'questions', 'survey_id')

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
        return super().validate(attrs)


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