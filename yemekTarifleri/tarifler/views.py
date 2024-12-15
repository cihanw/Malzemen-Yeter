# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarif, Malzeme, FavoriTarif
from .forms import TarifForm, MalzemeFiltreleForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

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

@login_required(login_url='main_page')
def tarif_ekle(request):
    malzemeler = Malzeme.objects.all()  # Tüm malzemeleri al

    if request.method == 'POST':
        baslik = request.POST.get('baslik')
        kategori = request.POST.get('kategori')
        tarif = request.POST.get('tarif')
        secilen_malzemeler = request.POST.get('malzemeler')  # '1,2,3' şeklinde gelir

        resim = request.FILES.get('resim')
        
        # ID'leri listeye dönüştür
        secilen_malzemeler_listesi = secilen_malzemeler.split(',')  # ['1', '2', '3']

        if not baslik or not kategori or not tarif:
            messages.error(request, "Lütfen tüm alanları doldurun.")
            return redirect('tarif_ekle')

        # Yeni tarif oluşturuluyor
        tarif_obj = Tarif.objects.create(
            baslik=baslik,
            kategori=kategori,
            tarif=tarif,
            olusturan_id=request.user.id,
            resim = resim
        )

        # ManyToMany ilişkilendirme
        malzeme_objs = Malzeme.objects.filter(id__in=secilen_malzemeler_listesi)  # Liste olarak kullan
        tarif_obj.malzemeler.add(*malzeme_objs)  # Malzemeleri ManyToMany ilişkisine ekle

        tarif_obj.save()  # Tarifi kaydet
        messages.success(request, "Tarif başarıyla kaydedildi!")
        return redirect('recipes')  # Başarılı yönlendirme

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

    return render(request, 'recipes.html', {'form': form, 'tarifler': tarifler})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        # Şifre eşleşme kontrolü
        if password != confirm_password:
            messages.error(request, "Şifreler eşleşmiyor.")
            return redirect('register')

        # Kullanıcı adı kontrolü
        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu kullanıcı adı zaten alınmış.")
            return redirect('register')

        # E-posta kontrolü
        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu e-posta adresi zaten kullanılıyor.")
            return redirect('register')

        # Yeni kullanıcı oluştur ve kaydet
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Başarılı olduğunda giriş sayfasına yönlendir
        messages.success(request, "Hesabınız başarıyla oluşturuldu. Giriş yapabilirsiniz.")
        return redirect('login')

    return render(request, 'register.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Giriş başarılı!")
            return redirect('main_page')  # Ana sayfaya yönlendirme
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı.")

    return render(request, 'login.html')


@login_required
def favori_ekle(request, tarif_id):
    try:
        tarif = Tarif.objects.get(id=tarif_id)
        # Kullanıcının favori tariflerini kontrol et
        if not FavoriTarif.objects.filter(user=request.user, tarif=tarif).exists():
            # Favoriye ekle
            FavoriTarif.objects.create(user=request.user, tarif=tarif)
            messages.success(request, f"{tarif.baslik} favorilerinize eklendi!")
        else:
            messages.info(request, f"{tarif.baslik} zaten favorilerinizde.")
    except Tarif.DoesNotExist:
        messages.error(request, "Tarif bulunamadı.")
    
    return redirect('recipes')  # Favoriye ekleme işlemi sonrası tarifler sayfasına dön

@login_required
def favori_cikar(request, tarif_id):
    try:
        tarif = Tarif.objects.get(id=tarif_id)
        # Kullanıcının favorilerinden çıkar
        favori_tarif = FavoriTarif.objects.filter(user=request.user, tarif=tarif).first()
        if favori_tarif:
            favori_tarif.delete()
            messages.success(request, f"{tarif.baslik} favorilerinizden çıkarıldı.")
        else:
            messages.info(request, f"{tarif.baslik} favorilerinizde değil.")
    except Tarif.DoesNotExist:
        messages.error(request, "Tarif bulunamadı.")
    
    return redirect('your_profile')  # Favoriden çıkarma işlemi sonrası tarifler sayfasına dön

@login_required
def favoriler(request):
    # Kullanıcının favori tariflerini al
    favori_tarifler = FavoriTarif.objects.filter(user=request.user).select_related('tarif')

    # favori_tarifler queryset'ini tarif objelerine dönüştür
    tarif_listesi = [favori.tarif for favori in favori_tarifler]

    return render(request, 'your_profile.html', {'favori_tarifler': tarif_listesi})
