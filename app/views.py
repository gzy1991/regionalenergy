#coding:utf-8
#!/usr/bin/python
# Create your views here.
from django.shortcuts import render
import json
import regionalenergy.settings as Setting
# Create your views here.

def getPage(request):
    province = request.GET.get("province")
    if(province=="" or province=="undefined"):
        province="河南省"
    resData={}
    resData["province"]=province
    type = request.GET.get("type")
    html=''
    if(type=="index"):
        # 获取页面数据
        Setting.FILR_DIR["INDEX_DIR"]

        html='index'
    elif(type=="trend"):
        html = 'trend'
    elif (type == "regionLink"):
        html = 'regionLink'
    elif(type=="prediction"):
        html = 'prediction'
    elif(type=="calendarPage"):
        html = 'calendar'
    elif(type=="formPage"):
        html = 'form'
    elif(type=="chartPage"):
        html = 'chart'
    elif(type=="tableListPage"):
        html = 'table-list'
    elif(type=="tableListImgPage"):
        html = 'table-list-img'
    elif(type=="signUpPage"):
        html = 'sign-up'
    elif(type=="loginPage"):
        html = 'login'
    elif(type=="errorPage"):
        html = '404'

    return render(request, 'app/'+html+'.html', resData)

def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    mydict = {"hello": "Hello World", "usersn": "123456"}
    return  render(request, 'app/index.html',{'province':"山西省"} )

def getIndexDate(request):
    Setting.FILR_DIR["INDEX_DIR"]  #文件路径


    return render(request)

# def home(request):
#     return  render(request, 'app/homePage.html')
#
# def regionLink(request):
#     return  render(request, 'app/regionLink.html')
#
# def tablesPage(request):
#     return  render(request, 'app/tables.html')
#
# def calendarPage(request):
#     return  render(request, 'app/calendar.html')
#
# def formPage(request):
#     return  render(request, 'app/form.html')
#
# def chartPage(request):
#     return  render(request, 'app/chart.html')
#
# def tableListPage(request):
#     return  render(request, 'app/table-list.html')
#
# def tableListImgPage(request):
#     return  render(request, 'app/table-list-img.html')
#
# def signUpPage(request):
#     return  render(request, 'app/sign-up.html')
#
# def loginPage(request):
#     return  render(request, 'app/login.html')
#
# def errorPage(request):
#     return  render(request, 'app/404.html')


