from rest_framework import serializers
from .models import Simulation
import numpy as np

class SimulationSerializer(serializers.ModelSerializer):
    # 1. Declarar explícitamente el campo calculado
    tree_density = serializers.SerializerMethodField()

    class Meta:
        model = Simulation
        
        fields = [
            'id', 'size', 'p', 'f', 'steps_count', 
            'grid_data', 'fire_histogram', 'tree_density', 'created_at'
        ]
        read_only_fields = ['id', 'steps_count', 'grid_data', 'fire_histogram', 'created_at', 'tree_density']

    def get_tree_density(self, obj):
        """
        Calcula la proporción de celdas con árboles (valor 1) respecto al total.
        Criterio RA7: Estadísticas en tiempo real.
        """
        # Convertimos a array de numpy asegurando que el tipo sea entero
        grid = np.array(obj.grid_data, dtype=int)
        
        if grid.size == 0:
            return 0.0
            
        # Contamos cuántas celdas tienen exactamente el valor 1 (TREE)
        trees = np.count_nonzero(grid == 1)
        
        # Devolvemos el porcentaje decimal (ej: 0.1534)
        return round(float(trees / grid.size), 4)

    def validate_size(self, value):
        """Validación del tamaño de la cuadrícula entre 20 y 200."""
        if not (20 <= value <= 200):
            raise serializers.ValidationError("El tamaño debe estar entre 20 y 200.")
        return value