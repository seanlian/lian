from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from login.models import Master
import json

# Create your views here.
def show_user_info(request):
    return render(request, 'user_info.html')
def show_user_modi_pwd(request):
    return render(request, 'user_modi_pwd.html')

@csrf_exempt
def update_pwd(request):
    oldpassword = request.POST.get('oldpassword')
    newpassword = request.POST.get('newpassword')
    ppassword = request.POST.get('ppassword')

    res = Master.objects.filter(password=oldpassword)
    obj = None
    for item in res:
        obj = item
    if obj is None:
        msg = {'code': 400, 'error': '密码不正确,请重新输入'}
    else:
        if newpassword == ppassword:
            obj.password = ppassword
            obj.save()
            msg = {'code': 200, 'error':'', 'success':'密码修改成功'}
        else:
            msg = {'code':300, 'error':'新密码两次输入不一致'}
    return HttpResponse(json.dumps(msg))

#查询登录人员信息
@csrf_exempt
def search_master_infor(request):
    username=request.POST.get('username')

    res=Master.objects.filter(username=username)
    msg={}

    msg['success']=json.loads(serializers.serialize('json',res))
    return JsonResponse(msg)


#修改登录人员信息
@csrf_exempt
def update_m_infor(request):
    username=request.POST.get('username')
    name=request.POST.get('name')
    phone=request.POST.get('phone')
    email=request.POST.get('email')

    Master.objects.filter(username=username).update(name=name)
    Master.objects.filter(username=username).update(phone=phone)
    Master.objects.filter(username=username).update(email=email)


    msg={'code':200}
    return JsonResponse(msg)