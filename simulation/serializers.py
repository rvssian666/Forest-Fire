from rest_framework import serializers
from .models import Simulation

class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = ['id', 'size', 'p', 'f', 'steps_count', 'grid_data', 'fire_histogram', 'created_at']
        read_only_fields = ['id', 'steps_count', 'grid_data', 'fire_histogram', 'created_at']

    def validate_size(self, value):
        if not (20 <= value <= 200):
            raise serializers.ValidationError("El tamaño debe estar entre 20 y 200.")
        return value