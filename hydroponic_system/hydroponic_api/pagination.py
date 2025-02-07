from rest_framework.pagination import PageNumberPagination


class HydroponicSystemPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'


class MeasurementPagination(PageNumberPagination):
    page_size = 4
    page_query_param = 'p'