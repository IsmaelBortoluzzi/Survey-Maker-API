from bson import ObjectId
from bson.errors import InvalidId
from django.core.exceptions import BadRequest

from rest_framework import status
from rest_framework.response import Response

from rest_framework_mongoengine.generics import ListCreateAPIView, get_object_or_404

from survey.models import Survey, SurveyToRespond
from survey.pagination import SurveyPageNumberPagination
from survey.serializer import SurveyToRespondSerializer


class SurveyToRespondAPIV1ListCreate(ListCreateAPIView):
    serializer_class = SurveyToRespondSerializer
    pagination_class = SurveyPageNumberPagination
    model = SurveyToRespond

    def parse_obj_id(self, _id):
        try:
            return ObjectId(_id)
        except InvalidId:
            raise BadRequest('Error: Invalid object ID')

    def get_queryset(self):
        _id = self.parse_obj_id(_id=self.request.query_params.get('survey', None))
        qs = self.model.objects.filter(survey=_id)
        return qs

