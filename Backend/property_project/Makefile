include .env

PROJECT_NAME=Core
BINARY_NAME=app

ps:
	docker-compose ps

down:
	docker-compose down

start:
	docker-compose start

stop:
	docker-compose stop

restart: stop start ps

build_:
	docker-compose build --no-cache

build:
	docker-compose build --no-cache

#dev_build:
#	docker-compose -f ./docker-compose.yml build --no-cache

up:
	docker-compose up -d

rebuild: down build up ps

showlogs:
	docker-compose logs -f --tail 100

bash:
	docker-compose exec python bash

runserver:
	docker-compose exec python python manage.py runserver 0.0.0.0:8000

collectstatic:
	docker-compose exec python python manage.py collectstatic

run: up runserver

django_shell:
	docker-compose exec python python manage.py shell

migrations:
	docker-compose exec python python manage.py makemigrations

migrate:
	docker-compose exec python python manage.py migrate

migrate_fake:
	docker-compose exec python python manage.py migrate --fake

migrate_auth:
	docker-compose exec python python manage.py migrate auth

migrations_auth:
	docker-compose exec python python manage.py makemigrations auth

migrate_userauth:
	docker-compose exec python python manage.py migrate user_auth

migrations_userauth:
	docker-compose exec python python manage.py makemigrations user_auth

migrations_sync:
	docker-compose exec python python manage.py makemigrations sync

migrate_sync:
	docker-compose exec python python manage.py migrate sync

init_db: migrate migrate_userauth migrations_sync migrate migrate_sync migrations_userauth migrate_userauth migrations createcachetable migrate

showmigrations:
	docker-compose exec python python manage.py showmigrations

test:
	docker-compose exec python python manage.py test

redis:
	docker-compose exec redis redis-cli

requirements:
	docker-compose exec python pip install -r requirements.txt

db_shell:
	docker-compose exec postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB}

c1:
	docker-compose exec postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB} -c "INSERT INTO django_migrations (app, name, applied) VALUES ('user_auth', '0001_initial', CURRENT_TIMESTAMP);"

c2:
	docker-compose exec postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB} -c "UPDATE django_content_type SET app_label = 'user_auth' WHERE app_label = 'auth' and model = 'user';"

drop_all_tables:
	docker-compose exec postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB} -c "DROP SCHEMA public CASCADE;"

create_schema:
	docker-compose exec postgres psql -U $(POSTGRES_USER) ${POSTGRES_DB} -c "CREATE SCHEMA public;"

clean_db: drop_all_tables create_schema

fix_user: c1 c2

# remove any existing containers
rm_containers:
	docker container rm -f $$(docker container ls -aq)

# run the app in dev configuration:
dev_named_up:
	docker-compose -f ./docker-compose.yml -p core-dev up -d

# check config for the production override:
check_dc_prod_config:
	docker-compose -f ./docker-compose.yml -f ./docker-compose-prod.yml config

hard_reload: rm_containers build up migrations fix_user migrate createsuperuser

load: build up makemigrations migrate createsuperuser

load_from_scratch: build up clean_db init_db migrate migrations

celery:
	docker-compose exec python celery -A config worker --loglevel=debug

celery_scheduler:
	docker-compose exec python celery -A config beat --loglevel=debug

nginx_conf:
	chmod +x docker/init-letsencrypt.sh

run_nginx_conf:
	sudo ./docker/init-letsencrypt.sh

dev_rm: rm_containers build dev_up clean_db init_db migrate migrate migrations migrate collectstatic createsuperuser

dev_up:
	docker-compose -f ./docker-compose.yml up -d

#dev_from_scratch: dev_build dev_up clean_db init_db migrate migrate migrations migrate collectstatic createsuperuser

up_v_3workers:
	docker-compose up -d --build --scale celery=3

# up_v_3workers:
	# docker-compose up -d --scale celery=3

# Insert allauth keys to db:
allauth_configure:
	docker-compose exec python python manage.py initial_allauth_configure

# Insert periodic sync with qb into db:
qb_celery_configure:
	docker-compose exec python python manage.py initial_celery_configure

# Full init configure
init_configure: allauth_configure qb_celery_configure

add_helper:
	docker-compose exec python python manage.py add_helper

createsuperuser:
	docker-compose exec python python manage.py create_superuser

ds_user:
	docker-compose exec python python manage.py create_ds_user

rebuild_db: clean_db init_db migrate migrations migrations migrate migrations migrate

httpbin:
	docker run -p 81:80 kennethreitz/httpbin

from_scratch: rm_containers nginx_conf build run_nginx_conf up clean_db init_db migrate migrate migrations createcachetable migrate collectstatic createsuperuser init_configure add_helper

scratch: nginx_conf build run_nginx_conf up clean_db init_db migrate migrate migrations createcachetable migrate collectstatic createsuperuser init_configure add_helper

dev_from_scratch: rm_containers build dev_up clean_db init_db migrate migrate migrations createcachetable migrate collectstatic createsuperuser init_configure add_helper

dev_scratch: build dev_up clean_db init_db migrate migrate migrations createcachetable migrate collectstatic createsuperuser init_configure add_helper

list_q:
	rabbitmqctl list_queues| grep cinder

tasks: bash list_q

prune_all:
	docker system prune -a

# For django cache framework
createcachetable:
	docker-compose exec python python manage.py createcachetable

monitor_log_file:
	tail -f -n 5 logs/log.log
