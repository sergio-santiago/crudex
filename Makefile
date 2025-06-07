PYTHON := python3
DB_NAME ?= crudex.db

# Run the interactive console by default
.DEFAULT_GOAL := console


.PHONY: install-dependencies list add get update delete console purge

install-dependencies:
	$(PYTHON) -m pip install -r requirements.txt

list:
	$(PYTHON) app.py list

add:
	$(PYTHON) app.py add "$(NAME)" "$(EMAIL)"

get:
	$(PYTHON) app.py get $(ID)

update:
	$(PYTHON) app.py update $(ID) "$(NAME)" "$(EMAIL)"

delete:
	$(PYTHON) app.py delete $(ID)

console:
	$(PYTHON) console.py

purge:
	rm -f $(DB_NAME)
