## TemplateView, Class-Based views, Extending Templates

### Initil Set Up
```shell
mkdir pages; cd pages

pipenv install django==2.1.7
pipenv shell

django-admin startproject pages_project .
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

### Templates
```html
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
```python
vim pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
```

### URLs
```python
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
### Add an About Page
```html
vim templates/about.html
<h1>About page</h1>

vim pages/views.py
...
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
vim pages/urls.py
urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
] 
```

### Extending Templates
```html
vim templates/base.html
<header>
    <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
</header>

{% block content %}
{% endblock content %}

vim templates/home.html
{% extends 'base.html' %}

{% block content %}
<h1>Homepage</h1>
{% endblock content %}

vim templates/about.html
{% extends 'base.html' %}

{% block content %}
<h1>About page</h1>
{% endblock content %}
```
