from django.shortcuts import render,HttpResponse,redirect
from studentapp.models import *
from django.core.paginator import Paginator
from django.db.models import Sum
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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


def send_mail_page(request,id):
    
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
   


    context = {}

    html_message = render_to_string('marks.html',{"studentMarks":studentMarks,"std":std,"total":total,"count":count})
    plain_message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [studentMarks[0].student.email]
    send_mail( "Report Card", plain_message, email_from, recipient_list ,html_message=html_message)
    
    return redirect("index")