from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def index(request):
    return  render(request, 'app/index.html')

def home(request):
    return  render(request, 'app/homePage.html')

