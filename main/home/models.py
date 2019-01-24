from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):
    name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=30,null=True)
    description=models.CharField(max_length=100)
    price=models.IntegerField()
    #photo=models.ImageField
    owner=models.OneToOneField(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    qauntity=models.FloatField()
    time=models.DateTimeField()

