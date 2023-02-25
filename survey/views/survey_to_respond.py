from bson import ObjectId
from bson.errors import InvalidId
from django.core.exceptions import BadRequest

from rest_framework import status
from rest_framework.response import Response

from rest_framework_mongoengine.generics import ListCreateAPIView, get_object_or_404, RetrieveDestroyAPIView

from survey.mixins import IdParserMixin
from survey.models import Survey, SurveyToRespond
from survey.pagination import SurveyPageNumberPagination
from survey.serializer import SurveyToRespondSerializer


class SurveyToRespondAPIV1ListCreate(IdParserMixin, ListCreateAPIView):
    serializer_class = SurveyToRespondSerializer
    pagination_class = SurveyPageNumberPagination
    model = SurveyToRespond

    def get_queryset(self):
        _id = self.parse_obj_id(_id=self.request.query_params.get('survey', None))
        qs = self.model.objects.filter(survey=_id)
        return qs


class SurveyToRespondAPIV1RetrieveDestroy(IdParserMixin, RetrieveDestroyAPIView):
    serializer_class = SurveyToRespondSerializer
    model = SurveyToRespond
    lookup_field = 'pk'

    def get_queryset(self):
        _id = self.parse_obj_id(_id=self.kwargs.get('pk', None))
        qs = self.model.objects.filter(id=_id)
        return qs
