# -*- coding: utf-8-*-
from blogster.blogs.models import Blogs, Yorum
from django.contrib import admin

class Blogs_Admin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("konu",)}
    list_display =('konu', 'icerik', 'yayinda', 'arsiv')

    class Media:
        js = ('/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js')

class Yorum_Admin(admin.ModelAdmin):
    list_display =('konu', 'tarih', 'isim', 'mesaj')

admin.site.register(Blogs, Blogs_Admin)
admin.site.register(Yorum, Yorum_Admin)
