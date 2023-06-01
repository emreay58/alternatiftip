from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('hacamat', views.hacamat, name='hacamat'),
    path('suluk-tedavisi', views.suluktedavisi, name='suluk'),
    path('prp-tedavisi', views.prptedavisi, name='prp'),
    path('ozon-terapisi', views.ozontedavisi, name='ozon'),

]
