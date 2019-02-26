from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import messages
from login.models import UserInfo
from .models import Message
from home.models import *
from datetime import datetime
# Create your views here.
def chat(request):
    print(request.user)
    s=Message.objects.filter(sender=request.user)
    print(s)
    chater=[]
    for i in s:
        if i.sender==request.user:
            chater.append(i.receiver)
            print(i.receiver)
        else:
            chater.append(i.sender)
            print(i.sender)    
    chater=list(set(chater))    
    c = {}
    c.update(csrf(request))
    c.update({"chaters": chater})
    return render_to_response('chat.html')