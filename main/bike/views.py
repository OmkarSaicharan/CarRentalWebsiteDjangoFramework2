from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.python functions.
def home(request):
    return HttpResponse("This is bike Modules")