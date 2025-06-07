# crudex

Aplicación de línea de comandos para realizar operaciones CRUD utilizando PostgreSQL. Puedes ejecutarla de forma local con Python o mediante contenedores Docker.

## Requisitos

- Docker y Docker Compose
- Python 3 (solo si deseas ejecutar la aplicación sin Docker)

## Build y puesta en marcha del servicio

1. Construye la imagen de la aplicación y el contenedor de base de datos:

```bash
docker compose build
```

2. Inicia los servicios en segundo plano:

```bash
docker compose up -d
```

## Entrar al contenedor para ejecutar comandos

Abre un shell dentro del contenedor de la aplicación:

```bash
docker compose run --rm crudex bash
```

Dentro del contenedor puedes usar los siguientes comandos de ejemplo:

```bash
python app.py add "John Doe" "john@example.com"
python app.py list
python app.py update 1 "Jane Doe" "jane@example.com"
python app.py delete 1
```

## Ejecutar comandos sin entrar al contenedor

Si prefieres lanzar un comando directamente, utiliza `docker compose run`:

```bash
docker compose run --rm crudex list
```
