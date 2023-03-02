from bson import ObjectId
from bson.errors import InvalidId
from django.core.exceptions import BadRequest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_mongoengine.generics import ListCreateAPIView, get_object_or_404, RetrieveDestroyAPIView

from survey.mixins import IdParserMixin
from survey.models import Survey, SurveyToRespond
from survey.pagination import SurveyPageNumberPagination
from survey.permissions import IsOwnerOfParentSurvey, CanDeleteSurveyToRespond
from survey.serializers import SurveyToRespondSerializer


class SurveyToRespondAPIV1ListCreate(IdParserMixin, ListCreateAPIView):
    serializer_class = SurveyToRespondSerializer
    pagination_class = SurveyPageNumberPagination
    model = SurveyToRespond
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsOwnerOfParentSurvey(), ]
        return super().get_permissions()

    def get_queryset(self):
        _id = self.parse_obj_id(_id=self.request.query_params.get('survey', None))
        qs = self.model.objects.filter(survey=_id)
        return qs

    def create(self, request, *args, **kwargs):
        _id = self.parse_obj_id(_id=request.data.get('survey', None))
        if Survey.objects.filter(id=_id).count() == 0:
            return Response({'Error': 'Survey does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)


class SurveyToRespondAPIV1RetrieveDestroy(IdParserMixin, RetrieveDestroyAPIView):
    serializer_class = SurveyToRespondSerializer
    model = SurveyToRespond
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthenticated(), CanDeleteSurveyToRespond(), ]
        return super().get_permissions()

    def get_queryset(self):
        _id = self.parse_obj_id(_id=self.kwargs.get('pk', None))
        qs = self.model.objects.filter(id=_id)
        return qs
