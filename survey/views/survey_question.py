from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_mongoengine.generics import GenericAPIView, get_object_or_404

from survey.mixins import IdParserMixin
from survey.models import Survey, Question, SurveyToRespond
from survey.serializers import QuestionSerializer


class SurveyAPIV1AddDelUpdateQuestion(IdParserMixin, GenericAPIView):
    lookup_field = 'parent_pk'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Survey.objects.all()

    def check_if_exists_question(self, name):
        survey = self.get_object()
        if len(list(filter(lambda x: x.name == name, survey.survey_model.questions))) >= 1:
            return True
        return False

    def check_if_exist_responses(self):
        _id = self.parse_obj_id(_id=self.kwargs.get(self.lookup_field, None))
        if SurveyToRespond.objects.filter(survey=_id).count() > 1:
            return True
        return False

    def get_object(self):
        _id = self.parse_obj_id(_id=self.kwargs.get(self.lookup_field, None))
        obj = get_object_or_404(self.get_queryset(), id=_id)
        self.check_object_permissions(self.request, obj)
        return obj

    @staticmethod
    def bad_request(message):
        return Response({"Error": message}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def not_found(message):
        return Response({"Error": message}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, parent_pk):
        if self.check_if_exist_responses() is True:
            return self.bad_request("You can't modify the questions if there already are responded surveys")

        survey = self.get_object()
        serializer = QuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = Question(**serializer.validated_data)

        if self.check_if_exists_question(question.name):
            return self.bad_request(f'There already is a question with the name "{question.name}"')

        survey.survey_model.questions.append(question)
        survey.save()
        return Response(status=status.HTTP_201_CREATED)

    def update_question(self, survey):
        current_name = self.request.query_params.get('current_name')
        new_name = self.request.data.get('name')

        for question in survey.survey_model.questions:
            if question.name == current_name:
                question.name = new_name

    def patch(self, request, parent_pk):
        if 'name' not in request.data.keys() or len(request.data.keys()) > 1:
            return self.bad_request('You can only update the field "name"')
        if self.check_if_exists_question(self.request.query_params.get('current_name')) is False:
            return self.not_found('A question with this name does not exist in this survey')

        survey = self.get_object()
        self.update_question(survey)
        survey.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, parent_pk):
        if self.check_if_exist_responses() is True:
            return self.bad_request("You can't modify the questions if there already are responded surveys")

        survey = self.get_object()
        question_name = self.request.query_params.get('name', None)
        if question_name is not None:
            survey.survey_model.questions = list(filter(lambda x: x.name != question_name, survey.survey_model.questions))
            survey.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
