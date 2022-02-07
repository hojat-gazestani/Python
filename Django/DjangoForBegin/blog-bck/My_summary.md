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