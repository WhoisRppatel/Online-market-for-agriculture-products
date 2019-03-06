from django.conf.urls import url
from .views import *
from chat.views import *

urlpatterns = [
    url(r'^addproduct/$', addproduct, name='addproduct'),
    url(r'^addproductprice/$', addproductprice, name='addproductprice'),
    url(r'^newproduct/$', newproduct, name='newproduct'),
    url(r'^nearby/$', nearby, name='nearby'),
    url(r'^loggedin/$', loggedin,name='loggedin'),
    url(r'^addprice/$', addprice),
    url(r'^chat/$', chat,name='chat'),
    url(r'^chatme/(?P<username>\w+)$', chatme,name='chatme'),
    url(r'^load_messages/(?P<username>\w+)$', LoadMessages,name='loadmessages'),
    url(r'^today/$', today,name='today'),
    url(r'^viewproducts/updateprice/(?P<product_id>\d+)$', updateprice,name='updateprice'),
    url(r'^viewproducts/$', viewproducts,name='viewproducts'),
    url(r'^report/$', report,name='report'),
    url(r'^review/$', review,name='review'),
    url(r'^addreview/$', addreview,name='addreview'),
    url(r'^deal/$', deal,name='deal'),
    url(r'^adddeal/$', adddeal,name='adddeal'),
]