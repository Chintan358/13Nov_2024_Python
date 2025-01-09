from django.db import models

# Create your models here.

class MyUser(models.Model):
    uname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.uname+" "+self.email+" "+self.phone