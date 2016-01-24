from django.conf.urls import url
from . import views

urlpatterns = [
    # root: /
    url(r'^$', views.home, name='home'),
    #  /posts/
    url(r'^posts/$', views.post, name='posts'),
]