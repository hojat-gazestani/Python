Django for Beginners
====================

- [Initial setup](#Initial-setup)
  - [Virtual Environments](#Virtual-Environments)
  - [Create an app](#Create-an-app)
  - [Django Architecture](#Django-Architecture)
  - [Views and URLConfs](#Views-and-URLConfs)
  - [Templates](#Templates)
  - [TemplateView](#TemplateView)
  - [Extending Templates](#Extending-Templates)
  - [Test](#Test)
- [database model](#database-model)
  - [Create a database model](#Create-a-database-model)
  - [ListView](#ListView)


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
* Views
 ```commandline
# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')
```

* URLs
```commandline
# pages/urls.py
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]
```

* Admin URL
```commandline
# helloworld_project/urls.py

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    ...
]
```

### Templates
* create a new templates directory
```commandline
mkdir -p pages/templates/pages/

vim templates/home.html
<!-- templates/home.html -->
<h1>Homepage</h1>

vim templates/about.html
<!-- templates/about.html -->
<h1>About page</h1>
```

* tell Django to look at the project-level for templates.
```commandline
# pages_project/settings.py

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
        ...
    },
]
```

### TemplateView
* use TemplateView to display our template
```commandline
# pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
```


```commandline
# pages/urls.py
from .views import HomePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
```

### Extending Templates
```commandline
vim templates/base.html
<!-- templates/base.html -->
<header>
  <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
</header>

{% block content %}
{% endblock content %}
```

* home
```commandline
<!-- templates/home.html -->

{% extends 'base.html' %}
{% block content %}
<h1>Homepage</h1>
{% endblock content %}
```

* about
```commandline
<!-- templates/about.html -->

{% extends 'base.html' %}
{% block content %}
<h1>About page</h1>
{% endblock content %}
```

### Test
```commandline
# pages/tests.py
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        
python manage.py test
```

## database model

### Create a database model
* a database model where we can store and display posts from our users.
```commandline
# posts/models.py
from django.db import models

class Post(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text[:50]
```

### Activating models

* Create iniial database
```commandline
python manage.py migrate
```

* makemigrations: generate the SQL commands for preinstalled apps
* migrate: build the actual database, does execute the instructions in our migrations file
```commandline
python manage.py makemigrations posts
python manage.py migrate posts
```

### Django Admin
```commandline
python manage.py createsuperuser
```

### display post in the admin.
```commandline
# posts/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Views/Templates/URLs
![alt text]()
### ListView
```commandline
# posts/views.py

from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
```

### template
```commandline
<!-- templates/home.html -->

<h1>Message board homepage</h1>
<ul>
    {% for post in object_list %}
        <li>{{ post }}</li>
    {% endfor %}
</ul>
```

### urls
```commandline
# posts/urls.py

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```

### Tests
```commandline
# posts/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='just a test')
        
    def test_text_content(self):
        post=Post.objects.get(id= )
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')
        
class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
        
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200 )
        self.assertTemplateUsed(resp, 'home.html')
      
python manage.py test
```

