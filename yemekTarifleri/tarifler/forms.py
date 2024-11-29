# forms.py
from django import forms
from .models import Tarif

class TarifForm(forms.ModelForm):
    class Meta:
        model = Tarif
        fields = ['baslik', 'kategori', 'malzemeler', 'yapilis', 'resim', 'olusturan']  # Hangi alanlar formda görünsün
