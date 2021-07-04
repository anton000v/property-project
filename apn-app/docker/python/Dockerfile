FROM python:3.8

COPY ./requirements.txt /srv/www/apn-app/requirements.txt
WORKDIR /srv/www/apn-app
RUN pip3 install -r requirements.txt

COPY . /srv/www/apn-app
WORKDIR /srv/www/apn-app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
