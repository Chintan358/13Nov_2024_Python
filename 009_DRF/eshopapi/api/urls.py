from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from api.views import *
from rest_framework.authtoken import views

urlpatterns = [
        path("categories",CategoryAPI.as_view()),
        path("products",ProductApI.as_view()),
        path("users",registerUser,name="users"),
        path('api-token-auth/', views.obtain_auth_token)
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)