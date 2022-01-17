### Virtual Environment
```commandline
cd my_project
pipenv install django==2.1
pipenv shell
django-admin startproject my_project .
python manage.py startapp TemplateView_pages
vim my_project/settings.py
```

### Add the 'TemplateView_pages' to project
```commandline
INSTALLED_APPS = [
    'TemplateView_pages.apps.TemplateviewPagesConfig',
    ...
]
```

### Create Template directory and html files
```commandline
mkdir TemplateView_pages/templates
vim TemplateView_pages/templates/home.html
<h1>Homepage</h1>
```

### Tell Django to look at the project-level for template
```commandline
TEMPLATES = [
    {
        ...
        'DIR': [os.path.join(BASE_DIR, 'template')],
        ...
    }
]
```

### Use The TemplateView to display our template.
```commandline
from django.views.generic import TemplateView

class HomePageView(templateView):
    template_name = 'home.html'
```
### In the project-level urls.py file point at our TemplateView_pages app
```commandline
from django.urls import include

urlpatterns = [
    ...
    path('', include('TemplateView_pages.urls')),
]
```

### Within TemplateView_pages urls.py math the views to routes
```commandline
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
```

