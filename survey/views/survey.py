import json

from bson.errors import InvalidId
from bson.objectid import ObjectId

from django.core.exceptions import BadRequest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from survey.models import Survey, SurveyToRespond
from survey.pagination import SurveyPageNumberPagination
from survey.permissions import IsAuthor, IsOwner
from survey.serializers import SurveySerializer, SurveyToRespondSerializer


class SurveyAPIV1ListCreate(ListCreateAPIView):
    serializer_class = SurveySerializer
    pagination_class = SurveyPageNumberPagination
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return Survey.objects.filter(author=self.request.user.id)

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user.pk

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SurveyAPIV1RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    model = Survey
    serializer_class = SurveySerializer
    pagination_class = SurveyPageNumberPagination
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwner]

    def parse_obj_id(self):
        try:
            return ObjectId(self.kwargs.get(self.lookup_field))
        except InvalidId:
            raise BadRequest('Error: Invalid object ID')

    def get_queryset(self):
        return Survey.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        _id = self.parse_obj_id()
        obj = get_object_or_404(queryset, id=_id)

        self.check_object_permissions(self.request, obj)

        return obj

    def update(self, request, *args, **kwargs):
        error_response = Response({'Error': 'You can only update the field "title"'})
        if 'title' not in request.data.keys() or len(request.data.keys()) > 1:
            return error_response
        return super().update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)