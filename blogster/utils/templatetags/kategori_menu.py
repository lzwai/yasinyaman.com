# -*- coding: utf-8-*-
from django.template import Library, Node
from yazkicom.kategori.models import Kategori
register = Library()

def kategori_menu():
    kategorilistesi = Kategori.objects.all().order_by('kategoriadi')
    menu = ''
    for i in range(len(kategorilistesi)):
        menu += ''+'<li><a href="/kategori/'+kategorilistesi[i].slug+'" title="'+kategorilistesi[i].kategoriadi+'">'+kategorilistesi[i].kategoriadi+'</a></li>'

    return menu 

register.simple_tag(kategori_menu)
