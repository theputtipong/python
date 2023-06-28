from django.urls import path
from member import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('contactus',views.contactus),
]