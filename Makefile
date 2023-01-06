WEB_CONTAINER_NAME := $(shell docker ps --format "{{.Names}}" | grep crawler_web_server)

.PHONY: init
init:
	cp .env.copy .env
	@echo "Please change variables in .env file if it need!"

.PHONY: migrate
migrate:
	docker exec -it $(WEB_CONTAINER_NAME) python3 ./src/manage.py makemigrations
	docker exec -it $(WEB_CONTAINER_NAME) python3 ./src/manage.py migrate

.PHONY: create-superuser
create-superuser:
	docker exec -it $(WEB_CONTAINER_NAME) python3 ./src/manage.py createsuperuser
