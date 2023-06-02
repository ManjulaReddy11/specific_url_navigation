from django.shortcuts import render

# Create your views here.
def virat(request):
    return render(request,'rcb.html')
from django.http import *
def second(request):
    return HttpResponse('<center><h1>This is http response for views </h1></center>')
