from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginpage(request):
    return render(request,"login.html")

def reg(request):
    return render(request,"reg.html")

@login_required(login_url="/")
def home(request):
    return render(request,"home.html")

def userreg(request):
    if request.method=="POST":
        data = request.POST
        uname = data.get("uname")
        fname = data.get("fname")
        lname = data.get("lname")
        email = data.get("email")
        password = data.get("pass")

        if User.objects.filter(username=uname).exists():
            messages.add_message(request, messages.ERROR, "Username already Exists !!!")
            return render(request,"reg.html")

        user = User(first_name=fname,last_name=lname,email=email,username=uname)
        user.set_password(password)
        user.save()

        messages.add_message(request, messages.SUCCESS, "Registration successFully !!!!")
        return render(request,"reg.html")

def userlogin(request):
    if request.method=='POST':
        data = request.POST
        username = data.get("uname")
        password = data.get("pass")

        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "Invalid credentials !!!!")
            return render(request,"login.html")

        user = authenticate(username=username,password=password)
        if user == None:
            messages.add_message(request, messages.ERROR, "Invalid credentials !!!!")
            return render(request,"login.html")
        else:
            login(request,user)
            return redirect("home")

def userlogout(request):
    logout(request)
    return render(request,"login.html")