from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from login.models import Client,Product
import time,json
import json
# Create your views here.
def show_account_add(request):
    return render(request,'account_add.html')
def show_account_list(request):
    return render(request,'account_list.html')
def show_account_modi(request):
    return render(request,'account_modi.html')
def show_account_detail(request):
    return render(request,'account_detail.html')

#定义函数完成对Client表的查询
@csrf_exempt
def select_client(request):
    page=int(request.POST.get('page'))
    pageSize=int(request.POST.get('pageSize'))

    res={}
    Client_list=Client.objects.all()#查询整个Master

    ptr=Paginator(Client_list,pageSize)
    res['total']=ptr.count
    Clients=ptr.page(page)
    res['list']=Clients
    res['list'] = json.loads(serializers.serialize("json",Clients))
    return JsonResponse(res)

#定义函数完成对Client表的添加功能
@csrf_exempt
def regist_client(request):
    then_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(" ")[0]
    name = request.POST.get('name')
    identify_num = request.POST.get('identify_num')
    osname = request.POST.get('osname')
    password=request.POST.get('password')

    phone = request.POST.get('phone')
    regist_time = then_time
    client_state='开通'

    res=Client.objects.filter(osname=osname)

    obj=None

    for item in res:
        obj=item
    if obj is None:
        Client.objects.create(osname=osname,name=name,identify_num=identify_num,password=password,phone=phone,regist_time=regist_time,client_state=client_state)
        msg={'code':200}
    else:
        msg = {'code': 300,'error':'用户名已存在'}
    return JsonResponse(msg)

#定义函数完成对Client表的添加功能
@csrf_exempt
def update_client(request):
    osname=request.POST.get('osname')
    name = request.POST.get('name')
    phone = request.POST.get('phone')

    Client.objects.filter(osname=osname).update(name=name)
    Client.objects.filter(osname=osname).update(phone=phone)
    msg={'code':200}
    return JsonResponse(msg)

#定义函数完成删除
@csrf_exempt
def delete_client(request):
    osname=request.POST.get('osname')

    Client.objects.filter(osname=osname).delete()

    msg={'code':200}
    return JsonResponse(msg)

@csrf_exempt
def stop_client(request):
    osname=request.POST.get('osname')
    identify_num = request.POST.get('identify_num')

    Client.objects.filter(osname=osname).update(client_state='暂停')

    msg={'code':200}
    return JsonResponse(msg)

@csrf_exempt
def update_client_p_name(request):
    osname=request.POST.get('osname')
    p_name = request.POST.get('p_name')



    res=Client.objects.filter(osname=osname)
    res1=Product.objects.filter(product_name=p_name)

    obj = None

    for item in res:
        obj=item
    if obj is not None:
        obj.p_name.set(res1)
        obj.save()
        msg={'code':200}

    else:
        msg={'code':300}
    return JsonResponse(msg)



