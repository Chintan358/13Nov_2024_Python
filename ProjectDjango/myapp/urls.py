
from django.contrib import admin
from django.urls import path,include
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   
   path("",index,name="index"),
   path("home",home,name="home"),
   path("about",about,name="about"),
   path("contact",contact,name="contact"),
   path("cart",cart,name="cart"),
   path("shop",shop,name="shop"),
   path("shopdetails",shopdetails,name="shopdetails"),
   path("registration",registration,name="registration"),
   path("login",loginuser,name="login"),
   path("logout",userlogout,name="logout")


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)