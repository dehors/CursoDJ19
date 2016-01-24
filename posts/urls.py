from django.conf.urls import url
from . import views

urlpatterns = [
    # root: /
    url(r'^$', views.home, name='home'),
    #  /posts/
    url(r'^posts/$', views.post, name='posts'),
    #  /posts/5/
    url(r'^posts/(?P<id>[0-9]+)/$', views.postshow, name='postshow'),
    #  /posts/new/
    url(r'^posts/new/$', views.postcreate, name='postcreate'),
]