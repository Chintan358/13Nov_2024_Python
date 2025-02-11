from django.db import models

# Create your models here.
class Department(models.Model):
    deptname = models.CharField(max_length=50)

class StudentId(models.Model):
    student_id = models.CharField(max_length=20)

class Student(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentId, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    email=models.CharField(max_length=50)

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()





