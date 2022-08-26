from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def yase(request):
    return HttpResponse("<h1>yase</>")