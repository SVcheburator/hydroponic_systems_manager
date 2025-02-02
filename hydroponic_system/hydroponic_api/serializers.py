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
    
    def validate_ph(self, value):
        if not (0 <= value <= 14):
            raise serializers.ValidationError("pH must be between 0 and 14")
        return value

    def validate_temperature(self, value):
        if not (0 <= value <= 100):
            raise serializers.ValidationError("Temperature must be realistic (0-100°C)")
        return value