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

    path('show_bill_item/', show_bill_item, name='show_bill_item'),
    path('show_bill_list/', show_bill_list, name='show_bill_list'),
    path('show_bill_service_detail/', show_bill_service_detail, name='show_bill_service_detail'),


    #查询客户的购买产品的种类
    path('select_client_message/', select_client_message, name='select_client_message'),
]
