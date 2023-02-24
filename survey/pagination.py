from rest_framework.pagination import PageNumberPagination


class SurveyPageNumberPagination(PageNumberPagination):
    page_size = 10
