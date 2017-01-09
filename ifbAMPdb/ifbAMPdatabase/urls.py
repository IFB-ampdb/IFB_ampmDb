from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name='Home'),
	url(r'^search/peptide/(?P<pk>[A-Za-z1-9.:]+)/$', views.detail, name='PeptideDetails'),
	url(r'^search/advanced/$', views.advSearch, name='AdvancedSearch'),
	url(r'^search/resoults/basic/', views.ampBasicSearch, name='SearchResoults'),
	url(r'^search/resoults/advanced/', views.advSearchResoults, name='AdvancedResoults'),
	url(r'', include('blog.urls')),
	url(r'^admin/', admin.site.urls),
]
