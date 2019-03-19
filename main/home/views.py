from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import messages
from login.models import *
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
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    c = {}
    c.update(csrf(request))
    c.update({"usertype": s.usertype})
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
            return render_to_response('home.html',c)
        else:
            p.save()
            return render_to_response('home.html',c)
    else:
        print("adfsvkhdbmhefsy")
        return render_to_response('home.html',c)

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
    mina=request.POST.get('lmin','')
    maxa=request.POST.get('lmax','')
    #print(min)
    #print(max)
    #print("Hello")
    market=Market.objects.get(id=product_id)
    if (mina != '') & (maxa != '') & (mina.isnumeric() & mina.isnumeric()):
        if(int(mina) < int(maxa)):
            market.minprice=mina
            market.maxprice=maxa
            market.save()
    print(market)
    return redirect('viewproducts')
def nearby(request):
    c={}
    c.update(csrf(request))
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
    c.update({"usertype": s.usertype,"L":Ans})                
    return render_to_response('nearby.html',c)


def report(request):
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    c = {}
    c.update(csrf(request))
    c.update({"usertype": s.usertype})
    c.update(csrf(request))
    if s.usertype == "Merchant":
        deals=Deal.objects.filter(buyer=s.userid,status=True)
    else:
        deals=Deal.objects.filter(seller=s.userid,status=True)
    c.update({"deals":deals})
    #print(c)
    return render_to_response('report.html',c)

def review(request):
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    c = {}
    c.update(csrf(request))
    c.update({"usertype": s.usertype})
    seller=request.POST.get('seller','')
    buyer=request.POST.get('buyer','')
    seller=User.objects.get(id=seller)
    buyer=User.objects.get(id=buyer)
    #print(to_user.username)
    deal_id=request.POST.get('deal_id','')
    #print(to_user.username)
    c.update(csrf(request))
    c.update({'seller': seller})
    c.update({'buyer': buyer})
    c.update({'deal_id':deal_id})
    if s.usertype == "Merchant":
        c.update({"to_user":seller})
    else:
        c.update({"to_user":buyer})
    try:
        if s.usertype == "Merchant":
            prev_review=Review.objects.get(deal_id=deal_id,from_user=buyer.id )
        else:
           prev_review=Review.objects.get(deal_id=deal_id,from_user=seller.id ) 
        print(prev_review)
        c.update({'prev_review':prev_review})
    except:
        print("error")
        pass
    return render_to_response('review.html',c)

def addreview(request):
    prevrate=0
    title=request.POST.get('title','')
    rating=request.POST.get('rating','')
    rating=int(rating)
    text=request.POST.get('text','')
    from_user=request.user
    to_user=request.POST.get('to_user','')
    deal_id=request.POST.get('deal_id','')
    to_user=User.objects.get(id=to_user)
    print(deal_id)
    from_user=User.objects.get(id=from_user.id)
    deal=Deal.objects.get(id=deal_id)
    time=datetime.now()
    try:
        prev_review=Review.objects.get(deal_id=deal_id,to_user_id=to_user.id)
        prevrate=prev_review.rating
        prev_review.delete()
    except:
        print("In exception")
    finally:
        r=Review(title=title,rating=rating,text=text,from_user=from_user,to_user=to_user,time=time,deal_id=deal)
        U=UserRating.objects.get(userid=to_user)
        print(U)
        t=rating-prevrate
        print(t,U.totalrating)
        U.totalrating=t+U.totalrating

        if prevrate==0:
            U.totalcount+=1
        U.save()    
        r.save()
    return redirect('report')

def deal(request):
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    c = {}
    c.update(csrf(request))
    c.update({"usertype": s.usertype})
    c.update(csrf(request))
    prod=request.POST.get('productId','')
    prod=Product.objects.get(id=prod)
    uid=request.user
    c.update({'prod':prod})
    c.update({'uid':uid})
    return render_to_response('adddeal.html',c)

def adddeal(request):
    c={}
    c.update(csrf(request))
    prod=request.POST.get('productId','')
    prod=Product.objects.get(id=prod)
    user=request.user
    price=request.POST.get('price','')
    quantity=request.POST.get('quantity','')
    quantity=int(quantity)
    deal=Deal(product_id=prod,buyer=user,seller=prod.owner,status=False,price_sold=price,quantity_sold=quantity,time=datetime.now())
    deal.save()
    return redirect('nearby')

def requestdeal(request):
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    c = {}
    c.update(csrf(request))
    c.update({"usertype": s.usertype})
    c.update(csrf(request))
    deal=Deal.objects.filter(seller=request.user,status=False)
    c.update({"Deal":deal})
    return render_to_response('requestdeal.html',c)

def approve(requset,id):
    deal=Deal.objects.get(id=id)
    prod=Product.objects.get(id=deal.product_id.id)
    if prod.quantity < deal.quantity_sold :
        deal.delete()
    elif prod.quantity==deal.quantity_sold :
        deal.status=True
        prod.quantity=0
        prod.status=True
        prod.save()
        deal.save()
    else:
        prod.quantity=prod.quantity-deal.quantity_sold
        prod.save()
        deal.status=True
        deal.save()
    return redirect('requestdeal')
def decline(request,id):
    deal=Deal.objects.get(id=id)
    deal.delete()       
    return redirect('requestdeal')

def pendingdeal(request):
    c={}
    u=request.user
    s=UserInfo.objects.get(userid=u)
    request.session["usertype"]=s.usertype
    c.update(csrf(request))
    c.update({"usertype": s.usertype})
    c.update(csrf(request))
    deal=Deal.objects.filter(buyer=request.user,status=False)
    c.update({"Deal":deal})
    return render_to_response('pendingdeal.html',c)    