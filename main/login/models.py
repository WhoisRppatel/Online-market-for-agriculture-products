from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    userid = models.OneToOneField(User,on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    mob = models.CharField(max_length=10)
# Create your models here.
