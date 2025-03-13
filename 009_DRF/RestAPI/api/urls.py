
from django.urls import path
from api.views import *

urlpatterns = [
    
    path("students/",viewstduents,name="students"),
    path("addstudents/",addstudents,name="students"),
    path("updatestudents/<id>",updatestudents,name="updatestudents"),
    path("deletestudents/<id>",deletestudents,name="deletestudents")
]
