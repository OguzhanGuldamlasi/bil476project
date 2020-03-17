from django.db import models
# Create your models here.
class Urunler(models.Model):
    firma = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    urunTipi = models.CharField(max_length=200)
    urunKategorisi = models.CharField(max_length=200)
    urun = models.CharField(max_length=200)
    hileGerekcesi = models.CharField(max_length=200)
    etkenMadde = models.CharField(max_length=200)
    marka = models.CharField(max_length=200)
    partiNo= models.CharField(max_length=200)
    enlem = models.CharField(max_length=200)
    boylam = models.CharField(max_length=200)
    tarih = models.CharField(max_length=200)
