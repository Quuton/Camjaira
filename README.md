# Camjaira Webserver
Pretty ok django project for school. 

## Setup
Before you can use the camjaira webserver, you need the following things.

1. Python 3.11 or newer
2. Django and pillow libraries

You can use `pip install Django, pillow` to install into your venv.

## Basic usage
Once the setup is done, you can use it rightaway

### Run locally

```
python camjaira/manage.py runserver
```

### Run on the local network(use your phone to view)

```
python camjaira/manage.py runserver 0.0.0.0:8000
```

### Reset the database

```
python camjaira/manage.py flush
```

### Create a superuser

```
python camjaira/manage.py createsuperuser
```
