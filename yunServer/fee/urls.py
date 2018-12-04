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
    path('show_fee_add/', show_fee_add, name='show_fee_add'),
    path('show_fee_list/', show_fee_list, name='show_fee_list'),
    path('show_fee_modi/', show_fee_modi, name='show_fee_modi'),
    path('show_fee_detail/', show_fee_detail, name='show_fee_detail'),

    # 查询产品信息
    path('select_product/', select_product, name="select_product"),
    path('create_product/',create_product,name='create_product'),
    path('update_product/',update_product,name='update_product'),
    path('delete_product/',delete_product,name='delete_product'),

    path('start_product/',start_product,name='start_product'),



]
