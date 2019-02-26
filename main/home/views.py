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
from home.models import *
from datetime import datetime

#from django.utils.timezone import timezone
# Create your views here.
def loggedin(request):
    if request.user.username == "admin" or request.user.username == "rp":
        return render_to_response('home2.html')
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    request.session["uid"]=s.id
    print(s.usertype)
    return render_to_response('home.html', {"usertype": s.usertype})

def addproduct(request):
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    c = {}
    c.update(csrf(request))
    c.update({"usertype": s.usertype})
    return render_to_response('addproduct.html',c)

def addproductprice(request):
    c={}
    c.update(csrf(request))
    return render_to_response('addproductprice.html',c)

def newproduct(request):
    name = request.POST.get('name', '')
    category = request.POST.get('category', '')
    description = request.POST.get('description', '')
    quantity = float(request.POST.get('quantity', ''))
    price1 = int(request.POST.get('price', ''))
    time=datetime.now()
    p = Product(name=name,category=category,quantity=quantity,time=time,owner=request.user,description=description,price=price1)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            p.pic_path = form.cleaned_data['picture']
            p.save()
            return render_to_response('home.html')
        else:
            p.save()
            return render_to_response('home.html')
    else:
        print("adfsvkhdbmhefsy")
        return render_to_response('home.html')

def addprice(request):
    c={}
    c.update(csrf(request))
    name=request.POST.get('name','')
    category=request.POST.get('category','')
    pricelow=request.POST.get('pricelow','')
    pricehigh=request.POST.get('pricehigh','')
    city=request.POST.get('city','')
    time=datetime.now()
    M=Market(city=city,category=category,minprice=int(pricelow),maxprice=int(pricehigh),time=time,name=name)
    if int(pricelow)>int(pricehigh):
        return render_to_response('addproductprice.html',c)
    else:
        M.save()
        return render_to_response('addproductprice.html',c)

def today(request):
    c={}
    c.update(csrf(request))
    M = Market.objects.all()
    c.update({"M": M})
    return render_to_response('today.html',c)

def viewproducts(request):
    c={}
    c.update(csrf(request))
    market=Market.objects.all()
    c.update({"market":market})
    return render_to_response('admin_market.html',c)

def updateprice(request,product_id):
    c={}
    c.update(csrf(request))
    print(product_id)
    min=request.POST.get('lmin','')
    max=request.POST.get('lmax','')
    #print(min)
    #print(max)
    #print("Hello")
    market=Market.objects.get(id=product_id)
    if (min != '') & (max != '') & (min.isnumeric() & min.isnumeric()):
        if(int(min) < int(max)):
            market.minprice=min
            market.maxprice=max
            market.save()
    print(market)
    return redirect('viewproducts')
def nearby(request):
    Ans=[]
    u=request.user
    s=UserInfo.objects.get(userid=u)
    if s.usertype=="Merchant":
        Q=Product.objects.filter(owner=u).values_list('name', flat=True)
        print(Q)
        S=UserInfo.objects.filter(usertype="Farmer",city=s.city)
        print(S)
        for i in S:
            print(i)
            p=Product.objects.filter(owner=i.userid)
            for j in p:
                if j.name in Q:
                    Ans.append(j)
    else:
        Q=Product.objects.filter(owner=u).values_list('name', flat=True)
        print(Q)
        S=UserInfo.objects.filter(usertype="Merchant",city=s.city)
        print(S)
        for i in S:
            print(i)
            p=Product.objects.filter(owner=i.userid)
            for j in p:
                if j.name in Q:
                    Ans.append(j)
    print(Ans)                
    return render_to_response('nearby.html', {"usertype1": s.usertype,"L":Ans})


def report(request):
    c={}
    c.update(csrf(request))
    if(request.session["uid"]):
        uid=request.session["uid"]
    if(request.session["usertype"] == "Merchant"):
        deals=Deal.objects.filter(buyer=uid)
    c.update({"deals":deals})
    print(c)
    return render_to_response('report.html',c)

def review(request):
    to_user=request.POST.get('to_user','')
    to_user=User.objects.get(id=to_user)
    print(to_user.username)
    product_id=request.POST.get('product_id','')
    #print(to_user.username)
    c={}
    c.update(csrf(request))
    c.update({'to_user':to_user})
    c.update({'product_id':product_id})
    return render_to_response('review.html',c)

def addreview(request):
    title=request.POST.get('title','')
    rating=request.POST.get('rating','')
    text=request.POST.get('text','')
    from_user=request.session["uid"]
    to_user=request.POST.get('to_user','')
    to_user=User.objects.get(id=to_user)
    from_user=User.objects.get(id=from_user)
    time=datetime.now()
    r=Review(title=title,rating=rating,text=text,from_user=from_user,to_user=to_user,time=time)
    r.save()
    return redirect('report')
