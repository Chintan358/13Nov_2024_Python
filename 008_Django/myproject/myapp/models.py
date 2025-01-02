from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=30,null=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)


class Faculty(models.Model):
    faculty_name=models.CharField(max_length=30)
    faculty_subject=models.CharField(max_length=20)