from django.shortcuts import render, get_object_or_404, render_to_response
from .models import peptide
from blog.views import homeBlog
from random import randrange
#from django.db.models import Q

# Create your views here.

def home(request):
	#reqHomeData = homeData()
	reqHomeBlog = homeBlog()
	pep=[]
	index= randrange(0,50)
	pep.append(peptide.objects.filter(pk=index)
	index= randrange(0,50)
	pep.append(peptide.objects.filter(pk=index)
	data = {
	'peptide':pep,
	reqHomeBlog[0]:reqHomeBlog[1]
	}
	return render(request, 'home.html',data )

def homeData():
	pep = peptide.objects.order_by()[:2]
	return {'peptide': pep}

def adv_search(request):
	return render(request, 'adv_search.html')

def search(request):
	pep = peptide.objects.all()
	return render(request, 'search.html', {'peptide': pep})

def detail(request,pk):
	pep = get_object_or_404(peptide, pdb_id = pk)
	return render(request,'detail.html', {'peptide' : pep})


def ampBasicSearch(request):
	pdbId = None
	org = None
	searchTerms = []
	pepList = []
	if 'pdbId' in request.GET:
		pdbId = request.GET['pdbId']
		if not pdbId is '':
			searchTerms.append(pdbId)
	if 'org' in request.GET:
		org = request.GET['org']
		if not org is '':
			searchTerms.append(org)
	#search Conditions
	if not pdbId is	''	and	not	org	is	'':
		pep = peptide.objects.filter(pdb_id = pdbId).filter(organism = org)
		for qr in pep:
			pepList.append(qr)
		return	render(request, 'resoult.html',{'peptides':pepList, 'searchTerms':searchTerms})

	elif not pdbId is '':
		pep = peptide.objects.filter(pdb_id = pdbId)
		for qr in pep:
			pepList.append(qr)
		return	render(request, 'resoult.html',{'peptides':pepList, 'searchTerms':searchTerms})
	else:
		pep = peptide.objects.filter(organism = org)
		for qr in pep:
			pepList.append(qr)
		return	render(request, 'resoult.html',{'peptides':pepList, 'searchTerms':searchTerms})
