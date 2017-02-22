from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^search/peptide/(?P<pk>[A-Za-z0-9.:]+)/$', views.detail, name='PeptideDetails'),
	url(r'^search/advanced/$', views.advSearch, name='AdvancedSearch'),
	url(r'^search/results/basic/', views.ampBasicSearch, name='SearchResults'),
	url(r'^search/results/advanced/', views.advSearchResults, name='AdvancedResults'),
]
