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
        path('role_add/',show_role_add,name='role_add'),
        path('role_list/',show_role_list,name='role_list'),
        path('role_modi/',show_role_modi,name='role_modi'),

        #删除显示信息
        path('delete_master/',delete_master,name='delete_master'),
        path('delete_master_many/',delete_master_many,name='delete_master_many'),
        # 更新显示信息
        path('update_master/', update_master, name='update_master'),
        # 更新管理员多条信息
        path('update_master_many/', update_master_many, name='update_master_many'),
]
