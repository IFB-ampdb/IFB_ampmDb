from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name='Home'),
	url(r'^search/peptide/(?P<pk>[A-Za-z1-9.:]+)/$', views.detail, name='PeptideDetails'),
	url(r'^search/advanced/$', views.advSearch, name='AdvancedSearch'),
	url(r'^search/results/basic/', views.ampBasicSearch, name='SearchResults'),
	url(r'^search/results/advanced/', views.advSearchResults, name='AdvancedResults'),
	url(r'', include('blog.urls')),
	url(r'^admin/', admin.site.urls),
]
