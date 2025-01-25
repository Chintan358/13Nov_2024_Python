from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
import re
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,"contact.html")

@login_required(login_url="login")
def cart(request):
    return render(request,"shoping-cart.html")

def shop(request):
    return render(request,"product.html")

def shopdetails(request):
    return render(request,"product-detail.html")

def registration(request):
    
    pettern = "^[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]{2,4}$"

    if request.method=="POST":
        data = request.POST
        username = data.get("uname")
        email = data.get("email")
        password = data.get("password")

        result = re.match(email,pettern)
        if result == None:
            return render(request,'registration.html',{"err" : "Invalid Email formate !!!"})
        
        if User.objects.filter(username=username).exists():
             return render(request,'registration.html',{"err" : "User alredy exist !!!"})
        
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        return render(request,'registration.html',{"msg" : "Registration successfully !!!"})

    return render(request,'registration.html')

def loginuser(request):
    if request.method=="POST":
        data = request.POST
        username = data.get("uname")
        password = data.get("password")

        user = authenticate(username=username,password=password)
        if not user : 
            return render(request,'login.html',{"err":"Invalid credentials"})
        else:
            login(request,user)
            return redirect("index")

    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return render(request,'index.html')
