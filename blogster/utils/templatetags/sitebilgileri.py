from django.template import Library, Node
from yazkicom.sitebilgileri.models import Sitebilgi
register = Library()

def sitebilgileri_menu():
    bilgiliste = Sitebilgi.objects.all()
    menu = ''
    for i in range(len(bilgiliste)):
        menu += ''+bilgiliste[i].siteadi+' <br/>  '+bilgiliste[i].siteaciklama+' <br/>  '+bilgiliste[i].sitelink+' <br/> '+bilgiliste[i].author+' '

    return menu 

register.simple_tag(sitebilgileri_menu)
