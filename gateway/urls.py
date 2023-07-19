from django.urls import path, include
from rest_framework import routers

from gateway.views import DeviceViewSet,  EmployeeViewSet, ServiceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
