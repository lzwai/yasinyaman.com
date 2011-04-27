# -*- coding: utf-8-*-

from django.db import models
from datetime import datetime

class Anasayfa(models.Model):
    konu = models.CharField(max_length=100, verbose_name="Konu")
    icerik = models.TextField(max_length=1000, verbose_name="İçerik")
    tarih = models.DateTimeField(verbose_name="Yayın Tarihi", default=datetime.now)
    
    
    def __unicode__(self):
        return self.konu
        return self.icerik

    class Meta:
        verbose_name_plural = "Anasayfa"
    
    
