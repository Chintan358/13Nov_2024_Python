from django.shortcuts import render
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"index.html")

def countries(request):
    allCountris  =Country.objects.all()
    return JsonResponse({"data":list(allCountris.values())})

def states(request):
    allstates = State.objects.filter(country_id=request.GET['cid'])
    return JsonResponse({"data":list(allstates.values())})

def cities(request):
    allCities = City.objects.filter(state_id=request.GET['sid'])
    return JsonResponse({"data":list(allCities.values())})