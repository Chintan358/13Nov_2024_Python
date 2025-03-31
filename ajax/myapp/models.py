from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

class State(models.Model):
    name = models.CharField(max_length=50)
    country_id=models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=50)
    state_id=models.ForeignKey(State,on_delete=models.CASCADE)