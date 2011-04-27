# -*- coding: utf-8-*-
from blogster.portfolyo.models import Portfolyo
from django.contrib import admin

class Portfolyo_Admin(admin.ModelAdmin):
    list_display =('isadi', 'tarih')
admin.site.register(Portfolyo, Portfolyo_Admin)
