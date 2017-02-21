from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name='Home'),
	url(r'', include('searchEngine.urls')),
	url(r'', include('blog.urls')),
	url(r'^admin/', admin.site.urls),
]
