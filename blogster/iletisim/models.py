# -*- coding: utf-8-*-
from django.db import models

class iletisimForm(models.Model):
	isim = models.CharField(max_length=30, verbose_name="Ad Soyad", help_text='Max: 30 karakter')
	mail = models.EmailField(help_text='Mail Adresi')
	tarih = models.DateTimeField(auto_now_add=True)
	konu = models.CharField(max_length=30, verbose_name="Konu", help_text='Max: 30 karakter')
	mesaj = models.TextField(verbose_name = "Mesaj")
	
	class Meta:
		verbose_name_plural = "İletişim Formu"
		


