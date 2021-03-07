include .env # Common env file
include .dev.env # Switch for dev/prod

#PROJECT_NAME=Core
#BINARY_NAME=app

DOCKER_COMPOSE_PATH := -f $(DOCKER_COMPOSE_FILE)


ps:
	docker-compose $(DOCKER_COMPOSE_PATH) ps

down:
	docker-compose $(DOCKER_COMPOSE_PATH) down

start:
	docker-compose $(DOCKER_COMPOSE_PATH) start

stop:
	docker-compose $(DOCKER_COMPOSE_PATH) stop

restart: stop start ps

build_:
	docker-compose $(DOCKER_COMPOSE_PATH) build --no-cache

build:
	docker-compose $(DOCKER_COMPOSE_PATH) build --no-cache

up:
	docker-compose $(DOCKER_COMPOSE_PATH) up -d

rebuild: down build up ps

showlogs:
	docker-compose $(DOCKER_COMPOSE_PATH) logs -f --tail 100

bash:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python bash

runserver:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py runserver 0.0.0.0:8000

collectstatic:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py collectstatic

run: up runserver

django_shell:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py shell

migrations:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py makemigrations

migrate:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py migrate

migrate_fake:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py migrate --fake

migrate_auth:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py migrate auth

migrations_auth:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py makemigrations auth

migrations_api:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py makemigrations api

init_db: migrate migrations_api migrate

showmigrations:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py showmigrations

test:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python python manage.py test

install_requirements:
	docker-compose $(DOCKER_COMPOSE_PATH) exec python pip install -r requirements.txt

db_shell:
	docker-compose $(DOCKER_COMPOSE_PATH) exec postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB}

showlogs:
	docker-compose $(DOCKER_COMPOSE_PATH) logs -f --tail 100
