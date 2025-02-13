from faker import Faker
fake = Faker()
import random
from studentapp.models import *


def generate_data(n=50):
    dept = Department.objects.all()
   
    for i in range(n):
        d_index = random.randint(0,len(dept)-1)
        d = dept[d_index]
        fname = fake.name().split()[0]
        lname = fake.name().split()[1]
        email=fake.email()
        age  = random.randint(20,40)
        s_id = StudentId.objects.create(student_id=f'STU_{random.randint(100,999)}')  
        Student.objects.create(dept=d,student_id=s_id,firstname=fname,lastname=lname,age=age,email=email)
       
def student_marks():
    students = Student.objects.all()
    for s in students:
        subject = Subject.objects.all()
        for sub in subject:
            marks = random.randint(0,100)
            Marks.objects.create(student=s, subject=sub, marks=marks)