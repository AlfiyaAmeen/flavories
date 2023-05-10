from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import fruits
from .models import commentbox
# Create your views here.
def product(request):
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)
    return render(request,"about.html",{"data":obj})
def comment(request):
    com=request.GET['cmtmsg']
    com1=request.GET['proid']
    com2=request.GET['user']
    obj=commentbox.objects.create(user=com2,msg=com,proid_id=com1,like=0)
    obj.save()
    return redirect("/product/?id="+com1)

def like(request):
    return render(request,"text.html")

