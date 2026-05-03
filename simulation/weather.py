import requests
from functools import lru_cache

@lru_cache(maxsize=128)
def geocode_city(city_name):
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
    coords = geocode_city(city_name)
    if not coords: return None
    lat, lon, name = coords
    url = "https://api.open-meteo.com/v1/forecast"
    params = {'latitude': lat, 'longitude': lon, 'current': 'temperature_2m,relative_humidity_2m', 'timezone': 'auto'}
    try:
        data = requests.get(url, params=params).json()['current']
        temp, hum = data['temperature_2m'], data['relative_humidity_2m']
        # Lógica simple para p y f
        p = 0.05 if hum < 50 else 0.08
        f = 0.002 if temp > 30 else 0.001
        return {'city': name, 'p': p, 'f': f, 'temp': temp, 'humidity': hum}
    except: return None