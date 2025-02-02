from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HydroponicSystemViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('systems', HydroponicSystemViewSet, basename='hydroponicsystem')
router.register('measurements', MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('', include(router.urls)),
]