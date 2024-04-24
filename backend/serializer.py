from rest_framework import serializers

from .models import CameraData

class CameraDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CameraData
        fields = '__all__'