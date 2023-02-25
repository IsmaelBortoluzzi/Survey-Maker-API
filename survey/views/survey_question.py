from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.generics import GenericAPIView, get_object_or_404

from survey.mixins import IdParserMixin
from survey.models import Survey, Question, SurveyToRespond
from survey.serializers import QuestionSerializer


class SurveyAPIV1AddDelQuestion(IdParserMixin, GenericAPIView):
    lookup_field = 'parent_pk'

    def get_queryset(self):
        return Survey.objects.filter()

    def check_if_exist_responses(self):
        _id = self.parse_obj_id(_id=self.kwargs.get(self.lookup_field, None))
        if SurveyToRespond.objects.filter(survey=_id).count() > 1:
            return True
        return False

    def get_object(self):
        _id = self.parse_obj_id(_id=self.kwargs.get(self.lookup_field, None))
        obj = get_object_or_404(self.get_queryset(), id=_id)
        return obj

    def patch(self, request, parent_pk):
        if self.check_if_exist_responses() is True:
            return Response(
                {"Error": "You can't modify the questions if there already are responded surveys"},
                status=status.HTTP_400_BAD_REQUEST
            )
        survey = self.get_object()
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question(**serializer.validated_data)
        survey.survey_model.questions.append(question)
        survey.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, parent_pk):
        if self.check_if_exist_responses() is True:
            return Response(
                {"Error": "You can't modify the questions if there already are responded surveys"},
                status=status.HTTP_400_BAD_REQUEST
            )
        survey = self.get_object()
        question_name = self.request.query_params.get('name', None)
        if question_name is not None:
            survey.survey_model.questions = list(filter(lambda x: x.name != question_name, survey.survey_model.questions))
            survey.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
