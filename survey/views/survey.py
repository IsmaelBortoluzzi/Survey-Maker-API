import json

from bson.errors import InvalidId
from bson.objectid import ObjectId

from django.core.exceptions import BadRequest

from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveDestroyAPIView, get_object_or_404

from survey.models import Survey, SurveyToRespond
from survey.pagination import SurveyPageNumberPagination
from survey.serializers import SurveySerializer, SurveyToRespondSerializer


class SurveyAPIV1ListCreate(ListCreateAPIView):
    serializer_class = SurveySerializer
    pagination_class = SurveyPageNumberPagination

    def get_queryset(self):
        return Survey.objects.filter()


class SurveyAPIV1RetrieveDestroy(RetrieveDestroyAPIView):
    model = Survey
    serializer_class = SurveySerializer
    pagination_class = SurveyPageNumberPagination
    lookup_field = 'pk'

    def parse_obj_id(self):
        try:
            return ObjectId(self.kwargs.get(self.lookup_field))
        except InvalidId:
            raise BadRequest('Error: Invalid object ID')

    def get_queryset(self):
        return Survey.objects.filter()

    def get_object(self):
        queryset = self.get_queryset()
        _id = self.parse_obj_id()
        obj = get_object_or_404(queryset, id=_id)

        self.check_object_permissions(self.request, obj)

        return obj


