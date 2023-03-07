# Camjaira Webserver
Pretty ok django project for school

## Setup
Before you can use the camjaira webserver, you need the following things.

1. Python 3.11 or newer
2. A venv with django and pillow libraries

## BASIC USAGE
Once the setup is done, you can use it rightaway
## BASIC USAGE
Once the setup is done, you can use it rightaway

### RUN LOCALLY ON MACHINE

```
python camjaira/manage.py runserver
```

### RUN ON LOCAL NETWORK

```
python camjaira/manage.py runserver 0.0.0.0:8000
```

### RESET THE DATABASE

```
python camjaira/manage.py flush
```

### CREATE ADMIN ACCOUNT

```
python camjaira/manage.py createsuperuser
```
