PYTHON := python3

# Run the interactive console by default
.DEFAULT_GOAL := console


.PHONY: install-dependencies list add get update delete console

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

