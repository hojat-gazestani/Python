## Create App, HttpResponse 

### Initil Set Up
```shell
mkdir helloworld; cd helloworld

pipenv install django==2.1.7
pipenv shell

django-admin startproject helloworld_project .

python manage.py runserver
```

### Create an app
```python
python manage.py startapp pages

vim helloworld_project/settings.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    ...
]
```
### Views and URLConfs
```python
vim pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')
```

```python
vim pages/urls.py
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
```

```python
vim helloworld_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```