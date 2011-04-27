# -*- coding: utf-8-*-
from blogster.anasayfa.models import Anasayfa
from django.contrib import admin

class Anasayfa_Admin(admin.ModelAdmin):
    list_display =('konu', 'icerik')
    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js')

admin.site.register(Anasayfa, Anasayfa_Admin)

