from django.conf.urls import url
from . import views

urlpatterns = [
    # root: /
    url(r'^$', views.home, name='home'),
]