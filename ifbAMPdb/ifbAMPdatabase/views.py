from django.shortcuts import render , get_object_or_404, render_to_response
from searchEngine.models import peptide
from blog.views import homeBlog
from searchEngine.views import *

# Create your views here.

def home(request):
	reqHomeBlog = homeBlog()
	pep = peptide.objects.order_by()[:2]
	data = {
	'peptides':pep,
	reqHomeBlog[0]:reqHomeBlog[1]
	}
	return render(request, 'home.html',data )

def homeData():
	pep = peptide.objects.order_by()[:2]
	return {'peptides': pep}

#def search(request):
#	pep = peptide.objects.all()
#	return render(request, 'search.html', {'peptide': pep})


