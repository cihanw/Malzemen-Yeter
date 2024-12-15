# tarifler/urls.py
from django.urls import path
from .views import tarif_listesi
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.main_page, name='main_page'),  # Ana sayfa

    path('sign-up/', views.register, name='register'),  # Sign Up
    path('sign-in/', LoginView.as_view(template_name='registration/login.html'), name='login'),
     path('sign-out/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

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

    path('favori-ekle/<int:tarif_id>/', views.favori_ekle, name='favori_ekle'),
    path('favori-cikar/<int:tarif_id>/', views.favori_cikar, name='favori_cikar'),
    path('favoriler', views.favoriler, name='favoriler'),

    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

