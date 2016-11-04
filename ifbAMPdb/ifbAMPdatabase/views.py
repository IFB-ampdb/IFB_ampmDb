from django.shortcuts import render, get_object_or_404, render_to_response
from .models import peptide
from blog.views import homeBlog
#from django.db.models import Q

# Create your views here.

def home(request):
	#reqHomeData = homeData()
	reqHomeBlog = homeBlog()
	pep = peptide.objects.order_by()[:2]
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

def resoult(request,pk):
	pep = get_object_or_404(peptide, pk=pk)
	return render(request,'ampinfo.html', {'peptide' : pep})


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
	else not org is '':
		pep = peptide.objects.filter(organism = org)
		for qr in pep:
			pepList.append(qr)
		return	render(request, 'resoult.html',{'peptides':pepList, 'searchTerms':searchTerms})
		'''
	else:
		return	render(request, 'notFound.html', {'searchTerms':searchTerms})
		'''

#def ampAdvSearch()

'''
class ampBasicSearch():
	def get_queryset(self):
		result = super(BlogSearchListView, self).get_queryset()

		query = self.request.GET.get('q')
		if query:
			query_list = query.split()
			result = result.filter(
				reduce(operator.and_,
					   (Q(title__icontains=q) for q in query_list)) |
				reduce(operator.and_,
					   (Q(content__icontains=q) for q in query_list))
			)

		return result
'''
