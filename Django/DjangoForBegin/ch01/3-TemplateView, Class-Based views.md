## TemplateView, Class-Based views

### Initil Set Up
```shell
mkdir pages; cd pages

pipenv install django==2.1.7
pipenv shell

django-admin startproject pages_project .
```

### Create an app
```shell
python manage.py startapp pages

vim helloworld_project/settings.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    ...
]
```

### Templates
```shell
mkdir templates/home.html
<h1>Homepage</h1>

vim pages_project/settings.py
TEMPLATES = [
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
]
```

### TemplateView, Class-Based views
```shell
vim pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
```

### URLs
```shell
vim pages_project/urls.py
from django.urls import path, include

urlpatterns = [

    path('', include('pages.urls")),
]

vim pages/urls.py
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```

