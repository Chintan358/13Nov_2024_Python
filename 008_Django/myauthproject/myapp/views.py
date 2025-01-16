from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def userlogin(request):
    return render(request,"login.html")

def reg(request):
    return render(request,"reg.html")

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