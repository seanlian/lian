from django.test import TestCase
from PIL import Image,ImageFont,ImageDraw
import pytesseract
from django.conf import settings
import random,os

# Create your tests here.
def get_infor():
    list1 = []
    #生成字母
    list1.extend([i for i in range(65,90)])
    #生成小写字母
    list1.extend([i for i in range(97,123)])
    #生成数字
    list1.extend([i for i in range(48,57)])
    index=random.randint(0, len(list1)-1)
    temp=list1[index]
    return chr(temp)

def get_background_color():
     r=random.randint(150,250)
     g=random.randint(160,220)
     b=random.randint(200,255)
     return (r,g,b)


def get_background_color2():
    r = random.randint(20, 120)
    g = random.randint(66, 100)
    b = random.randint(10, 50)
    return (r, g, b)

def get_code():
    cont=[]
    w,h=55,30
    image1=Image.new('RGB',(w,h),(255,255,255))
    f=open('yzm.txt','w+')
    font=ImageFont.truetype('yzm/123.ttf',23)
    #创建画笔
    draw=ImageDraw.Draw(image1)

    for x in range(w):
        for y in range(h):
            draw.point((x,y),fill=get_background_color())
    for i in range(4):
        draw.text((13*i+1,1),get_infor(),font=font,fill=get_background_color2())
        print(get_infor())
        f.write(get_infor())
        cont.append(get_infor())

    f.close()
    image1.show()
    return cont


im=Image.open('1.jpg')
print(pytesseract.image_to_string(im))




