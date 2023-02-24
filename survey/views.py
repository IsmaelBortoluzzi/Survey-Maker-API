import json

from bson.errors import InvalidId
from bson.objectid import ObjectId

from django.core.exceptions import BadRequest

from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from survey.models import Survey, SurveyToRespond
from survey.pagination import SurveyPageNumberPagination
from survey.serializer import SurveySerializer, SurveyToRespondSerializer


class SurveyAPIV1ListCreate(ListCreateAPIView):
    serializer_class = SurveySerializer
    pagination_class = SurveyPageNumberPagination

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
    pagination_class = SurveyPageNumberPagination
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


class SurveyToRespondAPIV1ListCreate(ListCreateAPIView):
    serializer_class = SurveyToRespondSerializer
    pagination_class = SurveyPageNumberPagination
    lookup_field = 'parent_pk'

    def parse_obj_id(self):
        try:
            return ObjectId(self.kwargs.get(self.lookup_field))
        except InvalidId:
            raise BadRequest('Error: Invalid object ID')

    def get_queryset(self):
        # qs = Survey.objects.filter(author=self.request.user.id)
        _id = self.parse_obj_id()
        qs = Survey.objects.filter(id=_id).only('responded_surveys').first().responded_surveys
        return qs

    def get_parent_queryset(self):
        return Survey.objects.filtter(id=self.parse_obj_id())

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.get_parent_queryset().update()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

