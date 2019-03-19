
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserInfo,UserRating
from .forms import SignUpForm

# Create your views here.
#for new login request add csrf and forward
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

#authenticate user retry for invalid
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        U=UserInfo.objects.get(userid=request.user)
        request.session["usertype"]=U.usertype
        #print(U.usertype)
        return HttpResponseRedirect('/home/loggedin/')
    else:
        c = {}
        c.update(csrf(request))
        c.update({"error": True})
        return render_to_response('login.html', c)

#new user request
def adduser(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('signup.html',c)

def signedup(request):
    return render_to_response('login.html', {"full_name": request.user.username, 'signup': True})


def invalidlogin(request):
    return render_to_response('invalidlogin.html')


def logout(request):
    c = {}
    c.update(csrf(request))
    auth.logout(request)
    return render_to_response('login.html', c)


def signup(request):
    unm = request.POST.get('username', '')
    pas = request.POST.get('password', '')
    mob = request.POST.get('mob', '')
    city = request.POST.get('city', '')
    name = request.POST.get('name', '')
    repas = request.POST.get('rpassword', '')
    email = request.POST.get('email', '')
    typeis=request.POST.get('typeis','')
    if repas == pas:
        if len(mob)==10 and (mob.isdigit()==True):
            s = User.objects.create_user(username=unm, password=pas, email=email,first_name=name)
            p = UserInfo(userid=s,name=name,mob=mob,city=city,usertype=typeis)
            d = UserRating(userid=s,totalrating=0,totalcount=0)
            s.save()
            p.save()
            d.save()
            return HttpResponseRedirect('/login/login/')
        else:
            messages.warning(request, 'Enter Valid Mobile Number')
            return HttpResponseRedirect('/login/adduser/')        
    else:
        messages.warning(request, 'Password fields do not match')
        return HttpResponseRedirect('/login/adduser/')

"""def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user..dob = form.cleaned_data.get('dob')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=user.username, password=raw_password)
            auth.login(request, user)
            return HttpResponseRedirect('/login/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})"""

   
def profile(request):
    c={}
    c.update(csrf(request))
    user=request.user
    userinfo=UserInfo.objects.get(userid=user)
    c.update({"uinfo":userinfo})
    rating=UserRating.objects.get(userid=user)
    c.update({"rating":rating})
    return render_to_response('profile.html',c)
