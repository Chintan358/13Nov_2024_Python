
from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("addstudent",addstudent,name="addstudent"),
    path("viewstudent",viewstudent,name="viewstudent")
]
