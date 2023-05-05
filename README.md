# Camjaira Webserver
Pretty ok django project for school. 

## Backend Todo List
- [ ] Implement features
  - [x] Suggestion Box
    - [x] Implement posting
    - [x] Implement viewing
    - [x] Implement Result filtering
  - [ ] Appointment Rework
  - [ ] Review system
    - [x] Implement viewing
    - [x] Implement posting
    - [ ] Implement editing review
- [ ] Write Unittests for modelInterface
  - [x] Room
  - [ ] Appointment
  - [ ] Account
  - [ ] Reviews
  - [ ] Suggestions
- [ ] Miscellaneous
  - [ ] Clean Code
  - [ ] Make Code Robust
- [ ] Integrate front end

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

### Create an admin user
For this page -> localhost:8000/admin
```
python camjaira/manage.py createsuperuser
```

### Reset the database

```
python camjaira/manage.py flush
```

