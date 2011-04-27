#-*- coding: utf-8-*-
from django.template import Library, Node
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate, login
register = Library()

def uyekontrol_menu(request):
    if request.user.is_authenticated():
        uyegirdi= "Giriş yapıldı"
    else:
        uyegirdi= "Giriş yapmadı"
register.simple_tag(uyekontrol_menu)