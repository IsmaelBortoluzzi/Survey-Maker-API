from django.urls import path

from survey.views import SurveyAPIV1ListCreate


app_name = 'survey'

urlpatterns = [
    path('survey/', SurveyAPIV1ListCreate.as_view(), name='list-surveys'),
    path('survey/<int:pk>/', SurveyAPIV1ListCreate.as_view(), name='retrieve-surveys'),
]