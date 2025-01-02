from django.shortcuts import render,HttpResponse

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