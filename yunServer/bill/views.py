from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from login.models import Client
import json
# Create your views here.
def show_bill_item(request):
    return render(request, 'bill_item.html')

def show_bill_list(request):
    return render(request, 'bill_list.html')
def show_bill_service_detail(request):
    return render(request, 'bill_service_detail.html')

@csrf_exempt
def select_client_message(request):
    osname=request.POST.get('osname')
    res=Client.objects.filter(osname=osname)

    obj=None
    msg={}
    for item in res:
        obj=item
    if obj is None:
        msg={'code':300}
    else:
        msg={}
        # for item in obj.p_name.all():
        #     names.append(item)
        # dic={'p_name':names}
        msg['list']=json.loads(serializers.serialize('json',obj.p_name.all()))
    return HttpResponse(json.dumps(msg))
