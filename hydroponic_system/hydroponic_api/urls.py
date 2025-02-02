from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HydroponicSystemViewSet

router = DefaultRouter()
router.register('systems', HydroponicSystemViewSet, basename='hydroponicsystem')

urlpatterns = [
    path('', include(router.urls)),
]