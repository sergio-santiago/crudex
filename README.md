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
