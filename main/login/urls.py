
from django.conf.urls import url
from home.views import *
from .views import *

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^adduser/$', adduser, name="adduser"),
    #url(r'^signup/$', signup),
    url(r'^signup/$', signup),
    url(r'^signedup/$', signedup),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout,name='logout'),
    url(r'^invalidlogin/$', invalidlogin),
    url(r'^profile/$',profile,name="profile"),
    url(r'^$', login),

]