# Arquitectura general

## Backend
La aplicación está desarrollada con FastAPI para la gestión de pedidos.

## Persistencia
La base de datos utilizada es SQLite mediante el archivo `orders.db`.

## Ejecución local
La aplicación puede levantarse con Docker Compose y expone el servicio en el puerto 8000.

## Componentes principales
- `app/`: código principal de la aplicación
- `tests/`: pruebas del proyecto
- `scripts/`: scripts auxiliares
- `azure-pipelines.yml`: definición del pipeline CI/CD