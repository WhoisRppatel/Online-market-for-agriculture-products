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
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def chat(request):
    print(request.user)
    u=request.user
    ss=UserInfo.objects.get(userid=u)
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
    c.update({"usertype":ss.usertype})
    c.update({"C1": chater})
    return render_to_response('chat.html',c)

@login_required
def LoadMessages(request,username):
    uu=request.user
    s=UserInfo.objects.get(userid=uu)
    current=User.objects.get(username=request.user.username)
    U=User.objects.get(username=username)
    SS=U.first_name
    SP=U.username
    M=Message.objects.filter(sender=current ,receiver=U) 
    M=M | Message.objects.filter(sender=U ,receiver=current)
    M=M.order_by('id')
    c = {}
    c.update(csrf(request))
    c.update({"usertype":s.usertype})
    c.update({"M1": M})
    c.update({"SP": SP})
    c.update({"SS":SS})
    return render_to_response('messages.html',c)

@login_required    
def AddMessage(request,username):
    #print(request.session.usertype)
    m = request.POST.get('message', '')
    U1=User.objects.get(username=request.user.username)
    U2=User.objects.get(username=username)
    M=Message(sender=U1,receiver=U2,message=m)
    M.save()
    return chatme(request,username)

@login_required
def chatme(request, username):
    uu=request.user
    s=UserInfo.objects.get(userid=uu)
    U=User.objects.get(username=username)
    SS=U.first_name
    SP=U.username
    c = {}
    c.update({"SP": SP})
    c.update(csrf(request))
    c.update({"SS":SS})
    c.update({"usertype":s.usertype})
    return render_to_response("chatme.html", c)