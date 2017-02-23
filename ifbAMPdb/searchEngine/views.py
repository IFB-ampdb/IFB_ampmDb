from django.shortcuts import render, get_object_or_404, render_to_response
from searchEngine.models import peptide

# Create your views here.

def homeData():
        pep = peptide.objects.order_by()[:2]
        return {'peptides': pep}

def detail(request,pk):
	pep = get_object_or_404(peptide, pdb_id = pk)
	return render(request,'searchEngine/detail.html', {'peptide' : pep})

#collects data from the Basic search in the Home Page and displays in the Result page.
def ampBasicSearch(request):
        searchTerms=[]
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
                organism = request.GET['organism']
                if not organism is "":
                        searchTerms.append({'Organism':organism})
                        pep = pep.filter(organism = organism)
        except:
                pass

        return render(request, 'searchEngine/results.html', {'peptides':pep,'searchTerms':searchTerms})

# Loads the Advanced Search page
def advSearch(request):
        return render(request, 'searchEngine/advSearch.html')

# Collects Data from the advanced search and fetch the result.
def advSearchResults(request):
        searchTerms=[]
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
                        pep = pep.filter(charge = charge)
        except:
                pass

        try:
                m_dipol = request.GET['m_dipol']
                if not m_dipol is "":
                        searchTerms.append({'Dipolar Momentum':m_dipol})
                        pep = pep.filter(m_dipol = m_dipol)
        except:
                pass

        try:
                charge_amt_atm = request.GET['charge_amt_atm']
                if not charge_amt_atm is "":
                        searchTerms.append({'Charge / Amout of Atoms':charge_amt_atm})
                        pep = pep.filter(charge_amt_atm = charge_amt_atm)
        except:
                pass

        try:
                m_dipol_amt_atm = request.GET['m_dipol_amt_atm']
                if not m_dipol_amt_atm is "":
                        searchTerms.append({'Dipolar Momentum / amout of atoms':m_dipol_amt_atm})
                        pep = pep.filter(m_dipol_amt_atm = m_dipol_amt_atm)
        except:
                pass

        try:
                sequence = request.GET['sequence']
                if not sequence is "":
                        searchTerms.append({'Sequence':sequence})
                        pep = pep.filter(sequence = sequence)
        except:
                pass

        try:
                organism = request.GET['organism']
                if not organism is "":
                        searchTerms.append({'Organism':organism})
                        pep = pep.filter(organism = organism)
        except:
                pass

        #Boolean Fields
        try:
                useCheckbox = request.GET['useCheckbox']
        except:
                 useCheckbox = False
        if useCheckbox == 'on':
                try:
                        hairpin = request.GET['hairpin']
                        if hairpin == 'on':
                                hairpin = True
                        else:
                                hairpin = False
                        pep = pep.filter(hairpin = hairpin)
                        searchTerms.append({'Hairpin':hairpin})
                except:
                        pass
                try:
                        beta_sheet = request.GET['beta_sheet']
                        if beta_sheet == 'on':
                                beta_sheet = True
                        else:
                                beta_sheet = False
                        pep = pep.filter(beta_sheet = beta_sheet)
                        searchTerms.append({'Beta Sheet':beta_sheet})
                except:
                        pass

                try:
                        alpha_helix = request.GET['alpha_helix']
                        if alpha_helix == 'on':
                                alpha_helix = True
                        else:
                                alpha_helix = False
                        pep = pep.filter(alpha_helix = alpha_helix)
                        searchTerms.append({'Aplha Helix':alpha_helix})
                except:
                        pass

                try:
                        alpha_helix_beta_sheet = request.GET['alpha_helix_beta_sheet']
                        if alpha_helix_beta_sheet == 'on':
                                alpha_helix_beta_sheet = True
                        else:
                                alpha_helix_beta_sheet = False
                        pep = pep.filter(alpha_helix_beta_sheet = alpha_helix_beta_sheet)
                        searchTerms.append({'Alpha Helix Beta Sheet':alpha_helix_beta_sheet})
                except:
                        pass


                try:
                        alpha_helix_beta_sheet_hairpin = request.GET['alpha_helix_beta_sheet_hairpin']
                        if alpha_helix_beta_sheet_hairpin == 'on':
                                alpha_helix_beta_sheet_hairpin = True
                        else:
                                alpha_helix_beta_sheet_hairpin = False
                        pep = pep.filter(alpha_helix_beta_sheet_hairpin = alpha_helix_beta_sheet_hairpin)
                        searchTerms.append({'Alpha Helix Beta Sheet Hairpin':alpha_helix_beta_sheet_hairpin})
                except:
                        pass

        return render(request, 'searchEngine/results.html', {'peptides':pep,'searchTerms':searchTerms})
