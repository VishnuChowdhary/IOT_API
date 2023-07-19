from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view, OpenApiParameter
from .models import Device, Employee, Service
from .serializers import DeviceSerializer, EmployeeSerializer, ServiceSerializer

@extend_schema(tags=['Devices'])
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

@extend_schema_view(
    list=extend_schema(tags=['Employees']),
    update=extend_schema(exclude=True),
)

@extend_schema(tags=['Employees'])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@extend_schema(tags=['Services'])
class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
