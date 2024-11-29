# tarifler/urls.py
from django.urls import path
from .views import tarif_listesi
from . import views

urlpatterns = [
    path('', tarif_listesi, name='tarif_listesi'),
    path('tarif-filtrele/', views.tarif_filtrele, name='tarif_filtrele'),
    path('tarif-ekle/', views.tarif_ekle, name='tarif_ekle'),  # Tarif ekleme sayfası için URL
]

