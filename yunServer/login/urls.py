"""yunServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import *

urlpatterns = [
    path('showLogin/',showLogin,name="sl"),#显示登录页面
    path('index/',showIndex,name='index'),#显示主页面
    path('show_master_regist/',show_master_regist,name='smr'),#显示注册管理员页面
    path('show_master_list/',show_master_list,name='sml'),#显示管理员页面列表
path('show_master_modi/',show_master_modi,name='smd'),#显示管理员页面列表
    path('show_error/', show_error, name='serr'),#显示错误提示页面
    path('show_nopower/', show_nopower, name='snop'),#显示权限提示页面
    path('superuser_login/',superuser_login,name='spl'),#管理员登录功能

    path('select_master/',select_master,name='select_master'),


    path('register_master/',register_master,name='rm'),#注册管理员

    

    path('reset_password/',reset_password,name='reset_password'),#注册管理员
 




  

   

 



]
