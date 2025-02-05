from django_filters import filters, FilterSet
from .models import HydroponicSystem, Measurement


class HydroponicSystemFilter(FilterSet):
    created_at = filters.DateFromToRangeFilter(field_name="created_at", label = "Created between (yyyy-mm-dd)")

    class Meta:
        model = HydroponicSystem
        fields = {
            "name": ["icontains"],
            "description": ["icontains"]
            }


class MeasurementFilter(FilterSet):
    system = filters.NumberFilter(field_name="system__id")
    time = filters.DateFromToRangeFilter(field_name="time", label = "Measurements date between (yyyy-mm-dd)")

    class Meta:
        model = Measurement
        fields = {
            "ph": ["gte", "lte"],
            "temperature": ["gte", "lte"],
            "tds": ["gte", "lte"]
            }