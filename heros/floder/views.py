from django.shortcuts import render
from .models import *
from django.http import JsonResponse,HttpResponse

import json
# Create your views here.

#渲染页面
def show(request):

    return render(request,'datas.html')


#加载英雄信息
def show_heros(request):
    res=Hero.objects.all()
    list1=[]
    for item  in res:
        dic = {}
        dic["title"]=item.title
        dic["model_name"] = item.model_name
        dic["link"] = item.link
        dic["img_url"] = item.img_url
        dic["kind"] = item.kind
        list1.append(dic)
    return HttpResponse(json.dumps({'res':list1}))



#加载装备

def show_shop(request):
    res=Shop.objects.all()
    list1=[]
    for item  in res:
        dic = {}

        dic["title"]=item.title
        dic["img_url"] = item.img_url
        list1.append(dic)
    return HttpResponse(json.dumps({'res':list1}))

#加载召唤师技能

def show_spell(requset):
    res=Spell.objects.all()
    list1=[]
    for item  in res:
        dic = {}
        dic["title"]=item.title
        dic["big_url"] = item.big_url
        dic["rank"] = item.rank
        dic["img_url"] = item.img_url
        dic["text"] = item.text
        list1.append(dic)
    return HttpResponse(json.dumps({'res':list1}))

#查询招魂师技能的具体信息

def show_spell_infors(request):

        datas=request.GET.get('data')

        res=Spell.objects(title=datas)


        list1=[]

        for item  in res:
            dic = {}
            dic["title"]=item.title
            dic["big_url"] = item.big_url
            dic["rank"] = item.rank
            dic["img_url"] = item.img_url
            dic["text"] = item.text
            list1.append(dic)

        msg = {'code': 200, 'res':list1}
        return HttpResponse(json.dumps(msg))