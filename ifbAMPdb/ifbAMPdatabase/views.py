from django.shortcuts import render, get_object_or_404, render_to_response
from .models import peptide
from blog.views import homeBlog

#from django.db.models import Q

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

def search(request):
	pep = peptide.objects.all()
	return render(request, 'search.html', {'peptide': pep})

def detail(request,pk):
	pep = get_object_or_404(peptide, pdb_id = pk)
	return render(request,'detail.html', {'peptide' : pep})


# Collects data from the Basic search in the Home Page and displays in the Resoult page.
def ampBasicSearch(request):
	pdbId = None
	org = None
	searchTerms = []
	pepList = []
	#Search items
	try:
		if 'pdbId' in request.POST:
			pdbId = request.POST['pdbId']
			if not pdbId is '':
				searchTerms.append(pdbId)
		if 'org' in request.POST:
			org = request.POST['org']
			if not org is '':
				searchTerms.append(org)
	except Exception as e:
		raise #treatment

	#search Conditions
	if not pdbId is	''	and	not	org	is	'':
		try:
			pep = peptide.objects.filter(pdb_id__icontains = pdbId).filter(organism__icontains = org)
		except Exception as e:
			raise #Expetion failed to filter item

		for qr in pep:
			pepList.append(qr)
		return	render(request, 'resoults.html',{'peptides':pepList, 'searchTerms':searchTerms})

	elif not pdbId is '':
		try:
			pep = peptide.objects.filter(pdb_id__icontains = pdbId)
		except Exception as e:
			raise #failed to filter item

		for qr in pep:
			pepList.append(qr)
		return	render(request, 'resoults.html',{'peptides':pepList, 'searchTerms':searchTerms})
	else:
		try:
			pep = peptide.objects.filter(organism__icontains = org)
		except Exception as e:
			raise #failed to filter item

		for qr in pep:
			pepList.append(qr)
		return	render(request, 'resoults.html',{'peptides':pepList, 'searchTerms':searchTerms})


# Loads the Advanced Search page
def advSearch(request):
	return render(request, 'advSearch.html')

# Collects Data from the advanced search and fech the resoult.
def advSearchResoults(request):
	searchTerms=[]
	pepList = []
	pep = peptide.objects
	#data Fields
	try:
		pdb_id = request.GET['pdb_id']
		if not pdb_id is "":
			searchTerms.append({'PDB iD': pdb_id})
		pep = pep.filter(pdb_id__icontains = pdb_id)
	except:
		pass

	try:
		hfobic_area = request.GET['hfobic_area']
		if not hfobic_area is "":
			searchTerms.append({'Hidrofobic Area':hfobic_area})
		pep = pep.filter(hfobic_area__icontains = hfobic_area)
	except:
		pass

	try:
		hfobic_avg = request.GET['hfobic_avg']
		if not hfobic_avg is "":
			searchTerms.append({'Average Hidrofobicity':hfobic_avg})
		pep = pep.filter(hfobic_avg__icontains = hfobic_avg)
	except:
		pass
	try:
		charge = request.GET['charge']
		if not charge is "":
			searchTerms.append({'Charge':charge})
		pep = pep.filter(charge__icontains = charge)
	except:
		pass

	try:
		m_dipol = request.GET['m_dipol']
		if not m_dipol is "":
			searchTerms.append({'Dipolar Momentum':m_dipol})
		pep = pep.filter(m_dipol__icontains = m_dipol)
	except:
		pass

	try:
		charge_amt_atm = request.GET['charge_amt_atm']
		if not charge_amt_atm is "":
			searchTerms.append({'Charge / Amout of Atoms':charge_amt_atm})
		pep = pep.filter(charge_amt_atm__icontains = charge_amt_atm)
	except:
		pass

	try:
		m_dipol_amt_atm = request.GET['m_dipol_amt_atm']
		if not m_dipol_amt_atm is "":
			searchTerms.append({'Dipolar Momentum / amout of atoms':m_dipol_amt_atm})
		pep = pep.filter(m_dipol_amt_atm__icontains = m_dipol_amt_atm)
	except:
		pass

	try:
		sequence = request.GET['sequence']
		if not sequence is "":
			searchTerms.append({'Sequence':sequence})
		pep = pep.filter(sequence__icontains = sequence)
	except:
		pass

	try:
		organism = request.GET['organism']
		if not organism is "":
			searchTerms.append({'Organism':organism})
	except:
		pass

	#Boolean Fields
	try:
		useCheckbox = request.GET['useCheckbox']
	except:
		 useCheckbox = False
	if useCheckbox is 'on':
		try:
			hairpin = request.GET['hairpin']
			if hairpin is 'on':
				hairpin = True
			else:
				hairpin = False
			pep = pep.filter(hairpin__icontains = hairpin)
		except:
			pass
		try:
			beta_sheet = request.GET['beta_sheet']
			if beta_sheet is 'on':
				beta_sheet = True
			else:
				beta_sheet = False
			pep = pep.filter(beta_sheet__icontains = beta_sheet)
		except:
			pass

		try:
			alpha_helix = request.GET['alpha_helix']
			if alpha_helix is 'on':
				alpha_helix = True
			else:
				alpha_helix = False
			pep = pep.filter(alpha_helix__icontains = alpha_helix)
		except:
			pass

		try:
			alpha_helix_beta_sheet = request.GET['alpha_helix_beta_sheet']
			if alpha_helix_beta_sheet is 'on':
				alpha_helix_beta_sheet = True
			else:
				alpha_helix_beta_sheet = False
			pep = pep.filter(alpha_helix_beta_sheet__icontains = alpha_helix_beta_sheet)
		except:
			pass

		try:
			alpha_helix_beta_sheet_hairpin = request.GET['alpha_helix_beta_sheet_hairpin']
			if alpha_helix_beta_sheet_hairpin in 'on':
				alpha_helix_beta_sheet_hairpin = True
			else:
				alpha_helix_beta_sheet_hairpin = False
			pep = pep.filter(alpha_helix_beta_sheet_hairpin__icontains = alpha_helix_beta_sheet_hairpin)
		except:
			pass

		try:
			searchTerms.append({'Hairpin':hairpin})
			searchTerms.append({'Beta Sheet':beta_sheet})
			searchTerms.append({'Aplha Helix':alpha_helix})
			searchTerms.append({'Alpha Helix Beta Sheet':alpha_helix_beta_sheet})
			searchTerms.append({'Alpha Helix Beta Sheet Hairpin':alpha_helix_beta_sheet_hairpin})
		except Exception as e:
			raise # Failed to append Boolean Fields

		for qr in pep:
			pepList.append(qr)


	return render(request, 'resoults.html', {'peptides':pepList,'searchTerms':searchTerms})
