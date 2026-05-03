# 🔥 Simulador de Incendios Forestales (Django + NumPy)

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![uv](https://img.shields.io/badge/managed%20by-uv-purple.svg)

Una aplicación web interactiva que simula la propagación de incendios forestales mediante autómatas celulares. El sistema integra datos meteorológicos en tiempo real para ajustar dinámicamente la probabilidad de crecimiento y propagación.

## 🚀 Características Principales

- **Motor de Simulación Eficiente**: Implementado con **NumPy**, permitiendo el procesamiento de matrices de hasta 200x200 con alto rendimiento.
- **API REST Robusta**: Desarrollada con **Django REST Framework**, con endpoints documentados para la gestión completa del ciclo de vida de las simulaciones.
- **Integración con Open-Meteo**: Conexión dinámica que ajusta los parámetros de la simulación según el viento, la humedad y la temperatura de cualquier ciudad del mundo.
- **Frontend Interactivo**: Interfaz moderna con un Canvas de HTML5 que permite ejecución manual y modo automático a tiempo real.
- **Estadísticas Técnicas**: Visualización de densidad de árboles, histogramas de incendios y seguimiento de pasos lógicos.

## 🛠️ Stack Tecnológico

* **Backend**: Django 4.2+, Django REST Framework.
* **Cálculo Científico**: NumPy (Gestión de matrices y lógica de estados).
* **Gestión de Entorno**: `uv` (Sustituyendo al tradicional pip para mayor velocidad y determinismo).
* **Frontend**: JavaScript (ES6), HTML5 Canvas, CSS Custom Properties.
* **Base de Datos**: SQLite3 con almacenamiento de estados complejos en `JSONField`.

## 📦 Instalación y Uso rápido

Este proyecto utiliza la herramienta **uv** para garantizar que las dependencias sean idénticas en cualquier equipo.

1. **Clonar el repositorio:**
   ```bash
   git clone <tu-url-de-github>
   cd forest-fire-project