# -*- coding: utf-8-*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Blogs(models.Model):
    konu = models.CharField(max_length=100, verbose_name="Konu")
    slug = models.SlugField(max_length=300, help_text='Max: 300 Karakter')
    user = models.ForeignKey(User,verbose_name="Ekleyen")
    icerikozet = models.TextField(max_length=250, verbose_name="İçerik Özeti")
    icerik = models.TextField(max_length=1000, verbose_name="İçerik")
    tarih = models.DateTimeField(verbose_name="Yayın Tarihi", default=datetime.now)
    yayinda = models.BooleanField(verbose_name="Yayınla")
    arsiv = models.BooleanField(verbose_name="Arşivle")
    
   
    def __unicode__(self):
        return self.konu
        return self.icerik
        return self.icerikozet

    class Meta:
        verbose_name_plural = "Blog"


class Yorum(models.Model):
    konu = models.ForeignKey(Blogs)
    isim = models.CharField(max_length=100, verbose_name="İsim")
    email = models.CharField(max_length=100, verbose_name="E Mail")
    mesaj = models.TextField(max_length=500, verbose_name="İçerik")
    ip = models.TextField(max_length=20)
    smd5 = models.TextField(max_length=500)
    tarih = models.DateTimeField(auto_now_add=True)
    
    
   
    def __unicode__(self):
        return self.mesaj


    class Meta:
        verbose_name_plural = "Yorum"


    
    


