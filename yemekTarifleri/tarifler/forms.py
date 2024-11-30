from django import forms
from .models import Tarif, Malzeme

class TarifForm(forms.ModelForm):
    malzemeler = forms.ModelMultipleChoiceField(
        queryset=Malzeme.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Tarif
        fields = ['baslik', 'kategori', 'malzemeler']
