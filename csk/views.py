from django.shortcuts import render

# Create your views here.
def dhoni(request):
    return render(request,'csk.html')
from django.http import *
def first(request):
    return HttpResponse('<center><h1>This is http response for views</h1></center>')