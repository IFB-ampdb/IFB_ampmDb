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
		return	render(request, 'advResoults.html',{'peptides':pepList, 'searchTerms':searchTerms})

def advSearch(request):
	return render(request, 'advSearch.html')

def advSearchResoults(request):
	pdb_id = request.GET['pdb_id']
	hfobic_area = request.GET['hfobic_area']
	hfobic_avg = request.GET['hfobic_avg']
	hairpin = request.GET['hairpin']
	beta_sheet = request.GET['beta_sheet']
	alpha_helix = request.GET['alpha_helix']
	alpha_helix_beta_sheet = request.GET['alpha_helix_beta_sheet']
	alpha_helix_beta_sheet_hairpin = request.GET['alpha_helix_beta_sheet_hairpin']
	charge = request.GET['charge']
	m_dipol = request.GET['m_dipol']
	charge_amt_atm = request.GET['charge_amt_atm']
	m_dipol_amt_atm = request.GET['m_dipol_amt_atm']
	sequence = request.GET['sequence']
	organism = request.GET['organism'] 
	
	searchTerms= [{'PDB iD': pdb_id}, {'Hidrofobic Area':hfobic_area}, {'Average Hidrofobicity':hfobic_avg}, {'Hairpin':hairpin}, {'Beta Sheet':beta_sheet}, {'Aplha Helix':alpha_helix}, {'Alpha Helix Beta Sheet':alpha_helix_beta_sheet} , {'Alpha Helix Beta Sheet Hairpin':alpha_helix_beta_sheet_hairpin}, {'Charge':charge}, {'Dipolar Momentum':m_dipol}, {'Charge / Amout of Atoms':charge_amt_atm}, {'Dipolar Momentum / amout of atoms':m_dipol_amt_atm}, {'Sequence':sequence}, {'Organism':organism}]
	
	return render(request, 'advResoults.html', {'searchTerms':searchTerms})
