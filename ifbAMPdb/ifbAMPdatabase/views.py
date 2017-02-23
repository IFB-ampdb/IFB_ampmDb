from django.shortcuts import render , get_object_or_404, render_to_response
from searchEngine.models import peptide
from blog.views import homeBlog
from searchEngine.views import homeData
#from searchEngine.views import *

# Create your views here.

def home(request):
	data = {}
	data.update(homeBlog())
	data.update(homeData())
	return render(request, 'home.html',data )


