from django.template import Library, Node
from django.contrib.flatpages.models import FlatPage
register = Library()

def flatpage_menu():
    pages = FlatPage.objects.all()
    menu = ''
    for i in range(len(pages)):
        menu += ''+'<a class="nav" href="'+pages[i].url+'">'+pages[i].title+'</a>'
    return menu 

register.simple_tag(flatpage_menu)

