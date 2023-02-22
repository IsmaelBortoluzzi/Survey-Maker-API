from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from contact.models import City, Contact
from contact.serializers import CitySerializer, ContactSerializer

from unicodedata import normalize


class ContactAPIV1Pagination(PageNumberPagination):
    page_size = 10


class ContactAPIV1ListCreate(ListCreateAPIView):
    serializer_class = ContactSerializer
    pagination_class = ContactAPIV1Pagination

    def get_queryset(self):
        return Contact.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        user = User(
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
        )
        user.set_password(data.get('password'))
        user.save()

        Contact.objects.create(
            city=data.get('city_id'),
            birthday=data.get('birthday'),
            gender=data.get('gender'),
            user=user,
        )

        return Response(status=status.HTTP_201_CREATED)


class ContactAPIV1RetrieveUpdate(RetrieveUpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


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
