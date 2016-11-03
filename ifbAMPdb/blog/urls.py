from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/post/(?P<pk>\d+)/$', views.blogPost, name='blog_post'),
]
