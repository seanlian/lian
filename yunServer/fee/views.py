from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from login.models import Product
import json
import time

# Create your views here.
def show_fee_add(request):
    return render(request,'fee_add.html')
def show_fee_list(request):
    return render(request,'fee_list.html')
def show_fee_modi(request):
    return render(request,'fee_modi.html')
def show_fee_detail(request):
    return render(request,'fee_detail.html')

@csrf_exempt
def select_product(request):
    page=int(request.POST.get('page'))
    pageSize=int(request.POST.get('pageSize'))
    res={}
    product_list=Product.objects.all()#查询整个Master
    ptr=Paginator(product_list,pageSize)
    res['total']=ptr.count
    products=ptr.page(page)
    res['list']=products
    res['list'] = json.loads(serializers.serialize("json",products))
    return JsonResponse(res)

@csrf_exempt
def create_product(request):
    then_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).split(" ")[0]
    product_name = request.POST.get('product_name')
    product_time=request.POST.get('product_time')
    product_cost=request.POST.get('product_cost')
    unit_cost = request.POST.get('unit_cost')
    regist_time=then_time
    kai_time=then_time
    product_type='暂停'
    #根据用户名修改管理员信息
    res= Product.objects.filter(product_name=product_name)
    obj=None
    for item in res:
        obj=item
    if obj is None:
        Product.objects.create(product_name=product_name,product_time=product_time,product_cost=product_cost,unit_cost=unit_cost,regist_time=regist_time,
                           kai_time=  kai_time,product_type=product_type
                           )
        msg={'code':200}
    else:
        msg={'code':300,'error':'产品名已存在'}

    return HttpResponse(json.dumps(msg))

@csrf_exempt
#更新产品信息
def update_product(request):
    product_name = request.POST.get('product_name')
    product_time=request.POST.get('product_time')
    product_cost= request.POST.get('product_cost')
    unit_cost = request.POST.get('unit_cost')


    #根据用户名修改管理员信息
    Product.objects.filter(product_name=product_name).update(product_time=product_time)
    Product.objects.filter(product_name=product_name).update(product_cost=product_cost)
    Product.objects.filter(product_name=product_name).update(unit_cost=unit_cost)


    msg={'code':200}
    return HttpResponse(json.dumps(msg))

#定义函数完成数据的删除
@csrf_exempt
def delete_product(request):
    product_name=request.POST.get('product_name')

    Product.objects.filter(product_name=product_name).delete()
    res = Product.objects.filter(product_name=product_name)
    obj=None
    for item in res:
        obj=item
    if obj is None:
        msg={'code':200}
    else:
        msg={'code':300}
    return HttpResponse(json.dumps(msg))


@csrf_exempt
def start_product(request):
    time1=str(time.strftime('%Y-%m-%d',time.localtime()))
    product_name = request.POST.get('product_name')
    product_type = '开通'
    kai_time=time1
    Product.objects.filter(product_name=product_name).update(product_type=product_type)
    Product.objects.filter(product_name=product_name).update(kai_time=kai_time)
    msg={'code':200}
    return HttpResponse(json.dumps(msg))
