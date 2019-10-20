"""regionalenergy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views
from amazeui import views as amazeuiViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('getDateInIdex/', views.getIndexDate), #获取首页的数据
    # path('home/', views.home),
    # path('regionLink/', views.regionLink),

    # path('tablesPage/', views.tablesPage),
    # path('calendarPage/', views.calendarPage),
    # path('formPage/', views.formPage),
    # path('chartPage/', views.chartPage),
    # path('tableListPage/', views.tableListPage),
    # path('tableListImgPage/', views.tableListImgPage),
    # path('signUpPage/', views.signUpPage),
    # path('loginPage/', views.loginPage),
    # path('errorPage/', views.errorPage),


    path('getPage/', views.getPage),

    #
    # path('amazeui/', amazeuiViews.index),
]
              # + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

