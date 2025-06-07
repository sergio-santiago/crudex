# crudex

Simple command-line CRUD app using PostgreSQL.

## Requirements

- Python 3

## Usage

Initialize the database and add a new entry:

```bash
python app.py add "John Doe" "john@example.com"
```

List all entries:

```bash
python app.py list
```

Update an entry by id:

```bash
python app.py update 1 "Jane Doe" "jane@example.com"
```

Delete an entry by id:

```bash
python app.py delete 1
```

## Docker

If you don't have Python installed, you can run the application in a container.

Build the image:

```bash
docker build -t crudex .
```

This image is intended to run together with a PostgreSQL container defined in
`docker-compose.yml`.

## Docker Compose

Para ejecutar la aplicación y la base de datos utiliza `docker compose`.
El archivo `docker-compose.yml` define un servicio `db` con PostgreSQL y el
servicio de la aplicación que se conecta a dicho contenedor.

Construye y ejecuta comandos así:

```bash
docker compose build
docker compose run --rm crudex add "John Doe" "john@example.com"
docker compose run --rm crudex list
```
