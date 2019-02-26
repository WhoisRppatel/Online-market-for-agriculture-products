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
    p=Message.objects.filter(receiver=request.user)
    chater=[]
    for i in s:
        chater.append(i.receiver)
    for i in p:
        chater.append(i.sender)    
    chater=list(set(chater))
    print(chater)
    c = {}
    c.update(csrf(request))
    c.update({"C1": chater})
    return render_to_response('chat.html',c)
def chatme(request,username):
    current=User.objects.get(username=request.user.username)
    U=User.objects.get(username=username)
    SS=U.first_name
    SP=U.username
    M=Message.objects.filter(sender=current,receiver=U) 
    S=Message.objects.filter(sender=U,receiver=current)
    c = {}
    c.update(csrf(request))
    c.update({"M1": M})
    c.update({"SP": SP})
    c.update({"M2": S})
    c.update({"SS":SS})
    return render_to_response('chatme.html',c)
    
def AddMessage(request,username):
    #print(request.session.usertype)
    m = request.POST.get('message', '')
    U1=User.objects.get(username=request.user.username)
    U2=User.objects.get(username=username)
    M=Message(sender=U1,receiver=U2,message=m)
    M.save()
    return chatme(request,username)    