from django.shortcuts import render
from .models import Hacamat, OzonTedavisi, PrpTedavisi, SulukTedavisi
from pages.models import ServicesField

# Create your views here.

def hacamat(request):
    hacamat = Hacamat.objects.all()
    services = ServicesField.objects.all()
    context = {
        'hacamat' : hacamat,
        'services' : services
    }
    return render(request, 'services/hacamat.html', context)

def suluktedavisi(request):
    suluk = SulukTedavisi.objects.all()
    services = ServicesField.objects.all()
    context = {
        'suluk' : suluk,
        'services' : services
    }
    return render(request, 'services/suluk.html', context)
   

def prptedavisi(request):
    prp = PrpTedavisi.objects.all()
    services = ServicesField.objects.all()
    context = {
        'prp' : prp,
        'services' : services
    }
    return render(request, 'services/prp.html', context)
  
def ozontedavisi(request):
    ozon = OzonTedavisi.objects.all()
    services = ServicesField.objects.all()
    context = {
        'ozon' : ozon,
        'services' : services
    }
    return render(request, 'services/ozon.html', context)
