# tarifler/urls.py
from django.urls import path
from .views import tarif_listesi
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),  # Ana sayfa

    path('sign-up/', views.register, name='register'),  # Sign Up
    path('sign-in/', views.login, name='login'),  # Sign In

    path('recipes/', views.recipes, name='recipes'),  # Recipes bağlantısı
    path('contact/', views.contact, name='contact'),  # Contact bağlantısı
    path('about-us/', views.about_us, name='about_us'),  # About Us bağlantısı
    path('profile/', views.your_profile, name='your_profile'),  # Your Profile bağlantısı
    #path('search-recipes/', views.search_recipes, name='search_recipes'),
    path('arama/', views.tarif_arama, name='tarif_arama'),

    #path('tarifler/', views.tarif_listesi, name='tarif_listesi'),
    path('tarif-ekle/', views.tarif_ekle, name='tarif_ekle'),
    path('tarif/<int:id>/', views.tarif_detay, name='tarif_detay'),

    #path('deneme_filtre/', views.deneme_filtre, name='deneme_filtre'),
    path('tarif_arama_deneme/', views.tarif_arama_deneme, name='tarif_arama_deneme'),
    
]

