from pyexpat import model
from django.db import models

# Create your models here.
#1 py manage.py makemigrations // step prepare model
#2 py manage.py migrate // step migrate model to db sqlite
class User(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    pname = models.CharField(max_length=3)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.CharField(max_length=80)
    phone = models.IntegerField(16)
    countrycode = models.IntegerField(4)
    image = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    lastvisit = models.CharField(max_length=40)