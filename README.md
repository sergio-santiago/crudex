# Crudex
> 🧪 This project is experimental and intended for testing AI-assisted code generation using OpenAI Codex.  

## Description

`crudex` is a minimal command-line application for performing CRUD operations on a SQLite database.
It is designed to be lightweight and easy to understand — ideal for experimenting with code generation, prototyping, or educational use.

## Requirements

- Python 3.11 or higher  
- No external database server is required, it uses SQLite by default.

## Usage

You can run the application via the provided `Makefile`. Simply running `make`
will launch the interactive console.

```bash
make console
make purge
```

### CRUD

```bash
make list
make add NAME="Sergio Santiago" EMAIL="sergio@example.com"
make get ID=1
make update ID=1 NAME="Sandra Alonso" EMAIL="sandra@example.com"
make delete ID=1
```

### Configuration

The application stores its data in a SQLite file. By default the file is
`crudex.db`, but you can override the location using the environment variable
`CRUDEX_DB` or by creating a small JSON file:

```json
{ "db_path": "/tmp/mydb.sqlite" }
```

Then run with `CRUDEX_CONFIG=path/to/file.json`.


## Running tests

Install the testing dependency (also available via `make install-dependencies`):

```bash
python3 -m pip install -r requirements.txt
```

Run the suite with:

```bash
pytest -q
```

## Contributing

1. Create a virtual environment and install dependencies with `pip install -r requirements.txt`.
2. Format your code using `black` and run `ruff` for linting.
3. Execute the test suite with `pytest` to ensure everything works as expected.
