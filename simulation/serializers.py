from rest_framework import serializers
from .models import Simulation

class SimulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simulation
        fields = ['id', 'size', 'p', 'f', 'steps_count', 'grid_data', 'fire_histogram', 'created_at']
        read_only_fields = ['id', 'steps_count', 'grid_data', 'fire_histogram', 'created_at']

    def get_tree_density(self, obj):
        """Calcula el porcentaje de celdas que son árboles (estado 1)."""
        import numpy as np
        grid = np.array(obj.grid_data)
        total_cells = grid.size
        trees = np.sum(grid == 1)
        return round(float(trees / total_cells), 4)

    def validate_size(self, value):
        """Validación del tamaño de la cuadrícula entre 20 y 200."""
        if not (20 <= value <= 200):
            raise serializers.ValidationError("El tamaño debe estar entre 20 y 200.")
        return value