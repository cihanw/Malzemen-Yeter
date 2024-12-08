# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarif, Malzeme
from .forms import TarifForm, MalzemeFiltreleForm
from django.http import JsonResponse

def main_page(request):
    tarifler = Tarif.objects.all()
    return render(request, 'main_page.html', {'tarifler': tarifler})

def recipes(request):
    return render(request, 'recipes.html')

def your_profile(request):
    return render(request, 'your_profile.html')

def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about_us.html')  # Google'a yönlendirme

def tarif_arama(request):
    search_query = request.GET.get('search_query', '')  # Formdan gelen arama kelimesi

    if search_query:
        # Tarifleri başlığa göre filtrele (case-insensitive)
        tarifler = Tarif.objects.filter(baslik__icontains=search_query)
    else:
        # Arama yapılmadıysa, tüm tarifleri getir
        tarifler = Tarif.objects.all()
    # Arama kelimesini ve filtrelenmiş tarifleri template'e gönder
    return render(request, 'recipes.html', {'tarifler': tarifler, 'search_query': search_query})

def tarif_ekle(request):
    malzemeler = Malzeme.objects.all()
    
    if request.method == 'POST':
        baslik = request.POST.get('baslik')
        kategori = request.POST.get('kategori')
        tarif = request.POST.get('tarif')
        secilen_malzemeler = request.POST.getlist('malzemeler')  # Multiple malzemeler
        
        # Yeni tarif oluşturuluyor
        tarif_obj = Tarif.objects.create(baslik=baslik, kategori=kategori, tarif=tarif, olusturan_id=request.user)
        
        # Seçilen malzemeleri tarif objesine ekliyoruz
        for malzeme_id in secilen_malzemeler:
            malzeme = Malzeme.objects.get(id=malzeme_id)  # Malzeme objesini al
            tarif_obj.malzemeler.add(malzeme)  # ManyToMany ilişkilendirmesi yapılıyor
        
        tarif_obj.save()  # Tarifi kaydediyoruz
        return redirect('recipes')

    return render(request, 'tarif_ekle.html', {'malzemeler': malzemeler})

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

def tarif_detay(request, id):
    tarif = get_object_or_404(Tarif, id=id)
    return render(request, 'tarif_detay.html', {'tarif': tarif})

"""
def deneme_filtre(request):
    return render(request, 'deneme_filtre.html')
"""
    
from django.shortcuts import render
from .models import Tarif, Malzeme

"""
def tarif_arama_deneme(request):
    malzeme_query = request.GET.get('malzeme', '')  # Kullanıcının girdiği malzeme

    if malzeme_query:
         # Kullanıcıdan gelen malzemeleri virgülle ayırarak listeye çevir
        malzeme_isimleri = malzeme_query.split(' ')

        # Listeyi temizlemek (boşlukları silmek ve küçük harfe dönüştürmek)
        malzeme_isimleri = [isim.strip().lower() for isim in malzeme_isimleri]

        # Veritabanında eşleşen malzemeleri bul
        malzemeler = Malzeme.objects.filter(isim__in=malzeme_isimleri)
        if malzemeler:
            # İlgili malzeme ile ilişkili tarifleri bul
            tarifler = Tarif.objects.filter(malzemeler__in=malzemeler).distinct()
        else:
            tarifler = []  # Eğer malzeme bulunmazsa boş liste döner
    else:
        # Eğer malzeme girişi yoksa tüm tarifleri getir
        tarifler = Tarif.objects.all()

    return render(request, 'deneme_filtre.html', {'tarifler': tarifler, 'malzeme_query': malzeme_query})
"""

def tarif_arama_deneme(request):
    form = MalzemeFiltreleForm(request.GET)
    tarifler = Tarif.objects.all()

    if form.is_valid():
        # Kullanıcının seçtiği malzemelerin ID'lerini al
        selected_malzeme_ids = form.cleaned_data['malzemeler']
        selected_malzemeler = set(Malzeme.objects.filter(id__in=selected_malzeme_ids))

        # Alt küme kontrolü için sonuçları filtrele
        filtered_tarifler = []
        for tarif in tarifler:
            tarif_malzemeler = set(tarif.malzemeler.all())
            if tarif_malzemeler.issubset(selected_malzemeler):
                filtered_tarifler.append(tarif)

        # Filtrelenmiş tarifleri döndür
        tarifler = filtered_tarifler

    return render(request, 'deneme_filtre.html', {'form': form, 'tarifler': tarifler})

