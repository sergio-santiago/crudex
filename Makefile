PYTHON := python3
DB_PATH ?= crudex.db

# Run the interactive console by default
.DEFAULT_GOAL := console


.PHONY: install-dependencies list add get update delete console purge

install-dependencies:
	$(PYTHON) -m pip install -r requirements.txt

lint:
	$(PYTHON) -m black .
	$(PYTHON) -m ruff .

list:
	CRUDEX_DB=$(DB_PATH) $(PYTHON) app.py list

add:
	CRUDEX_DB=$(DB_PATH) $(PYTHON) app.py add "$(NAME)" "$(EMAIL)"

get:
	CRUDEX_DB=$(DB_PATH) $(PYTHON) app.py get $(ID)

update:
	CRUDEX_DB=$(DB_PATH) $(PYTHON) app.py update $(ID) "$(NAME)" "$(EMAIL)"

delete:
	CRUDEX_DB=$(DB_PATH) $(PYTHON) app.py delete $(ID)

console:
	CRUDEX_DB=$(DB_PATH) $(PYTHON) console.py

purge:
	rm -f $(DB_PATH)
