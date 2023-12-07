import argparse
import docker
import subprocess

def list_containers(client, all_containers=False):
    for container in client.containers.list(all=all_containers):
        print(f"ID: {container.id}, Nombre: {container.name}, Estado: {container.status}")

def start_container(client, container_name):
    container = client.containers.get(container_name)
    container.start()
    print(f"Contenedor {container_name} iniciado.")

def stop_container(client, container_name):
    container = client.containers.get(container_name)
    container.stop()
    print(f"Contenedor {container_name} detenido.")

def remove_container(client, container_name):
    container = client.containers.get(container_name)
    container.remove()
    print(f"Contenedor {container_name} eliminado.")

def view_logs(client, container_name):
    container = client.containers.get(container_name)
    logs = container.logs()
    print(logs.decode())

def docker_compose_command(compose_file, command):
    result = subprocess.run(["docker-compose", "-f", compose_file, command], capture_output=True)
    if result.stderr:
        print(result.stderr.decode())
    else:
        print(result.stdout.decode())

parser = argparse.ArgumentParser(description="Gestor de Docker y Docker Compose")
parser.add_argument('--list', action='store_true', help='Lista todos los contenedores')
parser.add_argument('--start', help='Iniciar un contenedor')
parser.add_argument('--stop', help='Detener un contenedor')
parser.add_argument('--remove', help='Eliminar un contenedor')
parser.add_argument('--logs', help='Ver logs de un contenedor')
parser.add_argument('--compose-file', help='Archivo Docker Compose')
parser.add_argument('--compose-up', action='store_true', help='Iniciar servicios con Docker Compose')
parser.add_argument('--compose-down', action='store_true', help='Detener servicios con Docker Compose')

args = parser.parse_args()
client = docker.from_env()

if args.list:
    list_containers(client, True)
elif args.start:
    start_container(client, args.start)
elif args.stop:
    stop_container(client, args.stop)
elif args.remove:
    remove_container(client, args.remove)
elif args.logs:
    view_logs(client, args.logs)
elif args.compose_file:
    if args.compose_up:
        docker_compose_command(args.compose_file, "up -d")
    elif args.compose_down:
        docker_compose_command(args.compose_file, "down")
else:
    parser.print_help()
