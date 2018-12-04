from .settings  import fl
from flask import render_template,request

from .models import *

from flask import jsonify
import json


@fl.route('/')
def show():
    return  render_template('datas.html')

@fl.route('/show_data/',methods=['get'])
def show_data():
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
    return json.dumps({'res':list1})


#加载英雄
@fl.route('/show_heros/',methods=['get'])
def show_heros():
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
    return json.dumps({'res':list1})





#加载装备
@fl.route('/show_shop/',methods=['get'])
def show_shop():
    res=Shop.objects.all()
    list1=[]
    for item  in res:
        dic = {}

        dic["title"]=item.title
        dic["img_url"] = item.img_url
        list1.append(dic)
    return json.dumps({'res':list1})

#加载召唤师技能
@fl.route('/show_spell/',methods=['get'])
def show_spell():
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
    return json.dumps({'res':list1})

#查询招魂师技能的具体信息
@fl.route('/show_spell_infors/',methods=['get'])
def show_spell_infors():
    if request.method == 'GET':
        datas=request.values.get('data')

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
        return json.dumps(msg)