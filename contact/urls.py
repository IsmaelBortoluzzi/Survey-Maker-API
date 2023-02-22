from django.urls import path

from contact.views import CityAPIList, CityAPIRetrieve, ContactAPIV1ListCreate, ContactAPIV1RetrieveUpdate

app_name = 'contact'

urlpatterns = [
    path('city/', CityAPIList.as_view(), name='list-cities'),
    path('city/<int:pk>/', CityAPIRetrieve.as_view(), name='retrieve-city'),

    path('contact/', ContactAPIV1ListCreate.as_view(), name='list-cities'),
    path('contact/<int:pk>/', ContactAPIV1RetrieveUpdate.as_view(), name='retrieve-city'),

]