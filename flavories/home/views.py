from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")

def test1(request):
    return render(request,"text.html",{"val":"uname"})
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def loginsub(request):
    uname=request.POST["user"]
    pname=request.POST["pas"]
    u=auth.authenticate(username=uname,password=pname)
    if u:
        auth.login(request,u)
        return redirect("/")

    return render (request,"login.html",{"val":u})
def regsub(request):
    fname=request.POST["fname"]
    lname=request.POST["lname"]
    uname=request.POST["uname"]
    email=request.POST["email"]
    pas=request.POST["pas"]
    repas=request.POST["repas"]
    if pas==repas:
        if User.objects.filter(username=uname):
            msg="username is already taken"
            return render(request,"text.html",{"val":msg})
 
        elif User.objects.filter(email=email):
            msg="Email is already taken" 
            return render(request,"text.html",{"val":msg})
 

        else:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,
            password=pas)
            user.save();
            return redirect("/")
    else:
        msg="Password invalid"
        return render(request,"text.html",{"val":msg})
 
    
