from django.shortcuts import render

# Create your views here.
def shewag(request):
    return render(request,'shewag.html')
from django.http import *
def third(request):
    return HttpResponse('<center><h1>This is http response for views </h1></center>')
