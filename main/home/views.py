from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.timezone import timezone
# Create your views here.
def addproduct(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('addproduct.html',c)

def newproduct(request):
    name = request.POST.get('name', '')
    catagory = request.POST.get('catagory', '')
    date_time=timezone.now()
    description = request.POST.get('description', '')
    quantity = request.POST.get('quantity', '')
    price = request.POST.get('price', '')

    p = Product(name=name,catagory=catagory,time=date_time,description=description,price=price)
    p.save()
    return render_to_response('home.html')