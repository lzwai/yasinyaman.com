# -*- coding: utf-8-*-
from blogster.iletisim.models import iletisimForm

from django.contrib import admin

class iletisimForm_Admin(admin.ModelAdmin):
    list_display = ('isim', 'tarih','mail', 'mesaj')
    list_filter = ['tarih']
    date_hierarchy = 'tarih'
    ordering = ('tarih',)
    search_fields = ('isim',) 

admin.site.register(iletisimForm, iletisimForm_Admin)



