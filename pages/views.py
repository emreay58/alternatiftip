
from multiprocessing import context
import re
from unicodedata import category, name
from django.shortcuts import render
from .models import MessageModel, RandevuModel, ServicesField, PicturesModel

# Create your views here.

def index(request):
    services = ServicesField.objects.all()
    resim = PicturesModel.objects.all()
    context = {
        'services' : services,
        'resim' : resim
  
    }
    return render(request, 'pages/index.html', context)

def about(request):
     services = ServicesField.objects.all()
     context = {
            'services' : services
               }
     return render(request, 'pages/about.html', context)

def services(request):
    services = ServicesField.objects.all()

    context = {
        'services' : services
    }
    return render(request, 'pages/services.html', context)

def contact(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        konu = request.POST["konu"]
        message = request.POST["message"]

        mesaj = MessageModel(name=username, email=email, konu=konu, message=message)
        mesaj.save()
        return render(request, 'pages/contact.html', {'mesaj' : 'Mesajınızı Aldık. Sizinle iletişime geçeceğiz.'})

    services = ServicesField.objects.all()
    context = {
        'services' : services
    }
    return render(request, 'pages/contact.html',context)

def randevu(request):
    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        bolum = request.POST["bolum"]
        tarih = request.POST["tarih"]
        mesage = request.POST["message"]

        randevu = RandevuModel(name=username, email=email, tarih=tarih, phone=phone, bolum=bolum, mesage=mesage)
        randevu.save()
        return render(request, 'pages/randevu.html', {'randevu' : 'Randevunuz başarılı bir şekilde oluşturuldu. Sizinle irtibata geçeceğiz.'},)
    
    return render(request, 'pages/randevu.html')


def service_detail(request, slug):
    service = ServicesField.objects.get(slug=slug)
    services = ServicesField.objects.all()

    context = {
        'service' : service,
        'services' : services
    }

    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        bolum = request.POST["bolum"]
        tarih = request.POST["tarih"]
        mesage = request.POST["message"]

        randevu = RandevuModel(name=username, email=email, tarih=tarih, phone=phone, bolum=bolum, mesage=mesage)
        randevu.save()
        return render(request, 'pages/randevu.html', {'randevu' : 'Randevunuz başarılı bir şekilde oluşturuldu. Sizinle irtibata geçeceğiz.'},)

    return render(request, 'pages/service_detail.html',context)


def galeri(request):
    resim = PicturesModel.objects.all()
    return render(request, 'pages/galeri.html', {'resim': resim})

