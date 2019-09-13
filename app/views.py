#coding:utf-8
#!/usr/bin/python
# Create your views here.
from django.shortcuts import render
import json
# Create your views here.

def getPage(request):


    return render(request, 'app/index.html', {'province': "山西"})

def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    mydict = {"hello": "Hello World", "usersn": "123456"}
    return  render(request, 'app/index.html',{'province':"山西"} )

def home(request):
    return  render(request, 'app/homePage.html')

def regionLink(request):
    return  render(request, 'app/regionLink.html')

def tablesPage(request):
    return  render(request, 'app/tables.html')

def calendarPage(request):
    return  render(request, 'app/calendar.html')

def formPage(request):
    return  render(request, 'app/form.html')

def chartPage(request):
    return  render(request, 'app/chart.html')

def tableListPage(request):
    return  render(request, 'app/table-list.html')

def tableListImgPage(request):
    return  render(request, 'app/table-list-img.html')

def signUpPage(request):
    return  render(request, 'app/sign-up.html')

def loginPage(request):
    return  render(request, 'app/login.html')

def errorPage(request):
    return  render(request, 'app/404.html')

