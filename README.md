# 🔥 Simulador de Incendios Forestales (Django + NumPy)

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![Language Composition](https://img.shields.io/badge/Python-59.6%25-brightgreen.svg)
![Language Composition](https://img.shields.io/badge/HTML-40.4%25-orange.svg)

Una aplicación web interactiva que simula la propagación de incendios forestales mediante autómatas celulares. El sistema integra datos meteorológicos en tiempo real para ajustar dinámicamente los parámetros de la simulación.

## 🚀 Características Principales

- **Motor de Simulación Eficiente**: Implementado con **NumPy**, permitiendo el procesamiento de matrices de hasta 200x200 con alto rendimiento.
- **API REST Robusta**: Desarrollada con **Django REST Framework**, con endpoints documentados para la gestión completa del ciclo de vida de las simulaciones.
- **Integración con Open-Meteo**: Conexión dinámica que ajusta los parámetros de la simulación según el viento, la humedad y la temperatura de cualquier ciudad del mundo.
- **Frontend Interactivo**: Interfaz moderna con un Canvas de HTML5 que permite ejecución manual y modo automático a tiempo real.
- **Estadísticas Técnicas**: Visualización de densidad de árboles, histogramas de incendios y seguimiento de pasos lógicos.

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|-----------|-----------|
| **Backend** | Django 4.2+, Django REST Framework |
| **Cálculo Científico** | NumPy (Gestión de matrices y lógica de estados) |
| **Gestión de Entorno** | `uv` (Sustituyendo al tradicional pip) |
| **Frontend** | JavaScript (ES6), HTML5 Canvas, CSS Custom Properties |
| **Base de Datos** | SQLite3 con almacenamiento en `JSONField` |

## 📊 Composición del Repositorio

| Lenguaje | Porcentaje |
|----------|-----------|
| Python | 59.6% |
| HTML | 40.4% |

## 📦 Instalación y Uso Rápido

### Requisitos previos
- Python 3.11+
- `uv` (gestor de paquetes moderno)

### Pasos de instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/rvssian666/Forest-Fire.git
   cd Forest-Fire
   ```

2. **Instalar dependencias con uv:**
   ```bash
   uv sync
   ```

3. **Ejecutar migraciones de Django:**
   ```bash
   python manage.py migrate
   ```

4. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

5. **Acceder a la aplicación:**
   Abre tu navegador en `http://localhost:8000`

## 📖 Documentación de la API

### Endpoints Principales

- `GET /api/simulations/` - Listar todas las simulaciones
- `POST /api/simulations/` - Crear nueva simulación
- `GET /api/simulations/{id}/` - Obtener detalles de una simulación
- `POST /api/simulations/{id}/step/` - Ejecutar un paso de la simulación
- `POST /api/simulations/{id}/reset/` - Reiniciar la simulación
- `GET /api/weather/{city}/` - Obtener datos meteorológicos de Open-Meteo

## 🧪 Pruebas

Para ejecutar las pruebas unitarias:

```bash
python manage.py test
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios significativos:

1. Abre un issue para discutir los cambios propuestos.
2. Fork el repositorio.
3. Crea una rama para tu feature (`git checkout -b feature/mejora`).
4. Commit tus cambios (`git commit -m 'Añadir mejora'`).
5. Push a la rama (`git push origin feature/mejora`).
6. Abre un Pull Request.

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

## 👤 Autor

**rvssian666** - [GitHub Profile](https://github.com/rvssian666)

---

**Última actualización**: 2026-05-03 14:13:24