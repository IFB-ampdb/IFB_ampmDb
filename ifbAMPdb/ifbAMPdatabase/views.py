from django.shortcuts import render, get_object_or_404
from .models import peptide
from blog.views import homeBlog

# Create your views here.

def home(request):
    reqHomeData = homeData()
    reqHomeBlog = homeBlog()
    return render(request, 'home.html',  reqHomeData, reqHomeBlog)

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
