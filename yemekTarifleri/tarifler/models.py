# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Malzeme(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
    
class Tarif(models.Model):
    baslik = models.CharField(max_length=100)
    kategori = models.CharField(max_length=50)
    malzemeler = models.ManyToManyField(Malzeme, related_name='tarifler')  # ManyToMany veya ForeignKey ile ilişkilendirme
    tarif = models.TextField()
    resim = models.ImageField(upload_to='tarif_resimleri/', null=True, blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    olusturan = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.baslik
    
class FavoriTarif(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favori_tarifler')
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE, related_name='favori_kullanicilari')
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.tarif.baslik}"
    
class Yorum(models.Model):
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE, related_name='yorumlar')
    yazar = models.ForeignKey(User, on_delete=models.CASCADE)
    icerik = models.TextField()
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.yazar} - {self.icerik[:30]}..."

