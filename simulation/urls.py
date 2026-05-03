from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SimulationViewSet, get_weather

router = DefaultRouter()
router.register(r'simulations', SimulationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/weather/', get_weather),
]