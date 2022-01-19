### Virtual evirenment
```
cd mb
pepenv install django==2.1.5
pipenv shell
django-admin startproject mb_project .
python manage.py startapp posts
```

### Add posts app to the top of INSTALLED_APP
```
vim mb_project/settings.py 
INSTALLED_APPS = [
    'posts.apps.PostsConfig',
    ...
]
```

### Create an initial database
```
python manage.py migrate
```

### Create database model
```
vim posts/models.py
class Post(models.Model):
    text = models.TextField()

```

### Activating Models
```
python manage.py makemigrations posts 
python manage.py migrate posts
```

### Create superuser
```
python manage.py createsuperuser 
```

### Display posts in admin page
```
vim posts/admin.py
from .models import Post

admin.site.register(Post)
```

### Create a message board post in web interface

### Display first 50 characters of the text field.
```
vim posts/models.py
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
```

### Display our database content on our homepage
```
vim posts/views.py
from .models import Post
from django.views.generic import ListView

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
```

### Create project-level directory
```
mkdir templates
touch templates/home.html
```

### Tell Djanjo the location of template directory
```
vim mb_project/settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    }
]
```

### Use loop to list all objects in object_list (object_list is the name of variable that ListView returns
```
vim templates/home.html
<!-- templates/home.html -->
<h1>Message board homepage</h1>
<ul>
  {% for post in object_list %}
    <li>{{ post }}</li>
  {% endfor %}
</ul>
```

### 
```
vim posts/views.py
class HomePageView(ListView):
    …
    context_object_name = 'all_posts_list'
```

### Use Django Templating Language for loop to list all objects in object_list.
object_list is the name of variable that ListView return
```
vim templates/home.html
<h1>Message board homepage</h1>
<ul>
  {% for post in all_object_list %}
    <li>{{ post }}</li>
  {% endfor %}
</ul>
```

### Set up URLConfs
```
vim mb_project/urls.py
urlpatterns = [
    …
    path('', include('posts.urls')),
]
```

### Create URL conf
```
vim posts/urls.py
from django.urls import path

from .views import HomePageView

urlpatterns = [ 
    path('', HomePageView.as_view(), name='home'),

```
