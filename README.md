This is a website made in python with django.

For self: 

Apparently need to source with the following?
```
source .venv/bin/activate
```

django has some built in funtions that can be useful:
```
$ django-admin startproject <project-name>
#Creates a boilerplate django project

$ python manage.py startapp <app-name>
#Creats app folder and files

$ python manage.py makemigrations
#Preps our database for migrations

$ python manage.py migrate
#Executes our migrations & updates the database

$ python manage.py createsuperuser
#Creates a user with admin level permissions
```


To make a template (which is a dynamic, reusable HTML file) we make a dir in the app (e.g. `events/templates`) and a `base.html` inside that to be a basic template other pages will use.
From there we can use the Jinja templating engine.

Inside `base.html` we put a line saying 
```
<div class="container">{% block content %} {% endblock %}</div>
```
which allows for this base html structure to be copyable to other html templates.

Making `home.html` we can see this by adding the lines
```
{% extends "base.html" %} {% block title %} Home Page {% endblock %}
{% block content %}
<p>this is the home page</p>
{% endblock %}
```
What this does is overwrite the `title` and the `content` blocks.
