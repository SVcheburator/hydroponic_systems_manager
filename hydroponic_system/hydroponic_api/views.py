from rest_framework import viewsets, serializers
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer
from .filters import HydroponicSystemFilter, MeasurementFilter


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    serializer_class = HydroponicSystemSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = HydroponicSystemFilter

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MeasurementFilter

    ordering_fields = ['ph', 'temperature', 'tds', 'time']
    ordering = ['-time']

    def get_queryset(self):
        queryset = Measurement.objects.filter(system__owner=self.request.user)
        system_id = self.request.query_params.get("system")
        if system_id:
            queryset = queryset.filter(system_id=system_id)
        return queryset

    def perform_create(self, serializer):
        system = serializer.validated_data['system']
        if system.owner != self.request.user:
            raise serializers.ValidationError("You can only add measurements to systems you own.")
        serializer.save()