from rest_framework import serializers
from .models import HydroponicSystem, Measurement


class HydroponicSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ["id", "url", "name", "description", "created_at"]
        read_only_fields = ["id", "created_at"]


class MeasurementSerializer(serializers.ModelSerializer):
    system = serializers.HyperlinkedRelatedField(
        view_name="hydroponicsystem-detail",
        queryset=HydroponicSystem.objects.all()
    )

    class Meta:
        model = Measurement
        fields = ["id", "url", "system", "ph", "temperature", "tds", "time"]
        read_only_fields = ["id", "time"]