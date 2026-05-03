import requests
from functools import lru_cache

@lru_cache(maxsize=128)
def geocode_city(city_name):
    """
    Obtiene las coordenadas (lat, lon) de una ciudad usando la API de Open-Meteo.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {'name': city_name, 'count': 1, 'format': 'json'}
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        if 'results' not in data: return None
        res = data['results'][0]
        return (res['latitude'], res['longitude'], res.get('name', city_name))
    except: return None

def get_weather_params(city_name):
    """
    Consulta Open-Meteo y calcula p y f basados en la rúbrica:
    - Viento > 30 km/h: reduce p (los árboles caen).
    - Humedad > 70%: aumenta p (crecimiento) y f (tormentas).
    - Temp > 35°C: aumenta f (más rayos).
    """
    coords = geocode_city(city_name)
    if not coords: return None
    lat, lon, name = coords
    
    url = "https://api.open-meteo.com/v1/forecast"
    # Añadimos wind_speed_10m que es requisito del enunciado
    params = {
        'latitude': lat, 
        'longitude': lon, 
        'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m', 
        'timezone': 'auto'
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()['current']
        
        temp = data['temperature_2m']
        hum = data['relative_humidity_2m']
        wind = data['wind_speed_10m']

        # Valores base
        p = 0.05
        f = 0.001

        # Lógica basada estrictamente en el PDF del proyecto
        # 1. Viento fuerte (> 30 km/h) -> reduce p
        if wind > 30:
            p -= 0.02
        
        # 2. Humedad alta (> 70%) -> aumenta p y f
        if hum > 70:
            p += 0.03
            f += 0.001
        
        # 3. Temperatura alta (> 35°C) -> aumenta f
        if temp > 35:
            f += 0.002

        # Asegurar que los valores no sean negativos o absurdos
        p = max(0.01, min(0.2, p))
        f = max(0.0001, min(0.1, f))

        return {
            'city': name, 
            'p': round(p, 4), 
            'f': round(f, 4), 
            'temp': temp, 
            'humidity': hum,
            'wind_speed': wind
        }
    except Exception as e:
        print(f"Error en weather: {e}")
        return None