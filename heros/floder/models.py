from django.db import models

# Create your models here.
import mongoengine

class Hero(mongoengine.Document):
    model_name=mongoengine.StringField(max_length=20)
    kind = mongoengine.StringField(max_length=20)
    img_url = mongoengine.StringField(max_length=100)
    link = mongoengine.StringField(max_length=100)
    title= mongoengine.StringField(max_length=20)


class Shop(mongoengine.Document):
    img_url = mongoengine.StringField(max_length=100)
    title= mongoengine.StringField(max_length=20)
    model_name = mongoengine.StringField(max_length=20)



class Spell(mongoengine.Document):
    text=mongoengine.StringField(max_length=50)
    big_url= mongoengine.StringField(max_length=100)
    img_url = mongoengine.StringField(max_length=100)
    rank = mongoengine.StringField(max_length=20)
    title= mongoengine.StringField(max_length=20)
