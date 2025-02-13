from django.shortcuts import render
from studentapp.models import *
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    studentData = Student.objects.all()

    paginator = Paginator(studentData, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'index.html',{"studentData":page_obj})

def marks(request,id):
    studentId = StudentId.objects.get(student_id=id)
    student = Student.objects.get(student_id=studentId)
    studentMarks = Marks.objects.filter(student=student)
    return render(request, 'marks.html', {"studentMarks":studentMarks})