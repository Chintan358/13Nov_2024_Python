

from django.contrib import admin
from django.urls import path,include
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("",index,name="index"),
    path("adduser/",adduser,name="adduser"),
    path("deleteuser/<id>",deleteuser,name="deleteuser"),
    path("edituser/<id>",edituser,name="edituser")
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)