# -*- coding: utf-8-*-
from django.template import Library, Node
from yazkicom.dersler.models import derslerlar

register = Library()

def vitrin_menu():
    vitrinlistesi = derslerlar.objects.all()
    vitrinmenu = ''
    for i in range(len(vitrinlistesi)):
        if vitrinlistesi[i].vitrineekle:
            vitrinmenu += '<li>'+vitrinlistesi[i].ilanadi+'</li>'

    return vitrinmenu 

register.simple_tag(vitrin_menu)
