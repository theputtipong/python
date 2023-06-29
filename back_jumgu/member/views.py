from django.shortcuts import render
# from django.http import HttpResponse
from datetime import date
from member.models import Member


# Create your views here.
def index(request):
    username = "test_acc"
    lastvisit = date(2023, 6, 29)
    return render(request, "index.html", {"username": username, "lastvisit": lastvisit})


def ourmember(request):
    all_member = Member.objects.all()
    filter_countrycode = Member.objects.filter(countrycode=67)
    return render(request, "ourmember.html",{"all_member":all_member,"filter_member":filter_countrycode})


def contactus(request):
    # return HttpResponse("<h1>Contact Us</h1>") #return pure html
    return render(request, "contactus.html")
