from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HydroponicSystemViewSet, MeasurementViewSet, api_root, register_view, login_view, logout_view

router = DefaultRouter()
router.register('systems', HydroponicSystemViewSet, basename='hydroponicsystem')
router.register('measurements', MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]