import pymongo

client=pymongo.MongoClient(host="127.0.0.1",port=27017)

db=client.LOL

col=db.shop

res=col.find()


#print(res[0].update({'img_url':'http://39.105.1.33/img/hero/Aatrox.png'}))
for item in res:
    img_url=item['img_url'].replace('192.168.80.133:80','39.105.1.33')
    #res=item.update({'img_url':item['img_url']},{ '$set':{'img_url':img_url}},multi=True)

    res=col.update({'img_url':item['img_url']}, {'$set': {'img_url':img_url}}, multi=True)
    print(res)
#
#
# res=col.update({'title':'闪现'},{'$set':{'rank':'召唤师等级：1级'}})
#
#
# res2=col.update({'title':'魄罗投掷'},{'$set':{'rank':'召唤师等级：1级'}})
#
# print(res)





