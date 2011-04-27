from django.template import Library, Node
from yazkicom.sitebilgileri.models import Sitebilgi
register = Library()

def siteiletisimbilgileri_menu():
    iletisimbilgiliste = Sitebilgi.objects.all()
    menu = ''
    for i in range(len(iletisimbilgiliste)):
        menu += ''+iletisimbilgiliste[i].siteadi+'<br><br>'+'Tel: <font color="red">'+iletisimbilgiliste[i].telefon+'</font><br>Fax: '+iletisimbilgiliste[i].fax+'<br>Cep: '+iletisimbilgiliste[i].cep+''+'<br>Adres: '+iletisimbilgiliste[i].adres+''

    return menu 

register.simple_tag(siteiletisimbilgileri_menu)
