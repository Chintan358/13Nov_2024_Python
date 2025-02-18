from django.shortcuts import render
from studentapp.models import *
from django.core.paginator import Paginator
from django.db.models import Sum
# Create your views here.
def index(request):
    studentData = Student.objects.all()

    paginator = Paginator(studentData, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    return render(request, 'index.html',{"studentData":page_obj})

def marks(request,id):
    # studentId = StudentId.objects.get(student_id=id)
    # student = Student.objects.get(student_id=studentId)

    rank =  Student.objects.annotate(totalmarks = Sum("marks__marks")).order_by('-totalmarks')
    count = 0
    for i in rank:
        # print(i.totalmarks,i.student_id.student_id)
        count+=1
        if i.student_id.student_id==id:
            print(i.totalmarks)
            break
  
    studentMarks = Marks.objects.filter(student__student_id__student_id=id)
    std = studentMarks[0].student
    total =  studentMarks.aggregate(total = Sum("marks"))
   

    return render(request, 'marks.html', {"studentMarks":studentMarks,"std":std,"total":total,"count":count})