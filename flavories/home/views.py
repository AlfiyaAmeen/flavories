from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from product.models import fruits

# Create your views here.
def index(request):
    obj=fruits.objects.all()
    print("hi",obj)
    return render(request,"index.html",{"data":obj})


def test1(request):
    return render(request,"text.html",{"val":"uname"})


    return render(request,"register.html")
    
def login(request):
    if request.method=="POST":
        uname=request.POST["user"]
        pname=request.POST["pas"]
        u=auth.authenticate(username=uname,password=pname)
        if u:
            auth.login(request,u)
            return redirect("/")
        msg="invalid username and password"
        return render (request,"login.html",{"msg":msg})

    else:
         
         return render(request,"login.html")


    return render (request,"login.html",{"val":u})
def register(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        uname=request.POST["uname"]
        email=request.POST["email"]
        pas=request.POST["pas"]
        repas=request.POST["repas"]
        if pas==repas:
            if User.objects.filter(username=uname):
                msg="username is already taken"
                return render(request,"register.html",{"msg":msg})
        
            elif User.objects.filter(email=email):
                msg="Email is already taken" 
                return render(request,"register.html",{"msg":msg})
        

            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,
                password=pas)
                user.save();
                auth.login(request,user)
                return redirect("/")
    
    
            
            
        else:
            msg="Password invalid"
            return render(request,"register.html",{"msg":msg})
 
    else:
        return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect("/")