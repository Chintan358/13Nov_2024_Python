from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=50)
    categoryImage = models.ImageField(upload_to="catgory_images")

    def __str__(self):
        return self.categoryName


class Product(models.Model):
    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    productName=models.CharField(max_length=20)
    price=models.IntegerField()
    qty=models.IntegerField()
    productImage=models.ImageField(upload_to="product_images")

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    