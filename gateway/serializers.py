from rest_framework import serializers
from .models import Device, Employee, Service, DeviceValue

class DeviceValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceValue
        fields = ['id', 'timestamp', 'temperature', 'humidity']

class DeviceSerializer(serializers.ModelSerializer):
    values = DeviceValueSerializer(many=True, read_only=True)
    class Meta:
        model = Device
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    devices = DeviceSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'
        