from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^search/$', views.search, name='Search'),
    url(r'^amp/(?P<pk>)/$', views.ampInfo, name='AMP Info'), 
]
