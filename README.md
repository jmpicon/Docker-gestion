
# Gestor de Docker y Docker Compose

Este proyecto es una herramienta de línea de comandos para gestionar Docker y Docker Compose, permitiendo realizar operaciones comunes como listar, iniciar, detener y eliminar contenedores, además de manejar servicios definidos en archivos Docker Compose.

## Características

- Listar todos los contenedores Docker (activos y detenidos).
- Iniciar y detener contenedores Docker.
- Eliminar contenedores Docker.
- Ver los logs de los contenedores.
- Iniciar y detener servicios definidos en archivos `docker-compose.yml`.

## Requisitos Previos

Antes de comenzar, asegúrese de tener instalado lo siguiente:

- Python 3.6 o superior.
- Docker y Docker Compose.
- Biblioteca de Docker para Python, que se puede instalar con `pip install docker`.

## Instalación

Clone este repositorio en su máquina local utilizando el siguiente comando:

```bash
git clone [URL del Repositorio]
```

## Uso

Una vez clonado el repositorio, puede utilizar la herramienta con el siguiente formato:

```bash
python gestor_docker.py [argumento]
```

Los argumentos disponibles son:

- `--list`: Lista todos los contenedores Docker.
- `--start [nombre_contenedor]`: Inicia un contenedor Docker específico.
- `--stop [nombre_contenedor]`: Detiene un contenedor Docker específico.
- `--remove [nombre_contenedor]`: Elimina un contenedor Docker específico.
- `--logs [nombre_contenedor]`: Muestra los logs de un contenedor Docker específico.
- `--compose-file [ruta_docker-compose.yml]`: Especifica el archivo Docker Compose a utilizar.
- `--compose-up`: Inicia los servicios definidos en el archivo Docker Compose especificado.
- `--compose-down`: Detiene los servicios definidos en el archivo Docker Compose especificado.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si desea contribuir, por favor fork el repositorio y utilice una nueva rama para sus contribuciones.

