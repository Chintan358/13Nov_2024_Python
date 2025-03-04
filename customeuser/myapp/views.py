from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"reg.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("fname")
        lname = data.get("lname")
        phone = data.get("phone")
        password = data.get("password")

        user  =  CustomeUser(first_name=fname,last_name=lname,phone_number=phone)
        user.set_password(password)
        user.save()

        return redirect("index")
    