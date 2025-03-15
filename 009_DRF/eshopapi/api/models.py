from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=20)


class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_price = models.FloatField()
    product_qty = models.IntegerField()
    product_image = models.ImageField(upload_to="product_images")

class Cart(models.Model):
    user  =models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()


class Order(models.Model):
     user  =models.ForeignKey(User,on_delete=models.CASCADE)
     total = models.FloatField()
     payment_type = models.CharField(max_length=20)
     address = models.TextField(max_length=500)

class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()
