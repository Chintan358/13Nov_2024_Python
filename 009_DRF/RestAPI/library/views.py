from django.shortcuts import render
from library.models import *
from library.serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['get'])
def viewbooks(request):
    books = Book.objects.all()
    bookdata = BookSerializer(books,many=True)
    return Response({"books":bookdata.data})

@api_view(['post'])
def addbooks(request):
    try :
        bookdata = BookSerializer(data=request.data)
        if not bookdata.is_valid():
            return Response({'status':'202','message':'Something went wrong!','errors':bookdata.errors})
        bookdata.save()
        return Response({'status':'200','message':'Book inserted !','errors':bookdata.data})
    except Exception as e:
        print(e)
        return Response({'message':'Something went wrong'})
    
@api_view(['get'])
def bookbyauthor(request,id):
    books = Book.objects.filter(author=id)
    bookdata = BookSerializer(books,many=True)
    return Response({"books":bookdata.data})