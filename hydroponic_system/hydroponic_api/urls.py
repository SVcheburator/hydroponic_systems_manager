from django.urls import path, include, reverse
from rest_framework.routers import DefaultRouter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import HydroponicSystemViewSet, MeasurementViewSet

router = DefaultRouter()
router.register('systems', HydroponicSystemViewSet, basename='hydroponicsystem')
router.register('measurements', MeasurementViewSet, basename='measurement')


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'systems': request.build_absolute_uri(reverse('hydroponicsystem-list'))
    })

urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
]