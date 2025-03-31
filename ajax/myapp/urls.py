
from django.urls import path
from myapp.views import *
urlpatterns = [
    
    path("",index,name="index"),
    path("countries",countries,name="countries"),
    path("states",states,name="states"),
    path("cities",cities,name="cities")
]
