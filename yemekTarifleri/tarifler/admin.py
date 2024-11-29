# Register your models here.
from django.contrib import admin
from .models import Tarif, Yorum

@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'kategori', 'olusturan', 'olusturma_tarihi')
    search_fields = ('baslik', 'kategori')

@admin.register(Yorum)
class YorumAdmin(admin.ModelAdmin):
    list_display = ('tarif', 'yazar', 'olusturma_tarihi')
    search_fields = ('tarif__baslik', 'yazar__username')

