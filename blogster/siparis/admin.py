# -*- coding: utf-8-*-
from blogster.siparis.models import siparisForm
from django.contrib import admin

class siparisForm_Admin(admin.ModelAdmin):
    list_display = ('isim', 'tarih','mail', 'detay')
    list_filter = ['tarih']
    date_hierarchy = 'tarih'
    ordering = ('tarih',)
    search_fields = ('isim',) 
admin.site.register(siparisForm, siparisForm_Admin)


