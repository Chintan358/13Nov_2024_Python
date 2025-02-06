
from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("addstudent",addstudent,name="addstudent"),
    path("viewstudent",viewstudent,name="viewstudent"),
    path('deleteuser',deleteuser,name="deleteuser"),
    path('userbyid',userbyid,name="userbyid"),
    path('updatestudent',updatestudent,name="updatestudent"),
    path('searchstudent',searchstudent,name='searchstudent')

]
