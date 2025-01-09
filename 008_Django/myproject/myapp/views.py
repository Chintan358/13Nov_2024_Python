from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    allusers = MyUser.objects.all()
   
    return render(request,"index.html",{"users":allusers})

def adduser(request):
    if request.method=='POST':
        id=request.POST['id']
        uname = request.POST['uname']
        email= request.POST['email']
        phone=request.POST['phone']
        
        if(id):
           cuser = MyUser.objects.get(pk=id)
           cuser.uname=uname
           cuser.email=email
           cuser.phone=phone
           cuser.save()
        else:
            createdUser = MyUser.objects.create(uname=uname,email=email,phone=phone)
        
    
    return redirect("index")

def deleteuser(request,id):
    user =  MyUser.objects.get(pk=id)
    user.delete()
    return redirect("index")

def edituser(request,id):
    u =  MyUser.objects.get(pk=id)   
    allusers = MyUser.objects.all()
    return render(request,"index.html",{"u":u,"users":allusers})