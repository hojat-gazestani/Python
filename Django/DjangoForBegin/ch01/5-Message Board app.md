## Message Board app,

### Initil Set Up
```shell
mkdir mb; cd mb

pipenv install django==2.1.7
pipenv shell

django-admin startproject mb_project .
python manage.py startapp posts
```
### Create an app
```shell
python manage.py startapp pages

vim mb_project/settings.py
INSTALLED_APPS = [
    'posts.apps.PostsConfig',
    ...
]
```

### migrate to create database
```shell
python manage.py migrate
```

### Create a database model
```shell
vim posts/models.py
from django.db import models

class Post(models.Model):
    text = models.TextField()
```

### Activating models
```shell
python manage.py makemigrations posts
python manage.py migrate posts
```

### Django Admin
```shell
python manage.py createsuperuser
```

```python
vim posts/admin.py
from django.contrib import admin

from .models import Post

admin.site.register(Post)

```

### Add to database model
```python
vim posts/models.py
from django.db import models


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
```

### Views/Templates/URLs - ListView

#### Views
```python
vim posts/views.py
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
```

#### Templates
```shell
mkdir templates; touch templates/home.html

vim settings.py
TEMPLATES = [

        'DIRS': [os.path.join(BASE_DIR, 'templates')],
]

```html
vim templates/home.html
<h1>Message board homepage</h1>

<ul>
    {% for post in object_list %}
        <li>{{ post }}</li>
    {% endfor %}
</ul>
```

```python
vim posts/views.py
class HomePageView(ListView):

    context_object_name = 'all_posts_list'
    
vim templates/home.html
<h1>Message board homepage</h1>

<ul>
    {% for post in object_list %}
        <li>{{ post }}</li>
    {% endfor %}
</ul>
```

#### URLs
```python
vim mb_project/urls.py
urlpatterns = [
    path('', include('posts.urls')),
]

vim posts/urls.py
```



