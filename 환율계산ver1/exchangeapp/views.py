#views.py
from django.shortcuts import render
from exchangeapp.models import Lion
# Create your views here.
def home(request):
    return render(request,'exchangeapp/home.html')

def usd(request):
    korea = request.POST['korea']
    korea = int(korea)
    usd = korea/1217.50
    return render(request,'exchangeapp/usd.html',{'korea':korea,'usd':usd})

def jpy(request):
    korea = request.POST['korea']
    korea = int(korea)
    jpy = korea/1127.26*100
    return render(request,'exchangeapp/jpy.html',{'korea':korea,'jpy':jpy})

def can(request):
    korea = request.POST['korea']
    korea = int(korea)
    can = korea/871.70
    return render(request,'exchangeapp/can.html',{'korea':korea,'can':can})

def lion_list(request):
    lion_list = Lion.objects.all()
    return render(request,'exchangeapp/lions.html',{'lion_list':lion_list})


