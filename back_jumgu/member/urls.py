from django.urls import path
from member import views

urlpatterns = [
    path('',views.index),
    path('ourmember',views.ourmember),
    path('contactus',views.contactus),
]