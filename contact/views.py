from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from contact.models import City
from contact.serializers import CitySerializer

from unicodedata import normalize


class ContactAPIV1Pagination(PageNumberPagination):
    page_size = 10


class CityAPIList(ListAPIView):
    serializer_class = CitySerializer
    pagination_class = ContactAPIV1Pagination

    @staticmethod
    def normalize_field(field):
        return normalize('NFKD', field).encode('ASCII', 'ignore').decode('ASCII')

    def get_queryset(self):
        qp = self.request.query_params
        qs = City.objects.all()

        lookup_fields = {
            'name__iexact': self.normalize_field(qp.get('city', '')),
            'state__name__iexact': self.normalize_field(qp.get('state', '')),
            'state__country__name__iexact': self.normalize_field(qp.get('country', '')),
        }

        return qs.filter(**lookup_fields)


class CityAPIRetrieve(RetrieveAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.all()

    def get_object(self):
        return get_object_or_404(self.get_queryset(), id=self.kwargs.get('pk'))
