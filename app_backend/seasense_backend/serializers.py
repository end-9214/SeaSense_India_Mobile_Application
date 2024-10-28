# seasense_backend/serializers.py

from rest_framework import serializers
from .models import Region, State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'beaches']  # Include id field for reference

class RegionSerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True)

    class Meta:
        model = Region
        fields = ['id', 'name', 'states']  # Include id field for region
