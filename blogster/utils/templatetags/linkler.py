# -*- coding: utf-8-*-
from django.template import Library, Node
from yazkicom.linkler.models import Linkler

register = Library()
def linkler_menu():
    linkler = Linkler.objects.all()
    linklermenu = ''
    for i in range(len(linkler)):
        linklermenu += ''+'<a target="_blank" href="http://'+linkler[i].sitelink+'" >'+linkler[i].siteadi+'</a><br></br>'
    return linklermenu 

register.simple_tag(linkler_menu)
