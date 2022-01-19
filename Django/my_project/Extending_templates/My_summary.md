### Base file that would be inherited by all other templates
```
<!-- ./my_project/templates/base.html ->>

<header>
        <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>
</header>

{% block content %}
<% endblock content %}
```

### home.html which is extend the base.html 
```
<!-- ./my_project/templates/home.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Homepage</h1>
{% endblock content %}
```

### about.html which is extended the base.html
```
<!-- ./my_project/templates/about.html -->
{% extends 'base.html' %}

{% block content %}
<h1>Aboutpage</h1>
{% endblock content %}
```
