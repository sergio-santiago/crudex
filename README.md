# Crudex
> 🧪 This project is experimental and intended for testing AI-assisted code generation using OpenAI Codex.  

## Description

`crudex` is a minimal command-line application for performing CRUD operations on a SQLite database.  
It is designed to be lightweight, dependency-free, and easy to understand — ideal for experimenting with code generation, prototyping, or educational use.

## Requirements

- Python 3.11 or higher  
- No external database server is required, it uses SQLite by default.

## Usage

You can run the application in two ways: via the provided `Makefile`, or by running the Python script manually.

### Using the Makefile

```bash
make list
make add NAME="Sergio Santiago" EMAIL="sergio@example.com"
make get ID=1
make update ID=1 NAME="Sandra Alonso" EMAIL="sandra@example.com"
make delete ID=1
```

## Running tests

Install the testing dependency:

```bash
python3 -m pip install -r requirements.txt
```

Run the suite with:

```bash
pytest -q
```
