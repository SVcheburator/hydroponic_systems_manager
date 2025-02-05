from django.urls import reverse
from rest_framework import serializers
from .models import HydroponicSystem, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    system = serializers.HyperlinkedRelatedField(
        view_name="hydroponicsystem-detail",
        queryset=HydroponicSystem.objects.none()
    )

    class Meta:
        model = Measurement
        fields = ["id", "url", "system", "ph", "temperature", "tds", "time"]
        read_only_fields = ["id", "time"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        
        if request and request.user.is_authenticated:
            system_id = request.query_params.get("system")
            if system_id:
                try:
                    system = HydroponicSystem.objects.get(id=system_id, owner=request.user)
                    self.fields['system'].queryset = HydroponicSystem.objects.filter(id=system.id)
                except HydroponicSystem.DoesNotExist:
                    pass
            else:
                self.fields['system'].queryset = HydroponicSystem.objects.filter(owner=request.user)
    
    def validate_ph(self, value):
        if not (0 <= value <= 14):
            raise serializers.ValidationError("pH must be between 0 and 14")
        return value

    def validate_temperature(self, value):
        if not (0 <= value <= 100):
            raise serializers.ValidationError("Temperature must be realistic (0-100°C)")
        return value
    
    def validate_tds(self, value):
        if not (800 <= value <= 1500):
            raise serializers.ValidationError("TDS must be between 800 and 1500 ppm")
        return value


class HydroponicSystemSerializer(serializers.HyperlinkedModelSerializer):
    measurements_url = serializers.SerializerMethodField()

    class Meta:
        model = HydroponicSystem
        fields = ["id", "url", "name", "description", "created_at", "measurements_url"]
        read_only_fields = ["id", "created_at"]

    def get_measurements_url(self, obj):
        request = self.context.get('request')
        url = reverse('measurement-list') + f'?system={obj.id}'
        return request.build_absolute_uri(url)