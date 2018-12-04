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

    path('show_service_add/', show_service_add, name='show_service_add'),
    path('show_service_detail/', show_service_detail, name='show_service_detail'),
    path('show_service_list/', show_service_list, name='show_service_list'),
    path('show_service_modi/', show_service_modi, name='show_service_modi'),

    path('verify_id/',verify_id,name='verify_id'),

    path('delete_client_p_name/',delete_client_p_name,name='delete_client_p_name'),
    path('stop_client/',stop_client,name='stop_client'),


]
