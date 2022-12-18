from fileinput import filename
from turtle import onclick
from django.db import models
import datetime
import os
from django.contrib.auth.models import User


# Create your models here.
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y%m%d%H:%H:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('media/',filename)

class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=False)
    description=models.TextField(max_length=250,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")

    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.TextField(max_length=500,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Product(models.Model):

    category =models.ForeignKey(Category,on_delete=models.CASCADE)
    product_id=models.AutoField
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=True,blank=False)
    small_description=models.CharField(max_length=250,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)

    status=models.BooleanField(default=False,help_text="0-default,1-Hidden")

    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    tag=models.CharField(max_length=150,null=False,blank=False)
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.TextField(max_length=500,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)



      


class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=200)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField(max_length=800)
    image=models.FileField(upload_to="image/",max_length=250,null=True,default=None)
    def __str__(self):
        return self.product_name

class Advatisment(models.Model):
    image_1=models.FileField(upload_to="image/",max_length=250,null=True,default=None)
    image_2=models.FileField(upload_to="image/",max_length=250,null=True,default=None)
    image_3=models.FileField(upload_to="image/",max_length=250,null=True,default=None)
    image_sandle_1=models.FileField(upload_to="image/",max_length=250,null=True,default=None)
    image_sleeper_1=models.FileField(upload_to="image/",max_length=250,null=True,default=None)
class Customer(models.Model):
     
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    
    email=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=111)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default="")
    
    
