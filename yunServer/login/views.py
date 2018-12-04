from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import random,os
from .models import *
import json,time

from PIL import  Image
# Create your views here.
#渲染登录页面
def showLogin(request):
    return render(request,'login.html')
#渲染主页面
def showIndex(request):
    return render(request,'index.html')
#渲染管理员注册页面
def show_master_regist(request):
    return render(request,'admin/admin_add.html')
def show_master_list(request):
    return render(request,'admin/admin_list.html')
def show_master_modi(request):
    return render(request,'admin/admin_modi.html')

#渲染错误提示页面
def show_error(request):
    return render(request,'error.html')
#渲染权限提示页面
def show_nopower(request):
    return render(request,'nopower.html')

#定义函数完成管理员的注册
def register_master(request):
    name=request.POST.get('name')
    username=request.POST.get('username')
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    regist_time=request.POST.get('regist_time')
    limit_type=request.POST.get('limit_type')
    limit_time=request.POST.get('limit_time')

    #根据账号username在Master模型表格中查询
    res=Master.objects.filter(username=username)
    obj=None
    for item in res:
        obj=item
    if obj is None:
        Master.objects.create(name=name,username=username,password=password,phone=phone,email=email,limit_type=limit_type, regist_time= regist_time,limit_time=limit_time)
        msg={'code':200}
    else:
        msg={'code':300}
    return HttpResponse(json.dumps(msg))



#定义函数完超级管理员的登录
@csrf_exempt
def superuser_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    res = Master.objects.filter(username=username)
    obj=None
    for item in res:
        obj=item
    if  ( obj is None):
        msg={'code':300,'error':'用户名不存在'}
    else:
        if obj.password==password:
            msg = {'code': 200, 'error': '','success':obj.limit_type,'username':username}
        else:
            msg = {'code':205, 'error': '密码错误'}

    return HttpResponse(json.dumps(msg))

#定义函数完成普通管理员的登录
def master_login(request):
    username=models.POST.get('username')
    password=models.POST.get('password')

    res = Master.objects.filter(username=username)
    obj=None
    for item in res:
        obj=item
    if obj is None:
        msg={'code':205,'error':'用户名不存在'}
    else:
        if obj.password==password:
            msg={'code':200,'error':''}
        else:
            msg = {'code':300, 'error': '密码错误'}
    return HttpResponse(json.dumps(msg))
#定义函数完成管理员的查询
@csrf_exempt
def select_master(request):
    page=int(request.POST.get('page'))
    pageSize=int(request.POST.get('pageSize'))
    res={}
    master_list=Master.objects.all()#查询整个Master
    ptr=Paginator(master_list,pageSize)
    res['total']=ptr.count
    masters=ptr.page(page)
    res['list']=masters
    res['list'] = json.loads(serializers.serialize("json",masters))
    return JsonResponse(res)

#管理员密码重置
@csrf_exempt
def reset_password(request):
    username=request.POST.get('username')
    password='000000'
    Master.objects.filter(username=username).update(password=password)

    msg={'code':200}
    return JsonResponse(msg)












