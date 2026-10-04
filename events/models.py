from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=64)
    #SHA-256 responds a 64 character digest
