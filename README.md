# crudex

Aplicación de línea de comandos para realizar operaciones CRUD utilizando PostgreSQL.

## Requisitos

- Docker y Docker Compose

## Uso del Makefile

Utiliza las tareas definidas en el `Makefile` para construir la imagen y ejecutar los comandos de la aplicación.

```bash
make build                # Construye las imágenes
make up                   # Inicia los servicios en segundo plano
make down                 # Detiene y elimina los contenedores
make clean                # Elimina contenedores y volúmenes
make shell                # Abre un shell dentro del contenedor
make list                 # Ejecuta `python app.py list`
make add NAME="John Doe" EMAIL="john@example.com"
make update ID=1 NAME="Jane Doe" EMAIL="jane@example.com"
make delete ID=1
```
