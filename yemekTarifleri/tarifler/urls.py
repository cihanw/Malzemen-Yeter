# tarifler/urls.py
from django.urls import path
from .views import tarif_listesi
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa için index view'ını tanımlıyoruz
    path('tarifler/', views.tarif_listesi, name='tarif_listesi'),
    path('tarifler/ekle/', views.tarif_ekle, name='tarif_ekle'),
    # Diğer URL desenlerini buraya ekleyebilirsiniz
]

