# crudex

Aplicaci\xc3\xb3n de l\xc3\xadnea de comandos para realizar operaciones CRUD utilizando SQLite.

## Requisitos

- Python 3.11 o superior
- No se requiere un servidor de base de datos externo; se utiliza SQLite por defecto

## Instalaci\xc3\xb3n

No se requieren dependencias externas; el archivo `requirements.txt` se mantiene vacio para futuras extensiones.

## Uso del Makefile

Las tareas del `Makefile` permiten ejecutar los comandos de la aplicaci\xc3\xb3n sin necesidad de Docker.

```bash
make list                                # Ejecuta `python app.py list`
make add NAME="John Doe" EMAIL="john@example.com"
make update ID=1 NAME="Jane Doe" EMAIL="jane@example.com"
make delete ID=1
```

Tambi\xc3\xa9n puedes ejecutar los comandos de manera directa:

```bash
python app.py list
python app.py add "John Doe" "john@example.com"
python app.py update 1 "Jane Doe" "jane@example.com"
python app.py delete 1
```
