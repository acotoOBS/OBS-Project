## Abiente Local

Para acceder localmente:

http://localhost:8000/docs#/

---

## Stack Tecnológico

- Backend: FastAPI (Python)
- Base de datos: SQLite
- CI/CD: Azure DevOps Pipelines
- Cloud: AWS Elastic Beanstalk + S3
- Calidad de código: flake8
- Empaquetado: archivo .zip

---

## Pipeline CI/CD

### Integración Continua (CI)

- Instalación de dependencias
- Validación de código con flake8
- Construcción del artefacto (zip)

### Despliegue Continuo (CD)

- Carga del artefacto a S3
- Creación de versión de aplicación en Elastic Beanstalk
- Despliegue utilizando AWS CLI

---

## Retos Encontrados y Soluciones

### Manejo de credenciales AWS en scripts

Problema:  
Los pasos tipo script no heredan credenciales configuradas en Azure DevOps.

Solución:  
Se utilizaron exclusivamente tareas AWSCLI@1 para todas las operaciones relacionadas con AWS.

---

### Environment en estado Terminated

Problema:  
Elastic Beanstalk puede retornar environments existentes en estado Terminated, los cuales no son válidos para despliegue.

Solución:  
Se implementó una estrategia idempotente:

- Intentar update-environment
- Si falla, ejecutar create-environment

---

### Solution Stacks deprecados

Problema:  
Algunas versiones de runtime no estaban disponibles en la región.

Solución:  
Se utilizó un stack válido confirmado en ejecución:
- Amazon Linux 2023
- Python 3.11

---

### Despliegue asíncrono

Problema:  
Elastic Beanstalk no garantiza disponibilidad inmediata después del despliegue.

Solución:  
El pipeline no depende del estado final del environment, alineándose con prácticas reales de despliegue.

---

### Limitaciones de Azure DevOps

Problema:  
No es posible evaluar directamente el output de tareas AWSCLI en condiciones.

Solución:  
Se utilizó el resultado de ejecución de tareas (success/failure) para controlar el flujo del pipeline.

---

## Decisiones DevOps

- Implementación de despliegues idempotentes
- Eliminación de scripts innecesarios para evitar problemas de credenciales
- Uso exclusivo de AWS CLI dentro del pipeline
- Priorización de resiliencia sobre validaciones rígidas

---

## Evolución de la Solución

### Contenedorización

- Dockerización de la aplicación
- Uso de Amazon ECR + ECS o EKS

---

### Orquestación

- Migración a Kubernetes (EKS)
- Implementación de autoescalado

---

### Infraestructura como Código

- AWS CloudFormation
- Terraform

---

### Observabilidad

- Prometheus (métricas)
- Grafana (visualización)
- Loki (logs)
- Tempo (trazabilidad)

---

### Evolución Arquitectónica

- Arquitectura SaaS multi-tenant
- Integración con servicios DaaS

---

## Acceso a la API

Una vez desplegada, la API está disponible en:

http://<elastic-beanstalk-url>/docs

---

## Nota Final

Esta solución no solo cumple con los requerimientos funcionales, sino que incorpora prácticas reales de DevOps, considerando:

- estados inconsistentes de infraestructura
- errores en tiempo de ejecución
- resiliencia del pipeline
- automatización completa del ciclo de despliegue