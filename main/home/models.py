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
    pic_path=models.ImageField(upload_to = 'images/' , default='/nothing')
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='owner_name')
    status=models.BooleanField(default=False)
    quantity=models.FloatField(default=1.0)
    time=models.DateTimeField()