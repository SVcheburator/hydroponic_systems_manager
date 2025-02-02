from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .models import HydroponicSystem
from .serializers import HydroponicSystemSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({'systems': {'list': request.build_absolute_uri(reverse('system-list')),}})


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)