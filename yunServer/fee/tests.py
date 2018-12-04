from django.test import TestCase
import time
# Create your tests here.

print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
str1=str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
str1=str1.split(" ")
print(str1)
then_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()).split(" ")[0]
print(then_time)