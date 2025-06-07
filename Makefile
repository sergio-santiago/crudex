DC = docker compose

.PHONY: build up down clean shell add list update delete

build:
	$(DC) build

up:
	$(DC) up -d

down:
	$(DC) down

clean:
	$(DC) down -v

shell:
	$(DC) run --rm --entrypoint bash crudex

list:
	$(DC) run --rm crudex list

add:
	$(DC) run --rm crudex add "$(NAME)" "$(EMAIL)"

update:
	$(DC) run --rm crudex update $(ID) "$(NAME)" "$(EMAIL)"

delete:
	$(DC) run --rm crudex delete $(ID)

