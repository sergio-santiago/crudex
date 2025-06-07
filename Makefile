PYTHON := python3

.PHONY: install list add get update delete

install:
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

