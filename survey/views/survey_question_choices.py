from rest_framework import status
from rest_framework.response import Response

from survey.models import QuestionChoices
from survey.serializers import QuestionChoicesSerializer
from survey.views import SurveyAPIV1AddDelUpdateQuestion


class SurveyAPIV1AddDelQuestionChoice(SurveyAPIV1AddDelUpdateQuestion):
    def post(self, request, parent_pk):
        question_name = request.data.pop('question_name')
        survey = self.get_object()

        if self.check_if_exist_responses() is True:
            return self.bad_request("You can't modify the questions if there already are responded surveys")
        if self.check_if_exists_question(question_name) is False:
            return self.not_found(f'No question named "{request.query_params.get("question_name")} was found"')

        serializer = QuestionChoicesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question_choice = QuestionChoices(**serializer.validated_data)

        for question in survey.survey_model.questions:
            if question.name == question_name:
                question.answer_choices.append(question_choice)
        survey.save()
        return Response(status=status.HTTP_201_CREATED)

    def update_question(self, survey):
        question_name = self.request.data.pop('question_name')
        new_text = self.request.data.get('text')
        old_text = self.request.data.pop('old_text')

        for question in survey.survey_model.questions:
            if question.name == question_name:
                for choice in question.answer_choices:
                    if choice.text == old_text:
                        choice.text = new_text

    def patch(self, request, parent_pk):
        survey = self.get_object()

        if 'text' not in request.data.keys():
            return self.bad_request('You can only update the field "text"')
        if self.check_if_exists_question(request.data.get('question_name')) is False:
            return self.not_found(f'A question with name "{request.data.get("question_name")}" does not exist in this survey')

        self.update_question(survey)
        survey.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, parent_pk):
        survey = self.get_object()

        if self.check_if_exist_responses() is True:
            return self.bad_request("You can't modify the questions if there already are responded surveys")

        question_name = request.data.pop('question_name', None)
        text = request.data.pop('text', None)

        if question_name is not None and text is not None:
            for question in survey.survey_model.questions:
                if question.name == question_name:
                    question.answer_choices = list(filter(lambda x: x.text != text, question.answer_choices))
            survey.save()
        return Response(status=status.HTTP_204_NO_CONTENT)