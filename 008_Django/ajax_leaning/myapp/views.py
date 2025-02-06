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

def deleteuser(request):

    id = request.GET['uid']
    st = Student.objects.get(pk=id)
    Student.delete(st)
    return HttpResponse("User deleted !!!")

def userbyid(request):
    id = request.GET['uid']
    st = Student.objects.filter(id=id)
    print(st)
    return JsonResponse({"st":list(st.values())})

def updatestudent(request):
    if request.method=="POST":
        data = request.POST
        id = data.get("id")
        uname = data.get("uname")
        email = data.get("email")
        phone = data.get("phone")

        st = Student.objects.get(pk=id)
        st.username=uname
        st.email=email
        st.phone=phone
        st.save()

    return HttpResponse("User updated")

def searchstudent(request):
    data = request.GET['data']

    allStudent = Student.objects.filter(username__startswith=data)
    return JsonResponse({"allStudent":list(allStudent.values())})