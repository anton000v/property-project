FROM python:3.8

COPY . /srv/www/property-project
WORKDIR /srv/www/property-project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip3 install -r requirements.txt


# Now copy in our code, and run it
COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
