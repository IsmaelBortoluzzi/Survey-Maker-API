import json

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView

from survey.models import Survey
from survey.pagination import PageNumberPaginationMongoDB


class SurveyAPIV1ListCreate(ListCreateAPIView):
    pagination_class = PageNumberPaginationMongoDB

    def get_queryset(self):
        return Survey.objects.all()

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset()
        for x in qs:
            print(x)
        data = {'surveys': list(map(lambda x: json.loads(x.to_json()), self.get_queryset()))}
        return JsonResponse(data, status=status.HTTP_200_OK)
