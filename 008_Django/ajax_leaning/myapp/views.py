from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def addstudent(request):
    
    if request.method=="POST":
        data = request.POST
        uname = data.get("uname")
        email = data.get("email")
        phone = data.get("phone")
        
        Student.objects.create(username=uname,email=email,phone=phone)
    
    return HttpResponse("Registration success")

def viewstudent(request):
    allStudent = Student.objects.all()
    return JsonResponse({"allStudent":list(allStudent.values())})