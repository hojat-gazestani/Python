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
  - [Tests](#Tests)
  - [BlogListView](#BlogListView)
  - [Static files](#Static-files)
  - [DetailView](#DetailView)
- [Blog app](#Blog-app)
  - []


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
![alt text](https://github.com/hojat-gazestani/Python/blob/main/Django/DjangoForBegin/Pic/2-posts-model.png)
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

## BlogListView

### Initial Set Up
```commandline
$ mkdir blog
$ cd blog
$ pipenv install django== .
$ pipenv shell
(blog) $ django-admin startproject blog_project .
(blog) $ python manage.py startapp blog
(blog) $ python manage.py migrate
(blog) $ python manage.py runserver
```

```commandline
# blog_project/settings.py
INSTALLED_APPS = [
    'blog.apps.BlogConfig', # new
    ...
    ]
```

### Database Models
```commandline
# blog/models.py
from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    
    def __str__(self):
        return self.title
```

```commandline
(blog) $ python manage.py makemigrations blog
(blog) $ python manage.py migrate blog
```

### Admin
```commandline
python manage.py createsuperuser
```

### show post
```commandline
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### urls
```commandline
# blog_project/urls.py
from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # new
]
```

### BlogListView
```commandline
# blog/urls.py
from django.urls import path
from .views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]
```

### view 
```commandline
# blog/views.py
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
```

### Templates
```commandline
(blog) $ mkdir templates
(blog) $ touch templates/base.html
(blog) $ touch templates/home.html
```

```commandline
# blog_project/settings.py
TEMPLATES = [
{
...
'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
...
},
]
```

```commandline
vim templates/base.html
{% load staticfiles %}

<html>
  <head>
      <title>Django blog</title>
  </head>
  <body>
    <div>
      <header>
          <h1><a href="{% url 'home' &}">Django blog</a> </h1>
      </header>
    {% block content %}
    {% endblock content %}
    </div>
  </body>
</html>
```

```commandline
vim templates/home.html
{% extends 'base.html' %}

{% block content %}
  {% for post in object_list %}
    <div class="post-entry">
        <h2><a href="">{{ post.title }}</a> </h2>
        <p>{{ post.body }}</p>
    </div>
  {% endfor %}
{% endblock content %}% 
```

### Static files
```commandline
(blog) $ mkdir -p static/css
(blog) $ vim static/css/base.css
/* static/css/base.css */
header h1 a {
color: red;
}
```

```commandline
# blog_project/settings.py
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

```commandline
<!-- templates/base.html -->
{% load static %}
<html>
<head>
<title>Django blog</title>
<link href="{% static 'css/base.css' %}" rel="stylesheet">
</head>
...
```

### more
```commandline
<!-- templates/base.html -->
{% load static %}
<html>
<head>
  <title>Django blog</title>
  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:rel="stylesheet">
  <link href="{% static 'css/base.css' %}" rel="stylesheet">
</head>
...
```

```commandline
vim static/css/base.css
body {
  font-family: 'Source Sans Pro', sans-serif;
  font-size: 18px;
}

header {
  border-bottom: 1px solid #999;
  margin-bottom: 2rem;
  display: flex;
}
header h1 a {
    color: red;
    text-decoration: none;
}

.nav-left {
  margin-right: auto;
}

.nav-right {
  display: flex;
  padding-top: 2rem;
}

.post-entry {
  margin-bottom: 2rem;
}

.post-entry h2{
  margin: 0.2rem 0;
}

.post-entry h2 a,
.post-entry h2 a: visited {
  color: blue;
  text-decoration: none;
}

.post-entry p {
  margin: 0;
  font-weight: 400;
}

.post-entry h2 a:hovar {
  color: red;
}

```
### DetailView
### Individual blog pages
```commandline
vim blog/views.py
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')%    
```

### 
```commandline
❯ cat templates/post_detail.html
<!-- templates/post_detail.html -->
{% extends 'base.html' %}

{% block content %}
  <div class="post-entry">
      <h2>{{ post.title }}</h2>
      <h2>{{ post.body }}</h2>
  </div>


  <p><a href="{% url 'post_edit' post.pk %}">+ Edit Blog Post</a></p>
  <p><a href="{% url 'post_delete' post.pk %}">+ Delete Blog Post</a></p>
{% endblock content %}% 
```

### url
```commandline
❯ cat blog/urls.py
from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path('post/<int:pk>/delete/',
         BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/',
         BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home')
]% 
```

```commandline
❯ cat templates/home.html
{% extends 'base.html' %}

{% block content %}
  {% for post in object_list %}
    <div class="post-entry">
        <h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a> </h2>
        <p>{{ post.body }}</p>
    </div>
  {% endfor %}
{% endblock content %}% 
```

### test
```commandline
❯ cat blog/tests.py
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateNotUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateNotUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new')), {
            'title' : 'New title',
            'body'  : 'New text',
            'author': self.user,
        }
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1')), {
            'titile' : 'Update title',
            'body'   : 'Update text',
        }
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.get(
            reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)
```


### todo
...
### todo


### Blog app

### Initial Set Up

### Add created app to django
* blog_project/settings.py

### Database Models
* blog/models.py

### initiate database
```commandline
(blog) $ python manage.py makemigrations blog
(blog) $ python manage.py migrate blog
```

### Admin
```commandline
(blog) $ python manage.py createsuperuser
```

### add post to admin page
* blog/admin.py

### Create post in web

### blog urls
* blog/urls.py

### project urls
* blog_project/urls.py

### ListView
```commandline
vim blog/views.py
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
  model = Post
  template_name = 'home.html'
```

### Templates
```commandline
(blog) $ mkdir templates
(blog) $ touch templates/base.html
(blog) $ touch templates/home.html
```

```commandline
# blog_project/settings.py
TEMPLATES = [
{
...
'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
...
},
]
```

```commandline
<!-- templates/base.html -->
<html>
  <head>
    <title>Django blog</title>
  </head>
  <body>
    <header>
      <h1><a href="{% url 'home' %}">Django blog</a></h1>
    </header>
    <div>
      {% block content %}
      {% endblock content %}
    </div>
  </body>
</html>
```

```commandline
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block content %}
  {% for post in object_list %}
    <div class="post-entry">
      <h2><a href="">{{ post.title }}</a></h2>
      <p>{{ post.body }}</p>
    </div>
  {% endfor %}
{% endblock content %}
```