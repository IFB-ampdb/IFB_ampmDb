from django.shortcuts import render, get_object_or_404
from .models import AMP
from .models import Non_AMP
# Create your views here.

def home(request):
    amp = AMP.objects.all()
    return render(request, 'dbquery/home.html', {'amp': amp})

def search(request):
    amp = AMP.objects.all()
    return render(request, 'dbquery/search.html', {'amp': amp})

def ampInfo(request,pk):
    amp = get_object_or_404(AMP, pk=pk)
    return render(request,'dbquery/ampinfo.html', {'amp' : amp})
