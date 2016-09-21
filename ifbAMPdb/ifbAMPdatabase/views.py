from django.shortcuts import render, get_object_or_404
from .models import peptide
# Create your views here.

def home(request):
    amp = peptide.objects.all()
    return render(request, 'home.html', {'peptide': peptide})

def search(request):
    amp = peptide.objects.all()
    return render(request, 'search.html', {'peptide': peptide})

def ampInfo(request,pk):
    amp = get_object_or_404(peptide, pk=pk)
    return render(request,'ampinfo.html', {'peptide' : peptide})
