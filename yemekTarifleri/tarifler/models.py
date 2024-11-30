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
    malzemeler = models.TextField()
    tarif = models.TextField()
    resim = models.ImageField(upload_to='tarif_resimleri/', null=True, blank=True)
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    olusturan = models.CharField(max_length=50) # models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.baslik
    
class Yorum(models.Model):
    tarif = models.ForeignKey(Tarif, on_delete=models.CASCADE, related_name='yorumlar')
    yazar = models.ForeignKey(User, on_delete=models.CASCADE)
    icerik = models.TextField()
    olusturma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.yazar} - {self.icerik[:30]}..."

