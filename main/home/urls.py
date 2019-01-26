from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^addproduct/$', addproduct, name='addproduct'),
    url(r'^newproduct/$', newproduct, name='newproduct'),

]