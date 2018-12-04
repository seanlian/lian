from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from login.models import Client,Product
import time,json


# Create your views here.

def show_service_add(request):
    return render(request, 'service_add.html')
def show_service_detail(request):
    return render(request, 'service_detail.html')
def show_service_list(request):
    return render(request, 'service_list.html')
def show_service_modi(request):
    return render(request, 'service_modi.html')

#定义函数完成对成员身份的验证
@csrf_exempt
def  verify_id(request):
    identify_num= request.POST.get('identify_num')

    res=Client.objects.filter(identify_num=identify_num)
    obj=None
    for item in res:
        obj=item
    if obj is not None:
        msg={'code':200,'error':''}
    else:
        msg = {'code': 300, 'error': '身份证号不存在'}
    return HttpResponse(json.dumps(msg))

#定义函数完成对客户的资费选项删除
@csrf_exempt
def delete_client_p_name(request):
    identify_num=request.POST.get('identify_num')

    res=Client.objects.filter(identify_num=identify_num)

    obj=None
    for  item in res:
        obj=item
    if obj is not None:
        obj.p_name.set('')
        msg={'code':200}
    else:
        msg = {'code': 300}

    return JsonResponse(msg)

#定义函数完成对客户的资费的暂停

@csrf_exempt
def stop_client(request):

    identify_num = request.POST.get('identify_num')

    Client.objects.filter(identify_num =identify_num ).update(client_state='暂停')

    msg = {'code': 200}
    return JsonResponse(msg)