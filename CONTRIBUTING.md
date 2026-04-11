# Guía de Contribución - OBS Package Tracking API

¡Gracias por tu interés en contribuir al proyecto! Esta guía proporciona instrucciones claras para colaborar de manera efectiva.

---

## Requisitos Previos

- Docker Desktop instalado
- Git instalado
- Python 3.11+ (si deseas trabajar localmente sin Docker)
- Conocimiento básico de Git y FastAPI

---

## Setup Inicial

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/acotoOBS/OBS-Project.git
   cd OBS-Project

---

## Estructura del Proyecto y Dónde Contribuir


**Dónde agregar diferentes tipos de cambios:**
- Nuevo endpoint → `routes/` + test en `tests/`
- Nueva tabla/modelo → `models/` + schema en `schemas/`
- Lógica compleja → `services/`
- Utilidades reutilizables → `utils/`

---

## Configuración del IDE - VS Code

### Configurar debugging
Crea `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/app/main.py",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}