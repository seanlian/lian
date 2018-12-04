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
        path('show_account_add/',show_account_add,name='show_account_add'),
        path('show_account_list/',show_account_list,name='show_account_list'),
        path('show_account_modi/',show_account_modi,name='show_account_modi'),
        path('show_account_detail/',show_account_detail,name='show_account_detail'),

        #查询客户表格
        path('select_client/',select_client,name='select_client'),
        # 注册客户表格
        path('regist_client/', regist_client, name='regist_client'),
        # 更新客户表格
        path('update_client/', update_client, name='update_client'),
        # 删除客户数据
        path('delete_client/', delete_client, name='delete_client'),
        # 暂停客户
        path('stop_client/', stop_client, name='stop_client'),

        # 更新客户购买产品字段
        path('update_client_p_name/', update_client_p_name, name='update_client_p_name'),



]
