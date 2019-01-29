from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^addproduct/$', addproduct, name='addproduct'),
    url(r'^addproductprice/$', addproductprice, name='addproductprice'),
    url(r'^newproduct/$', newproduct, name='newproduct'),
    url(r'^loggedin/$', loggedin,name='loggedin'),
    url(r'^addprice/$', addprice),
    url(r'^today/$', today,name='today'),
]