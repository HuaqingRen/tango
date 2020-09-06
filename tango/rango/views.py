from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    html_link = "and here is " + "<a href=/rango/about/>About Page</a>"
    return HttpResponse("Rango says hey there partner!" + html_link)


def about(request):
    html_link = "and here is " + "<a href=/rango/>Index Page</a>"
    return HttpResponse("Rango says here is the about page." + html_link)