# seasense_backend/serializers.py

from rest_framework import serializers
from .models import Region, State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name', 'beaches']  # Include beaches field

class RegionSerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True)

    class Meta:
        model = Region
        fields = ['name', 'states']  # Include states for each region
