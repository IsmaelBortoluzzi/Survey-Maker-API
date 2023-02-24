from django.urls import path

from survey.views import SurveyAPIV1ListCreate, SurveyAPIV1RetrieveUpdateDestroy

app_name = 'survey'
lc = 'list-create'
rud = 'retrieve-update-destroy'

urlpatterns = [
    path('survey/', SurveyAPIV1ListCreate.as_view(), name=f'{lc}-surveys'),
    path('survey/<str:pk>/', SurveyAPIV1RetrieveUpdateDestroy.as_view(), name=f'{rud}-surveys'),
]