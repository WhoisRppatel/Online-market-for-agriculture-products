from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserInfo


class SignUpForm(UserCreationForm):
   # dob = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    pass
    #class Meta:
     #   model = User
      #  fields = ('username', 'dob', 'password1', 'password2', )