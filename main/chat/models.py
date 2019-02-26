from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django import forms
# Create your models here.
class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver')
    message=models.CharField(max_length=256)
    #time=models.DateTimeField()