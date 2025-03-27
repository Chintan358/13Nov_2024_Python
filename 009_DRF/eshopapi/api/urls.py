from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from api.views import *
from rest_framework.authtoken import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
        path("categories",CategoryAPI.as_view()),
        path("products",ProductApI.as_view()),
        path("users",registerUser,name="users"),
        path('api-token-auth/', views.obtain_auth_token),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path("cattegorygen",CategoryGenrice.as_view(),name="catgen")
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)