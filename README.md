# Django Project Demos
- django version 2.1.2

# helloworld project
- basic intro on django project with simple views and urls

## instructions:
- clone the repo
- cd helloworld
- pipenv install
- pipenv shell
- ./manage.py migrate
- ./manage.py createsuperuser
- ./manage.py runserver
- point your browser to localhost:8000


# bookstorev1 project
- simple django project that uses templates, static files/css, etc.

## instructions:
- clone the repo
- cd bookstorev1
- pipenv install
- pipenv shell
- ./manage.py migrate
- ./manage.py createsuperuser
- ./manage.py runserver
- point your browser to localhost:8000

# bookstorev2 project
- upgrade to v1
- uses bootstraps and models

## instructions:
- clone the repo
- cd bookstorev2
- pipenv install
- pipenv shell
- ./manage.py makemigrations
- ./manage.py migrate
- provided DB has two superusers: 
    admin:P@$sw0rd!
    user:user
- ./manage.py createsuperuser
- ./manage.py runserver
- point your browser to localhost:8000
 
