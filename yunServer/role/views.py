from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from login.models import Master
import json
# Create your views here.
def show_role_add(request):
    return render(request,'role_add.html')
def show_role_list(request):
    return render(request,'role_list.html')
def show_role_modi(request):
    return render(request,'role_modi.html')

#定义函数完成管理员的删除
#
def delete_master(request):
    name=request.POST.get('name')
    limt_type=request.POST.get('limit_type')

    Master.objects.filter(name=name).delete()
    res = Master.objects.filter(name=name)
    obj=None
    for item in res:
        obj=item
    if obj is None:
        msg={'code':200}
    return HttpResponse(json.dumps(msg))

#定义函数完成管理员的删除
#
def delete_master_many(request):
    username=request.POST.get('username')

    Master.objects.filter(username=username).delete()
    msg={'code':200}
    return HttpResponse(json.dumps(msg))

#定义函数完成管理员信息的更新
#
@csrf_exempt
#更新角色信息
def update_master(request):
    username = request.POST.get('username')
    name=request.POST.get('name')
    limit_type=request.POST.get('limit_type')

    #根据用户名修改管理员信息
    Master.objects.filter(username=username).update(name=name)
    Master.objects.filter(username=username).update(limit_type=limit_type)

    msg={'code':200}
    return HttpResponse(json.dumps(msg))
@csrf_exempt
#更新管理员信息
def update_master_many(request):
    username = request.POST.get('username')
    name=request.POST.get('name')
    phone= request.POST.get('phone')
    email = request.POST.get('email')
    limit_type=request.POST.get('limit_type')

    #根据用户名修改管理员信息
    Master.objects.filter(username=username).update(name=name)
    Master.objects.filter(username=username).update(phone=phone)
    Master.objects.filter(username=username).update(email=email)
    Master.objects.filter(username=username).update(limit_type=limit_type)

    msg={'code':200}
    return HttpResponse(json.dumps(msg))


