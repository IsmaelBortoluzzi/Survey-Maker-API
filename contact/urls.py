from django.urls import path

from contact.views import CityAPIList, CityAPIRetrieve

app_name = 'contact'

urlpatterns = [
    path('city/', CityAPIList.as_view(), name='list-cities'),
    path('city/<int:pk>/', CityAPIRetrieve.as_view(), name='retrieve-city'),
]