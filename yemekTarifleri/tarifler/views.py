# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarif, Malzeme
from .forms import TarifForm

def anasayfa(request):
    tarifler = Tarif.objects.all()
    return render(request, 'tarifler/anasayfa.html', {'tarifler': tarifler})  # 'anasayfa.html' dosyasını render et


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
        tarif = request.POST.get('tarif')
        secilen_malzemeler = request.POST.getlist('malzemeler')  # Multiple malzemeler
        
        # Yeni tarif oluşturuluyor
        tarif_obj = Tarif.objects.create(baslik=baslik, kategori=kategori, tarif=tarif, olusturan=request.user)
        
        # Seçilen malzemeleri tarif objesine ekliyoruz
        for malzeme_id in secilen_malzemeler:
            malzeme = Malzeme.objects.get(id=malzeme_id)  # Malzeme objesini al
            tarif_obj.malzemeler.add(malzeme)  # ManyToMany ilişkilendirmesi yapılıyor
        
        tarif_obj.save()  # Tarifi kaydediyoruz
        return redirect('tarif_listesi')

    return render(request, 'tarifler/tarif_ekle.html', {'malzemeler': malzemeler})

def tarif_detay(request, id):
    tarif = get_object_or_404(Tarif, id=id)
    return render(request, 'tarifler/tarif_detay.html', {'tarif': tarif})
