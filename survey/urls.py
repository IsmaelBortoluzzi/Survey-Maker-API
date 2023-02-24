from django.urls import path

from survey.views import *

app_name = 'survey'
lc = 'list-create'
rud = 'retrieve-update-destroy'

urlpatterns = [
    path('survey/', SurveyAPIV1ListCreate.as_view(), name=f'{lc}-surveys'),
    path('survey/<str:pk>/', SurveyAPIV1RetrieveDestroy.as_view(), name=f'{rud}-surveys'),

    path('survey-to-respond/', SurveyToRespondAPIV1ListCreate.as_view(), name=f'{lc}-surveys-to-respond'),
]