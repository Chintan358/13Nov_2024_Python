

from django.contrib import admin
from django.urls import path,include
from myapp.views import *
urlpatterns = [
    
    path("",index,name="index"),
    path("adduser/",adduser,name="adduser"),
    path("deleteuser/<id>",deleteuser,name="deleteuser"),
    path("edituser/<id>",edituser,name="edituser")
]
