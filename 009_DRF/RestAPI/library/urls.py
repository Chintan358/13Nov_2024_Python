

from django.urls import path
from library.views import *

urlpatterns = [

        path("viewbooks",viewbooks,name='viewbooks'),
        path('addbooks',addbooks,name="addbooks"),
        path('books/author/<id>',bookbyauthor,name='bookbyauthor')
]
