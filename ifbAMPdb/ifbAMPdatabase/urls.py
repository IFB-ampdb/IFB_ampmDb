from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'', include('blog.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.home, name='Home'),
	url(r'^search/$', views.search, name='Search'),
	url(r'^adv_search/$', views.adv_search, name='Advanced Search'),
	url(r'^peptide/(?P<pk>)/$', views.detail, name='AMP Detailes'),
	url(r'^ampBasicSeach/$', views.ampBasicSearch, name='ampBasicSeach'),
]
