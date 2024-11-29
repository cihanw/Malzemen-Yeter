# Create your views here.
from django.shortcuts import render, redirect
from .models import Tarif
from .forms import TarifForm

def tarif_listesi(request):
    tarifler = Tarif.objects.all()
    return render(request, 'tarifler/tarif_ekle.html', {'tarifler': tarifler})

def tarif_filtrele(request):
    arama_kelimesi = request.GET.get('malzeme', '')
    tarifler = Tarif.objects.all()

    if arama_kelimesi:
        tarifler = tarifler.filter(malzeme_detayi__icontains=arama_kelimesi)

    return render(request, 'tarifler/tarif_filtrele.html', {'tarifler': tarifler, 'arama_kelimesi': arama_kelimesi})


def tarif_ekle(request):
    if request.method == 'POST':
        form = TarifForm(request.POST, request.FILES)  # Kullanıcı dosya yüklerse FILES parametresini ekliyoruz
        if form.is_valid():
            form.save()  # Form geçerliyse kaydediyoruz
            return redirect('tarif_listesi')  # Başarılı olursa tarif listesine yönlendiriyoruz
    else:
        form = TarifForm()  # Form ilk kez açılıyorsa boş bir form döndür

    return render(request, 'tarifler/tarif_ekle.html', {'form': form})