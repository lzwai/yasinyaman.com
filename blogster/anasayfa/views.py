# -*- coding: utf-8-*-

# Create your views here.
from blogster.anasayfa.models import Anasayfa
from django.shortcuts import render_to_response

def anasayfa(request):
    kayitlarana = Anasayfa.objects.all()
    return render_to_response("anasayfa.html", {'kayitlarana':kayitlarana})
    
