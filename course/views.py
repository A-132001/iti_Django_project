from django.shortcuts import render
from django.http  import HttpResponse

def Home(req):
    return HttpResponse("<h1>Hello from course</h1")