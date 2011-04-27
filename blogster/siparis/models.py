# -*- coding: utf-8-*-
from django.db import models

class siparisForm(models.Model):
    isim = models.CharField(max_length=30, verbose_name="Ad Soyad", help_text='Max: 30 karakter')
    telefon = models.CharField(max_length=30, verbose_name="Telefon", help_text='Max: 15 karakter')
    mail = models.EmailField(help_text='Mail Adresi')
    tarih = models.DateTimeField(auto_now_add=True)
    hizmet = models.CharField(max_length=30, verbose_name="Hizmet Türü", help_text='Max: 30 karakter')
    detay = models.TextField(verbose_name="Proje Detayı")
    
    class Meta:
        verbose_name_plural = "Sipariş Formu"

