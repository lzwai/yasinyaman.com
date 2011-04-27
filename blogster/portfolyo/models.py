# -*- coding: utf-8-*-

from django.db import models
from datetime import datetime

class Portfolyo(models.Model):
    isadi = models.CharField(max_length=100, verbose_name="İşin Adı")
    tarih = models.DateTimeField(verbose_name="Yayın Tarihi")
    durum = models.CharField(max_length=100, verbose_name="Durum")
    araclar = models.CharField(max_length=100, verbose_name="Kulanılan Araçlar")
    tamhali = models.CharField(max_length=100, verbose_name="Sitenin Tam linki")
    yapan = models.CharField(max_length=100, verbose_name="Yapan")
    kucukresim = models.CharField(max_length=100, verbose_name="K. Resim")
    buyukresim = models.CharField(max_length=100, verbose_name="B. Resim")

    
    def __unicode__(self):
        return self.isadi
        return self.tarih
        return self.durum
        return self.yapan
        
    class Meta:
        verbose_name_plural = "Portofolyo"
   
