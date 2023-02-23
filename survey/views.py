from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from survey.models import Survey
from survey.serializers import SurveySerializer


class SurveyAPIV1Pagination(PageNumberPagination):
    page_size = 5


class SurveyAPIV1ListCreate(ListCreateAPIView):
    serializer_class = SurveySerializer
    pagination_class = SurveyAPIV1Pagination

    def get_queryset(self):
        return Survey.objects.mdb().all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        a = list(queryset)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
