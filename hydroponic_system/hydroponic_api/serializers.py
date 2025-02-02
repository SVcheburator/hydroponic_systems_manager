from rest_framework import serializers
from .models import HydroponicSystem, Measurement


class HydroponicSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HydroponicSystem
        fields = ["id", "url", "name", "description", "created_at"]
        read_only_fields = ["id", "created_at"]