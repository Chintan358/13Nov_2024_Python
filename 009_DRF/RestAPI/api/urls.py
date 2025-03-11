
from django.urls import path
from api.views import *

urlpatterns = [
    
    path("students/",viewstduents,name="students"),
    path("addstudents/",addstudents,name="students")
]
