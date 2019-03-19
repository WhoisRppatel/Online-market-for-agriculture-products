from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    picture = forms.ImageField()

class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=30,null=True)
    description=models.CharField(max_length=100,null=True)
    price=models.IntegerField()
    pic_path=models.ImageField(upload_to = 'static/images/' , default='/nothing')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner_name')
    status=models.BooleanField(default=False)
    quantity=models.FloatField(default=1.0)
    time=models.DateTimeField()

class Market(models.Model):
    city=models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=30)
    minprice=models.IntegerField()
    maxprice=models.IntegerField()
    time=models.DateTimeField()

class Deal(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='buyer_name')
    seller=models.ForeignKey(User,on_delete=models.CASCADE,related_name='seller_name',null=True)
    price_sold=models.IntegerField()
    quantity_sold=models.FloatField(default=1.0)
    time=models.DateTimeField()
    status=models.BooleanField(default=False,null=True)

class Review(models.Model):
    rating=models.IntegerField()
    title=models.CharField(max_length=20)
    text=models.CharField(max_length=150)
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    from_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='from_user')
    time=models.DateTimeField()
    deal_id=models.ForeignKey(Deal,on_delete=models.CASCADE,default='1')