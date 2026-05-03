from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Simulation
from .serializers import SimulationSerializer
from .engine import ForestFireEngine
from .weather import get_weather_params

class SimulationViewSet(viewsets.ModelViewSet):
    queryset = Simulation.objects.all()
    serializer_class = SimulationSerializer

    def perform_create(self, serializer):
        engine = ForestFireEngine(serializer.validated_data['size'], serializer.validated_data['p'], serializer.validated_data['f'])
        serializer.save(grid_data=engine.grid.tolist())

    @action(detail=True, methods=['post'])
    def step(self, request, pk=None):
        """
    Avanza la simulación N pasos.
    Parámetros:
        - steps (int, opcional): Número de pasos a avanzar. Por defecto 1.
    Respuesta:
        - JSON con el estado actualizado de la simulación.
    """
        sim = self.get_object()
        
        steps_val = request.data.get('steps') or request.query_params.get('steps', 1)
        try:
            steps = int(steps_val)
        except (ValueError, TypeError):
            steps = 1

        engine = ForestFireEngine(sim.size, sim.p, sim.f, grid=sim.grid_data)
        
        # IMPORTANTE: Convertir el historial de la DB a un diccionario con llaves INT
        if sim.fire_histogram:
            engine.fire_sizes = {int(k): v for k, v in sim.fire_histogram.items()}
        else:
            engine.fire_sizes = {}
        
        for _ in range(steps):
            engine.step()

        # Guardar resultados limpios
        sim.grid_data = engine.grid.tolist()
        sim.steps_count += steps
        sim.fire_histogram = engine.fire_sizes # Ya es un dict normal con llaves correctas
        sim.save()

        return Response(SimulationSerializer(sim).data)

def get_weather(request):
    city = request.GET.get('city')
    if not city: return JsonResponse({'error': 'Falta ciudad'}, status=400)
    return JsonResponse(get_weather_params(city))

def index(request): return render(request, 'index.html')
