from django.db import models

# Create your models here.

#定义管理员类
class Master(models.Model):
    username = models.CharField(primary_key=True,max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=30)
    regist_time = models.CharField(max_length=20)
    limit_type = models.CharField(max_length=50)
    limit_time = models.CharField(max_length=20)

#定义产品类
class Product(models.Model):
    product_name = models.CharField(primary_key=True,max_length=20)
    product_time=models.CharField(max_length=20)
    product_cost=models.CharField(max_length=20)
    unit_cost = models.CharField(max_length=20)
    regist_time = models.CharField(max_length=20)
    kai_time=models.CharField(max_length=20)
    product_type=models.CharField(max_length=20)

#定义客户类型
class Client(models.Model):

    osname = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    identify_num = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    regist_time = models.CharField(max_length=20)
    client_state =models.CharField(max_length=10)
    #定义客户表的外键,关键产品表
    p_name = models.ManyToManyField(Product)






