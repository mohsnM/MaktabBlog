# SimpleBlog
A project that wrote with django and js

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

![alt text](https://imagizer.imageshack.com/img923/2043/3r81cH.png)

# core based on:
  - Python 3.8 version
  - Django 3.1 version

# Technologies are used:
  - Celery
  - REST api
  - Forms
  - Crispy
  - Django jet

# Some issue that handel in this blog: ### 
   - Register by email and active link
   - Simple panel for manage your account
   - Authenticate 

# How to run it?

### install dependencies:

create virtualenv

    python3.8 -m venv venv

active virtualenv

    source venv/bin/activate

install packages

    pip install -r requirements/local.txt

    pip install -r requirements/production.txt

migrate migrations on db

    python manage.py migrate

run server

    python manage.py runserver

    python manage.py runserver 0.0.0.0:8000
