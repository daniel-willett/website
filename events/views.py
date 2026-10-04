from django.shortcuts import render, HttpResponse
from .models import Users

# Create your views here.
def home(request):
    return render(request, "home.html")

def users(request):
    items = Users.objects.all()
    return render(request, "users.html", {"users": items})

