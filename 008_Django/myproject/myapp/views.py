from django.shortcuts import render,HttpResponse
from myapp.models import *
# Create your views here.
def index(request):
    # return HttpResponse("Index calling")
    return render(request,"index.html",{"uname":"Paras"})

def home(request):
    # return HttpResponse("Home calling")
    return render(request,"home.html")

def about(request):
    # return HttpResponse("About calling")
    return render(request,"about.html")

def addStudent(request):
    
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
        phone = request.POST['phone']

        Student.objects.create(username=username,email=email,phone=phone,age=age)
    
    return render(request,"index.html",{"msg":"Registration successful"})