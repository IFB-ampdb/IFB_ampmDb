from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name='Home'),
	url(r'^ampBasicSeach/$', views.ampBasicSearch, name='ampBasicSeach'),
	url(r'^peptide/(?P<pk>[A-Za-z1-9.:]+)/$', views.detail, name='AMP Details'),
	url(r'^search/advanced/$', views.advSearch, name='Advanced Search'),
	url(r'^search/advanced/resoults', views.advSearchResoults, name='Advanced Resoults'),
	url(r'', include('blog.urls')),
	url(r'^admin/', admin.site.urls),
]
