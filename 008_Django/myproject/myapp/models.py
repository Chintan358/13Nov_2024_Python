from django.db import models

# Create your models here.

class MyUser(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10,null=True)
    lang = models.CharField(max_length=50,null=True)
    education = models.CharField(max_length=10,null=True)
    image = models.ImageField(upload_to="img",null=True)


    def __str__(self):
        return self.uname+" "+self.email+" "+self.phone