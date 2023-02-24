import json

from bson.errors import InvalidId
from bson.objectid import ObjectId

from django.core.exceptions import BadRequest

from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from survey.models import Survey
from survey.pagination import PageNumberPaginationMongoDB
from survey.serializer import *


class SurveyAPIV1ListCreate(ListCreateAPIView):
    serializer_class = SurveySerializer
    pagination_class = PageNumberPaginationMongoDB

    def get_queryset(self):
        # return Survey.objects.filter(author=self.request.user.id)
        return Survey.objects.filter()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class SurveyAPIV1RetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    model = Survey
    serializer_class = SurveySerializer
    pagination_class = PageNumberPaginationMongoDB
    lookup_field = 'pk'

    def parse_obj_id(self):
        try:
            return ObjectId(self.kwargs.get(self.lookup_field))
        except InvalidId:
            raise BadRequest('Error: Invalid object ID')

    def get_queryset(self):
        # return Survey.objects.filter(author=self.request.user.id)
        return Survey.objects.filter()

    def get_object(self):
        queryset = self.get_queryset()
        _id = self.parse_obj_id()
        obj = get_object_or_404(queryset, id=_id)

        self.check_object_permissions(self.request, obj)

        return obj

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
