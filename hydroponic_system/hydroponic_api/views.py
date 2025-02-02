from rest_framework import viewsets, serializers
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    serializer_class = HydroponicSystemSerializer

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        return Measurement.objects.filter(system__owner=self.request.user)

    def perform_create(self, serializer):
        system = serializer.validated_data['system']
        if system.owner != self.request.user:
            raise serializers.ValidationError("You can only add measurements to systems you own.")
        serializer.save()