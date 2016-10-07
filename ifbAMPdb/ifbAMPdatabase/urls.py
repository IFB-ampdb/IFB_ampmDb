from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='Home'),
    url(r'^search/$', views.search, name='Search'),
    url(r'^adv_search/$', views.adv_search, name='Advanced Search'),
    url(r'^amp/(?P<pk>)/$', views.resoult, name='AMP Info'), 
]
