Django for Beginners
====================

- [Initial setup](#Initial-setup)
  - [Virtual Environments](#Virtual-Environments)
  - [Create an app](#Create an app)
  - [Django Architecture](#Django-Architecture)


## Initial setup

### Virtual Environments
```commandline
pip3 install pipenv

mkdir django
cd django

pipenv install django==2.1.7
pipenv shell

django-admin startproject test_project .
python manage.py runserver
```

### Create an app
```commandline
python manage.py startapp pages
```
* admin.py is a configuration file for the built-in Django Admin app
* apps.py is a configuration file for the app itself
* migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync
* models.py is where we define our database models, which Django automatically
* tests.py is for our app-specific tests
* views.py is where we handle the request/response logic for our web app translates into database tables

### Add Created app
* Django doesn’t “know” about it until Add our new pages app at the top:
````commandline
# helloworld_project/settings.py
INSTALLED_APPS = [
'pages.apps.PagesConfig', 
...
]
````

### Django Architecture

![alt text](https://github.com/hojat-gazestani/Python/blob/main/Django/DjangoForBegin/Pic/1-Django-arch.png)

### Views and URLConfs