
from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [

    path("",userlogin,name="userlogin"),
    path("reg/",reg,name="reg"),
    path("home/",home,name="home"),
    path("userreg",userreg,name="userreg")
]
