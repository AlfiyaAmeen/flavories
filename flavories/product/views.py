from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import fruits
from .models import commentbox
# Create your views here.
def product(request):
    
    iname=request.GET['id']
    obj=fruits.objects.get(id=iname)
    if  "recent" in request.session:
        if iname in request.session["recent"]:
            request.session["recent"].remove(iname)
        data1=fruits.objects.filter(id__in=request.session["recent"])
        request.session["recent"].insert(0,iname)
        if len(request.session["recent"])>4:
            request.session["recent"].pop()
        
    else:
        data1=[]
        request.session["recent"]=[iname]
    request.session.modified=True
    
    return render(request,"about.html",{"data":obj,'rct':data1})
def comment(request):
    com=request.GET['cmtmsg']
    com1=request.GET['proid']
    com2=request.GET['user']
    obj=commentbox.objects.create(user=com2,msg=com,proid_id=com1,like=0)
    obj.save()
    return redirect("/product/?id="+com1)

def like(request):
    com1=request.GET['id']
    obj=commentbox.objects.filter(id=com1)
    i=int(obj[0].like)+1
    obj.update(like=str(i))
    return redirect("/product/?id="+str(obj[0].proid_id))


   

 
    
