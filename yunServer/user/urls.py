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

    path('show_user_info/', show_user_info, name='show_user_info'),
    path('show_user_modi_pwd/', show_user_modi_pwd, name='show_user_modi_pwd'),

    #修改密码
    path('update_pwd/', update_pwd, name='update_pwd'),

    #查看登录人员信息
    path('search_master_infor/', search_master_infor, name='search_master_infor'),


    path('update_m_infor/', update_m_infor, name='update_m_infor'),



]
