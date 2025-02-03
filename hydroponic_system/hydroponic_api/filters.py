from django_filters import filters, FilterSet
from .models import HydroponicSystem

class HydroponicSystemFilter(FilterSet):
    created_at = filters.DateFromToRangeFilter(field_name="created_at", label = "Created between (yyyy-mm-dd)")

    class Meta:
        model = HydroponicSystem
        fields = {"name": ["icontains"], "description": ["icontains"]}