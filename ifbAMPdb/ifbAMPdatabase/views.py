from django.shortcuts import render, get_object_or_404
from .models import peptide
# Create your views here.

def home(request):
    pep = peptide.objects.order_by(pk)[:2]
    return render(request, 'home.html', {'peptide': pep})

def search(request):
    pep = peptide.objects.all()
    return render(request, 'search.html', {'peptide': pep})

def ampInfo(request,pk):
    pep = get_object_or_404(peptide, pk=pk)
    return render(request,'ampinfo.html', {'peptide' : pep})
