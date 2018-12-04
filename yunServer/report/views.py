from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import  serializers
from django.views.decorators.csrf import  csrf_exempt
import json
from login.models import Client

# Create your views here.
def show_report_list(request):
    return render(request, 'report_list.html')


@csrf_exempt
def select_client_max(request):
    res=Client.objects.all()
    msg={}
    msg['result']=json.loads(serializers.serialize('json',res))
    return JsonResponse(msg)


