from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HydroponicSystem(models.Model):
    owner = models.ForeignKey(User, verbose_name="Owner", on_delete=models.CASCADE, related_name="systems")
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", blank=True, null=True)
    created_at = models.DateTimeField("Created_at", auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "HydroponicSystem"
        verbose_name_plural = "HydroponicSystems"


class Measurement(models.Model):
    system = models.ForeignKey(HydroponicSystem, verbose_name="System", on_delete=models.CASCADE, related_name="measurements")
    ph = models.FloatField("pH")
    temperature = models.FloatField("temperature")
    tds = models.FloatField("tds")
    time = models.DateTimeField("Time", auto_now_add=True)

    def __str__(self):
        return f"Measurement of {self.system.name} system at {self.time}"
    
    class Meta:
        verbose_name = "Measurement"
        verbose_name_plural = "Measurements"
