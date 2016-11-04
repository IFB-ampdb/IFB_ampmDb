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
	print('ampBasicSearch view')
	pdbId = None
	org = None
	if 'pdbId' in request.GET:
		pdbId = request.GET['pdbId']
		print('pdbId assigned', pdbId)
	if 'org' in request.GET:
		org = request.GET['org']
		print('org assigned', org)
	pepList = []
	if not pdbId is	''	and	not	org	is	'':
		print('in big if')
		pep = peptide.objects.filter(pdb_id = pdbId).filter(organizm = org)
		for qr in pep:
			pepList.append(qr)
	
		for i in pepList:
			print(i, type(i))
		return	render(request, 'resoult.html',{'peptides':pepList})
	elif not pdbId is '':
		pep = peptide.objects.filter(pdb_id = pdbId)
		if type(pep) is not list:
			pepList.append(pep)
		return	render(request, 'resoult.html',{'peptides':pepList})
	elif not org is '':
				pep = peptide.objects.filter(organizm = org)
				if type(pep) is not list:
					pepList.append(pep)
				return	render(request, 'resoult.html',{'peptides':pepList})
	else:
		return	render(request, 'notFound.html')

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
