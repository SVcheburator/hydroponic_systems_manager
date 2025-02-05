from django.contrib import admin
from .models import Measurement, HydroponicSystem


class HydroponicSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'description', 'created_at')


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('id', 'system', 'ph', 'temperature', 'tds', 'time')


admin.site.register(HydroponicSystem, HydroponicSystemAdmin)
admin.site.register(Measurement, MeasurementAdmin)