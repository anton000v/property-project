include .env # Common env file
include .dev.env # Switch for dev/prod

#PROJECT_NAME=Core
#BINARY_NAME=app

DOCKER_COMPOSE_PATH := -f $(DOCKER_COMPOSE_FILE)
PYTHON_CONTAINER := apn-app
VUEJS_CONTAINER := apn-ui


ps:
	docker-compose $(DOCKER_COMPOSE_PATH) ps

down:
	docker-compose $(DOCKER_COMPOSE_PATH) down

start:
	docker-compose $(DOCKER_COMPOSE_PATH) start

stop:
	docker-compose $(DOCKER_COMPOSE_PATH) stop

restart: stop start ps

build:
	docker-compose $(DOCKER_COMPOSE_PATH) build --no-cache

up:
	docker-compose $(DOCKER_COMPOSE_PATH) up -d

rebuild: down build up ps

showlogs:
	docker-compose $(DOCKER_COMPOSE_PATH) logs -f --tail 100

show-python-logs:
	docker-compose $(DOCKER_COMPOSE_PATH) logs -f --tail 100 $(PYTHON_CONTAINER)

bash:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) bash

runserver:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py runserver 0.0.0.0:8000

collectstatic:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py collectstatic

run: up runserver

django_shell:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py shell

migrations_api:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py makemigrations api

migrations:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py makemigrations

migrate:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py migrate

migrate_fake:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py migrate --fake

migrate_auth:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py migrate auth

migrations_auth:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py makemigrations auth

drop_all_tables:
	docker-compose $(DOCKER_COMPOSE_PATH) exec apn-postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB} -c "DROP SCHEMA public CASCADE;"

create_schema:
	docker-compose $(DOCKER_COMPOSE_PATH) exec apn-postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB} -c "CREATE SCHEMA public;"

clean_db: drop_all_tables create_schema

init_db: migrate migrations_api migrate

showmigrations:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py showmigrations

test:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py test

install_requirements:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) pip install -r requirements.txt

db_shell:
	docker-compose $(DOCKER_COMPOSE_PATH) exec postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB}

create_frontend_user:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py create_frontend_user

createsuperuser:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py create_superuser

fill_administrative_districts_todb:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py fill_administrative_districts_todb

fill_streets_todb:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(PYTHON_CONTAINER) python manage.py fill_streets_todb

main_app_configure: createsuperuser create_frontend_user fill_administrative_districts_todb fill_streets_todb

frontbuild:
	docker-compose $(DOCKER_COMPOSE_PATH) exec $(VUEJS_CONTAINER) npm run build

letsenrypt_conf:
	chmod +x docker/init-letsencrypt.sh

letsenrypt:
	sudo ./docker/init-letsencrypt.sh


from_scratch: letsenrypt_conf build letsenrypt up migrate collectstatic main_app_configure
