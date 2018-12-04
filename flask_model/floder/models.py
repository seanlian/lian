
from flask_mongoengine import MongoEngine
from main.app  import app

app.config['MONGODB_SETTINGS'] = {

    'db': 'LOL',

    'host': 'localhost',

    'port': 27017,


}

#创建mongo原型

mdb = MongoEngine()

mdb.init_app(app)


class Hero(mdb.Document):
    model_name=mdb.StringField(max_length=20)
    kind = mdb.StringField(max_length=20)
    img_url = mdb.StringField(max_length=100)
    link = mdb.StringField(max_length=100)
    title= mdb.StringField(max_length=20)


class Shop(mdb.Document):
    img_url = mdb.StringField(max_length=100)
    title= mdb.StringField(max_length=20)
    model_name = mdb.StringField(max_length=20)



class Spell(mdb.Document):
    text=mdb.StringField(max_length=50)
    big_url= mdb.StringField(max_length=100)
    img_url = mdb.StringField(max_length=100)
    rank = mdb.StringField(max_length=20)
    title= mdb.StringField(max_length=20)



