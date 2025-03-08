from django.contrib import admin
from myapp.models import *
# Register your models here.

class categorymodel(admin.ModelAdmin):
    list_display = ["categoryName","categoryImage"]

class productmodel(admin.ModelAdmin):
    list_display=["category","productName","price","qty","productImage"]


admin.site.register(Category,categorymodel)
admin.site.register(Product,productmodel)
admin.site.register(Cart)
admin.site.register(Address)