from django.shortcuts import render,HttpResponse
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from api.models import *
from api.serealizer import *
from rest_framework.authtoken.models import Token
# Create your views here.
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(["post"])
def registerUser(request):
    data = UserSerializer(data=request.data)
    if not data.is_valid():
            return Response({"status":"202","Errors":data.errors,"message":"something went wrong"})
    data.save()
    
    
    return Response({"message":"Data Inserted","data":data.data})

class CategoryAPI(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]



    def get(self, request):
        
        allCategories = Category.objects.all()
        data = CategorySerializer(allCategories,many=True)
        return Response(data.data)
    
    def post(self, request):
        data = CategorySerializer(data=request.data)
        if not data.is_valid():
            return Response({"status":"202","Errors":data.errors,"message":"something went wrong"})
        data.save()
        return Response({"message":"Data Inserted","data":data.data})
    
    def put(self, request):
        dataToUpdate = Category.objects.get(pk=request.data['id'])
        updatedData = CategorySerializer(dataToUpdate,request.data)
        if not updatedData.is_valid():
              return Response({"status":"202","Errors":updatedData.errors,"message":"something went wrong"})
        updatedData.save()
        return Response({"message":"Data Updated","data":updatedData.data})
    
    def delete(self, request):
        try :
            dataTodelete = Category.objects.get(pk=request.data['id'])
            dataTodelete.delete()
            return Response({"message":"Data Deleted"})
        except Exception as e:
            return Response({"mesaage":str(e)})
        

class ProductApI(APIView):

    def get(self,request):
        allproducts = Product.objects.all()
        data = ProductSerializer(allproducts,many=True)
        return Response(data.data)
    
    def post(self, request):
        data = ProductSerializer(data=request.data)
        if not data.is_valid():
            return Response({"status":"202","Errors":data.errors,"message":"something went wrong"})
        data.save()
        return Response({"message":"Data Inserted","data":data.data})