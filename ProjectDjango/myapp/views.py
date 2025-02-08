from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from django.http import JsonResponse
import re
# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,"index.html",{"categories":categories,"products":products})
   

def home(request):

    id = request.GET.get("id")
    categories = Category.objects.all()
    
    if id=="":
        products = Product.objects.all()
    else :
        ct = Category.objects.get(pk=id)
        
        products  =Product.objects.filter(category=ct)

    return JsonResponse({"products":list(products.values())})
    # return render(request,"index.html",{"categories":categories,"products":products})


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
    id  =request.GET['id']
    pdata =  Product.objects.get(pk=id)
    return render(request,"product-detail.html",{"pdata":pdata})

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

def search(request):
    val = request.GET['val']
    products  =Product.objects.filter(productName__istartswith=val)
    return JsonResponse({"products":list(products.values())})
    

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
