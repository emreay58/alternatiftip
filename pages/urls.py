from os import name
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('hakkimizda', views.about, name='about'),
    path('hizmetler', views.services, name='services',),
    path("hizmetler/<slug:slug>", views.service_detail, name='service_detail'),
    path('iletisim', views.contact, name='contact'),
    path('randevu', views.randevu, name='randevu'),
    path('galeri', views.galeri, name='galeri'),
] 



