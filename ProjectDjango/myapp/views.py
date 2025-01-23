from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,"contact.html")

def cart(request):
    return render(request,"shoping-cart.html")

def shop(request):
    return render(request,"product.html")

def shopdetails(request):
    return render(request,"product-detail.html")

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')