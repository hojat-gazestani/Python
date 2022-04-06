## Create Virtual envierment, Install and run Django
```shell
mkdir django; cd django

pipenv install django==2.1.7
pipenv shell

django-admin startproject test_project .

python manage.py runserver
```