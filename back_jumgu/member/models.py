# from pyexpat import model
from django.db import models
import uuid

# 1 py manage.py makemigrations // step prepare model
# 2 py manage.py migrate // step migrate model to db sqlite

# Create your models here.


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=40, null=True, blank=True)
    lastName = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=80)
    phone = models.IntegerField(null=True, blank=True)
    countrycode = models.IntegerField(null=True, blank=True)
    imageUrl = models.CharField(max_length=100, null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    lastVisit = models.DateField(auto_now_add=True)

    def __str__(self):
        return "email : " + self.email
