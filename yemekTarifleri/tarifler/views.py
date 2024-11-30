# Create your views here.
from django.shortcuts import render, redirect
from .models import Tarif, Malzeme
from .forms import TarifForm

def index(request):
    return render(request, 'tarifler/index.html')  # 'index.html' dosyasını render et


def tarif_listesi(request):
    arama_kelimesi = request.GET.get('arama', '')
    malzeme_ids = request.GET.getlist('malzemeler')

    tarifler = Tarif.objects.all()
    if arama_kelimesi:
        tarifler = tarifler.filter(baslik__icontains=arama_kelimesi)

    if malzeme_ids:
        tarifler = tarifler.filter(malzemeler__id__in=malzeme_ids).distinct()

    malzemeler = Malzeme.objects.all()
    return render(request, 'tarifler/tarif_listesi.html', {
        'tarifler': tarifler,
        'malzemeler': malzemeler,
        'arama_kelimesi': arama_kelimesi,
        'secili_malzemeler': malzeme_ids
    })


def tarif_ekle(request):
    malzemeler = Malzeme.objects.all()
    if request.method == 'POST':
        baslik = request.POST.get('baslik')
        kategori = request.POST.get('kategori')
        secilen_malzemeler = request.POST.getlist('malzemeler')

        tarif = Tarif.objects.create(baslik=baslik, kategori=kategori, olusturan=request.user)
        tarif.malzemeler.set(secilen_malzemeler)
        return redirect('tarif_listesi')

    return render(request, 'tarifler/tarif_ekle.html', {'malzemeler': malzemeler})