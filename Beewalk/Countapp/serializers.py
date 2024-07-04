from rest_framework import serializers
from .models import Record, Certification


class WalkDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
