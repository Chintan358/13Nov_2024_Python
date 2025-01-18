
from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [

    path("",loginpage,name="loginpage"),
    path("reg/",reg,name="reg"),
    path("home/",home,name="home"),
    path("userreg",userreg,name="userreg"),
    path("userlogin",userlogin,name="userlogin"),
    path("userlogout",userlogout,name="userlogout")
]
