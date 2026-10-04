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

$ python manage.py runserver
#Starts running the server locally through a local address like http://127.0.0.1:8000/
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




For a database we edit the `models.py` file and make a class using `models.Model` as an input. From there we have a number of custom fields. In this example, I'm storying users and their login hashes.
```
class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=64)
```

We then go to `admin.py` and register the model with the admin pannel through
```
from .models import Users
admin.site.register(Users)
```

We now need to aply a migration.
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

In order to use this, we need to create some functionality to interact with it.
First we make a new page via a template, `users.html`.
Next we need a view (from `views.py`) to render that template.
```
from .models import Users
def users(request):
    items = Users.objects.all() 
    return render(request, "users.html", {"users": items})
```
Next we need to make a valid URL for this template to be displayed from (i.e. from `urls.py`).
```
        ...,
        path("users/", views.users, name="UserList")
        ]
```

And that's it. This should now be viewable.
To actually interact with this, we'll need the help of the admin pannel (provided by Django)
