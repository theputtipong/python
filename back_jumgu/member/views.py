from django.shortcuts import render

# from django.http import HttpResponse
from datetime import date


# Create your views here.
def index(request):
    username = "test_acc"
    lastvisit = date(2023, 6, 29)
    return render(request, "index.html", {"username": username, "lastvisit": lastvisit})


def about(request):
    return render(request, "about.html")


def contactus(request):
    # return HttpResponse("<h1>Contact Us</h1>") #return pure html
    return render(request, "contactus.html")
