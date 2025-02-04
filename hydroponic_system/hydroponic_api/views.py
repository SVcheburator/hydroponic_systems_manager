from rest_framework import viewsets, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import HydroponicSystem, Measurement
from .serializers import HydroponicSystemSerializer, MeasurementSerializer
from .filters import HydroponicSystemFilter, MeasurementFilter
from .pagination import HydroponicSystemPagination, MeasurementPagination


# ViewSets
class HydroponicSystemViewSet(viewsets.ModelViewSet):
    serializer_class = HydroponicSystemSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = HydroponicSystemFilter

    pagination_class = HydroponicSystemPagination

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MeasurementFilter

    ordering_fields = ['ph', 'temperature', 'tds', 'time']
    ordering = ['-time']

    pagination_class = MeasurementPagination

    def get_queryset(self):
        queryset = Measurement.objects.filter(system__owner=self.request.user)
        system_id = self.request.query_params.get("system")
        if system_id:
            queryset = queryset.filter(system_id=system_id)
        return queryset

    def perform_create(self, serializer):
        system = serializer.validated_data['system']
        if system.owner != self.request.user:
            raise serializers.ValidationError("You can only add measurements to systems you own.")
        serializer.save()


# API root
@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    response = {}
    if request.user.is_authenticated:
        response["my systems"] = request.build_absolute_uri(reverse("hydroponicsystem-list"))
        response["logout"] = request.build_absolute_uri(reverse("logout"))
        if request.user.is_staff:
            response["admin"] = request.build_absolute_uri("admin/")
    else:
        response["login"] = request.build_absolute_uri(reverse("login"))
        response["register"] = request.build_absolute_uri(reverse("register"))
    return Response(response)


# User actions
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if not username or not password:
            return JsonResponse({"detail": "Username and password are required"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"detail": "Username already exists"}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)

        return redirect('api-root')

    return render(request, 'hydroponic_api/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('api-root')

        return JsonResponse({"detail": "Invalid credentials"}, status=400)

    return render(request, 'hydroponic_api/login.html')


def logout_view(request):
    logout(request)
    return redirect('api-root')