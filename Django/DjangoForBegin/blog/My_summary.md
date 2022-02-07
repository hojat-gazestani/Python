Blog project
============

### Create new BLOG project
```
mkdir blog
cd blog

pipenv install django==3.1
pipenv shell

django-admin startproject blog_project .
python manage.py startapp blog
python manage.py migrate 
python manage.py runserver
```
### Add posts BLOG to the top of INSTALLED_APP
```
vim mb_project/settings.py 
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    ...
]
```

### Create database model
post has a:
title : limit the length to 200 char
author: ForeignKey which allows for a many-to-one relationship
    (- A given user can be the author of many different blog post
    , But not the other way around.
    - The reference is to the to the built-in User model that djanog provide for authentication.
    - For many-to-one relationships such as a ForeignKey we must also specify an on_delete option.)
body  : automatically expand as needed
```
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

### Create a new migration record and migrate
```
python manage.py makemigrations blog
python manage.py migrate blog
```

### Create a super user to have access to our data
```
python manage.py createsuperuser
```

### Show Post in admin page
```
from .models import Post

admin.site.register(Post)
```

Display our blog posts on the homepage
--------------------------------------

### Configure our app-level URLConfs
```
vim blog/urls.py
from django.urls import path
from .views import BlogListView

urlpatterns = [ 
    path('', BlogListView.as_view(), name='home'),
```

### Update our project level URL
```commandline
vim blog_project/urls.py
urlpatterns = [
    ...
    path('', include('blog.urls'))
]

```

### Display our Post model using ListView
```commandline
from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
```

### Project level template
```commandline
mkdir templates
touch templates/base.html
touch templates/home.html
```

### Update Django settings to know where look for templates
```commandline
vim blog_project/settings.py
...
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

### Update base template
```commandline
vim templates/base.html 
{% load staticfiles %}

<html>
  <head>
      <title>Django blog</title>
      <link href="https://fonts.googleapis.com/css?family=Source+Sans+pro:400" rel="stylesheet">
      <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  <body>
    <header>
        <h1><a href="{% url 'home' &}">Django blog</a> </h1>
    </header>
    <div>
        {% block content %}
        {% endblock content %}
    </div>
  </body>
</html>
```

### Update home templte
```commandline
{% extends 'base.html' %}

{% block content %}
  {% for post in object_list %}
    <div>
        <h2><a href="">{{ post.title }}</a> </h2>
        <p>{{ post.body }}</p>
    </div>
  {% endfor %}
{% endblock content %}
```

Static file
-----------

### Project level directory for static file
```commandline
mkdir -p static/css
```

### Change the title to be red
```commandline
header h1 a {
    color: red;
    text-decoration: none;
}
```

### Add static files to our template
```commandline
vim templates/base.html
{% load staticfiles %}

<html>
  <head>
      <title>Django blog</title>
      <link href="{% static 'css/base.css' %}" rel="stylesheet">
  </head>
  ...

```

### Add a costume fonts
```commandline
{% load staticfiles %}

<html>
  <head>
      ...
      <link href="https://fonts.googleapis.com/css?family=Source+Sans+pro:400" rel="stylesheet">
      ...
  </head>
  ...
</html>

```

### update our CSS file
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
```

individual blog pages
---------------------
Create new view, url and template

### DetailView
Detail view provide a context object we can use in out template
called either object or the lowercase name.
expect either a primary key or a slug passed to it as the identifier.
```commandline
vim blog/views.py
from ... import DetailView

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
```

### template for post detail
```commandline
vim templates/post_detail.html
{% extends 'base.html' %}

{% block content %}
  <div class="post-entry">
      <h2>{{ object.title }}</h2>
      <h2>{{ object.body }}</h2>
  </div>
{% endblock content %}
```

### Add new URLconf for our view
All blog post entries will start with post 
next is primary key for out post whih is added automatically by Django
```commandline
vim blog/views.py
from .views import BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail')
    ...
]
```

### update home page
Directly access to individual blog posts
```commandline
vim templates/home.html
{% extends 'base.html' %}

{% block content %}
  ...
    <div class="post-entry">
        <h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a> </h2>
        ...
    ...
  ...
{% endblock content %}
```