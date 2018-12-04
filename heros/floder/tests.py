from django.test import TestCase

# Create your tests here.
import pymongo

client=pymongo.MongoClient(host="39.105.1.33",port=27017)

db=client.LOL

col=db.shop




# #print(res[0].update({'img_url':'http://39.105.1.33/img/hero/Aatrox.png'}))
# for item in res:
#     img_url=item['img_url'].replace('192.168.80.133:80','39.105.1.33')
#     #res=item.update({'img_url':item['img_url']},{ '$set':{'img_url':img_url}},multi=True)
#
#     res=col.update({'img_url':item['img_url']}, {'$set': {'img_url':img_url}}, multi=True)
#     print(res)
#
#
# res=col.update({'title':'闪现'},{'$set':{'rank':'召唤师等级：1级'}})
#
#
# res2=col.update({'title':'魄罗投掷'},{'$set':{'rank':'召唤师等级：1级'}})
#
# print(res)

name_list=[
'太空比尔吉沃特弯刀','太空玛莫提乌斯之噬','太空贪欲九头蛇',
    '太空水银弯刀','太空死亡之舞','傲之追猎者的刀锋','多兰的失落之刃',
    '坚忍之属性手杖','朔极之矛','激发之匣','傲之追猎者的刀锋','附魔：符能回声',
    '多兰的失落之戒','多兰的失落之偶','激发之匣','坚忍之属性手杖','太空海克斯科技枪刃',
    '太空骑士之誓','朔极之矛','太空玛莫提乌斯之噬','太空死亡之舞','贤者印章',
    ''
]

#for  i  in  range(len(name_list)):
    #col.delete_one({'name': 'xiaocai'})
col.delete_one({'title':'附魔：符能回声'})
