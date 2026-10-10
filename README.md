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



To do this, we use the superuser command:
```
$ python manage.py createsuperuser
```
for my example i made the user danielw

Then run the server and go to http://127.0.0.1:8000/admin

Then you can see the default `Authentication and Authorization` groups and under it is `EVENTS` with `Userss` (yes double "s"). 
Click "add".
I'm going to make `test user 1` with password `b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9` ("hello world" sha-256)
And again make `test user 2` with password `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (empty input sha-256)

Now go back to http://127.0.0.1:8000/users/ and you can see the users being displayed


=====================================

Django has a login system built into it. It has a `Users` already so we can use that actually.
First we edit `config/settings.py` by adding these lines:
```
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"
```

Then we add this line to `config/urls.py`:
```
    ...
    path("", include("events.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    ]
    ...
```

We add a login html file at `events/templates/registration/login.html` which tells django automatically what this is for by making this file path.
Finally to `event/views.py` we add the following lines:
```
from django.contrib.auth.decorators import login_required
...
@login_required
def calendar(request):
    return render(request, "events/calendar.html")
```
