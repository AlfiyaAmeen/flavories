from django.shortcuts import render
from django.http import HttpResponse
from .models import fruits
# Create your views here.
def product(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)
    return render(request,"about.html",{"data":obj})