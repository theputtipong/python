from django.contrib import admin
from member.models import Member

#1 py manage.py createsuperuser // set user,email,pass

# Register your models here.

admin.site.register(Member)
