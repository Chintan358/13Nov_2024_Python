from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import *
from api.serealizer import *
# Create your views here.

@api_view(['post'])
def addstudents(request):
    ser =  StudentSerializer(data=request.data)
    if not ser.is_valid():
                return Response({'status':'202','errors':ser.errors,'message':"something went wrong"})
    ser.save()
    return HttpResponse("post calling")

@api_view(['get'])
def viewstduents(request):
    allStudents = Student.objects.all()
    s_data = StudentSerializer(allStudents,many=True)
    print(s_data)
    return Response(data=s_data.data)