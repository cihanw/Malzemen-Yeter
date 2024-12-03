# tarifler/urls.py
from django.urls import path
from .views import tarif_listesi
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('tarifler/', views.tarif_listesi, name='tarif_listesi'),
    path('tarif-ekle/', views.tarif_ekle, name='tarif_ekle'),
    path('tarif/<int:id>/', views.tarif_detay, name='tarif_detay'),
]

