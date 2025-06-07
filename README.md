# crudex

Simple command-line CRUD app using SQLite.

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

Run commands using the container (data will not persist between runs):

```bash
docker run --rm crudex add "John Doe" "john@example.com"
docker run --rm crudex list
```

To preserve the database, mount a volume:

```bash
docker volume create crudex_data
docker run --rm -v crudex_data:/app crudex add "Jane Doe" "jane@example.com"
docker run --rm -v crudex_data:/app crudex list
```

## Docker Compose

Para simplificar la ejecución y conservar la base de datos puedes usar
`docker-compose`. El servicio definido en `docker-compose.yml` monta un
volumen llamado `crudex_data` que contiene el archivo de la base de datos.

Construye y ejecuta comandos así:

```bash
docker compose run --rm crudex add "John Doe" "john@example.com"
docker compose run --rm crudex list
```
